package bt
{
	import flash.display.DisplayObject;
	
	import org.hammerc.archer.bt.BehaviorStatus;
	import org.hammerc.archer.bt.actions.Action;
	import org.hammerc.archer.bt.base.BehaviorNode;
	
	public class MoveRightAction extends Action
	{
		private static const SPEED:Number = 100;
		private static const MAX_TIME:Number = 1.5;
		
		private var _time:Number;
		
		public function MoveRightAction(id:String = null)
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
				DisplayObject(tree.data).x = 400;
				return BehaviorStatus.SUCCESS;
			}
			
			_time += time;
			
			DisplayObject(tree.data).x -= SPEED * time;
			
			return BehaviorStatus.RUNNING;
		}
		
		override public function clone():BehaviorNode
		{
			return new MoveRightAction(_id);
		}
	}
}