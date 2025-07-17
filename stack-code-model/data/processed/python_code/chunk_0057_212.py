package services.vo.items
{
	import services.vo.MapValueObject;
	
	[Bindable]
	[RemoteClass(alias="MapVatPeriod")]
	public class VatPeriodVO extends MapValueObject
	{
		// active data:
		public var bBasicList:Boolean;
		public var iItemId:Number;
		public var iVatId:Number;
		public var sStart:String;
		public var sEnd:String;
		
		// for display only:
		public var sVatName:String;
	}
}