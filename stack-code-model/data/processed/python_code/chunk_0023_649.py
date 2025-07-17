import templateNewsy.util.*;
import templateNewsy.mvc.*
import templateNewsy.I.*
import templateNewsy.mvcgallery.*

class templateNewsy.mvcgallery.TimeView extends AbstractView {


var progressTime:MovieClip
var spiral:MovieClip
   
////////////////////////////////////////////////
   
  public function defaultController (model:Observable):Controller {
   return new TimeController(model);
  }
  
////////////////////////////////////////////////

function onLoad(){
	///Stage.addListener(this)	
}

//////////////////////////////////////////////////////////

function onResize(){
	this.onImageResize()	
}

///////////////////////////////////////////////////

  function hide(){
	  this.spiral._visible=false
}
  
////////////////////////////////////////////////////////////////////////////////////////	
  
  function onStopSlide(){
	  this.spiral._visible=false
	 }

////////////////////////////////////////////////////////////////////////////////////////	
	 
	function onStartSlide(){
		   	this.progressTime.clear();
		    this.spiral._visible=true
	}

////////////////////////////////////////////////////////////////////////////////////////	

  function onProgressTime(obj){
	var value=obj.value
	if(!this.progressTime){
		this.progressTime=this.createEmptyMovieClip("mc_circle",213)		
	}
	this.progressTime.clear();
	this.progressTime.beginFill(0x000000,100);
	var value2=-Math.ceil((value/100)*360)-6
	
	trace("value2 = "+value2)
	
	this.drawWedge(this.progressTime,0,0, 90,value2,150);
	this.progressTime.endFill();
	spiral.setMask(progressTime)
}

//////////////////////////////////////////////////////////////////////////////////////////

 function onImageResize(){
	var model:GalleryModel=GalleryModel(this.getModel())
	var gallery:Gallery=model.__target
	var image:ImageView=gallery.__image
	
	//this._x=image._x-0
	//this._y=image._y-image.getHeight()/2-33
	//this._x=image._x+image.getWidth()/2-164
	///this._y=image._y-image.getHeight()/2-23
	this._x = -49
	this._y=-30
 }
 
//////////////////////////////////////////////////////////////////////////////////////////
	
	function drawWedge(mc,x, y, startAngle, arc, radius, yRadius) {
	
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
};
 
 //////////////////////////////////////////////////////////////////////////////////////////
 
 
 
}