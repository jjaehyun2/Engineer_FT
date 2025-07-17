package {
	import org.flixel.*;
	public class PlayState extends FlxState {
		public var clouds:FlxGroup;
		public var aliens:FlxGroup;
		public var hudLives:FlxSprite;
		public var maleTux:FlxSprite;
		public var femaleTux:FlxSprite;
		public var heart:FlxSprite;
		public var hudScore:FlxText;
		public var hudAttribute:FlxText;
		[Embed(source="data/cloud160b.png")] public static var CloudSprite:Class;
		[Embed(source="data/lives.png")] public static var LivesSprite:Class;
		[Embed(source="data/male_tux.png")] public static var MaleTuxSprite:Class;
		[Embed(source="data/female_tux.png")] public static var FemaleTuxSprite:Class;
		[Embed(source="data/heart.png")] public static var HeartSprite:Class;
		[Embed(source="data/pos.mp3")] public static var PosSound:Class;
		[Embed(source="data/neg.mp3")] public static var NegSound:Class;
		public var player_x:Number = 320;
		public var player_y:Number = 400;
		public var player_w:Number = 100;
		public var soundEffectPlaying:Number = 0;
		public var soundEffectPlaying2:Number = 0;
		public var timeToNextCloud:Number = 0;
		public var timeToNextAlien:Number = 0;
		public var aliensKilled:uint = 0;
		public var lives:uint = 9;
		public var aliensPassed:uint = 0;
		override public function create():void {
			bgColor = 0xff80c0ff;
			//clouds
			clouds = new FlxGroup();
			add(clouds);
			//aliens
			aliens = new FlxGroup();
			add(aliens);
			//player
			maleTux = new FlxSprite(player_x-player_w-8,player_y-8,MaleTuxSprite);add(maleTux);
			femaleTux = new FlxSprite(player_x+player_w-8,player_y-8,FemaleTuxSprite);add(femaleTux);
			heart = new FlxSprite(player_x-8,player_y-8,HeartSprite);add(heart);
			heart.facing=0;
			//hud
			hudScore = new FlxText(2,2,120,"Score: 0");
			hudScore.setFormat(null,16,0xffffffff,'left',0xff000000);
			add(hudScore);
			hudLives = new FlxSprite(FlxG.width-16*lives-2,4);
			hudLives.loadGraphic(LivesSprite,false,false,16*lives,16);
			add(hudLives);
			hudAttribute = new FlxText(0,480-13,FlxG.width,"Created by Zanda Games");
			hudAttribute.setFormat(null,8,0xffffffff,'right',0xff000000);
			add(hudAttribute);
		}
		override public function update():void {
			if (FlxG.keys.M) {
				if (FlxG.music.playing) FlxG.music.pause();else FlxG.music.play();
			}
			//
			if (FlxG.keys.J) player_w+=FlxG.elapsed*100;
			if (FlxG.keys.K) if (player_w>20) player_w-=FlxG.elapsed*100;
			//
			var dir_x:Number=0;
			var dir_y:Number=0;
			if (FlxG.keys.LEFT || FlxG.keys.A) dir_x=-1;
			if (FlxG.keys.RIGHT || FlxG.keys.D) dir_x=1;
			if (FlxG.keys.UP || FlxG.keys.W) dir_y=-1;
			if (FlxG.keys.DOWN || FlxG.keys.S) dir_y=1;
			//
			player_x+=FlxG.elapsed*dir_x*300;
			player_y+=FlxG.elapsed*dir_y*300;if (player_y>450) player_y=450;if (player_y<100) player_y=100;
			maleTux.x=player_x-player_w-8;maleTux.y=player_y-8;
			femaleTux.x=player_x+player_w-8;femaleTux.y=player_y-8;
			heart.y=player_y-8;
			//
			if (heart.facing==1) {//right
				heart.velocity.x=FlxG.elapsed*20000;
			} else {//left
				heart.velocity.x=-FlxG.elapsed*20000;
			}
			if (heart.x<maleTux.x+16) {heart.facing=1;heart.x=maleTux.x+16;}
			if (heart.x+16>femaleTux.x) {heart.facing=0;heart.x=femaleTux.x-16;}
			//
			timeToNextAlien-=FlxG.elapsed;
			if (timeToNextAlien<0) {
				if (aliensKilled>(FlxG.width/2-16)/5) {
					aliens.add(new Alien(this,(FlxG.width-16)*Math.random(),20));
				} else {
					aliens.add(new Alien(this,FlxG.width/2-5*aliensKilled+(10*aliensKilled)*Math.random()-8,20));
				}
				timeToNextAlien=50*Math.random()/(10+aliensKilled);
				if (timeToNextAlien<1) timeToNextAlien=1;
			}
			//
			timeToNextCloud-=FlxG.elapsed;
			if (timeToNextCloud<0) {
				clouds.add(new FlxSprite((FlxG.width-160)*Math.random(),0,CloudSprite));
				clouds.members[clouds.members.length-1].velocity.x=0;
				clouds.members[clouds.members.length-1].velocity.y=40+aliensKilled/80;
				timeToNextCloud=6+2*Math.random();
			}
			//
			for(var i:uint=0;i<clouds.members.length;i++) {
				if (clouds.members[i].y>480) {
					clouds.remove(clouds.members[i],true);
					defaultGroup.remove(clouds.members[i],true);
				}
			}
			//
			if (soundEffectPlaying>=0) soundEffectPlaying-=FlxG.elapsed;
			if (soundEffectPlaying2>=0) soundEffectPlaying2-=FlxG.elapsed;
			hudScore.text="Score: "+aliensKilled;
			//
			hudLives.x=FlxG.width-16*lives-2;
			hudLives.loadGraphic(LivesSprite,false,false,16*lives,16);
			//
			super.update();
			//
			FlxU.overlap(aliens,maleTux,deathByAlien);
			FlxU.overlap(aliens,femaleTux,deathByAlien);
			FlxU.overlap(aliens,heart,loveTrumpsHate);
		}
		public function deathByAlien(alien:Alien,player:FlxSprite):void {
			if (alien.facing==0) {
				alien.facing=1;
				if (soundEffectPlaying<=0) {
					soundEffectPlaying=0.25;
					FlxG.play(NegSound);
				}
				aliens.remove(alien,true);
				defaultGroup.remove(alien,true);
				lives--;
				if (lives<=0) {
					FlxG.score=aliensKilled;
					FlxG.state = new EndState();
				} else {
					hudLives.x=FlxG.width-16*lives-2;
					hudLives.loadGraphic(LivesSprite,false,false,16*lives,16);
				}
			}
		}
		public function loveTrumpsHate(alien:Alien,heart:FlxSprite):void {
			if (alien.facing==0) {
				alien.facing=1;
				if (soundEffectPlaying2<=0) {
					soundEffectPlaying2=0.25;
					FlxG.play(PosSound);
				}
				aliensKilled++;
				aliens.remove(alien,true);
				defaultGroup.remove(alien,true);
			}
		}
	}
}