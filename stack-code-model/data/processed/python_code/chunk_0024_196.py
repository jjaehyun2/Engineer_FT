package zombie 
{
	/**
	 * ...
	 * @author Diogo Muller
	 */
	public class Assets 
	{
		/* IMAGES */
		[Embed(source = "../../assets/images/background.png")] public static const IMAGE_BACKGROUND : Class;
		
		/* TILESETS */
		[Embed(source = "../../assets/images/tileset.png")] public static const IMAGE_TILESET : Class;
		[Embed(source = "../../assets/images/tileset2.png")] public static const IMAGE_EVILTILE : Class;
		
		/* MAPS */
		[Embed(source = "../../assets/maps/MainMap.oel", mimeType = "application/octet-stream")] public static const MAP_MAIN : Class;
		
		/* SPRITES */
		[Embed(source = "../../assets/images/main-normal.png")] public static const SPRITE_MAIN_NORMAL : Class;
		[Embed(source = "../../assets/images/main-zombie.png")] public static const SPRITE_MAIN_ZOMBIE : Class;
		
		[Embed(source = "../../assets/images/npc-normal-01.png")] public static const SPRITE_NPC_NORMAL_01 : Class;
		[Embed(source = "../../assets/images/npc-zombie-01.png")] public static const SPRITE_NPC_ZOMBIE_01 : Class;
		[Embed(source = "../../assets/images/npc-normal-02.png")] public static const SPRITE_NPC_NORMAL_02 : Class;
		[Embed(source = "../../assets/images/npc-zombie-02.png")] public static const SPRITE_NPC_ZOMBIE_02 : Class;
		[Embed(source = "../../assets/images/npc-normal-03.png")] public static const SPRITE_NPC_NORMAL_03 : Class;
		[Embed(source = "../../assets/images/npc-zombie-03.png")] public static const SPRITE_NPC_ZOMBIE_03 : Class;
		[Embed(source = "../../assets/images/npc-normal-04.png")] public static const SPRITE_NPC_NORMAL_04 : Class;
		[Embed(source = "../../assets/images/npc-zombie-04.png")] public static const SPRITE_NPC_ZOMBIE_04 : Class;
        
        [Embed(source="../../assets/images/oldman.png")] public static const SPRITE_OLDMAN : Class;
		
		public static var SPRITE_NPC_NORMAL : Array = [SPRITE_NPC_NORMAL_01, SPRITE_NPC_NORMAL_02, SPRITE_NPC_NORMAL_03, SPRITE_NPC_NORMAL_04];
		public static var SPRITE_NPC_ZOMBIE : Array = [SPRITE_NPC_ZOMBIE_01, SPRITE_NPC_ZOMBIE_02, SPRITE_NPC_ZOMBIE_03, SPRITE_NPC_ZOMBIE_04];
		
		/* PARTICLES */
		[Embed(source = "../../assets/images/heart.png")] public static const PARTICLE_HEART : Class;
		[Embed(source = "../../assets/images/blood.png")] public static const PARTICLE_BLOOD : Class;
		
		/* BUTTON */
		[Embed(source = "../../assets/images/ButtonBase.png")] public static const BUTTON_NORMAL : Class;
		[Embed(source = "../../assets/images/ButtonOver.png")] public static const BUTTON_OVER : Class;
		[Embed(source = "../../assets/images/ButtonPressed.png")] public static const BUTTON_PRESSED : Class;
		
		/* MUSIC */
		[Embed(source = "../../assets/music/mus loop.mp3")] public static const MUSIC_BGM01 : Class;
		[Embed(source = "../../assets/music/zumclov.mp3")] public static const MUSIC_CREDITS : Class;
		[Embed(source = "../../assets/music/arp1.mp3")] public static const MUSIC_BGM02 : Class;
		[Embed(source = "../../assets/music/bal loop.mp3")] public static const MUSIC_BGM03 : Class;
		[Embed(source = "../../assets/music/night.mp3")] public static const MUSIC_BGM04 : Class;
		[Embed(source = "../../assets/music/parapira.mp3")] public static const MUSIC_OPENING : Class;
		[Embed(source = "../../assets/music/ariparap.mp3")] public static const MUSIC_EASTEREGG : Class;
		
		/* SOUND EFFECTS */
		[Embed(source = "../../assets/sounds/zombie01.mp3")] public static const SOUND_ZOMBIE : Class;
		[Embed(source = "../../assets/sounds/no1.mp3")] public static const SOUND_HUMAN1 : Class;
		[Embed(source="../../assets/sounds/no2.mp3")] public static const SOUND_HUMAN2 : Class;
	}

}