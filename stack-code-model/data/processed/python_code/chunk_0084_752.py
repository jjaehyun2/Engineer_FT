/*
 * VERSION:3.0
 * DATE:2014-10-15
 * ACTIONSCRIPT VERSION: 3.0
 * UPDATES AND DOCUMENTATION AT: http://www.wdmir.net 
 * MAIL:mir3@163.com
 */
package com.greensock.plugins {
	
/**
 * Tweens a MovieClip backward to a particular frame number, wrapping it if/when it reaches the beginning
 * of the timeline. For example, if your MovieClip has 20 frames total and it is currently at frame 10
 * and you want tween to frame 15, a normal frame tween would go forward from 10 to 15, but a frameBackward
 * would go from 10 to 1 (the beginning) and wrap to the end and continue tweening from 20 to 15. <br /><br />
 * 
 * <b>USAGE:</b><br /><br />
 * <code>
 * 		import com.greensock.TweenLite; <br />
 * 		import com.greensock.plugins.~~; <br />
 * 		TweenPlugin.activate([FrameBackwardPlugin]); //activation is permanent in the SWF, so this line only needs to be run once.<br /><br />
 * 
 * 		TweenLite.to(mc, 1, {frameBackward:15}); <br /><br />
 * </code>
 * 
 * <b>Copyright 2010, GreenSock. All rights reserved.</b> This work is subject to the terms in <a href="http://www.greensock.com/terms_of_use.html">http://www.greensock.com/terms_of_use.html</a> or for corporate Club GreenSock members, the software agreement that was issued with the corporate membership.
 * 
 * @author Jack Doyle, jack@greensock.com
 */
	public class FrameBackwardPlugin extends FrameForwardPlugin {
		/** @private **/
		public static const API:Number = 1.0; //If the API/Framework for plugins changes in the future, this number helps determine compatibility
		
		/** @private **/
		public function FrameBackwardPlugin() {
			super();
			this.propName = "frameBackward";
			_backward = true;
		}

	}
}