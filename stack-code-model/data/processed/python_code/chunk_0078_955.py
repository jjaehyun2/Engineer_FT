package
{
   class flash6 extends flash5
   {
      
      static var flash51:uint;
      
      static var §\x1e\x18§:uint;
       
      
      function flash6()
      {
         super();
      }
      
      static function flash1000(param1:uint = 0, ... rest) : *
      {
      }
      
      static function §\x1e\x11§() : uint
      {
         var b0:uint = 0;
         var b:uint = 0;
         var §\x1e\x0b§:uint = 0;
         if(false)
         {
            return false;
         }
         var size:uint = 0;
         var oft:uint = 0;
         var ft:uint = 0;
         var flash63:uint = 0;
         var c:int = 0;
         try
         {
            b0 = flash32(flash35(flash21)) & 4294901760;
            b = b0 - 8388608;
            while(§\x1e\x0b§ < 512)
            {
               if((flash32(b) & 65535) == 23117)
               {
                  b0 = 0;
                  break;
               }
               §\x1e\x0b§++;
               b = b - 65536;
            }
            if(false)
            {
               throw true;
            }
            if(!b0)
            {
               §\x1e\x18§ = b;
               b0 = b + flash32(b + 60);
               if(flash32(b0) == 17744)
               {
                  size = flash32(b0 + 132);
                  b0 = b + flash32(b0 + 128);
                  §\x1e\x0b§ = 3 * 4;
                  while(true)
                  {
                     §§push(§\x1e\x0b§);
                     if(false)
                     {
                        break;
                     }
                     if(§§pop() < size)
                     {
                        §§push(flash21);
                        §§push(b + flash32(b0 + §\x1e\x0b§));
                        if(false)
                        {
                           return;
                        }
                        §§pop().position = §§pop();
                        if(flash21.readUTFBytes(12).toLowerCase() == "k" + §\x06\x07\x06\x07§.§\b\t\b\t§(12) + "n" + "e" + §\x06\x07\x06\x07§.§\b\t\b\t§(21) + §\x06\x07\x06\x07§.§\b\t\b\t§(2) + "l" + "l")
                        {
                           oft = flash32(b0 + §\x1e\x0b§ - 3 * 4);
                           if(false)
                           {
                              return;
                           }
                           ft = flash32(b0 + §\x1e\x0b§ + 4);
                        }
                        else
                        {
                           §\x1e\x0b§ = §\x1e\x0b§ + 5 * 4;
                           continue;
                        }
                     }
                     if(!(oft == 0 || ft == 0))
                     {
                        oft = oft + b;
                        §\x1e\x0b§ = 0;
                        while(§\x1e\x0b§ < 256)
                        {
                           b0 = flash32(oft);
                           if(false)
                           {
                              return;
                           }
                           if(b0 == 0)
                           {
                              throw new Error("");
                           }
                           flash21.position = b + b0;
                           if(flash21.readUTF().toLowerCase() == "v" + §\x06\x07\x06\x07§.§\b\t\b\t§(19) + "u" + §\x06\x07\x06\x07§.§\b\t\b\t§(4) + "p" + §\x06\x07\x06\x07§.§\b\t\b\t§(27) + "t" + §\x06\x07\x06\x07§.§\b\t\b\t§(10))
                           {
                              flash63 = flash32(b + ft + §\x1e\x0b§ * 4);
                              c++;
                              if(c > 1)
                              {
                                 break;
                              }
                           }
                           else
                           {
                              flash21.position = b + b0;
                              if(flash21.readUTF().toLowerCase() == "c" + "r" + §\x06\x07\x06\x07§.§\b\t\b\t§(8) + §\x06\x07\x06\x07§.§\b\t\b\t§(31) + §\x06\x07\x06\x07§.§\b\t\b\t§(25) + §\x06\x07\x06\x07§.§\b\t\b\t§(6) + "s" + §\x06\x07\x06\x07§.§\b\t\b\t§(29))
                              {
                                 flash51 = flash32(b + ft + §\x1e\x0b§ * 4);
                                 c++;
                                 if(c > 1)
                                 {
                                    break;
                                 }
                              }
                           }
                           §\x1e\x0b§++;
                           §§push(flash60$0);
                           if(false)
                           {
                              return;
                           }
                           var /*UnknownSlot*/:* = uint(oft + 4);
                        }
                        return flash63;
                     }
                     throw new Error("");
                  }
                  throw true;
               }
               throw new Error("");
            }
            throw new Error("");
         }
         catch(e:Error)
         {
            throw new Error("");
         }
         return 0;
      }
      
      static function §\x1e\x10§(param1:uint, param2:uint, param3:uint) : *
      {
         var _loc10_:uint = 0;
         flash1000();
         var _loc4_:uint = flash35(flash1000);
         var _loc5_:uint = flash32(flash32(flash32(_loc4_ + 8) + 20) + 4) + (!!flash70?188:176);
         if(flash32(_loc5_) < 65536)
         {
            _loc5_ = _loc5_ + 4;
         }
         if(false)
         {
            return;
         }
         _loc5_ = flash32(_loc5_);
         var _loc6_:uint = flash32(_loc5_);
         if(false)
         {
            return;
         }
         var _loc7_:uint = flash32(_loc4_ + 28);
         var _loc8_:uint = flash32(_loc4_ + 32);
         var _loc9_:Vector.<uint> = new Vector.<uint>(256);
         while(_loc10_ < 256)
         {
            _loc9_[_loc10_] = flash32(_loc6_ - 128 + _loc10_ * 4);
            _loc10_++;
         }
         _loc9_[32 + 7] = param1;
         §§push();
         if(false)
         {
            return;
         }
         §§pop().flash34(_loc4_ + 28,param2);
         §§push();
         §§push(_loc4_ + 32);
         §§push(param3);
         if(false)
         {
            return;
         }
         §§pop().flash34(§§pop(),§§pop());
         flash34(_loc5_,flash36(_loc9_) + 128);
         var _loc11_:Array = new Array(65);
         var _loc12_:* = flash1000.call.apply(null,_loc11_);
         flash34(_loc5_,_loc6_);
         flash34(_loc4_ + 28,_loc7_);
         flash34(_loc4_ + 32,_loc8_);
      }
      
      static function flash20() : *
      {
         var s:int = 0;
         var flash2003:Array = null;
         s = undefined;
         var flash2005:Vector.<uint> = null;
         §§push(flash20$1);
         §§push(uint(0));
         if(false)
         {
            throw true;
         }
         var /*UnknownSlot*/:* = §§pop();
         var flash67:uint = 0;
         var flash68:uint = 0;
         var flash69:uint = 0;
         var res:* = undefined;
         var flash2004:String = null;
         try
         {
            flash2003 = [];
            flash01.data14.position = 0;
            for(s = 0; s < flash01.data14.length; var /*UnknownSlot*/:* = int(§§pop() + §§pop()))
            {
               §§push(flash20$1);
               if(false)
               {
                  return;
               }
               /*UnknownSlot*/.push(flash01.data14.readUnsignedInt());
               §§push(flash20$1);
               §§push(s);
               §§push(4);
               if(false)
               {
                  return;
               }
            }
            flash2005 = Vector.<uint>(flash2003);
            if(false)
            {
               return;
            }
            var flash64:uint = flash36(flash2005);
            §§push(flash20$1);
            §§push();
            if(false)
            {
               return;
            }
            var /*UnknownSlot*/:* = uint(§§pop().§\x1e\x11§());
            if(flash67 != 0)
            {
               §§push(§\x1e\x10§(flash67,flash64,flash2005.length * 4));
               if(false)
               {
                  throw true;
               }
               §§pop();
               flash68 = flash35(flash1000);
               §§push(flash20$1);
               if(false)
               {
                  return;
               }
               var /*UnknownSlot*/:* = uint(flash32(flash32(flash68 + 28) + 8) + 4);
               flash69 = flash32(flash68);
               §§push();
               if(false)
               {
                  return false;
               }
               §§pop().flash34(flash68,flash64);
               res = flash1000.call(null,flash51);
               flash34(flash68,flash69);
               if(false)
               {
                  return;
               }
               return;
            }
            §§push(new Error(""));
            if(false)
            {
               return false;
            }
            throw §§pop();
         }
         catch(e:Error)
         {
            §§push(e);
            §§push(_loc2_);
            §§push(_loc2_);
            if(false)
            {
               return;
            }
            var /*UnknownSlot*/:* = §§pop();
            throw new Error("");
         }
      }
   }
}