package fplib.gui 
{
	import net.flashpunk.Entity;
	import net.flashpunk.graphics.Graphiclist;
	import net.flashpunk.graphics.Image;
	import net.flashpunk.graphics.Text;
	import net.flashpunk.utils.Input;
	
	/**
	 * ...
	 * @author Diogo Muller
	 */
	public class Button extends Entity
	{
		protected var _normal : Graphiclist;
		protected var _over : Graphiclist;
		protected var _pressed : Graphiclist;
		
		protected var _callback : Function;
		
		public function Button(normalAsset:Class, overAsset:Class, pressedAsset:Class, text : String, x:Number, y:Number, width:int, height:int, callback:Function) 
		{
			super(x, y);
			
			_callback = callback;
			
			var normal : Image = new Image(normalAsset);
			var over : Image = new Image(overAsset);
			var pressed : Image = new Image(pressedAsset);
			
			var txt : Text = new Text(text);
			txt.y = 8;
			txt.width = width;
			txt.height = height;
			txt.align = "center";
            _normal = new Graphiclist(normal, txt);
			_over = new Graphiclist(over, txt);
			_pressed = new Graphiclist(pressed, txt);
			
			_normal.scrollX = _normal.scrollY = 0;
			
			graphic = _normal;
			setHitbox(width, height);
		}
		
		override public function update():void 
		{
			super.update();
			
			// se o mouse está cima, pode ser click ou over
			if ( collidePoint(x - world.camera.x, y -world.camera.y, Input.mouseX, Input.mouseY))
			{
				if (Input.mouseDown)
				{
					// apertou o mouse
					graphic = _pressed;
				}
				else if (Input.mouseReleased)
				{
					// clicou!
					if (_callback != null)
						_callback();
				}
				else
				{
					// mouse em cima
					graphic = _over;
				}
			}
			else
			{
				// normal
				graphic = _normal;
			}
		}
	}

}