package 
{
	import flash.display.Bitmap;

	public class AssetsManager
	{
		//// Embed the backround image
		[Embed(source="../assets/background.png")] 
		private var backgroundImgClass:Class;
		
		////// Embed pause image
		[Embed(source="../assets/pause.png")] 
		private var pauseGameImgClass:Class;
		
		//// Embed resume image
		[Embed(source="../assets/resume.png")] 
		private var resumeGameImgClass:Class;
		
		///// Embed blue plane image
		[Embed(source="../assets/plane.png")] 
		private var planeImgClass:Class;
		
		private var bgImage:Bitmap;
		private var pauseGameImg:Bitmap;
		private var resumeGameImg:Bitmap;
		private var planeImg:Bitmap;
		private static var _instance:AssetsManager;
		
		public function AssetsManager()
		{
			///// Using Singleton pattern for Asset Manager class
			if(_instance){
				throw new Error("AssetsManager... use getInstance()");
			}
			_instance = this;
		}
		
		public function LoadAllAssets():void{
			bgImage = new backgroundImgClass() as Bitmap;
			pauseGameImg = new pauseGameImgClass() as Bitmap;
			resumeGameImg = new resumeGameImgClass() as Bitmap;
			planeImg = new planeImgClass() as Bitmap;
		}
		
		public function getBackgroundImg():Bitmap{
			return bgImage;
		}
		
		public function getPauseGameImg():Bitmap{
			return pauseGameImg;
		}
		
		public function getResumeGameImg():Bitmap{
			return resumeGameImg;
		}
		
		public function getPlaneImg():Bitmap{
			return planeImg;
		}
		
		public static function getInstance():AssetsManager{
			if(!_instance){
				_instance = new AssetsManager();
				_instance.LoadAllAssets();
			} 
			return _instance;
		}
	}
}