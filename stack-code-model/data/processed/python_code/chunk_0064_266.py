package modules.nnGame.inerGame.view.pockerPart.card
{
	import modules.nnGame.NnGameModule;
	import modules.nnGame.inerGame.model.NnModel;
	import modules.nnGame.inerGame.view.NnView;
	
	import ui.niuniuGame.niuniuPart.item.PockerItemUI;
	
	
	

	/**扑克牌基类*/
	public class BasePocker
	{
		/**没牛*/
		public static const PAIXING_MEINIU:int = 0;
		/**牛1*/
		public static const PAIXING_NIUYI:int = 1;
		/**牛2*/
		public static const PAIXING_NIUER:int = 2;
		/**牛3*/
		public static const PAIXING_NIUSAN:int = 3;
		/**牛4*/
		public static const PAIXING_NIUSI:int = 4;
		/**牛5*/
		public static const PAIXING_NIUWU:int = 5;
		/**牛6*/
		public static const PAIXING_NIULIU:int = 6;
		/**牛7*/
		public static const PAIXING_NIUQI:int = 7;
		/**牛8*/
		public static const PAIXING_NIUBA:int = 8;
		/**牛9*/
		public static const PAIXING_NIUJIU:int = 9;
		/**牛牛*/
		public static const PAIXING_NIUNIU:int = 10;
		/**同花*/
		public static const PAIXING_TONGHUA:int = 11;
		/**顺子*/
		public static const PAIXING_SHUNZI:int = 12; 
		/**葫芦*/
		public static const PAIXING_HULU:int = 13;
		/**五花牛*/
		public static const PAIXING_WUHUA:int = 14;
		/**五小牛*/
		public static const PAIXING_WUXIAO:int = 15;
		/**炸弹*/
		public static const PAIXING_ZHADAN:int = 16;
		/**同花顺*/
		public static const PAIXING_TONGSHUN:int = 17;
		
		
		
		
		
		/**王*/
		public static const TYPE_WANG:int = 5;
		
		
		public static const PREPATH:String = "poker/";
		
		public static const CARD_REFERENCE:Object = {
			551:"xiao_w.png",552:"da_w.png",
			
			414:"hong_1.png",416:"hong_2.png",403:"hong_3.png",404:"hong_4.png",405:"hong_5.png",406:"hong_6.png",407:"hong_7.png",408:"hong_8.png",409:"hong_9.png",
			410:"hong_10.png",411:"hong_j.png",412:"hong_q.png",413:"hong_k.png",
			
			314:"fang_1.png",316:"fang_2.png",303:"fang_3.png",304:"fang_4.png",305:"fang_5.png",306:"fang_6.png",307:"fang_7.png",308:"fang_8.png",309:"fang_9.png",
			310:"fang_10.png",311:"fang_j.png",312:"fang_q.png",313:"fang_k.png",
			
			214:"hei_1.png",216:"hei_2.png",203:"hei_3.png",204:"hei_4.png",205:"hei_5.png",206:"hei_6.png",207:"hei_7.png",208:"hei_8.png",209:"hei_9.png",
			210:"hei_10.png",211:"hei_j.png",212:"hei_q.png",213:"hei_k.png",
			
			114:"mei_1.png",116:"mei_2.png",103:"mei_3.png",104:"mei_4.png",105:"mei_5.png",106:"mei_6.png",107:"mei_7.png",108:"mei_8.png",109:"mei_9.png",
			110:"mei_10.png",111:"mei_j.png",112:"mei_q.png",113:"mei_k.png"
			
			//113,213,313,413,105,205,305,103,203,106,306,109,409,110,210,311,312   四带二测试大
			
			//103,203,303,403,105,205,305,104,204,106,306,109,409,110,210,311,312  四带二测试小
			
			//113,213,313,114,214,314,305,103,203,106,306,109,409,412,112,212,312    飞机测试大
			
			//103,203,303,104,204,304,105,205,305,106,306,109,409,110,210,311,312  飞机测试小
		};
		
		/**5王牌 4红桃 3方块 2黑桃 1梅花*/
		public static function getT(card:int):int
		{
			return Math.floor(card/100);
		}
		
		/**牌值取A为14  取2为16*/
		public static function getV(card:int):int
		{
			return card%100;
		}
		
		/**取A为1 取2为2*/
		public static function getVShang(card:int):int
		{
			var value:int = card%100;
			if(value == 14)
			{
				value = 1;
			}
			else if(value == 16)
			{
				value = 2;
			}
			
			return value;
		}
		
		/**牛牛值*/
		public static function getVNn(card:int):int
		{
			var value:int = card%100;	
			if(value == 14)
			{
				value = 1;
			}
			else if(value == 16)
			{
				value = 2;
			}
			
			if(value >= 10)
			{
				value = 10;
			}
			return value;
		}
		
		/**牛牛是否花色*/
		public static function checkIsHua(card:int):Boolean
		{
			var value:int = card%100;	
			if(value == 11 || value == 12 || value == 13)
			{
				return true;
			}
			return false;
		}
		
		
		public static const STATE_UP:int = 0;
		public static const STATE_BACK:int = 1;
		public static const STATE_DOWN:int=2;
		
		public var skin:PockerItemUI;
		/**-1表示没有状态*/
		public var state:int = -1;
		public var cardIdx:int = 0;
		
		
		public function BasePocker(skin:PockerItemUI)
		{
			this.skin = skin;
			init();
		}
		
		protected function init():void
		{
			//reset();
		}
		
		public function up():void
		{
			if(state == STATE_UP)
			{
				return;
			}
			
			skin.valueImg.visible = true;
			skin.backImg.visible  = false;
			
			state = STATE_UP;
		}
		
		public function back():void
		{
			if(state == STATE_BACK)
			{
				return;
			}
			skin.backImg.visible  = true;
			skin.valueImg.visible = false;
			
			state = STATE_BACK;
		}
		
		public function down():void
		{
			if(state == STATE_DOWN)
			{
				return;
			}
			skin.backImg.visible  = false;
			skin.valueImg.visible = true;
			
			state = STATE_DOWN;
		}
		
		public function get visible():Boolean
		{
			return skin.visible;
		}
		
		public function show():void
		{
			skin.visible = true;
		}
		
		public function hide():void
		{
			skin.visible = false;
		}
		public function setCardImg(cardIdx:int):void
		{
			if(this.cardIdx == cardIdx)
			{
				return;
			}
			
			if(CARD_REFERENCE.hasOwnProperty(cardIdx.toString()))
			{
				skin.valueImg.skin = PREPATH + CARD_REFERENCE[cardIdx.toString()];
			}
			
			this.cardIdx = cardIdx;
		}
		
		
		
		public function set canControl(bool:Boolean):void
		{
			
		}
		
		public function set select(bool:Boolean):void
		{
			
		}
		
		public function get select():Boolean
		{
			return false;
		}
		
		protected function get view():NnView
		{
			return NnGameModule.instance.gameContext.view;
		}
		
		protected function get model():NnModel
		{
			return NnGameModule.instance.gameContext.model;
		}
		
		/**重置*/
		public function reset():void
		{
			hide();
			skin.backImg.visible = false;
			skin.valueImg.visible = false;
			skin.shadowImg.visible = false;
			state = -1;
			select = false;
		}
	}
}