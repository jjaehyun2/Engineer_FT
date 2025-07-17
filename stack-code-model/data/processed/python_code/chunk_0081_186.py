package flash.system
{
	import flash.display.DisplayObjectContainer;
	
	
	public class LoaderContext extends Object
	{
		public var checkPolicyFile:Boolean = false;
		public var applicationDomain:ApplicationDomain = null;
		public var securityDomain:SecurityDomain = null;
		public var allowCodeImport:Boolean;
	
		[API("670")]
		public var requestedContentParent:DisplayObjectContainer;
	
		[API("670")]
		public var parameters:Object;
	
		[API("671", "674")]
		public var imageDecodingPolicy:String;
	
		public function LoaderContext(checkPolicyFile:Boolean = false, applicationDomain:ApplicationDomain = null, securityDomain:SecurityDomain = null):void
		{
		}
	
	
		[API("661")]
		public function get allowLoadBytesCodeExecution():Boolean
		{
			return null;
		}
	
	
		[API("661")]
		public function set allowLoadBytesCodeExecution(allow:Boolean):void
		{
		}
	}
}