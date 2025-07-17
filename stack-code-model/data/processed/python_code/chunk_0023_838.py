package RiddleStrip 
{
	import flash.events.Event;
	import flash.display.*;
	import flash.events.TimerEvent;
	import flash.geom.*;
	import flash.display.Sprite;
	import mx.events.FlexEvent;
	import spark.components.Group;
	import spark.utils.TextFlowUtil;
	import flash.utils.Timer;
	import mx.controls.Alert;
	import gfw.core.Game;
	import gfw.core.GameObjectManager
	import spark.components.RichText;
	import spark.components.SkinnableContainer;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import gfw.input.Input;
	
	/**
	 * ...
	 * @author jk
	 */
	public class RiddleStripGame extends Game
	{
		static public const WndWidth:int = 1000;
		static public const WndHeight:int = 1000;
		static public const m_physScale:Number = 1;
	
	public function RiddleStripGame(sprite:Group) {
		super(sprite);
			setupWorld();	
			setupDebugDraw();
			SetupHud();
			NewLevel();
			//ShowMainMenu();
	}
	override public function Shutdown():void {
		super.Shutdown();
	}
	override public function NewLevel():void	{	
		super.NewLevel();
		NextLevel();
	}
	public function NextLevel():void {
		if (m_Level == null ) {
			m_Level = new RiddleStripLevel(this);
		} else {
			var currLevel:int = m_Level.GetLevelID();
			m_Level.Shutdown();
			m_Level = new RiddleStripLevel(this);
		}
		m_GameOver = false;
		m_Level.Startup();
		PauseGame(false);
	}	
	override public function IsLevelCompleted():Boolean {
		return m_Level.IsLevelFinished();
	}

	override public function IsGameOver():Boolean {
		if ( m_GameOver) return true;
		if ( IsGameRunning()) {
		//??
		}
		return false;
	}
	override public function MousePress():void {
		if (IsGamePaused() || !IsGameRunning()) return;
		//toogle pause on p
		if ( Input.isKeyReleased(80) ) {
			ShowMainMenu();
			return;
		}
		/*if (Input.isKeyPressed(38)) {
			(m_Level as HanoiLevel).Up(null );
		}
		if (Input.isKeyPressed(40)) {
			(m_Level as HanoiLevel).Down(null );
		}
		if (Input.isKeyPressed(37)) {
			(m_Level as HanoiLevel).Left(null );
		}
		if (Input.isKeyPressed(39)) {
			(m_Level as HanoiLevel).Right(null );
		}*/
	}
	override protected function UpdateGame(e:Event):void {
		MousePress();
		if (!IsGamePaused() ) {
			// Calculate the time since the last frame
			var thisFrame:Date = new Date();
			var _seconds:Number = (thisFrame.getTime() - m_LastFrame.getTime())/1000.0;
			m_LastFrame = thisFrame;
			UpdateMouseWorld();
			MouseDrag();

			m_Level.Tick(_seconds);
			if (IsLevelCompleted()) {
				NextLevel();
			}
			if (IsGameOver()) {
				m_GameOver = true;
			}
		}
		Input.update();
    }
	private function SetupHud():void {
	/*	var hint:RichText = new RichText();
		hint.x = 10;
		hint.y = WndHeight - 100;
		hint.width = WndWidth - 20;
		var text:String = new String("<p>Your goal is to move all red blocks from the left side to the right.</p>" +
			"<p>- you can move only one block at a time</p>" +
			"<p>- you may only drop a smaller block on a bigger block</p>" + 
			"<p>Use the plate at the middle to temporary store one or more blocks. Use the arrow keys to move between the plates and lift and drop a block.</p>");
		hint.textFlow = TextFlowUtil.importFromString(text);
		hint.setStyle("fontSize",14);
		m_Sprite.addElement(hint);*/
	}
	private function setupDebugDraw():void {
	}
	private function setupWorld():void {
		//m_Sprite.setStyle("backgroundColor",  0xAAAAAA);
		m_LoopTimer = new Timer(timeStep*1000, 0);
		m_LoopTimer.addEventListener(TimerEvent.TIMER,Tick);
		m_LoopTimer.start();
		GetView().addEventListener(Event.ENTER_FRAME, RenderGame);
	}
	}

}