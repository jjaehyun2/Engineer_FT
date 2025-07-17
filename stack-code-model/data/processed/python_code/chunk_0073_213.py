import templateSlider.mvcgallery.*
import templateSlider.mvc.*;
import templateSlider.util.*;
import templateSlider.I.*


class templateSlider.mvcgallery.ImageController extends AbstractController {
	
  public function ImageController (model:Observable) {
    super(model);
  }

 ////////////////////////////////////////////////////////////////////////////////////
 
  function onIntroEnd(){
	  var m:GalleryModel=GalleryModel(this.getModel())
	  var v:ImageView=ImageView(this.getView())
	  
	  if(m.isFlv()==false){
	  m.next_time()
	  }
	}
	
////////////////////////////////////////////////////////////////////////////////////

   function onExitEnd(){
	  var model:GalleryModel=GalleryModel(this.getModel())
		model.load()	
  }

 ////////////////////////////////////////////////////////////////////////////////////
  
 

  
}