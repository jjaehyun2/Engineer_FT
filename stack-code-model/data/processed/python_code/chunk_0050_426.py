/*
   Copyright aswing.org, see the LICENCE.txt.
 */

package org.aswing.decorators
{
	import org.aswing.components.Component;
	import starling.display.DisplayObject;
	
	/**
	 * Decorator for components, it return a display object to be the UI decorator.
	 */
	public interface Decorator
	{
		/**
		 * Returns the display object which is used as the component decorator.
		 * <p>
		 * For same component, this method must return same display object.
		 * </p>
		 * @param c the component which will use this decorator.
		 * @return the display object
		 */
		function getDisplay(c:Component):DisplayObject;
	
	}

}