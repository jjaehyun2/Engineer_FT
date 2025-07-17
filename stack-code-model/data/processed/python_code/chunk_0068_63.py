class mx.transitions.easing.None
{
	function None () {
	}
	static function easeNone(t, b, c, d) {
		return(((c * t) / d) + b);
	}
	static function easeIn(t, b, c, d) {
		return(((c * t) / d) + b);
	}
	static function easeOut(t, b, c, d) {
		return(((c * t) / d) + b);
	}
	static function easeInOut(t, b, c, d) {
		return(((c * t) / d) + b);
	}
	static var version = "1.1.0.52";
}