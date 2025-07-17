package com.illuzor.otherside.editor.tools  {
	
	import com.illuzor.framework.tools.ImageAtlas;
	import flash.display.Bitmap;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class Assets {
		
		[Embed(source="../../../../../../assets/atlas.png")]
		private static const MainAtlasClass:Class
		[Embed(source="../../../../../../assets/atlas.xml", mimeType = "application/octet-stream")]
		private static const MainAtlasXMLClass:Class;
		
		private static var _mainAtlas:ImageAtlas;
		
		public static function get mainAtlas():ImageAtlas {
			if (!_mainAtlas) _mainAtlas = new ImageAtlas((new MainAtlasClass() as Bitmap).bitmapData, XML(new MainAtlasXMLClass()));
			return _mainAtlas;
		}
		
		[Embed(source="../../../../../../assets/gameElements_atlas.png")]
		private static const GameAtlasClass:Class
		[Embed(source="../../../../../../assets/gameElements_atlas.xml", mimeType = "application/octet-stream")]
		private static const GameAtlasXMLClass:Class;
		
		private static var _gameAtlas:ImageAtlas;
		
		public static function get gamenAtlas():ImageAtlas {
			if (!_gameAtlas) _gameAtlas = new ImageAtlas((new GameAtlasClass() as Bitmap).bitmapData, XML(new GameAtlasXMLClass()));
			return _gameAtlas;
		}
		
	}
}