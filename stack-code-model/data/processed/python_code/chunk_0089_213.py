import mx.transitions.Tween;
import mx.transitions.easing.*
import templateSlider.mvcgallery.*
import templateSlider.mvc.AbstractView
import templateSlider.Configuration


class templateSlider.mvcgallery.ThumbView extends AbstractView {
	var __content:MovieClip
	var __columns:Number;
	var __rows:Number;
	var __property:Object
	var __index:Number
	var __network:NetworkView
	var corner:MovieClip
	var __mask:MovieClip
	static var __marginX1:Number=7
	static var __marginY1:Number=7
	static var __marginX2:Number=7
 	static var __marginY2:Number=7

	static var __oldThumb:ThumbView
	var __loader:MovieClipLoader;
	var __background:MovieClip
	var background2:MovieClip
	var title:TextField
	var __alphaRol:Number=100
	var __alphaOut:Number=100
	var __sample:Sound
	var mcLupe:MovieClip
	var colorOut = 0x404240
	var colorRol = 0x40ACC8
	

	
//////////////////////////////////////////////////////////////////////////////////////////////////////////////

	function ThumbView(){
		
		this.enabled = false
		
	}
		
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	function onLoad(){
			if(!__content&&!__loader){
		__content=this.createEmptyMovieClip("container",1)
		__content._x=__marginX1
		__content._y=__marginY1
		
		this.__background._x=0
		this.__background._y=0
		this.__background._width=ThumbView.getWidth()
		this.__background._height=ThumbView.getHeight()
		
		
		var spaceBackground:Number=0
		this.background2._x=spaceBackground
		this.background2._y=spaceBackground
		this.background2._width=ThumbView.getWidth()-spaceBackground*2
		this.background2._height=ThumbView.getHeight()-spaceBackground*2
		
		this.title._width=getWidth()
		this.title._y=getHeight()-this.title._height-2
		this.title._x=0
		this.title.text=this.__property.title
		
		
		
		__loader=new MovieClipLoader()
		__loader.addListener(this)
		}
	}
		
//////////////////////////////////////////////////////////////////////////////////////////////////////////////

	public function laduj(){
		__loader.loadClip(this.__property.picsmall,__content)
	}
	
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
		
	function onRollOver(sound_){
				
		if(this.hitTest(_root._xmouse,_root._ymouse,true)&&sound_!=false&&!__network.__mouseMove){
		this.__sample=new Sound(this)
		this.__sample.attachSound("thumb_sample")
		this.__sample.setVolume(29)
		this.__sample.start(0,1)
		}
		
		background2.colorTo(colorRol,0.5)
		
	
	var w=new Tween(this.__content,'_alpha',Strong.easeOut,this.__content._alpha,__alphaRol,.5,1)
		
	}
		
//////////////////////////////////////////////////////////////////////////////////////////////////////////////

	function onRollOut(par) {
		
			if(this!=ThumbView.__oldThumb||par){
		
		var w=new Tween(this.__content,'_alpha',Strong.easeOut,this.__content._alpha,__alphaOut,.5,1)
	      background2.colorTo(colorOut,0.5)
			}
	}
	
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	function onPress(pres:Boolean){
		__oldThumb.onRollOut(1)
		onRollOver(false)
		__oldThumb=this
		/////
		if(pres!=false){
		var model:GalleryModel=GalleryModel(this.getModel())
		model.slide_stop()
		model.loadImage(this.__index)
		}
	}
	
/////////////////////////////////////////////////////////	

function onLoadComplete(target:MovieClip){
		target._alpha=0
}

/////////////////////////////////////////////////////////	


	
	function onLoadInit(target:MovieClip){		
	var m:GalleryModel=GalleryModel(this.getModel())
	this.enabled=true		
	
	//////mask
	__mask=this.createEmptyMovieClip("mcMask",3212)
	__mask._x=__marginX1
	__mask._y=__marginY1
	Drawing.rectangle(__mask,0,0,Configuration.THUMB_WIDTH,Configuration.THUMB_HEIGHT,["0xFF0000",50])
	target.setMask(__mask)
	
	///////////resize thumb
	var size:Resize=new Resize(Configuration.THUMB_WIDTH,Configuration.THUMB_HEIGHT,target._width,target._height)
	var new_size:Object=size.max()
	target._width=new_size.w
	target._height=new_size.h
	
	
	
	if(ThumbView.__oldThumb==this){
		this.onRollOver()
	}else{
		var twen=new Tween(target,'_alpha',Strong.easeOut,0,__alphaOut,1,1)
	}
	
	////////////////addd icon flv
	var m:GalleryModel=GalleryModel(this.getModel())
	if(m.isFlv(__property.picbig)){
	var icon:MovieClip=this.attachMovie("_IconFlv","__IconFlv__",435435)
	icon._x=Configuration.THUMB_WIDTH/2-icon._width/2+__marginX1
	icon._y=Configuration.THUMB_HEIGHT/2-icon._height/2+__marginY1
	}
	
	////lupe
	mcLupe._x = Configuration.THUMB_WIDTH + __marginX1
	mcLupe._y = Configuration.THUMB_HEIGHT + __marginY1
	
	mcLupe.swapDepths(this.getNextHighestDepth()+100)
	
	}
	
//////////////////////////////////////////////////////////////////////////////////////////////////////////////			
	
	static function getWidth(){
	  return Configuration.THUMB_WIDTH+(ThumbView.__marginX2+ThumbView.__marginX1)
	}
	
//////////////////////////////////////////////////////////////////////////////////////////////////////////////	
	
	static function getHeight(){
	   return Configuration.THUMB_HEIGHT+(ThumbView.__marginY2+ThumbView.__marginY1)
	}
	
//////////////////////////////////////////////////////////////////////////////////////////////////////////////	
	
    function onUnload(){
		//ThumbView.__oldThumb=undefined
		
		
	}
	
////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	
}