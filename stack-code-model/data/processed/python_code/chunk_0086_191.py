dynamic class tm.freshComponents.forms.formItems.FormItemsFactory
{

    function FormItemsFactory()
    {
    }

    static function create(type, formManager, id, label, required)
    {
        if ((__reg0 = type) === tm.freshComponents.forms.formItems.FormItemType.TEXT) 
        {
            return new tm.freshComponents.forms.formItems.TextItem(formManager, id, label, required);
            return;
        }
        else 
        {
            if (__reg0 === tm.freshComponents.forms.formItems.FormItemType.SELECT) 
            {
                return new tm.freshComponents.forms.formItems.SelectItem(formManager, id, label, required);
                return;
            }
            else 
            {
                if (__reg0 === tm.freshComponents.forms.formItems.FormItemType.CHECKBOX) 
                {
                    return new tm.freshComponents.forms.formItems.CheckboxItem(formManager, id, label, required);
                    return;
                }
                else 
                {
                    if (__reg0 !== tm.freshComponents.forms.formItems.FormItemType.RADIOBUTTON) 
                    {
                        return new tm.freshComponents.forms.formItems.TextItem(formManager, id, label, required);
                        return;
                    }
                }
            }
        }
        return new tm.freshComponents.forms.formItems.RadiobuttonItem(formManager, id, label, required);
        return;
    }

}