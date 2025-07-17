import templateMp3.util.*;
import templateMp3.mvc.*
import templateMp3.I.*
import templateMp3.mvcMp3.*;

/**
* ...
* @author Default
* @version 0.1
*/

class templateMp3.mvcMp3.BufferView extends AbstractView {

	  
	var __oldPosition:Number
	var circle:MovieClip
///////////////////////////////////////////////////////////////////////////////////////

	public function BufferView() {
		
	}
	 
///////////////////////////////////////////////////////////////////////////////////////
	
  public function defaultController (model:Observable):Controller {
  return new BufferController(model)
 }
 
///////////////////////////////////////////////////////////////////////////////////////

function onLoad(){
this.onResize()
}

/////////////////////////////////////////////////////////////////////////////

function onResize(){
	
	var m:Mp3Model=Mp3Model(this.getModel())
	this._x=278
	this._y=4
	
}

//////////////////////////////////////////////////////////////////////////////////////////

function onProgressPlay(){
		var m:Mp3Model=Mp3Model(this.getModel())
		
		var position:Number=m.__sound.position
		
		
		
		if(position!=this.__oldPosition){
			this.gotoAndStop(1)		
			this.setColor(this,m.MP3_BUFFER_COLOR)
		}else{
			this.gotoAndStop(2)	
			this.setColor(this,m.MP3_BUFFER_COLOR)
		}
		
		
		this.__oldPosition=position
	
		
}

//////////////////////////////////////////////////////////////////////////////////////////////////

function setColor(mc_,color_){
	var k:Color=new Color(mc_)
	k.setRGB(color_)
}

//////////////////////////////////////////////////////////////////////////////////////////////////






	
}