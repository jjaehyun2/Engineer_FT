﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.protip.commands.ShowProTipCommand

package kabam.rotmg.protip.commands
{
    import kabam.rotmg.core.view.Layers;
    import kabam.rotmg.protip.view.ProTipView;
    import kabam.rotmg.protip.model.IProTipModel;

    public class ShowProTipCommand 
    {

        [Inject]
        public var layers:Layers;
        [Inject]
        public var view:ProTipView;
        [Inject]
        public var model:IProTipModel;


        public function execute():void
        {
            this.view.setTip(this.model.getTip());
            this.layers.overlay.addChild(this.view);
        }


    }
}//package kabam.rotmg.protip.commands