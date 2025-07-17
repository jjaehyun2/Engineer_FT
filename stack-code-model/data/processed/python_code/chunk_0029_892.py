/*
 Copyright aswing.org, see the LICENCE.txt.
*/

package devoron.aswing3d.plaf.basic.icon{

import org.aswing.ASColor;
import org.aswing.Component;
import org.aswing.graphics.Graphics2D;
import org.aswing.lookandfeel.plaf.UIResource;

/**
 * @private
 */
public class MenuArrowIcon extends SolidArrowIcon implements UIResource{
	
	public function MenuArrowIcon(){
		super(0, 8, ASColor.BLACK);
	}
	
	override public function updateIcon(c:Component, g:Graphics2D, x:int, y:int):void{
		super.updateIcon(c, g, x, y);
		paintIconWithColor(c.getMideground());
	}
}
}