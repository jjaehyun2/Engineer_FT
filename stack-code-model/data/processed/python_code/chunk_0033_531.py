import templateMp3.util.*;
import templateMp3.mvc.*;
import templateMp3.I.*


interface templateMp3.I.View {
  public function setModel (m:Observable):Void;
  public function getModel ():Observable;
  public function setController (c:Controller):Void;
  public function getController ():Controller;
  public function defaultController (model:Observable):Controller;
}