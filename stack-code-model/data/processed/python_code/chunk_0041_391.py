package devoron.sdk.sdkmediator.ascsh.commands 
{
	import devoron.sdk.sdkmediator.ascsh.CMD;
	/**
	 * BaseCMD
	 * @author Devoron
	 */
	public class BaseCMD extends CMD
	{
		private var code:String;
		
		public function BaseCMD() 
		{
			
		}
		
		public function setCode(code:String):void 
		{
			this.code = code;
			
		}
		
		override public function getCode():String 
		{
			return code;
		}
		
	}

}