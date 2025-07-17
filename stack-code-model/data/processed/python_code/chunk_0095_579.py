package ncolor {
	import npooling.IReusable;
	import npooling.Pool;
	
	public final class XYZColor implements IReusable {
		private static var _pool:Pool = Pool.getInstance();
		
		public var x:Number;
		public var y:Number;
		public var z:Number;
		
		public function XYZColor(pX:Number = 0.0, 
								 pY:Number = 0.0, 
								 pZ:Number = 0.0) {
			x = pX;
			y = pY;
			z = pZ;
		};
		
		public static function get BLACK():XYZColor {
			var result:XYZColor = _pool.get(XYZColor) as XYZColor;
			
			if (!result) {
				_pool.allocate(XYZColor, 1);
				result = new XYZColor();
			}
			
			return result;
		};
		
		public static function fromRGB(pColor:Color):XYZColor {
			var result:XYZColor = BLACK;
			
			var r:Number = adjust(pColor.r / Color.MAX) * 100;
			var g:Number = adjust(pColor.g / Color.MAX) * 100;
			var b:Number = adjust(pColor.b / Color.MAX) * 100;
			
			result.x = r * 0.4124 + g * 0.3576 + b * 0.1805;
			result.y = r * 0.2126 + g * 0.7152 + b * 0.0722;
			result.z = r * 0.0193 + g * 0.1192 + b * 0.9505;
			
			return result;
		};
		
		private static function adjust(pInput:Number):Number {
			if (pInput > 0.4045) {
				pInput = (pInput + 0.055) / 1.055;
				pInput = Math.pow(pInput, 2.4);
			} else {
				pInput = pInput / 12.92;
			}
			
			return pInput;
		};
		
		public function get reflection():Class {
			return XYZColor;
		};
		
		public function poolPrepare():void {
			x = y = z = 0.0;
		};
		
		public function dispose():void {
		};
	}
}