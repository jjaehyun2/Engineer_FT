﻿package away3d.primitives
{
	import away3d.arcane;
    import away3d.core.base.*;
    
	use namespace arcane;
	
    /**
    * Creates a 3d wire torus primitive.
    */ 
    public class WireTorus extends AbstractPrimitive
    {
        private var grid:Array;
        private var _radius:Number;
        private var _tube:Number;
        private var _segmentsR:int;
        private var _segmentsT:int;
        private var _yUp:Boolean;
        
		/**
		 * @inheritDoc
		 */
    	protected override function buildPrimitive():void
    	{
    		super.buildPrimitive();
    		
            var i:int;
            var j:int;

            grid = new Array(_segmentsR);
            for (i = 0; i < _segmentsR; ++i) {
                grid[i] = new Array(_segmentsT);
                for (j = 0; j < _segmentsT; ++j) {
                    var u:Number = i / _segmentsR * 2 * Math.PI;
                    var v:Number = j / _segmentsT * 2 * Math.PI;
                    
                    if (_yUp)
                    	grid[i][j] = createVertex((_radius + _tube*Math.cos(v))*Math.cos(u), _tube*Math.sin(v), (_radius + _tube*Math.cos(v))*Math.sin(u));
                    else
                    	grid[i][j] = createVertex((_radius + _tube*Math.cos(v))*Math.cos(u), -(_radius + _tube*Math.cos(v))*Math.sin(u), _tube*Math.sin(v));
                }
            }

            for (i = 0; i < _segmentsR; ++i) {
                for (j = 0; j < _segmentsT; ++j) {
                    addSegment(createSegment(grid[i][j], grid[(i+1) % _segmentsR][j]));
                    addSegment(createSegment(grid[i][j], grid[i][(j+1) % _segmentsT]));
                }
            }
    	}
    	
    	/**
    	 * Defines the overall radius of the wire torus. Defaults to 100.
    	 */
    	public function get radius():Number
    	{
    		return _radius;
    	}
    	
    	public function set radius(val:Number):void
    	{
    		if (_radius == val)
    			return;
    		
    		_radius = val;
    		_primitiveDirty = true;
    	}
    	
    	/**
    	 * Defines the tube radius of the wire torus. Defaults to 40.
    	 */
    	public function get tube():Number
    	{
    		return _tube;
    	}
    	
    	public function set tube(val:Number):void
    	{
    		if (_tube == val)
    			return;
    		
    		_tube = val;
    		_primitiveDirty = true;
    	}
    	
    	/**
    	 * Defines the number of radial segments that make up the wire torus. Defaults to 8.
    	 */
    	public function get segmentsR():Number
    	{
    		return _segmentsR;
    	}
    	
    	public function set segmentsR(val:Number):void
    	{
    		if (_segmentsR == val)
    			return;
    		
    		_segmentsR = val;
    		_primitiveDirty = true;
    	}
    	
    	/**
    	 * Defines the number of tubular segments that make up the wire torus. Defaults to 6.
    	 */
    	public function get segmentsT():Number
    	{
    		return _segmentsT;
    	}
    	
    	public function set segmentsT(val:Number):void
    	{
    		if (_segmentsT == val)
    			return;
    		
    		_segmentsT = val;
    		_primitiveDirty = true;
    	}
    	
    	/**
    	 * Defines whether the coordinates of the wire torus points use a yUp orientation (true) or a zUp orientation (false). Defaults to true.
    	 */
    	public function get yUp():Boolean
    	{
    		return _yUp;
    	}
    	
    	public function set yUp(val:Boolean):void
    	{
    		if (_yUp == val)
    			return;
    		
    		_yUp = val;
    		_primitiveDirty = true;
    	}
		
		/**
		 * Creates a new <code>WireTorus</code> object.
		 *
		 * @param	init			[optional]	An initialisation object for specifying default instance properties.
		 */
        public function WireTorus(init:Object = null)
        {
            super(init);

            _radius = ini.getNumber("radius", 100, {min:0});
            _tube = ini.getNumber("tube", 40, {min:0, max:radius});
            _segmentsR = ini.getInt("segmentsR", 8, {min:3});
            _segmentsT = ini.getInt("segmentsT", 6, {min:3});
			_yUp = ini.getBoolean("yUp", true);
			
			type = "WireTorus";
        	url = "primitive";
        }
        
		/**
		 * Returns the vertex object specified by the grid position of the mesh.
		 * 
		 * @param	r	The radial position on the primitive mesh.
		 * @param	t	The tubular position on the primitive mesh.
		 */
        public function vertex(r:int, t:int):Vertex
        {
        	if (_primitiveDirty)
    			updatePrimitive();
    		
            return grid[t][r];
        }
    }
}