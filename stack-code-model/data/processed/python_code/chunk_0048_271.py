package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	public class Shield extends MovieClip
	{
		public var type:String;
		var Online:Boolean;
		var Target:Object;
		function Shield(_x,_y,Type)
		{
			this.buttonMode = true;
			type = Type;
			Online = true;
			x = Math.round(_x);
			y = Math.round(_y);
			addEventListener(MouseEvent.MOUSE_DOWN, onClick);
			addEventListener(Event.ENTER_FRAME, enterFrame);
		}
		function onClick(e:MouseEvent)
		{
			FakeCannon.DragOn(this,type);
		}
		function enterFrame(e:Event)
		{
			Game.planetShield +=0.1;
		}
		public function remove()
		{
			
			var cannons:Array = Game.cannons;
			for(var i in cannons)
			{
				if(cannons[i] == this)
				{
					
					cannons.splice(i,1);
					break;
				}
			}
			removeEventListener(MouseEvent.CLICK, onClick);
			parent.removeChild(this);
		}
		function GoOffline()
		{
			
			Online = false;
			alpha = 0.50;
		}
		function GoOnline()
		{
			Online = true;
			alpha = 1;
		}
		public function Pause()
		{
			removeEventListener(MouseEvent.CLICK, onClick);
		}
		public function Resume()
		{
			addEventListener(MouseEvent.CLICK, onClick);
		}
	}
}