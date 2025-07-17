dynamic class tm.freshComponents.tabFixer.TabManager
{
    var _noFocusMovieClip;
    var _targetObjects;
    var _targetObjectsHandlers;
    var _targetObjectsHandlersOwners;

    function TabManager()
    {
        this._targetObjects = new Array();
        this._targetObjectsHandlers = new Array();
        this._targetObjectsHandlersOwners = new Array();
        var __reg4 = new Object();
        __reg4.onKeyDown = tm.utils.Delegate.create(this, this.moveFocus);
        Key.addListener(__reg4);
        var __reg3 = new Object();
        __reg3.onMouseMove = tm.utils.Delegate.create(this, this.mouseMoved);
        Mouse.addListener(__reg3);
        this._noFocusMovieClip = _root.createEmptyMovieClip("dummyTabManagerMovie", _root.getNextHighestDepth());
        this._noFocusMovieClip.useHandCursor = false;
        this._noFocusMovieClip.onRelease = function ()
        {
        }
        ;
    }

    static function getInstance()
    {
        if (tm.freshComponents.tabFixer.TabManager._tabManager == undefined) 
        {
            tm.freshComponents.tabFixer.TabManager._tabManager = new tm.freshComponents.tabFixer.TabManager();
        }
        return tm.freshComponents.tabFixer.TabManager._tabManager;
    }

    function mouseMoved()
    {
    }

    function moveFocus()
    {
        if (Key.getCode() == 13) 
        {
            var selectedObject = eval(Selection.getFocus());
            var selectedObjectId = this.isItemPresent(Selection.getFocus(), this._targetObjects);
            if (this._targetObjectsHandlersOwners[selectedObjectId]) 
            {
                var eFunction = this._targetObjectsHandlersOwners[selectedObjectId][this._targetObjectsHandlers[selectedObjectId]];
                eFunction.apply(this._targetObjectsHandlersOwners[selectedObjectId], [selectedObject]);
                return;
            }
            var enterHandler = this._targetObjectsHandlers[selectedObjectId];
            if (enterHandler && enterHandler.length > 0) 
            {
                selectedObject[enterHandler](selectedObject);
            }
        }
    }

    function registerTabFixer(items, enterHandler, enterHandlerOwner)
    {
        var __reg2 = 0;
        while (__reg2 < items.length) 
        {
            if (this.isItemPresent(String(items[__reg2]), this._targetObjects) == -1) 
            {
                this._targetObjects.push(items[__reg2]);
                this._targetObjectsHandlers.push(enterHandler);
                this._targetObjectsHandlersOwners.push(enterHandlerOwner);
            }
            ++__reg2;
        }
        this.updateTabIndexes();
    }

    function unregisterTabFixer(items)
    {
        var __reg5 = new Array();
        var __reg4 = new Array();
        var __reg3 = new Array();
        var __reg2 = 0;
        while (__reg2 < this._targetObjects.length) 
        {
            if (this.isItemPresent(String(this._targetObjects[__reg2]), items) == -1) 
            {
                __reg5.push(this._targetObjects[__reg2]);
                __reg4.push(this._targetObjectsHandlers[__reg2]);
                __reg3.push(this._targetObjectsHandlersOwners[__reg2]);
            }
            ++__reg2;
        }
        this._targetObjects = __reg5.concat();
        this._targetObjectsHandlers = __reg4.concat();
        this._targetObjectsHandlersOwners = __reg3.concat();
    }

    function updateTabIndexes()
    {
        var __reg2 = 0;
        for (;;) 
        {
            if (__reg2 >= this._targetObjects.length) 
            {
                return;
            }
            this._targetObjects[__reg2].tabIndex = __reg2;
            ++__reg2;
        }
    }

    function isItemPresent(item, source)
    {
        var __reg1 = 0;
        while (__reg1 < source.length) 
        {
            if (item == String(source[__reg1])) 
            {
                return __reg1;
            }
            ++__reg1;
        }
        return -1;
    }

    function removeFocus()
    {
        Selection.setFocus(this._noFocusMovieClip);
    }

}