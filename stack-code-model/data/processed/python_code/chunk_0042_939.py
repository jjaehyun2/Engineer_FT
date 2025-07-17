import mx.events.MenuEvent;
import mx.controls.Alert;
import mx.collections.*;

[Bindable]
public var menuBarCollection:XMLListCollection;

private var menubarXML:XMLList =
                <>
                	<menuitem label="File">
                        <menuitem label="New" data="1A"/>
                        <menuitem label="Open" data="1B"/>
                        <menuitem type="separator" />
                        <menuitem label="Close" data="1C" enabled="false"/>
                    </menuitem>
                    <menuitem label="Edit">
                        <menuitem label="Cut" data="2A"/>
                        <menuitem label="Copy" data="2B"/>
                        <menuitem label="Paste"   data="2C"/>
                    </menuitem>
                    <menuitem label="Format">
                        <menuitem label="Font" data="3A">
                        	<menuitem label="Arial" data="3ai" />
                        	<menuitem label="Verdana" data="3aii" />
                        	<menuitem label="Font not available" data="3aiii" enabled="false" />
                        </menuitem>
                     </menuitem>
                     <menuitem label="Help">
                     	<menuitem label="Help" />
                     </menuitem>
                </>;
      
      private function initCollections():void
            {
                menuBarCollection = new XMLListCollection(menubarXML);
            }

public var csscornerRadiusmenuBar:String = "";
public var cssbackgroundAlphamenuBar:String = "";
public var cssbackgroundColormenuBar:String = "";
public var cssborderColormenuBar:String = "";
public var csshighlightAlphasmenuBar:String = "";
public var cssfillAlphasmenuBar:String = "";
public var cssfillColorsmenuBar:String = "";
public var cssrollOverColormenuBar:String = "";
public var cssselectionColormenuBar:String = "";
public var csscolormenuBar:String = "";
public var csstextRollOverColormenuBar:String = "";
public var csstextSelectedColormenuBar:String = "";
public var cssdisabledColormenuBar:String = "";
public var cssthemeColormenuBar:String = "";

public var cssstrokeColorhRule:String = "";
public var cssshadowColorhRule:String = "";
public var cssstrokeWidthhRule:String = "";

public var csscornerRadiuslinkButton:String = "";
public var cssrollOverColorlinkButton:String = "";
public var cssselectionColorlinkButton:String = "";
public var csscolorlinkButton:String = "";
public var csstextRollOverColorlinkButton:String = "";
public var csstextSelectedColorlinkButton:String = "";
public var csspaddingLeftlinkButton:String = "";
public var csspaddingRightlinkButton:String = "";

public var cssborderColorprogressBar:String = "";
public var cssbarColorprogressBar:String = "";
public var csstrackColorsprogressBar:String = "";
public var csscolorprogressBar:String = "";
public var csspaddingLeftprogressBar:String = "";
public var csspaddingRightprogressBar:String = "";
public var csstextIndentprogressBar:String = "";
public var csstrackHeightprogressBar:String = "";
public var cssverticalGapprogressBar:String = "";


public function setValue(whichStyle:String, whatValue:Number, whatType:String, whichItem:String):void {
	

	if (whichItem == 'menuBar') { myMenuBar.setStyle(whichStyle, whatValue); }
	else if (whichItem == "hRule") {myHRule.setStyle(whichStyle, whatValue); }
	else if (whichItem == "linkButton") {myLinkButton.setStyle(whichStyle, whatValue); }
	else if  (whichItem == "progressBar") {myProgressBar.setStyle(whichStyle, whatValue); }
	
	
	setCSS(whichStyle, whatValue, whatType, whichItem);
}


public function rgbToHex(val:Number):String {
	var newVal:String = val.toString(16);
	while (newVal.length < 6) {	newVal = "0" + newVal; }			
	if (newVal.charAt(1) == 'x') {	newVal = newVal.slice(2, 8); }
	newVal = "#" + newVal;
	return newVal; 
}

public function setArrayCSS(whichStyle:String, whatValue1:Number, whatValue2:Number, isColor:Boolean, whichItem:String):void {
	var newValue:String;
	if (isColor == true) { newValue = rgbToHex(whatValue1) + ", " + rgbToHex(whatValue2); } 
	else { newValue =whatValue1 + ", " + whatValue2; }
	setCSS(whichStyle, 0, newValue, whichItem);
}

public function setArrayFourCSS(whichStyle:String, whatValue1:Number, whatValue2:Number, whatValue3:Number, whatValue4:Number, isColor:Boolean, whichItem:String):void {
	var newValue:String;
	if (isColor == true) { newValue = rgbToHex(whatValue1) + ", " + rgbToHex(whatValue2) + ", " + rgbToHex(whatValue3) + ", " + rgbToHex(whatValue4); } 
	else { newValue =whatValue1 + ", " + whatValue2 + ", " + whatValue3 + ", " + whatValue4; }
	setCSS(whichStyle, 0, newValue, whichItem);
}


public function setCSS(whichStyle:String, whatValue:Number, whatType:String, whichItem:String):void {


	if (whatType == 'color') { 	this["css" + whichStyle + whichItem] = "   " + whichStyle + ": " + rgbToHex(whatValue) + ";\n";	} 
	else if (whatType == 'number' ){ this["css" + whichStyle + whichItem] = "   " + whichStyle + ": " + whatValue + ";\n"; } 
	else {	this["css" + whichStyle + whichItem] = "   " + whichStyle + ": " + whatType + ";\n";}


	updateCSS();
	
	
		
}

public function updateCSS():void {

myCSS.text = 'MenuBar { \n'
	  + csscornerRadiusmenuBar
+ cssbackgroundAlphamenuBar
+ cssbackgroundColormenuBar
+ cssborderColormenuBar
+ csshighlightAlphasmenuBar
+ cssfillAlphasmenuBar
+ cssfillColorsmenuBar
+ cssrollOverColormenuBar
+ cssselectionColormenuBar
+ csscolormenuBar
+ csstextRollOverColormenuBar
+ csstextSelectedColormenuBar
+ cssdisabledColormenuBar
+ cssthemeColormenuBar
	+ "}\n\nHRule {\n"
 + cssstrokeColorhRule
+ cssshadowColorhRule
+ cssstrokeWidthhRule
	+ "}\n\nLinkButton {\n"
+ csscornerRadiuslinkButton
+ cssrollOverColorlinkButton
+ cssselectionColorlinkButton
+ csscolorlinkButton
+ csstextRollOverColorlinkButton
+ csstextSelectedColorlinkButton
+ csspaddingLeftlinkButton
+ csspaddingRightlinkButton
	+ "}\n\nProgressBar {\n"
+ cssborderColorprogressBar
+ cssbarColorprogressBar
+ csstrackColorsprogressBar
+ csscolorprogressBar
+ csspaddingLeftprogressBar
+ csspaddingRightprogressBar
+ csstextIndentprogressBar
+ csstrackHeightprogressBar
+ cssverticalGapprogressBar
		+ "}"
		; 
		
}

public function restoreDefaults():void {

	if (controlNavigator.selectedIndex == 0) {
		restoreMenuBar();
	} else if (controlNavigator.selectedIndex == 1) {
		restoreHRule();
	} else if (controlNavigator.selectedIndex == 2) {
		restoreLinkButton();
	} else {
		restoreProgressBar();
	}

	updateCSS();
	
}

public function restoreMenuBar():void {

myMenuBar.clearStyle('cornerRadius');
myMenuBar.clearStyle('backgroundAlpha');
myMenuBar.clearStyle('backgroundColor');
myMenuBar.clearStyle('borderColor');
myMenuBar.clearStyle('highlightAlphas');
myMenuBar.clearStyle('fillAlphas');
myMenuBar.clearStyle('fillColors');
myMenuBar.setStyle('rollOverColor', 0xAADEFF);
myMenuBar.setStyle('selectionColor', 0x7FCDFE);
myMenuBar.clearStyle('color');
myMenuBar.clearStyle('textRollOverColor');
myMenuBar.clearStyle('textSelectedColor');
myMenuBar.clearStyle('disabledColor');
myMenuBar.setStyle('themeColor', 0x009DFF);

myCornerRadiusmenuBar.value = myMenuBar.getStyle('cornerRadius');
myBackgroundAlphamenuBar.value = myMenuBar.getStyle('backgroundAlpha');
myBackgroundColormenuBar.selectedColor = 0xFFFFFF;
myBorderColormenuBar.selectedColor = myMenuBar.getStyle('borderColor');
myRollOverColormenuBar.selectedColor = 0xAADEFF;
mySelectionColormenuBar.selectedColor = 0x7FCDFE;
myColormenuBar.selectedColor = myMenuBar.getStyle('color');
myTextRollOverColormenuBar.selectedColor = myMenuBar.getStyle('textRollOverColor');
myTextSelectedColormenuBar.selectedColor = myMenuBar.getStyle('textSelectedColor');
myDisabledColormenuBar.selectedColor = myMenuBar.getStyle('disabledColor');
myThemeColormenuBar.selectedColor = myMenuBar.getStyle('themeColor');
highlightAlpha1menuBar.value = 0.3;
highlightAlpha2menuBar.value = 0;
myFillAlpha1menuBar.value = 0.6;
myFillAlpha2menuBar.value = 0.4;
fill1menuBar.selectedColor = 0xe6eeee;
fill2menuBar.selectedColor = 0xe6eeee;

csscornerRadiusmenuBar = "";
cssbackgroundAlphamenuBar = "";
cssbackgroundColormenuBar = "";
cssborderColormenuBar = "";
csshighlightAlphasmenuBar = "";
cssfillAlphasmenuBar = "";
cssfillColorsmenuBar = "";
cssrollOverColormenuBar = "";
cssselectionColormenuBar = "";
csscolormenuBar = "";
csstextRollOverColormenuBar = "";
csstextSelectedColormenuBar = "";
cssdisabledColormenuBar = "";
cssthemeColormenuBar = "";
 
}

public function restoreHRule ():void {
	myHRule.clearStyle('strokeColor');
	myHRule.clearStyle('shadowColor');
	myHRule.clearStyle('strokeWidth');
	
	myStrokeColorhRule.selectedColor = myHRule.getStyle('strokeColor');
	myShadowColorhRule.selectedColor = myHRule.getStyle('shadowColor');
	myStrokeWidthhRule.value = myHRule.getStyle('strokeWidth');

	cssstrokeColorhRule = "";
	cssshadowColorhRule = "";
	cssstrokeWidthhRule = "";

}

public function restoreLinkButton ():void {
	myLinkButton.clearStyle('cornerRadius');
	myLinkButton.clearStyle('rollOverColor');
	myLinkButton.clearStyle('selectionColor');
	myLinkButton.clearStyle('color');
	myLinkButton.clearStyle('textRollOverColor');
	myLinkButton.clearStyle('textSelectedColor');
	myLinkButton.clearStyle('paddingLeft');
	myLinkButton.clearStyle('paddingRight');

	myCornerRadiuslinkButton.value = myLinkButton.getStyle('cornerRadius');
	myRollOverColorlinkButton.selectedColor = myLinkButton.getStyle('rollOverColor');
	mySelectionColorlinkButton.selectedColor = myLinkButton.getStyle('selectionColor');
	myColorlinkButton.selectedColor = myLinkButton.getStyle('color');
	myTextRollOverColorlinkButton.selectedColor = myLinkButton.getStyle('textRollOverColor');
	myTextSelectedColorlinkButton.selectedColor = myLinkButton.getStyle('textSelectedColor');
	myPaddingLeftlinkButton.value = myLinkButton.getStyle('paddingLeft');
	myPaddingRightlinkButton.value = myLinkButton.getStyle('paddingRight');

	csscornerRadiuslinkButton = "";
	cssrollOverColorlinkButton = "";
	cssselectionColorlinkButton = "";
	csscolorlinkButton = "";
	csstextRollOverColorlinkButton = "";
	csstextSelectedColorlinkButton = "";
	csspaddingLeftlinkButton = "";
	csspaddingRightlinkButton = "";


}

public function restoreProgressBar ():void {
	myProgressBar.clearStyle('borderColor');
	myProgressBar.clearStyle('barColor');
	myProgressBar.clearStyle('trackColors');
	myProgressBar.clearStyle('color');
	myProgressBar.clearStyle('paddingLeft');
	myProgressBar.clearStyle('textIndent');
	myProgressBar.clearStyle('paddingRight');
	myProgressBar.clearStyle('trackHeight');
	myProgressBar.clearStyle('verticalGap');
	
	myBorderColorprogressBar.selectedColor = myProgressBar.getStyle('borderColor');
	myColorprogressBar.selectedColor = myProgressBar.getStyle('color');
	myPaddingLeftprogressBar.value = myProgressBar.getStyle('paddingLeft');
	myPaddingRightprogressBar.value = myProgressBar.getStyle('paddingRight');
	myTextIndentprogressBar.value = myProgressBar.getStyle('textIndent');
	myTrackHeightprogressBar.value = 3;
	myVerticalGapprogressBar.value = myProgressBar.getStyle('verticalGap');
	myBarColorprogressBar.selectedColor = 0x009DFF;
	track1progressBar.selectedColor = 0xe6eeee;
	track2progressBar.selectedColor = 0xe6eeee;
	
	cssborderColorprogressBar = "";
	cssbarColorprogressBar = "";
	csstrackColorsprogressBar = "";
	csscolorprogressBar = "";
	csspaddingLeftprogressBar = "";
	csspaddingRightprogressBar = "";
	csstextIndentprogressBar = "";
	csstrackHeightprogressBar = "";
	cssverticalGapprogressBar = "";

}




public function setProgressBar():void {
	myProgressBar.setProgress(30,100);
	myProgressBar.label= "CurrentProgress: 30%";
	initCollections();
}