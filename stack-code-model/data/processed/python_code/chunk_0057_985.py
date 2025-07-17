package modules.sddzGame.sddzInerGame.view.playerInfoPart
{
	import common.tools.SoundPlay;
	
	import laya.ani.swf.MovieClip;
	import laya.events.Event;
	import laya.utils.Dictionary;
	import laya.utils.Handler;
	import laya.utils.Tween;
	
	import manager.UIManager;
	
	import modules.sddzGame.sddzInerGame.view.pockerPart.card.BasePocker;

	public class GiftEff
	{
		private var expressUrl:String = "res/swfs/";
		
		private static var _instance:GiftEff;
		
		public static function get instance():GiftEff
		{
			if(_instance == null)
			{
				_instance = new GiftEff(new SingleForcer());
			}
			return _instance;
		}
		
		public function GiftEff(forcer:SingleForcer)
		{
			
		}
		
		public var loadedArr:Array = [];
		
		
		public function showGiftEff(fromDir:int,toDir:int,id:int):void
		{
			var mc:MovieClip = new MovieClip();
			mc.load(expressUrl+AppConfig.giftConfig[id-1].name + ".swf",true);
			
			var sound:String = AppConfig.giftConfig[id-1].sound;
			var sounddelay:int =  parseInt(AppConfig.giftConfig[id-1].sounddelay);
			
			if(loadedArr.indexOf(mc.basePath) != -1)
			{
				onLoaded(mc,fromDir,toDir,sound,sounddelay);
			}
			else
			{
				mc.on(Event.LOADED,this,onLoaded,[mc,fromDir,toDir,sound,sounddelay]);
			}
			//
		}
		
		protected var _mcMap:Dictionary = new Dictionary();
		
		public function showPockTypeEff(type:int,attach:Boolean=false):void
		{
			var mcPath:String = "";
			var soundPath:String = "";
			switch(type)
			{
				case BasePocker.PAIXING_SHUNZI:
					mcPath =  "res/swfs/pokerType/shunzi.swf";
					playAni(mcPath,-650);
					break;
				case BasePocker.PAIXING_FEIJI:
					mcPath = "";
					if(attach)
					{
						mcPath = "res/swfs/pokerType/feijichibang.swf";
						soundPath = "pockerType/type_feijichibang";
					}
					else
					{
						mcPath = "res/swfs/pokerType/feiji.swf";;
						soundPath = "pockerType/type_feiji";
					}
					playAni(mcPath,-260,0,soundPath);
					break;
				case BasePocker.PAIXING_ZHADAN:
					mcPath =  "res/swfs/pokerType/zhadan.swf";
					playAni(mcPath,-260,0,"pockerType/type_zhadan");
					break;
				case BasePocker.PAIXING_DUIWANG:
					mcPath =  "res/swfs/pokerType/huojian.swf";
					playAni(mcPath,-260,0,"pockerType/type_huojian");
					break;
				
				default :break;
			}
			
		}
		
		private function playAni(url:String, offsetX:Number = 0, offsetY:Number = 0,sound:String=""):void
		{
			var mc:MovieClip = new MovieClip();
			mc.load(url,true);
			
//			var sound:String = AppConfig.giftConfig[id-1].sound;
//			var sounddelay:int =  parseInt(AppConfig.giftConfig[id-1].sounddelay);
			
			if(loadedArr.indexOf(mc.basePath) != -1)
			{
				onLoadedPockTypeMc(mc,"",0,offsetX,offsetY);
			}
			else
			{
				mc.on(Event.LOADED,this,onLoadedPockTypeMc,[mc,sound,0,offsetX,offsetY]);
			}
		}
		
		protected function onLoaded(mc:MovieClip,fromDir:int,toDir:int,sound:String,sounddelay:int):void
		{
			if(loadedArr.indexOf(mc.basePath) == -1)
			{
				loadedArr.push(mc.basePath);
			}
			
			mc.stop();
			UIManager.instance.popLayer.addChild(mc);
			switch(fromDir)
			{
				case 0:
					mc.x = -32;
					mc.y = 858;
					break;
				case 1:
					mc.x = 468;
					mc.y = 166;
					break;
				case 2:
					mc.x = -32;
					mc.y = 166;
					break;
				case 3:
					mc.x = -50;
					mc.y = 90;
					break;
				default :
//					mc.x = 488;
//					mc.y = -50;
					break;
			}
			
			var tX:int,tY:int;
			
			switch(toDir)
			{
				case 0:
					tX = -32;
					tY = 858;
					break;
				case 1:
					tX = 468;
					tY = 166;
					break;
				case 2:
					tX = -32;
					tY = 166;
					break;
				case 3:
					tX = -50;
					tY = 90;
					break;
				default :
					tX = 188;
					tY = -50;
					break;
			}
			Tween.to(mc,{x:tX,y:tY},400,null,new Handler(this,onCompeteTween,[mc,sound,sounddelay]));
		}
		
		protected function onLoadedPockTypeMc(mc:MovieClip,sound:String,sounddelay:int,offsetX:Number = 0, offsetY:Number = 0):void
		{
			if(loadedArr.indexOf(mc.basePath) == -1)
			{
				loadedArr.push(mc.basePath);
			}
			
			mc.stop();
			UIManager.instance.popLayer.addChild(mc);
			mc.x = offsetX;
			mc.y = 200 +  offsetY;
			
			mc.playTo(0,mc.count-2,Handler.create(this,playEnd,[mc]));
			Laya.timer.once(3000,this,playEnd,[mc]);
		
			if(sounddelay == 0)
			{
				SoundPlay.playEffect(sound);
			}
			else
			{
				Laya.timer.once(sounddelay,this,playSound,[sound],false);
			}
		}
		
		private function onCompeteTween(mc:MovieClip,sound:String,sounddelay:int):void
		{
			mc.playTo(0,mc.count-2,Handler.create(this,playEnd,[mc]));
			Laya.timer.once(3000,this,playEnd,[mc]);
			if(sounddelay == 0)
			{
				SoundPlay.playEffect(sound);
			}
			else
			{
				Laya.timer.once(sounddelay,this,playSound,[sound],false);
			}
			
			
			
		}
		
		protected function playSound(sound:String):void
		{
			SoundPlay.playEffect(sound);
		}
		
		protected function playEnd(mc:MovieClip):void
		{
			mc && mc.removeSelf();
		}
		
		
	}
}

class SingleForcer{}