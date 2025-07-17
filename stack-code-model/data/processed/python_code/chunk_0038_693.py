package services.vo.common
{
	[RemoteClass(alias="MapSourceCodeGroup")]
	public class SourceCodesGroupVO
	{
		public var lGroupId:Number;
		public var sGroupName:String;
		
		public var aCodes:Array = [];
		
		[Transient] //for interface
		public var bIsSelected:Boolean = false;
	}
}