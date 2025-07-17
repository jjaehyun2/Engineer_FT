package  {
	
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.filters.BlurFilter;
	import flash.text.TextFormat;
	import org.flintparticles.common.counters.Blast;
	import org.flintparticles.common.debug.Stats;
	import org.flintparticles.common.initializers.AlphaInit;
	import org.flintparticles.common.initializers.ApplyFilter;
	import org.flintparticles.common.initializers.ColorInit;
	import org.flintparticles.common.initializers.ImageClass;
	import org.flintparticles.twoD.actions.ApproachNeighbours;
	import org.flintparticles.twoD.actions.BoundingBox;
	import org.flintparticles.twoD.actions.Friction;
	import org.flintparticles.twoD.actions.Move;
	import org.flintparticles.twoD.actions.ScaleAll;
	import org.flintparticles.twoD.emitters.Emitter2D;
	import org.flintparticles.twoD.initializers.Position;
	import org.flintparticles.twoD.renderers.DisplayObjectRenderer;
	import org.flintparticles.twoD.zones.RectangleZone;
	import org.flintparticles.common.displayObjects.Dot;
	import org.flintparticles.common.displayObjects.Ring;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	public class FlintScreen extends Sprite {
		
		public function FlintScreen() {
			var emitter:Emitter2D = new Emitter2D();
			emitter.counter = new Blast(500);
			
			emitter.addInitializer(new ColorInit(0xFF0000, 0x00FF00));
			emitter.addInitializer(new ApplyFilter(new BlurFilter(2, 2, 3)));
			emitter.addInitializer(new AlphaInit(0.9, 1));
			emitter.addInitializer(new ImageClass(Dot,[1.5]));
			//emitter.addInitializer(new ImageClass(Ring,[8]));
			
			emitter.addInitializer(new Position(new RectangleZone(0, 0, 640, 480)));
			
			emitter.addAction(new Move());
			emitter.addAction(new ApproachNeighbours(30, 100));
			emitter.addAction(new ScaleAll(2,10));
			emitter.addAction(new Friction(30));
			
			var renderer:DisplayObjectRenderer= new DisplayObjectRenderer();
			renderer.addEmitter(emitter);
			addChild(renderer);
			
			emitter.start();
		}
		
	}
}