package com.mojang.mario.sprites {

import java.awt.JGraphics;
import flash.display.BitmapData;

import com.mojang.mario.level.SpriteTemplate;

public class JSprite {
    public static var spriteContext:SpriteContext;
    
    public var xOld:Number = 0;
    public var yOld:Number = 0;
    public var x:Number = 0;
    public var y:Number = 0;
    public var xa:Number = 0;
    public var ya:Number = 0;
    
    public var xPic:int = 0;
    public var yPic:int = 0;
    public var wPic:int = 32;
    public var hPic:int = 32;
    public var xPicO:int = 0;
    public var yPicO:int = 0;
    public var xFlipPic:Boolean = false;
    public var yFlipPic:Boolean = false;
    public var sheet:Array;
    public var visible:Boolean = true;
    
    public var layer:int = 1;

    public var spriteTemplate:SpriteTemplate;
    
    public function move():void
    {
        x+=xa;
        y+=ya;
    }
    
    public function render(og:JGraphics, alpha:Number):void
    {
        if (!visible) return;

        var xPixel:int = (xOld + (x - xOld) * alpha) - xPicO;
        var yPixel:int = (yOld + (y - yOld) * alpha) - yPicO;

        og.drawImage6(sheet[xPic][yPic],
                      xPixel + (xFlipPic ? wPic : 0),
                      yPixel + (yFlipPic ? hPic : 0),
                      xFlipPic ? -wPic : wPic,
                      yFlipPic ? -hPic : hPic);
    }
    
    public function tick():void
    {
        xOld = x;
        yOld = y;
        move();
    }

    public function tickNoMove():void
    {
        xOld = x;
        yOld = y;
    }

    public function getX(alpha:Number):Number
    {
        return (xOld+(x-xOld)*alpha)-xPicO;
    }

    public function getY(alpha:Number):Number
    {
        return (yOld+(y-yOld)*alpha)-yPicO;
    }

    public function collideCheck():void
    {
    }

    public function bumpCheck(xTile:int, yTile:int):void
    {
    }

    public function shellCollideCheck(shell:Shell):Boolean
    {
        return false;
    }

    public function release(mario:Mario):void
    {
    }

    public function fireballCollideCheck(fireball:Fireball):Boolean
    {
        return false;
    }
}
}