import templateMove.mvcFLV.*;
import templateMove.mvc.*;
import templateMove.util.*;
import templateMove.I.*


class templateMove.mvcFLV.PlayPauseController extends AbstractController {

 ///////////////////////////////////////////////////////////////////////////////////////////
	
  public function PlayPauseController (model:Observable) {
    super(model);
  }  
  
 ///////////////////////////////////////////////////////////////////////////////////////////
  
  function onPressPlay(){
	  
	  var m:FLVModel=FLVModel(this.getModel())
	  
	 if(m.stan=="stop"||m.stan=="pause"){
	  	 m.Start(m.getUrl())
	 }else{
		m.Pause()
	 }
	  
	 
  }
  
/////////////////////////////////////////////////////////////////////////////////////////
  
   function onPressPause(){
	  var m:FLVModel=FLVModel(this.getModel())
	  m.Pause()
  }
  
 
 
////////////////////////////////////////////////////////////////////////////////////////
 
  
 

  
}