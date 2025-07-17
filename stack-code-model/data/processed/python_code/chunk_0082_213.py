import mx.controls.*;
private var myMenu:Menu;

public var myButtonBarStyle:CSSStyleDeclaration = new CSSStyleDeclaration();

public var csscornerRadiusbutton:String = "";
public var csstextIndentbutton:String = "";
public var csspaddingLeftbutton:String = "";
public var csspaddingRightbutton:String = "";
public var csspaddingTopbutton:String = "";
public var csspaddingBottombutton:String = "";
public var csshighlightAlphasbutton:String  = "";
public var cssfillAlphasbutton:String  = "";
public var cssfillColorsbutton:String  = "";
public var csscolorbutton:String  = "";
public var cssborderColorbutton:String = "";
public var cssthemeColorbutton:String  = "";
public var csstextRollOverColorbutton:String = "";
public var csstextSelectedColorbutton:String = "";

public var csscornerRadiuspopUpButton:String = "";
public var cssarrowButtonWidthpopUpButton:String = "";
public var csspopUpGappopUpButton:String = "";
public var csstextIndentpopUpButton:String = "";
public var csspaddingLeftpopUpButton:String = "";
public var csspaddingRightpopUpButton:String = "";
public var csspaddingToppopUpButton:String = "";
public var csspaddingBottompopUpButton:String = "";
public var csshighlightAlphaspopUpButton:String  = "";
public var cssfillAlphaspopUpButton:String  = "";
public var cssfillColorspopUpButton:String  = "";
public var csscolorpopUpButton:String  = "";
public var cssborderColorpopUpButton:String = "";
public var cssthemeColorpopUpButton:String  = "";
public var csstextRollOverColorpopUpButton:String = "";
public var csstextSelectedColorpopUpButton:String = "";

public var cssbuttonHeightbuttonBar:String = "";
public var cssbuttonWidthbuttonBar:String = "";
public var csshorizontalGapbuttonBar:String = "";
public var csscornerRadiusbuttonBar:String = "";
public var csstextIndentbuttonBar:String = "";
public var csshighlightAlphasbuttonBar:String  = "";
public var cssfillAlphasbuttonBar:String  = "";
public var cssfillColorsbuttonBar:String  = "";
public var csscolorbuttonBar:String  = "";
public var cssborderColorbuttonBar:String = "";
public var cssthemeColorbuttonBar:String  = "";
public var csstextRollOverColorbuttonBar:String = "";
public var csstextSelectedColorbuttonBar:String = "";


public function setValue(whichStyle:String, whatValue:Number, whatType:String, whichItem:String):void {
	if (whichItem == "button") { myButton.setStyle(whichStyle, whatValue); }
	else if (whichItem == "popUpButton") { myPopUpButton.setStyle(whichStyle, whatValue);}
	else {  myButtonBar.setStyle(whichStyle, whatValue);
	}
	setCSS(whichStyle, whatValue, whatType, whichItem);
}




public function setButtonStyleValue(whichStyle:String, whatValue:Number, whatType:String, whichItem:String):void {
	myButtonBarStyle.setStyle(whichStyle, whatValue);
	StyleManager.setStyleDeclaration(".myButtonBarStyleName", myButtonBarStyle, true);
	setCSS(whichStyle, whatValue, whatType, whichItem);
}

public function setButtonStyleArrayValue(whichStyle:String, whatValue1:Number, whatValue2:Number):void {
	myButtonBarStyle.setStyle(whichStyle, [whatValue1, whatValue2]);
	StyleManager.setStyleDeclaration(".myButtonBarStyleName", myButtonBarStyle, true);
}

public function setButtonStyleArrayFourValue(whichStyle:String, whatValue1:Number, whatValue2:Number, whatValue3:Number, whatValue4:Number):void {
	myButtonBarStyle.setStyle(whichStyle, [whatValue1, whatValue2, whatValue3, whatValue4]);
	StyleManager.setStyleDeclaration(".myButtonBarStyleName", myButtonBarStyle, true);
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
		
	myCSS.text = 'Button { \n'
		 + csscornerRadiusbutton
		 + csstextIndentbutton
		 + csspaddingLeftbutton
		 + csspaddingRightbutton
		 + csspaddingTopbutton
		 + csspaddingBottombutton
		 + csshighlightAlphasbutton
		 + cssfillAlphasbutton
		 + cssfillColorsbutton
		 + csscolorbutton
		 + csstextRollOverColorbutton
		 + csstextSelectedColorbutton
		 + cssborderColorbutton
		 + cssthemeColorbutton
		 + "}\n\nPopUpButton {\n"
		 + csscornerRadiuspopUpButton
		 + cssarrowButtonWidthpopUpButton
		 + csspopUpGappopUpButton
		 + csstextIndentpopUpButton
		 + csspaddingLeftpopUpButton
		 + csspaddingRightpopUpButton
		 + csspaddingToppopUpButton
		 + csspaddingBottompopUpButton
		 + csshighlightAlphaspopUpButton
		 + cssfillAlphaspopUpButton
		 + cssfillColorspopUpButton
		 + csscolorpopUpButton
		 + csstextRollOverColorpopUpButton
		 + csstextSelectedColorpopUpButton
		 + cssborderColorpopUpButton
		 + cssthemeColorpopUpButton
		 + "}\n\nButtonBar {\n"
		 + cssbuttonHeightbuttonBar
		 + cssbuttonWidthbuttonBar
		 + csshorizontalGapbuttonBar
		 + csstextIndentbuttonBar
		 + csscolorbuttonBar
		 + csstextRollOverColorbuttonBar
		 + csstextSelectedColorbuttonBar
		 + cssthemeColorbuttonBar
		 + '   buttonStyleName="myButtonBar";\n'
		 + "}\n\n.myButtonBar {\n"
		 + csscornerRadiusbuttonBar
		 + csshighlightAlphasbuttonBar
		 + cssfillAlphasbuttonBar
		 + cssfillColorsbuttonBar
		 + cssborderColorbuttonBar
		 + "}" ; 
		 
}

public function restoreDefaults():void {

if (controlNavigator.selectedIndex == 0) {
		restoreButton();
} else if (controlNavigator.selectedIndex == 1) {
	restorePopUpButton();
} else {
	restoreButtonBar();
}

}

public function restoreButton():void {

	myButton.clearStyle('cornerRadius');
	myButton.clearStyle('textIndent');
	myButton.clearStyle('paddingLeft');
	myButton.clearStyle('paddingRight');
	myButton.clearStyle('paddingTop');
	myButton.clearStyle('paddingBottom');
	myButton.clearStyle('highlightAlphas');
	myButton.clearStyle('fillAlphas');
	myButton.clearStyle('fillColors');
	myButton.clearStyle('color');
	myButton.clearStyle('borderColor');
	myButton.clearStyle('themeColor');
	myButton.clearStyle('textRollOverColor');
	myButton.clearStyle('textSelectedColor');
	
	
	myCornerRadiusButton.value = myButton.getStyle('cornerRadius');
	myTextIndentButton.value = myButton.getStyle('textIndent');
	myPaddingRightButton.value = myButton.getStyle('paddingRight');
	myPaddingLeftButton.value = myButton.getStyle('paddingLeft');
	myPaddingTopButton.value = myButton.getStyle('paddingTop');
	myPaddingLeftButton.value = myButton.getStyle('paddingLeft');
	myTextIndentButton.value = myButton.getStyle('textIndent');
	myTextRollOverColorButton.selectedColor = myButton.getStyle('textRollOverColor');
	myTextSelectedColorButton.selectedColor = myButton.getStyle('textSelectedColor');
	highlightAlpha1Button.value = .30;
	highlightAlpha2Button.value = 0;
	myFillAlpha1Button.value = .60;
	myFillAlpha2Button.value = .40;
	myFillAlpha3Button.value = .75;
	myFillAlpha4Button.value = .65;
	fill1Button.selectedColor = 0xFFFFFF;
	fill2Button.selectedColor = 0xCCCCCC;
	fill3Button.selectedColor = 0xFFFFFF;
	fill4Button.selectedColor = 0xEEEEEE;
	myColorButton.selectedColor = myButton.getStyle('color');
	myBorderColorButton.selectedColor = myButton.getStyle('borderColor');
	myThemeColorButton.selectedColor = myButton.getStyle('themeColor');
	
	
	csscornerRadiusbutton = "" ;
	csstextIndentbutton = "" ;
	csspaddingLeftbutton = "" ;
	csspaddingRightbutton = "" ;
	csspaddingTopbutton = "" ;
	csspaddingBottombutton = "" ;
	csshighlightAlphasbutton = "" ;
	cssfillAlphasbutton = "" ;
	cssfillColorsbutton = "" ;
	csscolorbutton  = "" ;
	cssborderColorbutton = "" ;
	cssthemeColorbutton = "" ;
	csstextSelectedColorbutton = "";
	csstextRollOverColorbutton = "";

	updateCSS();
}

public function restoreButtonBar():void {

	myButtonBar.clearStyle('buttonHeight');
	myButtonBar.clearStyle('buttonWidth');
	myButtonBar.clearStyle('horizontalGap');
	myButtonBar.clearStyle('cornerRadius');
	myButtonBar.clearStyle('textIndent');
	myButtonBar.clearStyle('highlightAlphas');
	myButtonBar.clearStyle('fillAlphas');
	myButtonBar.clearStyle('fillColors');
	myButtonBar.clearStyle('color');
	myButtonBar.clearStyle('borderColor');
	myButtonBar.clearStyle('themeColor');
	myButtonBar.clearStyle('textRollOverColor');
	myButtonBar.clearStyle('textSelectedColor');
	myButtonBarStyle.clearStyle('borderColor');
	myButtonBarStyle.clearStyle('cornerRadius');
	myButtonBarStyle.clearStyle('fillColors');
	myButtonBarStyle.clearStyle('fillAlphas');
	myButtonBarStyle.clearStyle('highlightAlphas');
	StyleManager.setStyleDeclaration(".myButtonBarStyleName", myButtonBarStyle, true);
	
	myButtonHeightButtonBar.value = 22;
	myButtonWidthButtonBar.value = 71;
	myHorizontalGapButtonBar.value = myButtonBar.getStyle('horizontalGap');
	myCornerRadiusButtonBar.value = 5;
	myTextIndentButtonBar.value = myButtonBar.getStyle('textIndent');
	myTextRollOverColorButtonBar.selectedColor = myButtonBar.getStyle('textRollOverColor');
	myTextSelectedColorButtonBar.selectedColor = myButtonBar.getStyle('textSelectedColor');
	highlightAlpha1ButtonBar.value = .30;
	highlightAlpha2ButtonBar.value = 0;
	myFillAlpha1ButtonBar.value = .60;
	myFillAlpha2ButtonBar.value = .40;
	myFillAlpha3ButtonBar.value = .75;
	myFillAlpha4ButtonBar.value = .65;
	fill1ButtonBar.selectedColor = 0xFFFFFF;
	fill2ButtonBar.selectedColor = 0xCCCCCC;
	fill3ButtonBar.selectedColor = 0xFFFFFF;
	fill4ButtonBar.selectedColor = 0xEEEEEE;
	myColorButtonBar.selectedColor = myButtonBar.getStyle('color');
	myBorderColorButtonBar.selectedColor = myButtonBarStyle.getStyle('borderColor');
	myThemeColorButtonBar.selectedColor = myButtonBar.getStyle('themeColor');
	
	cssbuttonHeightbuttonBar = "" ;
	cssbuttonWidthbuttonBar = "" ;
	csshorizontalGapbuttonBar = "" ;
	csscornerRadiusbuttonBar = "" ;
	csstextIndentbuttonBar = "" ;
	csshighlightAlphasbuttonBar = "" ;
	cssfillAlphasbuttonBar = "" ;
	cssfillColorsbuttonBar = "" ;
	csscolorbuttonBar  = "" ;
	cssborderColorbuttonBar = "" ;
	cssthemeColorbuttonBar = "" ;
	csstextSelectedColorbuttonBar = "";
	csstextRollOverColorbuttonBar = "";

	updateCSS();
}


public function restorePopUpButton():void {

	myPopUpButton.clearStyle('cornerRadius');
	myPopUpButton.clearStyle('arrowButtonWidth');
	myPopUpButton.clearStyle('popUpGap');
	myPopUpButton.clearStyle('textIndent');
	myPopUpButton.clearStyle('paddingLeft');
	myPopUpButton.clearStyle('paddingRight');
	myPopUpButton.clearStyle('paddingTop');
	myPopUpButton.clearStyle('paddingBottom');
	myPopUpButton.clearStyle('highlightAlphas');
	myPopUpButton.clearStyle('fillAlphas');
	myPopUpButton.clearStyle('fillColors');
	myPopUpButton.clearStyle('color');
	myPopUpButton.clearStyle('borderColor');
	myPopUpButton.clearStyle('themeColor');
	myPopUpButton.clearStyle('textRollOverColor');
	myPopUpButton.clearStyle('textSelectedColor');
	
	myCornerRadiusPopUpButton.value = myPopUpButton.getStyle('cornerRadius');
	myArrowButtonWidthPopUpButton.value = myPopUpButton.getStyle('arrowButtonWidth');
	myPopUpGapPopUpButton.value = myPopUpButton.getStyle('popUpGap');
	myTextIndentPopUpButton.value = myPopUpButton.getStyle('textIndent');
	myPaddingRightPopUpButton.value = myPopUpButton.getStyle('paddingRight');
	myPaddingLeftPopUpButton.value = myPopUpButton.getStyle('paddingLeft');
	myPaddingTopPopUpButton.value = myPopUpButton.getStyle('paddingTop');
	myPaddingLeftPopUpButton.value = myPopUpButton.getStyle('paddingLeft');
	myTextIndentPopUpButton.value = myPopUpButton.getStyle('textIndent');
	myTextRollOverColorPopUpButton.selectedColor = myPopUpButton.getStyle('textRollOverColor');
	myTextSelectedColorPopUpButton.selectedColor = myPopUpButton.getStyle('textSelectedColor');
	highlightAlpha1PopUpButton.value = .30;
	highlightAlpha2PopUpButton.value = 0;
	myFillAlpha1PopUpButton.value = .60;
	myFillAlpha2PopUpButton.value = .40;
	myFillAlpha3PopUpButton.value = .75;
	myFillAlpha4PopUpButton.value = .65;
	fill1PopUpButton.selectedColor = 0xFFFFFF;
	fill2PopUpButton.selectedColor = 0xCCCCCC;
	fill3PopUpButton.selectedColor = 0xFFFFFF;
	fill4PopUpButton.selectedColor = 0xEEEEEE;
	myColorPopUpButton.selectedColor = myPopUpButton.getStyle('color');
	myBorderColorPopUpButton.selectedColor = myPopUpButton.getStyle('borderColor');
	myThemeColorPopUpButton.selectedColor = myPopUpButton.getStyle('themeColor');
	
	
	csscornerRadiuspopUpButton = "" ;
	cssarrowButtonWidthpopUpButton = "";
	csspopUpGappopUpButton = "";
	csstextIndentpopUpButton = "" ;
	csspaddingLeftpopUpButton = "" ;
	csspaddingRightpopUpButton = "" ;
	csspaddingToppopUpButton = "" ;
	csspaddingBottompopUpButton = "" ;
	csshighlightAlphaspopUpButton = "" ;
	cssfillAlphaspopUpButton = "" ;
	cssfillColorspopUpButton = "" ;
	csscolorpopUpButton  = "" ;
	cssborderColorpopUpButton = "" ;
	cssthemeColorpopUpButton = "" ;
	csstextSelectedColorpopUpButton = "";
	csstextRollOverColorpopUpButton = "";
	
	updateCSS();

}




private function initMenu():void {
	myMenu = new Menu();
	var dp:Object = [{label: "Action 1"}, {label: "Action 2"}, {label: "Action 3"}];        
	myMenu.dataProvider = dp;
	myPopUpButton.popUp = myMenu;
}