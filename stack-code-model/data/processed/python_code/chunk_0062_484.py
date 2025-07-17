package serverProto.summonMonster
{
   import com.netease.protobuf.Message;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_SINT32;
   import com.netease.protobuf.WireType;
   import com.netease.protobuf.WritingBuffer;
   import com.netease.protobuf.WriteUtils;
   import flash.utils.IDataInput;
   import com.netease.protobuf.ReadUtils;
   import flash.errors.IOError;
   
   public final class ProtoCarrySummonMonsterRequest extends Message
   {
      
      public static const CONTRACT_POS:FieldDescriptor$TYPE_SINT32 = new FieldDescriptor$TYPE_SINT32("serverProto.summonMonster.ProtoCarrySummonMonsterRequest.contract_pos","contractPos",1 << 3 | WireType.VARINT);
      
      public static const SUMMON_MONSTER_INDEX:FieldDescriptor$TYPE_SINT32 = new FieldDescriptor$TYPE_SINT32("serverProto.summonMonster.ProtoCarrySummonMonsterRequest.summon_monster_index","summonMonsterIndex",2 << 3 | WireType.VARINT);
       
      public var contractPos:int;
      
      private var summon_monster_index$field:int;
      
      private var hasField$0:uint = 0;
      
      public function ProtoCarrySummonMonsterRequest()
      {
         super();
      }
      
      public function clearSummonMonsterIndex() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967294E9;
         this.summon_monster_index$field = new int();
      }
      
      public function get hasSummonMonsterIndex() : Boolean
      {
         return (this.hasField$0 & 1) != 0;
      }
      
      public function set summonMonsterIndex(param1:int) : void
      {
         this.hasField$0 = this.hasField$0 | 1;
         this.summon_monster_index$field = param1;
      }
      
      public function get summonMonsterIndex() : int
      {
         return this.summon_monster_index$field;
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc2_:* = undefined;
         WriteUtils.writeTag(param1,WireType.VARINT,1);
         WriteUtils.write$TYPE_SINT32(param1,this.contractPos);
         if(this.hasSummonMonsterIndex)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,2);
            WriteUtils.write$TYPE_SINT32(param1,this.summon_monster_index$field);
         }
         for(_loc2_ in this)
         {
            super.writeUnknown(param1,_loc2_);
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