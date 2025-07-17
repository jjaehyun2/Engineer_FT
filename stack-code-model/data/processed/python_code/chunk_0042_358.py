package widgets.HuanBaoJu.skins
{
	import mx.core.ClassFactory;
	
	import spark.components.DataGroup;
	
	[Event(name="itemClick", type="flash.events.Event")]
	
	public class DistrictCountDataGroup extends DataGroup
	{
		public function DistrictCountDataGroup()
		{
			super();
			
			this.itemRenderer = new ClassFactory( DistrictCountDataGroupRenderer );
		}
	}
}