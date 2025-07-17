package ro.ciacob.desktop.ui {
	import flash.display.DisplayObject;
	import flash.display.DisplayObjectContainer;
	import flash.events.Event;
	import flash.events.IEventDispatcher;
	import flash.utils.getDefinitionByName;
	
	import mx.binding.utils.BindingUtils;
	import mx.binding.utils.ChangeWatcher;
	import mx.collections.ArrayCollection;
	import mx.controls.Spacer;
	import mx.core.ClassFactory;
	import mx.core.IVisualElement;
	import mx.core.IVisualElementContainer;
	import mx.events.FlexEvent;
	import mx.utils.ObjectUtil;
	
	import spark.components.CheckBox;
	import spark.components.ComboBox;
	import spark.components.HSlider;
	import spark.components.Label;
	import spark.components.List;
	import spark.components.NumericStepper;
	import spark.components.TextInput;
	
	import ro.ciacob.desktop.ui.utils.CommonStrings;
	import ro.ciacob.desktop.ui.utils.Objects;
	import ro.ciacob.desktop.ui.utils.Strings;
	
	/**
	 * @see ro.ciacob.desktop.ui.IUiBuilder
	 */
	public class UiFlexBuilder implements IUiBuilder {
		
		// Configurable settings
		private static const _listLabelField : String = 'label';
		private static const _comboPrompt : String = 'Select or type to search';
		private static const _defaultDataproviderName : String = 'dataProvider';
		
		protected static function get LIST_LABEL_FIELD () : String {
			return _listLabelField;
		}
		
		protected static function get COMBO_PROMPT () : String {
			return _comboPrompt;
		}
		
		protected static function get DEFAULT_DATAPROVIDER_NAME () : String {
			return _defaultDataproviderName;
		}
		
		// Helpers
		private static const NO_MATCHES : Vector.<int> = new Vector.<int>;
		private static const LABEL_SUFFIX : String = 'Label';
		private static const TRUE : String = 'true';
		private static const FALSE : String = 'false';
		private static const RESERVED_KEYS : Array = [
			BlueprintKeys.CUSTOM_COMPONENT,
			BlueprintKeys.CLASS_FQN,
			BlueprintKeys.HIDE_LABEL,
			BlueprintKeys.DATAPROVIDER_NAME,
			BlueprintKeys.BINDING_SOURCE,
			BlueprintKeys.BINDING_TARGET,
			BlueprintKeys.CHANGE_EVENT_NAME
		];
		
		// Component fields
		private static const SELECTED : String = 'selected';
		private static const NAME : String = 'name';
		private static const VALUE : String = 'value';
		private static const DATA_PROVIDER : String = 'dataProvider'; 
		private static const SELECTED_ITEM : String = 'selectedItem';
		private static const SELECTED_ITEMS : String = 'selectedItems';
		private static const TEXT : String = 'text';

		
		private var _container : DisplayObjectContainer;
		private var _originator : Object;
		private var _componentGeneratedCallback : Function;
		private var _componentChangedCallback : Function;
		
		private var _baseProps : Object = {};
		private var _uiBindingsMap:Object = {};
		private var _spacerFactory : ClassFactory = new ClassFactory(Spacer);
		private var _labelFactory : ClassFactory = new ClassFactory(Label);
		private var _textInputFactory : ClassFactory = new ClassFactory(TextInput);
		private var _checkBoxFactory : ClassFactory = new ClassFactory(CheckBox);
		private var _numericStepperFactory : ClassFactory = new ClassFactory(NumericStepper);
		private var _sliderFactory : ClassFactory = new ClassFactory(HSlider);
		private var _comboBoxFactory : ClassFactory = new ClassFactory(ComboBox);
		private var _listFactory : ClassFactory = new ClassFactory(List);
		
		/**
		 * @constructor
		 * @see ro.ciacob.desktop.ui.IUiBuilder
		 * 
		 * @param	originator
		 * 			A reference to the originating class instance (the class whose public accessors are to rendered as UI components).
		 * 			An instance of a simple Object or an `Object` subclass is also accepted.
		 * 			@see IUiBuilder.get.originator
		 * 
		 * @param	container
		 * 			A reference to the visual container where UI components are to be dynamically created.
		 * 			@see IUiBuilder.get.container
		 * 
		 * @param	onComponentGenerated
		 * 			A reference to a function that is to be called as soon as a UI component has been generated; this acts as a signal
		 * 			that the next blueprint in the queue can be addressed.
		 * 			@see IUiBuilder.get.componentGeneratedCallback
		 * 
		 * @param	onComponentChanged
		 * 			A reference to a function that is to be called each time user changes a value in one of the generated UI Components.
		 * 			The expected function signature is:
		 * 
		 * 			myFunction (key : String, value : Object);
		 * 
		 * 			@see IUiBuilder.get.componentChangedCallback
		 */
		public function UiFlexBuilder (originator : Object, container : DisplayObjectContainer, onComponentGenerated : Function, onComponentChanged : Function) {
			_originator = originator;
			_container = container;
			_componentGeneratedCallback = onComponentGenerated;
			_componentChangedCallback = onComponentChanged;
		}
		
		/**
		 * Reference to the visual container where UI components are to be dynamically created. 
		 */
		public function get container () : DisplayObjectContainer {
			return 	_container;
		}
		
		/**
		 * Reference to a function that is to be called each time user changes a value in one
		 * of the generated UI Components.
		 */
		public function get componentChangedCallback () : Function {
			return _componentChangedCallback;
		}
		
		/**
		 * Reference to a function that is to be called as soon as a UI component has been 
		 * generated; this acts as a signal that the next blueprint in the queue can be addressed.
		 */		
		public function get componentGeneratedCallback () : Function {
			return	_componentGeneratedCallback;
		}
		
		/**
		 * Reference to the originating class (the class whose public accessors are to rendered as 
		 * UI components). An instance of a simple Object or an `Object` subclass is also accepted.
		 */
		public function get originator () : Object {
			return _originator;
		}
		

		
		/**
		 * Actually creates and returns an UI Component. Executed in turn for each item in the queue.
		 * Can return `null` in case a Component cannot be built out of the current blueprint.
		 */
		public function buildUiElement (blueprint : Object) : DisplayObject {
			
			// Base property set, shared by all generated components. Must only include properties that
			// are common to all supported components. Custom components will NOT use it.
			// Example:
			// baseProps.x = 10;
			_baseProps = {};
			
			// Create the UI component
			var component : DisplayObject = null;
			
			// Custom components, if any required, take precedence over standard components.
			if (BlueprintKeys.CUSTOM_COMPONENT in blueprint) {
 				component = _buildCustomComponent (_container, blueprint);
			} else {
				var type : String = (blueprint[BlueprintKeys.TYPE] as String);
				
				// Add a label unless the component is a CheckBox
				if (type != SupportedTypes.BOOLEAN) {
					_buildSpacer (_container);
					_buildLabel (_container, blueprint);
				}
				
				switch (type) {
					
					// Create a TextInput for a String accessor
					case SupportedTypes.STRING:
						component = _buildTextInput (_container, blueprint);
						break;
					
					// Create a CheckBox for a Boolean accessor
					case SupportedTypes.BOOLEAN:
						component = _buildCheckBox (_container, blueprint);
						break;
					
					// Create a NumericStepper or a Slider for an int or Number accessor
					case SupportedTypes.INT:
					case SupportedTypes.UINT:
					case SupportedTypes.NUMBER:
						component = _buildNumericComponent (_container, blueprint);
						break;
					
					// Create a ComboBox for a pair of similarly named Object/Array accessors
					case SupportedTypes.OBJECT:
						component = _buildComboBoxComponent (_container, blueprint);
						break;
					
					// Create a List for a pair of similarly named Array accessors
					case SupportedTypes.ARRAY:
						component = _buildListComponent (_container, blueprint);
						break;
				}
			}

			if (component != null) {
				component.addEventListener(FlexEvent.UPDATE_COMPLETE, _onGeneratedControlRendered);
			}
			return component;
		}
		
		/**
		 * Cleans up the current container, preparing it for either recycling or decommissioning.
		 * Also releases event listeners and watchers involved with the generated components.
		 * Called by the generator that uses this builder before each generating session.
		 */
		public function purgeContainer () : void {
			
			// Release components' events and watchers 
			var key : String;
			var bindingData : Object;
			var dispatcher : IEventDispatcher;
			var eventName : String;
			var listener : Function;
			var watcher : ChangeWatcher;
			for (key in _uiBindingsMap) {
				bindingData = _uiBindingsMap[key] as Object;
				dispatcher = bindingData[BlueprintKeys.BOUND_COMPONENT] as IEventDispatcher;
				eventName = bindingData[BlueprintKeys.BOUND_EVENT] as String;
				listener = bindingData[BlueprintKeys.BOUND_FUNCTION] as Function;
				dispatcher.removeEventListener(eventName, listener);
				watcher = bindingData[BlueprintKeys.BOUND_CHANGE_WATCHER] as ChangeWatcher;
				if (watcher) {
					watcher.unwatch();
				}
			}
			
			// Clear internal state
			_uiBindingsMap = {};
			
			// Remove generated components
			IVisualElementContainer (_container).removeAllElements();
		}
		
		/**
		 * Creates a spacer worth one row or column, depending on the layout defined on the container.
		 */
		private function _buildSpacer (container : DisplayObjectContainer) : DisplayObject {
			// Collect properties
			var spacerProps : Object = ObjectUtil.clone (_baseProps);
			delete spacerProps.uid;
			
			// Create the spacer
			_spacerFactory.properties = spacerProps;
			var component : DisplayObject = _spacerFactory.newInstance() as DisplayObject;
			IVisualElementContainer (container).addElement (IVisualElement(component));
			
			// Return created spacer
			return component;
		}
		
		/**
		 * Creates a label UI Component
		 */
		private function _buildLabel (container : DisplayObjectContainer, blueprint : Object) : DisplayObject {
			var name : String = (blueprint[BlueprintKeys.NAME] as String);
			var label : String = (blueprint[BlueprintKeys.LABEL] as String);
			var description : String = Strings.trim(blueprint[BlueprintKeys.DESCRIPTION] as String);
			
			// Collect properties
			var labelProps : Object = ObjectUtil.clone (_baseProps);
			delete labelProps.uid;
			labelProps.name = name + LABEL_SUFFIX;
			labelProps.text = label.concat (CommonStrings.COLON_SPACE);
			if (!Strings.isEmpty (description)) {
				labelProps.toolTip = description;
			}
			
			// Create the label
			_labelFactory.properties = labelProps;
			var component : DisplayObject = _labelFactory.newInstance() as DisplayObject;
			IVisualElementContainer (container).addElement (IVisualElement(component));
			
			// Return created label
			return component;
		}
		
		/**
		 * Creates a TextInput UI Component.
		 */
		private function _buildTextInput (container : DisplayObjectContainer, blueprint : Object) : DisplayObject {
			var name : String = (blueprint[BlueprintKeys.NAME] as String);
			var label : String = (blueprint[BlueprintKeys.LABEL] as String);
			var description : String = Strings.trim(blueprint[BlueprintKeys.DESCRIPTION] as String);
			
			// Collect properties
			var textInputProps:Object = ObjectUtil.clone(_baseProps);
			delete textInputProps.uid;
			textInputProps.name = name;
			textInputProps.toolTip = description;
			
			// Create the TextInput
			_textInputFactory.properties = textInputProps;
			var component : DisplayObject = _textInputFactory.newInstance() as DisplayObject;
			IVisualElementContainer (container).addElement (IVisualElement(component));
			
			// Binding: change generated component's value when the originating value changes
			var bindingClosure : Function = function (newValue : String) : void {
				component[TEXT] = newValue;
			}
			var watcher : ChangeWatcher = BindingUtils.bindSetter (bindingClosure, _originator, name);
			
			// Listen to TextInput text changes
			component.addEventListener(Event.CHANGE, _onTextInputChange);
			var bindData : Object = {};
			bindData[BlueprintKeys.BOUND_EVENT] = Event.CHANGE;
			bindData[BlueprintKeys.BOUND_FUNCTION] = _onTextInputChange;
			bindData[BlueprintKeys.BOUND_COMPONENT] = component;
			bindData[BlueprintKeys.BOUND_CHANGE_WATCHER] = watcher;
			_uiBindingsMap[name] = bindData;
			
			// Return created TextInput
			return component;
		}
		
		/**
		 * Creates a CheckBox UI Component.
		 */
		private function _buildCheckBox (container : DisplayObjectContainer, blueprint : Object) : DisplayObject {
			var name : String = (blueprint[BlueprintKeys.NAME] as String);
			var label : String = (blueprint[BlueprintKeys.LABEL] as String);
			var description : String = Strings.trim(blueprint[BlueprintKeys.DESCRIPTION] as String);
			
			// Collect properties
			var checkBoxProps:Object = ObjectUtil.clone(_baseProps);
			delete checkBoxProps.uid;
			checkBoxProps.name = name;
			checkBoxProps.label = label;
			checkBoxProps.toolTip = description;
			
			// Create the CheckBox
			_checkBoxFactory.properties = checkBoxProps;
			var component : DisplayObject = _checkBoxFactory.newInstance() as DisplayObject;
			IVisualElementContainer (container).addElement (IVisualElement(component));
			
			// Binding: change generated component's value when the originating value changes
			var bindingClosure : Function = function (newValue : Boolean) : void {
				component[SELECTED] = newValue;
			} 
			var watcher : ChangeWatcher = BindingUtils.bindSetter (bindingClosure, _originator, name);
			
			// Listen to CheckBox state changes
			component.addEventListener (Event.CHANGE, _onCheckBoxChange);
			var bindData : Object = {};
			bindData[BlueprintKeys.BOUND_EVENT] = Event.CHANGE;
			bindData[BlueprintKeys.BOUND_FUNCTION] = _onCheckBoxChange;
			bindData[BlueprintKeys.BOUND_COMPONENT] = component;
			bindData[BlueprintKeys.BOUND_CHANGE_WATCHER] = watcher;
			_uiBindingsMap[name] = bindData;
			
			// Return created CheckBox
			return component;
		}
		
		/**
		 * Create a NumericStepper or a Slider inside the provided container. If the accessor
		 * is of type Number and has a minimum of `0` and a maximum of `1`, then a Slider will
		 * be created; otherwise, a Numeric stepper will be created.
		 */
		private function _buildNumericComponent (container : DisplayObjectContainer, blueprint : Object) : DisplayObject {
			var name : String = (blueprint[BlueprintKeys.NAME] as String);
			
			// Collect properties
			var componentProps:Object = ObjectUtil.clone(_baseProps);
			delete componentProps.uid;
			componentProps.name = name;
			var minimum : Number = parseFloat (blueprint[BlueprintKeys.MINIMUM]) as Number;
			if (!isNaN (minimum)) {
				componentProps.minimum = minimum;
			} else {
				componentProps.minimum = int.MIN_VALUE;
			}
			var maximum : Number = parseFloat(blueprint[BlueprintKeys.MAXIMUM]) as Number;
			if (!isNaN (maximum)) {
				componentProps.maximum = maximum;
			} else {
				componentProps.maximum = int.MAX_VALUE;
			}
			var type : String = blueprint[BlueprintKeys.TYPE] as String;
			componentProps.stepSize = (type == SupportedTypes.NUMBER)? 0.01 : 1;
				
			// Decide what type of component to create
			var factory : ClassFactory = (type == SupportedTypes.NUMBER && minimum == 0 && maximum == 1)?
				_sliderFactory : _numericStepperFactory;
			if (factory == _sliderFactory) {
				componentProps.dataTipFormatFunction = Strings.toPercentageFormat;
			}
			
			// Create the component
			factory.properties = componentProps;
			var component : DisplayObject = factory.newInstance() as DisplayObject;
			IVisualElementContainer (container).addElement (IVisualElement(component));
			
			// Binding: change generated component's value when the originating value changes
			var bindingClosure : Function = function (newValue : Number) : void {
				component[VALUE] = newValue;
			} 
			var watcher : ChangeWatcher = BindingUtils.bindSetter (bindingClosure, _originator, name);
			
			// Listen to component value changes
			component.addEventListener (Event.CHANGE, _onNumericChange);
			var bindData : Object = {};
			bindData[BlueprintKeys.BOUND_EVENT] = Event.CHANGE;
			bindData[BlueprintKeys.BOUND_FUNCTION] = _onNumericChange;
			bindData[BlueprintKeys.BOUND_COMPONENT] = component;
			bindData[BlueprintKeys.BOUND_CHANGE_WATCHER] = watcher;
			_uiBindingsMap[name] = bindData;
			
			// Return created component
			return component;
		}
		
		/**
		 * Create a ComboBox for a pair of similarly named Object/Array accessors.
		 * 
		 * The ComboBox choices are read from a getter of type Array that uses the Object
		 * accessor's name as a prefix for its own name. For example, if the Object
		 * accessor has the name "myChoice", a matching Array accessor must exist that has
		 * the name "myChoiceSrc".
		 * 
		 * User will be faced with a listing of the values defined by "myChoiceSrc". When
		 * he selects a value, "myChoice" will be set to that value.
		 */
		private function _buildComboBoxComponent (container : DisplayObjectContainer, blueprint : Object) : DisplayObject {
			var name : String = (blueprint[BlueprintKeys.NAME] as String);
			
			// Collect properties
			var comboProps : Object = ObjectUtil.clone(_baseProps);
			delete comboProps.uid;
			comboProps.name = name;
			comboProps.labelField = LIST_LABEL_FIELD;
			comboProps.prompt = COMBO_PROMPT;
			comboProps.labelToItemFunction = _discardComboBoxInput;
			var source : Array = (blueprint[BlueprintKeys.SOURCE] as Array);
			if (source != null) {
				comboProps.dataProvider = new ArrayCollection (source);
			}

			// Create the ComboBox
			_comboBoxFactory.properties = comboProps;
			var component : DisplayObject = _comboBoxFactory.newInstance() as DisplayObject;
			IVisualElementContainer (container).addElement (IVisualElement(component));
			
			// Binding: change generated component's value when the originating value changes
			var bindingClosure : Function = function (newValue : Object) : void {
				
				// Cope with the case where the originator is a simple Object, and an empty
				// Object MUST be given as the property initial value. If we do not nullify
				// that empty Object here, "[Object object]" will be displayed in the
				// generated ComboBox prompt field.
				if (newValue && (newValue is Object) && (newValue.constructor == Object) && Objects.isEmpty (newValue)) {
					newValue = null;
				}
				if (component[DATA_PROVIDER]) {
					component[SELECTED_ITEM] = newValue;
				}
			} 
			var watcher : ChangeWatcher = BindingUtils.bindSetter (bindingClosure, _originator, name);
			
			// Listen to ComboBox state changes
			component.addEventListener (Event.CHANGE, _onComboBoxChange);
			var bindData : Object = {};
			bindData[BlueprintKeys.BOUND_EVENT] = Event.CHANGE;
			bindData[BlueprintKeys.BOUND_FUNCTION] = _onComboBoxChange;
			bindData[BlueprintKeys.BOUND_COMPONENT] = component;
			bindData[BlueprintKeys.BOUND_CHANGE_WATCHER] = watcher;
			_uiBindingsMap[name] = bindData;
			
			// Return created ComboBox
			return component;
		}
		
		/**
		 * Create a List for a pair of similarly named Array accessors.
		 * 
		 * The List choices are read from a getter of type Array that uses the original accessor's name
		 * as a prefix for its own name. For example, if the original accessor has the name "myChoices",
		 * a matching Array getter must exist that has the name "myChoicesSrc".
		 * 
		 * User will be faced with a listing of the values defined by "myChoicesSrc". When he selects
		 * some values, "myChoices" will be populates with those values. Generated lists will always
		 * have multiple selection enabled.
		 */
		private function _buildListComponent (container : DisplayObjectContainer, blueprint : Object) : DisplayObject {
			var name : String = (blueprint[BlueprintKeys.NAME] as String);
			
			// Collect properties
			var listProps : Object = ObjectUtil.clone(_baseProps);
			delete listProps.uid;
			listProps.name = name;
			listProps.labelField = LIST_LABEL_FIELD;
			listProps.allowMultipleSelection = true;
			var source : Array = (blueprint[BlueprintKeys.SOURCE] as Array);
			if (source != null) {
				listProps.dataProvider = new ArrayCollection(source);
			}
			
			// Create the list
			_listFactory.properties = listProps;
			var component : DisplayObject = _listFactory.newInstance() as DisplayObject;
			IVisualElementContainer (container).addElement (IVisualElement(component));
			
			// Binding: change generated component's value when the originating value changes
			var bindingClosure : Function = function (newValue : Object) : void {
				if (component[DATA_PROVIDER] && newValue) {
					component[SELECTED_ITEMS] = Vector.<Object> (newValue);
				}
			}
			var watcher : ChangeWatcher = BindingUtils.bindSetter (bindingClosure, _originator, name);
			
			// Listen to list state changes
			component.addEventListener (Event.CHANGE, _onListChange);
			var bindData : Object = {};
			bindData[BlueprintKeys.BOUND_EVENT] = Event.CHANGE;
			bindData[BlueprintKeys.BOUND_FUNCTION] = _onListChange;
			bindData[BlueprintKeys.BOUND_COMPONENT] = component;
			bindData[BlueprintKeys.BOUND_CHANGE_WATCHER] = watcher;
			_uiBindingsMap[name] = bindData;
			
			// Return created list
			return component;
		}
		
		/**
		 * Create a custom component for every accessor annotated or configured with "CustomComponent".
		 */
		private function _buildCustomComponent (container : DisplayObjectContainer, blueprint : Object) : DisplayObject {
			var name : String = (blueprint[BlueprintKeys.NAME] as String);
			var descriptor : Object = blueprint[BlueprintKeys.CUSTOM_COMPONENT];
			var className : String = (descriptor[BlueprintKeys.CLASS_FQN] as String);
			var test : Object;
			var classDefinition : Class;
			try {
				if (className) {
					test = getDefinitionByName (className);
				}
			} catch (error : ReferenceError) {
				trace ('Cannot render custom component for accessor ' + name +  ' because required class ' +
					className + ' could not be initialized. Skipping to next accessor. Error was:\n' +
					error.message);
			};
			if (test) {
				classDefinition = (test as Class);
			}
			
			// If component class is initializable, proceed with creating the component
			if (classDefinition) {
				
				// Provide a Label if not instructed otherwise
				var hideLabelSetting : Object = descriptor[BlueprintKeys.HIDE_LABEL]; 
				var mustHideLabel : Boolean = (hideLabelSetting === TRUE || hideLabelSetting === true);
				if (!mustHideLabel) {
					_buildSpacer (_container);
					_buildLabel (_container, blueprint);
				}
				
				// Collect properties
				var componentProps : Object = _filterProperties (descriptor, RESERVED_KEYS);
				componentProps.name = name;
				var dataProviderName : String = (descriptor[BlueprintKeys.DATAPROVIDER_NAME] as String) ||
					DEFAULT_DATAPROVIDER_NAME;
				var arraySource : Array = (blueprint[BlueprintKeys.SOURCE] as Array);
				componentProps[dataProviderName] = arraySource || blueprint[BlueprintKeys.DEFAULT];
				
				// Create the component
				var factory : ClassFactory = new ClassFactory (classDefinition);
				factory.properties = componentProps;
				var component : DisplayObject = factory.newInstance() as DisplayObject;
				IVisualElementContainer (container).addElement (IVisualElement(component));
				
				// Binding: change generated component's value when the originating value changes
				var bindingTargetName : String = (descriptor[BlueprintKeys.BINDING_TARGET] as String) || dataProviderName; 
				var bindingClosure : Function = function (newValue : Object) : void {
					if (arraySource) {
						if (component[dataProviderName] && newValue) {
							component[bindingTargetName] = newValue;
						}
					} else {
						component[bindingTargetName] = newValue;
					}
				};
				var bindingSourceName : String = (descriptor[BlueprintKeys.BINDING_SOURCE] as String) || name;
				var watcher : ChangeWatcher = BindingUtils.bindSetter (bindingClosure, _originator, bindingSourceName);
				
				// Listen to internal state changes
				var changeEventName : String = (blueprint[BlueprintKeys.CHANGE_EVENT_NAME] as String) || Event.CHANGE;
				var observedProperty : String = arraySource? bindingTargetName : dataProviderName;
				var changeCallback : Function = function (event : Event) : void {
					_componentChangedCallback (name, component[observedProperty]);
				};
				component.addEventListener (changeEventName, changeCallback);
				var bindData : Object = {};
				bindData[BlueprintKeys.BOUND_EVENT] = changeEventName;
				bindData[BlueprintKeys.BOUND_FUNCTION] = changeCallback;
				bindData[BlueprintKeys.BOUND_COMPONENT] = component;
				bindData[BlueprintKeys.BOUND_CHANGE_WATCHER] = watcher;
				_uiBindingsMap[name] = bindData;
				
				// Return created component
				return component;
			}
			
			// Otherwise, skip to next blueprint in queue
			trace ('NOT RENDERING', name, 'because custom component could not be initialized. Provided class name was: [' + className + '].');
			return null;
		}
		
		/**
		 * Triggered after a generated UI Component has been successfully rendered.
		 */
		private function _onGeneratedControlRendered (event : Event) : void {
			var target : IEventDispatcher = IEventDispatcher (event.target);
			target.removeEventListener(FlexEvent.UPDATE_COMPLETE, _onGeneratedControlRendered);
			_componentGeneratedCallback();
		}
		
		/**
		 * Called when user changes the value of a generated Checkbox UI Component
		 */
		private function _onCheckBoxChange(event:Event):void {
			var cb : CheckBox = (event.target as CheckBox);
			var key : String = cb.name;
			var value : Boolean = cb.selected;
			_componentChangedCallback (key, value);
		}

		/**
		 * Called when user changes the value of a generated TextInput UI Component
		 */
		private function _onTextInputChange (event : Event) : void {
			var ti : TextInput = (event.target as TextInput);
			var key : String = ti.name;
			var value : String = ti.text;
			_componentChangedCallback (key, value);
		}
		
		/**
		 * Called when user changes the value of a generated Numeric Stepper UI Component
		 */
		private function _onNumericChange(event:Event):void {
			var el : IVisualElement = (event.target as IVisualElement);
			var key : String = el[NAME];
			var value : Number = el[VALUE];
			_componentChangedCallback (key, value);
		}
		
		/**
		 * Called when user changes the value of a generated ComboBox UI Component
		 */
		private function _onComboBoxChange (event : Event) : void {
			var combo : ComboBox = (event.target as ComboBox);			
			var key : String = combo.name;
			var value : Object = combo.selectedItem;
			_componentChangedCallback (key, value);
		}
		
		/**
		 * Called when user changes the value of a generated List UI Component
		 */
		private function _onListChange (event : Event) : void {
			var list : List = (event.target as List);
			var key : String = list.name;
			var value : Array = [];
			var numItems : int;
			var i : int;
			var rawValue : Vector.<Object> = list.selectedItems;
			if (rawValue) {
				numItems = rawValue.length;
				for (i = 0; i < numItems; i++) {
					value[i] = rawValue[i];
				}
			}
			_componentChangedCallback(key, value);
		}

		/**
		 * Used as the "labelToItemFunction" property for all generated ComboBoxes.
		 * Prevents non-matching text typed by the user in the input field from 
		 * being submitted.
		 */
		private function _discardComboBoxInput (userInput : String) : Object {
			return null;
		}
		
		/**
		 * Helper for the `_buildCustomComponent()` method; filters out certain keys from
		 * a given Object and returns the result as a new Object. 
		 */
		private function _filterProperties (raw : Object, exclusionList : Array) : Object {
			var filtered : Object = {};
			var key : String;
			var value : Object;
			for (key in raw) {
				if (exclusionList.indexOf(key) != -1) {
					continue;
				}
				value = raw[key];
				filtered[key] = value;
			}
			return filtered;
		}
		
	}
}