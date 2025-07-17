package modules.nnGame.inerGame.view.pockerPart.singlePart.handlePart
{
	
	import modules.nnGame.inerGame.view.pockerPart.card.OtherHandlePocker;
	
	import ui.niuniuGame.niuniuPart.handlePart.OtherHandlePartUI;
	
	public class OtherSingleHandlePart extends BaseSingleHandlePart
	{
		
		
		protected var _skin:OtherHandlePartUI
		
		public function OtherSingleHandlePart(skin:OtherHandlePartUI,dir:int)
		{
			_skin = skin;
			
			
			super(skin);
			fromPos = [{x:495-skin.x,y:328-_skin.y},{x:495-skin.x,y:328-_skin.y},{x:495-skin.x,y:328-_skin.y},{x:495-skin.x,y:328-_skin.y},{x:495-skin.x,y:328-_skin.y}];
			toPos = [{x:0,y:0},{x:21,y:0},{x:42,y:0},{x:63,y:0},{x:84,y:0}];
		}
		
		override protected function init():void
		{
			
		
			
			var i:int,len:int=_pockers.length;
			
			for(i=0;i<len;i++)
			{
				_pockers[i] = new OtherHandlePocker(_skin["card"+i]);
			}
			
		
		}
		
		override public function showCards(cards:Array,dir:int):void
		{
			cards = cards.concat();
			
			var pos:int = model.getChairPosByDir(dir);
			
			hideAll();
			
			var i:int;
			
			for(i=0;i<cards.length;i++)
			{
				_pockers[i].setCardImg(cards[i]);
				_pockers[i].show();
				if(model.isEnd)
				{
					_pockers[i].down();
				}
				else
				{
					_pockers[i].up();
				}
			
				_pockers[i].select = false;
			}
			
		}
		
		override public function playQipaiEff(isLast:Boolean):void{
			//别人的暂时不做处理
			super.playQipaiEff(isLast);
		}
		
		/**显示玩家已完成*/
		override public function showComp(pos:int):void
		{
			_skin.comBox.visible = true;
			_skin.typeImg.skin = "niuniuGame/niuType/ready.png";
		}
		
		
		
		/**显示牌型*/
		override public function showPaixing(pos:int,paixing:int):void
		{
			_skin.comBox.visible = true;
			_skin.typeImg.skin = "niuniuGame/niuType/niu"+paixing+".png";
		}
		
		override public function reset():void
		{
			super.reset();
			_skin.comBox.visible = false;
		}
		
	}
}