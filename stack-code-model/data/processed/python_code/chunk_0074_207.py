package  
{
	import com.greensock.TweenLite;
	import flash.display.BitmapData;
	import net.flashpunk.Entity;
	import net.flashpunk.graphics.Image;
	import net.flashpunk.graphics.Text;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class MessageBox extends Entity 
	{
		private var _text:Text;
		private var _lastMessage:int = 0;
		private var _messageTimeout:int = 240;
		private var bg:Image;
		public function MessageBox() 
		{
			bg = new Image(new BitmapData(640, 20, true, 0xBB000000));
			graphic = bg;
			//_text = new Text("", 0, 450, { align:"center", width:640 } );
			_text = new Text("", 0, 0, { align:"center", width:640 } );
			//graphic = _text;
			addGraphic(_text);
			graphic.scrollX = 0;
			graphic.scrollY = 0;
		}
		
		public function showMessage(t:String, timeout:int = 240 ):void
		{
			if (_text.text != t)
			{
				_text.text = t;
				_messageTimeout = timeout;
			}
			_lastMessage = 0;
			TweenLite.to(this, 0.5, { y:0, overwrite:true } );
		}
		
		override public function update():void
		{
			_lastMessage++;
			if (_lastMessage == _messageTimeout)
			{
				_text.text = "";
				TweenLite.to(this, 0.5, { y:-20, overwrite:true } );
			}
		}
		
	}

}