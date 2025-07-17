package widgets.SearchEnhanced.supportClasses
{
	
	import com.esri.ags.Graphic;
	import com.esri.ags.geometry.Geometry;
	import com.esri.ags.geometry.MapPoint;
	import com.esri.ags.geometry.Multipoint;
	import com.esri.ags.geometry.Polygon;
	import com.esri.ags.geometry.Polyline;
	import com.esri.ags.symbols.Symbol;
	
	[Bindable]
	public class ResultItem
	{
		public function ResultItem(graphic:Graphic, attributes:ResultAttributes)
		{
			_graphic = graphic;
			_attributes = attributes;
			_center = getGeomCenter(graphic);
		}

		
		/** **************************************************************************
		 * GRAPHIC PROPERTY
		 * ************************************************************************ */
		
		private var _graphic:Graphic;
		
		public function get graphic():Graphic
		{
			return _graphic;
		}
		
		
		
		/** **************************************************************************
		 * ATTRIBUTES PROPERTY
		 * ************************************************************************ */
		
		private var _attributes:ResultAttributes;

		public function get attributes():ResultAttributes
		{
			return _attributes;
		}

		
		
		/** **************************************************************************
		 * CENTER PROPERTY
		 * ************************************************************************ */

		private var _center:MapPoint;
		
		public function get center():MapPoint
		{
			return _center;
		}
		

		
		/** **************************************************************************
		 * GEOMETRY PROPERTY
		 * ************************************************************************ */

		public function get geometry():Geometry
		{
			return _graphic.geometry;
		}
		
		
		
		/** **************************************************************************
		 * SYMBOL PROPERTY
		 * ************************************************************************ */

		public function get symbol():Symbol
		{
			return _graphic.symbol;
		}
	
		
		
		/* CLASS FUNCTIONS
		--------------------------------------------------------------------------------------------------- */
		
		/**
		 * Function to get the geometry centre of the geometry of the result shape.
		 * <p>
		 * <b>Parameters</b><br/>
		 * <ul>
		 * <li><i>graphic [Graphic]: </i>Graphic feature to calculate the geometric centre for.</li>
		 * </ul>
		 * </p>
		 */
		private function getGeomCenter(graphic:Graphic):MapPoint
		{
			var point:MapPoint;
			var geometry:Geometry = graphic.geometry;
			
			if (geometry)
			{
				switch (geometry.type)
				{
					case Geometry.MAPPOINT:
					{
						point = geometry as MapPoint;
						break;
					}
					case Geometry.MULTIPOINT:
					{
						const multipoint:Multipoint = geometry as Multipoint;
						point = multipoint.points && multipoint.points.length > 0 ? multipoint.points[0] as MapPoint : null;
						break;
					}
					case Geometry.POLYLINE:
					{
						var pl:Polyline = geometry as Polyline;
						var pathCount:Number = pl.paths.length;
						var pathIndex:int = int((pathCount / 2) - 1);
						var midPath:Array = pl.paths[pathIndex];
						var ptCount:Number = midPath.length;
						var ptIndex:int = int((ptCount / 2) - 1);
						point = pl.getPoint(pathIndex, ptIndex);
						break;
					}
					case Geometry.POLYGON:
					{
						const poly:Polygon = geometry as Polygon;
						point = poly.extent.center;
						break;
					}
				}
			}
			
			return point;
		}
	}

}