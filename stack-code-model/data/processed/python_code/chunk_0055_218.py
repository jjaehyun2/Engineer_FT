package devoron.sdk.sdkmediator.ascsh.commands
{
	import devoron.sdk.sdkmediator.ascsh.commands.CMD;
	
	/**
	 * MxmlcCMD
	 * @author Devoron
	 */
	public class MxmlcCMD extends CMD
	{
		//public var load_config:String;
		//public var o:String;
		
		public function MxmlcCMD()
		{
			//super.objectProperties.put("
		}
		
		public override function getCode():String
		{
			//\n
			
			// если параметр имеет значение, то он включается в команду
			
			return "mxmlc " + super.getArguments() + "\n";
			//return "mxmlc -load-config=runtime_mxmlc_config.xml -o F:/Projects/projects/flash/studio/Studio13/bin/generated" +(uid)+ ".swf\n"
			//return "mxmlc -load-config=config2.xml -o F:/Projects/projects/flash/studio/Studio13/bin/generated" +(uid++)+ ".swf\n"
			//return "mxmlc -load-config=config2.xml -o test1.swf\n"
		}
		
		public override function getDesctiption():String
		{
			return "mxmlc";
		}
		
	}

}