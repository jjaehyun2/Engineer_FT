import templateMove.mvcFLV.*;
import templateMove.mvc.*;
import templateMove.util.*;
import templateMove.I.*


class templateMove.mvcFLV.SpeakerController extends AbstractController {

 ///////////////////////////////////////////////////////////////////////////////////////////
	
  public function SpeakerController (model:Observable) {
    super(model);
  }  

///////////////////////////////////////////////////////////////////////////////////////////
  
  
  function onPressVolume(){
	   var m:FLVModel=FLVModel(this.getModel())
	   if(m.soundEnabled==true){
	 m.soundEnabled=false
	   }else{
		 m.soundEnabled=true
		   
	   }
	 
 }
   
 
////////////////////////////////////////////////////////////////////////////////////////
  
 

  
}