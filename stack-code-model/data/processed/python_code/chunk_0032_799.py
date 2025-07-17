import templateMove.util.*;
import templateMove.mvc.*;
import templateMove.I.*

/////////////////////////////////////////////////////////////////////////////
class templateMove.mvc.AbstractView extends MovieClip implements View {
  private var model:Observable;
  private var controller:Controller;

  /////////////////////////////////////////////////////////////////////////////
  
  public function AbstractView (m:Observable, c:Controller) {
   
    setModel(m);
  
    if (c !== undefined) {
      setController(c);
    }
  }

  public function defaultController (model:Observable):Controller {
    return null;
  }

 /////////////////////////////////////////////////////////////////////////////
 
  public function setModel (m:Observable):Void {
    model = m;
  }

 /////////////////////////////////////////////////////////////////////////////
 
  public function getModel ():Observable {
    return model;
  }

 /////////////////////////////////////////////////////////////////////////////
 
  public function setController (c:Controller):Void {
    controller = c;
    // Tell the controller this object is its view.
    getController().setView(this);

  }

  /////////////////////////////////////////////////////////////////////////////
  
  public function getController ():Controller {
       if (controller === undefined) {
    
      setController(defaultController(getModel()));
    }
    return controller;
  }

 /////////////////////////////////////////////////////////////////////////////
  
  public function update(o:Observable, infoObj:Object):Void {
  }
  
  /////////////////////////////////////////////////////////////////////////////
  
}