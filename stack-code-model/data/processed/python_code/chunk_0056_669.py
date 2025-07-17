import templateMove.util.*;
import templateMove.mvc.*
import templateMove.I.*
import templateMove.mvcFLV.*;

class templateMove.mvcFLV.PlayPauseView extends AbstractView {
	

	
	var button:MovieClip
	
///////////////////////////////////////////////////////////////////////////////////////////
	
  public function defaultController (model:Observable):Controller {
  return new PlayPauseController(model)
 }
	
///////////////////////////////////////////////////////////////////////////////////////////
 
 function PlayPause(){
	
 }
 
  ///////////////////////////////////////////
 
 function onResize(){
	 var m:FLVModel=FLVModel(this.getModel())
	 var target:FLV=FLV(m.__flv)
	 var image:ImageView=target.__image
	 var y=m.height-this._height-m.__toolsSymbolPosition
	 this._y=y
	
	  this._x=m.__marginToolsX1
 }
 
 /////////////////////////////////////////////////////////////////////////////////////////// 
 
   function onMetaData(obj){  
	 
		onResize()
	}
 

/////////////////////////////////////////////////////////////////////////////////////////// 

 function onLoad(){
	  var m:FLVModel=FLVModel(this.getModel())
	 /// NewColor.setColor(button.znaczek,m.FLV_COLOR_SYMBOL_BUTTON_ROLLOUT)
	 var c:PlayPauseController=PlayPauseController(this.getController())
		 
	 button.onPress=Delegate2.create(c,c.onPressPlay)
	 
	 ////rollover/rollout
	 button.onRollOver=Delegate2.create(this,onRollOverAll,button)
	 button.onRollOut=Delegate2.create(this,onRollOutAll,button)
			 
			 	 this.onResize()
 }
 
 ///////////////////////////////////////////////////////////////////////////////////////////

  function onRollOverAll(mc:MovieClip){
	   var m:FLVModel=FLVModel(this.getModel())
	  /// NewColor.setColor(button.znaczek,m.FLV_COLOR_SYMBOL_BUTTON_ROLLOVER)
	 mc.znaczek.gotoAndStop(2)
	m.sound_rol(this)
	
  }
  
  ///////////////////////////////////////////////////////////////////////////////////////////
  
  function onRollOutAll(mc:MovieClip){
	 mc.znaczek.gotoAndStop(1)
	 var m:FLVModel=FLVModel(this.getModel())
	/// NewColor.setColor(button.znaczek,m.FLV_COLOR_SYMBOL_BUTTON_ROLLOUT)
	
  }
 
 ///////////////////////////////////////////////////////////////////////////////////////////
  
 function onStart(){
	 button.gotoAndStop("stan_pause")
	 var m:FLVModel=FLVModel(this.getModel())
 }
 
///////////////////////////////////////////////////////////////////////////////////////////
 
 function onStop(){
		button.gotoAndStop("stan_play")
		 var m:FLVModel=FLVModel(this.getModel())
 }
 
 ///////////////////////////////////////////////////////////////////////////////////////////
  
 function onPauze(){
	button.gotoAndStop("stan_play")
    var m:FLVModel=FLVModel(this.getModel())
  }
 
 ///////////////////////////////////////////////////////////////////////////////////////////
 
 
 
 
 
	
  
}