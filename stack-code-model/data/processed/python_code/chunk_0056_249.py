package com.greensock.plugins
{
   import flash.filters.ColorMatrixFilter;
   import com.greensock.TweenLite;
   
   public class ColorMatrixFilterPlugin extends FilterPlugin
   {
      
      public function ColorMatrixFilterPlugin()
      {
         super("colorMatrixFilter");
      }
      
      public static const API:Number = 2;
      
      public static function setSaturation(param1:Array, param2:Number) : Array
      {
         if(isNaN(param2))
         {
            return param1;
         }
         var _loc3_:Number = 1 - param2;
         var _loc4_:Number = _loc3_ * _lumR;
         var _loc5_:Number = _loc3_ * _lumG;
         var _loc6_:Number = _loc3_ * _lumB;
         var _loc7_:Array = [_loc4_ + param2,_loc5_,_loc6_,0,0,_loc4_,_loc5_ + param2,_loc6_,0,0,_loc4_,_loc5_,_loc6_ + param2,0,0,0,0,0,1,0];
         return applyMatrix(_loc7_,param1);
      }
      
      public static function setHue(param1:Array, param2:Number) : Array
      {
         if(isNaN(param2))
         {
            return param1;
         }
         var param2:Number = param2 * Math.PI / 180;
         var _loc3_:Number = Math.cos(param2);
         var _loc4_:Number = Math.sin(param2);
         var _loc5_:Array = [_lumR + _loc3_ * (1 - _lumR) + _loc4_ * -_lumR,_lumG + _loc3_ * -_lumG + _loc4_ * -_lumG,_lumB + _loc3_ * -_lumB + _loc4_ * (1 - _lumB),0,0,_lumR + _loc3_ * -_lumR + _loc4_ * 0.143,_lumG + _loc3_ * (1 - _lumG) + _loc4_ * 0.14,_lumB + _loc3_ * -_lumB + _loc4_ * -0.283,0,0,_lumR + _loc3_ * -_lumR + _loc4_ * -(1 - _lumR),_lumG + _loc3_ * -_lumG + _loc4_ * _lumG,_lumB + _loc3_ * (1 - _lumB) + _loc4_ * _lumB,0,0,0,0,0,1,0,0,0,0,0,1];
         return applyMatrix(_loc5_,param1);
      }
      
      private static var _propNames:Array = [];
      
      protected static var _lumG:Number = 0.71516;
      
      public static function setContrast(param1:Array, param2:Number) : Array
      {
         if(isNaN(param2))
         {
            return param1;
         }
         var param2:Number = param2 + 0.01;
         var _loc3_:Array = [param2,0,0,0,128 * (1 - param2),0,param2,0,0,128 * (1 - param2),0,0,param2,0,128 * (1 - param2),0,0,0,1,0];
         return applyMatrix(_loc3_,param1);
      }
      
      protected static var _lumR:Number = 0.212671;
      
      public static function applyMatrix(param1:Array, param2:Array) : Array
      {
         var _loc6_:* = 0;
         var _loc7_:* = 0;
         if(!(param1 is Array) || !(param2 is Array))
         {
            return param2;
         }
         var _loc3_:Array = [];
         var _loc4_:* = 0;
         var _loc5_:* = 0;
         _loc6_ = 0;
         while(_loc6_ < 4)
         {
            _loc7_ = 0;
            while(_loc7_ < 5)
            {
               _loc5_ = _loc7_ == 4?param1[_loc4_ + 4]:0;
               _loc3_[_loc4_ + _loc7_] = param1[_loc4_] * param2[_loc7_] + param1[_loc4_ + 1] * param2[_loc7_ + 5] + param1[_loc4_ + 2] * param2[_loc7_ + 10] + param1[_loc4_ + 3] * param2[_loc7_ + 15] + _loc5_;
               _loc7_ = _loc7_ + 1;
            }
            _loc4_ = _loc4_ + 5;
            _loc6_ = _loc6_ + 1;
         }
         return _loc3_;
      }
      
      public static function setThreshold(param1:Array, param2:Number) : Array
      {
         if(isNaN(param2))
         {
            return param1;
         }
         var _loc3_:Array = [_lumR * 256,_lumG * 256,_lumB * 256,0,-256 * param2,_lumR * 256,_lumG * 256,_lumB * 256,0,-256 * param2,_lumR * 256,_lumG * 256,_lumB * 256,0,-256 * param2,0,0,0,1,0];
         return applyMatrix(_loc3_,param1);
      }
      
      public static function colorize(param1:Array, param2:Number, param3:Number = 1) : Array
      {
         if(isNaN(param2))
         {
            return param1;
         }
         if(isNaN(param3))
         {
            param3 = 1;
         }
         var _loc4_:Number = (param2 >> 16 & 255) / 255;
         var _loc5_:Number = (param2 >> 8 & 255) / 255;
         var _loc6_:Number = (param2 & 255) / 255;
         var _loc7_:Number = 1 - param3;
         var _loc8_:Array = [_loc7_ + param3 * _loc4_ * _lumR,param3 * _loc4_ * _lumG,param3 * _loc4_ * _lumB,0,0,param3 * _loc5_ * _lumR,_loc7_ + param3 * _loc5_ * _lumG,param3 * _loc5_ * _lumB,0,0,param3 * _loc6_ * _lumR,param3 * _loc6_ * _lumG,_loc7_ + param3 * _loc6_ * _lumB,0,0,0,0,0,1,0];
         return applyMatrix(_loc8_,param1);
      }
      
      public static function setBrightness(param1:Array, param2:Number) : Array
      {
         if(isNaN(param2))
         {
            return param1;
         }
         var param2:Number = param2 * 100 - 100;
         return applyMatrix([1,0,0,0,param2,0,1,0,0,param2,0,0,1,0,param2,0,0,0,1,0,0,0,0,0,1],param1);
      }
      
      protected static var _idMatrix:Array = [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0];
      
      protected static var _lumB:Number = 0.072169;
      
      protected var _matrix:Array;
      
      override public function setRatio(param1:Number) : void
      {
         _matrixTween.setRatio(param1);
         ColorMatrixFilter(_filter).matrix = _matrix;
         super.setRatio(param1);
      }
      
      protected var _matrixTween:EndArrayPlugin;
      
      override public function _onInitTween(param1:Object, param2:*, param3:TweenLite) : Boolean
      {
         var _loc4_:Object = param2;
         _initFilter(param1,{
            "remove":param2.remove,
            "index":param2.index,
            "addFilter":param2.addFilter
         },param3,ColorMatrixFilter,new ColorMatrixFilter(_idMatrix.slice()),_propNames);
         if(_filter == null)
         {
            trace("FILTER NULL! ");
            return true;
         }
         _matrix = ColorMatrixFilter(_filter).matrix;
         var _loc5_:Array = [];
         if(!(_loc4_.matrix == null) && _loc4_.matrix is Array)
         {
            _loc5_ = _loc4_.matrix;
         }
         else
         {
            if(_loc4_.relative == true)
            {
               _loc5_ = _matrix.slice();
            }
            else
            {
               _loc5_ = _idMatrix.slice();
            }
            _loc5_ = setBrightness(_loc5_,_loc4_.brightness);
            _loc5_ = setContrast(_loc5_,_loc4_.contrast);
            _loc5_ = setHue(_loc5_,_loc4_.hue);
            _loc5_ = setSaturation(_loc5_,_loc4_.saturation);
            _loc5_ = setThreshold(_loc5_,_loc4_.threshold);
            if(!isNaN(_loc4_.colorize))
            {
               _loc5_ = colorize(_loc5_,_loc4_.colorize,_loc4_.amount);
            }
         }
         _matrixTween = new EndArrayPlugin();
         _matrixTween._init(_matrix,_loc5_);
         return true;
      }
   }
}