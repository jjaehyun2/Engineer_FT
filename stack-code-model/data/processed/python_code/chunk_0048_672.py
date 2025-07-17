////////////////////////////////////////////////////////////////////////////////
//
//  CODE11.COM
//  Copyright 2011
//  licenced under GPU
//
//  @author		Romeo Copaciu romeo.copaciu@code11.com
//  @date		24 May 2011
//  @version	1.0
//  @site		code11.com
//
////////////////////////////////////////////////////////////////////////////////

package com.code11.google.calendar.valueObjects
{
	public class CalendarRequestVO
	{
		public function CalendarRequestVO(title:String,details:String = "",timeZone:String = "UTC",hidden:Boolean = false,color:String = "#2952A3", location:String = "") {
			data = new CalendarItem();
			data.title = title;
			data.details = details;
			data.timeZone = timeZone;
			data.hidden = hidden;
			data.color = color;
			data.location = location;
		}
		
		public var data:CalendarItem;
	}
	

}