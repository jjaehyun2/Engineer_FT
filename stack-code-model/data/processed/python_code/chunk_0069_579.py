import templateMove.util.*;
import templateMove.mvc.*
import templateMove.I.*
import templateMove.mvcFLV.*;

class templateMove.mvcFLV.PreloaderView extends AbstractView {
	var pasek:MovieClip
	var __width:Number
	private var __inter
	var __visible:Boolean=false
/////////////////////////////////////////////////////////////////////	

public function defaultController (model:Observable):Controller {
  return new PreloaderController(model)
 }
 
///////////////////////////////////////////////////////////////////////////////////////////

 function PreloaderView(){
	
	 this.hide()
	 this.onResize()
 }
 

///////////////////////////////////////////////////////////////////////////////////////////

 private function onProgressFilm(){
	 var m:FLVModel=FLVModel(this.getModel())
	 /////loader
		var m:FLVModel=FLVModel(this.getModel())
		var l=m.__ns.bytesLoaded
		var t=m.__ns.bytesTotal
		
		
		var c = Math.ceil((l/t)*this.__width);
				
		if(l>100000&&__visible==false){
			m.dispatchEvent({target:this,type:"onVisibleImage"})
			__visible=true
		}
		
		if(l>=t&&t>0){
	clearInterval(__inter)
		}
	 this.pasek._width=c
	 
 }
 
///////////////////////////////////////////////////////////////////////////////////////////
 
 function shov(){
    this._visible=true
	 var m:FLVModel=FLVModel(this.getModel())
     NewColor.setColor(this.pasek,m.FLV_COLOR_LINE_PROGRESS_PRELOADER)
 }
 
///////////////////////////////////////////////////////////////////////////////////////////
 
 function hide(){
this._visible=false
 }
 
///////////////////////////////////////////////////////////////////////////////////////////
	
 function onMetaData(){
	  shov()
 }
 
//////////////////////////////////////////////////////////////////////////////////
 
 function onResize(){
	 var m:FLVModel=FLVModel(this.getModel())
	 var target:FLV=FLV(m.__flv)
	 var image:ImageView=target.__image
	 var y=image._y+image._height+21
	 this.__width= m.width-285
	 this.onProgressFilm()
 }
 
///////////////////////////////////////////////////////////////////////////////// 

 function onLoad(){
	
 }
 
 /////////////////////////////////////////////////////////////////////////////////////////
 
 function onStart(){
	  var m:FLVModel=FLVModel(this.getModel())
	 
	//if(m.getUrl()){
		
	//} 
  }
 
 //////////////////////////////////////////////////////////////////////////////////////////
 
 function onSetUrl(){
	 this.__visible=false
	 start_preloader()
	reset()
 }

 //////////////////////////////////////////////////////////////////////////////////////////
 
 function start_preloader(){
	
	  reset()
	  onProgressFilm()
	    clearInterval(__inter)
	  __inter=setInterval(this,'onProgressFilm',1)
	 
 }
 
//////////////////////////////////////////////////////////////////////////////////////////
 
 function reset(){
	  this.pasek._width=0 
	  this._rotation=90
	  this.onResize()
 }
 
//////////////////////////////////////////////////////////////////////////////////////////
  
}