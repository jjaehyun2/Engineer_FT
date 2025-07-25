﻿import gfx.io.GameDelegate;
import gfx.ui.NavigationCode;
import gfx.ui.InputDetails;
import gfx.managers.FocusHandler;
import gfx.managers.InputDelegate;

import Map.LocalMap;
import Map.LocationFinder;
import Map.Legend;
import Shared.ButtonChange;
import Shared.GlobalFunc;

import skyui.components.ButtonPanel;
import skyui.components.MappedButton;
import skyui.defines.Input;

/*
	A few comments:
	* The map menu set up somewhat complicated. There's a lot of @API, so changing that was not an option.
	* The top-level clip contains 3 main components, and the bottombar.
		Root
		+-- MapMenu (aka WorldMap. this class)
		+-- LocalMap
		+-- LocationFinder (new)
		+-- BottomBar
	* To prevent WSAD etc from zooming while the location finder is active, we have to enter a fake local map mode.
	* LocalMap handles the overall state of the menu: worldmap(aka hidden), localmap, locationfinder
	* To open the LocationFinder, we send a request to localmap, which prepares the fake mode, then shows the location finder.
	* For handleInput, MapMenu acts as the root.
	* The bottombar changes happen in LocalMap when the mode is changed.
	* To detect E as NavEquivalent.ENTER, we have to enable a custom fixup in InputDelegate.
	* To receive mouse wheel input for the scrolling list, we need skse.EnableMapMenuMouseWheel(true).
	* Oh, and the localmap reuses this class somehow for its IconView...
 */

class Map.MapMenu
{
	#include "../../version.as"
	
  /* CONSTANTS */
  
	private static var REFRESH_SHOW: Number = 0;
	private static var REFRESH_X: Number = 1;
	private static var REFRESH_Y: Number = 2;
	private static var REFRESH_ROTATION: Number = 3;
	private static var REFRESH_STRIDE: Number = 4;
	private static var CREATE_NAME: Number = 0;
	private static var CREATE_ICONTYPE: Number = 1;
	private static var CREATE_UNDISCOVERED: Number = 2;
	private static var CREATE_STRIDE: Number = 3;
	private static var MARKER_CREATE_PER_FRAME: Number = 10;
	
	
  /* PRIVATE VARIABLES */
  
	private var _markerList: Array;
	
	private var _bottomBar: MovieClip;

	private var _nextCreateIndex: Number = -1;
	private var _mapWidth: Number = 0;
	private var _mapHeight: Number = 0;
	
	private var _mapMovie: MovieClip;
	private var _markerDescriptionHolder: MovieClip;
	private var _markerContainer: MovieClip;
	
	private var _selectedMarker: MovieClip;
	
	private var _platform: Number;
	
	private var _localMapButton: MovieClip;
	private var _journalButton: MovieClip;
	private var _playerLocButton: MovieClip;
	private var _findLocButton: MovieClip;
	private var _searchButton: MovieClip;
	private var _legendButton: MovieClip;
	
	private var _locationFinder: LocationFinder;
	private var _legend: Legend;
	
	private var _localMapControls: Object;
	private var _journalControls: Object;
	private var _zoomControls: Object;
	private var _playerLocControls: Object;
	private var _setDestControls: Object;
	private var _findLocControls: Object;
	private var _toggleLegendControls: Object;
	//                                                                   20                                      40                                      60            67
	private var showMarker:Array= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
	private var LegendMarkersIds=[67,73,76,90,91,84,70,78];
	private var LegendMarkersNames=["Town","Farms & Mines","Dungeons & Ruins","Village","Shrine","City","Camps & Forts","Others"];
	private var LegendMarkersEnabled=[1,1,1,1,1,1,1,1];
	private var test:Number;
  /* STAGE ELEMENTS */
  
  	public var locationFinderFader: MovieClip;
	public var LegendFader: MovieClip;
	public var localMapFader: MovieClip;
	

  /* PROPERTIES */

	// @API
	public var LocalMapMenu: MovieClip;

	// @API
	public var MarkerDescriptionObj: MovieClip;
	
	// @API
	public var PlayerLocationMarkerType: Number;
	
	// @API
	public var MarkerData: Array;
	
	// @API
	public var YouAreHereMarker: MovieClip;
	
	// @GFx
	public var bPCControlsReady: Boolean = true;


  /* INITIALIZATION */

	public function MapMenu(a_mapMovie: MovieClip)
	{
		_mapMovie = a_mapMovie == undefined ? _root : a_mapMovie;
		_markerContainer = _mapMovie.createEmptyMovieClip("MarkerClips", 1);
		
		_markerList = new Array();
		_nextCreateIndex = -1;
		test=0;
		LocalMapMenu = _mapMovie.localMapFader.MapClip;
		
		_locationFinder = _mapMovie.locationFinderFader.locationFinder;
		_legend = _mapMovie.legendFader.legend;
		_legend.setVisibilityArray(LegendMarkersEnabled);
        _legend.setMapMenu(this);
		_bottomBar = _root.bottomBar;
		
		if (LocalMapMenu != undefined) {
			LocalMapMenu.setBottomBar(_bottomBar);
			LocalMapMenu.setLocationFinder(_locationFinder);
			LocalMapMenu.setLegend(_legend);
			Mouse.addListener(this);
			FocusHandler.instance.setFocus(this,0);
		}
		
		_markerDescriptionHolder = _mapMovie.attachMovie("DescriptionHolder", "markerDescriptionHolder", _mapMovie.getNextHighestDepth());
		_markerDescriptionHolder._visible = false;
		_markerDescriptionHolder.hitTestDisable = true;
		
		MarkerDescriptionObj = _markerDescriptionHolder.Description;
		
		Stage.addListener(this);
		
		initialize();
	}
	
	public function InitExtensions(): Void
	{
		skse.EnableMapMenuMouseWheel(true);
	}
	
	private function initialize(): Void
	{		
	       
		onResize();

		if (_bottomBar != undefined)
			_bottomBar.swapDepths(4);
		
		if (_mapMovie.localMapFader != undefined) {
			_mapMovie.localMapFader.swapDepths(3);
			_mapMovie.localMapFader.gotoAndStop("hide");
		}
		
		if (_mapMovie.locationFinderFader != undefined) {
			_mapMovie.locationFinderFader.swapDepths(6);
		}
		
				
		if (_mapMovie.legendFader != undefined) {
			_mapMovie.legendFader.swapDepths(7);
		}
		
		
		
		GameDelegate.addCallBack("RefreshMarkers", this, "RefreshMarkers");
		GameDelegate.addCallBack("SetSelectedMarker", this, "SetSelectedMarker");
		GameDelegate.addCallBack("ClickSelectedMarker", this, "ClickSelectedMarker");
		GameDelegate.addCallBack("SetDateString", this, "SetDateString");
		GameDelegate.addCallBack("ShowJournal", this, "ShowJournal");

	}
	
	
  /* PUBLIC FUNCTIONS */

	// @API
	public function SetNumMarkers(a_numMarkers: Number): Void
	{
		if (_markerContainer != null)
		{
			_markerContainer.removeMovieClip();
			_markerContainer = _mapMovie.createEmptyMovieClip("MarkerClips", 1);
			onResize();
		}
		
		delete _markerList;
		_markerList = new Array(a_numMarkers);
		
		Map.MapMarker.topDepth = a_numMarkers;

		_nextCreateIndex = 0;
		SetSelectedMarker(-1);
		
		_locationFinder.list.clearList();
		_locationFinder.setLoading(true);
		_legend.list.clearList();
		_legend.setLoading(true);
	}

	// @API
	public function GetCreatingMarkers(): Boolean
	{
		return _nextCreateIndex != -1;
	}

	// @API
	public function CreateMarkers(): Void
	{		
	var i:Number;
		
		
		if (_nextCreateIndex == -1 || _markerContainer == null)
			return;
			
		var i = 0;
		var idx = _nextCreateIndex * CREATE_STRIDE;
		
		var markersLen = _markerList.length;
		var dataLen = MarkerData.length;
			
		while (_nextCreateIndex < markersLen && idx < dataLen && i < MARKER_CREATE_PER_FRAME) {
			var markerType = MarkerData[idx + CREATE_ICONTYPE];
			if (showMarker[markerType]){
				var markerName = MarkerData[idx + CREATE_NAME];
				var isUndiscovered = MarkerData[idx + CREATE_UNDISCOVERED];
			
				var mapMarker: MovieClip = _markerContainer.attachMovie("MapMarker", "Marker" + _nextCreateIndex, _nextCreateIndex, {markerType: markerType, isUndiscovered: isUndiscovered});
				_markerList[_nextCreateIndex] = mapMarker;
			
				if (markerType == PlayerLocationMarkerType) {
				YouAreHereMarker = mapMarker.IconClip;
				}
				mapMarker.index = _nextCreateIndex;
				mapMarker.label = markerName;
				mapMarker.Type=markerType;
			
				// Adding the markers directly so we don't have to create data obidxects.
				// NOTE: Make sure internal entry properties (mappedIndex etc) dont conflict with marker properties
				if (0 < markerType && markerType < Map.LocationFinder.TYPE_RANGE) {
					_locationFinder.list.entryList.push(mapMarker);

				}
			
				
					_nextCreateIndex++;

				
			}
			i++;
			idx += CREATE_STRIDE;
		}
				

		_locationFinder.list.InvalidateData();
	   
		if (_nextCreateIndex >= markersLen) {
			_locationFinder.setLoading(false);
			_legend.setLoading(false);
			_nextCreateIndex = -1;
		}
		
		_legend.list.clearList();
		 var j : Number;
	        for (j =0;j<8;j++){
				if (j==5){
					var mapMarker: MovieClip = _legend.attachMovie("MapMarker", "Marker" +  1000+j,  j, {markerType:LegendMarkersIds[j], isUndiscovered: (LegendMarkersEnabled[j])});
				}
				else {
					var mapMarker: MovieClip = _legend.attachMovie("MapMarker", "Marker" +  1000+j,  j, {markerType:LegendMarkersIds[j], isUndiscovered: !(LegendMarkersEnabled[j])});
				}
			mapMarker.index = j;
				mapMarker.label = LegendMarkersNames[j];
				test++;
				mapMarker.visible = false;
				_legend.list.entryList.push(mapMarker);
		}
		 _legend.list.InvalidateData();
	}

	// @API
	public function RefreshMarkers(): Void
	{
		var i: Number = 0;
		var idx: Number = 0;
		var markersLen: Number = _markerList.length;
		var dataLen: Number = MarkerData.length;
		
		while (i < markersLen && idx < dataLen) {
			var marker: MovieClip = _markerList[i];
			//_bottomBar.buttonPanel.button0.label = "testestest";
			marker._visible = MarkerData[idx + REFRESH_SHOW];
			if (marker._visible) {
				marker._x = MarkerData[idx + REFRESH_X] * _mapWidth;
				marker._y = MarkerData[idx + REFRESH_Y] * _mapHeight;
				marker._rotation = MarkerData[idx + REFRESH_ROTATION];
			}
			i++;
			idx += REFRESH_STRIDE;
		}
		if (_selectedMarker != undefined) {
			_markerDescriptionHolder._x = _selectedMarker._x + _markerContainer._x;
			_markerDescriptionHolder._y = _selectedMarker._y + _markerContainer._y;
		}
	}
	
		// @API
	public function RefreshVisibilityMarkers(Visible:Array): Void
	{   
	   
		var i: Number = 0;
		var idx: Number = 0;
		var markersLen: Number = _markerList.length;
	
		while (i < markersLen ) {
			var marker: MovieClip = _markerList[i];
			
			//Way to dirty check if marker needs to be disabled. If you are annoyed, feel free to fix it yourself and make it pretty
			
			
			if(marker.Type==67 || marker.Type==69 ||marker.Type==85 ||marker.Type==86 || marker.Type==92){
				if(Visible[0]==1){
			        marker.IconClip._visible = true;
				}
				else{
					marker.IconClip._visible = false;
				}
			}
			else if (marker.Type==73 || marker.Type==87 ||marker.Type==88 ||marker.Type==89){
				if(Visible[1]==1){
			        marker.IconClip._visible = true;
				}
				else{
					marker.IconClip._visible = false;
				}
			}
			
			else if (marker.Type==71 || marker.Type==72 ||marker.Type==74 ||marker.Type==75||marker.Type==76||marker.Type==77||marker.Type==78||marker.Type==79){
				if(Visible[2]==1){
			        marker.IconClip._visible = true;
				}
				else{
					marker.IconClip._visible = false;
				}
			}
			else if (marker.Type==90){
				if(Visible[3]==1){
			        marker.IconClip._visible = true;
				}
				else{
					marker.IconClip._visible = false;
				}
			}
			else if (marker.Type==91){
				if(Visible[4]==1){
			        marker.IconClip._visible = true;
				}
				else{
					marker.IconClip._visible = false;
				}
			}
			else if (marker.Type==80 || marker.Type==81 ||marker.Type==82 ||marker.Type==83||marker.Type==84){
				if(Visible[5]==1){
			        marker.IconClip._visible = true;
				}
				else{
					marker.IconClip._visible = false;
				}
			}
			else if (marker.Type==68 || marker.Type==70){
				if(Visible[6]==1){
			        marker.IconClip._visible = true;
				}
				else{
					marker.IconClip._visible = false;
				}
			}
			else {
				if(Visible[7]==1){
			        marker.IconClip._visible = true;
				}
				else{
					marker.IconClip._visible = false;
				}
			
			}
			
			// enables/disables Marker depending on the outcome
			marker.enabled=marker.IconClip._visible;
			
			
			
			/*if (marker._visible) {
				marker._x = MarkerData[idx + REFRESH_X] * _mapWidth;
				marker._y = MarkerData[idx + REFRESH_Y] * _mapHeight;
				marker._rotation = MarkerData[idx + REFRESH_ROTATION];
			}*/
			i++;

		}
		if (_selectedMarker != undefined) {
			_markerDescriptionHolder._x = _selectedMarker._x + _markerContainer._x;
			_markerDescriptionHolder._y = _selectedMarker._y + _markerContainer._y;
		}
		
		_legend.list.clearList();
         var j : Number;
            for (j =0;j<8;j++){
            	if (j==5){
					var mapMarker: MovieClip = _legend.attachMovie("MapMarker", "Marker" +  1000+j,  j, {markerType:LegendMarkersIds[j], isUndiscovered: (LegendMarkersEnabled[j])});
				}
				else {
					var mapMarker: MovieClip = _legend.attachMovie("MapMarker", "Marker" +  1000+j,  j, {markerType:LegendMarkersIds[j], isUndiscovered: !(LegendMarkersEnabled[j])});
				}
            mapMarker.index = j;
                mapMarker.label = LegendMarkersNames[j];
                test++;
                mapMarker.visible = false;
                _legend.list.entryList.push(mapMarker);
        }
        _legend.list.InvalidateData()
	}

	// @API
	public function SetSelectedMarker(a_selectedMarkerIndex: Number): Void
	{
		var marker: MovieClip = a_selectedMarkerIndex < 0 ? null : _markerList[a_selectedMarkerIndex];
		
		if (marker == _selectedMarker)
			return;
			
		if (_selectedMarker != null) {
			_selectedMarker.MarkerRollOut();
			_selectedMarker = null;
			_markerDescriptionHolder.gotoAndPlay("Hide");
		}
		
		if (marker != null && !_bottomBar.hitTest(_root._xmouse, _root._ymouse) && marker.visible && marker.MarkerRollOver()) {
			_selectedMarker = marker;
			_markerDescriptionHolder._visible = true;
			_markerDescriptionHolder.gotoAndPlay("Show");
			return;
		}
		_selectedMarker = null;
	}

	// @API
	public function ClickSelectedMarker(): Void
	{
		if (_selectedMarker != undefined) {
			_selectedMarker.MarkerClick();
		}
	}

	// @API
	public function SetPlatform(a_platform: Number, a_bPS3Switch: Boolean): Void
	{
	
		if (a_platform == ButtonChange.PLATFORM_PC) {
			_localMapControls = {keyCode: 38}; // L
			_journalControls = {name: "Journal", context: Input.CONTEXT_GAMEPLAY};
			_zoomControls = {keyCode: 283}; // special: mouse wheel
			_playerLocControls = {keyCode: 18}; // E
			_setDestControls = {keyCode: 256}; // Mouse1
			_findLocControls = {keyCode: 33}; // F
			_toggleLegendControls = {keyCode: 37}; // K
		} else {
			_localMapControls = {keyCode: 278}; // X
			_journalControls = {keyCode: 270}; // START
			_zoomControls = [	// LT/RT
				{keyCode: 280},
				{keyCode: 281}
			];
			_playerLocControls = {keyCode: 279}; // Y
			_setDestControls = {keyCode: 276}; // A
			_findLocControls = {keyCode: 273}; // RS
			_toggleLegendControls = {keyCode: 272}; //Left Thumb L3
		}
		
		if (_bottomBar != undefined) {
			
			_bottomBar.buttonPanel.setPlatform(a_platform, a_bPS3Switch);

			createButtons(a_platform != ButtonChange.PLATFORM_PC);
		}
		
		InputDelegate.instance.isGamepad = a_platform != ButtonChange.PLATFORM_PC;
		InputDelegate.instance.enableControlFixup(true);
		
		_platform = a_platform;
	}

	// @API
	public function SetDateString(a_strDate: String): Void
	{
		_bottomBar.DateText.SetText(a_strDate);
	}

	// @API
	public function ShowJournal(a_bShow: Boolean): Void
	{
		if (_bottomBar != undefined) {
			_bottomBar._visible = !a_bShow;
		}
	}

	// @API
	public function SetCurrentLocationEnabled(a_bEnabled: Boolean): Void
	{
		if (_bottomBar != undefined && _platform == ButtonChange.PLATFORM_PC) {
			_bottomBar.PlayerLocButton.disabled = !a_bEnabled;
		}
	}
	
	// @GFx
	public function handleInput(details: InputDetails, pathToFocus: Array): Boolean
	{			
		var nextClip = pathToFocus.shift();
		if (nextClip.handleInput(details, pathToFocus))
			return true;
		
		// Find Location - F
		if (_platform == ButtonChange.PLATFORM_PC) {
			if (GlobalFunc.IsKeyPressed(details) && (details.skseKeycode == 33)) {
				LocalMapMenu.showLocationFinder();
			}
			// Toggle Legend - K
			else if (GlobalFunc.IsKeyPressed(details) && (details.skseKeycode == 37)){
				LocalMapMenu.showLegend();
			}
		}
		else{// Toggle Legend - K
			if (GlobalFunc.IsKeyPressed(details) && (details.skseKeycode == 272)){
				LocalMapMenu.showLegend();
			}
		}

		return false;
	}
	
	
  /* PRIVATE FUNCTIONS */
	
	private function OnLocalButtonClick(): Void
	{
		GameDelegate.call("ToggleMapCallback", []);
	}

	private function OnJournalButtonClick(): Void
	{
		GameDelegate.call("OpenJournalCallback", []);
	}

	private function OnPlayerLocButtonClick(): Void
	{
		GameDelegate.call("CurrentLocationCallback", []);
	}
	
	private function OnFindLocButtonClick(): Void
	{
		LocalMapMenu.showLocationFinder();
	}
	
	private function OnLegendButtonClick(): Void
	{			
		LocalMapMenu.showLegend();
	}
	
	private function onMouseDown(): Void
	{
		if (_bottomBar.hitTest(_root._xmouse, _root._ymouse))
			return;
		GameDelegate.call("ClickCallback", []);
	}
	
	private function onResize(): Void
	{
		_mapWidth = Stage.visibleRect.right - Stage.visibleRect.left;
		_mapHeight = Stage.visibleRect.bottom - Stage.visibleRect.top;
		
		if (_mapMovie == _root) {
			_markerContainer._x = Stage.visibleRect.left;
			_markerContainer._y = Stage.visibleRect.top;
		} else {
			var localMap: LocalMap = LocalMap(_mapMovie);
			if (localMap != undefined) {
				_mapWidth = localMap.TextureWidth;
				_mapHeight = localMap.TextureHeight;
			}
		
		}
		GlobalFunc.SetLockFunction();
		_bottomBar.Lock("B");
	}
	
	private function createButtons(a_bGamepad: Boolean): Void
	{
		var buttonPanel: ButtonPanel = _bottomBar.buttonPanel;
		buttonPanel.clearButtons();

		_localMapButton =	buttonPanel.addButton({text: "$Local Map", controls: _localMapControls});			// 0
		_journalButton =	buttonPanel.addButton({text: "$Journal", controls: _journalControls});				// 1
							buttonPanel.addButton({text: "$Zoom", controls: _zoomControls});					// 2
		_playerLocButton =	buttonPanel.addButton({text: "$Current Location", controls: _playerLocControls});	// 3
		_findLocButton =	buttonPanel.addButton({text: "$Find Location", controls: _findLocControls});		// 4
							buttonPanel.addButton({text: "$Set Destination", controls: _setDestControls});		// 5
		_searchButton =		buttonPanel.addButton({text: "$Search", controls: Input.Space});					// 6
		_legendButton=		buttonPanel.addButton({text: "$Legend", controls: _toggleLegendControls});			// 7
		
		_localMapButton.addEventListener("click", this, "OnLocalButtonClick");
		_journalButton.addEventListener("click", this, "OnJournalButtonClick");
		_playerLocButton.addEventListener("click", this, "OnPlayerLocButtonClick");
		_findLocButton.addEventListener("click", this, "OnFindLocButtonClick");
		_legendButton.addEventListener("click", this, "OnLegendButtonClick");
		
		_localMapButton.disabled = a_bGamepad;
		_journalButton.disabled = a_bGamepad;
		_playerLocButton.disabled = a_bGamepad;
		_findLocButton.disabled = a_bGamepad;
		_legendButton.disabled = a_bGamepad;
		
		_findLocButton.visible = !a_bGamepad;
		_searchButton.visible = false;
		
		buttonPanel.updateButtons(true);
	}
}