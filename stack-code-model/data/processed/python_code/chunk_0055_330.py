import templateMove.util.*;
import templateMove.mvc.*
import templateMove.I.*
import templateMove.mvcFLV.*;

class templateMove.mvcFLV.FullScreenView extends AbstractView {
		
	var button:MovieClip
	
///////////////////////////////////////////////////////////////////////////////////////////
	
  public function defaultController (model:Observable):Controller {
  return new FullScreenController(model)
 }
	
///////////////////////////////////////////////////////////////////////////////////////////
 
 function SpeakerView(){
	
 }
 
/////////////////////////////////////////////////////////////////////////////////////////// 

 function onLoad(){
	  var m:FLVModel=FLVModel(this.getModel())
	  var m:FLVModel=FLVModel(this.getModel())
	 ///NewColor.setColor(button.symbol,m.FLV_COLOR_SYMBOL_BUTTON_ROLLOUT)
	  
	 var c:FullScreenController=FullScreenController(this.getController())
		 
	 button.onPress=Delegate2.create(c,c.onPressScreen)
	 
	 ////rollover/rollout
	 button.onRollOver=Delegate2.create(this,onRollOverAll,button)
	 button.onRollOut=Delegate2.create(this,onRollOutAll,button)
	 this.onResize()
	 
	 
	 if(m.fullScreen==false){
		 m.fullScreen=false
	 }
	 
	 
 }
 
////////////////////////////////////////////////////////////////////////////////////////
 
 function onResize(){
	 var m:FLVModel=FLVModel(this.getModel())
	 var target:FLV=FLV(m.__flv)
	 var image:ImageView=target.__image
	
	 this._y=m.height-15-m.__toolsSymbolPosition
	 this._x=m.width-m.__marginToolsX2-(this._width+1)
	 
	 if (Stage["displayState"] == "fullscreen") {
		onFullScreenYes()
	} else {
		onFullScreenNo()
	}
}
 
 /////////////////////////////////////////////////////////////////////////////////////////// 
 
   function onMetaData(obj){  
	 	///onResize()
	}
 

/////////////////////////////////////////////////////////////////////////////////////////// 

  function onRollOverAll(mc:MovieClip){
	 mc.gotoAndStop(2)
	  var m:FLVModel=FLVModel(this.getModel())
	 // NewColor.setColor(mc.symbol,m.FLV_COLOR_SYMBOL_BUTTON_ROLLOVER)
	/// button.symbol.gotoAndStop(2)	
	  m.sound_rol(this)
  }
  
 ///////////////////////////////////////////////////////////////////////////////////////////
  
  function onRollOutAll(mc:MovieClip){
	mc.gotoAndStop(1)
	 //button.symbol.gotoAndStop(1)	
	 
	 
		 var m:FLVModel=FLVModel(this.getModel())
	 ////NewColor.setColor(mc.symbol,m.FLV_COLOR_SYMBOL_BUTTON_ROLLOUT)
	
  }
  
 ///////////////////////////////////////////////////////////////////////////////////////////
 
function onFullScreenYes(){
	//this.button.symbol.gotoAndStop(2)	
}

 ///////////////////////////////////////////////////////////////////////////////////////////

function onFullScreenNo(){
	//this.button.symbol.gotoAndStop(1)		
}

/////////////////////////////////////////////////////////////////////////////////////////

// function to enable, disable context menu items, based on which mode we are in.
function menuHandler(obj, menuObj) {
	if (Stage["displayState"] == "normal") {
		// if we're in normal mode, enable the 'go full screen' item, disable the 'exit' item
		menuObj.customItems[0].enabled = true;
		menuObj.customItems[1].enabled = false;
	} else {
		// if we're in full screen mode, disable the 'go full screen' item, enable the 'exit' item
		menuObj.customItems[0].enabled = false;
		menuObj.customItems[1].enabled = true;
	}
}

/////////////////////////////////////////////////////////////////////////////////////////////////////

function create_menu(){
var m:FLVModel=FLVModel(this.getModel())
var fullscreenCM:ContextMenu = new ContextMenu(menuHandler);
fullscreenCM.hideBuiltInItems();
var fs:ContextMenuItem = new ContextMenuItem("Go Full Screen", Delegate2.create(m,m.full_screen));
fullscreenCM.customItems.push(fs);
var xfs:ContextMenuItem = new ContextMenuItem("Exit Full Screen",Delegate2.create(m,m.full_screen));
fullscreenCM.customItems.push(xfs);
m.__flv.__container.menu = fullscreenCM;
	
}

///////////////////////////////////////////////////////////////////////////////////////////////////////
 
 
	
  
}