package LS_Classes
{
   import flash.display.Sprite;
   import flash.geom.Point;
   
   public class LSDottedLine extends Sprite
   {
       
      
      private var m_StartX:Number;
      
      private var m_StartY:Number;
      
      private var m_EndX:Number;
      
      private var m_EndY:Number;
      
      private var m_Thikness:Number;
      
      private var m_LineWidth:Number;
      
      private var m_SpaceWidth:Number;
      
      private var m_Color:uint;
      
      public function LSDottedLine(param1:Number = 1.0, param2:Number = 1.0, param3:Number = 1.0, param4:uint = 0)
      {
         super();
         this.m_StartX = 0;
         this.m_StartY = 0;
         this.m_EndX = 0;
         this.m_EndY = 0;
         this.m_Thikness = param1;
         this.m_LineWidth = param2;
         this.m_SpaceWidth = param3;
         this.m_Color = param4;
      }
      
      public function setPattern(param1:Number, param2:Number, param3:Boolean = true) : void
      {
         this.m_LineWidth = param1;
         this.m_SpaceWidth = param2;
         if(param3)
         {
            this.validate();
         }
      }
      
      public function setThickness(param1:Number, param2:Boolean = true) : void
      {
         this.m_Thikness = param1;
         if(param2)
         {
            this.validate();
         }
      }
      
      public function setColor(param1:uint, param2:Boolean = true) : void
      {
         this.m_Color = param1;
         if(param2)
         {
            this.validate();
         }
      }
      
      public function setStartEndpoint(param1:Point, param2:Boolean = true) : void
      {
         this.m_StartX = param1.x;
         this.m_StartY = param1.y;
         if(param2)
         {
            this.validate();
         }
      }
      
      public function setEndEndpoint(param1:Point, param2:Boolean = true) : void
      {
         this.m_EndX = param1.x;
         this.m_EndY = param1.y;
         if(param2)
         {
            this.validate();
         }
      }
      
      public function setEndpoints(param1:Point, param2:Point, param3:Boolean = true) : void
      {
         this.m_StartX = param1.x;
         this.m_StartY = param1.y;
         this.m_EndX = param2.x;
         this.m_EndY = param2.y;
         if(param3)
         {
            this.validate();
         }
      }
      
      private function validate() : void
      {
         var _loc1_:Number = Math.sqrt((this.m_EndX - this.m_StartX) * (this.m_EndX - this.m_StartX) + (this.m_EndY - this.m_StartY) * (this.m_EndY - this.m_StartY));
         var _loc2_:Number = Math.atan2(this.m_EndY - this.m_StartY,this.m_EndX - this.m_StartX);
         graphics.clear();
         graphics.lineStyle(0,this.m_Color);
         graphics.beginFill(this.m_Color);
         var _loc3_:Number = this.m_LineWidth + this.m_SpaceWidth;
         var _loc4_:* = 0;
         while(_loc4_ < _loc1_)
         {
            graphics.drawRect(_loc4_,0,this.m_LineWidth,this.m_Thikness);
            _loc4_ = _loc4_ + _loc3_;
         }
         graphics.endFill();
         this.rotation = _loc2_ / Math.PI * 180;
      }
      
      private function colorARGB(param1:uint, param2:uint) : uint
      {
         var _loc3_:uint = 0;
         _loc3_ = _loc3_ + (param2 << 24);
         _loc3_ = _loc3_ + param1;
         return _loc3_;
      }
   }
}