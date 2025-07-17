package 
{
	import com.profusiongames.states.Game;
	import com.profusiongames.util.FontUtil;
	import flash.display.Sprite;
	import flash.events.Event;
	import org.flashdevelop.utils.FlashConnect;
	import starling.core.Starling;

	/**
	 * ...
	 * @author UnknownGuardian
	 */
	[Frame(factoryClass="Preloader")]
	public class Main extends Sprite 
	{
		private var starlingStage:Starling;
		public static var HEIGHT:int = 600;
		public static var WIDTH:int = 500;
		public function Main():void 
		{
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}

		private function init(e:Event = null):void 
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			// entry point
			FontUtil.init();
			
			starlingStage = new Starling(Game, stage, null, null, "auto", "baseline");
			starlingStage.start();
			starlingStage.showStatsAt("left", "bottom");
		}

	}

}