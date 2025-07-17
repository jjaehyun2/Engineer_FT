import templateMp3.util.*;
import templateMp3.mvc.*
import templateMp3.I.*
import templateMp3.mvcMp3.*;

class templateMp3.mvcMp3.ToolsMp3View extends AbstractView {
	var mc_next:MovieClip
	var mc_prev:MovieClip
	var mc_play_pause:MovieClip
	var mc_stop:MovieClip
	
	var __colorRol="0xF7A400"
	var __colorOut="0xCCCCCC"
////////////////////////////////////////////////////////////////////////////////
	
public function defaultController (model:Observable):Controller {
  return new ToolsMp3Controller(model)
 }
 
 /////////////////////////////////////////////////
 
 function ToolsMp3View(){
	 	 
	
 }
 
 /////////////////////////////////////////////////////////////////////////////
 
 function onInit(){
	var m:Mp3Model=Mp3Model(this.getModel())
	if(m.__array.length<=1){
		this.mc_next._visible=false
		this.mc_prev._visible=false
	}
 }
	
 ////////////////////////////////////////////////////////////////////////////////
 
  function onLoad(){
	 var m:Mp3Model=Mp3Model(this.getModel())
	 this.__colorRol=m.MP3_TOOLS_COLOR_ROL
	 this.__colorOut=m.MP3_TOOLS_COLOR_OUT
	 
	 createNavi()
	 this.onResize()
 }
 
 ////////////////////////////////////////////////////////////////////////////////
  
 function createNavi(){
	 var c:ToolsMp3Controller=ToolsMp3Controller(this.getController())
	 this.mc_next.onPress=Delegate2.create(c,c.onNext)
	 this.mc_prev.onPress=Delegate2.create(c,c.onPrev)
	 this.mc_stop.onPress=Delegate2.create(c,c.onStop)
	 this.mc_play_pause.onPress=Delegate2.create(c,c.onPlayPause)
	 
	 var array_mc=[mc_next,mc_prev,mc_stop,mc_play_pause]
	 for(var i in array_mc){
		 var mc:MovieClip=array_mc[i]
		 setColor(mc,this.__colorOut)
		 mc.onRollOver=Delegate2.create(this,this.onRollOverTools,mc)
		 mc.onRollOut=Delegate2.create(this,this.onRollOutTools,mc)
		 
	 }
	 
 }
 
 ////////////////////////////////////////////////////////////////////////////////
 
 function onPlay(){
	 this.mc_play_pause.gotoAndStop(2)
	 
	 if(!mc_play_pause.hitTest(_root._xmouse,_root._ymouse,true)){
	  onRollOutTools(mc_play_pause)
	 }
 }
 
 /////////////////////
 
 function setColor(mc_,color_){
	 var k:Color=new Color(mc_.symbol)
	// k.setRGB(color_)
 }
 
 //////////////////////////////////////////////////
 
 function onRollOverTools(mc:MovieClip){
	 this.setColor(mc,this.__colorRol)
}
 
 ////////////////////////////////////////////////////
 
 function onRollOutTools(mc){
	 this.setColor(mc,this.__colorOut)
 }
 
 ////////////////////////////////////////////////////////////////////////////////
 
 function onStop(){
	 	this.mc_play_pause.gotoAndStop(1)
		onRollOutTools(mc_play_pause)
 }
 
 ////////////////////////////////////////////////////////////////////////////////
 
 function onPause(){
	  this.mc_play_pause.gotoAndStop(1)
 }
 
////////////////////////////////////////////////////////////////////////////////

function onResize(){
	
	var m:Mp3Model=Mp3Model(this.getModel())
	
	this._x=180
	this._y=-3
	
}

////////////////////////////////////////////////////////////////////////////////
 
	
  
}