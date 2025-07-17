package hall.view.replay.item
{
	import manager.TextManager;
	
	import ui.hall.replay.PlayerRecordItemUI;

	public class PlayerRecordItem
	{
		protected var skin:PlayerRecordItemUI;
		
		public function PlayerRecordItem(s:PlayerRecordItemUI)
		{
			skin = s;	
		}
		
		public function show():void
		{
			skin.visible = true;
		}
		
		public function hide():void	
		{
			skin.visible = false;
		}
		
		/**刷新*/
		public function update(dat:Object,idx:int):void
		{
			
//			string userId = 1;//用户ID
//			string nickName = 2;//用户昵称
//			string icon = 3;//用户头像
//			int32 score = 4;//玩家分数
			skin.headImg.skin = dat.icon==""?"common/morentouxiang.png":dat.icon;
			skin.nameTf.text = dat.nickName;
			
			skin.scoreTf.font=dat.score>0?TextManager.NumberRedFont:TextManager.NumberLvFont;
			
			if(dat.score>0)
			{
				skin.scoreTf.text = "+" + dat.score;
			}
			else
			{
				skin.scoreTf.text = "" + dat.score;
			}
		}
	}
}