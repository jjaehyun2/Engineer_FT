////////////////////////////////////////////////////////////////////////////////
//
//  (C) 2010 BlooDHounD
//
////////////////////////////////////////////////////////////////////////////////

package by.blooddy.crypto {

	import com.adobe.crypto.MD5;
	
	/**
	 * @author					BlooDHounD
	 * @version					1.0
	 * @playerversion			Flash 10
	 * @langversion				3.0
	 */
	public class MD5Test extends BinaryTest {

		//--------------------------------------------------------------------------
		//
		//  Constructor
		//
		//--------------------------------------------------------------------------
		
		public function MD5Test() {
			super();
		}

		//--------------------------------------------------------------------------
		//
		//  Tests
		//
		//--------------------------------------------------------------------------
		
		[Test( description="by.blooddy.crypto.MD5", order=1 )]
		public function bloddy_crypto_md5():void {
			by.blooddy.crypto.MD5.hashBytes( _BIN );
		}
		
		[Test( description="com.adobe.crypto.MD5", order=2 )]
		public function as3corelib_md5():void {
			com.adobe.crypto.MD5.hashBytes( _BIN );
		}

	}

}