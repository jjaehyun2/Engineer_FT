﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.game.view.TextPanelMediator

package kabam.rotmg.game.view
{
    import robotlegs.bender.bundles.mvcs.Mediator;
    import kabam.rotmg.game.model.TextPanelData;

    public class TextPanelMediator extends Mediator 
    {

        [Inject]
        public var view:TextPanel;
        [Inject]
        public var data:TextPanelData;


        override public function initialize():void
        {
            this.view.init(this.data.message);
        }


    }
}//package kabam.rotmg.game.view