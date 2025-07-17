/**
 * Created by Akira on 03/03/2015.
 */
package com.bytesfromouterspace.stockbrokers.ui.components {
    import flash.display.Sprite;
    import flash.filters.BlurFilter;

    public class BlockerPanel extends ComponentBase {

        private var blockSprite:Sprite;

        public function BlockerPanel(_w:Number = 822, _h:Number = 634) {
            super(_w,_h);
            blockSprite = new Sprite();
            blockSprite.graphics.beginFill(0x212121, 0.9);
            blockSprite.graphics.drawRect(5, 5,_width-10, _height-10);
            blockSprite.graphics.lineStyle(1, 0x414141, 1);
            var i:int;
            for(i = 4; i < _width-8; i +=2) {
                blockSprite.graphics.moveTo(i, 4);
                blockSprite.graphics.lineTo(i, _height-8);
            }
            for(i = 4; i < _height-8; i +=2) {
                blockSprite.graphics.moveTo(4, i);
                blockSprite.graphics.lineTo(_width-8, i);
            }
            blockSprite.graphics.endFill();
            addChild(blockSprite);
        }
    }
}