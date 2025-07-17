package system.loader
{
	import flash.utils.Dictionary;

	public class ResManager
	{
		private var _resDict:Dictionary;
		private static var _instance:ResManager;
		
		public function ResManager()
		{
			_resDict = new Dictionary();
		}
		
		public function getRes(url:String):Res{
			if(!_resDict[url])
				_resDict[url] = new Res(url);
			return _resDict[url] as Res;
		}
		
		public static function instance():ResManager{
			if(!_instance)
				_instance = new ResManager();
			return _instance;
		}
	}
}