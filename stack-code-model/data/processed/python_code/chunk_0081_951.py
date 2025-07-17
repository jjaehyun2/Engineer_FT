package com.marioretana.checkersgame {
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	
	/**
	 * This is a utility class to embed all external resources to the application on compilation time.
	 * External resources may be images, sound effects, XML files and others.
	 * @author Mario Retana <maretanar@gmail.com>
	 */
	public class EmbeddedSources {
		
		[Embed(source="/../resources/Tiled/board.tmx", mimeType="application/octet-stream")]
		private static const BOARD_MAP_CLASS : Class;
		
		[Embed(source="/../resources/sprites/board.xml", mimeType="application/octet-stream")]
		private static const BOARD_XML_CLASS : Class;
		
		[Embed(source="/../resources/sprites/board.png")]
		private static const BOARD_BITMAP_CLASS : Class;
		
		[Embed(source="/../resources/sprites/chip-black.png")]
		private static const BLACK_CHIP_CLASS : Class;
		[Embed(source="/../resources/sprites/chip-red.png")]
		private static const RED_CHIP_CLASS : Class;
		[Embed(source="/../resources/sprites/chip-white.png")]
		private static const WHITE_CHIP_CLASS : Class;
		[Embed(source="/../resources/sprites/queen-black.png")]
		private static const BLACK_QUEEN_CLASS : Class;
		[Embed(source="/../resources/sprites/queen-red.png")]
		private static const RED_QUEEN_CLASS : Class;
		[Embed(source="/../resources/sprites/queen-white.png")]
		private static const WHITE_QUEEN_CLASS : Class;
		
		public static const BOARD_MAP:XML = XML(new BOARD_MAP_CLASS());
		public static const BOARD_XML:XML = XML(new BOARD_XML_CLASS());
		public static const BOARD_BITMAP_DATA:BitmapData = Bitmap(new BOARD_BITMAP_CLASS()).bitmapData;
		
		public static const BLACK_CHIP_BITMAPDATA:BitmapData = Bitmap(new BLACK_CHIP_CLASS()).bitmapData;
		public static const RED_CHIP_BITMAPDATA:BitmapData = Bitmap(new RED_CHIP_CLASS()).bitmapData;
		public static const WHITE_CHIP_BITMAPDATA:BitmapData = Bitmap(new WHITE_CHIP_CLASS()).bitmapData;
		public static const BLACK_QUEEN_BITMAPDATA:BitmapData = Bitmap(new BLACK_QUEEN_CLASS()).bitmapData;
		public static const RED_QUEEN_BITMAPDATA:BitmapData = Bitmap(new RED_QUEEN_CLASS()).bitmapData;
		public static const WHITE_QUEEN_BITMAPDATA:BitmapData = Bitmap(new WHITE_QUEEN_CLASS()).bitmapData;
	}
	
}