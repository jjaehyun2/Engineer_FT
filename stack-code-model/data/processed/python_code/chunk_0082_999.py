package com.controls.validators
{
	import flash.events.Event;
	
	import mx.core.UIComponent;
	import mx.effects.Effect;
	import mx.effects.Glow;
	import mx.events.ValidationResultEvent;
	import mx.styles.IStyleManager2;
	import mx.styles.StyleManager;
	import mx.validators.DateValidator;
	import mx.validators.ValidationResult;
	import mx.validators.Validator;
	
	[Exclude(kind="property", name="source")]
	[Exclude(kind="property", name="property")]
	[Exclude(kind="property", name="required")]
	public class StartEndDateValidator extends DateValidator
	{
		private static const START_DATE_CONTROL:int = 1;
		private static const END_DATE_CONTROL:int = 1;
		private static const BOTH_CONTROLS:int = 1;
		
		private var _startDateSource:Object;
		private var _startDateProperty:String;
		
		private var _endDateSource:Object;
		private var _endDateProperty:String;

		public var startDateRequired:Boolean = false;
		public var endDateRequired:Boolean = false;
		
		public function StartEndDateValidator()
		{
			super(); 
		}
		
		public function get startDateSource():Object
		{
			return _startDateSource;
		}

		public function set startDateSource(value:Object):void
		{
			_startDateSource = value;
		}

		public function get startDateProperty():String
		{
			return _startDateProperty;
		}

		public function set startDateProperty(value:String):void
		{
			_startDateProperty = value;
		}

		public function get endDateSource():Object
		{
			return _endDateSource;
		}

		public function set endDateSource(value:Object):void
		{
			_endDateSource = value;
		}

		public function get endDateProperty():String
		{
			return _endDateProperty;
		}

		public function set endDateProperty(value:String):void
		{
			_endDateProperty = value;
		}

		protected override function doValidation(value:Object):Array
		{
			var validatorResults:Array = new Array();   
			var msg:String = ""; 
			
			if(!value.startDate && startDateRequired)
			{
				msg = "Start Date is required."
				validatorResults.push(new ValidationResult(true, null, "Invalid Date Range", msg));
				setErrorString(msg, [startDateSource]);
			}
			else
				setErrorString("", [startDateSource]);
			
			if(!value.endDate && endDateRequired)
			{
				msg = "End Date is required.";
				validatorResults.push(new ValidationResult(true, null, "Invalid Date Range", msg));
				setErrorString(msg, [endDateSource]);
			}
			else
				setErrorString("", [endDateSource]);
			
			if(validatorResults.length > 0)
				return validatorResults;
			
			if((!value.startDate && !value.endDate) || (value.startDate && !value.endDate))
			{
				setErrorString("", [startDateSource, endDateSource]);
				return validatorResults;
			}
			
			if(!value.startDate && value.endDate)
			{
				msg = "Start Date is not set.";
				validatorResults.push(new ValidationResult(true, null, "Invalid Date Range", msg));
				setErrorString(msg, [startDateSource]);
			}
			else
				setErrorString("", [startDateSource]);
			
			if (value.endDate && value.startDate && 
				value.endDate.getTime() < value.startDate.getTime()) 
			{
				msg = "End Date is less then Start Date";
 				validatorResults.push(new ValidationResult(true, null, "Invalid Date Range", msg));
				setErrorString(msg, [endDateSource]);
			}
			else
				setErrorString("", [endDateSource]);
			
			return validatorResults;
		}
		
		protected function setErrorString(errorString:String, components:Array):void
		{
			for each(var component:UIComponent in components)
			{
				component.errorString = errorString;
			}
		}
		
		protected override function getValueFromSource():Object
		{
			var value:Object = {};
			
			value.startDate = startDateSource && startDateSource.hasOwnProperty(startDateProperty) ? startDateSource[startDateProperty] : null;  
			value.endDate = endDateSource && endDateSource.hasOwnProperty(endDateProperty) ? endDateSource[endDateProperty] : null;
			
			return value;
		}
		
	}
}