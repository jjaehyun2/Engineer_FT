package org.pong.mvcs.controller.commands 
{
	import org.pong.mvcs.model.BallModel;
	import org.pong.mvcs.vo.BallVO;
	
	/**
	 * 
	 * Command that calls calculation of initial values when <code>BallView</code> is added to stage. 
	 * 
	 * @author mc
	 */
	
	public class BallAdedToStageCommand 
	{		
		[Inject]
		public var ballModel:BallModel;
		
		public function execute(vo:BallVO):void
		{		
			ballModel.ballAddedToStage(vo);
		}
	}

}