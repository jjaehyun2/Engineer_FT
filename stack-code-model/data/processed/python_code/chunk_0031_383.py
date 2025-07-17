/**
 * Created by newkrok on 24/01/16.
 */
package src.menu.module.task
{
	import net.fpp.common.achievement.AchievementVO;
	import net.fpp.common.starling.module.AModel;

	public class TaskModel extends AModel
	{
		private var _worldID:uint;
		private var _tasks:Vector.<AchievementVO>;
		private var _completedTasksCount:uint;
		private var _rewardCarGraphicId:uint;

		public function setWorldID( value:uint ):void
		{
			this._worldID = value;
		}

		public function getWorldID():uint
		{
			return this._worldID;
		}

		public function setTasks( value:Vector.<AchievementVO> ):void
		{
			this._tasks = value;
		}

		public function getTasks():Vector.<AchievementVO>
		{
			return this._tasks;
		}

		public function setCompletedTasksCount( value:uint ):void
		{
			this._completedTasksCount = value;
		}

		public function getCompletedTasksCount():uint
		{
			return this._completedTasksCount;
		}

		public function setRewardCarGraphicId( value:uint ):void
		{
			this._rewardCarGraphicId = value;
		}

		public function getRewardCarGraphicId():uint
		{
			return this._rewardCarGraphicId;
		}
	}
}