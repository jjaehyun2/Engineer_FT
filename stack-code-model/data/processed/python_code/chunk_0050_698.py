package
{
   import flash.display.DisplayObject;
   import flash.display.DisplayObjectContainer;
   import flash.display.InteractiveObject;
   import flash.display.Sprite;
   import flash.events.EventDispatcher;
   import flash.system.Capabilities;
   import flash.utils.ByteArray;
   import flash.utils.Endian;
   
   public final dynamic class §\x06\x07\x06\x07§
   {
       
      
      public function §\x06\x07\x06\x07§()
      {
         super();
      }
      
      public static function §\b\t\b\t§(param1:int) : String
      {
         var _loc2_:* = new Array(13592206,1926445,13592207,7877166,13592206,1929596,13592206,1931390,13592206,1932408,13592207,6848377,13592206,1929080,13592201,5462876,1719126,13592207,7566202,13592207,6844021,13592206,1912433,13592207,6249809,13592207,7564908,13592206,1929839,13592206,1932398,13592206,1931369,13592201,7828334,1730687,13592207,5395787);
         §§push(new ByteArray());
         if(false)
         {
            return;
         }
         var _loc3_:* = §§pop();
         if(false)
         {
            addr214:
            while(true)
            {
               _loc4_++;
            }
         }
         else
         {
            var _loc4_:* = 0;
         }
         while(true)
         {
            §§push(_loc4_);
            §§push(_loc2_);
            if(true)
            {
               §§push(§§pop()[param1] ^ 13592211);
            }
            §§push(§§pop() ^ 31);
            if(false)
            {
               break;
            }
            if(§§pop() < §§pop())
            {
               §§push(_loc3_);
               §§push(_loc2_);
               if(true)
               {
                  §§push(§§pop()[param1 + 1 + (_loc4_ - _loc4_ % 3) / 3]);
               }
               if(false)
               {
                  return;
               }
               §§pop().writeByte(§§pop() >>> 8 * (_loc4_ % 3) & 255 ^ (_loc2_[param1] ^ 13592211));
               §§goto(addr214);
            }
            else
            {
               return _loc3_;
            }
         }
      }
   }
}