﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.news.view.NewsMediator

package kabam.rotmg.news.view
{
    import robotlegs.bender.bundles.mvcs.Mediator;
    import kabam.rotmg.news.controller.NewsDataUpdatedSignal;
    import kabam.rotmg.news.model.NewsModel;
    
    import kabam.rotmg.news.model.NewsCellVO;

    public class NewsMediator extends Mediator 
    {

        [Inject]
        public var view:NewsView;
        [Inject]
        public var update:NewsDataUpdatedSignal;
        [Inject]
        public var model:NewsModel;


        override public function initialize():void
        {
            this.view.update(this.model.news);
            this.update.add(this.onUpdate);
        }

        override public function destroy():void
        {
            this.update.remove(this.onUpdate);
        }

        private function onUpdate(_arg_1:Vector.<NewsCellVO>):void
        {
            this.view.update(_arg_1);
        }


    }
}//package kabam.rotmg.news.view