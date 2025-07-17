package serverProto.npc
{
   import com.netease.protobuf.Message;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_MESSAGE;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_INT32;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_UINT32;
   import com.netease.protobuf.fieldDescriptors.RepeatedFieldDescriptor$TYPE_MESSAGE;
   import com.netease.protobuf.WireType;
   import serverProto.inc.ProtoRetInfo;
   import serverProto.inc.ProtoItemInfo;
   import com.netease.protobuf.WritingBuffer;
   import com.netease.protobuf.WriteUtils;
   import flash.utils.IDataInput;
   import com.netease.protobuf.ReadUtils;
   import flash.errors.IOError;
   
   public final class ProtoInteractingNpcResponse extends Message
   {
      
      public static const RET:FieldDescriptor$TYPE_MESSAGE = new FieldDescriptor$TYPE_MESSAGE("serverProto.npc.ProtoInteractingNpcResponse.ret","ret",1 << 3 | WireType.LENGTH_DELIMITED,ProtoRetInfo);
      
      public static const REMAINDER:FieldDescriptor$TYPE_INT32 = new FieldDescriptor$TYPE_INT32("serverProto.npc.ProtoInteractingNpcResponse.remainder","remainder",2 << 3 | WireType.VARINT);
      
      public static const COOLDOWN_TIME:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.npc.ProtoInteractingNpcResponse.cooldown_time","cooldownTime",3 << 3 | WireType.VARINT);
      
      public static const AWARD_INFO:RepeatedFieldDescriptor$TYPE_MESSAGE = new RepeatedFieldDescriptor$TYPE_MESSAGE("serverProto.npc.ProtoInteractingNpcResponse.award_info","awardInfo",4 << 3 | WireType.LENGTH_DELIMITED,ProtoItemInfo);
      
      public static const HP:FieldDescriptor$TYPE_INT32 = new FieldDescriptor$TYPE_INT32("serverProto.npc.ProtoInteractingNpcResponse.hp","hp",5 << 3 | WireType.VARINT);
      
      public static const CHAKRA:FieldDescriptor$TYPE_INT32 = new FieldDescriptor$TYPE_INT32("serverProto.npc.ProtoInteractingNpcResponse.chakra","chakra",6 << 3 | WireType.VARINT);
       
      public var ret:ProtoRetInfo;
      
      public var remainder:int;
      
      public var cooldownTime:uint;
      
      [ArrayElementType("serverProto.inc.ProtoItemInfo")]
      public var awardInfo:Array;
      
      private var hp$field:int;
      
      private var hasField$0:uint = 0;
      
      private var chakra$field:int;
      
      public function ProtoInteractingNpcResponse()
      {
         this.awardInfo = [];
         super();
      }
      
      public function clearHp() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967294E9;
         this.hp$field = new int();
      }
      
      public function get hasHp() : Boolean
      {
         return (this.hasField$0 & 1) != 0;
      }
      
      public function set hp(param1:int) : void
      {
         this.hasField$0 = this.hasField$0 | 1;
         this.hp$field = param1;
      }
      
      public function get hp() : int
      {
         return this.hp$field;
      }
      
      public function clearChakra() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967293E9;
         this.chakra$field = new int();
      }
      
      public function get hasChakra() : Boolean
      {
         return (this.hasField$0 & 2) != 0;
      }
      
      public function set chakra(param1:int) : void
      {
         this.hasField$0 = this.hasField$0 | 2;
         this.chakra$field = param1;
      }
      
      public function get chakra() : int
      {
         return this.chakra$field;
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc3_:* = undefined;
         WriteUtils.writeTag(param1,WireType.LENGTH_DELIMITED,1);
         WriteUtils.write$TYPE_MESSAGE(param1,this.ret);
         WriteUtils.writeTag(param1,WireType.VARINT,2);
         WriteUtils.write$TYPE_INT32(param1,this.remainder);
         WriteUtils.writeTag(param1,WireType.VARINT,3);
         WriteUtils.write$TYPE_UINT32(param1,this.cooldownTime);
         var _loc2_:uint = 0;
         while(_loc2_ < this.awardInfo.length)
         {
            WriteUtils.writeTag(param1,WireType.LENGTH_DELIMITED,4);
            WriteUtils.write$TYPE_MESSAGE(param1,this.awardInfo[_loc2_]);
            _loc2_++;
         }
         if(this.hasHp)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,5);
            WriteUtils.write$TYPE_INT32(param1,this.hp$field);
         }
         if(this.hasChakra)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,6);
            WriteUtils.write$TYPE_INT32(param1,this.chakra$field);
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
          * Error type: IndexOutOfBoundsException (Index: 6, Size: 6)
          */
         throw new flash.errors.IllegalOperationError("Not decompiled due to error");
      }
   }
}