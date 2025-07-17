package
{
	import org.apache.royale.events.EventDispatcher;

	/**
	 * @externs
	 */
	COMPILE::JS	
	public class StimulsoftReports extends EventDispatcher
	{
		/** 
         * <inject_script>
		 * var script = document.createElement("script");
		 * script.setAttribute("src", "resources/stimulsoftreports/stimulsoft.js");
		 * document.head.appendChild(script);
		 * </inject_script>
		 */
		public function StimulsoftReports(){}

		public static function setLicenseKey(licenseKey:String):void {}

		public static function setLanguage(language:String):void {}

		public static function setParameters(parameters:Array):void {}

		public function initViewer(renderArea:String, printType:int, showEMail:Boolean, showSave:Boolean):void {}

		public function initDesigner(renderArea:String):void {}

		public function loadReportDefinition(definition:String, showWatermark:Boolean):void {}

		public function loadReportFile(file:String, showWatermark:Boolean):void {}

		public function loadReportData(data:Array, parameters:Array):void {}

		public function designReportDefinition(definition:String):void {}

		public function designReportFile(file:String):void {}
	}
}