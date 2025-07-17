package bt
{
	import flash.display.DisplayObject;
	
	import org.hammerc.archer.bt.BehaviorStatus;
	import org.hammerc.archer.bt.actions.Action;
	import org.hammerc.archer.bt.base.BehaviorNode;
	
	public class RotateAction extends Action
	{
		private static const SPEED:Number = 360;
		private static const MAX_TIME:Number = 1;
		
		private var _time:Number;
		
		public function RotateAction(id:String = null)
		{
			super(id);
		}
		
		override protected function enter():void
		{
			_time = 0;
		}
		
		override protected function execute(time:Number):int
		{
			if(_time >= MAX_TIME)
			{
				DisplayObject(tree.data).rotation = 0;
				return BehaviorStatus.SUCCESS;
			}
			
			_time += time;
			
			DisplayObject(tree.data).rotation += SPEED * time;
			
			return BehaviorStatus.RUNNING;
		}
		
		override public function clone():BehaviorNode
		{
			return new RotateAction(_id);
		}
	}
}