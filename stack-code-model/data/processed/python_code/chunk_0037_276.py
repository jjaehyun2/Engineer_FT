package game {
	
	public class Assets {
		// credits
		[Embed(source = "../../doc/credits.txt", mimeType="application/octet-stream")] public static const CREDITS:Class;
		
		// the player graphic
		[Embed(source = "../../res/img/avatar.png")] public static const PLAYER:Class;
		
		// the finish area image
		[Embed(source = "../../res/img/finish.png")] public static const FINISH:Class;
		
		// backdrop
		[Embed(source = "../../res/img/backdrop.png")] public static const BACKDROP_GRAPHICS:Class;
		
		// tilesheet
		[Embed(source = "../../res/img/buch_tiles.png")] public static const TILESHEET:Class;
		
		// main music
		[Embed(source = "../../res/sfx/Wave_After_Wave!_v0_9.mp3")] public static const MUSIC:Class;
		
		// portal effect
		[Embed(source = "../../res/sfx/portal.mp3")] public static const PORTAL_SOUND:Class;
		
		// explosion sound
		[Embed(source = "../../res/sfx/explosion.mp3")] public static const EXPLOSION_SOUND:Class;
		
		// custom game font
		[Embed(source = "../../res/font/SPACEMAN.ttf", embedAsCFF = "false", fontFamily = 'Space Font')] public const SPACE_FONT:Class;
		
		// choice
		[Embed(source = "../../res/sfx/choice.mp3")] public static const CHOICE:Class;
	}
	
}