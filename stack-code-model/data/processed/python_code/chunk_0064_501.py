package vo
{
	[Bindable]
	public class Flow
	{
		public function Flow()
		{
			public var id:int;
			public var switch_id:int;
			public var table_id:int;
			public var byte_count:int;
			public var packet_count:int;
			public var idle_timeout:int;
			public var hard_timeout:int;
			public var duration_sec:int;
			public var duration_nsec:int;
			public var priority:int;
			public var cookie:String;
			public var dl_type:String;
			public var dl_src:String;
			public var dl_dst:String;
			public var dl_vlan:int;
			public var nw_proto:int;
			public var nw_tos:int;
			public var nw_src:String;
			public var nw_dst:String;
			public var nw_src_masklen:int;
			public var nw_dst_masklen:int;
			public var tp_src:int;
			public var tp_dst:int;
			public var in_port:int;
			public var action:String;
			public var ctime:Date;
		}
	}
}