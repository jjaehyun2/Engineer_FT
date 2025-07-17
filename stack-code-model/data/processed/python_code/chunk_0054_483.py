package {
	import org.flixel.FlxG;
	
	public class Night extends SfsSprite {
		
		private const COLOR:Number = 0xaa090939;
		
		private var _isNight:Boolean = false;
		private var counter:Number;
		
		public function Night() {
			this.zOrder = 10000;
			super( 0, 0 );
			this.makeGraphic( 640, 480, COLOR, true );
			this.blend = "multiply";
			this.visible = false;
			this.alpha = 0;
		}
		
		public function toggleNight():void {
			isNight = !isNight;
			visible = true;
		}
		
		override public function update():void {
			counter += FlxG.elapsed;
			if (counter < 0.005 )
				return;
			counter = 0;
			if ( !isNight ) {
				if ( alpha <= 0 ) {
					isNight = false;
					visible  = false;
				} else {
					alpha -= 0.00125;
				}
			} else {
				if ( alpha >= 1 ) 
					return;
					alpha += 0.00125;			
			}
			super.update();
		}
		
		public function get isNight():Boolean 
		{
			return _isNight;
		}
		
		public function set isNight(value:Boolean):void 
		{
			_isNight = value;
		}
		
		public function revert():void {
			fill( COLOR );
		}
			
	}
}