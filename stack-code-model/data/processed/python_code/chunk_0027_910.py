package kabam.rotmg.friends.view {
import com.company.assembleegameclient.ui.Scrollbar;

import flash.display.DisplayObject;
import flash.display.Shape;
import flash.display.Sprite;
import flash.events.Event;

public class FriendListContainer extends Sprite {


    private const GAP_Y:int = 3;

    public function FriendListContainer(_arg_1:Number, _arg_2:Number) {
        super();
        this._currentY = 0;
        this._width = _arg_1;
        this._height = _arg_2;
        var _local3:Shape = new Shape();
        _local3.graphics.beginFill(0x224499);
        _local3.graphics.drawRect(0, 0, this._width, this._height);
        _local3.graphics.endFill();
        addChild(_local3);
        this.mask = _local3;
        this._itemContainer = new Sprite();
        addChild(this._itemContainer);
        this._scrollbar = new Scrollbar(16, this._height);
        this._scrollbar.x = this._width - 18;
        this._scrollbar.y = 0;
        this._scrollbar.visible = false;
        this._scrollbar.addEventListener("change", this.onScrollBarChange);
        addChild(this._scrollbar);
    }
    private var _currentY:int;
    private var _width:Number;
    private var _height:Number;
    private var _itemContainer:Sprite;
    private var _scrollbar:Scrollbar;

    override public function getChildAt(_arg_1:int):DisplayObject {
        return this._itemContainer.getChildAt(_arg_1) as Sprite;
    }

    override public function removeChildAt(_arg_1:int):DisplayObject {
        var _local2:Sprite = this._itemContainer.getChildAt(_arg_1) as Sprite;
        if (_local2 != null) {
            this._currentY = this._currentY - (_local2.height + 3);
        }
        return this._itemContainer.removeChildAt(_arg_1) as Sprite;
    }

    public function addListItem(_arg_1:FListItem):void {
        _arg_1.y = this._currentY;
        this._itemContainer.addChild(_arg_1);
        this._currentY = this._currentY + (_arg_1.height + 3);
        this.updateScrollbar(this._currentY > this._height);
    }

    public function getTotal():int {
        return this._itemContainer.numChildren;
    }

    public function clear():void {
        while (this._itemContainer.numChildren > 0) {
            this._itemContainer.removeChildAt(this._itemContainer.numChildren - 1);
        }
        this._currentY = 0;
    }

    private function updateScrollbar(_arg_1:Boolean):void {
        this._scrollbar.visible = _arg_1;
        if (_arg_1) {
            this._scrollbar.setIndicatorSize(this._height, this._currentY);
        }
    }

    private function onScrollBarChange(_arg_1:Event):void {
        this._itemContainer.y = -this._scrollbar.pos() * (this._itemContainer.height - this._height + 20);
    }
}
}