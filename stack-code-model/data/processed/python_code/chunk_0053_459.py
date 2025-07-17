package screens.map {
	
	import application.AssetsLoader;
	import application.utils.MyCanvas;
	import application.utils.StaticGUI;
	import cz.j4w.map.MapLayerOptions;
	import cz.j4w.map.MapOptions;
	import cz.j4w.map.events.MapEvent;
	import cz.j4w.map.geo.GeoMap;
	import cz.j4w.map.geo.GeoUtils;
	import cz.j4w.map.geo.Maps;
	import feathers.controls.Label;
	import feathers.controls.LayoutGroup;
	import feathers.core.FeathersControl;
	import feathers.layout.AnchorLayout;
	import feathers.layout.AnchorLayoutData;
	import feathers.layout.HorizontalAlign;
	import feathers.layout.VerticalAlign;
	import flash.events.Event;
	import flash.events.GeolocationEvent;
	import flash.events.StatusEvent;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.sensors.Geolocation;
	import starling.core.Starling;
	import starling.display.Image;
	import starling.display.Quad;
	import starling.text.TextFormat;
	import starling.textures.Texture;
	import starling.utils.Align;
	

	public class ScreenMap extends FeathersControl {
		
		private var mapOptions:MapOptions;
		private var geoMap:GeoMap;
		private var googleMaps:MapLayerOptions;
		private var contentGroup:LayoutGroup;
		private var geo:Geolocation;
		
		private var myMarker:Image;
		private var myMarkerTexture:Texture;
		
		private var addressStyle:TextFormat;
		private var cityStyle:TextFormat;
		private var distStyle:TextFormat;
		
		private var labelAddress:Label;
		private var labelCity:Label;
		private var labelDistance:Label;
		private var fromWorkTime:Label;
		private var fromWorkLab:Label;
		private var toWorkTime:Label;
		private var toWorkLab:Label;
		
		private var line:MyCanvas;
		private var line2:MyCanvas;
		
		private var mapScale:Number;
		
		public function ScreenMap() {
			super();
		}
		
		
		override public function dispose():void {
			
			
			if (geo) {
				geo.removeEventListener(GeolocationEvent.UPDATE, geoUpdateHandler);
				geo.removeEventListener(StatusEvent.STATUS, geoStatusHandler);
			}
			if (geoMap) {
				geoMap.removeEventListener(MapEvent.MARKER_TRIGGERED, onGeoMapMarkerTriggered);
				StaticGUI._safeRemoveChildren(geoMap, true);
			}
			
			if (contentGroup) StaticGUI._safeRemoveChildren(contentGroup, true);
			if (labelAddress) StaticGUI._safeRemoveChildren(labelAddress, true);
			if (labelCity) StaticGUI._safeRemoveChildren(labelCity, true);
			if (labelDistance) StaticGUI._safeRemoveChildren(labelDistance, true);
			if (fromWorkTime) StaticGUI._safeRemoveChildren(fromWorkTime, true);
			if (fromWorkLab) StaticGUI._safeRemoveChildren(fromWorkLab, true);
			if (toWorkTime) StaticGUI._safeRemoveChildren(toWorkTime, true);
			if (toWorkLab) StaticGUI._safeRemoveChildren(toWorkLab, true);
			if (line) StaticGUI._safeRemoveChildren(line, true);
			if (line2) StaticGUI._safeRemoveChildren(line2, true);
			if (myMarker) StaticGUI._safeRemoveChildren(myMarker, true);
			if (myMarkerTexture) StaticGUI._safeRemoveChildren(myMarkerTexture, true);
			
			myMarkerTexture = null;
			myMarker = null;
			
			addressStyle = null;
			cityStyle = null;
			distStyle = null;
			
			contentGroup = null;
			labelAddress = null;
			labelCity = null;
			labelDistance = null;
			fromWorkTime = null;
			fromWorkLab = null;
			toWorkTime = null;
			toWorkLab = null;
			line = null;
			line2 = null;
			mapOptions = null;
			geoMap = null;
			googleMaps = null;
			
			super.dispose();
		}
		
		override protected function initialize():void {
			super.initialize();
			
			
			addressStyle = new TextFormat;
			addressStyle.font = '_bpgArialRegular';
			addressStyle.size = Settings._getIntByDPI(24);
			addressStyle.color = 0x575757;
			
			cityStyle = new TextFormat;
			cityStyle.font = '_bpgArialRegular';
			cityStyle.size = Settings._getIntByDPI(24);
			cityStyle.color = 0x929394;
			
			distStyle = new TextFormat;
			distStyle.font = '_bpgArialRegular';
			distStyle.size = Settings._getIntByDPI(24);
			distStyle.horizontalAlign = HorizontalAlign.LEFT;
			distStyle.color = 0x186c97;
			
			var layout:AnchorLayout = new AnchorLayout();
			contentGroup = new LayoutGroup;
			contentGroup.layout = layout;
			contentGroup.y = Settings._getIntByDPI(130);
			addChild(contentGroup);
			
			var lineSize:uint = Settings._getIntByDPI(1);
			if (lineSize < 1) lineSize = 1;
			
			if (!line) {
				line = new MyCanvas;
				
				line.lineStyle(lineSize, 0xd5dce0);
				line.lineTo(0, 0);
				line.lineTo(stage.stageWidth, 0);
				line.endFill();
				line.y = Settings._getIntByDPI(255);
				contentGroup.addChild(line);
			}
			
			if (!line2) {
				line2 = new MyCanvas;
				
				line2.lineStyle(lineSize, 0xd5dce0);
				line2.lineTo(0, 0);
				line2.lineTo(0, Settings._getIntByDPI(23));
				line2.endFill();
				line2.y = Settings._getIntByDPI(59);
				line2.x = stage.stageWidth - Settings._getIntByDPI(150);
				contentGroup.addChild(line2);
			}
			
			
			labelAddress = StaticGUI._addLabel(contentGroup, "დავით აღმაშენებლის გამზ. №44", addressStyle);
			labelAddress.layoutData = new AnchorLayoutData(Settings._getIntByDPI(62), NaN, NaN, Settings._getIntByDPI(35));
			
			labelCity = StaticGUI._addLabel(contentGroup, "თბილისი", cityStyle);
			labelCity.layoutData = new AnchorLayoutData(Settings._getIntByDPI(95), NaN, NaN, Settings._getIntByDPI(35));
			
			labelDistance = StaticGUI._addLabel(contentGroup, int(Math.random()*1588).toString()+" მ", distStyle);
			labelDistance.layoutData = new AnchorLayoutData(Settings._getIntByDPI(62), Settings._getIntByDPI(133) - labelDistance.width, NaN, NaN);
			
			fromWorkLab = StaticGUI._addLabel(contentGroup, Settings._mui['map_local_working_from'][Settings._lang], addressStyle);
			fromWorkLab.layoutData = new AnchorLayoutData(Settings._getIntByDPI(150), NaN, NaN, Settings._getIntByDPI(35));
			
			fromWorkTime = StaticGUI._addLabel(contentGroup, "10.00-17.00", addressStyle);
			fromWorkTime.layoutData = new AnchorLayoutData(Settings._getIntByDPI(150), NaN, NaN, Settings._getIntByDPI(185));
			
			toWorkLab = StaticGUI._addLabel(contentGroup, Settings._mui['day_5'][Settings._lang]+':', addressStyle);
			toWorkLab.layoutData = new AnchorLayoutData(Settings._getIntByDPI(184), NaN, NaN, Settings._getIntByDPI(35));
			
			toWorkTime = StaticGUI._addLabel(contentGroup, "10.00-14.00", addressStyle);
			toWorkTime.layoutData = new AnchorLayoutData(Settings._getIntByDPI(184), NaN, NaN, Settings._getIntByDPI(185));
			
			
			mapScale = Starling.current.contentScaleFactor; // use 1 for non-retina displays
			GeoUtils.scale = mapScale;
			
			myMarkerTexture = AssetsLoader._asset.getTexture('map_user_pin.png');
			
			myMarker = new Image(myMarkerTexture);
			myMarker.alignPivot(Align.CENTER, Align.CENTER);
			
			
			
			//referance http://stackoverflow.com/questions/24797998/detect-the-closest-to-the-user-point
			if (Geolocation.isSupported) {
				geo = new Geolocation();
				if (!geo.muted)  { 
                    geo.addEventListener(GeolocationEvent.UPDATE, geoUpdateHandler);
                } 
				geo.addEventListener(StatusEvent.STATUS, geoStatusHandler);
			} else {
				if (!geoMap) {
					initMap(44.777580, 41.726495);
				}
				geoMap.addMarkerLongLat("myMarker", 44.777580, 41.726495, myMarker);	
			}

		}
		
		private function geoStatusHandler(e:Event):void {
			if (geo.muted)
                geo.removeEventListener(GeolocationEvent.UPDATE, geoUpdateHandler);
            else
                geo.addEventListener(GeolocationEvent.UPDATE, geoUpdateHandler);
		}
		
		private function geoUpdateHandler(e:GeolocationEvent):void{
			//embeddedIconPoi.latLng = new LatLng(e.latitude, e.longitude);
			if (!geoMap) {
				initMap(e.longitude, e.latitude);
			}
			
			geoMap.addMarkerLongLat("myMarker", e.longitude, e.latitude, myMarker);
		}
		
		private const RADIUS_OF_EARTH_IN_MILES:int = 3963;
		private const RADIUS_OF_EARTH_IN_FEET:int = 20925525;
		private const RADIUS_OF_EARTH_IN_KM:int = 6378;
		private const RADIUS_OF_EARTH_IN_M:int = 6378000;

		private function distanceBetweenCoordinates(lat1:Number,lon1:Number,
												lat2:Number,lon2:Number,
												units:String="miles"):Number{

			var R:int = RADIUS_OF_EARTH_IN_MILES;
			if (units == "km"){
				R = RADIUS_OF_EARTH_IN_KM;
			}
			if (units == "meters"){
				R = RADIUS_OF_EARTH_IN_M;
			}
			if (units =="feet"){
				R= RADIUS_OF_EARTH_IN_FEET;
			}

			var dLat:Number = (lat2-lat1) * Math.PI/180;
			var dLon:Number = (lon2-lon1) * Math.PI/180;

			var lat1inRadians:Number = lat1 * Math.PI/180;
			var lat2inRadians:Number = lat2 * Math.PI/180;

			var a:Number = Math.sin(dLat/2) * Math.sin(dLat/2) + 
							   Math.sin(dLon/2) * Math.sin(dLon/2) * 
							   Math.cos(lat1inRadians) * Math.cos(lat2inRadians);
			var c:Number = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
			var d:Number = R * c;

			return d;
		}
		
		private function initMap(long:Number, lat:Number):void {
			
			mapOptions = new MapOptions();
			mapOptions.initialCenter = new Point(long, lat);
			mapOptions.initialScale = 1 / 32 / mapScale;
			mapOptions.disableRotation = true;
			mapOptions.minimumScale = 1 / 64 / mapScale;
			mapOptions.maximumScale = 1 / 1 / mapScale;
			/*mapOptions.movementBounds = new Rectangle();
			mapOptions.movementBounds.left = GeoUtils.lon2x(-2.96842);
			mapOptions.movementBounds.top = GeoUtils.lat2y(43.28071);
			mapOptions.movementBounds.right = GeoUtils.lon2x(-2.90044);
			mapOptions.movementBounds.bottom = GeoUtils.lat2y(43.23870);*/
			
			geoMap = new GeoMap(mapOptions);
			geoMap.setSize(stage.stageWidth, stage.stageHeight - Settings._getIntByDPI(487)); // header and footer height
			geoMap.y = Settings._getIntByDPI(385);
			addChild(geoMap);
			
			googleMaps = Maps.GOOGLE_MAPS_SCALED(mapScale);
			googleMaps.notUsedZoomThreshold = 1;
			geoMap.addLayer("googleMaps", googleMaps);
			
			
			
			/*for (var i:int = 0; i < 100; i++) {
				var image:Image = new Image(markerTexture);
				image.alignPivot(HorizontalAlign.CENTER, VerticalAlign.BOTTOM);
				
				geoMap.addMarkerLongLat("marker" + i, mapOptions.initialCenter.x + .1 - Math.random() * .2, mapOptions.initialCenter.y + .1 - Math.random() * .2, image);
			}*/
			geoMap.addEventListener(MapEvent.MARKER_TRIGGERED, onGeoMapMarkerTriggered);
		}
		
		private function onGeoMapMarkerTriggered(e:MapEvent):void {
			trace(e.target);
		}
	}
}