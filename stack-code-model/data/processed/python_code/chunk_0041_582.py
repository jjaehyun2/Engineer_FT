package com.greensock.plugins
{
   public class FrameBackwardPlugin extends FrameForwardPlugin
   {
      
      public static const API:Number = 1;
       
      public function FrameBackwardPlugin()
      {
         super();
         this.propName = "frameBackward";
         _backward = true;
      }
      
      override public function autoSetNull() : void
      {
         if(super.hasOwnProperty("autoSetNull"))
         {
            super.["autoSetNull"]();
         }
      }
   }
}