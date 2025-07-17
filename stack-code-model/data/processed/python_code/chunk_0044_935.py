package system 
{
	[_link_Object_]
	[link_system]
	/**
	 * .net对象的基类。因为直接用Object会导致IDE不正常，所以改名为_Object_
	 * @author 
	 */
	public class _Object_
	{

		[creator];
		[native, _system_Object_creator__];
		private static function _creator(type:Class):*;
		
		[native, _system_Object_ctor];
		public function _Object_();
		
		[native,_system_Object_static_equals]
		public static function equals(objA:_Object_,objB:_Object_):Boolean;
		
		[native,_system_Object_static_referenceEquals]
		public static function referenceEquals(objA:_Object_,objB:_Object_):Boolean;
		
		[native,_system_Object_toString]
		public function toString():String;
		
		[native,_system_Object_getHashCode]
		public function getHashCode():int;
		
		[native,_system_Object_equals]
		public function equals(obj:_Object_):Boolean;
		
		
	}

}