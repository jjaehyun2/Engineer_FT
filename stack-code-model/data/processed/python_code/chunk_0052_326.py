package org.pong.mvcs.view 
{
	import org.pong.utils.graphic.GraphicUtils;
	
	/**
	 * 
	 * Interface that describes view component behaviour.
	 * 
	 * @author mc
	 */
	public interface IView 
	{
		/**
		 * 
		 * Added to stage handler
		 */
		function added():void
		
		/**
		 * 
		 * Removed from stage handler
		 */
		function removed():void;
		
		/**
		 * 
		 * Tick update handler
		 */
		function update(passedTime:Number):void;
		
		/**
		 * 
		 * Graphic utils getter
		 */
		function get graphicUtils():GraphicUtils;
		
		/**
		 * 
		 * Graphic utils setter
		 */
		function set graphicUtils(value:GraphicUtils):void;
	}
	
}