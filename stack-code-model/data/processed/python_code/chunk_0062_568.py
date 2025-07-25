package we3d.scene.dynamics 
{
	import flash.events.TimerEvent;
	import flash.utils.Timer;
	
	import we3d.we3d;
	import we3d.mesh.Face;
	import we3d.mesh.Vertex;
	import we3d.scene.SceneParticles;

	use namespace we3d;
	
	/**
	* Abstract base class for particle emitter. A emitter creates the particles over time and updates physics properties on the particles. 
	*/ 
	public class ParticleEmitter 
	{
		public function ParticleEmitter () {
			timer = new Timer(1000/25);
		}
		
		public var points:Vector.<Particle> = new Vector.<Particle>();
		public var so:SceneParticles;
		public var timer:Timer;
		public var generatePerTick:Number = 25;
		public var nozzle:String="box"; // box, sphere, vertices, normal, surface
		public var size:Vertex = new Vertex(50,50,50);
		public var center:Vertex = new Vertex(0,0,0);
		public var particleLimit:int = 500;
		public var gravity:Vertex = new Vertex(0,0,0);
		public var velocity_x:Number=0;
		public var velocity_y:Number=0;
		public var velocity_z:Number=0;
		
		// particle properties
		public var color:int= 0xffffff;  // color of the particles
		public var randomColor:Number= 0;	//  0 - 1 or higher
		public var constrainRandomColor:Boolean = true; // if false randomRed, randomGreen and randomBlue are added randomly to the color
		public var randomRed:int=0;    // 0 - 255
		public var randomGreen:int=0;  // 0 - 255
		public var randomBlue:int=0;   // 0 - 255
		
		public var alpha:Number= 1;
		public var randomAlpha:Number= 0;
		
		public var particleSize:Number=0;
		public var randomParticleSize:Number=0;
		
		public var weight:Number = 1;
		public var randomWeight:Number = 0;
		
		public var resistance:Number = .1;
		public var randomResistance:Number = 0;
		
		public var lifeTime:Number = 100;
		public var randomLifeTime:Number = 0;
		
		public var explosion:Number = 0.5;
		public var randomExplosion:Number = 0;
		
		public function tick(e:TimerEvent) :void {}
		
		public function start() :void 
		{
			timer.addEventListener(TimerEvent.TIMER, tick);
			timer.start();	
		}
		public function stop() :void 
		{
			timer.removeEventListener(TimerEvent.TIMER, tick);
			timer.stop();
		}
		
		public function clone () :ParticleEmitter 
		{
			var r:ParticleEmitter = new ParticleEmitter();
			r.copyFrom(this);
			return r;
		}
		
		public function copyFrom (src:ParticleEmitter) :void {
			timer.delay = src.timer.delay;
			alpha = src.alpha;
			center = src.center.clone();
			color = src.color;
			constrainRandomColor = src.constrainRandomColor;
			explosion = src.explosion;
			generatePerTick = src.generatePerTick;
			gravity = src.gravity.clone();
			lifeTime = src.lifeTime;
			nozzle = src.nozzle;
			particleLimit = src.particleLimit;
			particleSize = src.particleSize;
			randomAlpha = src.randomAlpha;
			randomBlue = src.randomBlue;
			randomColor = src.randomColor;
			randomExplosion = src.randomExplosion;
			randomGreen = src.randomGreen;
			randomLifeTime = src.randomLifeTime;
			randomParticleSize = src.randomParticleSize;
			randomResistance = src.randomResistance;
			randomWeight = src.randomWeight;
			resistance = src.resistance;
			size = src.size.clone();
			velocity_x = src.velocity_x;
			velocity_y = src.velocity_y;
			velocity_z = src.velocity_z;
			weight = src.weight;
		}
	}
}