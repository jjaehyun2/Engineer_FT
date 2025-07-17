package services.vo.checkOut.itemRouting
{
	import services.vo.MapValueObject;
	
	[RemoteClass(alias="MapPackageItems")]
	public class PackageItemsVO extends MapValueObject
	{
		public var lPaymentId:Number = 0;
		public var lPackageId:Number = 0;
		public var sPackageName:String;
		public var fSum:Number = 0;
		public var lAppliedAccount:Number = 0;
		
		public var aItems:Array = [];
	}
}