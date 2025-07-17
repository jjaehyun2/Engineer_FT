package framework.module
{
	
	/**
	* The HouseKeepingModule class is 
	*
	* @author  Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-07-18 11:52:03 +0300 (Сб, 18 июл 2009) $
	*
	*/
	[Bindable]	
	public class HouseKeepingModule
	{
		public var currPage:int = 0;
		public var pageNames:Array = ["House Keeper"];
		public var roomStatuses:Array; //HotelRoomStatusVO
	}
}