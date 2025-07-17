package zombie.behaviors 
{
	import fplib.base.Behavior;
	import net.flashpunk.utils.Input;
	import net.flashpunk.utils.Key;
	import net.flashpunk.FP;
	
	/**
	 * ...
	 * @author Diogo Muller
	 */
	public class DebugInfoBehavior extends Behavior
	{
		
		public function DebugInfoBehavior() 
		{
			Input.define("Debug", Key.F12);
		}
		
		override public function update():void 
		{
			super.update();
			
			if ( Input.check("Debug") )
			{
				FP.console.enable();
			}
		}
		
	}

}