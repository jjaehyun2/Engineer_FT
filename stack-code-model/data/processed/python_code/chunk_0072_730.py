package modules.nnGame.context
{
	import modules.nnGame.controller.NnMainController;
	
	import rb.framework.mvc.GameContext;
	import rb.framework.mvc.Module;
	
	public class NnMainContext extends GameContext
	{
		protected var _socketControl:NnMainController;

		public function get socketControl():NnMainController
		{
			return _socketControl;
		}

		
		public function NnMainContext(key:String="", module:Module=null, parentNode:GameContext=null)
		{
			super(key, module, parentNode);
		}
		
		public override function open():void{
			super.open();
			
			if(_socketControl == null)
			{
				_socketControl = new NnMainController();
			}
			this.addController(socketControl);
		}
	}
}