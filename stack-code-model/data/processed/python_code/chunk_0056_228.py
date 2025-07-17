package classes 
{
	import com.greensock.easing.Linear;
	import com.greensock.TweenLite;
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.filters.ColorMatrixFilter;
	import flash.geom.Point;
	import flash.text.TextField;
	import flash.utils.getTimer;
	import flash.utils.setTimeout;
	/**
	 * ...
	 * @author Lucas Moyano
	 */
	public class Character extends MovieClip
	{
		public var label:String;
		public var id:int;
		public var scene:int;
		public var getKey:Boolean;
		
		private var _direction:int;
		
		private var actions:Array;
		private var idx:int;
		private var timerLastAction:Number;
		private var lastTween:TweenLite;
		private var dialogue:Sprite;
		private var isOccupied:Boolean;
		private var isBlue:Boolean;
		private var isLastChar:Boolean;
		private var flagOpenMetalDoor:Boolean;
		private var metalDoor:MovieClip;
		private var isTeleport:Boolean;
		private var isPaused:Boolean;
		private var timerPausedTime:int;
		private var flagNextAction:Boolean;
		
		public var mc:MovieClip;
		
		public function Character(id:int) 
		{			
			cacheAsBitmap = true;
			isLastChar = true;
			mouseEnabled = false;
			actions = [];
			isOccupied = false;
			mouseChildren = false;
			idx = 0;
			timerLastAction = 0;
			this.id = id;
			
			if (id > 6)
				mc = new MCOldCharacter();
			else
				mc = new MCCharacter();
			
			direction = 3;
			addChild(mc);
			
			switch(id) // id
			{			
				case 0: // test
					addActions([
						{ name:"moveTo", x:488 + 10, y:243 + 10 },
						{ name:"awake" },
						
						{ name:"changeScene", value:4 },
						
					]);
					
					break;
					
				case 1:
					addActions([
						{ name:"setOccupation", value:true },
						{ name:"moveTo", x:488+10, y:243+10 },
						{ name:"awake" },
						
						{ name:"talk", value:"Que extraño... No recuerdo nada..." },
						{ name:"talk", value:"Y no tengo resaca..." },
						{ name:"rotate", value:4 },
						{ name:"rotate", value:3 },
						{ name:"rotate", value:2 },
						{ name:"rotate", value:3 },
						{ name:"talk", value:"Parece que estoy en una especie de Aventura Gráfica." },
						{ name:"rotate", value:2 },
						{ name:"talk", value:"Me molesta mucho ese cronómetro..." },
						{ name:"rotate", value:3 },
						
						{ name:"setOccupation", value:false }
					]);
					
					break;
					
				case 2:
					addActions([
						{ name:"setOccupation", value:true },
					 { name:"moveTo", x:572, y:288 } ,
					 { name:"awake" } ,
					// { name:"changeScene", value:2 } ,
					 { name:"wait", value:1 } ,
					 { name:"talk", value:"¡¿Pero qué?!" } ,
					 { name:"rotate", value:4 } ,
					 { name:"rotate", value:1 } ,
					 { name:"talk", value:"¡Un fantasma del pasado!" } ,
						{ name:"setOccupation", value:false }
					]);
					break;
					
				case 3:
					addActions([
						{ name:"setOccupation", value:true },
					 { name:"moveTo", x:595+20, y:344+20 } ,
					 { name:"awake" } ,
					// { name:"changeScene", value:2 } ,
						{ name:"setOccupation", value:false }
					]);
					break;
					
				case 4:
					addActions([
						{ name:"setOccupation", value:true },
					 { name:"moveTo", x:559+20, y:403+20 } ,
					 { name:"awake" } ,
						{ name:"setOccupation", value:false }
					]);
					break;
					
				case 5:
					addActions([
						{ name:"setOccupation", value:true },
					 { name:"moveTo", x:480+20, y:443+20 } ,
					 { name:"awake" } ,
						{ name:"setOccupation", value:false }
					]);
					break;
					
				case 6:
					addActions([
						{ name:"setOccupation", value:true },
					 { name:"moveTo", x:359+20, y:456+20 } ,
					 { name:"awake" } ,
					 { name:"talk", value:"¡Pero, joder, esto es imposible!" } ,
						{ name:"setOccupation", value:false }
					]);
					break;
					
				case 7:
					addActions([
						{ name:"setOccupation", value:true },
					 { name:"moveTo", x:241+20, y:437+20 } ,
					 { name:"awake" } ,
					 { name:"talk", value:"Me siento más viejo." } ,
						{ name:"setOccupation", value:false }
					]);
					break;
					
				case 8:
					addActions([
						{ name:"setOccupation", value:true },
					 { name:"moveTo", x:165+20, y:399+20 } ,
					 { name:"awake" } ,
					 { name:"talk", value:"Esto me recuerda a aquella orgía con 7 putas chinas que me monté el otro día" } ,
						{ name:"setOccupation", value:false }
					]);
					break;
					
				case 9:
					addActions([
						{ name:"setOccupation", value:true },
					 { name:"moveTo", x:127+20, y:331+20 } ,
					 { name:"awake" } ,
						{ name:"setOccupation", value:false }
					]);
					break;
					
				case 10:
					addActions([
						{ name:"setOccupation", value:true },
					 { name:"moveTo", x:172+20, y:285+20 } ,
					 { name:"awake" } ,
					{ name:"talk", value:"¡Me cago en el puto creador de este juego!" },
					{ name:"setOccupation", value:false }
					]);
					break;
					
				case 11:
					addActions([
						{ name:"setOccupation", value:true },
					 { name:"moveTo", x:248+20, y:245+10 } ,
					 { name:"awake" } ,
						{ name:"setOccupation", value:false }
					]);
					break;
					
				case 12:
					addActions([
						{ name:"setOccupation", value:true },
					 { name:"moveTo", x:363+20, y:223+20 } ,
					 { name:"awake" } ,
					{ name:"setOccupation", value:false }
					]);
					break;
			}
			
		}
		
		public function checkWaitAction():void
		{
			var aux:Number;
			
			if (!isLastChar) return;
			if (timerLastAction > 0)
			{
				aux = (getTimer() - timerLastAction) / 1000;
				if (aux > 0)
				{
					actions.push( { name:"wait", value:aux } );
					idx++;
					timerLastAction = 0;
				}
			}
		}
		
		public function setBlackAndWhite():void
		{
			var redValue:Number, greenValue:Number, blueValue:Number;
			var values:Array;
			var blackAndWhiteFilter:ColorMatrixFilter;
			
			isLastChar = false;
			
			redValue = 0.555;
			greenValue = 0.355;
			blueValue = 0.285;
			
			values = new Array();
			values = values.concat([redValue, greenValue, blueValue, 0, 0]); // red
			values = values.concat([redValue, greenValue, blueValue, 0, 0]); // green
			values = values.concat([redValue, greenValue, blueValue, 0, 0]); // blue
			values = values.concat([ 0, 0, 0, 1, 0]); // alpha
			
			blackAndWhiteFilter = new ColorMatrixFilter(values);
			this.filters = [blackAndWhiteFilter];
		}
		
		public function setNormalColor():void
		{
			this.filters = [];
		}
		
		public function addAction(obj:Object)
		{
			var action:Object;
			
			if (isOccupied) return;
			
			checkWaitAction();
			actions.push(obj);
			if (actions.length - 1 == idx)
			{
				nextAction();
			}
			else
			{
				if (obj.name == "walk")
				{
					action = actions[actions.length - 2 ];
					if (action.name == "walk")
					{
						lastTween.kill();
						action.x = x;
						action.y = y;
						completeAction();
					}
				}
			}
		}
		
		private function nextAction():void 
		{
			var obj:Object;
			
			if (isPaused)
			{
				flagNextAction = true;
				return;
			}
			
			if (actions.length == idx)
			{
				timerLastAction = getTimer();
				return;
			}
				
			obj = actions[idx];
			
			if (isTeleport)
			{
				if (obj.name == "talk")
				{
					// Hardcode
					return;
				}
			}
			
			if (obj.name == "end")
			{
				idx++;
				nextAction();
				return;
			}
			
			if (obj.name == "if")
			{
				if (!Keys.id(obj.value))
				{
					do
					{
						idx++;
						obj = actions[idx];
					}while (obj.name != "end");
				}
				idx++;
				nextAction();
				return;
			}
			
			if (obj.name == "if not")
			{
				if (Keys.id(obj.value))
				{
					do
					{
						idx++;
						obj = actions[idx];
					}while (obj.name != "end");
				}
				idx++;
				nextAction();
				return;
			}
			
			this[obj.name](obj);
		}
		
		function completeAction():void
		{
			try {
			mc["character"].gotoAndStop("stop");
			idx++;
			nextAction();
			} catch (e:Error){ }
		}
		
		// Actions
		
		public function putKey(obj:Object):void
		{
			try { // error
			mc["character"].gotoAndPlay("key");
			mc["character"].addEventListener("key", onCompleteSecretDoor, false, 0, true);
			} catch(e:Error) { }
		}
		
		// Passage
		public function openSecretDoor(obj:Object):void
		{
			if (getKey)
			{
				isOccupied = false;
				addAction({ name:"putKey" });
				obj.secretDoor.play();
				obj.secretDoor.label = "Cueva";
				obj.keySecretDoor.play();
				if (visible)
					Sounds.play(Sounds.tremorSound);
				
				addAction({ name:"setKey", id:Keys.S4_SECRET_DOOR, value:true });
				addAction({ name:"rotate", value:4 });
				addAction({ name:"rotate", value:1 });
				addAction( { name:"setOccupation", value:true } );
				addAction({ name:"talk", value:"Un pasadizo secreto, que oportuno." });
				addAction( { name:"setOccupation", value:false } );
				isOccupied = true;
			}
			else
			{
				isOccupied = false;
				addAction( { name:"setOccupation", value:true } );
				addAction( { name:"talk", value:"Creo que es un reloj sin manecillas." } );
				addAction( { name:"setOccupation", value:false } );
				isOccupied = true;
			}
			completeAction();
		}
		
		private function onCompleteSecretDoor(e:Event):void 
		{
			mc["character"].removeEventListener("key", onCompleteSecretDoor);
			completeAction();
		}
		
		// Metal Door
		public function tryOpenMetalDoor(obj:Object):void
		{
			mc["character"].gotoAndPlay("open_down");
			mc["character"].addEventListener("open_down", onTryOpenMetalDoor, false, 0, true);
			
			if (Keys.FIRST_METAL_DOOR)
			{
				if (Keys.SECOND_METAL_DOOR)
				{
					completeAction();
				}
				else
				{
					Keys.SECOND_METAL_DOOR = this;
					flagOpenMetalDoor = true;
					metalDoor = obj.door;
				}
			}
			else
				Keys.FIRST_METAL_DOOR = this;
		}
		
		private function onTryOpenMetalDoor(e:Event):void 
		{
			mc["character"].removeEventListener("open_down", onTryOpenMetalDoor);
			if (flagOpenMetalDoor)
			{
				mc["character"].gotoAndPlay("open_up");
				Keys.FIRST_METAL_DOOR.mc["character"].gotoAndPlay("open_up");
				mc["character"].addEventListener(Event.COMPLETE, onCompleteMetalDoor, false, 0, true);
				if (metalDoor.currentFrame == 1)
				{
					metalDoor.play();
					if (visible)
						Sounds.play(Sounds.metalDoor);
				}
			}
			else
				openingMetalDoor();
		}
		
		private function onCompleteMetalDoor(e:Event):void 
		{
			mc["character"].removeEventListener(Event.COMPLETE, onCompleteMetalDoor);
			completeAction();
			Keys.FIRST_METAL_DOOR.completeAction();
		}
		
		private function openingMetalDoor():void 
		{
			mc["character"].gotoAndPlay("opening");
			mc["character"].addEventListener("open_down", onTryOpenMetalDoor, false, 0, true);
		}
		
		
		
		/*
		public function openMetalDoor(obj:Object):void
		{
			if (obj.door)
			{
				if (obj.door.currentFrame == 1)
					obj.door.play();
			}
			mc["character"].gotoAndPlay("open_up");
			mc["character"].addEventListener(Event.COMPLETE, onCompleteMetalDoor);
		}
		
		public function backMetalDoor(obj:Object):void
		{
			mc["character"].gotoAndPlay("open_back");
			mc["character"].addEventListener(Event.COMPLETE, onCompleteBackMetalDoor);
		}
		
		private function onCompleteBackMetalDoor(e:Event):void 
		{
			mc["character"].removeEventListener(Event.COMPLETE, onCompleteBackMetalDoor);
			completeAction();
		}*/
		// End Metal Door
		
		public function changeScene(obj:Object):void
		{
			var game:Game;
			
			if (!parent) return;
			game = parent.parent as Game;
			scene = obj.value;
			
			game.changeScene(obj.value, this);
			completeAction();
		}
		
		public function changeObject(obj:Object):void
		{
			obj.obj[obj.action](obj.value);
			completeAction();
		}
		
		public function setOccupation(obj:Object):void
		{
			isOccupied = obj.value;
			completeAction();
		}
		
		public function setKey(obj:Object):void
		{
			Keys.setId(obj.id, obj.value);
			completeAction();
		}
		
		public function walk(obj:Object):void 
		{
			var time:Number;
			var distX:int, distY:int;
			var endX:int, endY:int;
			
			distX = obj.x - x;
			distX = distX < 0 ? distX * -1 : distX;
			
			distY = obj.y - y;
			distY = distY < 0 ? distY * -1 : distY;
			
			if (distX > distY)
			{
				if (obj.x > x)
					direction = 2;
				else
					direction = 4;
			}
			else 
			{
				if (obj.y > y)
					direction = 3;
				else
					direction = 1;				
			}
			
			mc["character"].gotoAndPlay("walk");
			
			endX = obj.x;
			endY = obj.y
			
			
			if (scene == 5)
			{
				if (obj.rX) {
					if (id <= 6)
						endX += obj.rX * (6) * 0.3 - 200;
					else
						endX += obj.rX * (id) * 0.3 - 200;
				}
			}
			else
			{
				if (obj.rX)
					endX += obj.rX * Math.random();
				if (obj.rY)
					endY += obj.rY * Math.random();
			}
			
			time = Point.distance(new Point(x, y), new Point(endX, endY)) / 100;
			
			if (time < 0.20)
			{
				completeAction();
				return;
			}
				
			lastTween = TweenLite.to(this, time, { x:endX, y:endY, onComplete:completeAction, ease:Linear.easeNone } );
		}
		
		public function endTeleport(obj:Object):void
		{
			mc["character"].addEventListener("end_teleport", onCompleteEndTeleport, false, 0, true);
			mc["character"].gotoAndPlay("end_teleport");
		}
		
		private function onCompleteEndTeleport(e:Event):void 
		{
			mc["character"].removeEventListener("end_teleport", onCompleteEndTeleport);
			completeAction();
		}
		
		public function wait(obj:Object):void 
		{
			/*if (isLastChar)
				completeAction();
			else*/
				lastTween = TweenLite.to(this, obj.value, { onComplete:completeAction } );
		}
		
		public function rotate(obj:Object):void
		{
			direction = obj.value;
			mc["character"].gotoAndStop("stop");
			lastTween = TweenLite.to(this, 0.5, { onComplete:completeAction } );
		}
		
		public function takeKey(obj:Object)
		{
			if (obj.keyPaint.currentFrame != 1) 
			{
				completeAction();
				return;
			}
			
			obj.keyPaint.play();
			getKey = true;
			completeAction();
		}
		
		public function open(obj:Object)
		{
			mc["character"].gotoAndPlay("open");
			mc["character"].addEventListener("open", onOpen, false, 0, true);
			if (visible)
				Sounds.play(Sounds.takeSound, 0.25);
		}
		
		public function kick(obj:Object)
		{
			mc["character"].gotoAndPlay("kick");
			mc["character"].addEventListener("kick", onKick, false, 0, true);
			if (visible)
				Sounds.play(Sounds.kickSound);
		}
		
		private function onKick(e:Event):void 
		{
			var game:Game;
			
			mc["character"].removeEventListener("kick", onKick);
			Keys.COUNT_KICK++;
			if (Keys.COUNT_KICK > 30)
			{
				game = parent.parent as Game;
				game.endGame();
				Keys.COUNT_KICK = 0;
			}
			completeAction();
		}
		
		public function push(obj:Object)
		{
			isBlue = obj.isBlue;
			mc["character"].gotoAndPlay("init_hand");
			mc["character"].addEventListener("init_hand", onCompletePush, false, 0, true);
		}
		
		private function endHand(obj:Object):void {
				mc["character"].gotoAndPlay("end_hand");
				mc["character"].addEventListener("end_hand", onCompleteEndHand, false, 0, true);
		}
		
		private function handComplete():void
		{
			if (!isLastChar) {
				completeAction();
				return;
			}
			
			isOccupied = false;
			addAction( { name:"teleport" } );
			addAction( { name:"changeScene", value:5 } );
			addAction( { name:"directionTo", value:1 } );
			addAction( { name:"moveTo", x:682, y:465} );
			addAction( { name:"endTeleport" } );
			addAction( { name:"setOccupation", value:false });
			isOccupied = true;
			completeAction();
		}
		
		private function teleport(obj:Object):void
		{
			direction = 2;
			if (scene != 4) {
				mc["character"].gotoAndStop("stop");
				return;
			}
			
			isTeleport = true;
			mc["character"].gotoAndPlay("teleport");
			mc["character"].addEventListener("teleport", onCompleteTeleport, false, 0, true);
		}
		
		private function onCompletePush(e:Event):void 
		{
			mc["character"].removeEventListener("init_hand", onCompletePush);
			
			if (isBlue)
			{
				mc["character"].stop();
				//mc["character"].gotoAndPlay("end_hand");
				//mc["character"].addEventListener("end_hand", onCompleteEndHand, false, 0, true);
			}
			else
			{
				if (Keys.id(Keys.S5_HAND_BLUE))
				{
					handComplete();
				}
				else
				{					
					isOccupied = false;
					addAction( { name:"endHand" } );
					addAction( { name:"setOccupation", value:false });
					isOccupied = true;
					completeAction();
				}
			}
		}
		
		private function onCompleteTeleport(e:Event):void 
		{
			var flagStop:Boolean;
			
			mc["character"].removeEventListener("teleport", onCompleteTeleport);
			if (isTeleport) {
				if (actions.length - 1 >= idx + 7) {
					if (actions[idx + 7].name == "talk") {
						do {
							idx++;
							if (actions[idx].name == "changeScene")
							{
								//Keys.setId(Keys.S5_HAND_RED, false);
								if (actions[idx].value == 5)
									flagStop = true;
							}
							if (idx > actions.length)
								flagStop = true;
						}	while (!flagStop);
						
						addAction( { name:"rotate", value:4 } );
						addAction( { name:"changeScene", value:5 } );
						
						changeScene( { value:5 } );
						return;
					}
				}
			}
			completeAction();
		}
		
		private function onCompleteEndHand(e:Event):void 
		{
			mc["character"].removeEventListener("end_hand", onCompleteEndHand);
			completeAction();
		}
		
		private function onOpen(e:Event):void 
		{
			removeEventListener("open", onOpen);
			completeAction();
		}
		
		public function awake(obj:Object)
		{
			mc["character"].gotoAndPlay("awake");
			mc["character"].addEventListener("awake", onAwake, false, 0, true);
		}
		
		private function onAwake(e:Event):void 
		{
			removeEventListener("awake", onAwake);
			completeAction();
		}
		
		public function talk(obj:Object)
		{
			var txt:TextField;
			
			mc["character"].gotoAndStop("talk");	
			
			dialogue = new Dialogue();
			
			addChild(dialogue);
			txt = dialogue["texto"];
			txt.wordWrap = true;
			
			txt.htmlText = obj.value;
			txt.y -= 200;
			
			lastTween = TweenLite.to(this, txt.length / 20, { onComplete:function()
			{
				try { // error
				if (contains(dialogue))
					removeChild(dialogue);
				dialogue = null;
				completeAction();
				} catch(e:Error) { }
			}} );
		}
		
		public function setName(value:String):void
		{
			label = value;
		}
		
		public function moveTo(obj:Object)
		{				
			this.x = obj.x;
			this.y = obj.y;
			
			if (obj.rX)
				this.x += obj.rX * Math.random();
			if (obj.rY)
				this.y += obj.rY * Math.random();
				
			completeAction();
		}
		
		public function directionTo(obj:Object)
		{
			direction = obj.value;
			completeAction();
		}
		
		public function startWalking():void
		{
			mc["character"].gotoAndPlay("walk");
		}
		
		public function stopWalking():void
		{
			mc["character"].gotoAndPlay("stoping_walk");
		}
		
		public function removeDialogue():void
		{
			if (dialogue) 
			{
				removeChild(dialogue);
				dialogue = null;
			}
		}
		
		public function reset():void 
		{
			if (lastTween)
				lastTween.kill();
				
			removeDialogue();
			
			isPaused = false;
			flagNextAction = false;
			metalDoor = null;
			flagOpenMetalDoor = false;
			isTeleport = false;
			isBlue = false;
			isOccupied = false;
			getKey = false;
			visible = true;
			scene = 0;
			idx = 0;
			direction = 3;
			nextAction();
		}
		
		public function addActions(array:Array):void 
		{
			var obj:Object;
			var i:uint, lengt:uint;
			
			if (isOccupied) return;
			checkWaitAction();
			
			lengt = array.length;
			for (i = 0; i < lengt; i++)
			{
				obj = array[i];
				if (obj.checkBefore)
				{
					if (obj.checkBefore == "if")
					{
						if (!Keys.id(obj.value))
						{
							var flag:Boolean;
							do
							{
								i++;
								obj = array[i];
							} while (obj.checkBefore != "end");
							continue;
						}
					}
					
					else if (obj.checkBefore == "if not")
					{
						if (Keys.id(obj.value))
						{
							do
							{
								i++;
								obj = array[i];
							} while (obj.checkBefore != "end");
							continue;
						}
					}
					
					else if (obj.checkBefore == "end")
					{
						continue;
					}
				}
				else
				{
					actions.push(obj);
				}
			}
			
			nextAction();
		}
		
		public function pause():void 
		{
			isPaused = true;
			if (lastTween)
			{
				lastTween.pause();
				//timerLastAction
			}
			timerPausedTime = getTimer();
		}
		
		public function start():void 
		{
			var difPausedTime:int;
			
			isPaused = false;
				
			if (timerLastAction > 0)
			{
				difPausedTime = getTimer() - timerPausedTime;
				timerLastAction += difPausedTime;
			}
			
			if (lastTween)
			{
				lastTween.play();
			}
			
			if (flagNextAction)
			{
				nextAction();
			}
		}
		
		public function kill():void 
		{
			reset();
			
			label = null;
			actions = null;
			lastTween = null;
			dialogue = null;
			metalDoor = null;
			mc = null;
		}
		
		public function get direction():int 
		{
			return _direction;
		}
		
		public function set direction(value:int):void 
		{
			mc.gotoAndStop(value);
			_direction = value;
		}
		
		
	}

}