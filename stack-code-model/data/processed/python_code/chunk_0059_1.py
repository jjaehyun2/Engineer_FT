package services.vo.reports
{
	[RemoteClass(alias="MapHouseKeepSearch")]
	public class HousekeepingReportVO
	{
		public var iId:int = 0;
		/**
	   * Array room types
	   * @var Array
	   */
		public var aRoomType:Array = new Array(); 
		public var aRoomStatus:Array = new Array();  
  		public var aHouseKeepingStatus:Array = new Array();  
/* 
		public var iStage:int;  */ 
		public var iFromRoom:int = 0;
  		public var iToRoom:int = 0;
  		
  		public var bShowName:Boolean;// Show or not show Guest name
  		public var iSortOrder:int;

	}
}


/* class MapHouseKeepSearch
{
  public $iId = 0;

  public $aRoomType;
  public $aRoomStatus;  
  public $aHouseKeepingStatus;  
  public $iFromRoom;
  public $iToRoom;
  public $bShowName; // Show or not show Guest name
  public $iSortOrder;
} */