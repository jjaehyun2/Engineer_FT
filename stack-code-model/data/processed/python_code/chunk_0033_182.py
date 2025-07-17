package system.loader
{
	public class ResDecoder
	{
		public static var TYPE_DISPLAYOBJECT:int = 0;
		public static var TYPE_TEXT:int = 1;
		
		public static var TEXT_TYPE_JSON:int = 0;
		
		public static function getResLoadType(url:String):int{
			var stype:String = url.substr(url.lastIndexOf(".")+1);
			var itype:int = TYPE_DISPLAYOBJECT;
			switch(stype){
				case "json":case"txt":
					itype = TYPE_TEXT;
					break;
				default:
					itype = TYPE_DISPLAYOBJECT;
					break;
			}
			return itype;
		}
		
		public static function getTextType(url:String):int{
			var stype:String = url.substr(url.lastIndexOf(".")+1);
			var itype:int = TEXT_TYPE_JSON;
			switch(stype){
				case "json":
					itype = TEXT_TYPE_JSON;
					break;
			}
			return itype;
		}
		
		public static function parseTextData(data:String):*{
			var itype:int = ResDecoder.getTextType(data);
			switch(itype){
				case TEXT_TYPE_JSON:
					return JSON.parse(data);
			}
		}
	}
}