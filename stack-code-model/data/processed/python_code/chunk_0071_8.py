package  
{
	import net.flashpunk.Entity;
	import net.flashpunk.graphics.Text;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class ScoreBox  extends Entity 
	{
		private var _text:Text;
		private var _counter:int = 0;
		private var _isRunning:Boolean = false;
		private var _updateCounter:int = 0;
		public function ScoreBox() 
		{
			_text = new Text("", 540, 0, { align:"right", width:95 } );
			graphic = _text;
			graphic.scrollX = 0;
			graphic.scrollY = 0;
		}
		
		
		public function start():void
		{
			_isRunning = true;
		}
		public function reset():void
		{
			_isRunning = false;
			_counter = 0;
			_text.text = "";// + _counter;
		}
		public function pause():void
		{
			_isRunning = false;
			_text.text = "" + _counter;
		}
		
		public function getScore():int
		{
			return _counter;
		}
		override public function update():void
		{
			if (!_isRunning) return;
			
			_counter++;
			
			//don't update it every frame or it has to regenerate a cache
			_updateCounter++;
			if (_updateCounter < 3)
			{
				return;
			}
			else
			{
				_updateCounter = 0;
			}
			_text.text = "" + _counter;
		}
		
	}

}