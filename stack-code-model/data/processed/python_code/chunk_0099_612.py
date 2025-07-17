dynamic class tm.freshComponents.forms.validators.FormValidatorsFactory
{

    function FormValidatorsFactory()
    {
    }

    static function create(type)
    {
        if ((__reg0 = type) === tm.freshComponents.forms.validators.FormValidatorType.STRING) 
        {
            return new tm.freshComponents.forms.validators.StringValidator();
            return;
        }
        else 
        {
            if (__reg0 === tm.freshComponents.forms.validators.FormValidatorType.NUMBER) 
            {
                return new tm.freshComponents.forms.validators.NumberValidator();
                return;
            }
            else 
            {
                if (__reg0 === tm.freshComponents.forms.validators.FormValidatorType.EMAIL) 
                {
                    return new tm.freshComponents.forms.validators.EmailValidator();
                    return;
                }
                else 
                {
                    if (__reg0 === tm.freshComponents.forms.validators.FormValidatorType.DATE) 
                    {
                        return new tm.freshComponents.forms.validators.DateValidator();
                        return;
                    }
                }
            }
        }
        return null;
    }

}