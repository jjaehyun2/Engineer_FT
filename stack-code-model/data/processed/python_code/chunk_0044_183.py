package framework.components
{
	import flash.display.DisplayObjectContainer;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	import flash.text.TextFormat;
	
	public class Label extends Component
	{
		private var _autoSize:Boolean = true;
		private var _text:String = "";
		private var _tf:TextField;
		
		/**
		 * Constructor
		 * @param parent The parent DisplayObjectContainer on which to add this Label.
		 * @param xpos The x position to place this component.
		 * @param ypos The y position to place this component.
		 * @param text The string to use as the initial text in this component.
		 */
		public function Label(parent:DisplayObjectContainer = null, xpos:Number = 0, ypos:Number =  0, text:String = "")
		{
			_text = text;
			super(parent, xpos, ypos);
		}
		
		/**
		 * Initializes the component.
		 */
		override protected function init():void
		{
			super.init();
			mouseEnabled = false;
			mouseChildren = false;
		}
		
		/**
		 * Creates and adds the child display objects of this component.
		 */
		 
		override protected function addChildren():void
		{
			//_height = 18;
			_tf = new TextField();
			_tf.height = _height;
			//_tf.textColor=0xff00ff;
			//_tf.embedFonts = true;
			//_tf.selectable = false;
			//_tf.mouseEnabled = false;
			//_tf.defaultTextFormat = new TextFormat("PF Ronda Seven", 8, Style.LABEL_TEXT);
			_tf.text = _text;			
			addChild(_tf);
			draw();
		}
		
		
		
		
		///////////////////////////////////
		// public methods
		///////////////////////////////////
		
		/**
		 * Draws the visual ui of the component.
		 */
		override public function draw():void
		{
			super.draw();
			_tf.text = _text;
			if(_autoSize)
			{
				_tf.autoSize = TextFieldAutoSize.LEFT;
				_width = _tf.width;
			}
			else
			{
				_tf.autoSize = TextFieldAutoSize.NONE;
				_tf.width = _width;
			}
			_height = _tf.height = 18;
		}
		
		///////////////////////////////////
		// event handlers
		///////////////////////////////////
		
		///////////////////////////////////
		// getter/setters
		///////////////////////////////////
		
		/**
		 * Gets / sets the text of this Label.
		 */
		public function set text(t:String):void	{
			_text = t;
			invalidate();
		}
		
		public function get text():String {
			return _text;
		}
		
		public function set color(c:Number):void {
			_tf.textColor = c;
		}
		
		public function set font(n:String):void {
			var format:TextFormat = new TextFormat();
 			format.font = n;
 			_tf.defaultTextFormat = format;
		}
		
		public function set size(n:int):void {
			var format:TextFormat = new TextFormat();
 			format.size = n;
 			_tf.defaultTextFormat = format;
		}
		
		/**
		 * Gets / sets whether or not this Label will autosize.
		 */
		public function set autoSize(b:Boolean):void {
			_autoSize = b;
		}
		
		public function get autoSize():Boolean {
			return _autoSize;
		}
	}
}