package feathers.controls
{
	import com.grantech.utils.Utils;

	import feathers.events.FeathersEventType;
	import feathers.layout.AnchorLayout;
	import feathers.layout.AnchorLayoutData;
	import feathers.layout.HorizontalLayout;
	import feathers.layout.HorizontalLayoutData;
	import feathers.layout.VerticalAlign;

	import starling.display.DisplayObject;
	import starling.display.Quad;
	import starling.events.Event;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.extensions.ColorArgb;

	public class ColorPicker extends LayoutGroup
	{
		private var inputDisplay:TextInput;
		private var buttonDisplay:Button;

		public static const INVALIDATION_FLAG_COLOR_PICKER_ELEMENT_FACTORY:String = "colorPickerElementFactory";

		protected var spectrumDisplay:ColorSpectrum;

		protected static function defaultSpctrumFactory():ColorSpectrum
		{
			return new ColorSpectrum();
		}
		
		private var _spectrumFactory:Function;
		public function get colorPickerElementFactory():Function
		{
			return this._spectrumFactory;
		}
		public function set colorPickerElementFactory(value:Function):void
		{
			if( this._spectrumFactory == value )
				return;

			this._spectrumFactory = value;
			this.invalidate(INVALIDATION_FLAG_COLOR_PICKER_ELEMENT_FACTORY);
		}
		
		private var _data:ColorArgb;
		public function get data():ColorArgb
		{
			return this._data;
		}
		public function set data(value:ColorArgb):void
		{
			if( value.equal(this.data) )
				return;
			this._data = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		public function ColorPicker() { super(); }
		override protected function initialize():void
		{
			super.initialize();
			var hLayout:HorizontalLayout = new HorizontalLayout();
			hLayout.verticalAlign = VerticalAlign.JUSTIFY;
			hLayout.gap = 4;
			this.layout = hLayout;

			this.buttonDisplay = new Button();
			this.buttonDisplay.width = 29;
			this.buttonDisplay.defaultIcon = new Quad(24, 24);
			this.buttonDisplay.addEventListener(Event.TRIGGERED, this.buttonDisplay_triggeredHandler);
			this.addChild(this.buttonDisplay);
			
			var textLayout:LayoutGroup = new LayoutGroup();
			textLayout.layout = new AnchorLayout();
			textLayout.layoutData = new HorizontalLayoutData(100);
			this.addChild(textLayout);

			this.inputDisplay = new TextInput();
			this.inputDisplay.paddingLeft = 16;
			this.inputDisplay.paddingRight = 6;
			this.inputDisplay.maxChars = 8;
			this.inputDisplay.restrict = "0-9a-fA-F";
			this.inputDisplay.addEventListener(FeathersEventType.ENTER, this.inputDisplay_enterHandler);
			this.inputDisplay.addEventListener(FeathersEventType.FOCUS_OUT, this.inputDisplay_enterHandler);
			this.inputDisplay.layoutData = new AnchorLayoutData(0, 0, 0, 0);
			textLayout.addChild(this.inputDisplay);

			var numSignDIsplay:Label = new Label();
			numSignDIsplay.layoutData = new AnchorLayoutData(NaN, NaN, NaN, 6, NaN, 0);
			numSignDIsplay.touchable = false;
			numSignDIsplay.text = "#"
			textLayout.addChild(numSignDIsplay)
		}

		protected function createSpectrum():void
		{
			if( this.spectrumDisplay !== null )
			{
				this.spectrumDisplay.removeEventListener(Event.CHANGE, this.spectrumDisplay_changeHandler);
				this.spectrumDisplay.dispose();
			}

			var factory:Function = this._spectrumFactory != null ? this._spectrumFactory : defaultSpctrumFactory;
			this.spectrumDisplay = ColorSpectrum(factory());
			this.spectrumDisplay.addEventListener(Event.CHANGE, this.spectrumDisplay_changeHandler);
			this.spectrumDisplay.y = this.buttonDisplay.y + this.buttonDisplay.height;
			this.spectrumDisplay.scaleX = 0.7;
			this.spectrumDisplay.scaleY = 0.7;
			this.spectrumDisplay.visible = false;
			this.stage.addChild(this.spectrumDisplay as DisplayObject);
		}

		protected function spectrumDisplay_changeHandler(e:Event):void
		{
			this.data = this.spectrumDisplay.data;
			this.dispatchEventWith(Event.CHANGE, false, this.data);
		}

		protected function inputDisplay_enterHandler(e:Event):void
		{
			var hexText:String = Utils.normalizeHEX(this.inputDisplay.text);
			this.inputDisplay.text = hexText;
			this.data = Utils.hexToARGB(hexText);
			this.dispatchEventWith(Event.CHANGE, false, this.data);
		}

		protected function buttonDisplay_triggeredHandler(e:Event):void
		{
			this.stage.addEventListener(TouchEvent.TOUCH, this.indicator_touchHandler);
		}

		protected function indicator_touchHandler(e:TouchEvent):void
		{
			var touch:Touch = e.getTouch(this.stage);
			if( touch == null )
				return;
			if( touch.phase == "ended" && touch.target == this.buttonDisplay )
			{
				this.spectrumDisplay.visible = !this.spectrumDisplay.visible;
				this.spectrumDisplay.data = this.data;
				this.spectrumDisplay.x = touch.globalX - 260 * this.spectrumDisplay.scale;
				this.spectrumDisplay.y = touch.globalY + this.buttonDisplay.height;
			}
			if( touch.phase == "ended" )
			{
				if( touch.target != this.buttonDisplay )
				{
					this.spectrumDisplay.visible = false;
					this.stage.removeEventListener(TouchEvent.TOUCH, this.indicator_touchHandler);
					return;
				}
			}	
		}

		override protected function draw():void
		{
			if( this.isInvalid(INVALIDATION_FLAG_COLOR_PICKER_ELEMENT_FACTORY) )
				this.createSpectrum();

			if( this.isInvalid(INVALIDATION_FLAG_DATA) )
			{
				if( this.buttonDisplay != null )
					Quad(this.buttonDisplay.defaultIcon).color = this.data.toArgb();
				if( this.inputDisplay != null )
					this.inputDisplay.text = Utils.colorToHEX(this.data.red, this.data.green, this.data.blue, this.data.alpha);
			}
			super.draw();
		}

		override public function dispose():void
		{
			this.buttonDisplay.removeEventListener(Event.TRIGGERED, this.buttonDisplay_triggeredHandler);
			this.spectrumDisplay.removeEventListener(Event.CHANGE, this.spectrumDisplay_changeHandler);
			this.inputDisplay.removeEventListener(FeathersEventType.ENTER, this.inputDisplay_enterHandler);
			super.dispose();
		}
	}
}