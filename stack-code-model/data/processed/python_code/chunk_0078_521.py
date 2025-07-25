package com.adobe.cep {
	/**
	 * @author harbs
	 */
	public class GradientColor {
		/**
		 * @class GradientColor
		 * Stores gradient color information.
		 *
		 * @param type          The gradient type, must be "linear".
		 * @param direction     A \c #Direction object for the direction of the gradient
		(up, down, right, or left).
		 * @param numStops          The number of stops in the gradient.
		 * @param gradientStopList  An array of \c #GradientStop objects.
		 *
		 * @return A new \c GradientColor object.
		 */
		public function GradientColor(info:Object) {
		    this.type = info.type;
    		this.direction = new Direction(info.direction);
    		this.numStops = info.numStops;
    		this.arrGradientStop = info.arrGradientStop;
		}

		public var type : String;
		public var direction : Direction;
		public var numStops : int;
		public var arrGradientStop : Array;
	}
}