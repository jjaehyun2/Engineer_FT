//06.23.14 - NE - Updated print function to deal with new popup security on USGS browsers. Updated release build. Updated legend behavior.
//12.07.12 - NE - Updated to include resource file info.
//10.13.11 - NE - Updated popup window component close functions.
//08.22.11 - NE - Added logic to deal with Full Screen lack of Text Input Adobe security issue.
//08.03.11 - NE - Updates to display data as 'n/a' if value is -999.
//03.13.11 - NE - Fixed bug with printing due to removal of Total Hg from constituents.
//03.10.11 - NE - Removed duplicates network/unit finder unit list.  Also, sorted unit list alphabetically.
//03.01.11 - NE - Added logic and UI for print map/chart options.
//03.01.11 - NE - Added ability to print pdf of charts.
//02.28.11 - NE - Separated tools into buttons.
//02.25.11 - NE - Adjusted _queryWindow initial location when in print mode.
//02.22.11 - NE - Updated HUC Query performance
//02.17.11 - NE - Changed query window behavior.
//02.4.11 - NE - Updated print pdf function and layout.
//12.15.10 - NE - Added right click zoom out behavior.
//10.27.10 - NE - Removed largest 4 scales from mapper.  
//10.27.10 - NE - Added download data to tools dropdown.
//10.20.10 - NE - Converted to Mercury Mapper 2.0

//End as template

//04.28.10 - NE - Added functions for lat/lng and map scale feedback in mapper.  Tweaked info query.
//04.23.10 - NE - Added basic PDF print functionality. Added opacity slider to map service layer.
//04.21.10 - NE - Added behavior to keep infoWindow from opening behind tools and menus.
//04.21.10 - NE - Adjusted Network/Unit Finder tool to zoom to extent of selected network and groups of units with same unit name.
//04.20.10 - NE - Changed infoWindow functionality to show values of all constituents on all queries
//04.19.10 - NE - Added Network/Unit Finder tool to zoom to extent of selected unit
//04.15.10 - NE - Adjusted code to change available layers box based on screen resolution and window size.
//04.14.10 - NE - Added functionality to minimize/maximize available Layers box.
//01.29.10 - JB - Used custom image component for shrinking effect, standardized layer toggling.
//01.26.10 - JB - Created
 /***
 * ActionScript file for Mercury Mapper */

import com.esri.ags.FeatureSet;
import com.esri.ags.Graphic;
import com.esri.ags.events.ExtentEvent;
import com.esri.ags.events.FindEvent;
import com.esri.ags.events.MapMouseEvent;
import com.esri.ags.geometry.Extent;
import com.esri.ags.geometry.MapPoint;
import com.esri.ags.geometry.Polygon;
import com.esri.ags.layers.TiledMapServiceLayer;
import com.esri.ags.symbols.InfoSymbol;
import com.esri.ags.tasks.QueryTask;
import com.esri.ags.tasks.supportClasses.AddressCandidate;
import com.esri.ags.tasks.supportClasses.AddressToLocationsParameters;
import com.esri.ags.tasks.supportClasses.FindResult;
import com.esri.ags.tasks.supportClasses.Query;
import com.esri.ags.utils.GraphicUtil;
import com.esri.ags.utils.JSON;
import com.esri.ags.utils.WebMercatorUtil;

import controls.MapServiceLegend;
import controls.skins.WiMInfoWindowSkin;

import flash.display.DisplayObject;
import flash.display.StageDisplayState;
import flash.events.Event;
import flash.events.MouseEvent;

import gov.usgs.wim.controls.WiMInfoWindow;
import gov.usgs.wim.utils.XmlResourceLoader;

import mx.charts.ColumnChart;
import mx.collections.ArrayCollection;
import mx.collections.Sort;
import mx.collections.SortField;
import mx.containers.VBox;
import mx.controls.*;
import mx.controls.sliderClasses.SliderThumb;
import mx.core.FlexGlobals;
import mx.core.UIComponent;
import mx.effects.Fade;
import mx.effects.Resize;
import mx.effects.Rotate;
import mx.events.CloseEvent;
import mx.events.DragEvent;
import mx.events.FlexEvent;
import mx.events.ItemClickEvent;
import mx.events.MenuEvent;
import mx.events.MoveEvent;
import mx.managers.CursorManager;
import mx.managers.PopUpManager;
import mx.resources.ResourceBundle;
import mx.rpc.AsyncResponder;
import mx.rpc.events.ResultEvent;
import mx.utils.Base64Decoder;
import mx.utils.ObjectProxy;

import org.alivepdf.cells.CellVO;
import org.alivepdf.colors.RGBColor;
import org.alivepdf.fonts.CoreFont;
import org.alivepdf.fonts.FontFamily;
import org.alivepdf.fonts.IFont;
import org.alivepdf.layout.Orientation;
import org.alivepdf.layout.Size;
import org.alivepdf.layout.Unit;
import org.alivepdf.pdf.PDF;
import org.alivepdf.saving.Download;
import org.alivepdf.saving.Method;

import spark.components.ComboBox;
import spark.components.Label;
import spark.components.SkinnableContainer;

			[Bindable]
			[Embed(source='assets/images/Satellite.png')] 
			private var satelliteIcon:Class;
			[Bindable]
			[Embed(source='assets/images/grayCanvas.png')]
			private var grayCanvasIcon:Class;
			/* Image based on file from Wikimedia Commons and is licensed under https://secure.wikimedia.org/wikipedia/en/wiki/en:GNU_Free_Documentation_License */
			[Bindable]
			[Embed(source='assets/images/mountain.png')] 
			private var mountainIcon:Class;
			[Bindable]
			[Embed(source='assets/images/shield.png')]
			private var streetsIcon:Class;

    		private var initExtent:Extent;    					
			private var mapCurrentExtent:Extent;
			private var mapCPoint:MapPoint;
			private var mapLevel:Number;
			
			//Array of parameters for info queries
			/*private var queryParameters:Object = {
													predMeHg: new ArrayCollection(["PMEHG", "Predicted MeHg", "http://wim.usgs.gov/ArcGIS/rest/services/MercuryMapper/nps_mapper/MapServer/6"]),
													wetland: new ArrayCollection(["NLCDP9", "Wetlands", "http://wim.usgs.gov/ArcGIS/rest/services/MercuryMapper/nps_mapper/MapServer/4"]),
													pH: new ArrayCollection(["MED_PH", "pH", "http://wim.usgs.gov/ArcGIS/rest/services/MercuryMapper/nps_mapper/MapServer/12"]),
													sulfate: new ArrayCollection(["MED_SULFAT", "Sulfate", "http://wim.usgs.gov/ArcGIS/rest/services/MercuryMapper/nps_mapper/MapServer/10"]),
													carbon: new ArrayCollection(["MED_CARBON", "Carbon", "http://wim.usgs.gov/ArcGIS/rest/services/MercuryMapper/nps_mapper/MapServer/8"])
												 };*/
		
			private var dataSICheck:Boolean;
			
			[Bindable]
			private var mapX:Number = 0;
			[Bindable]
			private var mapY:Number = 0;
			
			[Bindable]
			private var printS:String;
			
			private var pdf:PDF;
			private var pdfChart:PDF;
			    		
			[Bindable]
			private var genAlpha:Number = 0.72;   
			
			private var min:Resize = new Resize();
    		private var max:Resize = new Resize();		
			private var operLayersFull:Number = 0;
			private var operLayersTitleHeight:Number = 43;
			
			[Bindable] private var windLoc:String;
            private var queryPt:MapPoint;

			private var _queryWindow:WiMInfoWindow;
			private var queryX:Number;
			private var queryY:Number;

			private var _dataWindow:WiMInfoWindow;

			[Bindable]
			public var printFromMap:Function;
			
			private var tempObj:Object = {};

			private var wasInFullScreen:Boolean;

			private var popUpBoxes:Object = new Object();

			private var xmlResourceLoader:XmlResourceLoader = new XmlResourceLoader();
			
			/*[Bindable]
			private var npsUrlTemplate:String = "http://{subDomain}.tiles.mapbox.com/v3/nps.pt-shaded-relief,nps.pt-urban-areas,nps.pt-river-lines,nps.pt-admin-lines,nps.pt-park-poly,nps.pt-mask,nps.pt-hydro-features,nps.pt-admin-labels,nps.pt-roads,nps.pt-road-shields,nps.pt-park-points,nps.pt-hydro-labels,nps.pt-city-labels,nps.pt-park-labels/{level}/{col}/{row}.png"
			*/
			[Bindable]
			private var npsUrlTemplate:String = "http://{subDomain}.tiles.mapbox.com/v3/" +
				"nps.a6be40f0," +
				"nps.6ebce21f," +
				"nps.a706dc69," +
				"nps.8eb491cc," +
				"nps.5621c3ce," +
				"nps.61530aff," +
				"nps.5dfeaf68" +
				"/{level}/{col}/{row}.png";

			[Bindable]
			private var npsParkPolygonsUrlTemplate:String = "http://{subDomain}.tiles.mapbox.com/v3/" +
				"nps.6ebce21f," +
				"nps.5621c3ce," +
				"nps.61530aff," +
				"nps.3b98a97d" +
				"/{level}/{col}/{row}.png";
				
			[Bindable]
			private var npsLabelsUrlTemplate:String = "http://{subDomain}.tiles.mapbox.com/v3/" +
				"nps.3b98a97d" +
				"/{level}/{col}/{row}.png";
	

			private static const ABCD:Array = [ "a", "b", "c", "d" ];
			
			private var mainFont:IFont = new CoreFont( FontFamily.HELVETICA_BOLD );
			private var simpleFont:IFont = new CoreFont( FontFamily.HELVETICA );
			private var italicFont:IFont = new CoreFont( FontFamily.TIMES_ITALIC );
	
			private var printMode:Boolean = false;


			private function load():void
    		{
				initExtent = map.extent;
				ExternalInterface.addCallback("handleWheel", handleWheel);
				ExternalInterface.addCallback("rightClick", onRightClick);
				
				var lodsTemp:Array = map.lods;
				lodsTemp.length = 14;
				lodsTemp.splice(0,4);
				lodsTemp.reverse();
				map.lods = lodsTemp;
				
				//geocoder.searchValue.addEventListener(MouseEvent.CLICK, fullScreenHandler);
				
				//networkLegendService.send();
				//unitLegendService.send();
				
				xmlResourceLoader.load(["locale/en_US", "en_US"]);
				
				
				
			}

			/*private function fullScreenHandler(event):void {
				if (fullScreen.isFullScreen() == true) {
					wasInFullScreen = true;
					fullScreen.toggleFullScreen();
				} else {
					wasInFullScreen = false;
				}
			}*/

			private function deDupe(item:Object):Boolean {
				// the return value
				var retVal:Boolean = false;
				// check the items in the itemObj Ojbect to see if it contains the value being tested
				if (!tempObj.hasOwnProperty(item.label)) {
					// if not found add the item to the object
					tempObj[item.label] = item;
					retVal = true;
				}
				return retVal;
				// or if you want to feel like a total bad ass and use only one line of code, use a tertiary statement ;)
				// return (tempObj.hasOwnProperty(item.label) ? false : tempObj[item.label] = item && true);
			}

	    	private function onExtentChange(event:ExtentEvent):void            
    		{
    			if (queryPt != null) { windLoc = windLocCalc(); }
				
				printSubmit.enabled = false;
				
				trace(map.level);
			}
    		
    		/*private function initToolPop():void 
    		{
    			var toolMenu:Menu = new Menu();
    			var tools:Object = [
    				{label: "Network/Unit Finder"},
					{label: "Download Data"}
    			];
    			toolMenu.dataProvider = tools;
    			toolMenu.addEventListener("itemClick", toolSelection);
    			toolPop.popUp = toolMenu;
    		}
    		
    		private function toolSelection(event:MenuEvent):void 
    		{
    			var select:String = event.label;
    			if (select == "Network/Unit Finder") {
    				netUnitDrop.x = event.target.x;
    				netUnitDrop.y = event.target.y + 10;
    				netUnitDrop.visible = true;
				} else if (select == "Download Data") {
					navigateToURL(new URLRequest(''));
				}
    		}*/	

			private function netFindTool():void 
			{
				/*netUnitDrop.x = 165;
				netUnitDrop.y = 135;
				netUnitDrop.visible = true;*/
				
				_queryWindow = PopUpManager.createPopUp(map, NetworkUnitFinder, false) as WiMInfoWindow;
				_queryWindow.setStyle("skinClass", WiMInfoWindowSkin);
				_queryWindow.x = 165;
				_queryWindow.y = 135;
				_queryWindow.addEventListener(CloseEvent.CLOSE, closePopUp);
			}

			public function closePopUp(event:CloseEvent):void {
				PopUpManager.removePopUp(event.currentTarget as WiMInfoWindow);
				queryGraphicsLayer.clear();
			}
    		
    		//Handles all Previous Extent, Next Extent and Full Extent requests
    		/*private function navHandler(event:ItemClickEvent):void 
    		{
    			if (event.index == 0) {
    				navToolbar.zoomToPrevExtent();
    			} else if (event.index == 1) {
    				navToolbar.zoomToNextExtent();	
    			} else {
    				fullExtent();
    			}
    		}*/
    		
    		//Handles click requests for map layer info
    		private function onMapClick(event:MapMouseEvent):void
    		{
    			if (dataSourceVis.contains(8) || dataSourceVis.contains(10) || dataSourceVis.contains(12) || dataSourceVis.contains(14) || dataSourceVis.contains(16) ) {
				//if (hucDataCB.selected) {
    				
    				queryPt = event.mapPoint;
	    			
	    			queryGraphicsLayer.clear();
	    			infoGraphicsLayer.clear();
					PopUpManager.removePopUp(_queryWindow);
	    			
	    			windLoc = windLocCalc();
	    			
	    			var infoGraphicsSymbol:InfoSymbol = wetlandsGraphicSym;	 
	    			
	    			var query:Query = new Query();
	    			query.returnGeometry = true;
	    			query.geometry = event.mapPoint;
	    			//query.outFields = ["HUC","PREDMEHG","FULLMEHG","MED_PH","FULLPH","MED_SULF","FULLSULF","MED_TOC","FULLTOC","PRC_WTLD","FULLWTLD","NTWK_NA1","NTWK_NA2","NTWK_NA3","NTWK_NA4","PARK_NA1","PCT_AR1","PARK_NA2","PCT_AR2","PARK_NA3","PCT_AR3","PARK_NA4","PCT_AR4","PARK_NA5","PCT_AR5","PARK_NA6","PCT_AR6","PARK_NA7","PCT_AR7","PARK_NA8","PCT_AR8","PARK_NA9","PCT_AR9","PARK_NA10","PCT_AR10","PARK_NA11","PCT_AR11"];
	    			query.outFields = ["*"];
					
					var queryTask:QueryTask = new QueryTask(resourceManager.getString('urls', 'HgDataUrl')+"/8");						
					queryTask.showBusyCursor = true;
					queryTask.execute( query, new AsyncResponder(hucResult, queryFault, event.mapPoint));
			    	
			    	//Create info box for results, but don't display it yet.
    				var infoBoxGraphic:Graphic = new Graphic(event.mapPoint, infoGraphicsSymbol);
    				infoBoxGraphic.name = "infoBoxGraphic";
    				infoBoxGraphic.attributes = [];
    				infoBoxGraphic.visible = false;
    				
			    	//Add info box graphic to information layer
			    	infoGraphicsLayer.add(infoBoxGraphic);	
					
					queryX = event.stageX;
					queryY = event.stageY;
					
				}
				
    		}

			private function updateNPSServices(layerID:int):void {
				dataSourceVis.removeItemAt(0); 
				dataSourceVis.addItem(layerID); 
				npsServices.refresh(); 
				npsServicesLegend.aLegendService.send();
			}

			private function dataDownload():void 
			{
				_dataWindow = PopUpManager.createPopUp(map, DataDownloadWindow, false) as WiMInfoWindow;
				_dataWindow.setStyle("skinClass", WiMInfoWindowSkin);
				_dataWindow.x = (FlexGlobals.topLevelApplication.width/2) - (_dataWindow.width/2);
				_dataWindow.y = (FlexGlobals.topLevelApplication.height/2) - (_dataWindow.height/2);
				_dataWindow.addEventListener(CloseEvent.CLOSE, closePopUp);
			}
    		
    		private function hucResult(featureSet:FeatureSet, queryPoint:MapPoint):void
    		{
    			if (featureSet.features.length > 0) {
					
					_queryWindow = PopUpManager.createPopUp(map, MercuryDataWindow, false) as WiMInfoWindow;
					_queryWindow.setStyle("skinClass", WiMInfoWindowSkin);
					_queryWindow.x = (FlexGlobals.topLevelApplication.width/2) - (_queryWindow.width/2);
					_queryWindow.y = (FlexGlobals.topLevelApplication.height/2) - (_queryWindow.height/2);
					_queryWindow.addEventListener(CloseEvent.CLOSE, closePopUp);
					//_queryWindow.addEventListener(MouseEvent.MOUSE_OVER, alphaFull);
					//_queryWindow.addEventListener(MouseEvent.MOUSE_OUT, alphaPart);
					_queryWindow.addEventListener(MouseEvent.MOUSE_DOWN, addMoveEvent);
					_queryWindow.addEventListener(MouseEvent.MOUSE_UP, alphaFull);
					
					function addMoveEvent():void {
						_queryWindow.addEventListener(MoveEvent.MOVE, alphaPart);
					}
					
					function alphaPart():void {
						_queryWindow.alpha = 0.3;
					}
					
					function alphaFull():void {
						_queryWindow.alpha = 1.0;
					}
					
					var wetGraphic:Graphic = featureSet.features[0];            		
            		wetGraphic.symbol = wetQuerySym;
	            	queryGraphicsLayer.add(wetGraphic);
	            	
	            	var infoBoxGraphic:Graphic = infoGraphicsLayer.getChildByName("infoBoxGraphic") as Graphic;
	            	 
	            	//infoBoxGraphic.attributes = new ObjectProxy({PREDMEHG: "", PRC_WTLD:"", MED_PH: "", MED_SULF: "", MED_TOC: ""});
	            	//infoBoxGraphic.attributes[queryParameters[hucDataOpt.selectedValue][0]] = wetGraphic.attributes[queryParameters[hucDataOpt.selectedValue][0]];
	            	infoBoxGraphic.attributes = wetGraphic.attributes;
					
	            	infoBoxGraphic.attributes["infoTitle"] = "HUC: " + wetGraphic.attributes["HUC"];
	            	
					_queryWindow.data = infoBoxGraphic.attributes;
					
				}
    		}
    		    		
    		private function infoResult(aFeatureSet:FeatureSet, key:String):void
    		{	
    			var infoBoxGraphic:Graphic;
	    		if (aFeatureSet.features.length > 0) {
	    			infoBoxGraphic = infoGraphicsLayer.getChildByName("infoBoxGraphic") as Graphic;
	    			var infoAttributes:Object = aFeatureSet.features[0].attributes;
	    			if (infoBoxGraphic != null) {
		    			if (infoAttributes[key] == '0' || infoAttributes[key] == undefined) {
		    				infoBoxGraphic.attributes[key] = 'n/a';
		    			} else {
		    				infoBoxGraphic.attributes[key] = infoAttributes[key];
		    			}
	    			}
	    			infoGraphicsLayer.refresh();
	    		} else {
	    			infoBoxGraphic = infoGraphicsLayer.getChildByName("infoBoxGraphic") as Graphic;
	    			infoBoxGraphic.attributes[key] = 'n/a';
	    		}
				
				if (infoBoxGraphic.attributes.PMEHG != '' && infoBoxGraphic.attributes.MED_PH != '' && infoBoxGraphic.attributes.SULFAT != '' && infoBoxGraphic.attributes.MED_CARBON != '' && infoBoxGraphic.attributes.NLCDP9 != '') {
					_queryWindow.data = infoBoxGraphic.attributes;
					trace("queryWindow data object:" + _queryWindow.data.PMEHG + ' ' + 
						_queryWindow.data.MED_PH + ' ' + _queryWindow.data.MED_SULFAT + ' ' + 
						_queryWindow.data.MED_CARBON + ' ' + _queryWindow.data.NLCDP9);
				}
				
				/*if (_queryWindow.data.length > 0) {
					trace('length: ' + _queryWindow.data.length.toString());
				}*/
			}
    		   		
    		   
    		/* private function infoSingleResult(aFeatureSet:FeatureSet, configObjects:ArrayCollection):void
    		{

    			if (aFeatureSet.features.length != 0) {
                	      		
					var aGraphic:Graphic = aFeatureSet.features[0];
					
					if (aGraphic.attributes[configObjects[0]] != 0) {
						            		
	            		aGraphic.symbol = wetQuerySym;
		            	queryGraphicsLayer.add(aGraphic);
						
						var infoBoxGraphic:Graphic = infoGraphicsLayer.getChildByName("infoBoxGraphic") as Graphic;
		            	
		            	infoBoxGraphic.attributes = new ObjectProxy(aGraphic.attributes);
		            	infoBoxGraphic.attributes["infoTitle"] = configObjects[1];
		            	infoBoxGraphic.attributes["infoResult"] = aGraphic.attributes[configObjects[0]];
		            	infoBoxGraphic.visible = true;
		            	infoGraphicsLayer.refresh();		            
		   			} 	            	
				} 
			}   */
			
			private function queryFault(info:Object, token:Object = null):void
    		{
    			Alert.show(info.toString());
    		} 
    		   	
			private function baseSwitch(event:FlexEvent):void            
    		{                
	    		var tiledLayer:TiledMapServiceLayer = event.target as TiledMapServiceLayer;                
	    		//map.lods = tiledLayer.tileInfo.lods;
    		}
    		
    		private function fullExtent():void
    		{
    			map.extent = initExtent;
    		}

			private function disablePrint(event):void {
				printSubmit.enabled = false;
			}
    		
			private function enablePrint(event):void {
				printSubmit.enabled = true;
			}
    		
			private function geoCode(searchString:String):void
			{
				parkTask.execute(parkParams);
				if (wasInFullScreen == true) {
					//fullScreen.toggleFullScreen();
					wasInFullScreen = null;
				} else {
					wasInFullScreen = null;
				}
			}

    		private function parkResult(event:FindEvent):void
			{
				if (event.findResults.length > 0)
				{
					var graphic:Graphic = FindResult(event.findResults[0]).feature;
					var graphicsExtent:Extent = GraphicUtil.getGraphicsExtent(new Array(graphic));
					if (graphicsExtent)
					{
						map.extent = graphicsExtent;
						return;
					}
				} else {
					
					var parameters:AddressToLocationsParameters = new AddressToLocationsParameters();
					//parameters such as 'SingleLine' are dependent upon the locator service used.
					parameters.address = { SingleLine: geocoder.searchValue.text };
					
					// Use outFields to get back extra information
					// The exact fields available depends on the specific locator service used.
					parameters.outFields = [ "*" ];
					
					locator.addressToLocations(parameters, new AsyncResponder(onResult, onFault));
					function onResult(candidates:Array, token:Object = null):void
					{
						if (candidates.length > 0)
						{
							var addressCandidate:AddressCandidate = candidates[0];
							
							map.extent = com.esri.ags.utils.WebMercatorUtil.geographicToWebMercator(new Extent(addressCandidate.attributes.Xmin, addressCandidate.attributes.Ymin,  addressCandidate.attributes.Xmax, addressCandidate.attributes.Ymax, map.spatialReference)) as Extent;
							
						}
						else
						{
							Alert.show("Sorry, couldn't find a location for this address"
								+ "\nAddress: " + geocoder.searchValue.text);
						}
					}
					
					function onFault(info:Object, token:Object = null):void
					{
						//myInfo.htmlText = "<b>Failure</b>" + info.toString();
						Alert.show("Failure: \n" + info.toString());
					}
		
				}
			}
			
    		//legend methods
			private function getLegends(event:FlexEvent):void {
				//hgLegendService.send();
			}
			private function legendResults(resultSet:ResultEvent, aLegendContainer:SkinnableContainer, layerIDs:ArrayCollection, singleTitle:String = null):void
			{
				
				if (resultSet.statusCode == 200) {
					//Decode JSON result
					var decodeResults:Object = com.esri.ags.utils.JSON.decode(resultSet.result.toString());
					var legendResults:Array = decodeResults["layers"] as Array;
					//Clear old legend
					aLegendContainer.removeAllElements();	
					 
					//if signle title is specified use that
					if (singleTitle != null || aLegendContainer.id == 'siteLegend') {
						//Add outline with flash effect   
						var singleGroupDescription:spark.components.Label = new spark.components.Label();
						//singleGroupDescription.text = 'sample title';
						/*if (database.selectedValue == "all") {
							singleGroupDescription.text = 'Number of sample results, ';
						} else if (database.selectedValue == "E") {
							singleGroupDescription.text = 'Number of EPA STORET sample results, ';
						} else if (database.selectedValue == "N") {
							singleGroupDescription.text = 'Number of USGS NWIS sample results, ';
						}
						if (display.selectedValue == "0") {
							singleGroupDescription.text += 'by state';
						} else if (display.selectedValue == "1") {
							singleGroupDescription.text += 'by county';
						}*/
						//TODO: Move this to a single style
						singleGroupDescription.setStyle("verticalAlign", "middle");
						singleGroupDescription.setStyle("fontSize", "11");
						singleGroupDescription.height = 20;
						singleGroupDescription.top = 10;
						aLegendContainer.addElement(	singleGroupDescription );
					}
					
					for(var i:int = 0; i < legendResults.length; i++) {											
						if (layerIDs.contains(legendResults[i]["layerId"])) {
							//Add outline with flash effect   
							var groupDescription:spark.components.Label = new spark.components.Label();
							
							//if singleTitle is not specified, Add name with USGS capitalization, first letter only
							if (singleTitle == null) {
								var layerName:String = legendResults[i]["layerName"];
								groupDescription.text = layerName; //.charAt(0).toUpperCase() + layerName.substr(1, layerName.length-1).toLowerCase();
								//TODO: Move this to a single style
								groupDescription.setStyle("verticalAlign", "middle");
								groupDescription.setStyle("fontSize", "11");
								groupDescription.width = 300;
								groupDescription.top = 10;
								aLegendContainer.addElement(	groupDescription );
							}
							
							for each (var aLegendItem:Object in legendResults[i]["legend"]) {
								//Decode base 64 image data
								var b64Decoder:Base64Decoder = new Base64Decoder();							
								b64Decoder.decode(aLegendItem["imageData"].toString());
								//Make new image for decoded bytes
								var legendItemImage:Image = new Image();
								legendItemImage.load( b64Decoder.toByteArray() );
								var aLabel:String = aLegendItem["label"];
								//If singleTitle is specified and there is a single legend item with no label, use the layerName 
								if ((singleTitle != null) && (aLabel.length == 0) && ((legendResults[i]["legend"] as Array).length <= 1)) { aLabel = legendResults[i]["layerName"]; }
								//Use USGS sentance capitalization on labels
								aLabel = aLabel.charAt(0).toUpperCase() + aLabel.substr(1, aLabel.length-1).toLowerCase();								
								var legendItem:HGroup = 
									makeLegendItem( 
										legendItemImage, 
										aLabel
									);
								legendItem.paddingLeft = 20;
								aLegendContainer.addElement( legendItem );
								
							}			
						}
					} 
					
					
				}  else {
					Alert.show("No legend data found.");
				}		
				
				//Remove wait cursor
				CursorManager.removeBusyCursor();
			}
			
			private function makeLegendItem(swatch:UIComponent, label:String):HGroup {
				var container:HGroup = new HGroup(); 
				var layerDescription:spark.components.Label = new spark.components.Label();
				layerDescription.text = label;
				layerDescription.setStyle("verticalAlign", "middle");
				layerDescription.percentHeight = 100;
				container.addElement(swatch);
				container.addElement(layerDescription);
				
				return container;
			}
    		
    		
    		public function isFullScreen() : Boolean
    		{	
    			return (this.stage.displayState == StageDisplayState.FULL_SCREEN);
    		}
    		
    		public function goFullScreen():void
    		{
    			try {
    				this.stage.displayState = StageDisplayState.FULL_SCREEN;
    			}
    			catch (e:Error)
    			{
    				Alert.show(e.toString() + this.stage.displayState, "Error");
    			}
    		}
    		
    		public function exitFullScreen():void
    		{
    			this.stage.displayState = StageDisplayState.NORMAL;
    		}
    		
    		public function toggleFullScreen():void
    		{
    			//stage.addEventListener(FullScreenEvent.FULL_SCREEN, handleFullScreen);
    			if ( !isFullScreen() ) {
    				goFullScreen();
    			} else {
    				exitFullScreen();
    			}
    		}
    		
    		public function fade(object:DisplayObject,inOut:String,alphaFrom:Number,alphaTo:Number,duration:Number):void
    		{
    			
    			var fade:Fade = new Fade();
    			fade.target = object;
    			fade.alphaFrom = alphaFrom;
    			fade.alphaTo = alphaTo;
    			fade.play();
    			
    			if (inOut == "in") {
    				object.visible = true;
    			} else if (inOut == "out") {
    				object.visible = false;
    			}
    		}
    		
    		public function hideAll():void
    		{
    			header.visible = false;
    			headerLogo.visible = false;
				baseLayers.visible = false;
				navigation.visible = false;
				geocoder.visible = false;
				controlLayers.visible = false;
				netFindButton.visible = false;
				dataDownloadButton.visible = false;
				printButton.visible = false;
				map.zoomSliderVisible = false;
    		}
    		
    		public function showAll():void
    		{
    			header.visible = true;
    			headerLogo.visible = true;
				baseLayers.visible = true;
				navigation.visible = true;
				geocoder.visible = true;
				controlLayers.visible = true;
				netFindButton.visible = true;
				dataDownloadButton.visible = true;
				printButton.visible = true;
    		}
    		
    		public function centerMap():void
    		{
    			//map.centerAt(mapCPoint);//-10644926.307107488,4666939.198981996
    			map.level = mapLevel;
    			map.extent = mapCurrentExtent;
    			map.level = mapLevel;
    			map.extent = mapCurrentExtent;
    			map.level = mapLevel;
    			//map.centerAt(mapCPoint);
    			//map.centerAt(new MapPoint(-10644926.307107488,4666939.198981996));
    		}
			
			private function windLocCalc():String {
    			var xmax:Number = map.extent.xmax;
    			var xmin:Number = map.extent.xmin;
    			var ymax:Number = map.extent.ymax;
    			var ymin:Number = map.extent.ymin;
    			var xThird:Number = (xmax - xmin)/3;
    			var yThird:Number = (ymax - ymin)/3;
    			var yHalf:Number = (ymax - ymin)/2;
    			
    			if (queryPt.x < xmin + xThird) {
    				if (queryPt.y < (ymin + yThird)) {
    					windLoc = "upperRight";
    				} else if (queryPt.y < ymin + 2*yThird) {
    					windLoc = "right";
    				} else {
    					windLoc = "lowerRight";
    				}
    			} else if (queryPt.x < (xmin + 2*xThird)) {
    				if (queryPt.y < ymin + yHalf) {
    					windLoc = "top";
    				} else {
    					windLoc = "bottom";
    				}
    			} else {
    				if (queryPt.y < (ymin + yThird)) {
    					windLoc = "upperLeft";
    				} else if (queryPt.y < ymin + 2*yThird) {
    					windLoc = "left";
    				} else {
    					windLoc = "lowerLeft";
    				}
    			}
    			return windLoc;
    		}
    		
    		//function to set up mapper for PDF creation and print job
    		public function startPrint(pEvt:MouseEvent):void
    		{
				if (printMode == false) {
					
					printMode = true;
	    			printTitle.text = "";
	    			printNotes.text = "";
					
					if (pEvt.target is mx.controls.Button && pEvt.target.label == "Print Map") {
						printWithChartCheck.selected = false;
					} else if (pEvt.target.id == "mapAndChartPrintlink") {
						printWithChartCheck.selected = true;
					}
	    			
					fade(printFormBox,"in",0,1,1000);
					
					hideAll();
					
					var mapHeight:Number = map.height;
					var mapWidth:Number = map.width;
					
					var mapExtent:Extent = map.extent;
					var mapXmin:Number = mapExtent.xmin;
					var mapXmax:Number = mapExtent.xmax;
					var mapYmin:Number = mapExtent.ymin;
					var mapYmax:Number = mapExtent.ymax;
					var mapXcenter:Number = (mapXmax-mapXmin)/2+mapXmin;
					var mapYcenter:Number = (mapYmax-mapYmin)/2+mapYmin;
					var mapCenter:MapPoint = new MapPoint(mapXcenter,mapYcenter);
					mapCurrentExtent = map.extent;
					mapCPoint = new MapPoint(mapXcenter, mapYcenter);
					mapLevel = map.level;
					
					//map.visible = false;
					//map.centerAt(mapCPoint);
					
					map.x = (mapWidth/2)-400;
					map.y = (mapHeight/2)-257;
					map.height = 514;
					map.width = 800;
					
					if (_queryWindow != null) {
						_queryWindow.x = FlexGlobals.topLevelApplication.width - _queryWindow.width/2;
						_queryWindow.y = FlexGlobals.topLevelApplication.height - _queryWindow.height/2;
					}
					
					Alert.show("Position and scale the map to desired print area. To scroll, click and drag the map. To zoom, use the scroll wheel on your mouse or hold the shift key down while clicking and dragging to define a zoom-in extent (hold shift-control while clicking and dragging to zoom out).", "", 0, null, alertClose);
				}
			}
			
			//function to createPDF
			public function printPDF(title:String,remarks:String):void
    		{
				//validation of title and notes section performed here. returned if text too many characters.
				var titleVal:Array = title.split('');
    			var remarksVal:Array = remarks.split('');
    			
				fade(printFormBox,"out",1,0,1000);
    			showAll();
    			
				mapLevel = map.level;
    			
    			var pdfDate:Date = new Date();
    			var dateArray:Array = pdfDate.toString().split(" ");
    			var stamp:String = "Printed on " + dateArray[1] + " " + dateArray[2] + ", " + dateArray[5];
    			map.x = 0;
    			map.y = 0;
    			
    			pdf = new PDF (Orientation.LANDSCAPE, Unit.INCHES, Size.LETTER);
				
				pdf.addPage();
    			
				moreInfoIcon.visible = false;
				moreInfoIcon.includeInLayout = false;
				pdf.addImage(header, null, 0.61, 0.61, 7);
				moreInfoIcon.visible = true;
				moreInfoIcon.includeInLayout = true;
				
				pdf.setFont(mainFont, 11);
    			pdf.textStyle(new RGBColor (0x000000) );
    			pdf.setXY(8.125, 1.1);
    			pdf.addMultiCell(1.5, .2, title, 0, "L");
    			
				pdf.setFont(italicFont, 8);
				pdf.setXY(0.9, 7.5);
				pdf.addCell(1, 0.15, "http://wim.usgs.gov/MercuryMapper/MercuryMapper.html");
    			pdf.setXY(8.75, 7.5);
    			pdf.addCell(1, 0.15, stamp);
				
				pdf.setFont(mainFont, 11);
    			
    			var layerCt:int = 0;
    			var wetPx:int = 207;
    			var statPx:int = 120;
    			var ripPx:int = 83;
    			var ripStatPx:int = 101;
    			var expLoc:Number = 1.8;
    			var expFactor:int = 110;
    			
    			//Legend determination. Need to add more legend options and improve logic
				if (dataSourceVis.contains(8) || dataSourceVis.contains(10) || dataSourceVis.contains(12) || dataSourceVis.contains(14) || dataSourceVis.contains(16))
				{
					pdf.setXY(8, 1.9);
					pdf.addCell(2, 0.15, "EXPLANATION");
					pdf.addImage(legendGroup, null, 7.65, expLoc, 2);
				}
    			else
    			{ 
    				pdf.setFont(mainFont, 10);
    				pdf.textStyle(new RGBColor (0x000000) );
    				pdf.setXY(8.25, 2.25);
    				pdf.addMultiCell(1.75, 0.175, "No operational layers selected or no legend available", 0, "L");
				}
    			
				pdf.addImage(map, null, 0.61, 1.51, 7);
				/*if (queryGraphicsLayer.graphicProvider.length > 0) { 
					pdf.setFont(mainFont, 8);
					pdf.textStyle(new RGBColor (0x000000) );
					pdf.setXY(8.1, 5.25);
					pdf.addMultiCell(1.8, .25, _queryWindow.data.infoTitle, 0, "L");
					pdf.setFont(mainFont, 8);
					pdf.textStyle(new RGBColor (0x000000) );
					pdf.setXY(8.1, 5.4);
					pdf.addMultiCell(1.8, .25, "Data Summary", 0, "L");
					pdf.setFont(mainFont, 6);
					pdf.textStyle(new RGBColor (0x000000) );
					pdf.setXY(8.1, 5.65);
					pdf.addMultiCell(1.8, .25, "pH: " + checkValue(_queryWindow.data.CMED_PH,'ph'), 0, "L");
					pdf.setFont(mainFont, 6);
					pdf.textStyle(new RGBColor (0x000000) );
					pdf.setXY(8.1, 5.8);
					pdf.addMultiCell(1.8, .25, "Sulfate: " + checkValue(_queryWindow.data.CMED_SULF,'sulfate'), 0, "L");
					//pdf.writeFlashHtmlText(.25, "Sulfate: " + checkValue(_queryWindow.data.CMED_SULF, 'sulfate') + "<sub>4</sub>");
					//pdf.addImage(sulfateLabel, null, 8.1, 5.8, 2, .25);
					pdf.setFont(mainFont, 6);
					pdf.textStyle(new RGBColor (0x000000) );
					pdf.setXY(8.1, 5.95);
					pdf.addMultiCell(1.8, .25, "Total Organic Carbon: " + checkValue(_queryWindow.data.CMED_TOC,'toc'), 0, "L");
					pdf.setFont(mainFont, 6);
					pdf.textStyle(new RGBColor (0x000000) );
					pdf.setXY(8.1, 6.1);
					pdf.addMultiCell(1.8, .25, "Wetland: " + checkValue(_queryWindow.data.CPRC_WTLD,'wetland'), 0, "L");
					pdf.setFont(mainFont, 6);
					pdf.textStyle(new RGBColor (0x000000) );
					pdf.setXY(8.1, 6.25);
					pdf.addMultiCell(1.8, .25, "Predicted MeHg: " + checkValue(_queryWindow.data.CPREDMEHG,'mehg'), 0, "L");
				}*/
				
    			
				if (_queryWindow == null || queryGraphicsLayer.graphicProvider.length == 0) {
					pdf.textStyle(new RGBColor ( 0x000000 ) );
					
					pdf.setFont(mainFont, 7);
					pdf.addText("USER REMARKS:", 1, 6.6);
					
					pdf.setXY(0.95, 7.2);
					pdf.setFont(mainFont, 7);
					pdf.addMultiCell(9, .08, "DISCLAIMER: This map is for general reference only. The U.S. Geological Survey is not responsible for the accuracy or currentness of the data shown on this basemap.");
					
					pdf.setXY(1, 6.65);
					pdf.setFont(mainFont, 7);
					//pdf.addMultiCell(imageWidth/2, .2, "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.");
					pdf.addMultiCell(7, .18, remarks);
				} else {
					pdf.textStyle(new RGBColor ( 0x000000 ) );
					
					pdf.setXY(0.95, 6.4);
					pdf.setFont(mainFont, 6);
					pdf.addMultiCell(9, .2, "Hydrologic Unit Code (HUC): " + _queryWindow.data.CAT + " (" + _queryWindow.data.CAT_NAME + ")", 0, "L");
					
					pdf.setFont(mainFont, 7);
					pdf.addText("USER REMARKS:", 1, 6.7);
					
					pdf.setXY(0.95, 7.25);
					pdf.setFont(mainFont, 7);
					pdf.addMultiCell(9, .08, "DISCLAIMER: This map is for general reference only. The U.S. Geological Survey is not responsible for the accuracy or currentness of the data shown on this basemap.");
					
					pdf.setXY(1, 6.75);
					pdf.setFont(mainFont, 7);
					//pdf.addMultiCell(imageWidth/2, .2, "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.");
					pdf.addMultiCell(7, .18, remarks);
				}
    			
    			/*pdf.lineStyle(new RGBColor(0x000000), 0.03); 
    			pdf.drawRect(new Rectangle(0.86, 0.86, 9.28, 6.78));
    			pdf.lineStyle(new RGBColor(0x000000), 0.01);
    			pdf.drawRect(new Rectangle(0.92, 0.92, 9.16, 6.66));
    			pdf.drawRect(new Rectangle(1, 2.1, 7, 4.5));*/
    			
				map.zoomSliderVisible = true;
    			map.percentHeight = 100;
    			map.percentWidth = 100;
				
				printMode = false;
    			
    			//pdf.drawRect( new Rectangle	(dfd
    			
				if (queryGraphicsLayer.graphicProvider.length > 0 && printWithChartCheck.selected == true) { 
					printFromMap();
				} else {
					Alert.show("Click OK to choose a location to save your completed pdf.","PDF Completed", 0, null, PDFAlertClose);
					//pdf.save(Method.REMOTE, "http://137.227.242.85/wetland/Default.aspx", Download.ATTACHMENT, "MM_"+dateArray[1]+dateArray[2]+dateArray[5]+pdfDate.toTimeString()+".pdf", "_self");
				}
				
				//Alert.show("Wait a few seconds for download to begin.","PDF Completed", 0, null, alertClose);
				
				function PDFAlertClose(event:CloseEvent):void
				{
					var file:FileReference = new FileReference();
					var bytes:ByteArray = pdf.save( Method.LOCAL );
					var fileName:String = removeCharacters("NPSHgMap_"+dateArray[2]+dateArray[1]+dateArray[5]+"_"+pdfDate.toTimeString()+".pdf");
					file.save( bytes, fileName );
				}
				
				function removeCharacters(withSpaces:String):String {
					var withoutCharacters:String = "";
					
					withoutCharacters = removeCharacter(withSpaces, " ");
					withoutCharacters = removeCharacter(withoutCharacters, ":");
					
					return withoutCharacters;
				}
				
				function removeCharacter(withChar:String, char:String):String {
					var withoutCharacter:String = "";
					
					var splitString:Array = withChar.split(char);
					
					for (var i:int = 0; i < splitString.length; i++) {
						withoutCharacter += splitString[i];
					}
					
					return withoutCharacter;
				}
				
			}

			private function checkPredMeHgValue(value:String):String {
				var textValue:String;
				
				if (value != "-999" && Number(value) < 0.04) {
					textValue = value + " ng/L*";
				} else {
					textValue = value + " ng/L";
				}
				
				return textValue;
			}

			private function checkValue(attr:String,cons:String):String {
				var text:String;
				if (attr == '-999' || attr == null || attr == " ") {
					text = 'Insufficient Data';
				} else  if (cons == 'sulfate') {
					text = attr + " mg/L as SO4";
				} else if (cons == 'toc') {
					text = attr + " mg/L";
				} else if (cons == 'mehg' && Number(attr) < 0.04) {
					text = attr + " ng/L*";
				} else if (cons == 'mehg') {
					text = attr + " ng/L";
				} else if (cons == 'wetland') {
					text = attr + '%';
				} else if (cons == 'ph') {
					text = attr;
				}
				
				return text;
			}

			public function printCharts(netInt:String,parkInt:String,pmehgChart:VBox,phChart:VBox,sulfateChart:VBox,carbonChart:VBox,wetlandChart:VBox,withMap:Boolean):void
			{
				
				var pdfDate:Date = new Date();
				var dateArray:Array = pdfDate.toString().split(" ");
				var stamp:String = "Printed on " + dateArray[1] + " " + dateArray[2] + ", " + dateArray[5];
				
				if (withMap == false) {
					pdf = new PDF (Orientation.LANDSCAPE, Unit.INCHES, Size.LETTER);
					pdf.addPage();
				} else {
					pdf.addPage();
				}
				
				//Add Text Info ... date, title, networks intersected, parks intersected
				pdf.setFont(italicFont, 8);
				pdf.setXY(0.9, 7.5);
				pdf.addCell(1, 0.15, "http://wim.usgs.gov/MercuryMapper/MercuryMapper.html");
				pdf.setXY(8.75, 7.5);
				pdf.addCell(1, 0.15, stamp);
				pdf.setFont(mainFont, 11);
				pdf.textStyle(new RGBColor (0x000000) );
				pdf.setXY(1, .8);
				pdf.addMultiCell(9, .2, "Hydrologic Unit Code (HUC): " + _queryWindow.data.CAT + " (" + _queryWindow.data.CAT_NAME + ")", 0, "L");
				//pdf.addMultiCell(1.5, .2, _queryWindow.data.infoTitle, 0, "L");
				pdf.setFont(mainFont, 8);
				pdf.setXY(1, 1.2);
				pdf.addMultiCell(9, 0.2, netInt);
				pdf.setXY(1, 1.4);
				pdf.addMultiCell(9, 0.2, parkInt);
				
				//remove all ?s for each consituent label
				
				
				//Add Charts and labels
				pdf.setXY(1.25, 2);
				//pdf.addMultiCell(1.5, 0.175, "pH\n(standard units)", 0, "C");
				pdf.addImage(phChart, null, .75, 2.125, 1.5, 4.5);
				pdf.setXY(2.75, 2);
				//pdf.addMultiCell(1.5, 0.175, "SULFATE\n(mg/L)", 0, "C");
				pdf.addImage(sulfateChart, null, 2.5, 2.125, 1.5, 4.5);
				pdf.setXY(4.25, 2);
				//pdf.addMultiCell(1.5, 0.175, "TOTAL ORGANIC CARBON\n(mg/L)", 0, "C");
				pdf.addImage(carbonChart, null, 4.25, 2.125, 1.5, 4.5);
				pdf.setXY(5.75, 2);
				//pdf.addMultiCell(1.5, 0.175, "WETLAND\n(%)", 0, "C");
				pdf.addImage(wetlandChart, null, 6, 2.125, 1.5, 4.5);
				pdf.setXY(7.25, 2);
				
				//pdf.addMultiCell(1.5, 0.175, "PREDICTED METHYLMERCURY\n(ng/L)", 0, "C");
				pdf.addImage(pmehgChart, null, 7.75, 2, 1.5, 4.5);
				
				//(data.MED_TOC == -999) ? 'n/a' : data.MED_TOC + ' mg/L'
				
				if (_queryWindow.data.FULLMEHG != "-999" && Number(_queryWindow.data.CPREDMEHG) < 0.04) {
					pdf.setFont(mainFont, 6);
					pdf.setXY(1, 7);
					pdf.addMultiCell(9, 0.1, "*A methylmercury reporting level of 0.04 ng/L was established for the USGS Wisconsin Mercury Research Laboratory (WRML) in 2000. Advances in technology since this time have lead to analytical confidence in numbers as low as 0.02 ng/L. All methylmercury model calibration data were analyzed by the USGS WRML.");
					//pdf.addText("*A methylmercury reporting level of 0.04 ng/L was established for the USGS Wisconsin Mercury Research Laboratory (WRML) in 2000. Advances in technology since this time have lead to analytical confidence in numbers as low as 0.02 ng/L. All methylmercury model calibration data were analyzed by the USGS WRML.", 1, 8);
				}
				
				var predmehg:String;
				var med_ph:String;
				var med_sulf:String;
				var med_toc:String;
				var prc_wtld:String;
				
				if (_queryWindow.data.CPREDMEHG == " ") {
					predmehg = 'Insufficient Data';
				} else {
					predmehg = checkPredMeHgValue(_queryWindow.data.CPREDMEHG);
				}
				if (_queryWindow.data.CMED_PH == " ") {
					med_ph = 'Insufficient Data';
				} else {
					med_ph = _queryWindow.data.CMED_PH;
				} 
				if (_queryWindow.data.CMED_SULF == " ") {
					med_sulf = 'Insufficient Data';
				} else {
					med_sulf = _queryWindow.data.CMED_SULF + " mg/L as SO4";
				} 
				if (_queryWindow.data.CMED_TOC == " ") {
					med_toc = 'Insufficient Data';
				} else {
					med_toc = _queryWindow.data.CMED_TOC + " mg/L";
				}
				if (_queryWindow.data.CPRC_WTLD == undefined || _queryWindow.data.CPRC_WTLD == null || _queryWindow.data.CPRC_WTLD == '0') {
					prc_wtld = 'Insufficient Data';
				} else {
					prc_wtld = _queryWindow.data.CPRC_WTLD + "%";
				}
				
				//Add constituent values
				/*pdf.setFont(mainFont, 8);
				pdf.textStyle(new RGBColor (0x000000) );
				pdf.setXY(1, 6.25);
				pdf.addMultiCell(1.8, .25, "Data Summary", 0, "L");
				pdf.setFont(mainFont, 6);
				pdf.textStyle(new RGBColor (0x000000) );
				pdf.setXY(1, 6.5);
				pdf.addMultiCell(1.8, .25, "pH: " + med_ph, 0, "L");
				pdf.setFont(mainFont, 6);
				pdf.textStyle(new RGBColor (0x000000) );
				pdf.setXY(1, 6.65);
				pdf.addMultiCell(1.8, .25, "Sulfate: " + med_sulf, 0, "L");
				pdf.setFont(mainFont, 6);
				pdf.textStyle(new RGBColor (0x000000) );
				pdf.setXY(1, 6.8);
				pdf.addMultiCell(1.8, .25, "Total Organic Carbon: " + med_toc, 0, "L");
				pdf.setFont(mainFont, 6);
				pdf.textStyle(new RGBColor (0x000000) );
				pdf.setXY(1, 6.95);
				pdf.addMultiCell(1.8, .25, "Wetland: " + prc_wtld, 0, "L");
				pdf.setFont(mainFont, 6);
				pdf.textStyle(new RGBColor (0x000000) );
				pdf.setXY(1, 7.1);
				pdf.addMultiCell(1.8, .25, "Predicted MeHg: " + predmehg, 0, "L");*/
				
				//pdf.save(Method.REMOTE, "http://137.227.242.85/wetland/Default.aspx", Download.ATTACHMENT, "MM_Charts_"+dateArray[1]+dateArray[2]+dateArray[5]+pdfDate.toTimeString()+".pdf", "_self");
				
				
				Alert.show("Click OK to choose a location to save your completed pdf.","PDF Completed", 0, null, PDFAlertClose);
				
				function PDFAlertClose(event:CloseEvent):void
				{
					var file:FileReference = new FileReference();
					var bytes:ByteArray = pdf.save( Method.LOCAL );
					var fileName:String = removeCharacters("NPSHgMap_"+dateArray[2]+dateArray[1]+dateArray[5]+"_"+pdfDate.toTimeString()+".pdf");
					file.save( bytes, fileName );
				}
				
				function removeCharacters(withSpaces:String):String {
					var withoutCharacters:String = "";
					
					withoutCharacters = removeCharacter(withSpaces, " ");
					withoutCharacters = removeCharacter(withoutCharacters, ":");
					
					return withoutCharacters;
				}
				
				function removeCharacter(withChar:String, char:String):String {
					var withoutCharacter:String = "";
					
					var splitString:Array = withChar.split(char);
					
					for (var i:int = 0; i < splitString.length; i++) {
						withoutCharacter += splitString[i];
					}
					
					return withoutCharacter;
				}
				
				//Alert.show("Wait a few seconds for download to begin.","PDF Completed");
				
				//Legend determination. Need to add more legend options and improve logic
				/*pdf.setFont(mainFont, 10);
				pdf.textStyle(new RGBColor (0x000000) );
				pdf.setXY(8.25, 2.25);
				pdf.addMultiCell(1.75, 0.175, "No operational layers selected or no legend available", 0, "L");*/
			}
    		
    		private function alertClose(event:CloseEvent):void
    		{
    			//map.extent = mapCurrentExtent;
    			map.centerAt(mapCPoint);//-10644926.307107488,4666939.198981996
    			map.level = mapLevel;
    			mapMask.visible = false;
    			//map.visible = true;
    		}
    		
    		//function to close print form without executing pdf creation.  returns map to previous state.
    		public function closePrintForm():void
    		{
    			titleValText.includeInLayout = false;
				titleValText.visible = false;
				remarksValText.includeInLayout = false;
				remarksValText.visible = false;
				
    			fade(printFormBox,"out",1,0,1000);
    			showAll();
    			
    			map.x = 0;
    			map.y = 0;
    			map.percentHeight = 100;
    			map.percentWidth = 100;
				
				printMode = false;
    			
    			Alert.show("Print cancelled.", "", 0, null, alertClose);
			}

			private function onRightClick():void {
				//Recenter at mouse location
				var cursorLocation:Point = new Point(contentMouseX, contentMouseY);
				map.centerAt(map.toMap(cursorLocation));
				//Zoom out
				map.zoomOut();
			}
			
			public function handleWheel(event:Object): void {	
				var obj:InteractiveObject = null;	
				var objects:Array = getObjectsUnderPoint(new Point(event.x, event.y));	
				for (var i:int = objects.length - 1; i >= 0; i--) {
					if (objects[i] is InteractiveObject) {			
						obj = objects[i] as InteractiveObject;			
						break;		
					} else {			
						if (objects[i] is Shape && (objects[i] as Shape).parent) {				
							obj = (objects[i] as Shape).parent;				
							break;			
						}		
					}	
				}	if (obj) {		
					var mEvent:MouseEvent = new MouseEvent(MouseEvent.MOUSE_WHEEL, true, false, event.x, event.y, obj, event.ctrlKey, event.altKey, event.shiftKey, false, -Number(event.delta));		
					obj.dispatchEvent(mEvent);	
				}
			}

			//Custom USGS info/links popup function that locks the popup into an X-Y position no matter where you click on the icon to display it.
			//keeps the popup window from running off the screen if you click in the left side of the USGS icon.
			protected function showPopUpBox(event:MouseEvent, popupName:String):void
			{
				popUpBoxes[ popupName ] = PopUpManager.createPopUp(this, Group) as Group;
				popUpBoxes[ popupName ].addElement( this[ popupName ] );
				if (popupName == "NPSLinkBox") {
					popUpBoxes[ popupName ].x = 760;
					popUpBoxes[ popupName ].y = 15;
				} else {
					popUpBoxes[ popupName ].x = 20;
					popUpBoxes[ popupName ].y = 20;
				}
			}
			
			
			protected function popUp_mouseOutHandler(event:MouseEvent):void
			{
				var popupName:String = (event.currentTarget as UIComponent).id;
				if (!popUpBoxes[ popupName ].hitTestPoint(event.stageX, event.stageY, true)) {
					PopUpManager.removePopUp(popUpBoxes[ popupName ]);
				}
			}