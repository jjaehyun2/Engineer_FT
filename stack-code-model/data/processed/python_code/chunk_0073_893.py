/**
 * VERSION: 1.0
 * DATE: 2012-03-22
 * AS3 (AS2 and JS versions are also available)
 * UPDATES AND DOCS AT: http://www.greensock.com
 **/
package com.greensock.easing {
/**
 * @private
 * Eases in a strong fashion starting out slowly and then accelerating, then decelerating at the end. 
 * Produces an effect similar to the popular "Zeno's paradox" style of scripted easing, where each 
 * interval of time decreases the remaining distance by a constant proportion. 
 * 
 * <p><strong>Copyright 2014, GreenSock. All rights reserved.</strong> This work is subject to the terms in <a href="http://www.greensock.com/terms_of_use.html">http://www.greensock.com/terms_of_use.html</a> or for <a href="http://www.greensock.com/club/">Club GreenSock</a> members, the software agreement that was issued with the membership.</p>
 * 
 * @author Jack Doyle, jack@greensock.com
 **/
	final public class ExpoInOut extends Ease {
	
		/** The default ease instance which can be reused many times in various tweens in order to conserve memory and improve performance slightly compared to creating a new instance each time. **/
		public static var ease:ExpoInOut = new ExpoInOut();

		/** @inheritDoc **/
		override public function getRatio(p:Number):Number {
			return ((p*=2) < 1) ? 0.5 * Math.pow(2, 10 * (p - 1)) : 0.5 * (2 - Math.pow(2, -10 * (p - 1)));
		}
		
	}
	
}