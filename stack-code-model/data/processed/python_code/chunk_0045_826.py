package Components
{
	[Bindable]
	[RemoteClass(alias="cn.dlut.entity.Rule")]
	public class Rule
	{
		public var ruleid:int;
		public var nw_proto:String="";
		public var src_ip:String ="";
		public var dst_ip:String ="";
		public var tp_dst:int;
		public var action:String ="";
		public var priority:int;
		public var dl_type:String ="";
		
	}
}