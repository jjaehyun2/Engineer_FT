/*
SUMMARY			: 	This widget is an enhanced version of the standard coordinates widget
					supplied with the ESRI Flex Viewer (v2.5).  Modifications have been 
					made to allow user alter/specify the way the coordinate text is 
					displayed, including the style.  Also the current scale of the map
					can be optionally displayed as part of the text.

SOURCE			: 	ESRI Coordinate Widget (v2.5)
					The code has been updated to use the current version (2.5) as its base.
					The consortium modifcations from the previous releases have been ported
					into this new code and are marked appropriately.

DEVELOPED BY 	: 	Iain Campion, ECan.

CREATED			: 	15/11/2010
DEPENDENCIES	: 	None

CHANGES 
Change By 			| Change Date 	| Change Description
Iain Campion (ECan)	| 15/11/2010 	| Initial Development.
Ryan Elley (Ecan)	| 10/01/2011	| Port to version 2.2 Flex API
Ryan Elley (Ecan)	| 10/06/2011	| Port to version 2.3.1 Flex API
Ryan Elley (Ecan)	| 09/01/2012	| Port to version 2.5 Flex API and Viewer 2.5
									  Display of scale, number format and template are now configurable.  
Ryan Elley (Ecan)	| 26/01/2013	| Port to version 3.1 Flex API and Viewer 3.1
*/

///////////////////////////////////////////////////////////////////////////
// Copyright (c) 2010-2011 Esri. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
///////////////////////////////////////////////////////////////////////////
package widgets.CoordinateEnhanced
{
	//--------------------------------------
	//  Other metadata
	//--------------------------------------
	/**
	 * Utility class to pretty print decimal degree numbers.
	 * @private
	 */
	public final class DegToDMS
	{
	    // Constants to define the format.
	    public static const LAT:String = "lat";
	
	    public static const LON:String = "lon";
	
	    /**
	     * Utility function to format a decimal degree number into a pretty string with degrees, minutes and seconds.
	     * @param decDeg the decimal degree number.
	     * @param decDir "lat" for a latitude number, "lon" for a longitude value.
	     * @return A pretty print string with degrees, minutes and seconds.
	     */
	    public static function format(decDeg:Number, decDir:String):String
	    {
	        var d:Number = Math.abs(decDeg);
	        var deg:Number = Math.floor(d);
	        d = d - deg;
	        var min:Number = Math.floor(d * 60);
	        var av:Number = d - min / 60;
	        var sec:Number = Math.floor(av * 60 * 60);
	        if (sec == 60)
	        {
	            min++;
	            sec = 0;
	        }
	        if (min == 60)
	        {
	            deg++;
	            min = 0;
	        }
	        var smin:String = min < 10 ? "0" + min + "' " : min + "' ";
	        var ssec:String = sec < 10 ? "0" + sec + "\" " : sec + "\" ";
	        var sdir:String = (decDir == LAT) ? (decDeg < 0 ? "S" : "N") : (decDeg < 0 ? "W" : "E");
	        return deg + "\xB0 " + smin + ssec + sdir;
	    }
	}
}