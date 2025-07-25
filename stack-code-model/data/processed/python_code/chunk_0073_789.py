package feathers.examples.layoutExplorer.screens
{
	import feathers.controls.Button;
	import feathers.controls.Header;
	import feathers.controls.PanelScreen;
	import feathers.events.FeathersEventType;
	import feathers.examples.layoutExplorer.data.FlowLayoutSettings;
	import feathers.layout.FlowLayout;
	import feathers.system.DeviceCapabilities;

	import starling.core.Starling;
	import starling.display.DisplayObject;
	import starling.display.Quad;
	import starling.events.Event;

	[Event(name="complete",type="starling.events.Event")]

	[Event(name="showSettings",type="starling.events.Event")]

	public class FlowLayoutScreen extends PanelScreen
	{
		public static const SHOW_SETTINGS:String = "showSettings";

		public function FlowLayoutScreen()
		{
			super();
		}

		public var settings:FlowLayoutSettings;

		override protected function initialize():void
		{
			//never forget to call super.initialize()
			super.initialize();

			this.title = "Flow Layout";

			var layout:FlowLayout = new FlowLayout();
			layout.horizontalGap = this.settings.horizontalGap;
			layout.verticalGap = this.settings.verticalGap;
			layout.paddingTop = this.settings.paddingTop;
			layout.paddingRight = this.settings.paddingRight;
			layout.paddingBottom = this.settings.paddingBottom;
			layout.paddingLeft = this.settings.paddingLeft;
			layout.horizontalAlign = this.settings.horizontalAlign;
			layout.verticalAlign = this.settings.verticalAlign;
			layout.rowVerticalAlign = this.settings.rowVerticalAlign;

			this.layout = layout;
			this.snapScrollPositionsToPixels = true;

			var minQuadSize:Number = Math.min(Starling.current.stage.stageWidth, Starling.current.stage.stageHeight) / 15;
			for(var i:int = 0; i < this.settings.itemCount; i++)
			{
				var size:Number = (minQuadSize + minQuadSize * 2 * Math.random());
				var quad:Quad = new Quad(size, size, 0xff8800);
				this.addChild(quad);
			}

			this.headerFactory = this.customHeaderFactory;

			//this screen doesn't use a back button on tablets because the main
			//app's uses a split layout
			if(!DeviceCapabilities.isTablet(Starling.current.nativeStage))
			{
				this.backButtonHandler = this.onBackButton;
			}

			this.headerFactory = this.customHeaderFactory;

			this.addEventListener(FeathersEventType.TRANSITION_IN_COMPLETE, transitionInCompleteHandler);
		}

		private function customHeaderFactory():Header
		{
			var header:Header = new Header();
			//this screen doesn't use a back button on tablets because the main
			//app's uses a split layout
			if(!DeviceCapabilities.isTablet(Starling.current.nativeStage))
			{
				var backButton:Button = new Button();
				backButton.styleNameList.add(Button.ALTERNATE_STYLE_NAME_BACK_BUTTON);
				backButton.label = "Back";
				backButton.addEventListener(Event.TRIGGERED, backButton_triggeredHandler);
				header.leftItems = new <DisplayObject>
				[
					backButton
				];
			}
			var settingsButton:Button = new Button();
			settingsButton.label = "Settings";
			settingsButton.addEventListener(Event.TRIGGERED, settingsButton_triggeredHandler);
			header.rightItems = new <DisplayObject>
			[
				settingsButton
			];
			return header;
		}

		private function onBackButton():void
		{
			this.dispatchEventWith(Event.COMPLETE);
		}

		private function transitionInCompleteHandler(event:Event):void
		{
			this.revealScrollBars();
		}

		private function backButton_triggeredHandler(event:Event):void
		{
			this.onBackButton();
		}

		private function settingsButton_triggeredHandler(event:Event):void
		{
			this.dispatchEventWith(SHOW_SETTINGS);
		}
	}
}