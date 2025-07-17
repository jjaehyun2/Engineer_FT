package
{
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.text.TextField;

	import fin.desktop.ApplicationOptions;
	import fin.desktop.CaptureOptions;
	import fin.desktop.CapturingWindow;
	import fin.desktop.ExternalWindow;
	import fin.desktop.Window;
	import fin.desktop.RuntimeConfiguration;
	import fin.desktop.RuntimeLauncher;
	import fin.desktop.InterApplicationBus;
	import fin.desktop.WindowOptions;
	
	/**
	 * ...
	 * @author Wenjun
	 */
	public class Main extends Sprite 
	{
		protected var runtimeLauncher:RuntimeLauncher;
		private var textField:TextField;
		
		public function Main() 
		{
			textField = new TextField();
			textField.width = 200;
			textField.height = 100;
			textField.multiline = true;
			textField.text = "Starting OpenFin Runtime...\n";
			addChild(textField);
			
			var cfg:RuntimeConfiguration = new RuntimeConfiguration("Air Test App");
			cfg.appManifestUrl = "https://demoappdirectory.openf.in/desktop/config/apps/OpenFin/HelloOpenFin/app.json";
			cfg.onConnectionReady = onConnectionReady;
			cfg.onConnectionError = onConnectionError;
			cfg.onConnectionClose = onConnectionClose;
			cfg.connectionTimeout = 15000;

			runtimeLauncher = new RuntimeLauncher(cfg);
		}
		

		public function onConnectionReady():void {
			textField.appendText("Connection Successful! \n");
			InterApplicationBus.getInstance().publish("AirTopic", {value: "From Air Main Window"});
			fin.desktop.System.getInstance().getVersion(function (v:String): void {
				textField.appendText("Connected to Runtime " + v + "\n");
			});

			// Testing window capturing
            var captureOptions:CaptureOptions = new CaptureOptions();
            captureOptions.borderTop = captureOptions.borderRight = captureOptions.borderBottom = captureOptions.borderLeft = 30;
            var cw:CapturingWindow = new CapturingWindow(stage.nativeWindow);
            var appOpts:ApplicationOptions = new ApplicationOptions("Air Parent 1", "https://demoappdirectory.openf.in/desktop/config/apps/OpenFin/AirDemo/airChrome.html");
            var winOpts:WindowOptions = new WindowOptions();
            winOpts.autoShow = true;
            winOpts.defaultTop = 100;
            winOpts.defaultLeft = 100;
            winOpts.defaultHeight = winOpts.defaultWidth = 500;
            winOpts.frame = false;
            winOpts.contextMenu = true;
            winOpts.saveWindowState = false;
            appOpts.mainWindowOptions = winOpts;
            captureOptions.applicationOptions = appOpts;
            cw.capture(captureOptions, captureCallback);
		}

        public function captureCallback(event:*): void {
			textField.appendText("Capture worked \n");			
		}

		public function onConnectionError(reason:String = null):void {
			textField.appendText("Connection failed " + reason + "\n");
		}

		public function onConnectionClose(reason:String = null):void {
			textField.appendText("Connection close " + reason + "\n");
		}

		public function onExit(event:Event):void {
			textField.appendText("Exiting \n");
		}
		
	
	}
	
}