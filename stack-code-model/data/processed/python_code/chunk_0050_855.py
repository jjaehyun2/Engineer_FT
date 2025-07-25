﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.core.view.Layers

package kabam.rotmg.core.view
{
    import flash.display.Sprite;
    import flash.display.DisplayObjectContainer;
    import kabam.rotmg.tooltips.view.TooltipsView;
    import kabam.rotmg.dialogs.view.DialogsView;
    import io.decagames.rotmg.ui.popups.PopupView;

    public class Layers extends Sprite 
    {

        private var menu:ScreensView;
        public var overlay:DisplayObjectContainer;
        private var tooltips:TooltipsView;
        public var top:DisplayObjectContainer;
        public var mouseDisabledTop:DisplayObjectContainer;
        private var dialogs:DialogsView;
        private var popups:PopupView;
        public var api:DisplayObjectContainer;
        public var console:DisplayObjectContainer;

        public function Layers()
        {
            addChild((this.menu = new ScreensView()));
            addChild((this.overlay = new Sprite()));
            addChild((this.top = new Sprite()));
            addChild((this.mouseDisabledTop = new Sprite()));
            this.mouseDisabledTop.mouseEnabled = false;
            addChild((this.popups = new PopupView()));
            addChild((this.dialogs = new DialogsView()));
            addChild((this.tooltips = new TooltipsView()));
            addChild((this.api = new Sprite()));
            addChild((this.console = new Sprite()));
        }

    }
}//package kabam.rotmg.core.view