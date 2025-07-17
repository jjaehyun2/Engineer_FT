package com.illuzor.spinner.utils {
	
	import com.hurlant.crypto.prng.ARC4;
	import flash.utils.ByteArray;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public function encrypt(data:ByteArray, key:ByteArray):void {
		var encoder:ARC4 = new ARC4(key);
		encoder.encrypt(data);
		key.clear();
	}
}