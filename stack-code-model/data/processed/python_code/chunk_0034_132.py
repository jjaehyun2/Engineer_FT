package  
{
	import net.flashpunk.Entity;
	import net.flashpunk.FP;
	import roshan.buffer.ClientChange;
	import roshan.buffer.ACTION;
	import roshan.buffer.WorldChange;
	import flash.net.Socket;

	public class Network extends Entity 
	{
		private var sock:Socket;
		private var moveFunc:Function;
		private var mapFunc:Function;
		private var mapChangeFunc:Function;
		public var hero:Hero = null;
		public var sayText:String = "";
		private var actions:Array = [];
		private var directions:Array = [];
		private var send_walk_delay:Number = 0;
		
		public function Network(insock:Socket, inMoveFunc:Function, inMapChangeFunc:Function, inMapFunc:Function) 
		{
			sock = insock;
			moveFunc = inMoveFunc;
			mapFunc = inMapFunc;
			mapChangeFunc = inMapChangeFunc;
			
			var cs:ClientChange = new ClientChange();
			try {
				cs.writeDelimitedTo(sock);
				sock.flush();
			} catch (e:Error) {  }
		}
		
		public function startAction(action:int, direction:int):void {
			actions.push(action);
			directions.push(direction);
		}
		
		override public function update():void 
		{
			if ( hero != null &&
				(actions.length > 0 || sayText != "" || hero.towardsX != hero.lastX || hero.towardsY != hero.lastY)) {
				sendUpdate();
			}
			try {sock.bytesAvailable} catch (e:Error) { return; }
			if (sock.bytesAvailable > 0) 
			{
				try { /* Catch and throw away bad messags */
					var wc:WorldChange = new WorldChange();
					wc.mergeDelimitedFrom(sock);
				} catch (e:Error) { return; }
					
				wc.characterActions.forEach(moveFunc);
				wc.mapData.forEach(mapFunc);
				wc.mapChange.forEach(mapChangeFunc);
			}
		}
		
		private function sendUpdate():void 
		{
			var change:ClientChange;
			actions = actions.filter(function(action:int, i:int, all:Array):Boolean { 
				change = new ClientChange();
				change.action = action;
				change.direction = directions.pop();
				change.writeDelimitedTo(sock);
				return false;
			});

			if (send_walk_delay > 0.3 && (hero.towardsX != hero.lastX || hero.towardsY != hero.lastY))
			{
				change = new ClientChange();
				change.direction = xyKeyboard.dirFromXY(hero.lastX, hero.lastY, hero.towardsX, hero.towardsY);
				change.action = ACTION.WALK;
				change.writeDelimitedTo(sock);
				send_walk_delay = 0;
			}
			send_walk_delay += FP.elapsed;
				
			if (sayText != "") 
			{
				change = new ClientChange();
				change.action = ACTION.SAY;
				change.say = sayText;
				sayText = "";
				change.writeDelimitedTo(sock);
				
			}
			
			sock.flush();
		}
	}
}