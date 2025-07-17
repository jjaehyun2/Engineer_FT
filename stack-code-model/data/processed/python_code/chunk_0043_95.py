package {
	import org.flixel.FlxSprite;
	
	public class Road extends SfsSprite {
		
		[Embed(source = './data/road.png')] private var renderedRoad:Class;	
		
		public function Road() {
			this.zOrder = -99;
			super( -96, 192, renderedRoad );
			this.velocity.x = 500;
		}
		
		override public function update():void {
			
			if ( this.x >= 0 ) {
				this.x = -96;
			}
			super.update();
		}
		
	}
}