//=========================================================================================
//------ Path Variables - CHANGE THESE VALUES AT WILL
//=========================================================================================
var navHighlight:String = "0x00AEEF";										// controls the navigation highlight color
var borderSize:Number = 5;													// controls the border size around the site
var copyright:String = "(c) 2007 Your Company Name. All Rights Reserved." 	// Change to your own copyright message.

// Portfolio SubNav Variables
var subNavSpacer:Number = 16;												// Affects the spaces between the numbers in the portfolio
var subNavColor:String = "0xFFFFFF";										// Affects the text color for the portfolio SubNav
var subNav_arr:Array = ["Portfolio 1", "Portfolio 2", "Portfolio 3", "Portfolio 4", "Portfolio 5"];	// These set the titles for each portfolio (i.e. Landscape, Glamour, Portraits, etc.) - You'll want to keep portfolio names short.
var subNav_xml:Array = ["port1.xml", "port2.xml", "port3.xml", "port4.xml", "port5.xml"];			// Any time you add/delete an XML file, be sure to do the same here. 

// Set to false when deploying
var testMode:Boolean = true;


// NO NEED TO CHANGE ANYTHING PAST THIS LINE
//=========================================================================================
//------ Paths
//=========================================================================================
if (testMode == true) {
	var XMLPath:String = "../xml/";
	var portfolioPath:String = "../portfolio/";
} else {
	var XMLPath:String = "xml/";
	var portfolioPath:String = "portfolio/";
}
//=========================================================================================
//------ Imports
//=========================================================================================
// import fuseKit (http://www.mosessupposes.com/fuse)
import com.mosesSupposes.fuse.*;
ZigoEngine.simpleSetup(PennerEasing, Shortcuts);