import smallCalendar.mvctemplate.*
import smallCalendar.mvc.*;
import smallCalendar.util.*;
import smallCalendar.I.*


class smallCalendar.mvctemplate.MonthController extends AbstractController {
	 
	
	 
  public function MonthController (model:Observable) {
    super(model);
  }
    
  
/////////////////////////////////////////////////////////////////////////////
  
  function onPressRow(mc:MovieClip){
	  var m:CalendarModel=CalendarModel(this.getModel())
	  var v:MonthView=MonthView(this.getView())
	  m.dispatchEvent({target:mc,type:"onPressNumber"})
  }
  
/////////////////////////////////////////////////////////////////////////////
	
  
 

  
}