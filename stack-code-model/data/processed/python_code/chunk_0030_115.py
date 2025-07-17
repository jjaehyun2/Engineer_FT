package com.illuzor.otherside.tools {
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public final class AssetsFlash {
		
		// ATLASSES XML BEGIN
		
		[Embed(source = "../../../../../bin/graphics/atlas_1.xml", mimeType = "application/octet-stream")]
		public static const atlas_1_xml:Class;
		
		[Embed(source = "../../../../../bin/graphics/menu_atlas.xml", mimeType = "application/octet-stream")]
		public static const menu_atlas_xml:Class;
		
		[Embed(source = "../../../../../bin/graphics/asteroids_atlas.xml", mimeType = "application/octet-stream")]
		public static const asteroids_atlas_xml:Class;
		
		// ATLASSES XML END
		
		
		// ATLASSES ATF BEGIN
		[Embed(source = "../../../../../bin/graphics/atlas_1.atf", mimeType = "application/octet-stream")]
		public static const atlas_1:Class;
		
		[Embed(source = "../../../../../bin/graphics/menu_atlas.atf", mimeType = "application/octet-stream")]
		public static const menu_atlas:Class;
		
		[Embed(source = "../../../../../bin/graphics/asteroids_atlas.atf", mimeType = "application/octet-stream")]
		public static const asteroids_atlas:Class;
		
		// ATLASSES ATF END
		
		
		// LANGUAGES BEGIN
		
		[Embed(source = "../../../../../bin/configs/langs/en.lang", mimeType = "application/octet-stream")]
		public static const en:Class;
		
		[Embed(source = "../../../../../bin/configs/langs/ru.lang", mimeType = "application/octet-stream")]
		public static const ru:Class;
		
		// LANGUAGES END
		
		
		// LEVELS BEGIN
		
		[Embed(source = "../../../../../bin/configs/levels/zone1level1.osl", mimeType = "application/octet-stream")]
		public static const zone1level1:Class;
		
		// LEVELS END
		
		
		// OTHER CONFING BEGIN
		
		[Embed(source = "../../../../../bin/configs/fonts/press_font.fnt", mimeType = "application/octet-stream")]
		public static const press_font:Class;
		
		[Embed(source = "../../../../../assets/curves.json", mimeType = "application/octet-stream")]
		public static const curves:Class;
		
		// OTHER CONFING END 
		
	}
}