package com.arxterra.layouts
{
	import mx.core.ILayoutElement;
	
	import spark.components.supportClasses.GroupBase;
	import spark.layouts.supportClasses.LayoutBase;
	
	// import org.osmf.layout.HorizontalAlign;
	import org.osmf.layout.VerticalAlign;
	
	public class FlowLayoutH extends LayoutBase
	{
		// PUBLIC PROPERTIES AND GET/SET METHOD GROUPS
		
		/*
		private var _sAlignH:String = HorizontalAlign.LEFT;
		[Inspectable (defaultValue="left", enumeration="center,left,right")]
		public function get horizontalAlign():String
		{
			return _sAlignH;
		}
		public function set horizontalAlign(value:String):void
		{
			_sAlignH = value;
			_LayoutInvalidate ( );
		}
		*/
		
		private var _nGapH:Number = 4;
		public function get horizontalGap():Number
		{
			return _nGapH;
		}
		public function set horizontalGap(value:Number):void
		{
			_nGapH = value;
			_LayoutInvalidate ( );
		}
		
		private var _nPadB:Number = 0;
		public function get paddingBottom():Number
		{
			return _nPadB;
		}
		public function set paddingBottom(value:Number):void
		{
			_nPadB = value;
			_LayoutInvalidate ( );
		}
		
		private var _nPadL:Number = 0;
		public function get paddingLeft():Number
		{
			return _nPadL;
		}
		public function set paddingLeft(value:Number):void
		{
			_nPadL = value;
			_LayoutInvalidate ( );
		}
		
		private var _nPadR:Number = 0;
		public function get paddingRight():Number
		{
			return _nPadR;
		}
		public function set paddingRight(value:Number):void
		{
			_nPadR = value;
			_LayoutInvalidate ( );
		}
		
		private var _nPadT:Number = 0;
		public function get paddingTop():Number
		{
			return _nPadT;
		}
		public function set paddingTop(value:Number):void
		{
			_nPadT = value;
			_LayoutInvalidate ( );
		}
		
		private var _sAlignV:String = VerticalAlign.TOP;
		[Inspectable (defaultValue="top", enumeration="bottom,middle,top")]
		public function get verticalAlign():String
		{
			return _sAlignV;
		}
		public function set verticalAlign(value:String):void
		{
			_sAlignV = value;
			_LayoutInvalidate ( );
		}
		
		private var _nGapV:Number = 4;
		public function get verticalGap():Number
		{
			return _nGapV;
		}
		public function set verticalGap(value:Number):void
		{
			_nGapV = value;
			_LayoutInvalidate ( );
		}
		
		
		// PUBLIC METHODS
		
		override public function measure():void
		{
			var nWdTotal:Number = 0;
			var nHtTotal:Number = 0;
			var nX:Number = _nPadL;
			var nY:Number = _nPadT;
			var nWdMax:Number = 0;
			var nHtMax:Number = 0;
			var nHtRow:Number = 0;

			// loop through the elements
			var gbTarget:GroupBase = target;
			var nWdPref:Number = gbTarget.getPreferredBoundsWidth ( );
			var iLim:int = gbTarget.numElements;
			var iCounted:int = 0;
			var i:int;
			var i_elem:ILayoutElement;
			var i_nWdElem:Number;
			var i_nHtElem:Number;
			
			_iRowCount = 0;
			_vRowHts = new <Number> [];
			var uRowHtsLen:uint = 0;
			
			if ( isNaN ( nWdPref ) || nWdPref < 1 )
			{
				for (i = 0; i < iLim; i++)
				{
					// Get the current element
					i_elem = gbTarget.getElementAt(i);
					
					if ( !i_elem || !i_elem.includeInLayout )
					{
						continue;
					}
					iCounted++;
					
					// Find the preferred sizes    
					i_nWdElem = i_elem.getPreferredBoundsWidth();
					i_nHtElem = i_elem.getPreferredBoundsHeight();
					
					nWdTotal += i_nWdElem;
					nHtTotal = Math.max(nHtTotal, i_nHtElem);
				}
				if (iCounted > 0)
				{
					nWdTotal += (iCounted - 1) * _nGapH;
				}
				
				_vRowHts [ 0 ] = nHtTotal;
				_iRowCount = 1;
				
				nWdTotal += _nPadL + _nPadR;
				nHtTotal += _nPadT + _nPadB;
				
				gbTarget.measuredWidth = nWdTotal;
				gbTarget.measuredHeight = nHtTotal;
				
				// Since we really can't fit the content in space any
				// smaller than this, set the measured minimum size
				// to be the same as the measured size.
				// If the container is clipping and scrolling, it will
				// ignore these limits and will still be able to 
				// shrink below them.
				gbTarget.measuredMinWidth = nWdTotal;
				gbTarget.measuredMinHeight = nHtTotal; 
			}
			else
			{
				nWdPref -= _nPadR;
				for (i = 0; i < iLim; i++)
				{
					// Get the current element
					i_elem = gbTarget.getElementAt(i);
					
					if ( !i_elem || !i_elem.includeInLayout )
					{
						continue;
					}
					
					// Find the preferred sizes    
					i_nWdElem = i_elem.getPreferredBoundsWidth();
					i_nHtElem = i_elem.getPreferredBoundsHeight();
					
					// Would the element fit on this line, or should we move
					// to the next line?
					if ( nX + i_nWdElem > nWdPref )
					{
						// Store row info for use during updateDisplayList
						_vRowHts [ uRowHtsLen++ ] = nHtRow;
						
						// Start from the left side
						nX = _nPadL;
						
						// Move down by row height
						nY += nHtRow + _nGapV;
						
						// Reset row height
						nHtRow = 0;
					}
					
					// Update row height
					nHtRow = Math.max ( nHtRow, i_nHtElem );
					
					// Find maximum element extents. This is needed for
					// the scrolling support.
					nWdMax = Math.max(nWdMax, nX + i_nWdElem);
					nHtMax = Math.max(nHtMax, nY + nHtRow);
					
					// Update the current position, add the gap
					nX += i_nWdElem + _nGapH;
				}
				
				// Store last row info and count
				_vRowHts [ uRowHtsLen++ ] = nHtRow;
				_iRowCount = uRowHtsLen;
				
				nWdMax += _nPadR;
				nHtMax += _nPadB;
				
				gbTarget.measuredWidth = nWdMax;
				gbTarget.measuredHeight = nHtMax;
				
				gbTarget.measuredMinWidth = nWdMax;
				gbTarget.measuredMinHeight = nHtMax;
			}
		}
		
		override public function updateDisplayList ( containerWidth:Number, containerHeight:Number ) : void
		{
			// The position for the current element
			var nX:Number = _nPadL;
			var nY:Number = _nPadT;
			var nWdMax:Number = 0;
			var nHtMax:Number = 0;
			var nHtRow:Number = _vRowHts [ 0 ];
			var nWdWrap:Number = containerWidth - _nPadR;
			
			// loop through the elements
			var gbTarget:GroupBase = target;
			var iLim:int = gbTarget.numElements;
			var iRowIdx:int = 0;
			var i:int;
			var i_elem:ILayoutElement;
			var i_nWdElem:Number;
			var i_nHtElem:Number;
			
			var fOffsetY:Function;
			if ( _sAlignV == VerticalAlign.MIDDLE )
			{
				fOffsetY = function ( htElem:Number, htRow:Number ) : Number
				{
					return Math.floor ( ( htRow - htElem ) / 2 );
				};
			}
			else if ( _sAlignV == VerticalAlign.BOTTOM )
			{
				fOffsetY = function ( htElem:Number, htRow:Number ) : Number
				{
					return Math.floor ( htRow - htElem );
				};
			}
			else
			{
				// default to TOP
				fOffsetY = function ( htElem:Number, htRow:Number ) : Number
				{
					return 0;
				};
			}
			
			for ( i = 0; i < iLim; i++)
			{
				// Get the current element
				i_elem = gbTarget.getElementAt(i);
				
				if ( !i_elem || !i_elem.includeInLayout )
				{
					continue;
				}
				
				// Resize the element to its preferred size by passing
				// NaN for the width and height constraints
				i_elem.setLayoutBoundsSize(NaN, NaN);
				
				// Find out the element's dimensions sizes.
				// We do this after the element has been already resized
				// to its preferred size.
				i_nWdElem = i_elem.getLayoutBoundsWidth();
				i_nHtElem = i_elem.getLayoutBoundsHeight();
				
				// Would the element fit on this line, or should we move
				// to the next line?
				if ( nX + i_nWdElem > nWdWrap )
				{
					// Start from the left side
					nX = _nPadL;
					
					// Move down by row height
					nY += nHtRow + _nGapV;
					
					// Reset row height
					iRowIdx++;
					if ( iRowIdx < _iRowCount )
					{
						nHtRow = _vRowHts [ iRowIdx ];
					}
					else
					{
						nHtRow = 0;
					}
				}
				
				// Update row height
				nHtRow = Math.max ( nHtRow, i_nHtElem );
				
				// Position the element
				i_elem.setLayoutBoundsPosition(nX, nY + fOffsetY ( i_nHtElem, nHtRow ) );
				
				// Find maximum element extents. This is needed for
				// the scrolling support.
				nWdMax = Math.max(nWdMax, nX + i_nWdElem);
				nHtMax = Math.max(nHtMax, nY + nHtRow);
				
				// Update the current position, add the gap
				nX += i_nWdElem + _nGapH;
			}
			
			nWdMax += _nPadR;
			nHtMax += _nPadB;
			
			// Scrolling support - update the content size
			gbTarget.setContentSize(nWdMax, nHtMax);
		}
		
		
		// PRIVATE PROPERTIES
		
		private var _iRowCount:int = 1;
		private var _vRowHts:Vector.<Number> = new <Number> [ 0 ];
		
		
		// PRIVATE METHODS
		
		private function _LayoutInvalidate ( ) : void
		{
			// invalidate the layout
			var gbTarget:GroupBase = target;
			if ( gbTarget )
			{
				gbTarget.invalidateSize();
				gbTarget.invalidateDisplayList();
			}
		}
	}
}