package flare.vis.operator.layout
{
	import flare.animate.Transitioner;
	import flare.util.Property;
	import flare.vis.data.NodeSprite;
	
	import flash.geom.Rectangle;
	
	/**
	 * Layout that places node in a TreeMap layout that optimizes for low
	 * aspect ratios of visualized tree nodes. TreeMaps are a form of
	 * space-filling layout that represents nodes as boxes on the display, with
	 * children nodes represented as boxes placed within their parent's box.
	 * This layout determines the area of nodes in the tree map by looking up
	 * the <code>sizeField</code> property on leaf nodes. By default, this
	 * property is "size", such that the layout will look for size
	 * values in the <code>DataSprite.size</code> property.
	 * 
	 * <p>
	 * This particular algorithm is taken from Bruls, D.M., C. Huizing, and 
	 * J.J. van Wijk, "Squarified Treemaps" In <i>Data Visualization 2000, 
	 * Proceedings of the Joint Eurographics and IEEE TCVG Sumposium on 
	 * Visualization</i>, 2000, pp. 33-42. Available online at:
	 * <a href="http://www.win.tue.nl/~vanwijk/stm.pdf">
	 * http://www.win.tue.nl/~vanwijk/stm.pdf</a>.
	 * </p>
	 * <p>
	 * For more information on TreeMaps in general, see 
	 * <a href="http://www.cs.umd.edu/hcil/treemap-history/">
	 * http://www.cs.umd.edu/hcil/treemap-history/</a>.
	 * </p>
	 */
	public class TreeMapLayout extends Layout
	{
		private static const AREA:String = "treeMapArea";
		
		private var _kids:Array = new Array();
		private var _row:Array  = new Array();
		private var _r:Rectangle = new Rectangle();
		
		private var _size:Property = Property.$("size");
		
		/** The property from which to access size values for leaf nodes. */
		public function get sizeField():String { return _size.name; }
		public function set sizeField(s:String):void { _size = Property.$(s); }
		
		// --------------------------------------------------------------------
		
		/**
		 * Creates a new TreeMapLayout 
		 * @param sizeField the data property from which to access the size
		 *  value for leaf nodes. The default is the "size" property.
		 */
		public function TreeMapLayout(sizeField:String="size") {
			this.sizeField = sizeField;
		}
		
		/** @inheritDoc */
		protected override function layout():void
		{
	        // setup
	        var root:NodeSprite = layoutRoot as NodeSprite;
	        var b:Rectangle = layoutBounds;
	        _r.x=b.x; _r.y=b.y; _r.width=b.width-1; _r.height=b.height-1;
	        
	        // process size values
	        computeAreas(root);
	        
	        // layout root node
	        var o:Object = _t.$(root);
	        o.x = 0;//_r.x + _r.width/2;
	        o.y = 0;//_r.y + _r.height/2;
	        o.u = _r.x;
	        o.v = _r.y;
	        o.w = _r.width;
	        o.h = _r.height;
	
	        // layout the tree
	        updateArea(root, _r);
	        doLayout(root, _r);
		}
		
	    /**
    	 * Compute the pixel areas of nodes based on their size values.
	     */
	    private function computeAreas(root:NodeSprite):void
	    {
	        // reset all sizes to zero
	        root.visitTreeDepthFirst(function(n:NodeSprite):void {
	        	n.props[AREA] = 0;
	        });
        
	        // set raw sizes
	        root.visitTreeDepthFirst(function(n:NodeSprite):void {
	        	if (n.childDegree == 0) {
	        		var sz:Number = _size.getValue(_t.$(n));
              // Guard against possible negative values for area calculations.
              if (sz < 0)
                sz = 0;
	        		n.props[AREA] = sz;
	        		var p:NodeSprite = n.parentNode;
	        		for (; p != null; p=p.parentNode)
	        			p.props[AREA] += sz;
	        	}
	        });
        
	        // scale sizes by display area factor
	        var b:Rectangle = layoutBounds;
	        var area:Number = (b.width-1)*(b.height-1);
	        const rootArea:Number = root.props[AREA];
          if (!isNaN(rootArea) && rootArea !== 0) {
            const scale:Number = area / rootArea;
   	        root.visitTreeDepthFirst(function(n:NodeSprite):void {
   	        	n.props[AREA] *= scale;
   	        });
          }
	    }
	    
	    /**
	     * Compute the tree map layout.
	     */
	    private function doLayout(p:NodeSprite, r:Rectangle):void
	    {
	        // create sorted list of children's properties
	        for (var i:uint = 0; i < p.childDegree; ++i) {
	        	_kids.push(p.getChildNode(i).props);
	        }
	        _kids.sortOn(AREA, Array.NUMERIC);
	        // update array to point to sprites, not props
	        for (i = 0; i < _kids.length; ++i) {
	        	_kids[i] = _kids[i].self;
	        }
	        
	        // do squarified layout of siblings
	        var w:Number = Math.min(r.width, r.height);
	        squarify(_kids, _row, w, r); 
	        _kids.splice(0, _kids.length); // clear _kids
	        
	        // recurse
	        for (i=0; i<p.childDegree; ++i) {
	        	var c:NodeSprite = p.getChildNode(i);
	        	if (c.childDegree > 0) {
	        		updateArea(c, r);
	        		doLayout(c, r);
	        	}
	        }
	    }
	    
	    private function updateArea(n:NodeSprite, r:Rectangle):void
	    {
	    	var o:Object = _t.$(n);
			r.x = o.u;
			r.y = o.v;
			r.width = o.w;
			r.height = o.h;
			return;
			
			/*
	        Rectangle2D b = n.getBounds();
	        if ( m_frame == 0.0 ) {
	            // if no framing, simply update bounding rectangle
	            r.setRect(b);
	            return;
	        }
	        
	        // compute area loss due to frame
	        double dA = 2*m_frame*(b.getWidth()+b.getHeight()-2*m_frame);
	        double A = n.getDouble(AREA) - dA;
	        
	        // compute renormalization factor
	        double s = 0;
	        Iterator childIter = n.children();
	        while ( childIter.hasNext() )
	            s += ((NodeItem)childIter.next()).getDouble(AREA);
	        double t = A/s;
	        
	        // re-normalize children areas
	        childIter = n.children();
	        while ( childIter.hasNext() ) {
	            NodeItem c = (NodeItem)childIter.next();
	            c.setDouble(AREA, c.getDouble(AREA)*t);
	        }
	        
	        // set bounding rectangle and return
	        r.setRect(b.getX()+m_frame,       b.getY()+m_frame, 
	                  b.getWidth()-2*m_frame, b.getHeight()-2*m_frame);
	        return;
	        */
	    }
	    
	    private function squarify(c:Array, row:Array, w:Number, r:Rectangle):void
	    {
	    	var worst:Number = Number.MAX_VALUE, nworst:Number;
	    	var len:int;
	        
	        while ((len=c.length) > 0) {
	            // add item to the row list, ignore if negative area
	            var item:NodeSprite = c[len-1];
				var a:Number = item.props[AREA];
	            if (a <= 0.0) {
	            	c.pop();
	                continue;
	            }
	            row.push(item);
	            
	            nworst = getWorst(row, w);
	            if (nworst <= worst) {
	            	c.pop();
	                worst = nworst;
	            } else {
	            	row.pop(); // remove the latest addition
	                r = layoutRow(row, w, r); // layout the current row
	                w = Math.min(r.width, r.height); // recompute w
	                row.splice(0, row.length); // clear the row
	                worst = Number.MAX_VALUE;
	            }
	        }
	        if (row.length > 0) {
	            r = layoutRow(row, w, r); // layout the current row
	            row.splice(0, row.length); // clear the row
	        }
	    }
	
	    private function getWorst(rlist:Array, w:Number):Number
	    {
	    	var rmax:Number = Number.MIN_VALUE;
	    	var rmin:Number = Number.MAX_VALUE;
	    	var s:Number = 0;

			for each (var n:NodeSprite in rlist) {
				var r:Number = n.props[AREA];
				rmin = Math.min(rmin, r);
				rmax = Math.max(rmax, r);
				s += r;
			}
	        s = s*s; w = w*w;
	        return Math.max(w*rmax/s, s/(w*rmin));
	    }
	    
	    private function layoutRow(row:Array, ww:Number, r:Rectangle):Rectangle
	    {
	    	var s:Number = 0; // sum of row areas
	        for each (var n:NodeSprite in row) {
	        	s += n.props[AREA];
	        }
			
			var xx:Number = r.x, yy:Number = r.y, d:Number = 0;
			var hh:Number = ww==0 ? 0 : s/ww;
			var horiz:Boolean = (ww == r.width);
	        
	        // set node positions and dimensions
	        for each (n in row) {
	        	var p:NodeSprite = n.parentNode;
	        	var nw:Number = n.props[AREA]/hh;
	        	
	        	var o:Object = _t.$(n);
				if (horiz) {
	        		o.u = xx + d;
	        		o.v = yy;
	        		o.w = nw;
	        		o.h = hh;
	        		//o.x = xx + d + nw/2;
	        		//o.y = yy + hh/2;
	        	} else {
	        		o.u = xx;
	        		o.v = yy + d;
	        		o.w = hh;
	        		o.h = nw;
	        		//o.x = xx + hh/2;
	        		//o.y = yy + d + nw/2;
	        	}
	        	o.x = 0;
	        	o.y = 0;
	        	d += nw;
	        }
	        
	        // update space available in rectangle r
	        if (horiz) {
	        	r.x = xx; r.y = yy+hh; r.height -= hh;
	        } else {
	        	r.x = xx+hh; r.y = yy; r.width -= hh;
	        }
	        return r;
	    }
	}
}