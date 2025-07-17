import pl.drawing.Rysowanie
import templateList.mvcgallery.*
import templateList.mvc.*
import templateList.I.*
import flash.display.BitmapData
import templateList.util.Observable


class templateList.mvcgallery.PreloaderView extends AbstractView {
var field:TextField


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
		var procent=Math.ceil((l/t)*100)
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