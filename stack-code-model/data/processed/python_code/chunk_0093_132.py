import pl.drawing.Rysowanie
import smallCalendar.mvctemplate.*
import smallCalendar.mvc.*
import smallCalendar.I.*
import flash.display.BitmapData
import smallCalendar.util.Observable
import smallCalendar.Configuration
 
class smallCalendar.mvctemplate.MonthView extends AbstractView {
var model	
	
var __container:MovieClip	
var __containerWeek:MovieClip
var __width:Number
var __height:Number
var __spaceX:Number
var __spaceY:Number
var __maxColumns:Number

////////////////////////////////////////////////////////////////////////////////////////////////////

public function defaultController (model:Observable):Controller {
  return new MonthController(model)
 }

////////////////////////////////////////////////////////////////////////////////////////////////////

function MonthView(){
this.updateVars()
}

///////////////////////////////////////////////////////////////////////////////////////////////////

function updateVars(){
var m:CalendarModel=CalendarModel(this.getModel())
__width=m.__width
__height=m.__height
__spaceX=m.__spaceX
__spaceY=m.__spaceY	
__maxColumns=m.__maxColumns
}
 
////////////////////////////////////////////////////////////////////////////////////////////////////
 
function onLoad(){
	create_day_week()
}

////////////////////////////////////////////////////////////////////////////////////////////////////

function onUpdate(){
	updateVars()
	create_day_week()
	this.create()	
}

////////////////////////////////////////////////////////////////////////////////////////////////////

function create(){
	var c:MonthController=MonthController(this.getController())
	var m:CalendarModel=CalendarModel(this.getModel())
	var month=m.month
	var year=m.year
    ///////////////////////////////////////////////////////
	var firstColumns:Number=m.getColumnsFirstDayWeek()
	var allNumber:Number=new Date(year,month+1,0).getDate()  ////all number in monat
	////////////////////////////////////////////////////////
	var counter:Number=1
	var counterColumns:Number=firstColumns
	var old:MovieClip
	this.__container=this.createEmptyMovieClip("mcContainer",1)
	this.__container._y=20
	
	for(var all_mc in this.__container){
		var mc:MovieClip=this.__container[all_mc]
		mc.stopTween()
	}
	
	for(var i=firstColumns;i<(firstColumns+allNumber);i++){
		var row:MovieClip=this.__container.attachMovie("_numberCalendar","row"+i,i)
		
		////////////background
		row.background._width=m.__width
		row.background._height=m.__height
		
		
		
		row.selectedItem={}
		row.selectedItem.day=m.format_number(counter)
		row.selectedItem.month=m.format_number(m.month+1)
		row.selectedItem.year=m.format_number(m.year)
		row.onPress=Delegate2.create(c,c.onPressRow,row)
		var format:TextFormat=new TextFormat()
		format.size=m.__numberSize
		format.color=Configuration.COLOR_NUMBER
		row.t.text=counter
		row.t.setTextFormat(format)
		
		//////////////textField
		row.t.autoSize=true
		row.t._x=m.__width/2-row.t._width/2
		row.t._y=m.__height/2-row.t._height/2
		
		
		/////BACKGROUND NUMBER
		var k:Color=new Color(row.background.background2)
		k.setRGB(Configuration.COLOR_BACKGROUND_NUMBER)
		
			
		
		///////////////////////////////////////////today select
		if(m.__date.getDate()==counter&&m.month==m.today_month&&m.year==m.today_year){
		row.mcFrame.gotoAndStop(2)
		row.mcFrame._width=m.__width
		row.mcFrame._height=m.__height
		
		///////color frame today
		var k:Color=new Color(row.mcFrame)
		k.setRGB(Configuration.COLOR_FRAME_TODAY)
		
		/////auto display the event for the current date
		if(Configuration.AUTO_DISPLAY_EVENT=="true"){
		row.onPress()
		}
	
		}
		
		
		///////////////////////////////////events select
		if(m.getEvents(year,(month+1),counter)!=undefined){
		var obj=row.background.filters[0]
		obj.color=Configuration.COLOR_GLOW_EVENTS
		row.background.filters=new Array(obj)
		}else{
		var obj=row.background.filters[0]
		obj.color=Configuration.COLOR_GLOW_NORMAL
		row.background.filters=new Array(obj)			
		}
		
		row._x=(!old) ? firstColumns*(__width+__spaceX) : (old._x+__width+__spaceX)
		row._y=(!old) ? 0 : old._y
		
		row._alpha=0
		row.stopTween()
		row.tween('_alpha',100,1,'easeOutCubic',counter/70,{})
	
		
		
		
		
		if(counterColumns>__maxColumns){
			row._x=0
			row._y+=(__height+__spaceY)
			counterColumns=0
		}
		counter++
		counterColumns++
		old=row
	}
	
}

////////////////////////////////////////////////////////////////////////////////////////////////////

function create_day_week(){
	var m:CalendarModel=CalendarModel(this.getModel())
	var array:Array=m.__dayWeek
	
	
	this.__containerWeek=this.createEmptyMovieClip("mcDayWeek",5)
	this.__containerWeek._y=0
	
	for(var i=0;i<array.length;i++){
		var label=array[i].label
		var index=array[i].index
		
		var day:MovieClip=this.__containerWeek.attachMovie("_numberCalendar","row"+index,i)
		///trace(day)
		day.background._visible=false
		day.t._width=m.__width
		day._x=i*(__width+__spaceX)
		day.t.text=label.substr(0,2)
		day.t.textColor=Configuration.COLOR_NUMBER_WEEK
		
	}
		
}


////////////////////////////////////////////////////////////////////////////////////////////////////



 

}