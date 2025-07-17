import templateList.util.*;
import templateList.mvc.*;
import templateList.I.*



interface templateList.I.Controller {
 
  public function setModel (m:Observable):Void;

 
  public function getModel ():Observable;

  
  public function setView (v:View):Void;

 
  public function getView ():View;
}