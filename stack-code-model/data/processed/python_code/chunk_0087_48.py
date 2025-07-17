package com.illuzor.otherside.utils {
	
	import com.hurlant.crypto.prng.ARC4;
	import flash.utils.ByteArray;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public function decrypt(data:ByteArray, key:ByteArray):void {
		var encoder:ARC4 = new ARC4(key);
		encoder.decrypt(data);
		key.clear();
	}
}