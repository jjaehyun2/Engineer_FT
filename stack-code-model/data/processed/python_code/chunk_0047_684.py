dynamic class tm.freshComponents.forms.validators.DateValidator implements tm.freshComponents.forms.validators.IFormValidator
{
    var mask: String = "mm/dd/yyyy";
    var daysIndex: Number = 3;
    var monthsIndex: Number = 0;
    var yearsIndex: Number = 6;
    var dateIsNotValidError: String = "dateIsNotValidError";
    var _validationErrorMessage;
    var maxDateAllowed;
    var minDateAllowed;

    function DateValidator()
    {
    }

    function updateProperties(data)
    {
        if (data.mask.value && String(data.mask.value).length > 0) 
        {
            var __reg3 = String(data.mask.value);
            if (__reg3.indexOf("dd") != -1 && __reg3.indexOf("mm") != -1 && __reg3.indexOf("yyyy") != -1) 
            {
                this.mask = __reg3;
                this.daysIndex = __reg3.indexOf("dd");
                this.monthsIndex = __reg3.indexOf("mm");
                this.yearsIndex = __reg3.indexOf("yyyy");
            }
        }
        if (data.minDateAllowed.value && String(data.minDateAllowed.value).length > 0) 
        {
            var __reg4 = String(data.minDateAllowed.value);
            if (this.checkDateByMask(__reg4)) 
            {
                this.minDateAllowed = __reg4;
            }
        }
        if (data.maxDateAllowed.value && String(data.maxDateAllowed.value).length > 0) 
        {
            var __reg5 = String(data.maxDateAllowed.value);
            if (this.checkDateByMask(__reg5)) 
            {
                this.maxDateAllowed = __reg5;
            }
        }
    }

    function checkDateByMask(dateString)
    {
        var __reg8 = Number(dateString.substr(this.daysIndex, 2));
        var __reg5 = Number(dateString.substr(this.monthsIndex, 2));
        var __reg9 = Number(dateString.substr(this.yearsIndex, 4));
        var __reg11 = 1;
        var __reg15 = 31;
        var __reg13 = 1;
        var __reg16 = 12;
        var __reg12 = 1950;
        var __reg14 = 2100;
        if (this.minDateAllowed && this.minDateAllowed.length > 0) 
        {
            var __reg7 = Number(this.minDateAllowed.substr(this.daysIndex, 2));
            var __reg6 = Number(this.minDateAllowed.substr(this.monthsIndex, 2));
            var __reg10 = Number(this.minDateAllowed.substr(this.yearsIndex, 4));
            if (__reg7 && __reg7 > 1 && __reg7 < 31) 
            {
                __reg11 = __reg7;
            }
            if (__reg6 && __reg6 > 1 && __reg6 < 31) 
            {
                __reg13 = __reg6;
            }
            if (__reg10 && __reg10 > 1950 && __reg10 < 2100) 
            {
                __reg12 = __reg10;
            }
        }
        if (this.maxDateAllowed && this.maxDateAllowed.length > 0) 
        {
            var __reg4 = Number(this.maxDateAllowed.substr(this.daysIndex, 2));
            var __reg2 = Number(this.maxDateAllowed.substr(this.monthsIndex, 2));
            var __reg3 = Number(this.maxDateAllowed.substr(this.yearsIndex, 4));
            if (__reg4 && __reg4 > 1 && __reg4 < 31 && __reg4 > __reg11) 
            {
                __reg15 = __reg4;
            }
            if (__reg2 && __reg2 > 1 && __reg2 < 31 && __reg2 > __reg13) 
            {
                __reg16 = __reg2;
            }
            if (__reg3 && __reg3 > 1950 && __reg3 < 2100 && __reg3 > __reg12) 
            {
                __reg14 = __reg3;
            }
        }
        if (!__reg8 || isNaN(__reg8) || __reg8 < __reg11 || __reg8 > __reg15) 
        {
            this._validationErrorMessage = this.dateIsNotValidError;
            return false;
        }
        if (!__reg5 || isNaN(__reg5) || __reg5 < __reg13 || __reg5 > __reg16) 
        {
            this._validationErrorMessage = this.dateIsNotValidError;
            return false;
        }
        if (!__reg9 || isNaN(__reg9) || __reg9 < __reg12 || __reg9 > __reg14) 
        {
            this._validationErrorMessage = this.dateIsNotValidError;
            return false;
        }
        return true;
    }

    function validate(value)
    {
        var __reg2 = String(value);
        return this.checkDateByMask(__reg2);
    }

    function error()
    {
        return this._validationErrorMessage;
    }

}