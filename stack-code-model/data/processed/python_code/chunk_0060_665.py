package kabam.rotmg.classes.view {
import flash.display.DisplayObject;

import kabam.rotmg.classes.model.CharacterClass;
import kabam.rotmg.classes.model.ClassesModel;

import robotlegs.bender.bundles.mvcs.Mediator;

public class CharacterSkinListMediator extends Mediator {


    public function CharacterSkinListMediator() {
        super();
    }
    [Inject]
    public var view:CharacterSkinListView;
    [Inject]
    public var model:ClassesModel;
    [Inject]
    public var factory:CharacterSkinListItemFactory;

    override public function initialize():void {
        this.model.selected.add(this.setSkins);
        this.setSkins(this.model.getSelected());
    }

    override public function destroy():void {
        this.model.selected.remove(this.setSkins);
    }

    private function setSkins(charClass:CharacterClass):void {
        var items:Vector.<DisplayObject> = this.factory.make(charClass.skins);
        this.view.setItems(items);
    }
}
}