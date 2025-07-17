package com.controls.validators
{
	
	import flash.display.DisplayObject;
	
	import mx.collections.ArrayCollection;
	import mx.controls.RadioButtonGroup;
	import mx.core.UIComponent;
	import mx.effects.Effect;
	import mx.effects.Glow;
	import mx.events.ValidationResultEvent;
	import mx.styles.StyleManager;
	import mx.validators.IValidator;
	import mx.validators.Validator;
    
    public class ValidatorsGroup extends ArrayCollection
    {
		private var _errorEffect:Effect;
		
        public function validate(useAnimation:Boolean = true):Boolean
        {
            if (length == 0)
                return true;

            var result:Boolean = true;

            var animatedControls:Array = [];
	
            for each (var item:* in this)
            {
                var validator:IValidator = item as IValidator;
                
                if (validator && validator.enabled && 
                    validator.validate().type == ValidationResultEvent.INVALID)
                {
                    result = false;
					
					if(validator is StartEndDateValidator)
                    {
						if(StartEndDateValidator(validator).startDateSource.errorString)
                    		animatedControls.push(StartEndDateValidator(validator).startDateSource);
						if(StartEndDateValidator(validator).endDateSource.errorString)
                    		animatedControls.push(StartEndDateValidator(validator).endDateSource);
                    }
                    else if (validator['source'] is DisplayObject)
                    {
                        animatedControls.push(validator['source']);
                    }
                }
            }

            if (!result && useAnimation && animatedControls.length > 0)
            {
                errorEffect.end();
                errorEffect.play(animatedControls);
            }

            return result;
        }
        
		protected function set errorEffect(value:Effect):void
		{
			_errorEffect = value;
		}
		
		protected function get errorEffect():Effect
		{
			if (!_errorEffect) 
			{
				_errorEffect = new Glow();
				Glow(errorEffect).color = 0xF7291E;
			}
			
			return _errorEffect;
		}
   }
}