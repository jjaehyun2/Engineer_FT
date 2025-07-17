package
{
	import flash.media.SoundChannel;
	import flash.media.SoundTransform;
	import flash.events.Event;
	public class Sounds 
	{
		public static var backgroundMusic;
		public static const enemyHitSFX:EnemyHitSFX = new EnemyHitSFX();
		public static const weapon1SFX:Weapon1SFX = new Weapon1SFX();
		public static const weapon2SFX:Weapon2SFX = new Weapon2SFX();
		public static const homingLaserSFX:HomingLaserSFX = new HomingLaserSFX();
		public static const spreadCannonShotSFX:SpreadCannonShotSFX = new SpreadCannonShotSFX();
		public static const spreadCannonSplitSFX:SpreadCannonSplitSFX = new SpreadCannonSplitSFX();
		public static const enemyImpactSFX:EnemyImpactSFX = new EnemyImpactSFX();
		public static const chargingLaserSFX:ChargingLaserSFX = new ChargingLaserSFX();
		public static const aoeCannonSFX:AOECannonSFX = new AOECannonSFX();
		public static const flakCannonSFX:FlakCannonSFX = new FlakCannonSFX();
		public static const rocketLauncherSFX:RocketLauncherSFX = new RocketLauncherSFX();
		public static const energyPrisonSFX:EnergyPrisonSFX = new EnergyPrisonSFX();
		
		public static var MainChannel:SoundChannel;
		public static var MusicChannel:SoundChannel;
		public static var myTransform:SoundTransform = new SoundTransform();
		public static function NewSound(SFX)
		{
			if(Main.sounds == true)
			{
				Sounds.MainChannel = Sounds[SFX].play();
			}
		}
		public static function LaserSound()
		{
			var LaserChannel:SoundChannel;
			LaserChannel =  Sounds["chargingLaserSFX"].play(0,10000);
			return LaserChannel;
		}
		public static function StartMusic()
		{
			var backgroundMusic = new MainMenuMusic();
			Sounds.MusicChannel = backgroundMusic.play(0,10000);
			myTransform.volume = 0;
			MusicChannel.soundTransform = myTransform;
		}
		public static function PlayMusic()
		{
			myTransform.volume = 1;
			MusicChannel.soundTransform = myTransform;
		}
		public static function StopMusic()
		{
			myTransform.volume = 0;
			MusicChannel.soundTransform = myTransform;
		}
		public static function ChangeSong()
		{
			Sounds.MusicChannel.stop()
			backgroundMusic = null;
			var g = Math.round(Math.random()*3);
			if(g == 0)
			{
				backgroundMusic = new BackgroundMusic();
			}
			else if(g == 1)
			{
				backgroundMusic = new g1music();
			}
			else if(g == 2)
			{
				backgroundMusic = new g2music();
			}
			else if(g == 3)
			{
				backgroundMusic = new g3music();
			}
			Sounds.MusicChannel = backgroundMusic.play(0,10000);
			if(Main.music == false)
			{
				myTransform.volume = 0;
			}
			MusicChannel.soundTransform = myTransform;
		}
		public static function MainMenuSong()
		{
			Sounds.MusicChannel.stop()
			backgroundMusic = null;
			var backgroundMusic = new MainMenuMusic();
			Sounds.MusicChannel = backgroundMusic.play(0,10000);
			if(Main.music == false)
			{
				myTransform.volume = 0;
			}
			MusicChannel.soundTransform = myTransform;
		}
		
		
	}
}