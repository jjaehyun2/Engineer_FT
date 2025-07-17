package kitaec.controls.comboboxes.autoComplete {

import kitaec.controls.comboboxes.AutoPopulatedValueComboBox;
import kitaec.controls.comboboxes.autoComplete.renderers.DefaultAutoCompleteItemRenderer;
import kitaec.controls.comboboxes.autoComplete.renderers.IAutoCompleteRenderer;

import flash.events.FocusEvent;
	
	import flashx.textLayout.operations.CopyOperation;
	import flashx.textLayout.operations.FlowOperation;
	
	import mx.collections.ListCollectionView;
	import mx.core.ClassFactory;
	import mx.core.IVisualElement;
	import mx.core.mx_internal;
	
	import spark.events.IndexChangeEvent;
	import spark.events.TextOperationEvent;
	
	use namespace mx_internal;
	
	public class AutoCompleteComboBox extends AutoPopulatedValueComboBox {
		
		public static const DEFAULT_PROMPT:String = "Type to Search";
		
		protected var filterDataProvider:Boolean = false;
		private var _filterFunction:Function = autoCompleteFilter;
		private var _typeAheadText:String = '';
		
		private var textOperation:FlowOperation;
		
		public function AutoCompleteComboBox() {
			super();
			prompt = DEFAULT_PROMPT;
			addEventListener(IndexChangeEvent.CHANGE, onChange);
			itemRenderer = new ClassFactory(DefaultAutoCompleteItemRenderer);
		}
		
		override protected function commitProperties():void {
			
			var selectedIndexChanged:Boolean = _proposedSelectedIndex != NO_PROPOSED_SELECTION;
			
			if (filterDataProvider == true && selectedIndexChanged == false && selectedIndex != NO_SELECTION) {
				selectedIndex = NO_SELECTION;
				userProposedSelectedIndex = NO_SELECTION;
			}
			
			super.commitProperties();
			
			if (filterDataProvider == true) {
				if ((textInput.text == '') && (typeAheadText != '')) {
					textInput.text = typeAheadText;
					textInput.selectRange(typeAheadText.length, typeAheadText.length);
				}
				
				var tempSelectedItem:*;
				if (selectedItem) {
					tempSelectedItem = selectedItem;
				}
				
				refreshDataProvider();
				
				if (tempSelectedItem) {
					selectedItem = tempSelectedItem;
					super.commitProperties();
				}
				
				filterDataProvider = false;
			}
			
			if ((selectedIndexChanged)) {
				if (selectedIndex == NO_SELECTION) {
					if ((textInput.text != typeAheadText)) {
						textInput.text = typeAheadText;
					}
					
				} else if ((selectedIndex >= 0) && (textInput.text == '')) {
					updateLabelDisplay();
				}
			}
		}
		
		[Bindable]
		[Inspectable(category = "AutoComplete", defaultValue = "autoCompleteFilter", name = "AutoComplete Filter Function", type = "Function")]
		public function get filterFunction():Function {
			return _filterFunction;
		}
		
		public function set filterFunction(value:Function):void {
			_filterFunction = value;
		}
		
		[Bindable]
		public function get typeAheadText():String {
			return _typeAheadText;
		}

        public function set typeAheadText(value:String):void {
			_typeAheadText = value;
			dirtyDataProviderFilter();
			invalidateProperties();
		}
		protected function autoCompleteFilter(item:Object):Boolean {
			var label:String = itemToLabel(item);
			
			label = label.substring(0, typeAheadText.length);
			return label.toUpperCase() == typeAheadText.toUpperCase();
		}
		
		protected function dirtyDataProviderFilter():void {
			filterDataProvider = true;
			invalidateProperties();
		}
		
		override public function updateRenderer(renderer:IVisualElement, itemIndex:int, data:Object):void {
			if (renderer is IAutoCompleteRenderer) {
				var acRenderer:IAutoCompleteRenderer = renderer as IAutoCompleteRenderer;
				acRenderer.autoComplete = this;
				acRenderer.typeAheadText = typeAheadText;
			}
			super.updateRenderer(renderer, itemIndex, data);
		}
		
		
		protected function refreshDataProvider():void {
			if (dataProvider) {
				(dataProvider as ListCollectionView).filterFunction = filterFunction;
				(dataProvider as ListCollectionView).refresh();
			}
		}
		
		protected function onChange(event:IndexChangeEvent):void {
			if ((event.oldIndex < 0) && (event.newIndex >= 0)) {
				typeAheadText = "";
			}
		}
		
		override protected function textInput_changeHandler(event:TextOperationEvent):void {
			super.textInput_changeHandler(event);
			textOperation = event.operation;
			if (event.operation is CopyOperation) {
				return;
			}
			
			typeAheadText = textInput.text;
			
			if (openOnInput) {
				if (textInput.text == '') {
					if (isDropDownOpen) {
						closeDropDown(false);
					}
					return;
				}
				
				if ((!isDropDownOpen)) {
					openDropDown();
					return;
				} else if (typeAheadText == '') {
					closeDropDown(false);
				}
			}
		}
		
		override mx_internal function dataProviderRefreshed():void {
			// do nothing 
		}
		
		override protected function focusOutHandler(event:FocusEvent):void {
			super.focusOutHandler(event);
			typeAheadText = "";
		}
	}
}