package com.vini123
{
	import com.vini123.component.bitmap.ScaleBitmap;
	import com.vini123.component.scrollBar.VScrollBar;
	import com.vini123.component.system.FPSMonitor;
	import com.vini123.implement.IScrollBar;
	
	import flash.display.BitmapData;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.geom.Rectangle;
	
	[SWF(width="550", height="396", frameRate="30")]
	public class Main extends Sprite
	{
		private var _width:Number;
		private var _height:Number;
		
		protected var itemsContainer:Sprite;
		private var vscrollBar:IScrollBar;
		
		private var gril:Girl;
		
		private var fps:FPSMonitor;
		
		public function Main()
		{
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align = StageAlign.TOP_LEFT;
			
			itemsContainer = new Sprite();
			addChild(itemsContainer);
			
			gril = new Girl();
			itemsContainer.addChild(gril);
			
			var  barout:ScaleBitmap = new ScaleBitmap((new BarOut() as BitmapData));
			barout.scale9Grid = new Rectangle(3 , 5 , 3 , 44);
			
			var barover:ScaleBitmap = new ScaleBitmap((new BarOver() as BitmapData));
			barover.scale9Grid = new Rectangle(3 , 5 , 3 , 44);
						
			vscrollBar = new VScrollBar();
			vscrollBar.setMouseWheelTarget(this);
			vscrollBar.getDragBar().setOutSkin(barout);
			vscrollBar.getDragBar().setOverSkin(barover);
			vscrollBar.getDragBar().setDownSkin(barover);
			vscrollBar.updateTargetPositionCallBack = updateTargetPosition;
			addChild(vscrollBar as VScrollBar);
			
			this.width = 550;
			this.height = 396;
			refreshScrollBar();
			
			fps = new FPSMonitor(240, 80);
			fps.visible = true;
			addChild(fps);
		}
		
		protected function get itemsContainerHeight():Number
		{
			return itemsContainer.height;
		}
		
		private function updateTargetPosition(value:Number):void
		{
			var position:Number = value;
			itemsContainer.y = -(itemsContainerHeight - _height) * position;
		}
		
		private  function refreshScrollBar():void
		{
			if (itemsContainerHeight > _height)
			{
				if (!vscrollBar.parent)
				{
					addChild(vscrollBar as VScrollBar);
				}
				vscrollBar.pageSize = itemsContainerHeight;
			}
			else
			{
				if (vscrollBar.parent)
				{
					removeChild(vscrollBar as VScrollBar);
				}
			}
		}
		
		override public function set height(value:Number):void
		{
			_height = value;
			if(vscrollBar)
			{
				vscrollBar.height = value;
			}
		}
		
		override public function set width(value:Number):void
		{
			_width = value;
			if(vscrollBar)
			{
				vscrollBar.x = _width - vscrollBar.width - 3;
			}
		}
	}
}