////////////////////////////////////////////////////////////////////////////////
	//
	// Copyright (c) 2010 ESRI
	//
	// All rights reserved under the copyright laws of the United States.
	// You may freely redistribute and use this software, with or
	// without modification, provided you include the original copyright
	// and use restrictions.  See use restrictions in the file:
	// <install location>/License.txt
	//
	////////////////////////////////////////////////////////////////////////////////
package widgets.LocatePoint.components.supportClasses
{
		import com.esri.ags.geometry.MapPoint;
		
		import flash.events.EventDispatcher;
		
		[Bindable]
		[RemoteClass(alias="widgets.LocatePoint.LocateResult")]
		
		public class LocateResult extends EventDispatcher
		{
			public var title:String;
			
			public var icon:String;
			
			public var content:String;
			
			public var point:MapPoint;
			
			public var link:String;
			
			public var selected:Boolean;
		}
		
	}