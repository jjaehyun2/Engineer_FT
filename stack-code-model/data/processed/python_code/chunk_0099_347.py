import templateSlider.mvcgallery.*
import templateSlider.mvc.AbstractView

import mx.events.EventDispatcher


class templateSlider.mvcgallery.PortionThumbView extends AbstractView {

var __portion:PortionComponentsView

//////////////////////////////////////////////////////////////////////////////////

	function PortionThumbView(){
		create()	
	}

//////////////////////////////////////////////////////////////////////////////////
	
function create(){
var m:GalleryModel=GalleryModel(this.getModel())
 __portion=PortionComponentsView(this.attachMovie("portion","portion",1))
 __portion.setModel(this.getModel())
 this.__portion.setPageLength=m.__thumbModel.getLength()
 this.__portion.selectedIndex(1,false)
 this.__portion.addEventListener("onChanged",this)
 ArrowPosition()
}
	
	
//////////////////////////////////////////////////////////////////////////////////

	function onLoadThumb(){
		var m:GalleryModel=GalleryModel(this.getModel())
		var index=m.__thumbModel.getCurrent()
		var length=m.__thumbModel.getLength()
		this.__portion.setPageLength=length
       this.__portion.selectedIndex(index,false)
	   create()
	}
	 
//////////////////////////////////////////////////////////////////////////////////

	function onChangedPortion(){  
		var m:GalleryModel=GalleryModel(this.getModel())
		var index=m.__thumbModel.getCurrent()
		var length=m.__thumbModel.getLength()
		this.__portion.setPageLength=length
       this.__portion.selectedIndex(index,false)
	    ArrowPosition()
	}
	
//////////////////////////////////////////////////////////////////////////////////

	function onChanged(){
		var m:GalleryModel=GalleryModel(this.getModel())
		m.slide_stop()
		m.setPortionThumb(this.__portion.__current)
	}
	
//////////////////////////////////////////////////////////////////////////////////

	function onChangedIndex(){
	var m:GalleryModel=GalleryModel(this.getModel())
	var nr=m.__thumbModel.getNumer(m.index)
	this.__portion.selectedIndex(nr,false)
	ArrowPosition()
	}

//////////////////////////////////////////////////////////////////////////////////

	function ArrowPosition(){
		var left=this.__portion.arrow_left
		var right=this.__portion.arrow_right
	}

//////////////////////////////////////////////////////////////////////////////////
	
	
	
	
}