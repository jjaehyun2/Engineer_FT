package feathers.controls
{
	import feathers.core.FeathersControl;
	import feathers.core.IFeathersControl;

	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.geom.Point;

	import starling.display.Image;
	import starling.events.Event;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	import starling.extensions.ColorArgb;
	import starling.textures.Texture;

	public class ColorSpectrum extends FeathersControl implements IFeathersControl
	{
		[Embed(source="/media/palette.png")]
		public static var PaletteBitmap:Class;

		private var bitmap:Bitmap;
		private var colorPalette:Image;
		private var bitmapData:BitmapData;

		private var _data:ColorArgb;
		public function get data():ColorArgb
		{
			return _data;
		}
		public function set data(value:ColorArgb):void
		{
			_data = value;
		}

		private var _gap:Number = 1;
		public function get gap():Number
		{
			return _gap;
		}
		public function set gap(value:Number):void
		{
			_gap = value;
		}

		private var _padding:Number;
		public function get padding():Number
		{
			return _padding;
		}
		public function set padding(value:Number):void
		{
			_padding = value;
		}

		public function ColorSpectrum() { super(); }

		override protected function initialize():void
		{
			super.initialize();
			this.bitmap = new PaletteBitmap();
			this.bitmapData = this.bitmap.bitmapData;
			this.colorPalette = new Image(Texture.fromBitmap(bitmap));
			this.colorPalette.addEventListener(TouchEvent.TOUCH, this.palette_touchHandler);
			this.x = this.x;
			this.y = this.y;
			this.addChild(this.colorPalette);

			/* this.alphaSlider = new Slider();
			this.alphaSlider.minimum = 0;
			this.alphaSlider.maximum = 255;
			this.alphaSlider.value = this.a;
			this.alphaSlider.y = colorPalette.height + this.gap;
			this.alphaSlider.width = colorPalette.width - 20;
			this.alphaSlider.maximumTrackFactory = function():Button
			{
				var track:Button = new Button();
				track.height = 20;
				return track;
			};
			this.alphaSlider.minimumTrackFactory = function():Button
			{
				var track:Button = new Button();
				track.height = 20;
				return track;
			};
			this.alphaSlider.thumbFactory = function():Button
			{
				var button:Button = new Button();
				button.height = 20;
				button.width = 20;
				return button;
			};
			this.alphaSlider.addEventListener(Event.CHANGE, alphaSlider_changeHandler);
			
			this.addChild(alphaSlider); */

			/* this.colorIndicator = new Quad(20,20, toArgb());
			this.colorIndicator.x = colorPalette.width - this.colorIndicator.width;
			this.colorIndicator.y = colorPalette.height + this.gap;

			this.addChild(this.colorIndicator); */
		}

		/* protected function alphaSlider_changeHandler(e:Event):void
		{
			this.a = this.alphaSlider.value;
			this.colorIndicator.alpha = this.a/255;
			this.dispatchEventWith(Event.CHANGE, false, {red: this.r, green: this.g, blue: this.b, alpha:this.a });
		} */

		protected function palette_touchHandler(e:TouchEvent):void
		{
			var touches:Vector.<Touch> = e.getTouches(stage);
			var touch:Touch = e.getTouch(stage);
			if (touch)
			{
				var m_TouchEndedPoint:Point = new Point(touch.globalX, touch.globalY);
				if (touch.phase == TouchPhase.BEGAN)
				{
					touch.getLocation(this.colorPalette, m_TouchEndedPoint);
					// this.colorIndicator.color = this.bitmapData.getPixel(m_TouchEndedPoint.x, m_TouchEndedPoint.y);
				}

				if (touch.phase == TouchPhase.MOVED)
				{
					if (stage.hitTest(m_TouchEndedPoint) == touch.target)
					{
						touch.getLocation(this.colorPalette, m_TouchEndedPoint);
						this.changeColor(m_TouchEndedPoint);
						// this.colorIndicator.color = this.bitmapData.getPixel(m_TouchEndedPoint.x, m_TouchEndedPoint.y);
					}
				}

				if (touch.phase == TouchPhase.ENDED)
				{
					if (stage.hitTest(m_TouchEndedPoint) == touch.target)
					{
						touch.getLocation(this.colorPalette, m_TouchEndedPoint);
						this.changeColor(m_TouchEndedPoint);
					}
				}
			}
		}

		private function changeColor(point:Point):void
		{
				var currentColor:uint = this.bitmapData.getPixel(point.x, point.y);
				// this.colorIndicator.color = currentColor;
				var a:Number = this.data.alpha
				this.data = ColorArgb.fromArgb(currentColor);
				this.data.alpha = a;
				this.dispatchEventWith(Event.CHANGE, false, this.data);
		}

		override public function dispose():void
		{
			this.colorPalette.removeEventListener(TouchEvent.TOUCH, this.palette_touchHandler);
			// this.alphaSlider.removeEventListener(Event.CHANGE, alphaSlider_changeHandler);
			super.dispose();
		}
	}
}