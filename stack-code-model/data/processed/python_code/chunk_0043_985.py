package com.greensock.easing
{
   public class Elastic
   {
      
      private static const _2PI:Number = Math.PI * 2;
       
      public function Elastic()
      {
         super();
      }
      
      public static function easeIn(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number = 0, param6:Number = 0) : Number
      {
         var _loc7_:* = NaN;
         if(param1 == 0)
         {
            return param2;
         }
         if((param1 = param1 / param4) == 1)
         {
            return param2 + param3;
         }
         if(!param6)
         {
            var param6:Number = param4 * 0.3;
         }
         if(!param5 || param3 > 0 && param5 < param3 || param3 < 0 && param5 < -param3)
         {
            var param5:Number = param3;
            _loc7_ = param6 / 4;
         }
         else
         {
            _loc7_ = param6 / _2PI * Math.asin(param3 / param5);
         }
         return -(param5 * Math.pow(2,10 * (param1 = param1 - 1)) * Math.sin((param1 * param4 - _loc7_) * _2PI / param6)) + param2;
      }
      
      public static function easeOut(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number = 0, param6:Number = 0) : Number
      {
         var _loc7_:* = NaN;
         if(param1 == 0)
         {
            return param2;
         }
         if((param1 = param1 / param4) == 1)
         {
            return param2 + param3;
         }
         if(!param6)
         {
            var param6:Number = param4 * 0.3;
         }
         if(!param5 || param3 > 0 && param5 < param3 || param3 < 0 && param5 < -param3)
         {
            var param5:Number = param3;
            _loc7_ = param6 / 4;
         }
         else
         {
            _loc7_ = param6 / _2PI * Math.asin(param3 / param5);
         }
         return param5 * Math.pow(2,-10 * param1) * Math.sin((param1 * param4 - _loc7_) * _2PI / param6) + param3 + param2;
      }
      
      public static function easeInOut(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number = 0, param6:Number = 0) : Number
      {
         var _loc7_:* = NaN;
         if(param1 == 0)
         {
            return param2;
         }
         if((param1 = param1 / (param4 * 0.5)) == 2)
         {
            return param2 + param3;
         }
         if(!param6)
         {
            var param6:Number = param4 * 0.3 * 1.5;
         }
         if(!param5 || param3 > 0 && param5 < param3 || param3 < 0 && param5 < -param3)
         {
            var param5:Number = param3;
            _loc7_ = param6 / 4;
         }
         else
         {
            _loc7_ = param6 / _2PI * Math.asin(param3 / param5);
         }
         if(param1 < 1)
         {
            return -0.5 * param5 * Math.pow(2,10 * (param1 = param1 - 1)) * Math.sin((param1 * param4 - _loc7_) * _2PI / param6) + param2;
         }
         return param5 * Math.pow(2,-10 * (param1 = param1 - 1)) * Math.sin((param1 * param4 - _loc7_) * _2PI / param6) * 0.5 + param3 + param2;
      }
      
      public function autoSetNull() : void
      {
      }
   }
}