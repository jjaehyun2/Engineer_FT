﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.classes.view.CharacterSkinListMediator

package kabam.rotmg.classes.view
{
    import robotlegs.bender.bundles.mvcs.Mediator;
    import kabam.rotmg.classes.model.ClassesModel;
    
    import flash.display.DisplayObject;
    import kabam.rotmg.classes.model.CharacterClass;

    public class CharacterSkinListMediator extends Mediator 
    {

        [Inject]
        public var view:CharacterSkinListView;
        [Inject]
        public var model:ClassesModel;
        [Inject]
        public var factory:CharacterSkinListItemFactory;


        override public function initialize():void
        {
            this.model.selected.add(this.setSkins);
            this.setSkins(this.model.getSelected());
        }

        override public function destroy():void
        {
            this.model.selected.remove(this.setSkins);
        }

        private function setSkins(_arg_1:CharacterClass):void
        {
            var _local_2:Vector.<DisplayObject> = this.factory.make(_arg_1.skins);
            this.view.setItems(_local_2);
        }


    }
}//package kabam.rotmg.classes.view