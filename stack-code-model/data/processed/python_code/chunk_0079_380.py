package widgets.HuanBaoJu.skins
{
	import mx.core.ClassFactory;
	
	import spark.components.DataGroup;
	
	[Event(name="itemClick", type="flash.events.Event")]
	
	public class PollutionTypeDataGroup extends DataGroup
	{
		public function PollutionTypeDataGroup()
		{
			super();
			
			this.itemRenderer = new ClassFactory( PollutionTypeDataGroupRenderer );
		}
	}
}