/*
 Copyright aswing.org, see the LICENCE.txt.
*/

package devoron.aswing3d.plaf{

/**
 * Pluginable ui for MenuItem.
 * @see devoron.aswing3d.JMenuItem
 * @author iiley
 */
public interface MenuElementUI extends ComponentUI{
	
	/**
	 * Subclass override this to process key event.
	 */
	function processKeyEvent(code:uint):void;
}
}