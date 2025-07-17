import templateLoader.mvctemplate.*
import templateLoader.mvc.*
import templateLoader.I.*
import flash.display.BitmapData
import templateLoader.util.Observable

import mx.transitions.Tween
import mx.transitions.easing.*



 
  

class templateLoader.mvctemplate.FullScreenView extends AbstractView {
		
	



////////////////////////////////////////////////////////////

public function defaultController (model:Observable):Controller {
  return new FullScreenController(model)
 }
 
////////////////////////////////////////////////////////////

function onLoad(){

this.onResize()	

/*
var inter=setInterval(function(){
Stage["displayState"] = "fullScreen";
trace("full screen!")
clearInterval(inter)
},2000)

this.onPress()
/*/
}

/////////////////////////////////////////////////////////////////////////

function onResize(){
	var m:LoaderModel=LoaderModel(this.getModel())
		
	if(Stage["displayState"] == "fullScreen"){
	 this.gotoAndStop(1)
	}else{
	this.gotoAndStop(2)
	}
	
	this._x = m.width - this._width-10
	this._y=9

	
}

/////////////////////////////////////////////////////////////////////////

function onRelease(){
	if(Stage["displayState"] == "normal"||Stage["displayState"]==undefined){
		Stage["displayState"] = "fullScreen";
	}else{
		Stage["displayState"] = "normal";
	}
	
}

/////////////////////////////////////////////////////////////////////////
}