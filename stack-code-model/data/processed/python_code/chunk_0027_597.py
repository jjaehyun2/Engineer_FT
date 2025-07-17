dynamic class tm.freshComponents.forms.formItems.FormItem
{
    var _required: Boolean = false;
    var fieldRequiredError: String = "fieldIsRequired";
    var _formManager;
    var _group;
    var _id;
    var _label;
    var _target;
    var _type;

    function FormItem(formManager, id, label, required)
    {
        this._formManager = formManager;
        this._id = id;
        this._label = label;
        this._required = required;
    }

    function updateParameters(data)
    {
    }

    function updateGroups(data)
    {
        if (data.group.value && data.group.value.length > 0) 
        {
            this._group = this._formManager.registerItemsGroup(this, data.group.value, data.group);
        }
    }

    function validate()
    {
        return true;
    }

    function getValue()
    {
        return null;
    }

    function init()
    {
    }

    function reset()
    {
    }

    function get id()
    {
        return this._id;
    }

    function get label()
    {
        return this._label;
    }

    function get required()
    {
        return this._required;
    }

    function get type()
    {
        return this._type;
    }

    function get target()
    {
        return this._target;
    }

    function set target(targetObject)
    {
        this._target = targetObject;
    }

    function get group()
    {
        return this._group;
    }

}