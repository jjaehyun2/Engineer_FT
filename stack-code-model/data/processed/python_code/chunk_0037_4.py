package gfw.core
{
	/**
	 * ...
	 * @author jk
	 * enthält alle Level-Objekte und -zustände
	 */
	public class Level 
	{
		
	public function Level(Controller:Game) {
		m_Controller = Controller;
	}
	public function GetLevelID():int {
		return 1;
	}
	public function Startup():void {
	}
	public function Shutdown(): void {
		m_Controller = null;
	}
	public function Tick(dt:Number):void {
		GameObjectManager.Instance.enterFrame();
	}
	public function IsLevelFinished():Boolean {
		return false;
	}
	protected var m_Controller:Game = null;
	}

}