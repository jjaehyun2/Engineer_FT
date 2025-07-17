package 
{
	import managers.SoundManager;
	import screens.Game;
	import screens.Menu;
	import starling.display.Sprite;
	import starling.utils.AssetManager;
	import utils.Preloader;
	/**
	 * ...
	 * @author LeleoSan
	 */
	public class Root extends Sprite
	{
		/** assets */
		private var preloader:Preloader;
		private var assetManager:AssetManager;
		public static var assets:AssetManager;
		/** objects */
		private var menu:Menu;
		private var game:Game;
		
		public function Root()  { }
		public function init():void
		{
			assetManager = new AssetManager();
			assetManager.verbose = true;
			Root.assets = assetManager;
			
			preloader = new Preloader(start);
			addChild(preloader);
		}
		private function start():void
		{
			if (preloader) { preloader.destroy(); preloader = null; }
			
			SoundManager.initVolumes(0.4);
			
			loadMenu();
		}
		private function loadMenu():void
		{
			menu = new Menu(loadGame);
			addChild(menu);
		}
		private function loadGame():void
		{
			if (menu) { menu = null; }
			
			game = new Game();
			addChild(game);
		}
		public function destroy():void
		{
			removeChildren(0, -1, true);
			
			Root.assets.dispose();
			Root.assets.purge();
			Root.assets.purgeQueue();
		}
	}

}