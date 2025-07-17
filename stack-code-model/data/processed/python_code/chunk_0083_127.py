package org.pong.mvcs.controller.commands 
{
	import org.pong.mvcs.model.BallModel;
	import org.pong.mvcs.vo.BallVO;
	
	/**
	 * 
	 * Command that calls new direction calculation when <code>BallView</code> hits the borders of stage.
	 * 
	 * @author mc
	 */
	
	public class BallHitWallCommand 
	{
		[Inject]
		public var ballModel:BallModel;
		
		public function execute(vo:BallVO):void
		{
			trace(this + ", execute()");
			
			ballModel.ballHitWall(vo);
		}
	}
}