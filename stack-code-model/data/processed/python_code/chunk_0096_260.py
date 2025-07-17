import templateMp3.mvcMp3.*;
import templateMp3.mvc.*;
import templateMp3.util.*;
import templateMp3.I.*


class templateMp3.mvcMp3.SpeakerView extends AbstractView {
	var mc_speaker:MovieClip
	
////////////////////////////////////////////////////////////////////////////////	

public function defaultController (model:Observable):Controller {
  return new SpeakerController(model)
 }
  
//////////////////////////////////////////////////////////////////////////////// 
  
  function onLoad(){
	  var m:Mp3Model=Mp3Model(this.getModel())
	  var c:SpeakerController=SpeakerController(this.getController())
	  this.mc_speaker.onPress=Delegate2.create(c,c.onPressSpeaker)	  
	  this.mc_speaker.onRollOver=Delegate2.create(this,this.onRollOverSpeaker)	
	  this.mc_speaker.onRollOut=Delegate2.create(this,this.onRollOutSpeaker)
	  
	  this.setColor(this.mc_speaker,m.MP3_SPEAKER_COLOR_OUT)
  }
  
/////////////////////
 
 function setColor(mc_,color_){
	 var k:Color=new Color(mc_.symbol)
	  k.setRGB(color_)
 }
 
 //////////////////////////////////////////////////
  
   function onMuteOff(){
	  this.gotoAndStop(2)
  }
 
 ////////////////////////////////////////////////////////////////////////////////
 
  function onMuteOn(){
	  this.gotoAndStop(1)
  }

 ////////////////////////////////////////////////////////////////////////////////
 
 function onRollOverSpeaker(){
	var m:Mp3Model=Mp3Model(this.getModel())
	 this.setColor(this.mc_speaker,m.MP3_SPEAKER_COLOR_ROL)
 }
 
 ///////////////////
 
 function onRollOutSpeaker(){
	 var m:Mp3Model=Mp3Model(this.getModel())
	this.setColor(this.mc_speaker,m.MP3_SPEAKER_COLOR_OUT)
	 
 }
 
 //////////////////////
  
 

  
}