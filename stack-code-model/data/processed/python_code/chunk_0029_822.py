package as3 {
	
	import flash.display.MovieClip;
	import flash.events.*;
	import flash.desktop.NativeApplication;
	import flash.desktop.SystemIdleMode;
	import flash.system.System;
	
	public class GSMatch extends GameScene {

		var playerPos1:Object = {x:31.5,y:33.85};
		var playerPos2:Object = {x:255.7,y:33.85};
		var playerPos3:Object = {x:31.5,y:141.55};
		var playerPos4:Object = {x:255.7,y:141.55};
		var playerPos5:Object = {x:31.5,y:247.1};
		var playerPos6:Object = {x:255.7,y:247.1};
		var playerPos7:Object = {x:144.1,y:359.05};

		var players:Array = new Array();

		var ourHealth = 0;
		var ourInfect = 0;
		var infectKillAt = 0;
		var isDead = true;
		var player = false;

		var chatVisible = false;

		var winnerObject;
		var chatroomObject;

		public function GSMatch(isPlayer:Boolean, midMatch:Boolean) {
			NativeApplication.nativeApplication.systemIdleMode = SystemIdleMode.KEEP_AWAKE;
			if(!isPlayer){
				bttnMinusHealth.visible = false;
				bttnPlusHealth.visible = false;
				bttnMinusInfect.visible = false;
				bttnPlusInfect.visible = false;
				txtLoading.visible = false;
				txtHealth.visible = false;
				txtInfect.visible = false;
				bgInfect.visible = false;
				bgHealth.visible = false;
				chatroomObject = new Chatroom();
				addChild(chatroomObject);
				chatroomObject.x = 0;
				chatroomObject.y = 744;
				chatroomObject.bttnShowChat.addEventListener(MouseEvent.CLICK, handleToggleChat);
				chatroomObject.inputChat.addEventListener(KeyboardEvent.KEY_DOWN, handleChatSubmit);
			}
			if(midMatch){
				Game.socket.sendInfoRequest();
			}
			player = isPlayer;
			trace("=============[Loaded Match Events]==============");
		}
		private function handleToggleChat(e:MouseEvent):void{
			if(!chatVisible){
				chatroomObject.y = 0;
				chatVisible = true;
			}else{
				chatroomObject.y = 744;
				chatVisible = false;
			}
		}
		private function handleChatSubmit(e:KeyboardEvent):void{
			if(e.keyCode == 13) sendMsg();
		}
		private function sendMsg():void{
			Game.socket.sendMessage(chatroomObject.inputChat.text);
			chatroomObject.inputChat.text = "";
		}
		public function displayChat(username, incomingMessage:String):void{
			//trace(incomingMessage);
			//chatroomObject.txtChat.text = incomingMessage;
			chatroomObject.txtChatBox.text += username;
			chatroomObject.txtChatBox.text += ": ";
			chatroomObject.txtChatBox.text += incomingMessage;
			chatroomObject.txtChatBox.text += "\n";
			chatroomObject.txtChatBox.scrollV = chatroomObject.txtChatBox.maxScrollV;
		}
		private function handleInput(eventType:Number):Function{
			return function(e:MouseEvent):void{
				//TODO: Check what type of input we are handling and tell the server
				Game.socket.sendInput(eventType);
			}
		}
		public function startUpdate(playerID, health, infect, username, maxInfect):void{
			//TODO: This will run every time we get a new player from the servers players array
			//We need to spawn a Player object and position it and store it in an array
			var newPlayer:Player = new Player(playerID, username, health, infect, maxInfect);
			addChild(newPlayer);
			players.push(newPlayer);
			trace(">Loaded new player: " + username);
			//trace(playerID+"|"+health+"|"+infect+"|"+username+"|"+maxInfect);
			positionNewPlayer(newPlayer);
			txtHealth.text = health;
			txtInfect.text = infect;
			infectKillAt = maxInfect;
			chatroomObject.parent.setChildIndex(chatroomObject, chatroomObject.parent.numChildren - 1);
		}
		public function update(playerID, newHealth, newInfect):void{
			for(var k = 0; k < players.length; k++){
				if(players[k].id == playerID){
					players[k].update(newHealth, newInfect);
					break;
				}
			}
		}
		public function privateUpdate(newHealth, newInfect):void{
			ourHealth = newHealth;
			ourInfect = newInfect;

			if(ourInfect >= infectKillAt || ourHealth <= 0){
				ourHealth = "RIP";
				ourInfect = "RIP";
			}

			txtHealth.text = ourHealth.toString();
			txtInfect.text = ourInfect.toString();
		}
		public function gameOver(winner):void{
			for(var i = numChildren - 1; i >= 0; i--){
				var child = getChildAt(i);
				if(child.hasOwnProperty("dispose")) child.dispose();
				removeChildAt(i);
			}
			winnerObject = new Winner();
			addChild(winnerObject);
			winnerObject.y = 320;
			winnerObject.txtWinner.text = winner;
			if(player){
				winnerObject.bttnRestart.addEventListener(MouseEvent.CLICK, handleRestart);
				winnerObject.bttnQuit.addEventListener(MouseEvent.CLICK, handleQuit);
			}else{
				winnerObject.bttnRestart.visible = false;
				winnerObject.bttnQuit.visible = false;
			}
		}
		public function unlockInput():void{
			trace(">Input unlocked");
			if(player){
				bttnMinusHealth.addEventListener(MouseEvent.CLICK, handleInput(1));
				bttnPlusHealth.addEventListener(MouseEvent.CLICK, handleInput(2));
				bttnMinusInfect.addEventListener(MouseEvent.CLICK, handleInput(3));
				bttnPlusInfect.addEventListener(MouseEvent.CLICK, handleInput(4));
			}
			txtLoading.visible = false;
		}
		private function handleRestart(e:MouseEvent):void{
			winnerObject.bttnRestart.removeEventListener(MouseEvent.CLICK, handleRestart);
			winnerObject.bttnQuit.removeEventListener(MouseEvent.CLICK, handleQuit);
			Game.socket.sendRestart();
		}
		private function handleQuit(e:MouseEvent):void{
			NativeApplication.nativeApplication.exit();
		}
		private function positionNewPlayer(newPlayer):void{
			//trace("Player had their position set");
			switch(players.length){
				case 1:
				    newPlayer.x = playerPos1.x;
				    newPlayer.y = playerPos1.y;
				    break;
				case 2:
				    newPlayer.x = playerPos2.x;
				    newPlayer.y = playerPos2.y;
				    break;
				case 3:
				    newPlayer.x = playerPos3.x;
				    newPlayer.y = playerPos3.y;
				    break;
				case 4:
				    newPlayer.x = playerPos4.x;
				    newPlayer.y = playerPos4.y;
				    break;
				case 5:
				    newPlayer.x = playerPos5.x;
				    newPlayer.y = playerPos5.y;
				    break;
				case 6:
				    newPlayer.x = playerPos6.x;
				    newPlayer.y = playerPos6.y;
				    break;
				case 7:
				    newPlayer.x = playerPos7.x;
				    newPlayer.y = playerPos7.y;
				    break;
			}
		}
		public override function dispose():void {
			if(!player) {
				chatroomObject.bttnShowChat.removeEventListener(MouseEvent.CLICK, handleToggleChat);
				chatroomObject.inputChat.addEventListener(KeyboardEvent.KEY_DOWN, handleChatSubmit);
			}else{
				bttnMinusHealth.removeEventListener(MouseEvent.CLICK, handleInput);
				bttnPlusHealth.removeEventListener(MouseEvent.CLICK, handleInput);
				bttnMinusInfect.removeEventListener(MouseEvent.CLICK, handleInput);
				bttnPlusInfect.removeEventListener(MouseEvent.CLICK, handleInput);
			}
			trace("=============[Unloaded Match Events]==============");
		}
	}
}