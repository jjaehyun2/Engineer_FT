package serverProto.dungeon
{
   import com.netease.protobuf.Message;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_MESSAGE;
   import com.netease.protobuf.fieldDescriptors.RepeatedFieldDescriptor$TYPE_MESSAGE;
   import com.netease.protobuf.WireType;
   import serverProto.inc.ProtoRetInfo;
   import com.netease.protobuf.WritingBuffer;
   import com.netease.protobuf.WriteUtils;
   import flash.utils.IDataInput;
   import com.netease.protobuf.ReadUtils;
   import flash.errors.IOError;
   
   public final class ProtoGetBefallDungeonListResponse extends Message
   {
      
      public static const RET:FieldDescriptor$TYPE_MESSAGE = new FieldDescriptor$TYPE_MESSAGE("serverProto.dungeon.ProtoGetBefallDungeonListResponse.ret","ret",1 << 3 | WireType.LENGTH_DELIMITED,ProtoRetInfo);
      
      public static const BEFALL_DUNGEON_LIST:RepeatedFieldDescriptor$TYPE_MESSAGE = new RepeatedFieldDescriptor$TYPE_MESSAGE("serverProto.dungeon.ProtoGetBefallDungeonListResponse.befall_dungeon_list","befallDungeonList",2 << 3 | WireType.LENGTH_DELIMITED,ProtoBefallDungeonInfo);
       
      private var ret$field:ProtoRetInfo;
      
      [ArrayElementType("serverProto.dungeon.ProtoBefallDungeonInfo")]
      public var befallDungeonList:Array;
      
      public function ProtoGetBefallDungeonListResponse()
      {
         this.befallDungeonList = [];
         super();
      }
      
      public function clearRet() : void
      {
         this.ret$field = null;
      }
      
      public function get hasRet() : Boolean
      {
         return this.ret$field != null;
      }
      
      public function set ret(param1:ProtoRetInfo) : void
      {
         this.ret$field = param1;
      }
      
      public function get ret() : ProtoRetInfo
      {
         return this.ret$field;
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc3_:* = undefined;
         if(this.hasRet)
         {
            WriteUtils.writeTag(param1,WireType.LENGTH_DELIMITED,1);
            WriteUtils.write$TYPE_MESSAGE(param1,this.ret$field);
         }
         var _loc2_:uint = 0;
         while(_loc2_ < this.befallDungeonList.length)
         {
            WriteUtils.writeTag(param1,WireType.LENGTH_DELIMITED,2);
            WriteUtils.write$TYPE_MESSAGE(param1,this.befallDungeonList[_loc2_]);
            _loc2_++;
         }
         for(_loc3_ in this)
         {
            super.writeUnknown(param1,_loc3_);
         }
      }
      
      override final function readFromSlice(param1:IDataInput, param2:uint) : void
      {
         /*
          * Decompilation error
          * Code may be obfuscated
          * Tip: You can try enabling "Automatic deobfuscation" in Settings
          * Error type: IndexOutOfBoundsException (Index: 2, Size: 2)
          */
         throw new flash.errors.IllegalOperationError("Not decompiled due to error");
      }
   }
}