package services.vo
{
	import flash.display.DisplayObject;
	import flash.geom.Point;
	
	import framework.model.AppModelLocator;
	import framework.view.pages.inHouse.data.ValidateType;
	import services.vo.backend.RoomTypesObjectVO;
	import services.vo.backend.RoomWithBedTypesObjectVO;
	import services.vo.hotels.HotelInfoTotalVO;
	
	import mx.collections.ArrayCollection;
	import mx.controls.DateField;
	import mx.controls.ToolTip;
	import mx.managers.ToolTipManager;
	
	public class GlobalFunctions
	{
		public static function createAdressOfHotel(data:HotelInfoTotalVO):String
		{
			var str:String;
			if (data.sHotelName == null)
			{
				str = "";
			}
			else
			{
				str = data.sHotelName + " Addr.: ";
				if (data.sHotelCountry != null)
					str += data.sHotelCountry + " ";
				if (data.sHotelRegion != null)
					str = str + data.sHotelRegion + " ";
				if (data.sHotelCity != null)
					str = str + data.sHotelCity + " ";
				if (data.sHotelStreet != null)
					str = str + data.sHotelStreet;
				if (data.sHotelPhone != null)
					str = str + " Tel.: " + data.sHotelPhone;
			}
			return str; 
		}
		
		
		/**
		*	Compare two DateField. If first argumen > second argument - replace
		*/
		public static function compareDateFields(d1:Date, d2:Date):void
		{
			var tempDate:Number = 0;
			if (d1.time > d2.time)
			{
				tempDate = d1.time;
				d1.time = d2.time;
				d2.time = tempDate;
			}
		}
		
		public static function cleareHotelSettings():void
		{
			AppModelLocator.getInstance().hotelsModule.hotelRoomTypes.removeAll();
			GlobalStorage.vipHotel.removeAll();
			AppModelLocator.getInstance().hotelsModule.stageDP.removeAll();
			AppModelLocator.getInstance().hotelsModule.hotelRoomSettings.removeAll();
		}
		
		// convert to need format
		public static function dateConvert(item:String):String
		{
			var res:String;			
			var dateTemp:Date = DateField.stringToDate(item, GlobalSettings.DATE_SERVER_FORMAT);
			res = DateField.dateToString(dateTemp, GlobalSettings.DATE_FORMAT);
			return res;
		}
		
		public function GlobalFunctions()
		{
		}
		
		public static function stringToNumber(value:String):Number
		{
			return (isNaN(Number(value))) ? 0 : Number(value);
		}
		
		public static function search(from:ArrayCollection, what:String, sortBy:Array):ArrayCollection
		{
		
			var objects:ArrayCollection = new ArrayCollection();
			var myReg:RegExp = new RegExp(what,'i');
			
			for (var jj:int = 0; jj < sortBy.length; jj ++)
				for (var ii:int = 0; ii < from.length; ii ++)
				{
					if(!myReg.test(from[ii][sortBy[jj]])) continue;
					if(from[ii][sortBy[jj]] == "") continue;
					
					if (!objects.contains(from[ii]))
					objects.addItem(from[ii]);
				} 
			return objects;
		}
		
		// type of item array collection is RoomWithBedTypeVO 
		public static function searchRoomType(from:ArrayCollection, what:String, sortBy:Array):ArrayCollection
		{
			var ii:int = 0;
			var jj:int = 0;
			var kk:int = 0;
			
			var objects:ArrayCollection = new ArrayCollection();
			var myReg:RegExp = new RegExp(what,'i');
			
			for (jj = 0; jj < sortBy.length; jj ++)
			{
				if (sortBy[jj] == "sQualityName")
				{
					for (ii = 0; ii < from.length; ii ++)
					{
						if(!myReg.test((from[ii] as RoomWithBedTypesObjectVO).oRoomQuality[sortBy[jj]])) continue;
						if((from[ii] as RoomWithBedTypesObjectVO).oRoomQuality[sortBy[jj]] == "") continue;
						
						if (!objects.contains(from[ii]))
						objects.addItem(from[ii]);
					}
				}
				
				if (sortBy[jj] == "sTypeName")
				{
					for (ii = 0; ii < from.length; ii ++)
					{
						if ((from[ii] as RoomWithBedTypesObjectVO).aRoomWithBedTypes != null)
						{
							for (kk = 0; kk < (from[ii] as RoomWithBedTypesObjectVO).aRoomWithBedTypes.length; kk ++)
							{
								if(!myReg.test((from[ii] as RoomWithBedTypesObjectVO).aRoomWithBedTypes[kk].oBedType[sortBy[jj]])) continue;
								if((from[ii] as RoomWithBedTypesObjectVO).aRoomWithBedTypes[kk].oBedType[sortBy[jj]] == "") continue;
							
								if (!objects.contains(from[ii]))
								objects.addItem(from[ii]);
							}
						}
						/* else // it's standalon
						{
							if(!myReg.test((from[ii] as RoomWithBedTypesObjectVO).flx_oRoomStandalone.oBedType[sortBy[jj]])) continue;
								if((from[ii] as RoomWithBedTypesObjectVO).flx_oRoomStandalone.oBedType[sortBy[jj]] == "") continue;
							
								if (!objects.contains(from[ii]))
								objects.addItem(from[ii]);
						} */
						
					}
				}
				
				
				
				
				
				if (sortBy[jj] == "sShortName" || sortBy[jj] == "sDescription")
				{
					for (ii = 0; ii < from.length; ii ++)
					{
						if ((from[ii] as RoomWithBedTypesObjectVO).aRoomWithBedTypes != null)
						{
							for (kk = 0; kk < (from[ii] as RoomWithBedTypesObjectVO).aRoomWithBedTypes.length; kk ++)
							{
								if(!myReg.test((from[ii] as RoomWithBedTypesObjectVO).aRoomWithBedTypes[kk][sortBy[jj]])) continue;
								if((from[ii] as RoomWithBedTypesObjectVO).aRoomWithBedTypes[kk][sortBy[jj]] == "") continue;
							
								if (!objects.contains(from[ii]))
								objects.addItem(from[ii]);
							}
						}
						else
						{
								if(!myReg.test((from[ii] as RoomWithBedTypesObjectVO).flx_oRoomStandalone[sortBy[jj]])) continue;
								if((from[ii] as RoomWithBedTypesObjectVO).flx_oRoomStandalone[sortBy[jj]] == "") continue;
							
								if (!objects.contains(from[ii]))
								objects.addItem(from[ii]);
						}
						
					}
				}
			}
			
			return objects;
		}
		
		
		public static function getRoomTypeByQualityId(id:Number):RoomTypesObjectVO
		{
			var rtDP:ArrayCollection = AppModelLocator.getInstance().roomTypesModule.roomTypesDP;
			
			for(var i:int=0;i<rtDP.length;i++)
			{
				if((rtDP.getItemAt(i) as RoomWithBedTypesObjectVO).oRoomQuality.lQualityId == id)
					return rtDP.getItemAt(i) as RoomTypesObjectVO;
			} 
			
			return null;
		}
		
		public static function getDate():Date
		{
			var currDate:Date = new Date(AppModelLocator.getInstance().lCurrentTime);
			
			return currDate;
		}
		
		
		private static var errorTip:ToolTip;
		private static var error:String;
		
		public static function clearErrorTip():void
		{
			if (errorTip)
			{
				ToolTipManager.destroyToolTip(errorTip);
				errorTip = null;
			}
		}
		
		public static function validateEntry(type:String, target:DisplayObject):void
		{
			if (errorTip) clearErrorTip();
			
			// NOTE: Validation logic would go here.
			switch(type)
			{
				case ValidateType.NAMES_LENGTH:
					error = "Minimum 2 letters";
					break;
				case ValidateType.PASSPORT_LENGTH:
					error = "Passport have to contain 10 letters";
					break;
				case ValidateType.ROOM_NUMBER:
					error = "Please enter only numbers";
					break;
				case ValidateType.FIRST_NAME:
				case ValidateType.LAST_NAME:
				case ValidateType.COMPANY_NAME:
					error = "Please enter only letters";
					break;
				case ValidateType.ZIP_CODE:
					error = "Please enter min 5 letters";
					break;
			}
			
			var coord:Point = getDepths(target);
			errorTip = ToolTipManager.createToolTip(error, coord.x + target.width + 17, coord.y + 25) as ToolTip;
			
			// Apply the errorTip class selector.
			errorTip.setStyle("styleName", "errorTip");
		}
		
		private static function getDepths(target:DisplayObject):Point
		{
			var depth:Point = new Point(target.x, target.y);
			
			if (target.parent)
			{
				var parentDepth:Point = getDepths(target.parent);
				depth.x += parentDepth.x;
				depth.y += parentDepth.y;
			}
			
			return depth;
		}
	}
}