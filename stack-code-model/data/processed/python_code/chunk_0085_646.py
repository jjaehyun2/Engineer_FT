import pl.drawing.Rysowanie
import templateGallery.mvcgallery.*
import templateGallery.mvc.*
import templateGallery.I.*
import flash.display.BitmapData
import templateGallery.util.Observable

import templateGallery.Configuration


class templateGallery.mvcgallery.PreloaderView extends AbstractView {
var field:TextField
var mcProgress:MovieClip
var circle:MovieClip
var containerCircle:MovieClip


function onLoad() {

	 ///current preloader
	 NewColor.setColor(containerCircle.circle_mask, Configuration.COLOR_PRELOADER_CURRENT.split(",")[0])
	 containerCircle.circle_mask._alpha = Configuration.COLOR_PRELOADER_CURRENT.split(",")[1]
	 
	 ////bcg preloader
 NewColor.setColor(containerCircle.bcg, Configuration.COLOR_BCG_PRELOADER.split(",")[0])
	 containerCircle.bcg._alpha = Configuration.COLOR_BCG_PRELOADER.split(",")[1]
}

///////////////////////////////////////////////////////////////////////////////////

	function shov(){
		this._visible=true
	}
	
///////////////////////////////////////////////////////////////////////////////////
		
	function hide(){
		this._visible=false
	}
	
///////////////////////////////////////////////////////////////////////////////////

	function onLoadImageStart(){
		shov()
		this.field.text=""
		position()
	}
	
////////////////////////////////////////////////////////////////////////
	
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


///////////////////////////////////////////////////////////////////////////////////
	
	function onLoadImageProgress(obj){
		var obj=obj.loader
		var l=obj.l
		var t=obj.t
		var target=obj.target
		var procent = Math.ceil((l / t) * 100)
		
		mcProgress._xscale=procent
		
		field.text="LOADING  "+procent+"%"
		
		
	if(!circle){
		circle =containerCircle.createEmptyMovieClip("mc_circle", 213)	
		circle._alpha=50
	}
	
	var valueCircle=-Math.ceil((procent/100)*360)-6
	
	this.drawWedge(circle, 0, 0, 90, valueCircle, 30);
	
	containerCircle.circle_mask.setMask(circle)
		
	position()
	}

///////////////////////////////////////////////////////////////////////////////////
	
	function onLoadImageInit(){
		hide()
	}
	
/////////////////////////////////////////////////////////////////
	
    function position(){
		
		var gallery:Gallery=Gallery.getInstance()
		var image:ImageView=gallery.__image
		field.autoSize=true
		this._x=image._x-this._width/2
		this._y=image._y-this._height/2
		//this._x=-field._width/2
		//this._y=-field._height/2
		
		
	}

///////////////////////////////////////
	
	
}