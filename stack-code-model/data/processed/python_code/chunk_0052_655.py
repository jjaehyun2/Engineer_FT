import templateNewsy.util.*;
import templateNewsy.mvc.*
import templateNewsy.I.*
import templateNewsy.mvcgallery.*

class templateNewsy.mvcgallery.BSlideView extends AbstractView {

var mc_slide:MovieClip
var __visibility:Boolean=true
var positionY:Number=10

 function BSlideView(){addEvents()}

///////////////////////////////////

function onLoad(){
	//Stage.addListener(this)
	mc_slide._y=positionY
	
}

////////////////////////////////////////////

function onResize(){
	this.onImageResize()	
}

///////////////////////////////////////////////////////////////////////////////////////// 

 function onLoadThumb(){
	 this.hide()
 }
 
///////////////////////////////

function onPressClose(){
	this.hide()	
}
 
/////////////////////////////////////////////////////////////////////////////////////////

function onChangedIndex(){
  ///this.shov()
}

///////////////////////////////////////////////////////////////////

function onLoadImage(){
	///this.shov()	
}

/////////////////////////////////////////////////////////////////////////////////////////

function shov(){
	if(this.__visibility==false){
mc_slide._visible=true
mc_slide.enabled = false

mc_slide._visible = true
mc_slide._alpha = 0
mc_slide.tween('_alpha',100,0.5,'easeOutCubic')

__visibility=true
}
}

/////////////////////////////////////////////////////////////////////////////////////////

function hide(){
if(this.__visibility==true){	
mc_slide._visible=false
__visibility=false
}
}

//////////////////////////////////////////////////////////////////////////////////////////  

public function defaultController (model:Observable):Controller {
   return new BSlideController(model);
}


//////////////////////////////////////////////////////////////////////////////////////////  

  function addEvents(){
 mc_slide.onPress=Delegate2.create(this,onPressSlide)
 mc_slide.onRollOver=Delegate2.create(this,onRollOverSlide)
 mc_slide.onRollOut=Delegate2.create(this,onRollOutSlide)
 mc_slide.enabled=false
  }
  
/////////////////////////////////////////////////  

function onStopSlide(){  
this.mc_slide.gotoAndStop(1)
}

//////////////////////////////////////////////////////////////////////////////////////////  

function onStartSlide(){  
 this.mc_slide.gotoAndStop(2)
}

//////////////////////////////////////////////////////////////////////////////////////////    

function onPressSlide(){
	  var m:GalleryModel=GalleryModel(this.getModel())
	  if(this.mc_slide._currentframe==1){
	    m.slide_start()
	  }else{
		 m.slide_stop() 
	  }
	  onRollOverSlide()
}

////////////////////////////////////////////////////////////////////////////////////////// 

function onRollOverSlide(){
	 	 this.mc_slide.mc_play.gotoAndStop(2)
		 this.mc_slide.mc_pause.gotoAndStop(2)
		 
		  this.mc_slide.tween('_y',0,.3,'easeOutCubic')
}

//////////////////////////////////////////////////////////////////////////////////////////    

function onRollOutSlide(){
	 	 this.mc_slide.mc_play.gotoAndStop(1)
		 this.mc_slide.mc_pause.gotoAndStop(1)
		 
		 this.mc_slide.tween('_y',positionY,.3,'easeOutCubic')
}

//////////////////////////////////////////////////////////////////////////////////////////

function onImageResize(){
setPositionSlide()
}

///////////////////////////////////////////////////////////////////////////////

private function setPositionSlide(){
	var model:GalleryModel=GalleryModel(this.getModel())
	var gallery:Gallery=model.__target
	var image:ImageView=gallery.__image
	this._x=image._x+image.getWidth()/2-110
	this._y=image._y-image.getHeight()/2
}

/////////////////////////////////////////////////////////////////////////////////////////

function onIntroEnd(){
	this.shov()
	
	var model:GalleryModel=GalleryModel(this.getModel())
	var slide=model.__slide
	if(slide==false){
	this.mc_slide.enabled=true
	}
}

/////////////////////////////////////////////////////////////////////////////////////////

function onExitStart(){
	var model:GalleryModel=GalleryModel(this.getModel())
	var slide=model.__slide
	if(slide==false){
	this.mc_slide.enabled=false
	}
}

/////////////////////////////////////////////////////////////////////////////////////////
  
}