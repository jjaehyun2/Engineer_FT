package org.pong.mvcs.controller.commands 
{
	import org.pong.mvcs.model.BallModel;
	import org.pong.mvcs.vo.BallVO;
	/**
	 * 
	 * Command that calls new direction calculations when <code>BallView</code> hits the paddle.
	 * 
	 * @author mc
	 */
	
	public class BallHitPaddleCommand 
	{
		[Inject]
		public var ballModel:BallModel;
		
		public function execute(vo:BallVO):void
		{
			trace(this + ", execute()");
			
			ballModel.ballHitPaddle(vo);
		}
	}

}