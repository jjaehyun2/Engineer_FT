import banner.mvcgallery.GalleryModel;
import mx.transitions.Tween;
import mx.transitions.easing.*
import templateList.mvcgallery.*
import templateList.mvc.AbstractView
import templateList.Configuration
import templateLoader.mvctemplate.LoaderModel;

import com.asual.swfaddress.SWFAddress
import com.asual.swfaddress.SWFAddressEvent


class templateList.mvcgallery.ThumbView extends AbstractView {
	var __content:MovieClip
	var __columns:Number;
	var __rows:Number;
	var __property:Object
	var __index:Number
	var __network:NetworkView
	var corner:MovieClip
	var __mask:MovieClip
	static var __marginX1:Number=0
	static var __marginY1:Number=0
	static var __marginX2:Number=680
 	static var __marginY2:Number=0

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
	var colorRol = 0x6D706D
	var mcLine:MovieClip
	

	
//////////////////////////////////////////////////////////////////////////////////////////////////////////////

	function ThumbView(){
		
		///this.enabled = false
		
	}
		
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	function onLoad() {
		var m:GalleryModel = GalleryModel(this.getModel())
		
		
		
		///COLOR SEP
		NewColor.setColor(mcLine,Configuration.COLOR_SEP)
		
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
		this.background2._width=__marginX1+Configuration.THUMB_WIDTH+__marginX1///ThumbView.getWidth()-spaceBackground*2
		this.background2._height=ThumbView.getHeight()-spaceBackground*2
		
		this.title._width = __marginX2
		this.title._height=Configuration.THUMB_HEIGHT
		this.title._y=__marginY1
		this.title._x = __marginX1 + Configuration.THUMB_WIDTH + 20
		title.styleSheet = Configuration.CSS_STYLE
		
		title.embedFonts=true
		this.title.htmlText=this.__property.child.childNodes[0].firstChild.nodeValue
		title.border = false
		title.borderColor=0xFF0000
		
		
		mcLine._x = 0
		mcLine._y= ThumbView.getHeight()+__network.__spaceY/2
		
		__loader=new MovieClipLoader()
		__loader.addListener(this)
		}
		
		
		var loader_model:LoaderModel = LoaderModel(LoaderModel.getInstance())
		var redirect_to_menu_id:String=__property.redirect_to_menu_id
		var redirect_to_url:String=__property.redirect_to_url
		var redirect_swfAdres=__property.redirect_SwfAddress
		
		
		
		
		
		
		
		if (redirect_to_menu_id==undefined && redirect_to_url==undefined&&redirect_swfAdres==undefined) {
			this.enabled = false
		}else {
			this.enabled=true
		}
		
		
	}
		
//////////////////////////////////////////////////////////////////////////////////////////////////////////////

	public function laduj(){
		__loader.loadClip(this.__property.picsmall,__content)
	}
	
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
		
	function onRollOver(sound_){
				
		if(this.hitTest(_root._xmouse,_root._ymouse,true)&&sound_!=false&&!__network.__mouseMove){
		//this.__sample//=new Sound(this)
		//this.__sample.attachSound("thumb_sample")
		//this.__sample.setVolume(29)
		//this.__sample.start(0,1)
		}
		
		background2.colorTo(colorRol,0.5)
		
	
		///this.background2.tween('_alpha',50)
	
		var w=new Tween(this.__content,'_alpha',Strong.easeOut,this.__content._alpha,__alphaRol,.5,1)
		
	}
		
//////////////////////////////////////////////////////////////////////////////////////////////////////////////

	function onRollOut(par) {
		
			if(this!=ThumbView.__oldThumb||par){
		
		 var w=new Tween(this.__content,'_alpha',Strong.easeOut,this.__content._alpha,__alphaOut,.5,1)
	      background2.colorTo(colorOut, 0.5)
		  ///this.background2.tween('_alpha',100)
			}
	}
	
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	function onPress(pres:Boolean) {
		//trace("on press thumb!")
		__oldThumb.onRollOut(1)
		onRollOver(false)
		__oldThumb=this
		/////
		if(pres!=false){
		var model:GalleryModel=GalleryModel(this.getModel())
		///model.slide_stop()
		///model.loadImage(this.__index)
		
		
		/////////////REDIRECT////////////////////////////////
		
		var loader_model:LoaderModel = LoaderModel(LoaderModel.getInstance())
		var redirect_to_menu_id:Number=Number(__property.redirect_to_menu_id)
		var redirect_to_url:String=__property.redirect_to_url
		var redirect_swfAdres=__property.redirect_SwfAddress
		
		//////redirect menu
		if(redirect_to_menu_id!=undefined){
		loader_model.setSelectedId(redirect_to_menu_id)
		}
		
		/////redirect in browser
		if (redirect_to_url != undefined) {
			////target
			var target = redirect_to_url.split(",")[1]
			if (target == undefined) { target = "_blank" }
			///adress
			if(redirect_to_url.indexOf(",")>=0){
			var adress = redirect_to_url.split(",")[0]
			}else {
			var adress = redirect_to_url
			}
			
			getURL(adress,target)
		}
		
		/////redirect swf Addres
		if (redirect_swfAdres != undefined) {
			SWFAddress.setValue(redirect_swfAdres)
		}
		
		
	
		
		
		
		
		
		}
	}
	
/////////////////////////////////////////////////////////	

function onLoadComplete(target:MovieClip){
		target._alpha=0
}

/////////////////////////////////////////////////////////	


	
	function onLoadInit(target:MovieClip){		
	var m:GalleryModel=GalleryModel(this.getModel())
	//this.enabled=true		
	
	//////mask
	__mask//=this.createEmptyMovieClip("mcMask",3212)
	__mask._x=__marginX1
	__mask._y=__marginY1
	Drawing.rectangle(__mask,0,0,Configuration.THUMB_WIDTH,Configuration.THUMB_HEIGHT,["0xFF0000",50])
	//target.setMask(__mask)
	
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
	var icon:MovieClip//=this.attachMovie("_IconFlv","__IconFlv__",435435)
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