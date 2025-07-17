package baseflex.utils.displayObject
{
	import flash.display.DisplayObject;
	
	public class GetDisplayObject
	{
		public function GetDisplayObject()
		{
		}
		
		
		public static function getChild(target:Object, name:String):DisplayObject {
			for(var i:int =0; i<target.numChildren;++i) {
				var child:DisplayObject = target.getChildAt(i) as DisplayObject;
				if(String(child).toLowerCase().indexOf(name.toLowerCase()) > -1) {
					return child;					
				}
			}
			
			return null;
		}
	}
}