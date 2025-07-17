package vo
{
	[Bindable]
	[RemoteClass(alias="cn.dlut.entity.Vnet_userip")]
	public class Vnet_userip
	{
		public var userip_id:String;
		public var userip_addr:String;
		public var userip_mask:String;
		public var host_id:String;
		public var osport_id:String;
		
		public function Vnet_userip(_id:String, _addr:String, _mask:String, host_id:String):void{
			this.userip_id = _id;
			this.userip_addr = _addr;
			this.userip_mask = _mask;
			this.host_id = host_id;
		}
	}
}