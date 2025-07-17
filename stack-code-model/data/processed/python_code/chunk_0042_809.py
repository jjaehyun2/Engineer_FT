import templateNewsy.util.*;
import templateNewsy.mvc.*;
import templateNewsy.I.*


class templateNewsy.mvc.AbstractController implements Controller {
  private var model:Observable;
  private var view:View;

  
  public function AbstractController (m:Observable) {
  
    setModel(m);
  }
  
 
  
  public function setModel (m:Observable):Void {
    model = m;
  }

  
  public function getModel ():Observable {
    return model;
  }

  
  public function setView (v:View):Void {
    view = v;
  }

  
  public function getView ():View {
    return view;
  }
}