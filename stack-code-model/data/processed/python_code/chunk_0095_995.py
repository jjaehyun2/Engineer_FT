/*
include "../includes/License.as.inc";
 */

package temple.core.display
{
	import flash.display.DisplayObject;
	import flash.display.Graphics;
	import flash.display.Sprite;
	import flash.geom.Rectangle;
	import flash.media.SoundTransform;

	/**
	 * @author Thijs Broerse
	 */
	public interface ISprite extends IDisplayObjectContainer
	{
		function get buttonMode():Boolean;
		function set buttonMode(value:Boolean):void;

		function get dropTarget():DisplayObject;

		function get graphics():Graphics;

		function get hitArea():Sprite;
		function set hitArea(value:Sprite):void;

		function get soundTransform():SoundTransform;
		function set soundTransform(sndTransform:SoundTransform):void;

		function startDrag(lockCenter:Boolean = false, bounds:Rectangle = null):void;

		function stopDrag():void;

		function get useHandCursor():Boolean;
		function set useHandCursor(value:Boolean):void;
	}
}