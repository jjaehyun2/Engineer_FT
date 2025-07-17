package widgets.HuanBaoJu
{
	import flash.events.EventDispatcher;
	import flash.events.IEventDispatcher;
	
	public class BlockCount extends EventDispatcher
	{
		[Bindable] public var blockName:String;
		[Bindable] public var count:Number;
		
		public function BlockCount(target:IEventDispatcher=null)
		{
			super(target);
		}
	}
}