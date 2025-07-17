Stage.scaleMode = "noScale";
Stage.align = "TL";
//import do engine fuse
import com.mosesSupposes.fuse.*;
ZigoEngine.simpleSetup(Shortcuts, PennerEasing, Fuse, FuseFMP);
//funcao para colocar movieclips no stage a fullscreen**********************************************************
function toStage(mc:MovieClip, visibleProp:String, xPos:Number, yPos:Number, mcWidth:Number, mcHeight:Number) {
	if (visibleProp == "!visible") {
		mc._visible = false;
	} else if (visibleProp == "visible") {
		mc._visible = true;
	} else if (visibleProp == "!alpha") {
		mc._alpha = 0;
	} else if (visibleProp == "alpha") {
		mc._alpha = 100;
	}
	mc._x = Math.floor(xPos);
	mc._y = Math.floor(yPos);
	mc._width = mcWidth;
	mc._height = mcHeight;
}
//funcao para animar(slideTo) movieclips com componente zigo no stage a fullscreen******************************
function doSlide(mc:MovieClip, xPos:Number, yPos:Number, time:Number, easeTween:String, mcWidth:Number, mcHeight:Number) {
	ZigoEngine.doTween(mc, '_x,_y', [xPos, yPos], time, easeTween);
	mc._width = mcWidth;
	mc._height = mcHeight;
}
//
function doBlur(mc:MovieClip, blurX:Number, blurY:Number, time:Number, easeTween:String) {
	ZigoEngine.doTween(mc, 'Blur_blurX,Blur_blurY', [blurX, blurY], time, easeTween);
}