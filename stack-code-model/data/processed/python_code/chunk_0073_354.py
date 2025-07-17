package de.domigotchi.ui.layout 
{
	import flash.display3D.IndexBuffer3D;
	import flash.geom.Rectangle;
	/**
	 * ...
	 * @author Dominik Saur
	 */
	public class VerticalLayout extends AbstractContainerLayout 
	{
		private var _useAutoSize:Boolean = true;
		
		public function VerticalLayout(target:ILayoutableContainer, anchor:String = AnchorTypes.LEFT_TOP, useAutoSize:Boolean = true, isRelativeLayout:Boolean = false)
		{
			_useAutoSize = useAutoSize;
			super(target, anchor, isRelativeLayout);
		}
		
		
		protected override function updateChildren():void 
		{	
			var numChildren:uint = _container.numChildren;
			var child:ILayoutable;
			var heightSpace:uint;
			var currentY:uint;
			var currentHeight:uint;
			var completeHeight:uint = boundaries ? boundaries.height : _container.height;
			
			if(_useAutoSize)
				heightSpace = target.height / numChildren;
			var childHeight:uint;
			
			
			for (var i:int; i < numChildren; i++)
			{
				child = _container.getLayoutChildAt(i);
				
				if (child)
				{
					if (heightSpace != 0)
					{
						currentHeight = heightSpace;
					}
					else
					{
						var remainingHeight:Number = (completeHeight - currentY);
						if (numChildren - 1 == i)
							currentHeight = remainingHeight;
						else
							currentHeight = remainingHeight > child.height ? child.height : remainingHeight;
					}
					
					if (child.layout)
					{
						var tmpBoundaries:Rectangle = child.layout.boundaries;
						if (!tmpBoundaries) 
						{
							child.layout.boundaries = tmpBoundaries = new Rectangle();
						}
						tmpBoundaries.setTo(0, currentY, _container.width, currentHeight);
						child.layout.doLayout();
					}
					else
					{
						child.x = 0;
						child.y = currentY;
						child.width = _container.width;
						child.height = currentHeight;
					}
					
					currentY += currentHeight; 
				}
			}

		}
		
		public function get useAutoSize():Boolean 
		{
			return _useAutoSize;
		}
		
		public function set useAutoSize(value:Boolean):void 
		{
			_useAutoSize = value;
		}

		
	}

}