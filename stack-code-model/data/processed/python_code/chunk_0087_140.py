package modules.sddzGame.sddzInerGame.view.calculate.item
{
	
	import manager.TextManager;
	
	import modules.sddzGame.SDdzGameModule;
	import modules.sddzGame.sddzInerGame.model.SddzModel;
	import modules.sddzGame.sddzInerGame.view.SddzGameView;
	
	import ui.sddzGame.calculate.item.CalculatePerItemUI;

	public class CalculatePerItem
	{
		protected var _skin:CalculatePerItemUI;
		
		public function CalculatePerItem(skin:CalculatePerItemUI)
		{
			_skin = skin;
			init();
		}
		
		protected function init():void{
			
		}
		
		/**展示这一条数据*/
		public function update(pos:int,data:Object = null,isLiu:Boolean=false):void
		{
			var player:Object = model.playerByPos(pos);
			if(player == null)
			{
				player = model.playerByUid(model.beKickedPlayer[pos]);
			}
			
			if(player == null)
			{
				_skin.visible = false;
			}
			else
			{
				_skin.visible = true;
				_skin.nameTf.text = player.nickname;
			}
			
			if(pos == model.dizhuPos)
			{
				_skin.dizhuImg.visible = true;
			}
			else
			{
				_skin.dizhuImg.visible = false;
			}
			
			if(isLiu)
			{
				_skin.difenTf.text =   ""+0 ;
				_skin.beishuTf.text =  ""+0 ;
				_skin.zongfenTf.font = TextManager.NumberYellowFont;
				_skin.zongfenTf.text = ""+0 ;
				_skin.chunImg.visible = false;
				_skin.fanchunImg.visible = false;
				return;
			}
			
//			int32 Seat = 1; //椅子号
//			int32 Difen = 2; //底分
//			int32 Beishu = 3; //倍数
//			int32 Score = 4; //当前奖励分数
//			int32 Total_score = 5; //当前总分数
//			bool Chun = 6;//春天 非地主
//			bool Fanchun = 7;//反春 地主
			
			if(data)
			{
				_skin.difenTf.text =  data.Difen != undefined ?""+ data.Difen : ""+0 ;
				_skin.beishuTf.text =  data.Beishu != undefined ?""+ data.Beishu : ""+0 ;
				
				if(data.Score == undefined)
				{
					data.Score  = 0;
				}
				if(data.Score  > 0)
				{
					_skin.zongfenTf.font = TextManager.NumberYellowFont;
					_skin.zongfenTf.text = "+" + player.zongchengji;
					
					_skin.zongfenTf.text = "+" + data.Score ;
				}
				else
				{
					_skin.zongfenTf.font = TextManager.NumberBlueFont;
					_skin.zongfenTf.text = data.Score ;
				}
				
			
				
				_skin.chunImg.visible = data.Chun;
				_skin.fanchunImg.visible = data.Fanchun;
			}
		
			
			
			

		}
		
		public function reset():void
		{
			
		}
		
		protected function get model():SddzModel
		{
			return SDdzGameModule.instance.gameContext.model;
		}
		
		protected function get view():SddzGameView
		{
			return SDdzGameModule.instance.gameContext.view;
		}
	}
}