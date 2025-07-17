package com.profusiongames.containers 
{
	import com.profusiongames.scenery.Scenery;
	import org.flashdevelop.utils.FlashConnect;
	import starling.display.DisplayObject;
	import starling.display.Image;
	import starling.display.Quad;
	import starling.display.Sprite;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class ScrollingContainer extends Sprite 
	{
		private var _sceneryLayerBack:Layer = new Layer(5);
		private var _sceneryLayerFront:Layer = new Layer(3);
		private var _activeLayer:Layer = new Layer();
		
		private var minClip:Quad = new Quad(500, 5, 0xFF00FF);
		private var maxClip:Quad = new Quad(500, 3, 0x00FF00);
		private var midClip:Quad = new Quad(300, 2, 0xFF0000);
		
		public function ScrollingContainer() 
		{
			//addChild(new Quad(100, 100, 0xFF00FF));
			addChild(_sceneryLayerBack);
			addChild(_sceneryLayerFront);
			addChild(_activeLayer);
			/*addChild(minClip);
			addChild(maxClip);
			addChild(midClip);
			
			/scaleY = 0.2;
			scaleX = 0.2;
			y = 400;*/
			

				
		}
		
		public function reset():void
		{
			_sceneryLayerBack.y = _sceneryLayerFront.y = _activeLayer.y = 0;
			_sceneryLayerBack.removeChildren();
			_sceneryLayerFront.removeChildren();
			_activeLayer.removeChildren(10);
		}
		
		public function setMinMax(min:int, max:int):void
		{
			minClip.y = min;
			maxClip.y = max;
		}
		public function setMid(m:int):void
		{
			midClip.y = m;
		}
		
		public function addActive(s:Sprite):void
		{
			_activeLayer.addChild(s);
		}
		
		public function removeActive(s:Sprite):DisplayObject
		{
			return _activeLayer.removeChild(s);
		}
		
		public function addScenery(s:Scenery, layer:String = "random"):void
		{
			if (layer == "random")
			{
				if (Math.random() > 0.5) _sceneryLayerBack.addChild(s);
				else _sceneryLayerFront.addChild(s);
			}
			else if (layer == "front")
				_sceneryLayerFront.addChild(s);
			else if (layer == "back")
				_sceneryLayerBack.addChild(s);
				
			s.layer = s.parent as Layer;
		}
		
		public function removeScenery(s:Scenery):DisplayObject
		{
			return s.parent.removeChild(s);
		}
		
		public function centerOn(s:Sprite):void
		{
			_activeLayer.x = -s.x + 500 / 2;
			_activeLayer.y = -s.y + 600 / 2;
			handleSceneryLayers();
		}
		
		public function centerVerticallyOn(s:Sprite):void
		{
			var newY:int =  -s.y + 600 / 2;
			if (newY > _activeLayer.y)
			{
				_activeLayer.y = newY;
				handleSceneryLayers();
			}
		}
		
		public function centerVerticallyOnUsingMax(s:Sprite):void
		{
			var newY:int =  -s.y + 600 / 2;
			if (newY > _activeLayer.y)
			{
				_activeLayer.y = newY;
				handleSceneryLayers();
			}
		}
		
		public function handleSceneryLayers():void
		{
			_sceneryLayerBack.y = int(_activeLayer.y) / _sceneryLayerBack.scrollScale;
			_sceneryLayerFront.y = int(_activeLayer.y) / _sceneryLayerFront.scrollScale;
		}
		
		public function getScreenAltitude():int
		{
			return _activeLayer.y;
		}
	}

}