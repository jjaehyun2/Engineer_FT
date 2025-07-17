dynamic class tm.freshComponents.forms.validators.EmailValidator implements tm.freshComponents.forms.validators.IFormValidator
{
    var minLettersAfterLastPoint: Number = 2;
    var maxLettersAfterLastPoint: Number = 4;
    var minLettersBeforeAt: Number = 2;
    var maxLettersBeforeAt: Number = 20;
    static var emailNotValidError: String = "emailNotValid";
    var _validationErrorMessage;

    function EmailValidator()
    {
    }

    function updateProperties(data)
    {
        if (data.minLettersAfterLastPoint.value && Number(data.minLettersAfterLastPoint.value) > 0) 
        {
            this.minLettersAfterLastPoint = data.minLettersAfterLastPoint.value;
        }
        if (data.maxLettersAfterLastPoint.value && Number(data.maxLettersAfterLastPoint.value) > 0) 
        {
            this.maxLettersAfterLastPoint = data.maxLettersAfterLastPoint.value;
        }
        if (data.minLettersBeforeAt.value && Number(data.minLettersBeforeAt.value) > 0) 
        {
            this.minLettersBeforeAt = data.minLettersBeforeAt.value;
        }
        if (data.maxLettersBeforeAt.value && Number(data.maxLettersBeforeAt.value) > 0) 
        {
            this.maxLettersBeforeAt = data.maxLettersBeforeAt.value;
        }
    }

    function validate(value)
    {
        var __reg2 = String(value);
        if (__reg2.length > 0) 
        {
            var __reg5 = __reg2.substring(0, 1);
            if (!isNaN(__reg5) || __reg5 == "." || __reg5 == "-" || __reg5 == "_") 
            {
                this._validationErrorMessage = tm.freshComponents.forms.validators.EmailValidator.emailNotValidError;
                return false;
            }
            var __reg4 = __reg2.substring(__reg2.length, -1);
            if (!isNaN(__reg4) || __reg4 == "." || __reg4 == "-" || __reg4 == "_") 
            {
                this._validationErrorMessage = tm.freshComponents.forms.validators.EmailValidator.emailNotValidError;
                return false;
            }
            var __reg17 = this.maxLettersAfterLastPoint;
            var __reg3 = __reg2.indexOf("@", 0);
            var __reg20 = __reg2.lastIndexOf("@", __reg2.length);
            if (__reg3 == -1 || __reg3 >= __reg2.length - __reg17 || __reg3 == 0 || __reg3 !== __reg20) 
            {
                this._validationErrorMessage = tm.freshComponents.forms.validators.EmailValidator.emailNotValidError;
                return false;
            }
            var __reg23 = __reg2.indexOf(".", 0);
            var __reg6 = __reg2.lastIndexOf(".", __reg2.length);
            if (__reg23 == 0 || __reg6 == -1) 
            {
                this._validationErrorMessage = tm.freshComponents.forms.validators.EmailValidator.emailNotValidError;
                return false;
            }
            var __reg13 = __reg2.length - __reg6 - 1;
            if (__reg13 < this.minLettersAfterLastPoint || __reg13 > this.maxLettersAfterLastPoint) 
            {
                this._validationErrorMessage = tm.freshComponents.forms.validators.EmailValidator.emailNotValidError;
                return false;
            }
            var __reg7 = __reg2.charAt(__reg3 - 1);
            var __reg11 = __reg2.charAt(__reg3 + 1);
            if (__reg7 == "." || __reg7 == "_" || __reg7 == "-" || __reg11 == "." || __reg11 == "_" || __reg11 == "-") 
            {
                this._validationErrorMessage = tm.freshComponents.forms.validators.EmailValidator.emailNotValidError;
                return false;
            }
            var __reg14 = __reg2.indexOf("-", 0);
            var __reg8 = __reg2.charAt(__reg14 - 1);
            var __reg12 = __reg2.charAt(__reg14 + 1);
            var __reg15 = __reg2.indexOf("_", 0);
            var __reg9 = __reg2.charAt(__reg15 - 1);
            var __reg10 = __reg2.charAt(__reg15 + 1);
            if (__reg8 == "." || __reg8 == "_" || __reg8 == "@" || __reg12 == "." || __reg12 == "_" || __reg12 == "@" || __reg9 == "." || __reg9 == "-" || __reg9 == "@" || __reg10 == "." || __reg10 == "-" || __reg10 == "@") 
            {
                this._validationErrorMessage = tm.freshComponents.forms.validators.EmailValidator.emailNotValidError;
                return false;
            }
            var __reg16 = __reg2.substring(0, __reg3);
            var __reg18 = __reg2.indexOf("..", 0);
            var __reg19 = __reg2.indexOf("--", 0);
            var __reg21 = __reg2.indexOf("-", __reg6);
            var __reg22 = __reg2.indexOf("_", __reg6);
            if (__reg18 !== -1 || __reg19 !== -1 || __reg21 !== -1 || __reg22 !== -1 || __reg16.length < this.minLettersBeforeAt || __reg16.length > this.maxLettersBeforeAt) 
            {
                this._validationErrorMessage = tm.freshComponents.forms.validators.EmailValidator.emailNotValidError;
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