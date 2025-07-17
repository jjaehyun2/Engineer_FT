package classes {
	
	import classes.Piece;
	import classes.WhiteMan;
	import classes.BlackMan;
	import classes.Queen;
	import classes.Striker;
	import flash.utils.Timer;
	import flash.events.TimerEvent;
	import flash.display.MovieClip;
	
	public dynamic class PieceEngine extends Array {
		public var rotateTimer:Timer = new Timer(0,180);
		protected var timer:Timer = new Timer(0);
		protected var board:MovieClip;
		protected var holeArray:Array = new Array();
		protected var deadMen:Array = new Array();
		protected var currentPlayer:int;
		protected var currentRound:int;
		protected var roundPlayed:Boolean = false;
		protected var players:Array = new Array();
		
		public function PieceEngine(Board:MovieClip){
			rotateTimer.addEventListener(TimerEvent.TIMER, rotateTick);
			timer.addEventListener(TimerEvent.TIMER, update);
			board = Board;
			holeArray.push(board.hole1);
			holeArray.push(board.hole2);
			holeArray.push(board.hole3);
			holeArray.push(board.hole4);
		}
		
		public function newGame():void {
			currentPlayer = 1;
			currentRound = 1;
			const r:Number = 31 / 2;
			deadMen = new Array();
			for each(var piece in this) {
				board.removeChild(piece);
			}
			this.length = 0;
			
			push(new Striker(0, 245.2));
			
			push(new Queen(0,0));
			
			push(new WhiteMan(0,	+2*Math.sqrt(3)*r	));
			push(new WhiteMan(0, 	-2*Math.sqrt(3)*r	));
			push(new WhiteMan(-3*r, +Math.sqrt(3)*r		));
			push(new WhiteMan(-3*r, -Math.sqrt(3)*r		));
			push(new WhiteMan(-2*r, 0					));
			push(new WhiteMan(r, 	+Math.sqrt(3)*r		));
			push(new WhiteMan(r, 	-Math.sqrt(3)*r		));
			push(new WhiteMan(3*r,	+Math.sqrt(3)*r		));
			push(new WhiteMan(3*r,	-Math.sqrt(3)*r		));
	
			push(new BlackMan(-4*r,	0					));
			push(new BlackMan(-2*r,	+2*Math.sqrt(3)*r	));
			push(new BlackMan(-2*r,	-2*Math.sqrt(3)*r	));
			push(new BlackMan(-r,	+Math.sqrt(3)*r		));
			push(new BlackMan(-r,	-Math.sqrt(3)*r		));
			push(new BlackMan(2*r,	0					));
			push(new BlackMan(2*r,	+2*Math.sqrt(3)*r	));
			push(new BlackMan(2*r,	-2*Math.sqrt(3)*r	));
			push(new BlackMan(4*r,	0					));
			
			for each(piece in this) {
				board.addChild(piece);
			}
			
			start();
		}
		
		public function checkForNextRound() {
			currentRound++;
			deadMen[currentRound] = new Array();
			var nextPlayer:Boolean = false;
			if (!deadMen[currentRound-1].length) nextPlayer = true;
			//if ()
		}
//		public function arrayContainsType(array:Array, type:String):Boolean {
//			//for each()
//		}
		public function nextRound() {
			currentPlayer = int(!Boolean(currentPlayer));
			roundPlayed = false;
			rotateTimer.reset();
			rotateTimer.start();
		}
		public function start():void {
			timer.start();
		}
		
		public function stop():void{
			timer.stop();
		}
		
		public function getPieceAt(x:Number, y:Number){
			var temp = null;
			for each(var piece in this){
				if(piece.x == x && piece.y == y){
					temp = piece;
				}
			}
			return temp;
		}
		
		public function update(e:TimerEvent):void {
			for each(var piece in this) {
				checkForDeadMen(piece);
				applyFricition(piece);
				piece.x += piece.vX;
				piece.y += piece.vY;
			}
			
			CheckAndPerformWallCollision();
			CheckForCarromPieceCollision();
			
			if (piecesIsMoving()) {
				roundPlayed = true;
			}
			
			if (!piecesIsMoving() && !rotateTimer.running && roundPlayed) {
				checkForNextRound();
			}
		}
		
		private function piecesIsMoving():Boolean {		
			var pieces_moving:Boolean = false;
			for each (var piece in this) {
				if (piece.vX != 0 || piece.vY != 0) {
					pieces_moving = true;
				}
			}
			return pieces_moving;
		}
		
		private function CheckAndPerformWallCollision():void {
			for each(var piece in this) {
				if (piece.x >= 370 - piece.radius) {
					piece.vX = - Math.abs(piece.vX);
					piece.x = 370 - piece.radius;
				} if (piece.x <= -370 + piece.radius) {
					piece.vX = Math.abs(piece.vX);
					piece.x = -370 + piece.radius;
				} if (piece.y <= -370 + piece.radius) {
					piece.vY = Math.abs(piece.vY);
					piece.y = -370 + piece.radius;
				} if (piece.y >= 370 - piece.radius) {
					piece.vY = - Math.abs(piece.vY);
					piece.y = 370 - piece.radius;
				}
			}
		}
			
		private function CheckForCarromPieceCollision():void {
			for (var i:int = 1; i < this.length; i++ ) {
				for (var j:int = 0; j < i; j++ ) {
					var dX:Number = this[i].x - this[j].x;
					var dY:Number = this[i].y - this[j].y;
					var minD:Number = this[i].radius + this[j].radius;
					
					if (dX * dX + dY * dY <= minD * minD) {
						PerformCarromPieceCollision(this[i], this[j]);
					}
				}
			}
		}
		
		private function applyFricition(piece:Piece):void {
			var vX:Number = piece.vX;
			var vY:Number = piece.vY;
			var v:Number = Math.sqrt(vX * vX + vY * vY);
			
			if (Math.abs(v) > 25*piece.friction) {
				piece.vX -= piece.friction * (vX / v);
				piece.vY -= piece.friction * (vY / v);
			}else if (Math.abs(v) > 4*piece.friction) {
				piece.vX -= 4*piece.friction * (vX / v);
				piece.vY -= 4*piece.friction * (vY / v);
			}else {
				piece.vX = 0;
				piece.vY = 0;
			}
		}
		
		private function PerformCarromPieceCollision(obj1, obj2):void {
			var m1:Number = obj1.mass;
			var m2:Number = obj2.mass;
			
			var vX1:Number = obj1.vX;
			var vY1:Number = obj1.vY;
			var vX2:Number = obj2.vX;
			var vY2:Number = obj2.vY;
			
			var dX:Number = obj1.x - obj2.x;
			var dY:Number = obj1.y - obj2.y
			var d:Number = Math.sqrt(dX * dX + dY * dY);
			
			var vP1:Number = (vX1 * dX + vY1 * dY) / d;
			var vP2:Number = (vX2 * dX + vY2 * dY) / d;
			var vN1:Number = (vX1 * dY - vY1 * dX) / d;
			var vN2:Number = (vX2 * dY - vY2 * dX) / d;
			
			var vP1_New:Number = (m1 * vP1 - m2 * vP1 + 2 * m2 * vP2) / (m1 + m2);
			var vP2_New:Number = (m2 * vP2 - m1 * vP2 + 2 * m1 * vP1) / (m1 + m2);
			
			obj1.vX = (vP1_New * dX + vN1 * dY) / d;
			obj2.vX = (vP2_New * dX + vN2 * dY) / d;
			obj1.vY = (vP1_New * dY - vN1 * dX) / d;
			obj2.vY = (vP2_New * dY - vN2 * dX) / d;
			
			obj1.x += dX / (2 * d) * (obj1.radius + obj2.radius - d);
			obj2.x -= dX / (2 * d) * (obj1.radius + obj2.radius - d);
			obj1.y += dY / (2 * d) * (obj1.radius + obj2.radius - d);
			obj2.y -= dY / (2 * d) * (obj1.radius + obj2.radius - d);
		}
		
		private function checkForDeadMen(obj:Piece):void{
			for each(var hole in holeArray) {
				var dx:Number = (hole.x - obj.x);
				var dy:Number = (hole.y - obj.y);
				var d:Number = Math.sqrt(dx * dx + dy * dy);
				if (d < hole.width / 2) {
					board.removeChild(obj);
					deadMen[currentRound].push(obj);
					this.splice(this.indexOf(obj), 1);
				}
			}
		}
		
		protected function rotateTick(e:TimerEvent):void{			
			const boardLength:int = 600;
			board.rotation += 1;
			if(Math.abs(board.rotation % 180) > 45 && Math.abs(board.rotation % 180) < 135){
				board.scaleX = boardLength/740 * Math.sqrt(2)/2;
				board.scaleY = boardLength/740 * Math.sqrt(2)/2;
			}else{
				board.height = boardLength;
				board.width = boardLength;
			}
		}
		
		public function get Players():Array {
			return players;
		}
		
		public function set Players(newValue:Array):void {
			players = newValue;
		}
		
		public function get CurrentPlayer():int {
			return currentPlayer;
		}
		
		public function set CurrentPlayer(newValue:int):void {
			currentPlayer = newValue;
		}
	}
}