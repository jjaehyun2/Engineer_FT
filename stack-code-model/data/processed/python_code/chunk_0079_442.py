import templateMove.mvcFLV.*;
import templateMove.mvc.*;
import templateMove.util.*;
import templateMove.I.*


class templateMove.mvcFLV.SoundController extends AbstractController {

 	
/////////////////////////////////////////////////////////////

  public function SoundController (model:Observable) {
	super(model);
	
  }
  
//////////////////////////////////////////////////////////////  

function onChangeSuwak(){
	var m:FLVModel=FLVModel(this.getModel())
	var v:SoundView=SoundView(this.getView())
		
	var value=v.__scroll.getScrollPosition()
	m.volume=value
}

//////////////////////////////////////////////////////////////   




  
}