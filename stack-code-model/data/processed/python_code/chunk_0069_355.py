/* See LICENSE for copyright and terms of use */

import org.actionstep.NSImageRep;
import org.actionstep.NSPoint;
import org.actionstep.NSSize;
import org.actionstep.themes.standard.images.ASResizeUpDownCursorRep;

/**
 * This class draws the diagonal resizing cursor, that appears with the same
 * slope as a "\".
 * 
 * @author Scott Hyndman
 */
class org.actionstep.themes.standard.images.ASResizeDiagonalDownCursorRep extends NSImageRep 
{
	public function ASResizeDiagonalDownCursorRep() 
	{
		m_size = new NSSize(12.73,12.73);
	}

	public function description():String 
	{
		return "ASResizeDiagonalDownCursorRep(size=" + size() + ")";
	}
	
	public function draw():Void
	{
		var depth:Number;
		
		if (m_drawClip.view != null) {
			depth = m_drawClip.view.getNextDepth();
		} else {
			depth = m_drawClip.getNextHighestDepth();
		}
		
		var mc:MovieClip = m_drawClip.createEmptyMovieClip("imageRep" + depth,
			depth);
		var rep:NSImageRep = new ASResizeUpDownCursorRep();
		rep.setFocus(mc);
		rep.drawAtPoint(new NSPoint((m_size.width - rep.size().width) / 2, 0));
		rep.setFocus(null);
		
		mc._rotation = -45;
		mc._x = -rep.size().width;
		mc._y = 0;
		
		addImageRepToDrawClip(mc);
	}
	
}