package com.greensock.plugins
{
   import com.greensock.TweenLite;
   import flash.display.MovieClip;
   
   public class FrameLabelPlugin extends FramePlugin
   {
      
      public static const API:Number = 2;
       
      
      public function FrameLabelPlugin()
      {
         super();
         _propName = "frameLabel";
      }
      
      override public function _onInitTween(param1:Object, param2:*, param3:TweenLite) : Boolean
      {
         if(!param3.target is MovieClip)
         {
            return false;
         }
         _target = param1 as MovieClip;
         this.frame = _target.currentFrame;
         var _loc4_:Array = _target.currentLabels;
         var _loc5_:String = param2;
         var _loc6_:int = _target.currentFrame;
         var _loc7_:int = _loc4_.length;
         while(--_loc7_ > -1)
         {
            if(_loc4_[_loc7_].name == _loc5_)
            {
               _loc6_ = _loc4_[_loc7_].frame;
               break;
            }
         }
         if(this.frame != _loc6_)
         {
            _addTween(this,"frame",this.frame,_loc6_,"frame",true);
         }
         return true;
      }
   }
}