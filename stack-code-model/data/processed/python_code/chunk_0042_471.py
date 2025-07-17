dynamic class tm.freshComponents.forms.formItems.TextItem extends tm.freshComponents.forms.formItems.FormItem
{
    var defaultValue: String = "";
    var textToShow: String = "";
    var password: Boolean = false;
    var _required;
    var _target;
    var _type;
    var fieldRequiredError;
    var maxChars;
    var restrict;
    var text;
    var updateGroups;
    var validationError;
    var validator;

    function TextItem(formManager, id, label, required)
    {
        super(formManager, id, label, required);
        this._type = tm.freshComponents.forms.formItems.FormItemType.TEXT;
    }

    function updateParameters(data)
    {
        if (data.defaultValue.value && data.defaultValue.value.length > 0) 
        {
            this.defaultValue = data.defaultValue.value;
        }
        if (data.textToShow.value && data.textToShow.value.length > 0) 
        {
            this.textToShow = data.textToShow.value;
        }
        if (data.validator.value && data.validator.value.length > 0) 
        {
            this.validator = tm.freshComponents.forms.validators.FormValidatorsFactory.create(data.validator.value);
            this.validator.updateProperties(data);
        }
        if (data.restrict.value && data.restrict.value.length > 0) 
        {
            this.restrict = data.restrict.value;
        }
        if (data.maxChars.value && data.maxChars.value.length > 0) 
        {
            this.maxChars = data.maxChars.value;
        }
        if (data.password.value && data.password.value == "true") 
        {
            this.password = true;
        }
        this.updateGroups(data);
    }

    function validate()
    {
        var __reg2 = this.getValue();
        if (this._required) 
        {
            if (!__reg2 || __reg2.length <= 0 || __reg2 == this.textToShow) 
            {
                this.validationError = this.fieldRequiredError;
                return false;
            }
        }
        if (this.validator && !this.validator.validate(__reg2)) 
        {
            this.validationError = this.validator.error();
            return false;
        }
        return true;
    }

    function getValue()
    {
        return TextField(this._target).text;
    }

    function init()
    {
        var __reg3 = TextField(this._target);
        __reg3.textToShow = this.textToShow;
        __reg3.onSetFocus = function ()
        {
            this;
            if (this.text == this.textToShow) 
            {
                this.text = "";
            }
        }
        ;
        __reg3.onKillFocus = function ()
        {
            this;
            if (this.text == "") 
            {
                this.text = this.textToShow;
            }
        }
        ;
        this.reset();
    }

    function reset()
    {
        var __reg2 = TextField(this._target);
        __reg2.text = this.textToShow;
        __reg2.hscroll = 0;
        __reg2.scroll = 0;
    }

    function get target()
    {
        return this._target;
    }

    function set target(targetObject)
    {
        this._target = targetObject;
        TextField(this._target).restrict = this.restrict;
        TextField(this._target).maxChars = this.maxChars;
        TextField(this._target).password = this.password;
    }

}