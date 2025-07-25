package de.dittner.siegmar.utils {
public class ClassUtils {
	public function ClassUtils() {
	}

	public static function instantiate(clazz:Class, args:Array = null):* {
		var result:*;
		var a:Array = (args == null) ? [] : args;

		switch (a.length) {
			case 0:
				result = new clazz();
				break;
			case 1:
				result = new clazz(a[0]);
				break;
			case 2:
				result = new clazz(a[0], a[1]);
				break;
			case 3:
				result = new clazz(a[0], a[1], a[2]);
				break;
			case 4:
				result = new clazz(a[0], a[1], a[2], a[3]);
				break;
			case 5:
				result = new clazz(a[0], a[1], a[2], a[3], a[4]);
				break;
			case 6:
				result = new clazz(a[0], a[1], a[2], a[3], a[4], a[5]);
				break;
			case 7:
				result = new clazz(a[0], a[1], a[2], a[3], a[4], a[5], a[6]);
				break;
			case 8:
				result = new clazz(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7]);
				break;
			case 9:
				result = new clazz(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8]);
				break;
			case 10:
				result = new clazz(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9]);
				break;
			default:
				throw new Error("Too many args for constructor: " + clazz);
		}

		return result;
	}
}
}