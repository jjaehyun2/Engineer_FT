package com.profusiongames.scenery 
{
	import com.profusiongames.containers.Layer;
	import org.flashdevelop.utils.FlashConnect;
	import starling.display.Sprite;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Scenery extends Sprite 
	{
		private var _layer:Layer;
		public function Scenery() 
		{
			
		}
		
		public function get layer():Layer 
		{
			return _layer;
		}
		
		public function set layer(value:Layer):void 
		{
			_layer = value;
			scaleX = scaleY =  layer.scrollScale == 5 ? 0.7 : 1;
		}
		
		public function get yRelativeToScreen():int
		{
			//FlashConnect.atrace(layer, layer.y, layer.scrollScale,layer.y * layer.scrollScale + y);
			if (layer == null) return y;
			return layer.y + y;
		}
		
		public function set yRelativeToScreen(value:int):void
		{
			if (layer == null)
			{
				y = value;
				return;
			}
			y = value - layer.y;
		}
	}

}