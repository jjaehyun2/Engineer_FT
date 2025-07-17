dynamic class tm.freshComponents.forms.FormManager
{
    var buttonsOutLabel;
    var buttonsOverLabel;
    var gotoAndPlay;
    var itemsCollection;
    var itemsGroups;
    var labelRollOut;
    var labelRollOver;
    var resetButton;
    var submitButton;
    var submitFormOnEnter;
    var validateRequiredOnly;

    function FormManager()
    {
        this.itemsCollection = new Array();
        this.itemsGroups = new Array();
    }

    function init()
    {
        var tabItems = new Array();
        this.itemsCollection.sortOn("id", Array.NUMERIC);
        var i = 0;
        while (i < this.itemsCollection.length) 
        {
            if (tm.freshComponents.forms.formItems.FormItem(this.itemsCollection[i]) && tm.freshComponents.forms.formItems.FormItem(this.itemsCollection[i]).__get__target()) 
            {
                var item = eval(String(tm.freshComponents.forms.formItems.FormItem(this.itemsCollection[i]).__get__target()));
                item._focusrect = false;
                item.tabEnabled = true;
                tabItems.push(item);
                tm.freshComponents.forms.formItems.FormItem(this.itemsCollection[i]).init();
            }
            ++i;
        }
        if (this.submitButton) 
        {
            this.submitButton._focusrect = false;
            this.submitButton.tabEnabled = true;
            tabItems.push(this.submitButton);
            this.submitButton.labelRollOver = this.buttonsOverLabel;
            this.submitButton.labelRollOut = this.buttonsOutLabel;
            this.submitButton.onRollOver = function ()
            {
                this.gotoAndPlay(this.labelRollOver);
            }
            ;
            this.submitButton.onRollOut = function ()
            {
                this.gotoAndPlay(this.labelRollOut);
            }
            ;
            this.submitButton.onSetFocus = function ()
            {
                this.gotoAndPlay(this.labelRollOver);
            }
            ;
            this.submitButton.onKillFocus = function ()
            {
                this.gotoAndPlay(this.labelRollOut);
            }
            ;
            this.submitButton.onRelease = tm.utils.Delegate.create(this, this.submitForm);
        }
        if (this.resetButton) 
        {
            this.resetButton._focusrect = false;
            this.resetButton.tabEnabled = true;
            tabItems.push(this.resetButton);
            this.resetButton.labelRollOver = this.buttonsOverLabel;
            this.resetButton.labelRollOut = this.buttonsOutLabel;
            this.resetButton.onRollOver = function ()
            {
                this.gotoAndPlay(this.labelRollOver);
            }
            ;
            this.resetButton.onRollOut = function ()
            {
                this.gotoAndPlay(this.labelRollOut);
            }
            ;
            this.resetButton.onSetFocus = function ()
            {
                this.gotoAndPlay(this.labelRollOver);
            }
            ;
            this.resetButton.onKillFocus = function ()
            {
                this.gotoAndPlay(this.labelRollOut);
            }
            ;
            this.resetButton.onRelease = tm.utils.Delegate.create(this, this.resetForm);
        }
        tm.freshComponents.tabFixer.TabManager.getInstance().registerTabFixer(tabItems, "onEnterKeyPress", this);
    }

    function addNewItem(item)
    {
        if (item.id && item.label && item.label.length > 0) 
        {
            var __reg3 = tm.freshComponents.forms.formItems.FormItemsFactory.create(item.type, this, item.id, item.label, item.required);
            __reg3.updateParameters(item);
            this.itemsCollection.push(__reg3);
        }
    }

    function submitForm()
    {
        if (this.validate(this.validateRequiredOnly)) 
        {
            this.onValidFormSubmit();
        }
        tm.freshComponents.tabFixer.TabManager.getInstance().removeFocus();
    }

    function resetForm()
    {
        var __reg2 = 0;
        while (__reg2 < this.itemsCollection.length) 
        {
            tm.freshComponents.forms.formItems.FormItem(this.itemsCollection[__reg2]).reset();
            ++__reg2;
        }
        this.onFormReset();
        tm.freshComponents.tabFixer.TabManager.getInstance().removeFocus();
    }

    function validate(requiredOnly)
    {
        var __reg2 = undefined;
        __reg2 = 0;
        while (__reg2 < this.itemsCollection.length) 
        {
            var __reg3 = tm.freshComponents.forms.formItems.FormItem(this.itemsCollection[__reg2]);
            if (!requiredOnly || requiredOnly && __reg3.__get__required()) 
            {
                if (!__reg3.validate()) 
                {
                    this.onValidationError(__reg3, __reg3.validationError);
                    return false;
                    break;
                }
            }
            ++__reg2;
        }
        __reg2 = 0;
        while (__reg2 < this.itemsGroups.length) 
        {
            var __reg4 = tm.freshComponents.forms.formItems.FormItemsGroup(this.itemsGroups[__reg2]);
            if (!__reg4.validate()) 
            {
                this.onFormGroupValidationError(__reg4, __reg4.validationError);
                return false;
                break;
            }
            ++__reg2;
        }
        return true;
    }

    function getFormItem(id)
    {
        var __reg2 = 0;
        while (__reg2 < this.itemsCollection.length) 
        {
            if (this.itemsCollection[__reg2].id == id) 
            {
                return this.itemsCollection[__reg2];
            }
            ++__reg2;
        }
        return undefined;
    }

    function getFormData()
    {
        var __reg6 = new Array();
        var __reg7 = new Array();
        var __reg4 = 0;
        while (__reg4 < this.itemsCollection.length) 
        {
            var __reg2 = tm.freshComponents.forms.formItems.FormItem(this.itemsCollection[__reg4]);
            var __reg3 = __reg2.__get__label();
            var __reg5 = __reg2.getValue();
            if (__reg2.__get__group() && this.isValidItemsGroup(__reg2.__get__group().name)) 
            {
                if (!tm.utils.Utils.inArray(__reg2.__get__group().name, __reg7)) 
                {
                    __reg7.push(__reg2.__get__group().name);
                    __reg3 = __reg2.__get__group().name;
                    __reg5 = __reg2.__get__group().getData();
                    __reg6.push({key: __reg3, value: __reg5, id: __reg2.__get__id()});
                }
            }
            else 
            {
                if (__reg2.__get__type() != tm.freshComponents.forms.formItems.FormItemType.RADIOBUTTON) 
                {
                    if (__reg2.__get__type() == tm.freshComponents.forms.formItems.FormItemType.CHECKBOX) 
                    {
                        __reg5 = __reg5 == "true" ? "yes" : "no";
                    }
                    __reg6.push({key: __reg3, value: __reg5, id: __reg2.__get__id()});
                }
            }
            ++__reg4;
        }
        return __reg6;
    }

    function registerItemsGroup(formItem, groupName, groupParameters)
    {
        var __reg3 = this.isValidItemsGroup(groupName);
        if (__reg3) 
        {
            __reg3.addNewItem(formItem);
            return __reg3;
            return;
        }
        var __reg2 = new tm.freshComponents.forms.formItems.FormItemsGroup(groupName, groupParameters);
        __reg2.addNewItem(formItem);
        this.itemsGroups.push(__reg2);
        return __reg2;
    }

    function isValidItemsGroup(groupName)
    {
        var __reg2 = 0;
        while (__reg2 < this.itemsGroups.length) 
        {
            if (tm.freshComponents.forms.formItems.FormItemsGroup(this.itemsGroups[__reg2]).name == groupName) 
            {
                return tm.freshComponents.forms.formItems.FormItemsGroup(this.itemsGroups[__reg2]);
            }
            ++__reg2;
        }
        return null;
    }

    function onEnterKeyPress(target)
    {
        if (target == this.resetButton) 
        {
            this.resetForm();
            return;
        }
        if (this.submitFormOnEnter || target == this.submitButton) 
        {
            this.submitForm();
        }
    }

    function onValidationError(formItem, validationError)
    {
    }

    function onFormGroupValidationError(group, validationError)
    {
    }

    function onValidFormSubmit()
    {
    }

    function onFormReset()
    {
    }

}