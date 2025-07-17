package serverProto.knowledgeTest
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
   
   public final class ProtoKnowledgeTestVoteResponse extends Message
   {
      
      public static const RET_INFO:FieldDescriptor$TYPE_MESSAGE = new FieldDescriptor$TYPE_MESSAGE("serverProto.knowledgeTest.ProtoKnowledgeTestVoteResponse.ret_info","retInfo",1 << 3 | WireType.LENGTH_DELIMITED,ProtoRetInfo);
      
      public static const NPC_DATA_ARY:RepeatedFieldDescriptor$TYPE_MESSAGE = new RepeatedFieldDescriptor$TYPE_MESSAGE("serverProto.knowledgeTest.ProtoKnowledgeTestVoteResponse.npc_data_ary","npcDataAry",2 << 3 | WireType.LENGTH_DELIMITED,ProtoKnowledgeTestNpcData);
       
      public var retInfo:ProtoRetInfo;
      
      [ArrayElementType("serverProto.knowledgeTest.ProtoKnowledgeTestNpcData")]
      public var npcDataAry:Array;
      
      public function ProtoKnowledgeTestVoteResponse()
      {
         this.npcDataAry = [];
         super();
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc3_:* = undefined;
         WriteUtils.writeTag(param1,WireType.LENGTH_DELIMITED,1);
         WriteUtils.write$TYPE_MESSAGE(param1,this.retInfo);
         var _loc2_:uint = 0;
         while(_loc2_ < this.npcDataAry.length)
         {
            WriteUtils.writeTag(param1,WireType.LENGTH_DELIMITED,2);
            WriteUtils.write$TYPE_MESSAGE(param1,this.npcDataAry[_loc2_]);
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