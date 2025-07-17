dynamic class tm.freshComponents.forms.formItems.SelectItem extends tm.freshComponents.forms.formItems.FormItem
{
    var depth: Number = 1;
    var _formManager;
    var _listeners;
    var _rawData;
    var _target;
    var _type;
    var dataProvider;
    var dependence;
    var fieldRequiredError;
    var firstItem;
    var updateGroups;
    var validationError;

    function SelectItem(formManager, id, label, required)
    {
        super(formManager, id, label, required);
        this._type = tm.freshComponents.forms.formItems.FormItemType.SELECT;
        this._listeners = new Array();
    }

    function updateParameters(data)
    {
        if (data.firstItem.value && data.firstItem.value.length > 0) 
        {
            this.firstItem = data.firstItem.value;
        }
        if (data.dataProvider.value) 
        {
            if (typeof data.dataProvider.value == "string") 
            {
                if (data.dataProvider.depth && Number(data.dataProvider.depth) > 1) 
                {
                    this.depth = data.dataProvider.depth;
                }
                if (data.dataProvider.dependence && Number(data.dataProvider.dependence) > 0) 
                {
                    this.dependence = data.dataProvider.dependence;
                }
                this.dataProvider = new Array();
                if (this.firstItem && this.firstItem.length > 0) 
                {
                    this.dataProvider.push({label: this.firstItem, data: this.firstItem});
                }
                var __reg4 = new tm.utils.XMLParser();
                __reg4.load(data.dataProvider.value, this, this.onXMLDataLoaded);
            }
            else 
            {
                this.dataProvider = new Array();
                if (this.firstItem && this.firstItem.length > 0) 
                {
                    this.dataProvider.push({label: this.firstItem, data: this.firstItem});
                }
                var __reg2 = 0;
                while (__reg2 < data.dataProvider.value.length) 
                {
                    this.dataProvider.push({label: data.dataProvider.value[__reg2].value, data: data.dataProvider.value[__reg2].value});
                    ++__reg2;
                }
                this.dependanceNodeDataChanged();
            }
        }
        this.updateGroups(data);
    }

    function onXMLDataLoaded(success, data)
    {
        if (success && data) 
        {
            this._rawData = data;
            var __reg3 = undefined;
            if (this.dependence) 
            {
                var __reg2 = tm.freshComponents.forms.formItems.SelectItem(this._formManager.getFormItem(this.dependence));
                __reg3 = __reg2.getValue();
                __reg2.registerForChange(this);
            }
            this.dependanceNodeDataChanged(__reg3);
            return;
        }
        mx.controls.ComboBox(this._target)._editable = false;
    }

    function getItemsAtDepth(dataCollection, targetDepth, dependanceNodeData)
    {
        var __reg6 = new Array();
        if (targetDepth > 0) 
        {
            var __reg2 = 0;
            while (__reg2 < dataCollection.length) 
            {
                if (dataCollection[__reg2].value != undefined && typeof dataCollection[__reg2].value == "string" && targetDepth == 1) 
                {
                    __reg6.push(dataCollection[__reg2].value);
                }
                else 
                {
                    if (dataCollection[__reg2].item && dataCollection[__reg2].item.length > 0 && targetDepth > 1) 
                    {
                        if (dependanceNodeData && dependanceNodeData.length > 0 && dataCollection[__reg2].data == dependanceNodeData || !dependanceNodeData || targetDepth != 2) 
                        {
                            __reg6 = __reg6.concat(this.getItemsAtDepth(dataCollection[__reg2].item, targetDepth - 1, dependanceNodeData));
                        }
                    }
                    else 
                    {
                        if (targetDepth == 1 && dataCollection[__reg2].data && dataCollection[__reg2].data.length > 0) 
                        {
                            __reg6.push(dataCollection[__reg2].data);
                        }
                    }
                }
                ++__reg2;
            }
        }
        return __reg6;
    }

    function dependanceNodeDataChanged(dependanceNodeData)
    {
        if (this._rawData) 
        {
            this.dataProvider = new Array();
            if (this.firstItem && this.firstItem.length > 0) 
            {
                this.dataProvider.push({label: this.firstItem, data: this.firstItem});
            }
            var __reg3 = this.getItemsAtDepth(this._rawData.item, this.depth, dependanceNodeData);
            var __reg2 = 0;
            while (__reg2 < __reg3.length) 
            {
                this.dataProvider.push({label: __reg3[__reg2], data: __reg3[__reg2]});
                ++__reg2;
            }
            mx.controls.ComboBox(this._target).dataProvider = this.dataProvider;
        }
    }

    function validate()
    {
        if (this.firstItem && this.firstItem.length > 0 && this.__get__required() && this.getValue() == this.firstItem) 
        {
            this.validationError = this.fieldRequiredError;
            return false;
        }
        return true;
    }

    function getValue()
    {
        var __reg2 = mx.controls.ComboBox(this._target).selectedItem;
        return __reg2.data;
    }

    function init()
    {
        var __reg3 = mx.controls.ComboBox(this._target);
        var __reg2 = new Object();
        __reg2.change = tm.utils.Delegate.create(this, this.onChange);
        __reg3.addEventListener("change", __reg2);
    }

    function onChange()
    {
        var __reg2 = 0;
        for (;;) 
        {
            if (__reg2 >= this._listeners.length) 
            {
                return;
            }
            tm.freshComponents.forms.formItems.SelectItem(this._listeners[__reg2]).dependanceNodeDataChanged(this.getValue());
            ++__reg2;
        }
    }

    function registerForChange(listener)
    {
        this._listeners.push(listener);
    }

    function reset()
    {
        mx.controls.ComboBox(this._target).selectedIndex = 0;
    }

    function get target()
    {
        return this._target;
    }

    function set target(targetObject)
    {
        this._target = targetObject;
        this.dependanceNodeDataChanged();
    }

}