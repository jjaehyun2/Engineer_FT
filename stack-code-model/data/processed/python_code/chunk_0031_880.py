/* 
  Copyright (c) 2002-2010, Open-Plug
  All rights reserved.

  Redistribution and use in source and binary forms, with or without 
  modification, are permitted provided the above copyright notice, 
  this list of conditions and the following disclaimer is retained.
  
  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/ 

import com.adobe.serialization.json.JSON;

import flash.events.Event;
import flash.events.IOErrorEvent;
import flash.net.URLLoader;
import flash.net.URLRequest;
import flash.sensors.Geolocation;
import flash.utils.Timer;

import mx.collections.ArrayCollection;
import mx.controls.Label;
import mx.core.UIComponent;
import mx.events.CloseEvent;
import mx.events.ListEvent;

import op.MyListData;

import openplug.elips.controls.Alert;
import openplug.elips.controls.BaseList;
import openplug.elips.controls.GroupList;
import openplug.elips.controls.List;
import openplug.elips.controls.listClasses.ListIndex;
import openplug.elips.device.Capabilities;
import openplug.elips.events.AccessoryButtonEvent;
import openplug.elips.events.ItemEvent;
import openplug.elips.events.ItemTouchTapEvent;
import openplug.elips.services.SystemAPI;

[Bindable]
private var simpleDataProvider:ArrayCollection = new ArrayCollection();

[Bindable]
private var myData:MyListData = new MyListData();

private var slideTimer:Timer;
private var slideCurrent:int = 0;

[Bindable]
private var buttonSize:int = 25;

protected var _curList:Boolean = false;
protected var _curGrList:Boolean = false;

private function initImage():void
{
	imgLoader.addEventListener(Event.COMPLETE, onLoadingComplete);
	imgLoader.addEventListener(IOErrorEvent.IO_ERROR, onLoadingError);
}

private function initButton():void
{
	navBar.addEventListener(ItemTouchTapEvent.ITEM_TOUCH_TAP, onItemTouch);
}

private function initWeb():void
{
	html.location = txtUrl.text;
}

private function init():void
{
	var myObject:Object= new Object();

	slideTimer = new Timer(3000, 0);
	slideTimer.addEventListener(TimerEvent.TIMER, slideTimeout);

	if ((openplug.elips.device.Capabilities.getDeviceCapabilities().platform.name == "iPhone OS 3.0") || 
		(openplug.elips.device.Capabilities.getDeviceCapabilities().platform.name == "Android 1.6")) 
	{
		myObject.label = "Web View";
		myObject.data = "Web";
		widgetsCollection.addItem(myObject);
	}
	
	// Set list accessory buttons
	widgetList_setAccessoryButton(widgetsList, widgetsCollection);
	list_genProviders();
	
	// To update button height when phone view height is higher than 480px
	if (height > 480)
	{
		buttonSize = 60;
	}
	
	SystemAPI.dispatcher.addEventListener("storeImageDone", onImageStored);
	SystemAPI.dispatcher.addEventListener("storeImageAborted", onImageAborted);

	stage.addEventListener(KeyboardEvent.KEY_DOWN, handleKeyDown);
	setFocus();
}

public function handleKeyDown(event:KeyboardEvent) :void
{
	if (txtKey!=null)
		txtKey.text = "Press a Key: " + event.keyCode;
}

private function slideShowIterate():void
{

	if (slideCurrent < (slideCollection.length - 1)) {
		slideCurrent ++;
	} else {
		slideCurrent = 0;
	}

	if (slideShow != null) {
		slideShow.source = slideCollection[slideCurrent].data;
		fadeIn.play([slideShow]);
	}
}

private function slideTimeout(evt:TimerEvent):void
{
	slideShowIterate();
}

private function onAlertTouch(e:CloseEvent):void
{
	if (e.detail==Alert.OK){
        Alert.show("OK", "Title");
    } else {
        Alert.show("Cancel", "Title");
    }
}

private function onTextEntryComplete(e:Event):void
{
	txtEntry.text = SystemAPI.textEntryString;
	SystemAPI.dispatcher.removeEventListener("textEntry", onTextEntryComplete);
}

private function onItemTouch(e:ItemTouchTapEvent):void
{
	Alert.show("You pressed item "+e.index.toString(), "Item pressed: (0-left, 1-middle, 2-right)", (Alert.OK | Alert.CANCEL),null, onAlertTouch);
}

// Increment so that the file name changes every time, to update source properly
private var pictIndex:int = 0;

private function onImageStored(e:Event):void
{
	Alert.show("Done", "Store Image");
	photo.source = "/pict" + (pictIndex++) + ".jpg";
	trace(photo.source);
}

private function onImageAborted(e:Event):void
{
	Alert.show("Aborted", "Store Image");
}

private function onLoadingComplete(e:Event):void
{
	actImg.stop();
}

private function onLoadingError(e:IOErrorEvent):void
{
	Alert.show("Aborted", "Image Loading Error");
	actImg.stop();
}

private function onWidgetSelect(evt:ItemTouchTapEvent):void
{
	goToScreen(evt.item.data);
}

private function openApp():void
{
	var URLApp:URLRequest;
	
	if (openplug.elips.device.Capabilities.getDeviceCapabilities().platform.name == "iPhone OS 3.0") {
		URLApp = new URLRequest('itms://itunes.apple.com/app/twitteasy/id370146826?mt=8');
	} else if (openplug.elips.device.Capabilities.getDeviceCapabilities().platform.name == "Android 1.6"){
		URLApp = new URLRequest('market://details?id=com.Twitteasy.Twitteasy');		
	}
	if (URLApp is String) {
		navigateToURL(URLApp);
	} else {
		Alert.show('Cannot navigate to this URL "'+URLApp+'" !','WARNING');
	}
}

//
// Geolocation related methods
//
private var geo:Geolocation;
private var _isGeolocActivated:Boolean = false;
private var latMap:String = "43.62732737288085";
private var lonMap:String = "7.049853295711845";

private function loadMap():void
{
	actMap.start();
	staticMap.source='http://maps.google.com/maps/api/staticmap?zoom=5&size='+width+'x'+width+'&maptype=roadmap&markers=color:blue|label:S|'+latMap+','+lonMap+'&sensor=false';
	staticMap.load();
}

private function geoLocationCallback(evt:GeolocationEvent):void
{	
	if (geo.muted)
	{
		GPSstate.text = "GPS is disabled";
		position.text = "-----";
	}
	else
	{
		GPSstate.text = "GPS is enabled";
		latMap = evt.latitude.toString();
		lonMap = evt.longitude.toString();
		position.text = "Latitude: " + latMap + " °\n"
			+ "Longitude: " + lonMap + " °\n"
			+ "Altitude: " + evt.altitude + " m\n"
			+ "Heading: " + evt.heading + " °\n"
			+ "Speed: " + evt.speed + " m/s\n";
	}
}

private function startGPS():void
{
	if (!Geolocation.isSupported)
	{
		GPSstate.text = "GPS is not supported";
		position.text = "-----";
	}
	else
	{
		// Activate Geolocation
		if (!_isGeolocActivated)
		{
			// Alloc geo var only if not already done
			if (geo == null)
			{
				geo = new Geolocation();
			}
			geo.addEventListener("update", geoLocationCallback);
			GPSstate.text = "GPS is enabled";
			geolocBtn.label = "Stop Geolocation";
			_isGeolocActivated = true;
		}
		else
		{
			geo.removeEventListener("update", geoLocationCallback,false);
			GPSstate.text = "GPS is stopped";
			geolocBtn.label = "Start Geolocation";
			_isGeolocActivated = false;
		}
		
		// Check if GPS is activated
		if (geo.muted)
		{
			GPSstate.text = "GPS is disabled";
			position.text = "-----";
		}
	}
}

//
// From StyleApp
//
public function changeStyle(selector:String, prop:String, value:String):void
{
	var decl:CSSStyleDeclaration;
	
	decl = StyleManager.getStyleDeclaration(selector);
	
	if (decl == null)
	{
		decl = new CSSStyleDeclaration(selector);
	}
	
	decl.setStyle(prop, value);
}

public function backToDefaultStyle():void
{
	theBox.clearStyle('color');
	clearProp('.abc', 'color');
	clearProp('Button', 'color');
	theBox.clearStyle('fontWeight')
	btoit.clearStyle('fontStyle');
	StyleManager.clearStyleDeclaration('.def', true);
}

public function clearProp(selector:String, prop:String):void
{
	var decl:CSSStyleDeclaration;
	
	decl = StyleManager.getStyleDeclaration(selector);
	
	if (decl != null)
	{
		decl.clearStyle(prop);
	}
}

//
// Google Search related 
//

private function searchReplace(block:String, find:String, replace:String):String
{
	// Search & Replace substring in string 
	return block.split(find).join(replace);
} 

private function onSearchServerResponse(event:Event):void {
	
	var loader:URLLoader = URLLoader(event.target)
	
	try {
		var json:Object = JSON.decode(loader.data as String);
		// now have some fun with the results...
		var results:Array = json.responseData.results;
		
		total.text = String(results.length) + " result(s)";
		result.text = ""; 
		
		for (var i : int = 0; i<results.length; i++) {
			result.text += "Result " + String(i+1)+ ": " + results[i].titleNoFormatting + "\n"
				+ results[i].url + "\n\n";
		}
		
	} catch(ignored:Error) {
		total.text = "0 result(s)";
		result.text = ""; 
	}
	
	searchActivity.stop();
	searchActivity.visible=false;
}

private function errorHandler(e:IOErrorEvent):void 
{
	Alert.show("The search failed", "Error");
	searchActivity.stop();
	searchActivity.visible=false;
}

private function googleSearch(keyword:String):void 
{
	// Build url request according to Google AJAX Search API documentation
	var url:String = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=" + searchReplace(keyword," ","+");
	
	var urlLoader:URLLoader = new URLLoader();
	var urlRequest:URLRequest = new URLRequest(url);
	
	urlLoader.addEventListener(Event.COMPLETE, onSearchServerResponse);
	urlLoader.addEventListener(IOErrorEvent.IO_ERROR, errorHandler);
	urlLoader.dataFormat = "text";
	urlLoader.load(urlRequest);
	
	searchActivity.start();
	searchActivity.visible=true;
}

//
// List related functions
//
protected function list_accessoryButtonTapHandler(event:AccessoryButtonEvent, feedback:Label):void
{
	feedback.text = "accessoryButtonTap " + event.index.toString();
}

protected function list_itemInsertedHandlerSimple(provider:ArrayCollection, event:ItemEvent, feedback:*):void
{
	feedback.text = "itemInserted " + event.index.toString();
	
	var newObj:Object = new Object();
	newObj.text = "New Item";
	newObj.desc = "Editable for deletion";

	provider.addItemAt(newObj, event.index.row);

	simpleList.setItemEditingStyle(BaseList.EDITING_STYLE_DELETE, new ListIndex(event.index.row));
}

protected function list_itemDeletedHandlerSimple(provider:ArrayCollection, event:ItemEvent, feedback:*):void
{
	feedback.text = "itemDeleted " + event.index.toString();
	
	provider.removeItemAt(event.index.row);
}

protected function list_itemMovedHandlerSimple(provider:ArrayCollection, event:ItemEvent, feedback:*):void
{
	feedback.text = "itemMoved from " + event.oldIndex.toString() + " to " + event.index.toString();
	
	provider.moveItem(event.oldIndex.row, event.index.row);
}

//
// List shared functions
//
private static const MODIFY:String = "Modify";
private static const DONE:String = "Done";
private static const IPHONE_IPAD:String = "iPhone OS 3.0";

private static const MODE_NORMAL:int = BaseList.MODE_NORMAL;
private static const MODE_EDITING:int = BaseList.MODE_EDITING;

private var list0_Mode:int = MODE_NORMAL;

private function list_genProviders():void
{
	var ListItemObject:Object;
	
	ListItemObject = new Object();
	ListItemObject.text = "Item 0";
	ListItemObject.desc = "Non editable item - indent true - should not indent";
	simpleDataProvider.addItem(ListItemObject);
	
	ListItemObject = new Object();
	ListItemObject.text = "Item 1";
	ListItemObject.desc = "Non editable item - indent false - should not indent";
	simpleDataProvider.addItem(ListItemObject);
	
	ListItemObject = new Object();
	ListItemObject.text = "Item 2";
	ListItemObject.desc = "Editable item for deletion - should indent";
	simpleDataProvider.addItem(ListItemObject);

	ListItemObject = new Object();
	ListItemObject.text = "Item 3";
	ListItemObject.desc = "Editable item for deletion - should indent - 'Custom delete'";
	simpleDataProvider.addItem(ListItemObject);
	
	ListItemObject = new Object();
	ListItemObject.text = "Item 4";
	ListItemObject.desc = "Editable item for insertion - should indent";
	simpleDataProvider.addItem(ListItemObject);
	
	ListItemObject = new Object();
	ListItemObject.text = "Item 5";
	ListItemObject.desc = "Editable item for insertion - should indent - accessory in editing mode";
	simpleDataProvider.addItem(ListItemObject);

	ListItemObject = new Object();
	ListItemObject.text = "Item 6";
	ListItemObject.desc = "Editable item for move - should indent - accessory in normal mode only";
	simpleDataProvider.addItem(ListItemObject);
	
	ListItemObject = new Object();
	ListItemObject.text = "Item 7";
	ListItemObject.desc = "Editable item for move - should not indent";
	simpleDataProvider.addItem(ListItemObject);

	ListItemObject = new Object();
	ListItemObject.text = "Item 8";
	ListItemObject.desc = "Editable item for move & delete - should indent";
	simpleDataProvider.addItem(ListItemObject);

	ListItemObject = new Object();
	ListItemObject.text = "Item 9";
	ListItemObject.desc = "Editable item for move & insert - should indent";
	simpleDataProvider.addItem(ListItemObject);
}

private function initLists():void
{
	//
	// Simple Lists
	//
	simpleList.setItemIsEditable(false, new ListIndex(0));
	
	simpleList.setItemIsEditable(false, new ListIndex(1));
	simpleList.setShouldIndentWhileEditing(false, new ListIndex(1));
	
	simpleList.setItemEditingStyle(BaseList.EDITING_STYLE_DELETE, new ListIndex(2));

	simpleList.setItemEditingStyle(BaseList.EDITING_STYLE_DELETE, new ListIndex(3));
	simpleList.setItemEditingDescription('Custom Delete', new ListIndex(3));

	simpleList.setItemEditingStyle(BaseList.EDITING_STYLE_INSERT, new ListIndex(4));

	simpleList.setItemEditingStyle(BaseList.EDITING_STYLE_INSERT, new ListIndex(5));
	simpleList.setItemEditingAccessoryType(BaseList.ACCESSORY_TYPE_DISCLOSURE_INDICATOR, new ListIndex(5));

	simpleList.setItemEditingStyle(BaseList.EDITING_STYLE_NONE, new ListIndex(6));
	simpleList.setItemAccessory(BaseList.ACCESSORY_TYPE_CHECKMARK, new ListIndex(6));
	simpleList.setItemCanReorder(true, new ListIndex(6));

	simpleList.setItemEditingStyle(BaseList.EDITING_STYLE_NONE, new ListIndex(7));
	simpleList.setItemCanReorder(true, new ListIndex(7));
	simpleList.setShouldIndentWhileEditing(false, new ListIndex(7));
	
	simpleList.setItemEditingStyle(BaseList.EDITING_STYLE_DELETE, new ListIndex(8));
	simpleList.setItemCanReorder(true, new ListIndex(8));
	
	simpleList.setItemEditingStyle(BaseList.EDITING_STYLE_INSERT, new ListIndex(9));
	simpleList.setItemCanReorder(true, new ListIndex(9));
	
	//
	// Group List
	//
	grpList_setItemAccessory(BaseList.ACCESSORY_TYPE_DETAIL_DISCLOSURE_BUTTON);
}

private function setListMode():void
{
	if (list0_Mode == MODE_NORMAL)
	{
		simpleList.setMode(MODE_EDITING);
		list0_Mode = MODE_EDITING;
		
		if (openplug.elips.device.Capabilities.getDeviceCapabilities().platform.name == IPHONE_IPAD)
			listsNavBar.rightAction = DONE;
		else
			btnList0.label = DONE;
	}
	else
	{
		simpleList.setMode(MODE_NORMAL);
		list0_Mode = MODE_NORMAL;	
		
		if (openplug.elips.device.Capabilities.getDeviceCapabilities().platform.name == IPHONE_IPAD)
			listsNavBar.rightAction = MODIFY;
		else
			btnList0.label = MODIFY;
	}
}

private function updateRightButtonLabel(selectedTab:int):void
{
	switch (selectedTab)
	{
		case 0:
			listsNavBar.rightAction = (list0_Mode == MODE_NORMAL) ? MODIFY : DONE;
			break;
		
		default:
			listsNavBar.rightAction = null;
			break;
	}
}

private function grpList_accessoryButtonTapped(provider:MyListData, event:AccessoryButtonEvent, feedback:*):void
{
	feedback.text = "Accessory button tapped on " + event.index.toString();
}

private function widgetList_setAccessoryButton(list:openplug.elips.controls.List, provider:ArrayCollection):void
{
	list.defaultItemAccessory = BaseList.ACCESSORY_TYPE_DISCLOSURE_INDICATOR;
}

private function grpList_touchHandler(evt:ItemTouchTapEvent):void
{
	
	if (evt.section == 0)
	{
		var row:int = evt.index;
		switch (row)
		{
			case 0:
				grpList_setItemAccessory(BaseList.ACCESSORY_TYPE_NONE);
				break;
			
			case 1:
				grpList_setItemAccessory(BaseList.ACCESSORY_TYPE_DISCLOSURE_INDICATOR);
				break;
			
			case 2:
				grpList_setItemAccessory(BaseList.ACCESSORY_TYPE_DETAIL_DISCLOSURE_BUTTON);
				break;
			
			case 3:
				grpList_setItemAccessory(BaseList.ACCESSORY_TYPE_CHECKMARK);
				break;
		}
	}
}
 
private function grpList_setItemAccessory(accType:int):void
{
	lst2.defaultItemAccessory = accType;
}