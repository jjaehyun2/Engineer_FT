// Fig. 18.13 : map.as
// Handle the map functions for the Address Book application
import mx.managers.CursorManager;
import com.yahoo.webapis.maps.methodgroups.*;
import mx.controls.Alert;

// define constants
private const swfDomID : String = "addressBook";   
private const UUID : int = Math.random() * 10000;

// YahooAPIKey string must be your own from developer.yahoo.com
private const YahooAPIKey : String = "Your Yahoo! API Key here";
private const mapURL : String = "as2map.swf";
private var mapController : MapController;

private function initMap() : void
{
   CursorManager.setBusyCursor(); // turn on busy cursor

   // wait for map to load, then call onMapLoaded method
   yahooMap.addEventListener( 'onMapLoad', onMapLoaded );  
   yahooMap.addEventListener( 'onMapError', onMapError );
} // end function initMap

// handle map after it has loaded
public function onMapLoaded( event : Object ) : void 
{   
   // instantiate map controller
   mapController = new MapController( yahooMap ); 
      
   // instantiate panTool method
   var panTools : PanTool = new PanTool( yahooMap ); 

   // allow user to pan across the map
   panTools.setPanTool( true ); 
   
   // instantiate the maps widget class
   var widgets : Widgets = new Widgets( yahooMap ); 
      
   // activate Navigator widget
   widgets.showNavigatorWidget(); 
      
   // activate map-type selection widget
   widgets.showSatelliteControlWidget();

   // turn off busy cursor
   CursorManager.removeBusyCursor(); 
} // end function onMapLoaded

public function onMapError( errorCode:String, httpStatus:String ) : void 
{
   Alert.show( errorCode + '\n' + httpStatus, 'Map Load Error' );
} // end function onMapError

// place a labeled marker at the currently selected address
public function setMarkerByAddress() : void 
{
   mapController.removeAllMarkers(); // clear previous markers
   
   // add marker at specified address,
   // labeled with contact's name and address
   mapController.addCustomPOIMarker(
      ( contactsView.selectedItem.street + " " + 
      contactsView.selectedItem.city + " " + 
      contactsView.selectedItem.state ), 
      contactsView.selectedItem.firstname, 
      contactsView.selectedItem.lastname,  
      (contactsView.selectedItem.street + "\n" + 
      contactsView.selectedItem.city + ", " + 
      contactsView.selectedItem.state + " " + 
      contactsView.selectedItem.zip ),
      0x990099, 0xFFFFFF );

   // instantly center on address and zoom in
   mapController.setCenterByAddressAndZoom(
      contactsView.selectedItem.street + " " +
      contactsView.selectedItem.city + " " + 
      contactsView.selectedItem.state, 5, 0 );
} // end function setMarkerByAddress

/*
**************************************************************************
* ( C ) Copyright 1992-2007 by Deitel & Associates, Inc. and             *
* Pearson Education, Inc. All Rights Reserved.                           *
*                                                                        *
* DISCLAIMER: The authors and publisher of this book have used their     *
* best efforts in preparing the book. These efforts include the          *
* development, research, and testing of the theories and programs        *
* to determine their effectiveness. The authors and publisher make       *
* no warranty of any kind, expressed or implied, with regard to these    *
* programs or to the documentation contained in these books. The authors *
* and publisher shall not be liable in any event for incidental or       *
* consequential damages in connection with, or arising out of, the       *
* furnishing, performance, or use of these programs.                     *
**************************************************************************
*/