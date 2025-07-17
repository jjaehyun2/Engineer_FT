dynamic class tm.freshComponents.forms.validators.StringValidator implements tm.freshComponents.forms.validators.IFormValidator
{
    var minChars: Number = 0;
    var pattern: String = "";
    var flags: String = "";
    var minCharsLimitError: String = "minCharsLimitError";
    var reqExpError: String = "reqExpError";
    var _validationErrorMessage;
    var regExp;

    function StringValidator()
    {
    }

    function updateProperties(data)
    {
        if (data.minChars.value && Number(data.minChars.value) > 0) 
        {
            this.minChars = data.minChars.value;
        }
        if (data.reqExp.value && String(data.reqExp.value).length > 0) 
        {
            this.pattern = data.reqExp.value;
            if (data.reqExpFlags.value && String(data.reqExpFlags.value).length > 0) 
            {
                this.flags = data.reqExpFlags.value;
            }
            this.regExp = new tm.utils.RegExp(this.pattern, this.flags);
        }
    }

    function validate(value)
    {
        var __reg2 = String(value);
        if (__reg2.length < this.minChars) 
        {
            this._validationErrorMessage = this.minCharsLimitError;
            return false;
        }
        if (this.pattern && this.pattern.length > 0 && this.regExp) 
        {
            var __reg3 = this.regExp.test(__reg2);
            if (!__reg3) 
            {
                this._validationErrorMessage = this.reqExpError;
                return false;
            }
        }
        return true;
    }

    function error()
    {
        return this._validationErrorMessage;
    }

}