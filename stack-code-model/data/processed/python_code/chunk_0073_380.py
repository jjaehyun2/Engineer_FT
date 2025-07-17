package widgets.DrawAdvanced.components.supportClasses
{
	import com.esri.ags.Graphic;
	import com.esri.ags.SpatialReference;
	import com.esri.ags.geometry.*;
	import com.esri.ags.symbols.*;
	
	import flash.text.TextFormat;
	
	public class LegacyGraphicLoaderUtil
	{
		/**
		 * Deserialises graphics stored in the previous widget format (From Robert S's Code)
		 */
		public static function ImportGraphics(dobj:Object):Array
		{
			var i:Number;
			var graphics:Array = [];
			for (i = 0; i < dobj.length; i++)
			{
				var gObj:Object = dobj[i];
				var gArrObj:Object;
				var Geom:Geometry;
				var gArray:Array;
				var pA:Array;
				var m:int;
				var nX:Number;
				var nY:Number;
				var gA:Array;
				var sMP:String;
				
				switch (gObj.geomtype){
					case "MAPPOINT":
					{
						gArrObj = gObj.geomarray;
						nX = gArrObj[0].x;
						nY = gArrObj[0].y;
						Geom = new MapPoint(nX,nY,new SpatialReference(gObj.geomsr));
						break;
					}
						
					case "POLYLINE":
					{
						gArrObj = gObj.geomarray;
						pA = [];
						for (m=0; m<gArrObj.length; m++)
						{
							nX = gArrObj[m].x;
							nY = gArrObj[m].y;
							pA.push(new MapPoint(nX,nY,new SpatialReference(gObj.geomsr)));
						}
						var pLine:Polyline = new Polyline(null,new SpatialReference(gObj.geomsr));
						pLine.addPath(pA);
						
						Geom = pLine;
						break;
					}
						
					case "POLYGON":
					{
						gArrObj = gObj.geomarray;
						pA = [];
						for (m=0; m<gArrObj.length; m++)
						{
							nX = gArrObj[m].x;
							nY = gArrObj[m].y;
							pA.push(new MapPoint(nX,nY,new SpatialReference(gObj.geomsr)));
						}
						var pPoly:Polygon = new Polygon(null,new SpatialReference(gObj.geomsr));
						pPoly.addRing(pA);
						
						Geom = pPoly;
						break;
					}
						
					case "EXTENT":
					{
						gArrObj = gObj.geomarray;
						pA = [];
						for (m=0; m<gArrObj.length; m++)
						{
							nX = gArrObj[m].x;
							nY = gArrObj[m].y;
							pA.push(new MapPoint(nX,nY,new SpatialReference(gObj.geomsr)));
						}
						var pExtent:Extent = new Extent(pA[0].x,pA[0].y, pA[1].x, pA[1].y, new SpatialReference(gObj.geomsr));
						
						Geom = pExtent;
						break; 
					}
				}
				
				// Get the attributes 
				var atts:Object = gObj.gattributes;
				
				// Construct the graphic
				var gra:Graphic = new Graphic(Geom,null,atts);
				gra.name = gObj.gname;
				gra.toolTip = "Double click to open this graphics symbology properties";
				
				switch(gObj.symtypename){
					
					case "TextSymbol":
					{
						var symFontE:String = gObj.symfonte;
						var fBold:Boolean = symFontE.indexOf("B") > -1 ? true:false;
						var fItal:Boolean = symFontE.indexOf("I") > -1 ? true:false;
						var fUnd:Boolean = symFontE.indexOf("U") > -1 ? true:false;
						
						var txtsymBackground:Boolean = Boolean(gObj.txtsymbackground == "true") || false;
						var txtsymBackgroundColour:uint = Number(gObj.txtsymbackgroundcolour) || 0x000000;
						var txtsymBorder:Boolean = Boolean(gObj.txtsymborder == "true") || false;
						var txtsymBorderColour:uint = Number(gObj.txtsymbordercolour) || 0x000000;
						
						var txtSym:TextSymbol = new TextSymbol(gObj.symtext);
						txtSym.background = txtsymBackground;
						txtSym.backgroundColor = txtsymBackgroundColour;
						txtSym.border = txtsymBorder;
						txtSym.borderColor = txtsymBorderColour;
						
						var txtFormat:TextFormat = new TextFormat(gObj.symtype, gObj.symsize, gObj.symcolor, fBold, fItal, fUnd);
						txtSym.textFormat = txtFormat;
						gra.symbol = txtSym;
						break;
					}
						
					case "SimpleMarkerSymbol":
					{
						var outlineSym0:SimpleLineSymbol = new SimpleLineSymbol(gObj.symltype, gObj.symcolor2, gObj.symalpha2, gObj.symwidth);
						var ptSym:SimpleMarkerSymbol = new SimpleMarkerSymbol(gObj.symtype, gObj.symsize, gObj.symcolor, gObj.symalpha1,0,0,0,outlineSym0);
						gra.symbol = ptSym;
						break;
					}
						
					case "SimpleLineSymbol":
					{
						var lineSym:SimpleLineSymbol = new SimpleLineSymbol(gObj.symtype, gObj.symcolor, gObj.symalpha1, gObj.symwidth);
						gra.symbol = lineSym;
						break;
					}
						
					case "SimpleFillSymbol":
					{
						var outlineSym:SimpleLineSymbol = new SimpleLineSymbol(gObj.symltype, gObj.symcolor2, gObj.symalpha2, gObj.symwidth);
						var polySym:SimpleFillSymbol = new SimpleFillSymbol(gObj.symtype, gObj.symcolor, gObj.symalpha1, outlineSym);
						gra.symbol = polySym;
						break;
					}
				}
				graphics.push(gra);
			}
			
			return graphics;
		}
		
		/**
		 * Check if the suppied object contains legacy format saved graphics.
		 */
		public static function isLegacyFormat(dobj:Object):Boolean
		{
			var isLegacy:Boolean = false;
			
			if (dobj.length > 0)
			{
				// Get the first object
				var gObj:Object = dobj[0];
				
				// Check for the legacy format object properties
				if (gObj.geomtype && gObj.geomarray && gObj.gname)
				{
					isLegacy = true;
				}
			}
			
			return isLegacy;
		}
	}
}