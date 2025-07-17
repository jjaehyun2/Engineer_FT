import templateMove.mvcFLV.*;
import templateMove.mvc.*;
import templateMove.util.*;
import templateMove.I.*


class templateMove.mvcFLV.ProgressController extends AbstractController {

 	
var __przedWcisnieciem   /////jaki stan byl odtwarzacza przed nacisnieciem na suwak:)

		
///////////////////////////////////////////////////////////////////////////////////////////

  public function ProgressController (model:Observable) {
    super(model);
  }
  
//////////////////////////////////////////////////////////////   

  function onChangeSuwak(){
	  var m:FLVModel=FLVModel(this.getModel())
	  var v:ProgressView=ProgressView(this.getView())
	  var value=v.__scroll.getScrollPosition()
	   m.position=value
 }

 ///////////////////////////////////////////////////////////////////////////////////////////
 
 function onPressSuwak(){  
	  var m:FLVModel=FLVModel(this.getModel())
	  this.__przedWcisnieciem=m.stan
	  m.Pause()
 }
 
///////////////////////////////////////////////////////////////////////////////////////////

 function onReleaseSuwak(){
	  var m:FLVModel=FLVModel(this.getModel())
	  if(this.__przedWcisnieciem=="play"){ ///jesli przed wcisniem suwaka suwak sie poruszal
	 m.Start()
	 }
}

//////////////////////////////////////////////////////////////   
 

  
}