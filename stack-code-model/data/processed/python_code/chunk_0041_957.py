import templateMp3.util.*;
import templateMp3.mvc.*
import templateMp3.I.*
import templateMp3.mvcMp3.*;

class templateMp3.mvcMp3.ContainerRootView extends AbstractView {

var background:MovieClip
	
////////////////////////////////////////////////////////////////////////////////

public function defaultController (model:Observable):Controller {
  return new ContainerRootController(model)
 }
 
 ///////////////////////////////////////////////////////////////
 
 function onLoad(){
	   var m:Mp3Model=Mp3Model(this.getModel())
	  this.setColor(this.background.background2,m.MP3_BACKGROUND_COLOR) 
	  
	  
	  if(m.MP3_GLOW_COLOR.length){
	    var obj=background.filters[0]
		obj.color=m.MP3_GLOW_COLOR
		background.filters=new Array(obj)
	  }else{
		background.filters=undefined
		  
	  }
		
		
	 
	 this.onResize()
	 Stage.addListener(this)
 }
	
 ///////////////////////////////////////////////////////////////
 
 function ContainerRootView (){
	 this.background.background2.swapDepths(1111)
 }
 
 ///////////////////////////////////////////////////////////////
 
 function onSetSize(){
	   var m:Mp3Model=Mp3Model(this.getModel())
	   
	   this.onResize()
 }
 
 ///////////////////////////////////////////////////////////////
 
 function setColor(mc_,color_){
	 var k:Color=new Color(mc_)
	 k.setRGB(color_)
 }
 
 /////////////////////////////////////////////////////////////////////////
 
 function onResize(){
	 var m:Mp3Model=Mp3Model(this.getModel())
	 this.background.background2._width=m.width
 }
 
 //////////////////////////////////////////////////////////////////////
	
  
}