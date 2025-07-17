package
{
	import net.flashpunk.World;
	import net.flashpunk.graphics.Text;
	import net.flashpunk.tweens.misc.VarTween;
	import net.flashpunk.FP;
	public class DisconWorld extends World
	{
		public var counter:Number = 0;
		
		public function DisconWorld()
		{
			var txt:Text = new Text("Unable to connect to server.", 180, 240, { color: 'black'} );
			addGraphic(txt);
		}
		override public function update():void {
			super.update()
			counter += FP.elapsed;
			if (counter >= 3)
				FP.world = new GameWorld;
		}
		
	}
}