package devoron.data.core.base 
{
	import devoron.data.core.UID;
	/**
	 * ...
	 * @author Devoron
	 */
	public final class DataUID 
	{
		private var _uid:String;
		
		public function DataUID() 
		{
			_uid = UID.create();
		}
		
		public function toString():void {
			return _uid;
		}
		
	}

}