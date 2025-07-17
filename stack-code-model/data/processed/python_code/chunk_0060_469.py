package widgets.supportClasses.utils
{
	import com.esri.ags.Graphic;
	import com.esri.ags.SpatialReference;
	import com.esri.ags.geometry.Extent;
	import com.esri.ags.geometry.MapPoint;
	import com.esri.ags.geometry.Polyline;
	import com.esri.ags.symbols.SimpleLineSymbol;
	import com.esri.ags.symbols.SimpleMarkerSymbol;
	import com.esri.ags.symbols.Symbol;
	
	import flash.utils.ByteArray;
	
	public class GPXUtil
	{
		private static const EPSG_GEOGRAPHIC:Number = 4326;
		private static const DOUBLEQUOTES:String = String.fromCharCode(34);
		
		
		/**
		 * Converts the contents of a GPS file into an object with point and track graphics.
		 */
		public static function GenerateGraphics(data:ByteArray, fileSize:Number):Object
		{
			// Create arrays to store results
			var resultpoints:Array = [];
			var resultlines:Array = [];
			var resultpolys:Array = [];
			
			// Determine the name space to utilise for the type of GPX file
			var gpxString:String = data.readUTFBytes(fileSize);
			var namespaces:Array = [];
			
			var f:Number = gpxString.indexOf("xmlns=");
			var ff:Number = gpxString.indexOf(DOUBLEQUOTES,f+7) - (f +7);
			
			while (f != -1)
			{
				namespaces.push(gpxString.substr(f+7,ff));
				f = gpxString.indexOf("xmlns=", f+1);
				ff = gpxString.indexOf(DOUBLEQUOTES,f+7) - (f+7);
			}
			
			// Check for valid namespaces
			if (namespaces.length >= 1)
			{
				// Set the default namespace for loading the xml file. 
				var matched:Boolean = false;
				for (var n:int = 0; n < namespaces.length; n++)
				{
					if (matched == false) 
					{
						switch(String(namespaces[n]))
						{
							case "http://www.topografix.com/GPX/1/1":
							{
								namespace gpx11 = "http://www.topografix.com/GPX/1/1";
								default xml namespace = gpx11; 
								matched = true;
								break;
							}
								
							case "http://www.topografix.com/GPX/1/0":
							{
								namespace gpx10 = "http://www.topografix.com/GPX/1/0";
								default xml namespace = gpx10; 
								matched = true;
								break;
							}
								
							default:
							{
								// do nothing
								return null;
							}
						}					
					}
					else {
						break;
					}
				}
				
				/*
				switch(String(namespaces[0]))
				{
					case "http://www.topografix.com/GPX/1/1":
					{
						namespace gpx11 = "http://www.topografix.com/GPX/1/1";
						default xml namespace = gpx11; 
						break;
					}
					
					case "http://www.topografix.com/GPX/1/0":
					{
						namespace gpx10 = "http://www.topografix.com/GPX/1/0";
						default xml namespace = gpx10; 
						break;
					}

					default:
					{
						return null;
					}
				}
				*/
				
				// Load the data
				var gpx:XML = XML(data);
				
				// Set the time variable
				var time:Date;
				var t:String = gpx.time[0];
				if (t == null)
				{
					time = new Date();
				}
				else
				{
					time = parseDate(t);
				}
				
				var sref:SpatialReference = new SpatialReference(EPSG_GEOGRAPHIC);
				var att:XML;
				
				// Get bounds
				var bounds:Extent = null;
				var boundsList:XMLList = gpx.bounds;
				if (boundsList.length() > 0)
				{
					att = boundsList[0];
					bounds = new Extent(Number(att.@minlon), Number(att.@minlat), Number(att.@maxlon), Number(att.@maxlat), sref);					
				}
				
				// Get waypoint objects
				var wpts:XMLList = gpx.wpt;
				for each (var wpt:XML in wpts)
				{
					// Create a graphic
					var wptgraphic:Graphic =  generatePointGraphic(wpt,sref);
					
					// Add to results set
					resultpoints.push(wptgraphic);
				}
				
				// Get route objects
				var rtes:XMLList = gpx.rte;
				for each (var rte:XML in rtes)
				{
					var rtepts:Array = [];
					var rteatts:Object = {};
					for each (var rteatt:XML in rte.children())
					{
						// Check if this is a point object
						if (rteatt.name().localName == "rtept")
						{
							// Add to the points list
							var rteptGraphic:Graphic = generatePointGraphic(rteatt,sref);
	
							// Add point to array
							rtepts.push(rteptGraphic.geometry);

							// Add to results set
							resultpoints.push(rteptGraphic);
						}
						else
						{
							// Add to the attributes
							rteatts[rteatt.name().localName] = rteatt.toString();						
						}
					}
					
					// Create a route line object
					var rteLine:Polyline = new Polyline([rtepts],sref);
					
					// Create a graphic
					var rtegraphic:Graphic = new Graphic(rteLine, getLineSymbol("Route"), rteatts);
					
					// Add to results set
					resultlines.push(rtegraphic);
				}
				
				// Get track objects
				var trks:XMLList = gpx.trk;
				for each (var trk:XML in trks)
				{
					var trkPaths:Array = [];
					var trkAtts:Object = {};

					for each(var trkAtt:XML in trk.children())
					{
						if (trkAtt.name().localName == "trkseg")
						{
							// Get the points from each segment
							var segpts:Array = [];
							var seglist:XMLList = trkAtt.trkpt;
							
							for each (var trkpt:XML in seglist)
							{
								// Add to the points list
								var trkptGraphic:Graphic = generatePointGraphic(trkpt,sref);
								
								// Add point to array
								segpts.push(trkptGraphic.geometry);
								
								// Add to results set
								// resultpoints.push(trkptGraphic);
							}
							
							// Add segment points to the paths array
							if (segpts.length > 0)
							{
								trkPaths.push(segpts);
							}
						}
						else
						{
							// Add to the attributes
							trkAtts[trkAtt.name().localName] = trkAtt.toString();
						}
					}

					if (trkPaths.length > 0)
					{
						// Create a track line object
						var trkLine:Polyline = new Polyline(trkPaths,sref);
						
						// Create a graphic
						var trkgraphic:Graphic = new Graphic(trkLine, getLineSymbol("Track"), trkAtts);
						
						// Add to results set
						resultlines.push(trkgraphic);
					}
				}
				
				// Reset the default namespace
				default xml namespace = null;
			}
			
			
			return { points: resultpoints, lines: resultlines, extent: bounds };
		}
		
		private static function parseUTCDate(str:String):Date 
		{ 
			var matches : Array = str.match(/(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)Z/); 
			
			var d : Date = new Date(); 
			
			d.setUTCFullYear(int(matches[1]), int(matches[2]) - 1, int(matches[3])); 
			d.setUTCHours(int(matches[4]), int(matches[5]), int(matches[6]), 0); 
			
			return d; 
		} 
		
		private static function parseDate(str:String):Date
		{
			var matches : Array = str.match(/(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)Z*/);
			
			var d : Date = new Date();
			
			if (matches != null)
			{
				d.setFullYear(int(matches[1]), int(matches[2]) - 1, int(matches[3]));
				d.setHours(int(matches[4]), int(matches[5]), int(matches[6]), 0);
				return d;
			}
			else
				return null;
		}

		
		/**
		 * Generates a point graphic from a GPX xml fragment.
		 */		
		private static function generatePointGraphic(xml:XML, sref:SpatialReference = null):Graphic
		{
			if (sref == null)
			{
				sref = new SpatialReference(EPSG_GEOGRAPHIC);
			}
			
			var pt:MapPoint = new MapPoint(Number(xml.@lon), Number(xml.@lat), sref);
			var atts:Object = {};							
			for each (var att:XML in xml.children())
			{
				switch(att.name().localName)
				{
					case "time":
					{
						atts["time"] = parseDate(att.toString());
						break;
					}
						
					case "ele":
					{
						atts["elevation"] = Number(att.toString());
						break;
					}
						
					default:
					{
						atts[att.name().localName] = att.toString();						
					}
				}
			}
			
			// Build a point graphic
			return new Graphic(pt, getMarkerSymbol(atts["sym"]), atts);
		}
		
		
		/* --------------------------------------------------------------------
		Basic symbol functions
		-------------------------------------------------------------------- */
		
		/** 
		 * Generate a default marker symbol for the GPX point graphic.
		 */ 
		private static function getMarkerSymbol(symbolname:String = null):Symbol
		{
			var symbol:Symbol;
			
			switch(symbolname)
			{
				case "Waypoint":
				{
					symbol = new SimpleMarkerSymbol("diamond",12,0xFF0000,1,0,0,0,new SimpleLineSymbol("solid",0x000000,1,2));
					break;
				}
					
				case "Trail Head":
				{
					symbol = new SimpleMarkerSymbol("square",12,0xFFFFFF,1,0,0,0,new SimpleLineSymbol("solid",0x000000,1,2));
					break;
				}
					
				default:
				{
					symbol = new SimpleMarkerSymbol("circle",12,0x00FF00,1,0,0,0,new SimpleLineSymbol("solid",0x000000,1,2));
					break;
				}
			}
			
			return symbol;
		}

		/** 
		 * Generate a default marker symbol for the GPX line graphic.
		 */ 
		private static function getLineSymbol(symbolname:String = null):Symbol
		{
			var symbol:Symbol;
			
			switch(symbolname)
			{
				case "Track":
				{
					symbol = new SimpleLineSymbol("dash",0x000000,1,2);
					break;
				}
					
				case "Route":
				{
					symbol = new SimpleLineSymbol("solid",0xFF0000,1,2);
					break;
				}
					
				default:
				{
					symbol = new SimpleLineSymbol("solid",0x00FF00,1,2);
					break;
				}
			}
			
			return symbol;
		}

	}
}