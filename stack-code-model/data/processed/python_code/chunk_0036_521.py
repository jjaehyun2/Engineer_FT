/**
 * VERSION: 1.0
 * DATE: 2012-03-22
 * AS3 (AS2 and JS versions are also available)
 * UPDATES AND DOCS AT: http://www.greensock.com
 **/
package com.greensock.easing {
/**
 * @private
 * Eases in with an overshoot, initially dipping below the starting value before accelerating towards the end.
 * 
 * <p><strong>Copyright 2013, GreenSock. All rights reserved.</strong> This work is subject to the terms in <a href="http://www.greensock.com/terms_of_use.html">http://www.greensock.com/terms_of_use.html</a> or for <a href="http://www.greensock.com/club/">Club GreenSock</a> members, the software agreement that was issued with the membership.</p>
 * 
 * @author Jack Doyle, jack@greensock.com
 **/
	final public class BackIn extends Ease {
		
		/** The default ease instance which can be reused many times in various tweens in order to conserve memory and improve performance slightly compared to creating a new instance each time. **/
		public static var ease:BackIn = new BackIn();
	
		/**
		 * Constructor
		 * 
		 * @param overshoot affects the degree or strength of the overshoot (default: 1.70158)
		 */
		public function BackIn(overshoot:Number=1.70158) {
			_p1 = overshoot;
		}
		
		/** @inheritDoc **/
		override public function getRatio(p:Number):Number {
			return p * p * ((_p1 + 1) * p - _p1);
		}
		
		/**
		 * Permits customization of the ease with various parameters.
		 * 
		 * @param overshoot affects the degree or strength of the overshoot	(default: 1.70158)
		 * @return new BackIn instance that is configured according to the parameters provided
		 */
		public function config(overshoot:Number=1.70158):BackIn {
			return new BackIn(overshoot);
		}
	
	}
	
}