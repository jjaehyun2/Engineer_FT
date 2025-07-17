package widgets.HuanBaoJu
{
	import flash.events.EventDispatcher;
	import flash.events.IEventDispatcher;
	
	public class DistrictCount extends EventDispatcher
	{
		[Bindable] public var districtName:String;
		[Bindable] public var count:Number;
		
		public function DistrictCount(target:IEventDispatcher=null)
		{
			super(target);
		}
	}
}