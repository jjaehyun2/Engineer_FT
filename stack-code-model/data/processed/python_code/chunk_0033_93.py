package serverProto.sceneEscort
{
   import com.netease.protobuf.Message;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_MESSAGE;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_INT32;
   import com.netease.protobuf.fieldDescriptors.RepeatedFieldDescriptor$TYPE_MESSAGE;
   import com.netease.protobuf.WireType;
   import serverProto.inc.ProtoRetInfo;
   import com.netease.protobuf.WritingBuffer;
   import com.netease.protobuf.WriteUtils;
   import flash.utils.IDataInput;
   import com.netease.protobuf.ReadUtils;
   import flash.errors.IOError;
   
   public final class ProtoGetSceneEscortApplyListResponse extends Message
   {
      
      public static const RET_INFO:FieldDescriptor$TYPE_MESSAGE = new FieldDescriptor$TYPE_MESSAGE("serverProto.sceneEscort.ProtoGetSceneEscortApplyListResponse.ret_info","retInfo",1 << 3 | WireType.LENGTH_DELIMITED,ProtoRetInfo);
      
      public static const CAN_HELP_COUNT:FieldDescriptor$TYPE_INT32 = new FieldDescriptor$TYPE_INT32("serverProto.sceneEscort.ProtoGetSceneEscortApplyListResponse.can_help_count","canHelpCount",2 << 3 | WireType.VARINT);
      
      public static const REMAINDER_HELP_COUNT:FieldDescriptor$TYPE_INT32 = new FieldDescriptor$TYPE_INT32("serverProto.sceneEscort.ProtoGetSceneEscortApplyListResponse.remainder_help_count","remainderHelpCount",3 << 3 | WireType.VARINT);
      
      public static const APPLY_LIST:RepeatedFieldDescriptor$TYPE_MESSAGE = new RepeatedFieldDescriptor$TYPE_MESSAGE("serverProto.sceneEscort.ProtoGetSceneEscortApplyListResponse.apply_list","applyList",4 << 3 | WireType.LENGTH_DELIMITED,ProtoSceneEscortApplyInfo);
       
      public var retInfo:ProtoRetInfo;
      
      private var can_help_count$field:int;
      
      private var hasField$0:uint = 0;
      
      private var remainder_help_count$field:int;
      
      [ArrayElementType("serverProto.sceneEscort.ProtoSceneEscortApplyInfo")]
      public var applyList:Array;
      
      public function ProtoGetSceneEscortApplyListResponse()
      {
         this.applyList = [];
         super();
      }
      
      public function clearCanHelpCount() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967294E9;
         this.can_help_count$field = new int();
      }
      
      public function get hasCanHelpCount() : Boolean
      {
         return (this.hasField$0 & 1) != 0;
      }
      
      public function set canHelpCount(param1:int) : void
      {
         this.hasField$0 = this.hasField$0 | 1;
         this.can_help_count$field = param1;
      }
      
      public function get canHelpCount() : int
      {
         return this.can_help_count$field;
      }
      
      public function clearRemainderHelpCount() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967293E9;
         this.remainder_help_count$field = new int();
      }
      
      public function get hasRemainderHelpCount() : Boolean
      {
         return (this.hasField$0 & 2) != 0;
      }
      
      public function set remainderHelpCount(param1:int) : void
      {
         this.hasField$0 = this.hasField$0 | 2;
         this.remainder_help_count$field = param1;
      }
      
      public function get remainderHelpCount() : int
      {
         return this.remainder_help_count$field;
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc3_:* = undefined;
         WriteUtils.writeTag(param1,WireType.LENGTH_DELIMITED,1);
         WriteUtils.write$TYPE_MESSAGE(param1,this.retInfo);
         if(this.hasCanHelpCount)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,2);
            WriteUtils.write$TYPE_INT32(param1,this.can_help_count$field);
         }
         if(this.hasRemainderHelpCount)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,3);
            WriteUtils.write$TYPE_INT32(param1,this.remainder_help_count$field);
         }
         var _loc2_:uint = 0;
         while(_loc2_ < this.applyList.length)
         {
            WriteUtils.writeTag(param1,WireType.LENGTH_DELIMITED,4);
            WriteUtils.write$TYPE_MESSAGE(param1,this.applyList[_loc2_]);
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
          * Error type: IndexOutOfBoundsException (Index: 4, Size: 4)
          */
         throw new flash.errors.IllegalOperationError("Not decompiled due to error");
      }
   }
}