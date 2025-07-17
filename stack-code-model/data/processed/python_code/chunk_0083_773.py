package {
	import com.epologee.development.logging.TraceLogger;
	import com.epologee.development.logging.logger;

	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;

	/**
	 * @author Eric-Paul Lecluse (c) epologee.com
	 */
	[SWF(backgroundColor="#000000", frameRate="31", width="640", height="480")]
	public class RobotLegsNavigatorExample extends Sprite {
		private var context : ExampleContext;

		public function RobotLegsNavigatorExample() {
			logger = new TraceLogger();
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;

			context = new ExampleContext(this);
		}
	}
}