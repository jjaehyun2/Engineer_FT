package starling.animation.easing {

	/**
	 * Quad
	 * Easing equations (t*t) for the KTween class
	 * @author Yusuke Kawasaki
	 * @version 1.0
	 */	
	public class Quad {
		/**
		 * Easing equation function for quad tween
		 * @param t		Current time (0.0: begin, 1.0:end)
		 * @return      Current ratio (0.0: begin, 1.0:end) 
		 */
		static public function easeIn(t:Number):Number {
			return t * t;
		}

		/**
		 * Easing equation function for quad tween
		 * @param t		Current time (0.0: begin, 1.0:end)
		 * @return      Current ratio (0.0: begin, 1.0:end) 
		 */
		static public function easeOut(t:Number):Number {
			return 1.0 - easeIn(1.0 - t);
		}

		/**
		 * Easing equation function for quad tween
		 * @param t		Current time (0.0: begin, 1.0:end)
		 * @return      Current ratio (0.0: begin, 1.0:end) 
		 */
		static public function easeInOut(t:Number):Number {
			return (t < 0.5) ? easeIn(t * 2.0) * 0.5 : 1 - easeIn(2.0 - t * 2.0) * 0.5;
		}
	}
}