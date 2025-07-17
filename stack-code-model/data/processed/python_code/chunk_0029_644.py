import templateMp3.util.*;
import templateMp3.mvc.*
import templateMp3.I.*
import templateMp3.mvcMp3.*;

class templateMp3.mvcMp3.VolumeView extends AbstractView {

var __scroll:ScrollComponents

////////////////////////////////////////////////////////////////////////////////
	
 public function defaultController (model:Observable):Controller {
  return new VolumeController(model)
 }
	
 ////////////////////////////////////////////////////////////////////////////////  
 
 function onLoad(){
	  var m:Mp3Model=Mp3Model(this.getModel())
	 this.create()
	 onChangedVolume()
	 this.__scroll.setScrollPosition(m.__volumeFirst)
	 this.onResize()	 
 }
 
////////////////////////////////////////////////////////////////////////////////  
 
function VolumeView(){
   
 }
 
 //////////////////////////////////////////////////////////////////////////////
 
 function create(){
	 var m:Mp3Model=Mp3Model(this.getModel())

	this.__scroll=ScrollComponents(this.attachMovie("_scrollProgressFLV","_scrollProgressFLV_",1,{__backgroundColor:m.MP3_VOLUME_COLOR_BACKGROUND,__colorCurrent:m.MP3_VOLUME_COLOR_CURRENT}))
	this.__scroll.addEventListener("onChangeSuwak",this)
	this.__scroll.addEventListener("onPressSuwak",this)
	this.__scroll.addEventListener("onReleaseSuwak",this)
	__scroll.__scaleBackground = false;
	__scroll.__rectangleHeightNull = true;
	__scroll.height =  93
	__scroll.firstLast = [0,100];
	__scroll._rotation=-90
	
	
	
	this.__scroll.mcBackground.onPress=Delegate2.create(this,this.onPressBackground)
	this.__scroll.mcBackground.onRelease=Delegate2.create(this,this.onReleaseBackground)
	this.__scroll.mcBackground.useHandCursor=false
	
	__scroll.setColorGlow(m.MP3_VOLUME_GLOW_COLOR_SCROLL)
	

	__scroll.setColorCircle(m.MP3_VOLUME_COLOR_CIRCLE)
	
	if(m.MP3_CIRCLE_VISIBLE=="false"){
				__scroll.rectangle._alpha=0
	}
	
	
	 
 }
 
 
/////////////////////////////////////////////////////////////////////////////////

function onPressBackground(){
	var m:Mp3Model=Mp3Model(this.getModel())
	__scroll.rectangle._y=__scroll._ymouse
	onChangeSuwak()
}

////////////////////////////////////////////////////////////////////////////////////

function onReleaseBackground(){
	
	
}

////////////////////////////////////////////////////////////////////////////////
  
 function onChangedVolume(){
	 var m:Mp3Model=Mp3Model(this.getModel())
	this.__scroll.setScrollPosition(m.volume)
	}
	

////////////////////////////////////////////////////////////////////////////////

function onPressSuwak(){
		
}

/////////////////////////////////

function onReleaseSuwak(){
	
}

////////////////////////////////////////////////////////////////////////////////

	function onPressScroll(){    

	}

////////////////////////////////////////////////////////////////////////////////

	function onReleaseScroll(){  
	
	}

////////////////////////////////////////////////////////////////////////////////

	function onChangeSuwak(){   
	var c:VolumeController=VolumeController(this.getController())
	c.onChangeScroll()
	}
	
////////////////////////////////////////////////////////////////////////////////

  function onMuteOff(){
	 this.__scroll._visible=false
  }

////////////////////////////////////////////////////////////////////////////////

  function onMuteOn(){
	  this.__scroll._visible=true
  }

////////////////////////////////////////////////////////////////////////////////

function onResize(){
	var m:Mp3Model=Mp3Model(this.getModel())
	
	this._x=24
	this._y=12
	
}

////////////////////////////////////////////////////////////////////////////////
  
  
 
 
 
 
	
  
}