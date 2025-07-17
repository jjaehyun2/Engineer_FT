import templateLoader.mvctemplate.*
import templateLoader.mvc.*
import templateLoader.I.*
import flash.display.BitmapData
import templateLoader.util.Observable

import mx.transitions.Tween
import mx.transitions.easing.*

   

class templateLoader.mvctemplate.PreloaderView extends AbstractView {
		

var t:TextField
var rectangle:MovieClip
var circle:MovieClip
var containerCircle:MovieClip
var bcg:MovieClip
///////////////////////////////////////////////////////////

function PreloaderView() {
	rectangle._xscale=0
	this.hide()	
}

////////////////////////////////////////////////////////////

public function defaultController (model:Observable):Controller {
  return new PreloaderController(model)
 }
 
////////////////////////////////////////////////////////////

function onLoad() {
	if(ConfigurationSite.PRELOADER_BACKGROUND_COLOR.length){
   NewColor.setColor(bcg, ConfigurationSite.PRELOADER_BACKGROUND_COLOR.split(",")[0])
   bcg._alpha = ConfigurationSite.PRELOADER_BACKGROUND_COLOR.split(",")[1]
   }
}

////////////////////////////////////////////////////////////

function shov(){

	this._visible=true
	this.onResize()
}

/////////////////////////////////////////////////////////////////////////

function hide(){
	this._visible=false	
}

///////////////////////////////////////////////////////////////////////////

function onLoadXml(){
//	this.shov()	
}

////////////////////////////////////////////////////////////////////////////

function onLoadStart(){
	this.shov()	
	
}

//////////////////////////////////////////////////////////////////////////////

function onLoadProgress(target:MovieClip, l:Number,t:Number){
	this.shov()	
	////nr
	var nr = Math.ceil((l / t) * 100)
	if(nr>100){nr=100}
	
	this.t.text = "LOADING             "+ nr + "%"
	
	if(ConfigurationSite.PRELOADER_COLOR_TEXT.length){
	this.t.textColor = ConfigurationSite.PRELOADER_COLOR_TEXT.split(",")[0]
    this.t._alpha=ConfigurationSite.PRELOADER_COLOR_TEXT.split(",")[1]
	}
	
	

	
	var procent:Number = (l / t) * 100
	
	if(ConfigurationSite.PRELOADER_BAR_COLOR.length){
	NewColor.setColor(rectangle, ConfigurationSite.PRELOADER_BAR_COLOR.split(",")[0])
	rectangle._alpha = ConfigurationSite.PRELOADER_BAR_COLOR.split(",")[1]
	}
	
	this.rectangle._xscale = (l / t) * 100
	
	
	if(!circle){
		circle =containerCircle.createEmptyMovieClip("mc_circle", 213)	
		circle._alpha=50
	}
	
	var valueCircle=-Math.ceil((procent/100)*360)-6
	
	//trace("valueCircle = "+valueCircle)
	
	this.drawWedge(circle, 0, 0, 90, valueCircle, 30);
	
	containerCircle.circle_mask.setMask(circle)
}

///////////////////////////////////////////////////////////////////////////

function drawWedge(mc,x, y, startAngle, arc, radius, yRadius) {
	mc.clear();
	mc.beginFill(0x000000, 100);
	
	
	if (arguments.length<5) {
		return;
	}
	mc.moveTo(x, y);
	
	if (yRadius == undefined) {
		yRadius = radius;
	}

	var segAngle, theta, angle, angleMid, segs, ax, ay, bx, by, cx, cy;

	if (Math.abs(arc)>360) {
		arc = 360;
	}

	segs = Math.ceil(Math.abs(arc)/45);

	segAngle = arc/segs;
	theta = -(segAngle/180)*Math.PI;

	angle = -(startAngle/180)*Math.PI;

	if (segs>0) {
		ax = x+Math.cos(startAngle/180*Math.PI)*radius;
		ay = y+Math.sin(-startAngle/180*Math.PI)*yRadius;
		mc.lineTo(ax, ay);
	
		for (var i = 0; i<segs; i++) {
			angle += theta;
			angleMid = angle-(theta/2);
			bx = x+Math.cos(angle)*radius;
			by = y+Math.sin(angle)*yRadius;
			cx = x+Math.cos(angleMid)*(radius/Math.cos(theta/2));
			cy = y+Math.sin(angleMid)*(yRadius/Math.cos(theta/2));
			mc.curveTo(cx, cy, bx, by);
		}
	
		mc.lineTo(x, y);
	}
	mc.endFill();
};

///////////////////////////////////////////////////////////////////////////

private function progress(){
		
}

/////////////////////////////////////////////////////////////////////////////

function onLoadInit(){
	this.hide()	
	
}

///////////////////////////////////////////////////////////////////////////////

function onResize(){
	var m:LoaderModel=LoaderModel(this.getModel())
	var stage_w=m.__width
	var stage_h=m.__height
	
	this._x=m.widthContent/2-145/2
	this._y=m.heightContent/2-54/2
}

//////////////////////////////////////////////////////////////////////////////


}