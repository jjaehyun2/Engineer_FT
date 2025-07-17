import templateSlider.mvcgallery.*
import templateSlider.mvc.AbstractView

import mx.events.EventDispatcher


class templateSlider.mvcgallery.PortionImageView extends AbstractView {
	
var __portion:PortionComponentsView
var tween
	
////////////////////////////////////////////////////////////////////////////////////////	

function PortionImageView() {
	this._alpha=0	
}

////////////////////////////////////////////////////////////

function onIntroEnd(){
var m:GalleryModel=GalleryModel(this.getModel())
m.removeEventListener("onIntroEnd",this)
}

////////////////////////////////////////////////////////////

function onIntroStart(){
if(this._alpha == 0) {
	this.tween('_alpha',100,1,'easeOutCubic')
}
}

////////////////////////////////////////////////////////////////////////////////////////	

function create(){
var m:GalleryModel=GalleryModel(this.getModel())
__portion=PortionComponentsView(this.attachMovie("portion","portion",2))
this.__portion.__viev_length=15
__portion.setModel(this.getModel())
this.__portion.setPageLength=(m.__array.length-1)
this.__portion.addEventListener("onChanged",this)
}

////////////////////////////////////////////////////////////////////////////////////////	

function onImageResize(){
this.resize()
}

////////////////////////////////////////////////////////////////////////////////////////	

function onResize() {
	resize()
}

////////////////////////////////////////////////////////////////////////////////////////	

function resize(){
	var model:GalleryModel=GalleryModel(this.getModel())
	var gallery:Gallery=Gallery.getInstance()
	var image:ImageView=gallery.__image
	var height=image._y+image.getHeight()/2-image.__spaceDown/2-10
	
	this.__portion._x=image._x-image.getWidth()/2-this.__portion.getBounds(this.__portion).xMin+image.__space
	this.__portion._y = height
	
	//trace(image.getWidth())
	
}

////////////////////////////////////////////////////////////////////////////////////////	

	function onLoadThumb(){
		var m:GalleryModel=GalleryModel(this.getModel())
		var index=m.__thumbModel.getCurrent()
		var length=m.__thumbModel.getLength()
		this.__portion.setPageLength=length
        this.__portion.selectedIndex(index,false)
	}

////////////////////////////////////////////////////////////////////////////////////////	

	function onChangedIndex(){
		create()	
		var m:GalleryModel=GalleryModel(this.getModel())
		var m:GalleryModel=GalleryModel(this.getModel())
		var nr=m.index
		this.__portion.selectedIndex(nr,false)
		this.resize()
	}

////////////////////////////////////////////////////////////////////////////////////////	

	function onChanged(){
	var m:GalleryModel=GalleryModel(this.getModel())
	m.slide_stop()
	var nr=this.__portion.__current
	m.loadImage(nr)
	}

////////////////////////////////////////////////////////////////////////////////////////	

	function ArrowPosition(){
		var left=this.__portion.arrow_left
		var right=this.__portion.arrow_right
	}

////////////////////////////////////////////////////////////////////////////////////////	
	
	
	
}