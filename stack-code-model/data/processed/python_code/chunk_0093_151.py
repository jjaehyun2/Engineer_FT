//05.15.12 - NE - Added two levels of details for zoom slider map levels.
//06.18.10 - NE - Added SCAT data to mapper and identify results.
//06.16.10 - NE - Added functionality to query multiple layers in one identify and show results for all layers.
//05.13.10 - NE - Added new layers.  Fixed bug with max/min available layers box.
//05.12.10 - NE - Added functionality to max/min available layers box
//05.12.10 - NE - Added infoWindow for click on Protected Areas.
//05.12.10 - NE - Added Graphic for incident site.  Added functionality for toggling layers.
//05.12.10 - NE - Added opacity sliders and functionality.  Limited levels of detail.
//05.11.10 - NE - Layout adjustments.  Addition of NOAA spill plume map service.
//05.11.10 - NE - Initial set up.
 /***
 * ActionScript file for template */

import com.esri.ags.FeatureSet;
import com.esri.ags.Graphic;
import com.esri.ags.events.ExtentEvent;
import com.esri.ags.events.MapMouseEvent;
import com.esri.ags.geometry.Extent;
import com.esri.ags.geometry.MapPoint;
import com.esri.ags.geometry.Polygon;
import com.esri.ags.layers.TiledMapServiceLayer;
import com.esri.ags.tasks.supportClasses.IdentifyParameters;
import com.esri.ags.tasks.supportClasses.IdentifyResult;
import com.esri.ags.utils.WebMercatorUtil;
import com.esri.ags.virtualearth.VEGeocodeResult;

import flash.display.StageDisplayState;
import flash.events.Event;
import flash.events.MouseEvent;
import flash.events.TimerEvent;
import flash.utils.Timer;

import gov.usgs.wim.utils.XmlResourceLoader;

import mx.collections.ArrayCollection;
import mx.controls.*;
import mx.controls.sliderClasses.SliderThumb;
import mx.effects.Rotate;
import mx.events.CloseEvent;
import mx.events.FlexEvent;
import mx.rpc.AsyncResponder;
import mx.utils.ObjectProxy;

			private var xmlResourceLoader:XmlResourceLoader = new XmlResourceLoader();
			
			private var protAreasPt:MapPoint;
			
			private var ptGraphic:Graphic;
			private var graphic:Graphic;
			private var polyQ:Polygon;
			
			[Bindable]
			private var genAlpha:Number = 0.7;
			[Bindable]
			private var mapX:Number = 0;
			[Bindable]
			private var mapY:Number = 0;
			[Bindable] 
			private var spillPlumeDesc:Array;
			[Bindable]
			private var transLayer:String = "";
			
			private var operLayersFull:Number = 0;
			private var operLayersTitleHeight:Number = 40;
			private var operLayersExpandHeight:Number; 
			
			[Bindable]
			private var layerExpsMaxHeight:Number;
			
			private var discAlert:Alert;
			
			private var identifyAttr:Object = new Object();
			
			


			/**
    		* load mapper
    		* */
    		private function load():void
    		{   
				
				xmlResourceLoader.load(["locale/en_US", "en_US"]);
				
    			var disclaimer:String = "User Information: This Web Mapper has been compiled from a variety of sources that depict the extent and location of important fish and wildlife resource areas along the coast of the Gulf of Mexico. To help assess the potential effects of the 2010 Deepwater Horizon oil spill, data that intersects a one mile buffer along the shoreline is represented with additional detail. It should be noted that every attempt has been made to display areas as accurately as possible, however due to the limitations of scale this should be used to approximate relative location and distribution of resource areas important to fish and wildlife resources.\n\nIt is not the purpose or intent of this application to be used for any site specific study or quantitative measure. Persons intending to engage in activities involving any fish and wildlife resource area depicted here should seek the advice of the appropriate Federal, State or local resource agencies. \n\nFor additional information see on-line resources at: http://www.fws.gov/";
    			discAlert = Alert.show(disclaimer, "", 0, null, initAlertClose);
    			
    			//code to adjust height of layer list and explanations for different screen sizes
    			//use only if needed
    			layerExpsMaxHeight = application.height - 456;
	    		
    			slider.addEventListener(MouseEvent.ROLL_OUT, sliderFadeOut, false);
    			
    			//var lodsTemp:Array = map.lods.reverse();
    			//lodsTemp.length = 14;
    			//lodsTemp.reverse();
    			//map.lods = lodsTemp;
    			//map.extent = init;
    			
    			var dwhiGraphic:Graphic = new Graphic();
    			var dwhiPoint:MapPoint = new MapPoint(-9839367.426,3341935.530,map.spatialReference);
    			dwhiGraphic.geometry = dwhiPoint;
    			dwhiGraphic.symbol = dwhiSym;
    			
    			DWHILayer.add(dwhiGraphic);
    			
    			//var name:String= scat.layerInfos[0].name;
    			
    		}
				
    		
    		//Handles click requests for map layer info
    		private function onMapClick(event:MapMouseEvent):void
    		{
    			
    			identifyAttr = new Object();
    			
    			queryGraphicsLayer.clear();
    			infoGraphicsLayer.clear();
    			
    			protAreasPt = event.mapPoint;
    			
    			if (protAreas.visible) {
					protAreasQuery.geometry = protAreasPt;
					protAreasTask.execute( protAreasQuery, new AsyncResponder(infoSingleResult, infoFault, "protAreas"));
    			}
				
				if (critHab.visible) {
					critHabQuery.geometry = protAreasPt;
					critHabTask.execute( critHabQuery, new AsyncResponder(infoSingleResult, infoFault, "critHab"));
				}
				
				if (hurricane.visible) {
					var hurricaneParams:com.esri.ags.tasks.supportClasses.IdentifyParameters = new IdentifyParameters();
					hurricaneParams.returnGeometry = true;
					hurricaneParams.layerOption = "all";
					hurricaneParams.layerIds = [0];
					hurricaneParams.width = map.width;
					hurricaneParams.height = map.height;
					hurricaneParams.geometry = event.mapPoint;
					hurricaneParams.tolerance = 1;
					hurricaneParams.mapExtent = map.extent;
					hurricaneParams.spatialReference = map.spatialReference;										
			    	 				
	    			var hurricaneTask:IdentifyTask = hurricaneTask;
	    			hurricaneTask.execute( hurricaneParams, new AsyncResponder(hurricaneResult, hurricaneFault) );
				}
				
				if (scat.visible) {
					var scatParams:IdentifyParameters = new IdentifyParameters();
					scatParams.returnGeometry = true;
					scatParams.layerOption = "all";
					scatParams.layerIds = [0];
					scatParams.width = map.width;
					scatParams.height = map.height;
					scatParams.geometry = event.mapPoint;
					scatParams.tolerance = 1;
					scatParams.mapExtent = map.extent;
					scatParams.spatialReference = map.spatialReference;										
			    	 				
	    			var scatTask:IdentifyTask = scatTask;
	    			scatTask.execute( scatParams, new AsyncResponder(scatResult, scatFault) );
				}
			}
			
			private function onExtentChange(event:ExtentEvent):void            
    		{
    			//Alert.show(map.extent.toString());
    		}
    		
    		/* function for feedback of lat/lng of current mouse position */
    		private function mouseMove(event:MouseEvent):void
    		{
    			if (map.loaded) {
    				var mapPoint:MapPoint = map.toMapFromStage(event.stageX, event.stageY);
    				var mapPt:MapPoint = WebMercatorUtil.webMercatorToGeographic(mapPoint) as MapPoint;
    				mapX = mapPt.x;
    				mapY = mapPt.y;
    			}
    		}
    		
    		/* Query tooltip methods */
    		
    	   	private function infoSingleResult(featureSet:com.esri.ags.FeatureSet, key:String):void
			{
				
				if (featureSet.features.length > 0) {
					
					if (key == "protAreas") {
            			var protAreasAttr:Object = featureSet.features[0].attributes;
            			var polyQG:Graphic = featureSet.features[0];
            			polyQ = polyQG.geometry as Polygon;
	            		if (protAreasAttr.Class_Desc == 1000) {
	            			protAreasAttr.Class_Desc = "Federal Land";
	            		} else if (protAreasAttr.Class_Desc == 3000) {
	            			protAreasAttr.Class_Desc = "State Land";
	            		} else if (protAreasAttr.Class_Desc == 6000) {
	            			protAreasAttr.Class_Desc = "Non-Governmental Organization";
	            		}
	            		identifyAttr.Parcel_Nam = protAreasAttr.Parcel_Nam;
	            		identifyAttr.Class_Desc = protAreasAttr.Class_Desc;
	            		identifyAttr.Website = protAreasAttr.Website;
	            		var protAreasGraphic:Graphic = featureSet.features[0];
	            		protAreasGraphic.symbol = protAreasQuerySym;
	            		queryGraphicsLayer.add(protAreasGraphic);
	            		infoGraphicsLayer.clear();
	            		ptGraphic = new Graphic(protAreasPt, singleGraphicSym);
	            		ptGraphic.attributes = new ObjectProxy(identifyAttr);
	            		infoGraphicsLayer.add(ptGraphic);
	            	} else if (key == "critHab") {
            			var critHabAttr:Object = featureSet.features[0].attributes;
            			identifyAttr.COMNAME = critHabAttr.COMNAME;
            			var critHabGraphic:Graphic = featureSet.features[0];
            			critHabGraphic.symbol = critHabQuerySym;
            			queryGraphicsLayer.add(critHabGraphic);
            			infoGraphicsLayer.clear();
        				ptGraphic = new Graphic(protAreasPt, singleGraphicSym);
            			ptGraphic.attributes = new ObjectProxy(identifyAttr);
            			infoGraphicsLayer.add(ptGraphic);
            		} 
            		
            	}
					
			}
			
			private function infoFault(info:Object, key:String):void
    		{
    			Alert.show(info.toString()+key);
    		}	
    		
    		private function hurricaneResult(results:Array, clickGraphic:Graphic = null):void
			{
				if (results && results.length > 0) {
					var result:IdentifyResult = results[0];         
					var hurricaneAttr:Object = result.feature.attributes;
        			identifyAttr.NAME = hurricaneAttr.NAME;
        			var hurricaneGraphic:Graphic = result.feature;
        			hurricaneGraphic.symbol = hurricaneQuerySym;
        			queryGraphicsLayer.add(hurricaneGraphic);
        			infoGraphicsLayer.clear();
    				ptGraphic = new Graphic(protAreasPt, singleGraphicSym);
        			ptGraphic.attributes = new ObjectProxy(identifyAttr);
        			infoGraphicsLayer.add(ptGraphic);
				}
			}
			
			private function hurricaneFault(error:Object, clickGraphic:Graphic = null):void
    		{
    			trace(error.toString());
    		}   	
    		
    		private function scatResult(results:Array, clickGraphic:Graphic = null):void
			{
				if (results && results.length > 0) {
					var result:com.esri.ags.tasks.supportClasses.IdentifyResult = results[0];         
					var scatAttr:Object = result.feature.attributes;
        			identifyAttr.Oiling_Category = scatAttr.Oiling_Category;
        			identifyAttr.Survey_Date = scatAttr.Survey_Date;
        			var scatGraphic:Graphic = result.feature;
        			scatGraphic.symbol = scatQuerySym;
        			queryGraphicsLayer.add(scatGraphic);
        			infoGraphicsLayer.clear();
    				ptGraphic = new Graphic(protAreasPt, singleGraphicSym);
        			ptGraphic.attributes = new ObjectProxy(identifyAttr);
        			infoGraphicsLayer.add(ptGraphic);
				}
			}
			
			private function scatFault(error:Object, clickGraphic:Graphic = null):void
    		{
    			trace(error.toString());
    		}   		
    		   
    		/* End query tooltip methods */
		
		
			private function toggleLayers(event:Event):void
    		{
    			/* if (spillPlumeCB.selected == true) {
    				spillPlume.visible = true;            
    			} else {
    				spillPlume.visible = false;
    			} */
    			if (critHabCB.selected == true) {
    				critHab.visible = true;            
    			} else {
    				critHab.visible = false;
    			}
    			if (hurricaneCB.selected == true) {
    				hurricane.visible = true;            
    			} else {
    				hurricane.visible = false;
    			}
    			if (protAreasCB.selected == true) {
    				protAreas.visible = true;
    			} else {
    				protAreas.visible = false;
    				queryGraphicsLayer.clear();
    				infoGraphicsLayer.clear();
    			}
    			if (birdAreasCB.selected == true) {
    				birdAreas.visible = true;
    			} else {
    				birdAreas.visible = false;
    			}
    			if (coastBarrierCB.selected == true) {
    				cbrs.visible = true;
    			} else {
    				cbrs.visible = false;
    			}
    			if (wetlandsCB.selected == true) {
    				wetlands.visible = true;
    			} else {
    				wetlands.visible = false;
    			}
    			if (coastWetCB.selected == true) {
    				coastWet.visible = true;
    			} else {
    				coastWet.visible = false;
    			}
    			if (landConserveCB.selected == true) {
    				landConserve.visible = true;
    			} else {
    				landConserve.visible = false;
    			}
    			
    		}
    			
    		    		
    		private function baseSwitch(event:FlexEvent):void            
    		{                
	    		var tiledLayer:TiledMapServiceLayer = event.target as TiledMapServiceLayer;                
	    	}
    		
    		/* Geo-coding methods */
    		private function geoCode():void
    		{
    			veGeocoder.addressToLocations(geoCodeVal.text, new AsyncResponder(onResult, onFault));
    			function onResult(results:Array, token:Object = null):void
    			{
    				if (results.length > 0)
    				{
    					var veResult:VEGeocodeResult = results[0];
    					map.extent = WebMercatorUtil.geographicToWebMercator(veResult.bestView) as Extent;
    					//map.extent = veResult.bestView;
    				}
    				else
    				{
    					Alert.show("Could not find " + geoCodeVal.text + ". Please try again");
    				}
    			}
    		}
    		
    		private function onFault(info:Object, token:Object = null):void
    		{
    			Alert.show("Error: " + info.toString(), "problem with Locator");
    		}
    		
    		/* End geo-coding methods */
    		
    		
    		
    		/* Full screen methods */
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
    		
    		/* End full screen methods */
    		
    	
    		public function collapseLegend(event:MouseEvent):void {
    			
	    			layerList.visible = !layerList.visible;
	    			layerExps.visible = !layerExps.visible;
	    			if (!layerList.visible) {
	    				layerList.scaleY = 0;
	    				layerExps.scaleY = 0;
	    			} else {
	    				layerList.scaleY = 1;
	    				layerExps.scaleY = 1;
	    			} 
    			
    		}
    		
    		
    		/* public function toggleOverlays():void {
    			if (header.visible) {
    				header.visible = false;
	    			headerLogo.visible = false;
					baseLayers.visible = false;
					navigation.visible = false;
					geocoder.visible = false;
					operationLayers.visible = false;
					printButton.visible = false;
    			} else {
    				header.visible = true;
    				headerLogo.visible = true;
					baseLayers.visible = true;
					navigation.visible = true;
					geocoder.visible = true;
					operationLayers.visible = true;
					printButton.visible = true;					
    			}
    		} */
    		
    		
    		//function to set up mapper for PDF creation and print job
    		public function startPrint(pEvt:MouseEvent):void
    		{
    			//toggleOverlays();
				//printFormBox.fadeIn(1000);				
											
				//Shrink to half the view size
				/*var newWidth:Number = map.width/2;
				var newHeight:Number = map.height/2;
				map.x = (map.width-newWidth)/2;
				map.y = (map.height-newHeight)/2;
				map.percentHeight = 50;
				map.percentWidth = 50;*/
									
				Alert.show("Position and scale the map in the window provided to ensure the printed product will contain the desired area.");
								
			}
			
			private function initAlertClose(event:CloseEvent):void
    		{
    			mapMask.visible = false;
    		}
			
			//Function to close print form without executing pdf creation. Returns map to previous state.
    		public function printFormClose():void
    		{
    			//toggleOverlays(); 
    			
    			map.x = 0;
    			map.y = 0;
    			map.percentHeight = 100;
    			map.percentWidth = 100;
    		}
    		
    		private function transAdjust(layer:String):void {
    			map.getLayer(transLayer).alpha = transSlide.value;
    		}
    		
    		private function sliderFadeIn(event:MouseEvent):void {
    			transSlide.value = map.getLayer(transLayer).alpha;
    			slider.x = event.stageX-slider.width+10;
    			slider.y = event.stageY-slider.height+10;
    			slider.visible = true;
			}
    		
    		private function sliderFadeOut(event:MouseEvent):void {
				if (!(event.relatedObject is mx.controls.sliderClasses.SliderThumb) &&  (!event.buttonDown)) {
					slider.visible = false;
				} 
			}
			
			private function protectedAreaLinksShow(event:MouseEvent):void {
				protectedAreaLinks.y = event.stageY - 5;
				protectedAreaLinks.x = event.stageX - 425;
				protectedAreaLinks.visible = true;
			}
			
			
			private function maxMin():void 
    		{
    			layerList.visible = !layerList.visible;
    			layerExps.visible = !layerExps.visible;
    			if (!layerList.visible) {
    				layerList.scaleY = 0;
    				layerExps.scaleY = 0;
    				maxMinImg.source = "assets/images/plus.png";
    				rotateMaxMin();
    				operationLayers.setStyle('paddingBottom', 0);
    			} else {
    				layerList.scaleY = 1;
    				layerExps.scaleY = 1;
    				maxMinImg.source = "assets/images/minus.png";
    				rotateMaxMin();
    				operationLayers.setStyle('paddingBottom', 10);
    			}
    			timer();
    		}
    		
    		private function timer():void {
    			var timer:Timer = new Timer(30, 1);
    			
    			timer.addEventListener(TimerEvent.TIMER_COMPLETE, timerComp);
    			
    			timer.start();
    		}
    		
    		private function timerComp(event:TimerEvent):void {
    			layerExps.maxHeight = layerExpsMaxHeight;
    		}
    		
    		private function rotateMaxMin():void 
    		{
    			var rotMaxMin:Rotate = new Rotate();
    			rotMaxMin.target = maxMinImg;
    			rotMaxMin.angleFrom = 0;
    			rotMaxMin.angleTo = 360;
    			rotMaxMin.duration = 300;
    			rotMaxMin.play();
    		}