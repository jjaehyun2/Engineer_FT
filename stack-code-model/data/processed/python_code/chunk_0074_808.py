package modules.srddzGame.srddzInerGame.view.calculate.item
{
	import laya.display.Sprite;
	import laya.ui.Image;
	
	import manager.TextManager;
	
	import modules.srddzGame.SrddzGameModule;
	import modules.srddzGame.srddzInerGame.model.SrddzModel;
	
	import ui.srddzGame.calculate.item.CalculatePerItemUI;
	
	public class CalculatePerItem
	{
		protected var _skin:CalculatePerItemUI;
		protected var headImg:Image;
		private var headw:Number=0,headh:Number=0;
		
		public function CalculatePerItem(skin:CalculatePerItemUI)
		{
			_skin = skin;
			init();
		}
		protected function init():void
		{
			headImg = _skin.headImg;
			headw = headImg.width;
			headh = headImg.height;
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
				
				if(player.Icon != "")
				{
					var photo:Sprite=new Sprite();
					photo.loadImage(player.Icon,0,0,headw,headh);//AppConfig.httpPhotoUrl+obj.uid
					//photo.mouseEnabled=true;
					headImg.addChild(photo);
				}
			}
			
			
			
			if(pos == model.dizhuPos)
			{
				_skin.dizhuImg.visible = true;
				if(data)
				{
					_skin.directImg.visible = model.isSeleStrictWin;
				}
				else
				{
					_skin.directImg.visible = false;
				}
				
			}
			else
			{
				_skin.dizhuImg.visible = false;
				_skin.directImg.visible = false;
			}
			
			if(isLiu)
			{
				_skin.difenTf.text =   ""+0 ;
				_skin.beishuTf.text =  ""+0 ;
				_skin.zongfenTf.font = TextManager.NumberYellowFont;
				_skin.zongfenTf.text = ""+0 ;
				_skin.directImg.visible = false;
				//				_skin.chunImg.visible = false;
				//				_skin.fanchunImg.visible = false;
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
				
				
				
				
				//				_skin.chunImg.visible = data.Chun;
				//				_skin.fanchunImg.visible = data.Fanchun;
			}
			
			
			
			
			
		}
		
		public function reset():void
		{
			
		}
		
		
		protected function get model():SrddzModel
		{
			return SrddzGameModule.instance.gameContext.model;
		}
	}
}