/*
 * IndicatorCellRenderer
 * by PhilFlash - http://philflash.inway.fr
 *
 * Dont't forget :
 * - to create a new symbol in Flash MX2004
 *   Insert > New Symbol
 *   with properties :
 *    Name : IndicatorCellRenderer
 *    Behavior : MovieClip : Checked
 *   For Linkage:
 *    Identifier: IndicatorCellRenderer
 *    AS 2.0 Class : IndicatorCellRenderer
 *    Export for Actionscript : Checked
 *    Export for in first frame : Checked
 */

import mx.core.UIComponent;

class IndicatorCellRenderer extends UIComponent
{

	var limits:Array;
	var intValue:Number = 0;	
	var previousValue:String = null;
	
	var backgroundDepth:Number = 1;
	var labelDepth:Number = 2;
	
	var localBackground:MovieClip;
	var textLabel:TextField;

 	var owner; // The row that contains this cell	
	var listOwner : MovieClip; // the reference we receive to the list
	var getCellIndex : Function; // the function we receive from the list
	var	getDataLabel : Function; // the function we receive from the list
	
	function IndicatorCellRenderer()
	{
	}

 	// -----   ----- 	
	function init(Void):Void
	{
		super.init();
		
		// set default limit value and fill color
		var defaultLimits:Array = new Array();
		defaultLimits.push({value:0, color:0x00FF00});   //  green
		defaultLimits.push({value:20, color:0xFFA500});  // orange
		defaultLimits.push({value:40, color:0xFFFF00});  // yellow
		defaultLimits.push({value:60, color:0xFF0000});  // red
		defaultLimits.push({value:90, color:0xFF00FF});  // magenta	
		setLimits(defaultLimits);
	}

 	// -----   ----- 	
	function createChildren(Void):Void
	{
	
		// Create the background.
		localBackground = createEmptyMovieClip("background_mc", backgroundDepth);

		// Create label
		textLabel = createLabel("textLabel",labelDepth);
		textLabel.tabEnabled = false;
		textLabel.selectable = false;
		textLabel.styleName = this;		
		textLabel.text = "";
	}

 	// -----   ----- 
	function size(Void):Void
	{
		invalidate();
	}
	
 	// -----   ----- 	
	function draw(Void):Void
	{
		var h = __height;
		var w = __width;
		
		this._y = 1;
		
		if (textLabel.text == "") {
			return;
		}
		var val:Number = intValue;
		var color:Number;

		var len:Number = limits.length;		
		for (var i = 0; i < len; i++) {
			var limit = limits[i];
			if (limit.value < val) {
				color = limit.color;
			}
		}
		
		// 5, 4 is the recommended text padding
		var xPad:Number = 5;
		var yPad:Number = 4;
		
		var iw:Number = (w * intValue ) / 100;
		localBackground.clear();
		localBackground.beginFill(color, 100);
		localBackground.moveTo(0, 0);
		localBackground.lineTo(iw-2,0);
		localBackground.lineTo(iw-2,h-2);
		localBackground.lineTo(0,h-2);
		localBackground.lineTo(0, 0);
		localBackground.endFill();	

     	textLabel.setSize(textLabel.textWidth+xPad,textLabel.textHeight+yPad);
     	var cWidth:Number = width/2 - textLabel.width/2;
     	var cHeight:Number = height/2 - textLabel.height/2;
		textLabel.move(cWidth,cHeight); 
	}

 	// -----   ----- 
	function setValue(value:String, item:Object, sel:Boolean):Void
	{
		if (item == undefined) 
		{
		 	localBackground._visible = false;
		 	textLabel._visible = false;
		 	return;
		}
		localBackground._visible = true;
		textLabel._visible = true;
		if (previousValue == undefined || (value != previousValue)) {
			intValue = parseInt(value);
			textLabel.text = value + " %";
			previousValue = value;
			// Force draw
			invalidate();
		}
	}

 	// -----   ----- 
	// owner.__height par defaut 20
	function getPreferredHeight(Void):Number
	{
		return (owner == undefined ? 20 : owner.__height);
	}
	
	// ----- set limit value and fill color -----
	function setLimits(newLimits:Array):Void
	{
		if (newLimits != undefined && newLimits.length != 0) 
		{
			limits = newLimits;
			limits.sortOn("value", Array.NUMERIC);
		}
	}

}