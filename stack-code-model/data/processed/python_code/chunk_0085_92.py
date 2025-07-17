package  
{
	import com.greensock.TweenLite;
	import flash.display.BitmapData;
	import flash.geom.Point;
	import flash.net.navigateToURL;
	import flash.net.URLRequest;
	import net.flashpunk.Entity;
	import net.flashpunk.FP;
	import net.flashpunk.Graphic;
	import net.flashpunk.graphics.Canvas;
	import net.flashpunk.graphics.Emitter;
	import net.flashpunk.graphics.Graphiclist;
	import net.flashpunk.graphics.Image;
	import net.flashpunk.graphics.Spritemap;
	import net.flashpunk.utils.Input;
	import net.flashpunk.utils.Key;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Player extends Entity
	{
		[Embed(source = "Assets/Graphics/Characters/optimized_char_16x16.png")]private static const ANIM:Class;
		public var anim:Spritemap = new Spritemap(ANIM, 16, 16);
		
		private var _v:Point;
		private var _spawnPoint:Point = new Point();
		private static const GRAVITY:Number = .70;
		private static const FRICTION:Number = .80;
		
		private const maxXSpeed:Number = 18;//25.2;
		private var numJumpsLeft:Number = 0;
		
		private var _bootsEquipped:Boolean = false;		
		
		private var currentTrack:int = -1;
		
		
		
		private var tombEmitter:Emitter;
		private const TOMB_MAX_PARTICLES:uint = 100;
		
		public function Player(p:Point) 
		{
			anim.setFrame(1);
			x = _spawnPoint.x = p.x;
			y = _spawnPoint.y = p.y;
			_v = new Point();
			
			graphic = anim;
			var frameRate:Number = 20;
			anim.add("down", [11, 10, 9], frameRate, true);
			anim.add("left", [3, 4, 5], frameRate, true);
			anim.add("right", [6, 7, 8], frameRate, true);
			anim.add("up", [9, 10, 11], frameRate, true);
			anim.add("still", [0,1,2], frameRate/4, true);
			anim.add("stillLadder", [9,10,11], frameRate/4, true);
			//graphic = new Image(new BitmapData(16,16,false,0x00FF00));
			setHitbox(16, 16, 0, 0);
			type = "player";
			
			layer = 201;
			
			/*tombEmitter = new Emitter(new BitmapData(1, 1), 1, 1);
			tombEmitter.newType("death", [0]);
			tombEmitter.relative = false;
			tombEmitter.setAlpha("death", 1, 0);
			tombEmitter.setMotion("death", 70, 10, 0.2, 40 , 80, 0.2);
			
			graphic = new Graphiclist(anim, tombEmitter);
			
			*/
		}
		
		public override function update():void
		{
			updateMovement();
			updateCollision();
			super.update();
		}
		
		private function updateMovement():void
		{
			if ((Input.pressed(Key.Z)) && numJumpsLeft > 0)
			//if(Input.mousePressed && numJumpsLeft > 0)
			{
				MainMenu.jumpSound.play(.2);
				_v.y = -8;
				numJumpsLeft--;
			}
			else if (_v.y > 15.5) _v.y = 15.5;
			
			if (Input.check(Key.LEFT) || Input.check(Key.A))
			{
				_v.x += -.9;
			}
			else if (Input.check(Key.RIGHT) || Input.check(Key.D))
			{
				_v.x += .9;
			}
			
			//explosion testing
			if (Input.check(Key.SPACE))
			{
				/*for (var i:int = 0; i < TOMB_MAX_PARTICLES; i++)
				{
					tombEmitter.emit("death", x+width/2, y + height/2);
				}*/
			}
			/*if (world.mouseX > x+8+20)
			{
				_v.x += .9;
				//anim.play("right");
			}
			else if (world.mouseX < x+8-20)
			{
				_v.x += -.9;
				//anim.play("left");
			}*/
			//if (_v.x < 0.5 && _v.x > -0.5) anim.play("still");
		}
		
		private function updateCollision():void
		{
			var spike:Entity =  collide("Spike", x, y);
			if (spike != null)
			{
				var tomb:Tomb = new Tomb(this, spike);
				world.add(tomb);
				
				var sp:Spike = spike as Spike;
				if (sp.anim.frame == 8)
				{
					_v.y = -8
				}
				else if (sp.anim.frame == 7)
				{
					_v.x = 8;
				}
				else if (sp.anim.frame == 6)
				{
					_v.x = -8;
				}
				else if (sp.anim.frame == 4)
				{
					_v.y = 8;
				}
				
				
				
				
				
				//_v.x = -_v.x * 2;
				//_v.y = -_v.y * 1.5;
			}
			
			var fireball:Entity = collide("Fireball", x, y);
			if (fireball != null)
			{
				var tomb2:Tomb = new Tomb(this, fireball);
				world.add(tomb2);
				world.remove(fireball);
				
				MainMenu.hitSound.play();
				
				
				respawn();
				return;
			}
			
			var sign:Entity = collide("Sign", x, y);
			if (sign != null)
			{
				(world as MainMenu).getMessageBox().showMessage((sign as Sign).message,(sign as Sign).timeout);
				
				if (sign as Sign == Sign.Profusion && Input.released(Key.SPACE))
				{
					navigateToURL(new URLRequest("http://www.profusiongames.com/?gameref=miniPassage"));
				}
				if (sign as Sign == Sign.Music && Input.released(Key.SPACE))
				{
					trace("trying to toggle music");
					if (FP.volume == 1) 
					{
						FP.volume = 0;
						(sign as Sign).setMessage("Music OFF. Click to toggle.");
					}
					else 
					{
						FP.volume = 1;
						(sign as Sign).setMessage("Music ON. Click to toggle.");
						MainMenu.unmuteToggleSound.play();
					}
					MainMenu.flash.start(0xFFFFFF,.5,.6);
				}
			}
			
			if (_v.x > maxXSpeed) _v.x = maxXSpeed;
			else if (_v.x < -maxXSpeed) _v.x = -maxXSpeed;
			if (collide("Water", x, y))
			{
				_v.x *= .9;
				_v.y *= .95;
			}
			if (collide("Lava", x, y))
			{
				_v.x *= .80;
				_v.y *= .99;
				_v.y = -4;
				var tomb3:Tomb = new Tomb(this, null);
				world.add(tomb3);
				MainMenu.hitSound.play(0.8);
				//bump the player up for an 'ouch'
			}
			_v.x *= FRICTION;
			x += _v.x;
			
			
			if (collide("level", x, y) || collide("FireSpitter",x,y))
			{
				//Handle Collision here.
				if (FP.sign(_v.x) > 0)
				{
					//moving to the right
					_v.x = 0;
					x = Math.floor(x / 16) * 16 + 16 - width;
				}
				else
				{
					_v.x = 0;
					x = Math.floor(x/16) * 16 + 16
				}
			}
			var onLadder:Boolean = MainMenu.ladder.collidePoint(0, 0, x+4, y+8) || MainMenu.ladder.collidePoint(0, 0, x, y+16) || MainMenu.ladder.collidePoint(0, 0, x+12, y+8);//collide("Ladder", x, y) != null;
			if (onLadder)
			{
				if (Input.check(Key.W) || Input.check(Key.UP))
				//if (world.mouseY < y+8-15)
				{
					_v.y += -.9;
					//anim.play("down");
				}
				//else if (world.mouseY > y+8+15)
				else if (Input.check(Key.S) || Input.check(Key.DOWN))
				{
					_v.y += .9;
					//anim.play("up");
				}
				else
				{
					_v.y *= .8
					//anim.play("stillLadder");
				}
				
				if (_v.y > 3.5) _v.y = 3.5;
				if (_v.y < -3.5) _v.y = -3.5;
			}
			else //not touching a ladder
			{
				_v.y += GRAVITY;
			}
			y += _v.y;
			if (collide("level", x, y) || collide("FireSpitter",x,y))
			{
				//Handle Collision here.
				if (FP.sign(_v.y) > 0)
				{
					//moving to the ground
					y = Math.floor((y) / 16) * 16 + 16 - height;
					_v.y = 0;
					numJumpsLeft = 2;
				}
				else
				{
					//moving to the ceiling
					y = Math.floor((y) / 16) * 16 + 16
					_v.y = 0;
				}
			}
			
			
			if (onLadder)
			{
				if (_v.y > 1.9)
					anim.play("up");
				else if (_v.y < -1.9)
					anim.play("down");
				else
					anim.play("stillLadder");
			}
			else
			{
				if (_v.x > 1.5)
					anim.play("right");
				else if (_v.x < -1.5)
					anim.play("left");
				else
					anim.play("still");
			}
			
			
			
			
			
			if (x > 600)
			{
				MainMenu.scoreBox.start();
				if (x < 615)
				{
					currentTrack = y < 400 ? 1 : y < 500 ? 2 : 3;
					FP.tween(MainMenu.menuMusic, { volume:0 }, 1, { type:2 } );
					MainMenu.gameMusic.loop(1);
					FP.tween(MainMenu.gameMusic, { volume:1 }, 1, { type:2 } );
					MainMenu.flash.start(0xFFFFFF,.5,1);
				}
			}
			else
			{
				if (MainMenu.gameMusic.playing)
				{
					MainMenu.flash.start(0x000000,.5,1);
					FP.tweener.clearTweens();
					MainMenu.gameMusic.stop();
					MainMenu.gameMusic.volume = 0;
					MainMenu.menuMusic.loop(1);
					FP.tween(MainMenu.menuMusic, { volume:1 }, 2, { type:2 } );
				}
				MainMenu.scoreBox.reset();
				currentTrack = -1;
			}
			
				
			if (x > 5040)
			{
				MainMenu.flash.start(0xFFFFFF, .5, 1);
				
				//game finished!
				MainMenu.scoreBox.pause();
				var score:int = MainMenu.scoreBox.getScore();
				var isHigherScore:Boolean = ScoreTracker.beatLevel(currentTrack, score);
				var combinedScore:int = ScoreTracker.getCombinedScore();
				trace("Beat " + currentTrack + " with score " + score + ". Is that score better than an old one? " + isHigherScore +  "  The combined score is " + combinedScore + ".");
				
				var textToShow:String = "";
				if (isHigherScore)
					textToShow += "Faster Run! ";
				textToShow += "Your run time was " + score + ". ";
				textToShow += " Your combined total is " + combinedScore + ".";
				
				
				(world as MainMenu).getMessageBox().showMessage(textToShow,10000);
				//update highscores
				Sign.Adventure.setMessage( "Adventure! Best run time: " + ScoreTracker.getHighScore(3));
				Sign.Tricky.setMessage( "Tricky! Best run time: " + ScoreTracker.getHighScore(2));
				Sign.Simple.setMessage( "Simple! Best run time: " + ScoreTracker.getHighScore(1));
				
				
				/*if (ScoreTracker.getHighScore(1) < 60 * 60 &&
					ScoreTracker.getHighScore(2) < 60 * 60 &&
					ScoreTracker.getHighScore(3) < 60 * 60)
				{
					trace("Attempting to get leaderboard");
					var o:Object = { n: [8, 9, 0, 12, 4, 8, 12, 1, 9, 7, 14, 0, 15, 13, 10, 11], f: function (i:Number,s:String):String { if (s.length == 16) return s; return this.f(i+1,s + this.n[i].toString(16));}};
					var boardID:String = o.f(0,"");
					MochiScores.showLeaderboard({boardID: boardID});
				}*/
				
				x = _spawnPoint.x;
				y = _spawnPoint.y;
				
				FP.tween(MainMenu.gameMusic, { volume:0 }, 1, { type:2, complete:function():void { MainMenu.gameMusic.stop() } } );
				MainMenu.menuMusic.loop(1);
				FP.tween(MainMenu.menuMusic, { volume:1 }, 1, { type:2 } );
			}
			
			var guessX:int = int(FP.lerp(FP.camera.x, x - 320, 0.2));
			var guessY:int = int(FP.lerp(FP.camera.y, y - 240, 0.2));
			FP.camera.x = guessX > 4480 ? 4480 : guessX < 0? 0 :guessX;
			FP.camera.y = guessY > 480 ? 480 : guessY < 0 ? 0 : guessY;
			//trace(guessX, guessY);
		}
		
		public function respawn():void
		{
			_v.x = 0;
			_v.y = 0;
		}
	}

}