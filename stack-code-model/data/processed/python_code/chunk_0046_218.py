package
{
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.MouseEvent;
	public class Platform extends MovieClip
	{
		public var type:String;
		public var Online:Boolean;
		function Platform(_x,_y,Type)
		{
			Online = true;
			type = Type;
			Weapons.Weapon21Cost = 50;
			x = Math.round(_x);
			y = Math.round(_y);
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
		}
		public function Resume()
		{
		}
	}
}