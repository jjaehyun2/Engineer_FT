package Helpers{
	import flash.external.ExternalInterface;

	public class Console{

		// a simple wrapper function to console.log...because I hate using fdb
		public static function log(message:*):void{
			try{
				if(ExternalInterface.available){
					ExternalInterface.call('console.log',message);
				}
			}					
			catch(e:Error){
				trace('Error using console.log');
				trace(e.message);
			}
		}
	}
}