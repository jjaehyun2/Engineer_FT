﻿/*
 Copyright aswing.org, see the LICENCE.txt.
*/

import GUI.fox.aswing.awml.AwmlNamespace;
import GUI.fox.aswing.awml.AwmlParser;
import GUI.fox.aswing.awml.AwmlUtils;
import GUI.fox.aswing.awml.component.ComponentParser;
import GUI.fox.aswing.Component;
import GUI.fox.aswing.geom.Point;
import GUI.fox.aswing.JViewport;

/**
 * Parses {@link GUI.fox.aswing.JViewport} level elements.
 * 
 * @author Igor Sadovskiy
 */
class GUI.fox.aswing.awml.component.ViewportParser extends ComponentParser {
	
	private static var ATTR_HORIZONTAL_BLOCK_INCREMENT:String = "horizontal-block-increment";
	private static var ATTR_VERTICAL_BLOCK_INCREMENT:String = "vertical-block-increment";
	private static var ATTR_HORIZONTAL_UNIT_INCREMENT:String = "horizontal-unit-increment";
	private static var ATTR_VERTICAL_UNIT_INCREMENT:String = "vertical-unit-increment";
	private static var ATTR_VIEW_POSITION_X:String = "view-position-x";
	private static var ATTR_VIEW_POSITION_Y:String = "view-position-y";
	
	/**
	 * Constructor.
	 */
	public function ViewportParser(Void) {
		super();
	}
	
	public function parse(awml:XMLNode, view:JViewport, namespace:AwmlNamespace) {
		
		view = super.parse(awml, view, namespace);
		
		// init block increments
		view.setHorizontalBlockIncrement(getAttributeAsNumber(awml, ATTR_HORIZONTAL_BLOCK_INCREMENT, view.getHorizontalBlockIncrement()));
		view.setVerticalBlockIncrement(getAttributeAsNumber(awml, ATTR_VERTICAL_BLOCK_INCREMENT, view.getVerticalBlockIncrement()));
		view.setHorizontalUnitIncrement(getAttributeAsNumber(awml, ATTR_HORIZONTAL_UNIT_INCREMENT, view.getHorizontalUnitIncrement()));
		view.setVerticalUnitIncrement(getAttributeAsNumber(awml, ATTR_VERTICAL_UNIT_INCREMENT, view.getVerticalUnitIncrement()));
		
		// init view position
		var x:Number = getAttributeAsNumber(awml, ATTR_VIEW_POSITION_X, view.getViewPosition().x);
		var y:Number = getAttributeAsNumber(awml, ATTR_VIEW_POSITION_Y, view.getViewPosition().y);
		
		view.setViewPosition(new Point(x,y));
		
        // init events
        attachEventListeners(view, JViewport.ON_STATE_CHANGED, getAttributeAsEventListenerInfos(awml, ATTR_ON_STATE_CHANGED));
		
		return view;
	}

	private function parseChild(awml:XMLNode, nodeName:String, view:JViewport, namespace:AwmlNamespace):Void {

		super.parseChild(awml, nodeName, view, namespace);

		if (AwmlUtils.isComponentNode(nodeName)) {
			var component:Component = AwmlParser.parse(awml, null, namespace);
			if (component != null) view.setView(component);	
		}
	}

    private function getClass(Void):Function {
    	return JViewport;	
    }

}