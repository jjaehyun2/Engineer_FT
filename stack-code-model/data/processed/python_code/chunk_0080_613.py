package com.scene
{
	import com.component.gt.TextGame;
	
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;

	public class ResearchScene extends Scene
	{
		private var strArray:Vector.<String>;
		private var stars:Vector.<TextGame>;

		private var current:TextGame;
		
		public function ResearchScene()
		{
			super();
			
			strArray = new Vector.<String>;
			strArray.push("机体：解锁更多可用战机");
			strArray.push("火炮：提升战机攻击力");
			strArray.push("护盾：提升战机HP");
			strArray.push("量产：提升战机生产的速度");
			strArray.push("能耗：减少建造消耗的金钱");
			
			stars = new Vector.<TextGame>;
			
			current = new TextGame("");
			current.width = 150;
			current.x = Game.STAGE_WIDTH>>1;
			current.y = 100;
			addChild(current);
			
			for(var i:int=0;i<5;i++){
				var str:String = strArray[i];
				var text:TextGame = new TextGame(str);
				text.width = 150;
				text.x = Game.STAGE_WIDTH/4;
				text.y = Game.STAGE_HEIGHT/4 + 50 * i;
				addChild(text);
				
				var star:TextGame = new TextGame();
				star.width = 200;
				star.x = Game.STAGE_WIDTH/2;
				star.y = text.y;
				addChild(star);
				stars.push(star);
				
				var upgrade:TextGame = new TextGame("升级");
				upgrade.x = Game.STAGE_WIDTH*3/4;
				upgrade.y = text.y;
				upgrade.name = "upgrade"+i;
				upgrade.index = i;
				addChild(upgrade);
			}
			update();
			
			var back:TextGame = new TextGame("返回");
			back.x = Game.STAGE_WIDTH >> 1;
			back.y = 550;
			addChild(back);
			back.name = "back";
			
			addEventListener(TouchEvent.TOUCH,onTouch);
		}
		
		private function onTouch(e:TouchEvent):void
		{
			var touch:Touch = e.getTouch(this,TouchPhase.ENDED);
			var text:TextGame = e.target as TextGame;
			if(touch && text){
				if(text.name!=null && text.name.slice(0,7)=="upgrade"){
					Research.getInstance().levelUp(text.index);
					update();
				}else if(text.name == "back"){
					removeEventListener(TouchEvent.TOUCH,onTouch);
					this.parent.removeChild(this);
					
					var start:StartScene = new StartScene();
					UnitManager.getInstance().sceneSprite.addChild(start);
				}
			}
		}
		
		public function update():void{
			for(var i:int=0;i<5;i++){
				var level:int = Research.getInstance().getLevel(i);
				stars[i].text = "【"+Tools.starString(level,5)+"】";
			}
			current.text = "当前拥有升级点数：" + Research.getInstance().left;
		}
	}
}