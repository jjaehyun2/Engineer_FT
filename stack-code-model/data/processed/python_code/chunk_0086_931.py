package {
	import flash.display.GraphicsGradientFill;
	import org.flixel.FlxEmitter;
	import org.flixel.FlxPoint;
	import org.flixel.FlxSprite;
	import org.flixel.FlxG;
	
	public class Car extends SfsGroup {
		
		private var _carSprite:FlxSprite;
		private var lights:FlxSprite;
		private var emitter:FlxEmitter;
		private var _point:FlxPoint;
		private var lightsStarted:Boolean;
		private var counter:Number;
		private var flicker:Number;
		
		public function Car( carGraphic:Class, carLightsGraphic:Class, width:int=111, height:int=60 ) {
				
			this.carSprite  = new FlxSprite( -500, -500 );
			this.lights     = new FlxSprite( -500, -500 );
			this._point     = new FlxPoint( -500, -500 );
			
			this.carSprite.loadGraphic( carGraphic, true, false, width, height );
			this.lights.loadGraphic( carLightsGraphic, false, false, 0, 0, true );
			this.lights.visible = false;
			this.lights.blend = "screen";
			this.carSprite.addAnimation( "Running", [0, 1, 2, 3], 20, true );
			this.carSprite.play( "Running" );	
			
			var smoke:Smoke = new Smoke();
			emitter = this.loadSmokeEmitter();		
			emitter.add( smoke );
			emitter.at( this.carSprite );
			emitter.start( false, 0.166, 0.25, 0 );	
			
			this.add( carSprite );
			this.add( emitter );
			this.add( lights );
			
			resetLightPosition();
		}
		
	    public function setVelocityX( velocity:int ):Car {
			this.carSprite.velocity.x = velocity;
			this.lights.velocity.x    = velocity;
			return this;
		}
		
		public function setVelocityY( velocity:int ):Car {
			this.carSprite.velocity.y = velocity;
			this.lights.velocity.y    = velocity;
			return this;
		}
		
		public function setPosition( x:int, y:int ):Car {
			this.carSprite.x = x;
			this.carSprite.y = y;
			resetLightPosition();
			return this;
		}
		
		private function resetLightPosition(): void {
			_point = this.carSprite.getMidpoint();
			this.lights.x = _point.x - ( carSprite.width>>1 ) - 142;
			this.lights.y = _point.y - ( carSprite.height>>1 ) + 5;	
		}
		
		private function loadSmokeEmitter(): FlxEmitter {
			var emit:FlxEmitter     = new FlxEmitter(100, 100, 1);
			emit.maxRotation        = 0;
			emit.minRotation        = 0;
			emit.maxParticleSpeed.x = 50;
			emit.maxParticleSpeed.y = 0;
			emit.minParticleSpeed.x = 50;
			emit.minParticleSpeed.y = 0;	
			return emit;
		}
		
		override public function update():void {
			
			counter += FlxG.elapsed;
			flicker += FlxG.elapsed;
				
			emitter.x = this.carSprite.x + this.carSprite.width + 5;	
			emitter.y = this.carSprite.y + this.carSprite.height - 16;
			emitter.setXSpeed( this.carSprite.velocity.x + 50, this.carSprite.velocity.x + 50 );	
			
			super.update();
			
			//needs optimizing
			if ( !( lightsStarted ) && Registry.nightScene.isNight && Registry.nightScene.alpha > 0.5 ) {
				lightsStarted = true;
				counter = 0;
				flicker = 0;
			} else { 
				if ( lightsStarted && ! ( Registry.nightScene.isNight ) && Registry.nightScene.alpha < 0.4 ) {
					lightsStarted = false;
					counter = 0;
					flicker = 0;
				}
			}
			
			if ( counter < 0.4 ) {
				if ( counter <= 0.3 && flicker > 0.1 ) {
					flicker = 0;
					lights.visible = !lights.visible;
				}
				
				if ( counter > 0.3 ) {
					if ( lightsStarted ) {
						lights.visible = true;
					} else {
						lights.visible = false;
					}
				}
			}
		}
		
		public function stampNight( night:NightScene ):void {
			if ( lights.visible ) {
				night.stamp( lights, lights.x, lights.y );
			}
		}
		
		public function get carSprite():FlxSprite {
			return _carSprite;
		}
		
		public function set carSprite(value:FlxSprite):void {
			_carSprite = value;
		}
		
	}
}