package devoron.sdk.sdkmediator.ascsh.commands 
{
	/**
	 * HelpCMD
	 * @author Devoron
	 */
	public class HelpCMD extends CMD
	{
		
		public function HelpCMD() 
		{
			
		}
		
		public override function getCode():String {
			return "help\n"
		}
		
		public override function getDesctiption():String {
			return "help";
		}
		
	}

}