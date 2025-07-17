import smallCalendar.mvc.*
import smallCalendar.I.*
import smallCalendar.mvctemplate.*
import smallCalendar.util.Observable


 
class smallCalendar.mvctemplate.Calendar{
 var __model:CalendarModel
 var __target:MovieClip
 static var __instance:Calendar
 
 ///////////View
 var __background:BackgroundView
 var __tools:ToolsView  ///toools
 var __month:MonthView ///container month
 var __title:TitleView
 
 ///navi view
 var __nextMonth:NextMonthView
 var __prevMonth:PrevMonthView
 
 //////desc
 var __desc:DescView
 
//////////////////////////////////////////////////////////////////////////////////////////////////////
  
  static function getInstance(){
	  if(Calendar.__instance==undefined){
		  trace("WARNING !!! - Calndar NOT instance!")		  
	  }
	  return __instance
  }
  
//////////////////////////////////////////////////////////////////////////////////////////////////////
  
  public function Calendar(target:MovieClip) {
	  this.__target=target
	 __instance=this
	
   	 __model=new CalendarModel(this)
			
	/////////////////////////tools
	__tools=ToolsView(target.attachMovie("_tools","_toolse_",3452,{_x:0,_y:0}))
	__tools.setModel(__model)
	
	/////////////////////////month container
	this.__month=MonthView(target.attachMovie("_month","_month_",2,{_x:0,_y:20}))
	this.__month.setModel(__model)
	this.__model.addEventListener("onUpdate",this.__month)
	
	/////////////////////////title view
	this.__title=TitleView(target.attachMovie("_titleCalendarView","_titleCalendarView_",32432,{_x:0,_y:0}))
	this.__title.setModel(__model)
	this.__model.addEventListener("onUpdate",this.__title)
	
		
	////////////////////////nextMonthButton
	this.__nextMonth=NextMonthView(this.__tools.attachMovie("_nextMonthView ","_nextMonthView_",43))
	this.__nextMonth.setModel(__model)
	this.__model.addEventListener("onUpdate",this.__nextMonth)
	
	////////////////////////prevMonthButton
	this.__prevMonth=PrevMonthView(this.__tools.attachMovie("_prevMonthView","_prevMonthView_",47))
	this.__prevMonth.setModel(__model)
	this.__model.addEventListener("onUpdate",this.__prevMonth)
	
	
	///////////////////////desc
	this.__desc=DescView(target.attachMovie("_descView","_descView_",677,{_x:0,_y:0}))
	this.__desc.setModel(__model)
	__model.addEventListener("onUpdate",this.__desc)
	__model.addEventListener("onPressNumber", this.__desc);
	
	
	
  }
  
//////////////////////////////////////////////////////////////////////////////////////////////////////

 

}