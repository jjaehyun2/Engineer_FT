package widgets.HuanBaoJu.skins
{
	import mx.core.ClassFactory;
	
	import spark.components.DataGroup;
	
	[Event(name="itemClick", type="flash.events.Event")]
	
	public class BlockCountDataGroup extends DataGroup
	{
		public function BlockCountDataGroup()
		{
			super();
			
			this.itemRenderer = new ClassFactory( BlockCountDataGroupRenderer );
		}
	}
}