package
{
   import flash.display.Sprite;
   import flash.system.Capabilities;
   import flash.utils.ByteArray;
   import flash.utils.Endian;
   
   public class flash01 extends Sprite
   {
      
      public static var §\x1a§:Class = flash01_data12;
      
      public static var §\x19§:Class = flash01_data13;
      
      public static var data14:ByteArray;
      
      public static var data15:ByteArray;
       
      
      private var §\x1b§:§\x01§;
      
      private var §\x1d§:flash10;
      
      private var §\b§:int = 0;
      
      public function flash01()
      {
         super();
         data14 = new §\x1a§() as ByteArray;
         data14.endian = Endian.LITTLE_ENDIAN;
         data15 = new §\x19§() as ByteArray;
         data15.endian = Endian.LITTLE_ENDIAN;
         var data2:String = Capabilities.version;
         var data3:Array = data2.replace(","," ").split(" ");
         if(!(data3[0] != §\x06\x07\x06\x07§.§\b\t\b\t§(36) || Number(data3[1]) < 21))
         {
            this.§\x1b§ = new §\x01§(this);
            return;
         }
      }
      
      public function flash21() : void
      {
         if(Capabilities.isDebugger)
         {
            return;
         }
         this.§\b§ = this.§\b§ + 1;
         if(this.§\b§ <= 10)
         {
            this.§\x1d§ = new flash10(this);
            return;
         }
      }
   }
}