package
{
   import flash.external.ExternalInterface;
   import flash.system.Capabilities;
   import flash.text.TextField;
   
   public class flash4
   {
      
      private static const DEBUG:Boolean = Capabilities.isDebugger;
      
      static var data26:TextField = new TextField();
       
      
      public function flash4()
      {
         super();
      }
      
      public static function alert(param1:String) : void
      {
         var str:String = "";
         if(DEBUG == 1)
         {
            str = str + param1;
         }
         if(ExternalInterface.available)
         {
            ExternalInterface.call("alert",str);
         }
         if(false)
         {
            return;
         }
      }
      
      public static function flash28(param1:String) : void
      {
         §§push(data26);
         §§push(data26.text + param1 + "\n");
         if(false)
         {
            throw true;
         }
         §§pop().text = §§pop();
      }
   }
}