package vo
{
	import mx.collections.ArrayCollection;
	import mx.core.FlexGlobals;

	[Bindable]
	[RemoteClass(alias="cn.dlut.entity.Vnet_request")]
	public class Vnet_request
	{
		public var request_id:int;
		public var request_name:String;
		public var request_type:String;
		public var vnet_id:String;
		public var content_id:String;
		public var request_status:String;
		public var request_group:String;
		public var request_timestamp:String;
		
		public function Vnet_request(name:String,type:String,vnet_id:String,content_id:String,request_group:String) {
			this.request_name = name;
			this.request_type = type;
			this.vnet_id = vnet_id;
			this.content_id = content_id;
			this.request_group = request_group;
			var tmplist:Array = request_group.split("~");
			this.request_timestamp = tmplist[1];
			this.request_status = "wait";
		}
	}
}