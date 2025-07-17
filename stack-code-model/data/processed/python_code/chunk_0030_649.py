package com.controls.tabNavigator
{
    import flash.display.DisplayObject;
    import flash.events.Event;
    
    import mx.collections.IList;
    import mx.containers.ViewStack;
    import mx.controls.TabBar;
    import mx.core.ClassFactory;
    import mx.core.IFlexDisplayObject;
    import mx.core.mx_internal;
    import mx.events.CloseEvent;
    
    /**
     *  Dispathec after deattach closed tabs. In detail property passed remove
     *  tab index. 
     */ 
    [Event(name="close", type="mx.events.CloseEvent")]

    /**
     *  Extened tab bar with. If tab added when closeEnabled is TRUE tab will 
     *  have close button. 
     */ 
    public class TabBarExtended extends TabBar
    {
        use namespace mx_internal;

        private var _closeEnabled:Boolean;


        public function TabBarExtended()
        {
            super();
            navItemFactory = new ClassFactory(TabExtended);
        }

        public function get closeEnabled():Boolean
        {
            return this._closeEnabled;
        }

        public function set closeEnabled(value:Boolean):void
        {
            this._closeEnabled = value;
            this.invalidateDisplayList();
        }

        public function onCloseTabClicked(event:Event):void
        {
            var index:int = getChildIndex(DisplayObject(event.currentTarget));
            dispatchEvent(new CloseEvent(CloseEvent.CLOSE, true, false, index));
        }

        override protected function createNavItem(label:String, icon:Class = null):IFlexDisplayObject
        {
            var tab:TabExtended = super.createNavItem(label, icon) as TabExtended;

            tab.closeEnabled = this._closeEnabled;
            tab.addEventListener(TabExtended.CLOSE_TAB_EVENT, onCloseTabClicked, false, 0, true);

            return tab;
        }
    }
}