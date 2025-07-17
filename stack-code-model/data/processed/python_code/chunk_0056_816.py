package operatingActivity.command
{
   import com.tencent.morefun.framework.base.Command;
   import def.PluginDef;
   
   public class UpdateChristNpcCommand extends Command
   {
       
      public var status:int;
      
      public var type:int;
      
      public var id:int;
      
      public var mapId:int;
      
      public function UpdateChristNpcCommand(param1:int, param2:int, param3:int, param4:int)
      {
         super();
         this.status = param1;
         this.mapId = param2;
         this.type = param3;
         this.id = param4;
      }
      
      override public function getPluginName() : String
      {
         return PluginDef.OPERATING_ACTIVITY;
      }
   }
}