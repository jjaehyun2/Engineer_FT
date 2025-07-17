import pl.drawing.Rysowanie
import templateSlider.mvcgallery.*
import templateSlider.mvc.*
import templateSlider.I.*
import flash.display.BitmapData
import templateSlider.util.Observable
import templateSlider.Configuration


class templateSlider.mvcgallery.PreloaderView extends AbstractView {
var field:TextField
var mcProgress:MovieClip
var bcg:MovieClip

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
	
///////////////////////////////////////////////////////////////////////////////////
	
	function onLoadImageProgress(obj){
		var obj=obj.loader
		var l=obj.l
		var t=obj.t
		var target=obj.target
		var procent = Math.ceil((l / t) * 100)
		
		
		mcProgress._xscale = procent
		
		////color current
		if(Configuration.PRELOADER_CURRENT.length){
		NewColor.setColor(mcProgress, Configuration.PRELOADER_CURRENT.split(",")[0])
		mcProgress._alpha = Configuration.PRELOADER_CURRENT.split(",")[1]
		}
		
		////color background
		if(Configuration.PRELOADER_BCG.length){
		NewColor.setColor(bcg, Configuration.PRELOADER_BCG.split(",")[0])
		bcg._alpha = Configuration.PRELOADER_BCG.split(",")[1]
		}
		
		
		field.text="LOADING  "+procent+"%"
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