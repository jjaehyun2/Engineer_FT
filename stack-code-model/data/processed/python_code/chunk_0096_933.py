/**
 * This is a generated class and is not intended for modification.  
 */
package restServices.WorkspaceWebServicePortal.valueobjects
{
	import com.adobe.fiber.styles.IStyle;
	import com.adobe.fiber.styles.Style;
	import com.adobe.fiber.styles.StyleValidator;
	import com.adobe.fiber.valueobjects.AbstractEntityMetadata;
	import com.adobe.fiber.valueobjects.AvailablePropertyIterator;
	import com.adobe.fiber.valueobjects.IPropertyIterator;
	import mx.events.ValidationResultEvent;
	import com.adobe.fiber.core.model_internal;
	import com.adobe.fiber.valueobjects.IModelType;
	import mx.events.PropertyChangeEvent;
	
	use namespace model_internal;
	
	[ExcludeClass]
	internal class _WorkspaceDataItemEntityMetadata extends com.adobe.fiber.valueobjects.AbstractEntityMetadata
	{
		private static var emptyArray:Array = new Array();
		
		model_internal static var allProperties:Array = new Array("WorkspaceID", "Title", "Description", "MapExtent", "MapServices", "GraphicLayers", "CreatedTime", "LastModified");
		model_internal static var allAssociationProperties:Array = new Array();
		model_internal static var allRequiredProperties:Array = new Array("WorkspaceID", "Title", "Description", "MapExtent", "MapServices", "GraphicLayers", "CreatedTime", "LastModified");
		model_internal static var allAlwaysAvailableProperties:Array = new Array("WorkspaceID", "Title", "Description", "MapExtent", "MapServices", "GraphicLayers", "CreatedTime", "LastModified");
		model_internal static var guardedProperties:Array = new Array();
		model_internal static var dataProperties:Array = new Array("WorkspaceID", "Title", "Description", "MapExtent", "MapServices", "GraphicLayers", "CreatedTime", "LastModified");
		model_internal static var derivedProperties:Array = new Array();
		model_internal static var collectionProperties:Array = new Array("MapExtent");
		model_internal static var collectionBaseMap:Object;
		model_internal static var entityName:String = "WorkspaceDataItem";
		model_internal static var dependentsOnMap:Object;
		model_internal static var dependedOnServices:Array = new Array();
		
		
		model_internal var _WorkspaceIDIsValid:Boolean;
		model_internal var _WorkspaceIDValidator:com.adobe.fiber.styles.StyleValidator;
		model_internal var _WorkspaceIDIsValidCacheInitialized:Boolean = false;
		model_internal var _WorkspaceIDValidationFailureMessages:Array;
		
		model_internal var _TitleIsValid:Boolean;
		model_internal var _TitleValidator:com.adobe.fiber.styles.StyleValidator;
		model_internal var _TitleIsValidCacheInitialized:Boolean = false;
		model_internal var _TitleValidationFailureMessages:Array;
		
		model_internal var _DescriptionIsValid:Boolean;
		model_internal var _DescriptionValidator:com.adobe.fiber.styles.StyleValidator;
		model_internal var _DescriptionIsValidCacheInitialized:Boolean = false;
		model_internal var _DescriptionValidationFailureMessages:Array;
		
		model_internal var _MapExtentIsValid:Boolean;
		model_internal var _MapExtentValidator:com.adobe.fiber.styles.StyleValidator;
		model_internal var _MapExtentIsValidCacheInitialized:Boolean = false;
		model_internal var _MapExtentValidationFailureMessages:Array;
		
		model_internal var _MapServicesIsValid:Boolean;
		model_internal var _MapServicesValidator:com.adobe.fiber.styles.StyleValidator;
		model_internal var _MapServicesIsValidCacheInitialized:Boolean = false;
		model_internal var _MapServicesValidationFailureMessages:Array;
		
		model_internal var _GraphicLayersIsValid:Boolean;
		model_internal var _GraphicLayersValidator:com.adobe.fiber.styles.StyleValidator;
		model_internal var _GraphicLayersIsValidCacheInitialized:Boolean = false;
		model_internal var _GraphicLayersValidationFailureMessages:Array;
		
		model_internal var _CreatedTimeIsValid:Boolean;
		model_internal var _CreatedTimeValidator:com.adobe.fiber.styles.StyleValidator;
		model_internal var _CreatedTimeIsValidCacheInitialized:Boolean = false;
		model_internal var _CreatedTimeValidationFailureMessages:Array;
		
		model_internal var _LastModifiedIsValid:Boolean;
		model_internal var _LastModifiedValidator:com.adobe.fiber.styles.StyleValidator;
		model_internal var _LastModifiedIsValidCacheInitialized:Boolean = false;
		model_internal var _LastModifiedValidationFailureMessages:Array;
		
		model_internal var _instance:_Super_WorkspaceDataItem;
		model_internal static var _nullStyle:com.adobe.fiber.styles.Style = new com.adobe.fiber.styles.Style();
		
		public function _WorkspaceDataItemEntityMetadata(value : _Super_WorkspaceDataItem)
		{
			// initialize property maps
			if (model_internal::dependentsOnMap == null)
			{
				// depenents map
				model_internal::dependentsOnMap = new Object();
				model_internal::dependentsOnMap["WorkspaceID"] = new Array();
				model_internal::dependentsOnMap["Title"] = new Array();
				model_internal::dependentsOnMap["Description"] = new Array();
				model_internal::dependentsOnMap["MapExtent"] = new Array();
				model_internal::dependentsOnMap["MapServices"] = new Array();
				model_internal::dependentsOnMap["GraphicLayers"] = new Array();
				model_internal::dependentsOnMap["CreatedTime"] = new Array();
				model_internal::dependentsOnMap["LastModified"] = new Array();
				
				// collection base map
				model_internal::collectionBaseMap = new Object()
				model_internal::collectionBaseMap["MapExtent"] = "Number";
			}
			
			model_internal::_instance = value;
			model_internal::_WorkspaceIDValidator = new StyleValidator(model_internal::_instance.model_internal::_doValidationForWorkspaceID);
			model_internal::_WorkspaceIDValidator.required = true;
			model_internal::_WorkspaceIDValidator.requiredFieldError = "WorkspaceID is required";
			//model_internal::_WorkspaceIDValidator.source = model_internal::_instance;
			//model_internal::_WorkspaceIDValidator.property = "WorkspaceID";
			model_internal::_TitleValidator = new StyleValidator(model_internal::_instance.model_internal::_doValidationForTitle);
			model_internal::_TitleValidator.required = true;
			model_internal::_TitleValidator.requiredFieldError = "Title is required";
			//model_internal::_TitleValidator.source = model_internal::_instance;
			//model_internal::_TitleValidator.property = "Title";
			model_internal::_DescriptionValidator = new StyleValidator(model_internal::_instance.model_internal::_doValidationForDescription);
			model_internal::_DescriptionValidator.required = true;
			model_internal::_DescriptionValidator.requiredFieldError = "Description is required";
			//model_internal::_DescriptionValidator.source = model_internal::_instance;
			//model_internal::_DescriptionValidator.property = "Description";
			model_internal::_MapExtentValidator = new StyleValidator(model_internal::_instance.model_internal::_doValidationForMapExtent);
			model_internal::_MapExtentValidator.required = true;
			model_internal::_MapExtentValidator.requiredFieldError = "MapExtent is required";
			//model_internal::_MapExtentValidator.source = model_internal::_instance;
			//model_internal::_MapExtentValidator.property = "MapExtent";
			model_internal::_MapServicesValidator = new StyleValidator(model_internal::_instance.model_internal::_doValidationForMapServices);
			model_internal::_MapServicesValidator.required = true;
			model_internal::_MapServicesValidator.requiredFieldError = "MapServices is required";
			//model_internal::_MapServicesValidator.source = model_internal::_instance;
			//model_internal::_MapServicesValidator.property = "MapServices";
			model_internal::_GraphicLayersValidator = new StyleValidator(model_internal::_instance.model_internal::_doValidationForGraphicLayers);
			model_internal::_GraphicLayersValidator.required = true;
			model_internal::_GraphicLayersValidator.requiredFieldError = "GraphicLayers is required";
			//model_internal::_GraphicLayersValidator.source = model_internal::_instance;
			//model_internal::_GraphicLayersValidator.property = "GraphicLayers";
			model_internal::_CreatedTimeValidator = new StyleValidator(model_internal::_instance.model_internal::_doValidationForCreatedTime);
			model_internal::_CreatedTimeValidator.required = true;
			model_internal::_CreatedTimeValidator.requiredFieldError = "CreatedTime is required";
			//model_internal::_CreatedTimeValidator.source = model_internal::_instance;
			//model_internal::_CreatedTimeValidator.property = "CreatedTime";
			model_internal::_LastModifiedValidator = new StyleValidator(model_internal::_instance.model_internal::_doValidationForLastModified);
			model_internal::_LastModifiedValidator.required = true;
			model_internal::_LastModifiedValidator.requiredFieldError = "LastModified is required";
			//model_internal::_LastModifiedValidator.source = model_internal::_instance;
			//model_internal::_LastModifiedValidator.property = "LastModified";
		}
		
		override public function getEntityName():String
		{
			return model_internal::entityName;
		}
		
		override public function getProperties():Array
		{
			return model_internal::allProperties;
		}
		
		override public function getAssociationProperties():Array
		{
			return model_internal::allAssociationProperties;
		}
		
		override public function getRequiredProperties():Array
		{
			return model_internal::allRequiredProperties;   
		}
		
		override public function getDataProperties():Array
		{
			return model_internal::dataProperties;
		}
		
		override public function getGuardedProperties():Array
		{
			return model_internal::guardedProperties;
		}
		
		override public function getUnguardedProperties():Array
		{
			return model_internal::allAlwaysAvailableProperties;
		}
		
		override public function getDependants(propertyName:String):Array
		{
			if (model_internal::dataProperties.indexOf(propertyName) == -1)
				throw new Error(propertyName + " is not a data property of entity WorkspaceDataItem");  
			
			return model_internal::dependentsOnMap[propertyName] as Array;  
		}
		
		override public function getDependedOnServices():Array
		{
			return model_internal::dependedOnServices;
		}
		
		override public function getCollectionProperties():Array
		{
			return model_internal::collectionProperties;
		}
		
		override public function getCollectionBase(propertyName:String):String
		{
			if (model_internal::collectionProperties.indexOf(propertyName) == -1)
				throw new Error(propertyName + " is not a collection property of entity WorkspaceDataItem");  
			
			return model_internal::collectionBaseMap[propertyName];
		}
		
		override public function getAvailableProperties():com.adobe.fiber.valueobjects.IPropertyIterator
		{
			return new com.adobe.fiber.valueobjects.AvailablePropertyIterator(this);
		}
		
		override public function getValue(propertyName:String):*
		{
			if (model_internal::allProperties.indexOf(propertyName) == -1)
			{
				throw new Error(propertyName + " does not exist for entity WorkspaceDataItem");
			}
			
			return model_internal::_instance[propertyName];
		}
		
		override public function setValue(propertyName:String, value:*):void
		{
			if (model_internal::dataProperties.indexOf(propertyName) == -1)
			{
				throw new Error(propertyName + " is not a data property of entity WorkspaceDataItem");
			}
			
			model_internal::_instance[propertyName] = value;
		}
		
		override public function getMappedByProperty(associationProperty:String):String
		{
			switch(associationProperty)
			{
				default:
				{
					return null;
				}
			}
		}
		
		override public function getPropertyLength(propertyName:String):int
		{
			switch(propertyName)
			{
				default:
				{
					return 0;
				}
			}
		}
		
		override public function isAvailable(propertyName:String):Boolean
		{
			if (model_internal::allProperties.indexOf(propertyName) == -1)
			{
				throw new Error(propertyName + " does not exist for entity WorkspaceDataItem");
			}
			
			if (model_internal::allAlwaysAvailableProperties.indexOf(propertyName) != -1)
			{
				return true;
			}
			
			switch(propertyName)
			{
				default:
				{
					return true;
				}
			}
		}
		
		override public function getIdentityMap():Object
		{
			var returnMap:Object = new Object();
			
			return returnMap;
		}
		
		[Bindable(event="propertyChange")]
		override public function get invalidConstraints():Array
		{
			if (model_internal::_instance.model_internal::_cacheInitialized_isValid)
			{
				return model_internal::_instance.model_internal::_invalidConstraints;
			}
			else
			{
				// recalculate isValid
				model_internal::_instance.model_internal::_isValid = model_internal::_instance.model_internal::calculateIsValid();
				return model_internal::_instance.model_internal::_invalidConstraints;        
			}
		}
		
		[Bindable(event="propertyChange")]
		override public function get validationFailureMessages():Array
		{
			if (model_internal::_instance.model_internal::_cacheInitialized_isValid)
			{
				return model_internal::_instance.model_internal::_validationFailureMessages;
			}
			else
			{
				// recalculate isValid
				model_internal::_instance.model_internal::_isValid = model_internal::_instance.model_internal::calculateIsValid();
				return model_internal::_instance.model_internal::_validationFailureMessages;
			}
		}
		
		override public function getDependantInvalidConstraints(propertyName:String):Array
		{
			var dependants:Array = getDependants(propertyName);
			if (dependants.length == 0)
			{
				return emptyArray;
			}
			
			var currentlyInvalid:Array = invalidConstraints;
			if (currentlyInvalid.length == 0)
			{
				return emptyArray;
			}
			
			var filterFunc:Function = function(element:*, index:int, arr:Array):Boolean
			{
				return dependants.indexOf(element) > -1;
			}
			
			return currentlyInvalid.filter(filterFunc);
		}
		
		/**
		 * isValid
		 */
		[Bindable(event="propertyChange")] 
		public function get isValid() : Boolean
		{
			if (model_internal::_instance.model_internal::_cacheInitialized_isValid)
			{
				return model_internal::_instance.model_internal::_isValid;
			}
			else
			{
				// recalculate isValid
				model_internal::_instance.model_internal::_isValid = model_internal::_instance.model_internal::calculateIsValid();
				return model_internal::_instance.model_internal::_isValid;
			}
		}
		
		[Bindable(event="propertyChange")]
		public function get isWorkspaceIDAvailable():Boolean
		{
			return true;
		}
		
		[Bindable(event="propertyChange")]
		public function get isTitleAvailable():Boolean
		{
			return true;
		}
		
		[Bindable(event="propertyChange")]
		public function get isDescriptionAvailable():Boolean
		{
			return true;
		}
		
		[Bindable(event="propertyChange")]
		public function get isMapExtentAvailable():Boolean
		{
			return true;
		}
		
		[Bindable(event="propertyChange")]
		public function get isMapServicesAvailable():Boolean
		{
			return true;
		}
		
		[Bindable(event="propertyChange")]
		public function get isGraphicLayersAvailable():Boolean
		{
			return true;
		}
		
		[Bindable(event="propertyChange")]
		public function get isCreatedTimeAvailable():Boolean
		{
			return true;
		}
		
		[Bindable(event="propertyChange")]
		public function get isLastModifiedAvailable():Boolean
		{
			return true;
		}
		
		
		/**
		 * derived property recalculation
		 */
		public function invalidateDependentOnWorkspaceID():void
		{
			if (model_internal::_WorkspaceIDIsValidCacheInitialized )
			{
				model_internal::_instance.model_internal::_doValidationCacheOfWorkspaceID = null;
				model_internal::calculateWorkspaceIDIsValid();
			}
		}
		public function invalidateDependentOnTitle():void
		{
			if (model_internal::_TitleIsValidCacheInitialized )
			{
				model_internal::_instance.model_internal::_doValidationCacheOfTitle = null;
				model_internal::calculateTitleIsValid();
			}
		}
		public function invalidateDependentOnDescription():void
		{
			if (model_internal::_DescriptionIsValidCacheInitialized )
			{
				model_internal::_instance.model_internal::_doValidationCacheOfDescription = null;
				model_internal::calculateDescriptionIsValid();
			}
		}
		public function invalidateDependentOnMapExtent():void
		{
			if (model_internal::_MapExtentIsValidCacheInitialized )
			{
				model_internal::_instance.model_internal::_doValidationCacheOfMapExtent = null;
				model_internal::calculateMapExtentIsValid();
			}
		}
		public function invalidateDependentOnMapServices():void
		{
			if (model_internal::_MapServicesIsValidCacheInitialized )
			{
				model_internal::_instance.model_internal::_doValidationCacheOfMapServices = null;
				model_internal::calculateMapServicesIsValid();
			}
		}
		public function invalidateDependentOnGraphicLayers():void
		{
			if (model_internal::_GraphicLayersIsValidCacheInitialized )
			{
				model_internal::_instance.model_internal::_doValidationCacheOfGraphicLayers = null;
				model_internal::calculateGraphicLayersIsValid();
			}
		}
		public function invalidateDependentOnCreatedTime():void
		{
			if (model_internal::_CreatedTimeIsValidCacheInitialized )
			{
				model_internal::_instance.model_internal::_doValidationCacheOfCreatedTime = null;
				model_internal::calculateCreatedTimeIsValid();
			}
		}
		public function invalidateDependentOnLastModified():void
		{
			if (model_internal::_LastModifiedIsValidCacheInitialized )
			{
				model_internal::_instance.model_internal::_doValidationCacheOfLastModified = null;
				model_internal::calculateLastModifiedIsValid();
			}
		}
		
		model_internal function fireChangeEvent(propertyName:String, oldValue:Object, newValue:Object):void
		{
			this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, propertyName, oldValue, newValue));
		}
		
		[Bindable(event="propertyChange")]   
		public function get WorkspaceIDStyle():com.adobe.fiber.styles.Style
		{
			return model_internal::_nullStyle;
		}
		
		public function get WorkspaceIDValidator() : StyleValidator
		{
			return model_internal::_WorkspaceIDValidator;
		}
		
		model_internal function set _WorkspaceIDIsValid_der(value:Boolean):void 
		{
			var oldValue:Boolean = model_internal::_WorkspaceIDIsValid;         
			if (oldValue !== value)
			{
				model_internal::_WorkspaceIDIsValid = value;
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "WorkspaceIDIsValid", oldValue, value));
			}                             
		}
		
		[Bindable(event="propertyChange")]
		public function get WorkspaceIDIsValid():Boolean
		{
			if (!model_internal::_WorkspaceIDIsValidCacheInitialized)
			{
				model_internal::calculateWorkspaceIDIsValid();
			}
			
			return model_internal::_WorkspaceIDIsValid;
		}
		
		model_internal function calculateWorkspaceIDIsValid():void
		{
			var valRes:ValidationResultEvent = model_internal::_WorkspaceIDValidator.validate(model_internal::_instance.WorkspaceID)
			model_internal::_WorkspaceIDIsValid_der = (valRes.results == null);
			model_internal::_WorkspaceIDIsValidCacheInitialized = true;
			if (valRes.results == null)
				model_internal::WorkspaceIDValidationFailureMessages_der = emptyArray;
			else
			{
				var _valFailures:Array = new Array();
				for (var a:int = 0 ; a<valRes.results.length ; a++)
				{
					_valFailures.push(valRes.results[a].errorMessage);
				}
				model_internal::WorkspaceIDValidationFailureMessages_der = _valFailures;
			}
		}
		
		[Bindable(event="propertyChange")]
		public function get WorkspaceIDValidationFailureMessages():Array
		{
			if (model_internal::_WorkspaceIDValidationFailureMessages == null)
				model_internal::calculateWorkspaceIDIsValid();
			
			return _WorkspaceIDValidationFailureMessages;
		}
		
		model_internal function set WorkspaceIDValidationFailureMessages_der(value:Array) : void
		{
			var oldValue:Array = model_internal::_WorkspaceIDValidationFailureMessages;
			
			var needUpdate : Boolean = false;
			if (oldValue == null)
				needUpdate = true;
			
			// avoid firing the event when old and new value are different empty arrays
			if (!needUpdate && (oldValue !== value && (oldValue.length > 0 || value.length > 0)))
			{
				if (oldValue.length == value.length)
				{
					for (var a:int=0; a < oldValue.length; a++)
					{
						if (oldValue[a] !== value[a])
						{
							needUpdate = true;
							break;
						}
					}
				}
				else
				{
					needUpdate = true;
				}
			}
			
			if (needUpdate)
			{
				model_internal::_WorkspaceIDValidationFailureMessages = value;   
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "WorkspaceIDValidationFailureMessages", oldValue, value));
				// Only execute calculateIsValid if it has been called before, to update the validationFailureMessages for
				// the entire entity.
				if (model_internal::_instance.model_internal::_cacheInitialized_isValid)
				{
					model_internal::_instance.model_internal::isValid_der = model_internal::_instance.model_internal::calculateIsValid();
				}
			}
		}
		
		[Bindable(event="propertyChange")]   
		public function get TitleStyle():com.adobe.fiber.styles.Style
		{
			return model_internal::_nullStyle;
		}
		
		public function get TitleValidator() : StyleValidator
		{
			return model_internal::_TitleValidator;
		}
		
		model_internal function set _TitleIsValid_der(value:Boolean):void 
		{
			var oldValue:Boolean = model_internal::_TitleIsValid;         
			if (oldValue !== value)
			{
				model_internal::_TitleIsValid = value;
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "TitleIsValid", oldValue, value));
			}                             
		}
		
		[Bindable(event="propertyChange")]
		public function get TitleIsValid():Boolean
		{
			if (!model_internal::_TitleIsValidCacheInitialized)
			{
				model_internal::calculateTitleIsValid();
			}
			
			return model_internal::_TitleIsValid;
		}
		
		model_internal function calculateTitleIsValid():void
		{
			var valRes:ValidationResultEvent = model_internal::_TitleValidator.validate(model_internal::_instance.Title)
			model_internal::_TitleIsValid_der = (valRes.results == null);
			model_internal::_TitleIsValidCacheInitialized = true;
			if (valRes.results == null)
				model_internal::TitleValidationFailureMessages_der = emptyArray;
			else
			{
				var _valFailures:Array = new Array();
				for (var a:int = 0 ; a<valRes.results.length ; a++)
				{
					_valFailures.push(valRes.results[a].errorMessage);
				}
				model_internal::TitleValidationFailureMessages_der = _valFailures;
			}
		}
		
		[Bindable(event="propertyChange")]
		public function get TitleValidationFailureMessages():Array
		{
			if (model_internal::_TitleValidationFailureMessages == null)
				model_internal::calculateTitleIsValid();
			
			return _TitleValidationFailureMessages;
		}
		
		model_internal function set TitleValidationFailureMessages_der(value:Array) : void
		{
			var oldValue:Array = model_internal::_TitleValidationFailureMessages;
			
			var needUpdate : Boolean = false;
			if (oldValue == null)
				needUpdate = true;
			
			// avoid firing the event when old and new value are different empty arrays
			if (!needUpdate && (oldValue !== value && (oldValue.length > 0 || value.length > 0)))
			{
				if (oldValue.length == value.length)
				{
					for (var a:int=0; a < oldValue.length; a++)
					{
						if (oldValue[a] !== value[a])
						{
							needUpdate = true;
							break;
						}
					}
				}
				else
				{
					needUpdate = true;
				}
			}
			
			if (needUpdate)
			{
				model_internal::_TitleValidationFailureMessages = value;   
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "TitleValidationFailureMessages", oldValue, value));
				// Only execute calculateIsValid if it has been called before, to update the validationFailureMessages for
				// the entire entity.
				if (model_internal::_instance.model_internal::_cacheInitialized_isValid)
				{
					model_internal::_instance.model_internal::isValid_der = model_internal::_instance.model_internal::calculateIsValid();
				}
			}
		}
		
		[Bindable(event="propertyChange")]   
		public function get DescriptionStyle():com.adobe.fiber.styles.Style
		{
			return model_internal::_nullStyle;
		}
		
		public function get DescriptionValidator() : StyleValidator
		{
			return model_internal::_DescriptionValidator;
		}
		
		model_internal function set _DescriptionIsValid_der(value:Boolean):void 
		{
			var oldValue:Boolean = model_internal::_DescriptionIsValid;         
			if (oldValue !== value)
			{
				model_internal::_DescriptionIsValid = value;
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "DescriptionIsValid", oldValue, value));
			}                             
		}
		
		[Bindable(event="propertyChange")]
		public function get DescriptionIsValid():Boolean
		{
			if (!model_internal::_DescriptionIsValidCacheInitialized)
			{
				model_internal::calculateDescriptionIsValid();
			}
			
			return model_internal::_DescriptionIsValid;
		}
		
		model_internal function calculateDescriptionIsValid():void
		{
			var valRes:ValidationResultEvent = model_internal::_DescriptionValidator.validate(model_internal::_instance.Description)
			model_internal::_DescriptionIsValid_der = (valRes.results == null);
			model_internal::_DescriptionIsValidCacheInitialized = true;
			if (valRes.results == null)
				model_internal::DescriptionValidationFailureMessages_der = emptyArray;
			else
			{
				var _valFailures:Array = new Array();
				for (var a:int = 0 ; a<valRes.results.length ; a++)
				{
					_valFailures.push(valRes.results[a].errorMessage);
				}
				model_internal::DescriptionValidationFailureMessages_der = _valFailures;
			}
		}
		
		[Bindable(event="propertyChange")]
		public function get DescriptionValidationFailureMessages():Array
		{
			if (model_internal::_DescriptionValidationFailureMessages == null)
				model_internal::calculateDescriptionIsValid();
			
			return _DescriptionValidationFailureMessages;
		}
		
		model_internal function set DescriptionValidationFailureMessages_der(value:Array) : void
		{
			var oldValue:Array = model_internal::_DescriptionValidationFailureMessages;
			
			var needUpdate : Boolean = false;
			if (oldValue == null)
				needUpdate = true;
			
			// avoid firing the event when old and new value are different empty arrays
			if (!needUpdate && (oldValue !== value && (oldValue.length > 0 || value.length > 0)))
			{
				if (oldValue.length == value.length)
				{
					for (var a:int=0; a < oldValue.length; a++)
					{
						if (oldValue[a] !== value[a])
						{
							needUpdate = true;
							break;
						}
					}
				}
				else
				{
					needUpdate = true;
				}
			}
			
			if (needUpdate)
			{
				model_internal::_DescriptionValidationFailureMessages = value;   
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "DescriptionValidationFailureMessages", oldValue, value));
				// Only execute calculateIsValid if it has been called before, to update the validationFailureMessages for
				// the entire entity.
				if (model_internal::_instance.model_internal::_cacheInitialized_isValid)
				{
					model_internal::_instance.model_internal::isValid_der = model_internal::_instance.model_internal::calculateIsValid();
				}
			}
		}
		
		[Bindable(event="propertyChange")]   
		public function get MapExtentStyle():com.adobe.fiber.styles.Style
		{
			return model_internal::_nullStyle;
		}
		
		public function get MapExtentValidator() : StyleValidator
		{
			return model_internal::_MapExtentValidator;
		}
		
		model_internal function set _MapExtentIsValid_der(value:Boolean):void 
		{
			var oldValue:Boolean = model_internal::_MapExtentIsValid;         
			if (oldValue !== value)
			{
				model_internal::_MapExtentIsValid = value;
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "MapExtentIsValid", oldValue, value));
			}                             
		}
		
		[Bindable(event="propertyChange")]
		public function get MapExtentIsValid():Boolean
		{
			if (!model_internal::_MapExtentIsValidCacheInitialized)
			{
				model_internal::calculateMapExtentIsValid();
			}
			
			return model_internal::_MapExtentIsValid;
		}
		
		model_internal function calculateMapExtentIsValid():void
		{
			var valRes:ValidationResultEvent = model_internal::_MapExtentValidator.validate(model_internal::_instance.MapExtent)
			model_internal::_MapExtentIsValid_der = (valRes.results == null);
			model_internal::_MapExtentIsValidCacheInitialized = true;
			if (valRes.results == null)
				model_internal::MapExtentValidationFailureMessages_der = emptyArray;
			else
			{
				var _valFailures:Array = new Array();
				for (var a:int = 0 ; a<valRes.results.length ; a++)
				{
					_valFailures.push(valRes.results[a].errorMessage);
				}
				model_internal::MapExtentValidationFailureMessages_der = _valFailures;
			}
		}
		
		[Bindable(event="propertyChange")]
		public function get MapExtentValidationFailureMessages():Array
		{
			if (model_internal::_MapExtentValidationFailureMessages == null)
				model_internal::calculateMapExtentIsValid();
			
			return _MapExtentValidationFailureMessages;
		}
		
		model_internal function set MapExtentValidationFailureMessages_der(value:Array) : void
		{
			var oldValue:Array = model_internal::_MapExtentValidationFailureMessages;
			
			var needUpdate : Boolean = false;
			if (oldValue == null)
				needUpdate = true;
			
			// avoid firing the event when old and new value are different empty arrays
			if (!needUpdate && (oldValue !== value && (oldValue.length > 0 || value.length > 0)))
			{
				if (oldValue.length == value.length)
				{
					for (var a:int=0; a < oldValue.length; a++)
					{
						if (oldValue[a] !== value[a])
						{
							needUpdate = true;
							break;
						}
					}
				}
				else
				{
					needUpdate = true;
				}
			}
			
			if (needUpdate)
			{
				model_internal::_MapExtentValidationFailureMessages = value;   
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "MapExtentValidationFailureMessages", oldValue, value));
				// Only execute calculateIsValid if it has been called before, to update the validationFailureMessages for
				// the entire entity.
				if (model_internal::_instance.model_internal::_cacheInitialized_isValid)
				{
					model_internal::_instance.model_internal::isValid_der = model_internal::_instance.model_internal::calculateIsValid();
				}
			}
		}
		
		[Bindable(event="propertyChange")]   
		public function get MapServicesStyle():com.adobe.fiber.styles.Style
		{
			return model_internal::_nullStyle;
		}
		
		public function get MapServicesValidator() : StyleValidator
		{
			return model_internal::_MapServicesValidator;
		}
		
		model_internal function set _MapServicesIsValid_der(value:Boolean):void 
		{
			var oldValue:Boolean = model_internal::_MapServicesIsValid;         
			if (oldValue !== value)
			{
				model_internal::_MapServicesIsValid = value;
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "MapServicesIsValid", oldValue, value));
			}                             
		}
		
		[Bindable(event="propertyChange")]
		public function get MapServicesIsValid():Boolean
		{
			if (!model_internal::_MapServicesIsValidCacheInitialized)
			{
				model_internal::calculateMapServicesIsValid();
			}
			
			return model_internal::_MapServicesIsValid;
		}
		
		model_internal function calculateMapServicesIsValid():void
		{
			var valRes:ValidationResultEvent = model_internal::_MapServicesValidator.validate(model_internal::_instance.MapServices)
			model_internal::_MapServicesIsValid_der = (valRes.results == null);
			model_internal::_MapServicesIsValidCacheInitialized = true;
			if (valRes.results == null)
				model_internal::MapServicesValidationFailureMessages_der = emptyArray;
			else
			{
				var _valFailures:Array = new Array();
				for (var a:int = 0 ; a<valRes.results.length ; a++)
				{
					_valFailures.push(valRes.results[a].errorMessage);
				}
				model_internal::MapServicesValidationFailureMessages_der = _valFailures;
			}
		}
		
		[Bindable(event="propertyChange")]
		public function get MapServicesValidationFailureMessages():Array
		{
			if (model_internal::_MapServicesValidationFailureMessages == null)
				model_internal::calculateMapServicesIsValid();
			
			return _MapServicesValidationFailureMessages;
		}
		
		model_internal function set MapServicesValidationFailureMessages_der(value:Array) : void
		{
			var oldValue:Array = model_internal::_MapServicesValidationFailureMessages;
			
			var needUpdate : Boolean = false;
			if (oldValue == null)
				needUpdate = true;
			
			// avoid firing the event when old and new value are different empty arrays
			if (!needUpdate && (oldValue !== value && (oldValue.length > 0 || value.length > 0)))
			{
				if (oldValue.length == value.length)
				{
					for (var a:int=0; a < oldValue.length; a++)
					{
						if (oldValue[a] !== value[a])
						{
							needUpdate = true;
							break;
						}
					}
				}
				else
				{
					needUpdate = true;
				}
			}
			
			if (needUpdate)
			{
				model_internal::_MapServicesValidationFailureMessages = value;   
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "MapServicesValidationFailureMessages", oldValue, value));
				// Only execute calculateIsValid if it has been called before, to update the validationFailureMessages for
				// the entire entity.
				if (model_internal::_instance.model_internal::_cacheInitialized_isValid)
				{
					model_internal::_instance.model_internal::isValid_der = model_internal::_instance.model_internal::calculateIsValid();
				}
			}
		}
		
		[Bindable(event="propertyChange")]   
		public function get GraphicLayersStyle():com.adobe.fiber.styles.Style
		{
			return model_internal::_nullStyle;
		}
		
		public function get GraphicLayersValidator() : StyleValidator
		{
			return model_internal::_GraphicLayersValidator;
		}
		
		model_internal function set _GraphicLayersIsValid_der(value:Boolean):void 
		{
			var oldValue:Boolean = model_internal::_GraphicLayersIsValid;         
			if (oldValue !== value)
			{
				model_internal::_GraphicLayersIsValid = value;
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "GraphicLayersIsValid", oldValue, value));
			}                             
		}
		
		[Bindable(event="propertyChange")]
		public function get GraphicLayersIsValid():Boolean
		{
			if (!model_internal::_GraphicLayersIsValidCacheInitialized)
			{
				model_internal::calculateGraphicLayersIsValid();
			}
			
			return model_internal::_GraphicLayersIsValid;
		}
		
		model_internal function calculateGraphicLayersIsValid():void
		{
			var valRes:ValidationResultEvent = model_internal::_GraphicLayersValidator.validate(model_internal::_instance.GraphicLayers)
			model_internal::_GraphicLayersIsValid_der = (valRes.results == null);
			model_internal::_GraphicLayersIsValidCacheInitialized = true;
			if (valRes.results == null)
				model_internal::GraphicLayersValidationFailureMessages_der = emptyArray;
			else
			{
				var _valFailures:Array = new Array();
				for (var a:int = 0 ; a<valRes.results.length ; a++)
				{
					_valFailures.push(valRes.results[a].errorMessage);
				}
				model_internal::GraphicLayersValidationFailureMessages_der = _valFailures;
			}
		}
		
		[Bindable(event="propertyChange")]
		public function get GraphicLayersValidationFailureMessages():Array
		{
			if (model_internal::_GraphicLayersValidationFailureMessages == null)
				model_internal::calculateGraphicLayersIsValid();
			
			return _GraphicLayersValidationFailureMessages;
		}
		
		model_internal function set GraphicLayersValidationFailureMessages_der(value:Array) : void
		{
			var oldValue:Array = model_internal::_GraphicLayersValidationFailureMessages;
			
			var needUpdate : Boolean = false;
			if (oldValue == null)
				needUpdate = true;
			
			// avoid firing the event when old and new value are different empty arrays
			if (!needUpdate && (oldValue !== value && (oldValue.length > 0 || value.length > 0)))
			{
				if (oldValue.length == value.length)
				{
					for (var a:int=0; a < oldValue.length; a++)
					{
						if (oldValue[a] !== value[a])
						{
							needUpdate = true;
							break;
						}
					}
				}
				else
				{
					needUpdate = true;
				}
			}
			
			if (needUpdate)
			{
				model_internal::_GraphicLayersValidationFailureMessages = value;   
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "GraphicLayersValidationFailureMessages", oldValue, value));
				// Only execute calculateIsValid if it has been called before, to update the validationFailureMessages for
				// the entire entity.
				if (model_internal::_instance.model_internal::_cacheInitialized_isValid)
				{
					model_internal::_instance.model_internal::isValid_der = model_internal::_instance.model_internal::calculateIsValid();
				}
			}
		}
		
		[Bindable(event="propertyChange")]   
		public function get CreatedTimeStyle():com.adobe.fiber.styles.Style
		{
			return model_internal::_nullStyle;
		}
		
		public function get CreatedTimeValidator() : StyleValidator
		{
			return model_internal::_CreatedTimeValidator;
		}
		
		model_internal function set _CreatedTimeIsValid_der(value:Boolean):void 
		{
			var oldValue:Boolean = model_internal::_CreatedTimeIsValid;         
			if (oldValue !== value)
			{
				model_internal::_CreatedTimeIsValid = value;
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "CreatedTimeIsValid", oldValue, value));
			}                             
		}
		
		[Bindable(event="propertyChange")]
		public function get CreatedTimeIsValid():Boolean
		{
			if (!model_internal::_CreatedTimeIsValidCacheInitialized)
			{
				model_internal::calculateCreatedTimeIsValid();
			}
			
			return model_internal::_CreatedTimeIsValid;
		}
		
		model_internal function calculateCreatedTimeIsValid():void
		{
			var valRes:ValidationResultEvent = model_internal::_CreatedTimeValidator.validate(model_internal::_instance.CreatedTime)
			model_internal::_CreatedTimeIsValid_der = (valRes.results == null);
			model_internal::_CreatedTimeIsValidCacheInitialized = true;
			if (valRes.results == null)
				model_internal::CreatedTimeValidationFailureMessages_der = emptyArray;
			else
			{
				var _valFailures:Array = new Array();
				for (var a:int = 0 ; a<valRes.results.length ; a++)
				{
					_valFailures.push(valRes.results[a].errorMessage);
				}
				model_internal::CreatedTimeValidationFailureMessages_der = _valFailures;
			}
		}
		
		[Bindable(event="propertyChange")]
		public function get CreatedTimeValidationFailureMessages():Array
		{
			if (model_internal::_CreatedTimeValidationFailureMessages == null)
				model_internal::calculateCreatedTimeIsValid();
			
			return _CreatedTimeValidationFailureMessages;
		}
		
		model_internal function set CreatedTimeValidationFailureMessages_der(value:Array) : void
		{
			var oldValue:Array = model_internal::_CreatedTimeValidationFailureMessages;
			
			var needUpdate : Boolean = false;
			if (oldValue == null)
				needUpdate = true;
			
			// avoid firing the event when old and new value are different empty arrays
			if (!needUpdate && (oldValue !== value && (oldValue.length > 0 || value.length > 0)))
			{
				if (oldValue.length == value.length)
				{
					for (var a:int=0; a < oldValue.length; a++)
					{
						if (oldValue[a] !== value[a])
						{
							needUpdate = true;
							break;
						}
					}
				}
				else
				{
					needUpdate = true;
				}
			}
			
			if (needUpdate)
			{
				model_internal::_CreatedTimeValidationFailureMessages = value;   
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "CreatedTimeValidationFailureMessages", oldValue, value));
				// Only execute calculateIsValid if it has been called before, to update the validationFailureMessages for
				// the entire entity.
				if (model_internal::_instance.model_internal::_cacheInitialized_isValid)
				{
					model_internal::_instance.model_internal::isValid_der = model_internal::_instance.model_internal::calculateIsValid();
				}
			}
		}
		
		[Bindable(event="propertyChange")]   
		public function get LastModifiedStyle():com.adobe.fiber.styles.Style
		{
			return model_internal::_nullStyle;
		}
		
		public function get LastModifiedValidator() : StyleValidator
		{
			return model_internal::_LastModifiedValidator;
		}
		
		model_internal function set _LastModifiedIsValid_der(value:Boolean):void 
		{
			var oldValue:Boolean = model_internal::_LastModifiedIsValid;         
			if (oldValue !== value)
			{
				model_internal::_LastModifiedIsValid = value;
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "LastModifiedIsValid", oldValue, value));
			}                             
		}
		
		[Bindable(event="propertyChange")]
		public function get LastModifiedIsValid():Boolean
		{
			if (!model_internal::_LastModifiedIsValidCacheInitialized)
			{
				model_internal::calculateLastModifiedIsValid();
			}
			
			return model_internal::_LastModifiedIsValid;
		}
		
		model_internal function calculateLastModifiedIsValid():void
		{
			var valRes:ValidationResultEvent = model_internal::_LastModifiedValidator.validate(model_internal::_instance.LastModified)
			model_internal::_LastModifiedIsValid_der = (valRes.results == null);
			model_internal::_LastModifiedIsValidCacheInitialized = true;
			if (valRes.results == null)
				model_internal::LastModifiedValidationFailureMessages_der = emptyArray;
			else
			{
				var _valFailures:Array = new Array();
				for (var a:int = 0 ; a<valRes.results.length ; a++)
				{
					_valFailures.push(valRes.results[a].errorMessage);
				}
				model_internal::LastModifiedValidationFailureMessages_der = _valFailures;
			}
		}
		
		[Bindable(event="propertyChange")]
		public function get LastModifiedValidationFailureMessages():Array
		{
			if (model_internal::_LastModifiedValidationFailureMessages == null)
				model_internal::calculateLastModifiedIsValid();
			
			return _LastModifiedValidationFailureMessages;
		}
		
		model_internal function set LastModifiedValidationFailureMessages_der(value:Array) : void
		{
			var oldValue:Array = model_internal::_LastModifiedValidationFailureMessages;
			
			var needUpdate : Boolean = false;
			if (oldValue == null)
				needUpdate = true;
			
			// avoid firing the event when old and new value are different empty arrays
			if (!needUpdate && (oldValue !== value && (oldValue.length > 0 || value.length > 0)))
			{
				if (oldValue.length == value.length)
				{
					for (var a:int=0; a < oldValue.length; a++)
					{
						if (oldValue[a] !== value[a])
						{
							needUpdate = true;
							break;
						}
					}
				}
				else
				{
					needUpdate = true;
				}
			}
			
			if (needUpdate)
			{
				model_internal::_LastModifiedValidationFailureMessages = value;   
				this.dispatchEvent(mx.events.PropertyChangeEvent.createUpdateEvent(this, "LastModifiedValidationFailureMessages", oldValue, value));
				// Only execute calculateIsValid if it has been called before, to update the validationFailureMessages for
				// the entire entity.
				if (model_internal::_instance.model_internal::_cacheInitialized_isValid)
				{
					model_internal::_instance.model_internal::isValid_der = model_internal::_instance.model_internal::calculateIsValid();
				}
			}
		}
		
		
		/**
		 * 
		 * @inheritDoc 
		 */ 
		override public function getStyle(propertyName:String):com.adobe.fiber.styles.IStyle
		{
			switch(propertyName)
			{
				default:
				{
					return null;
				}
			}
		}
		
		/**
		 * 
		 * @inheritDoc 
		 *  
		 */  
		override public function getPropertyValidationFailureMessages(propertyName:String):Array
		{
			switch(propertyName)
			{
				case("WorkspaceID"):
				{
					return WorkspaceIDValidationFailureMessages;
				}
				case("Title"):
				{
					return TitleValidationFailureMessages;
				}
				case("Description"):
				{
					return DescriptionValidationFailureMessages;
				}
				case("MapExtent"):
				{
					return MapExtentValidationFailureMessages;
				}
				case("MapServices"):
				{
					return MapServicesValidationFailureMessages;
				}
				case("GraphicLayers"):
				{
					return GraphicLayersValidationFailureMessages;
				}
				case("CreatedTime"):
				{
					return CreatedTimeValidationFailureMessages;
				}
				case("LastModified"):
				{
					return LastModifiedValidationFailureMessages;
				}
				default:
				{
					return emptyArray;
				}
			}
		}
		
	}
	
}