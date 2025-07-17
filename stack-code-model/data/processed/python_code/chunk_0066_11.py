package de.domigotchi.ui.layout 
{
	import flash.geom.Rectangle;
	/**
	 * ...
	 * @author Dominik Saur
	 */
	public class GridLayout extends AbstractContainerLayout 
	{
		private var _autoSize:Boolean;
		private var _preferEvenLayout:Boolean;
		
		public function GridLayout(container:ILayoutableContainer, anchor:String = AnchorTypes.LEFT_TOP, isRelativeLayout:Boolean = false, autoSize:Boolean = true, preferEvenLayout:Boolean = true) 
		{
			super(container, anchor, isRelativeLayout);
			_preferEvenLayout = preferEvenLayout;
			_autoSize = autoSize;
			
		}
		
		override protected function updateChildren():void 
		{
			var numRows:int;
			var numCols:int;
			var numChildren:uint = _container.numChildren;
			if (numChildren > 0)
			{
				var child:ILayoutable = _container.getLayoutChildAt(0);
				var childWidth:int = child.width;
				var childHeight:int = child.height;
				
				var layoutWidth:int = _boundaries ? _boundaries.width : _container.width;
				var layoutHeight:int = _boundaries ? _boundaries.height : _container.height; 
				
				if (_autoSize)
				{
					var aspectRatio:Number = 0;
					
					aspectRatio = layoutWidth /layoutHeight;
					
					var childQuantity:Number = Math.sqrt(numChildren);
					if (_preferEvenLayout && childQuantity % int(childQuantity) == 0)
					{
						numRows = numCols = childQuantity;
					}
					else
					{
						numRows = numChildren / aspectRatio;	
						numCols = Math.ceil(Math.min(numChildren / numRows, numChildren));
						
						numRows = Math.min(numChildren, Math.ceil(numChildren / numCols));
					}
					
					childWidth = layoutWidth / numCols;
					childHeight = layoutHeight / numRows;

				}
				else
				{
					numCols = layoutWidth / childWidth;
					numRows = layoutHeight / childHeight;
				}
				
				
				
				var currentX:int;
				var currentY:int;
				var currentWidth:int = layoutWidth/numCols;
				var currentHeight:int = layoutHeight/numRows;
				
				var index:int = 0;
				var breakReached:Boolean = false;
				for (var i:int; i < numRows; i++)
				{
					currentY = i * currentHeight;
					for (var j:int = 0; j < numCols; j++)
					{
						currentX = j * currentWidth;
						if (index < numChildren)
						{
							child = _container.getLayoutChildAt(index);
							if (child)
							{
								if (_autoSize)
								{
									//child.width = childWidth;
									//child.height = childHeight;
								}
								
								if (child.layout)
								{
									if(!child.layout.boundaries)
										child.layout.boundaries = new Rectangle(currentX, currentY, currentWidth, currentHeight);
									else
										child.layout.boundaries.setTo(currentX, currentY, currentWidth, currentHeight);
									
									child.layout.doLayout();
								}
								else
								{
									child.x = currentX;
									child.y = currentY;
									child.width = currentWidth;
									child.height = currentHeight;
								}
							}
							index ++;
						}
						else
						{
							breakReached = true;
							break;
						}
					}
					if (breakReached)
						break;
				}
				
				
			}
		}
		
	}

}