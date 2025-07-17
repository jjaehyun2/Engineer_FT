package vo
{
	import mx.core.FlexGlobals;
	
	[Bindable]
	[RemoteClass(alias="cn.dlut.entity.Vnet_imgae")]
	public class Vnet_image
	{
		public var image_id:int;
		public var image_osid:String;
		public var image_name:String;
		public var image_format:String;
		public var image_size:String;
	}
}