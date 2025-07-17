package
{
	import com.pblabs.engine.resource.ResourceBundle;
	
	public class Resources extends ResourceBundle
	{
		
		[Embed(source = "../assets/levelDescriptions.xml", mimeType = 'application/octet-stream')]
		public var _levelDesc:Class;
		
		[Embed(source = "../assets/Levels/level1.pbelevel", mimeType = 'application/octet-stream')]
		public var _level1:Class;
		
		[Embed(source = "../assets/Levels/level2.pbelevel", mimeType = 'application/octet-stream')]
		public var _level2:Class;
		
		[Embed(source = "../assets/Levels/level3.pbelevel", mimeType = 'application/octet-stream')]
		public var _level3:Class;
		
		[Embed(source = "../assets/Levels/level4.pbelevel", mimeType = 'application/octet-stream')]
		public var _level4:Class;
		
	}
}