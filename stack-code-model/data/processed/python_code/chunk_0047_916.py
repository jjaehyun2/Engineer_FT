package local.managers
{
	import flash.net.URLRequest;
	import flash.net.navigateToURL;
	import flash.text.TextField;
	
	import local.main;
	import local.display.PictureStage;
	import local.display.GalleryMenu;
	import local.display.SWFLoader;
	
	public class XmlManager extends Object
	{
		public static var xml: XML;
		public static var statusText: TextField;
		public static var picStage: PictureStage;
		public static var galleryMenu: GalleryMenu;
		public static var swfLoader: SWFLoader;
		
		private static const grid: Array = [
												[ 0  ,  0   ],
												[ 100, -100 ],
												[ 250,  0   ],
												[ 350,  -75 ],
												[-100,  -75 ],
												[ 150,  120  ]
										   ];
		
		public static function initialize(_xml: XML) : void
		{
			xml = _xml;
			picStage = PictureStage.instance;
			galleryMenu = GalleryMenu.instance;
			swfLoader = SWFLoader.instance;
		}
		
		public static function populateAsHome() : void
		{
			picStage.clear();
			galleryMenu.clear();
			swfLoader.clear();
			var total: int = xml.image.length();
			
			for (var i: int = 0; i < total; i++)
				picStage.addPicture(xml.image[i], grid[i][0], grid[i][1]);
			
			if (total > 0)
				main.instance.activity.show();
		}
		
		public static function showGallery(arr: Array) : void
		{
			var node: XML = arr[0];
			picStage.clear();
			swfLoader.clear();
			galleryMenu.show(node);
			statusText.text = "-    " + node.@name;
		}
		
		public static function showSWF(arr: Array) : void
		{
			picStage.clear();
			galleryMenu.clear();
			swfLoader.show(arr[0], arr[1], arr[2]);
			statusText.text = "-    " + arr[3];
		}
	}
}