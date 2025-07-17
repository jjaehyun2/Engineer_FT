package devoron.sdk.sdkmediator.ascsh.commands
{
	import devoron.sdk.sdkmediator.ascsh.commands.CMD;
	import flash.utils.flash_proxy;
	
	/**
	 * CompileCMD
	 * @author Devoron
	 */
	use namespace flash_proxy;
	
	dynamic public class CompileCMD extends CMD
	{
		
		public function CompileCMD()
		{
		
		}
		
		public override function getCode():String
		{
			//\n
			
			// если параметр имеет значение, то он включается в команду
			var args:String = getArguments();
			
			if (args != "") {
				return "compile " + getArguments() + "\n";
			}
			//return "mxmlc -load-config=runtime_mxmlc_config.xml -o F:/Projects/projects/flash/studio/Studio13/bin/generated" +(uid)+ ".swf\n"
			//return "mxmlc -load-config+=F:/Projects/projects/flash/studio/Studio13/application2.xml -o F:/Projects/projects/flash/studio/Studio13/bin/generatedSTD" +12/*(uid++)*/+ ".swf\n"
			return "mxmlc -incremental=true -load-config+=F:/Projects/projects/flash/studio/Studio13/application2.xml -o F:/Projects/projects/flash/studio/Studio13/bin/generatedSTD" +12/*(uid++)*/+ ".swf\n"
			//return "mxmlc -load-config=config2.xml -o test1.swf\n"
		}
		
		public override function getArguments():String
		{
			var args:String = "";
			var keys:Array = objectProperties.keys();
			var value:uint = objectProperties.get("-id");
			
			if (value != 0)
			{
				args += value;
			}
			//for each (var key:String in keys) 
			//{
			//value = objectProperties.get(key);
			//if (value != null) {
			//args += key + "=" + value + " " ;
			//}
			//}
			
			return args;
		}
		
		public override function getDesctiption():String
		{
			return "compile";
		}
	
	}

}