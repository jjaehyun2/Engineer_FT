package littleGame.events
{
   import flash.events.Event;
   
   public class LittleLivingEvent extends Event
   {
      
      public static const Die:String = "die";
      
      public static const PosChenged:String = "posChanged";
      
      public static const Collided:String = "collide";
      
      public static const DirectionChanged:String = "directionChanged";
      
      public static const DoAction:String = "doAction";
      
      public static const InhaledChanged:String = "inhaledChanged";
      
      public static const GetScore:String = "getscore";
      
      public static const HeadChanged:String = "headChanged";
       
      
      private var _paras:Array;
      
      public function LittleLivingEvent(param1:String, ... rest)
      {
         this._paras = rest;
         super(param1);
      }
      
      public function get paras() : Array
      {
         return this._paras;
      }
   }
}