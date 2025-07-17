package org.pong.mvcs.model 
{
	import org.pong.mvcs.model.signals.BallModelUpdatedSignal;
	import org.pong.mvcs.vo.BallVO;
	
	/**
	 * 
	 * The BallModel contains necessary logic to direct movement of the Ball view.
	 * 
	 * @author mc
	 */
	
	public class BallModel 
	{
		/**
		 * Dispatched when model recalculates new ball direction and position.
		 */
		[Inject]
		public var ballModelUpdatedSignal:BallModelUpdatedSignal;
		
		/**
		 * Value object that containes Ball view values (like direction, velocity etc..)
		 */
		private var _vo:BallVO;
		
		/**
		 * 
		 * Calculates initial values once Ball view is added to stage.
		 * 
		 * @event ballModelUpdatedSignal() dispached when called.
		 * 
		 * @param	vo	Initial value object passed from view component.
		 * */
		public function ballAddedToStage(vo:BallVO):void
		{
			trace(this + " ballAddedToStage()");
			trace("x: " + vo.x + " " + "y: " + vo.y);
			
			_vo = createNewVO(vo);
			
			_vo = randomizeDirection(_vo);
			
			ballModelUpdatedSignal.dispatch(_vo);
		}
		
		/**
		 * 
		 * Calculates new direction once Ball view touches stage border.
		 * 
		 * @event ballModelUpdatedSignal dispached when direction recalculated.
		 * 
		 * @param	vo	Value object with the old direction values.
		 */
		public function ballHitWall(vo:BallVO):void
		{				
			_vo = createNewVO(vo);
			
			trace(this + " ballHitWall()");
			trace("old value - x: " + _vo.x + " " + "y: " + _vo.y);
			
			_vo = recalculateBallDirectionAfterWallHit(_vo);
			
			trace("new value - x: " + _vo.x + " " + "y: " + _vo.y);
			
			ballModelUpdatedSignal.dispatch(_vo);
		}
		
		/**
		 * 
		 * Recalculates the ball direction to create bounce effect.
		 * 
		 * @param	vo Value object with the old direction values.
		 * @return	Value object with the new direction values.
		 */
		private function recalculateBallDirectionAfterWallHit(vo:BallVO):BallVO
		{
			// TODO optimaze change direction algoritham
			
			if (vo.x <= 0)
			{
				vo.x = 1;
				vo.directionX *= -1;
			}
			else if (vo.x + vo.width >= vo.stageWidth)
			{
				vo.x = vo.stageWidth - vo.width - 1;
				vo.directionX *= -1;
			}
			
			if (vo.y <= 0)
			{
				vo.y = 1;
				vo.directionY *= -1;
				
			}
			else if (vo.y + vo.height >= vo.stageHeight)
			{
				vo.y = vo.stageHeight - vo.height - 1;
				vo.directionY *= -1;
			}
			
			return vo;
		}
		
		/**
		 * 
		 * Calculates new direction. Called when Ball view collides with Paddle view.
		 * 
		 * @event ballModelUpdatedSignal() dispached new direction calculated.
		 * 
		 * @param	vo Value object with the old direction values.
		 */
		public function ballHitPaddle(vo:BallVO):void
		{
			_vo = createNewVO(vo);
			
			trace(this + " ballHitPaddle()");
			trace("old value - x: " + _vo.x + " " + "y: " + _vo.y);
			
			_vo.directionX *= -1;
			
			trace("new value - x: " + _vo.x + " " + "y: " + _vo.y);
			
			ballModelUpdatedSignal.dispatch(_vo);
		}
		
		/**
		 * 
		 * Randomizes ball direction once the match has been won.
		 * 
		 * @event ballModelUpdatedSignal() dispached when new direction reacquired
		 * 
		 * @param	vo Value object with the old values.
		 */
		public function playerWon(vo:BallVO):void
		{		
			_vo = createNewVO(vo);
			
			_vo = randomizeDirection(_vo);
			
			ballModelUpdatedSignal.dispatch(_vo);
		}
		
		/**
		 * 
		 * Creates random directions that Ball view should movie next. 
		 * 
		 * @param	vo Value object with the old direction values.
		 * @return	vo Value object with the new randomized direction values.
		 */
		private function randomizeDirection(vo:BallVO):BallVO
		{
			trace(this + " randomizeDirection()");
			
			vo.directionX = Math.random() > 0.5 ? -1 : 1;
			vo.directionY = Math.random() > 0.5 ? -1 : 1;
			
			return vo;
		}
		
		/**
		 * 
		 * Takes an old value object and creates the new instance of the same type and with same values.
		 * That way objects stay immutable.
		 * 
		 * @param	oldVO Old value object.
		 * @return	New BallVO instance.
		 */
		private function createNewVO(oldVO:BallVO):BallVO
		{
			//TODO - this should be dynamic 
			
			var newVO:BallVO = new BallVO;
			
			newVO.velocity = oldVO.velocity;
			
			newVO.x = oldVO.x;
			newVO.y = oldVO.y;
			
			newVO.stageHeight = oldVO.stageHeight;
			newVO.stageWidth = oldVO.stageWidth;
			
			newVO.width = oldVO.width;
			newVO.height = oldVO.height;
			
			newVO.directionX = oldVO.directionX;
			newVO.directionY = oldVO.directionY;
			
			return newVO;
		}
	}

}