package framework.module
{
	import mx.collections.ArrayCollection;
	
	[Bindable]
	public class CheckInModule
	{
		public var currPage:int = 0;
		public var pageNames:Array = ["Check In"];
		
		public var currentProfileId:int = 0;
		public var currentProfileRoomId:int = 0;
		public var currentCheckInProfileId:int = 0;
		
		public var counter:int = 0;
		
		public var floorsData:ArrayCollection = new ArrayCollection();
		public var checkInData:ArrayCollection = new ArrayCollection();
		public var roomSettings:ArrayCollection = new ArrayCollection( [{label:"Smoker", slug:"smoker"}, 
																		{label:"Non-Smoker", slug:"nonSmoker"},
																		{label:"Disabled", slug:"disabled"}, 
																		{label:"Elevator", slug:"elevator"}] );
		
	}
}