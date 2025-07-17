package widgets.HuanBaoJu
{
	import flash.events.EventDispatcher;
	import flash.events.IEventDispatcher;
	
	public class PollutionType extends EventDispatcher
	{
		[Bindable] public var label:String;
		[Bindable] public var name:String;
		[Bindable] public var selected:Boolean;
		
		public function PollutionType(target:IEventDispatcher=null)
		{
			super(target);
		}
	}
}