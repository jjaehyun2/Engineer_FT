package serverProto.summonMonster
{
   import com.netease.protobuf.Message;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_INT32;
   import com.netease.protobuf.fieldDescriptors.RepeatedFieldDescriptor$TYPE_MESSAGE;
   import com.netease.protobuf.WireType;
   import serverProto.inc.ProtoItemInfo;
   import com.netease.protobuf.WritingBuffer;
   import com.netease.protobuf.WriteUtils;
   import flash.utils.IDataInput;
   import com.netease.protobuf.ReadUtils;
   import flash.errors.IOError;
   
   public final class ProtoCaptureFightFinishNotify extends Message
   {
      
      public static const SUMMON_MONSTER_ID:FieldDescriptor$TYPE_INT32 = new FieldDescriptor$TYPE_INT32("serverProto.summonMonster.ProtoCaptureFightFinishNotify.summon_monster_id","summonMonsterId",1 << 3 | WireType.VARINT);
      
      public static const REWARD_LIST:RepeatedFieldDescriptor$TYPE_MESSAGE = new RepeatedFieldDescriptor$TYPE_MESSAGE("serverProto.summonMonster.ProtoCaptureFightFinishNotify.reward_list","rewardList",2 << 3 | WireType.LENGTH_DELIMITED,ProtoItemInfo);
       
      private var summon_monster_id$field:int;
      
      private var hasField$0:uint = 0;
      
      [ArrayElementType("serverProto.inc.ProtoItemInfo")]
      public var rewardList:Array;
      
      public function ProtoCaptureFightFinishNotify()
      {
         this.rewardList = [];
         super();
      }
      
      public function clearSummonMonsterId() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967294E9;
         this.summon_monster_id$field = new int();
      }
      
      public function get hasSummonMonsterId() : Boolean
      {
         return (this.hasField$0 & 1) != 0;
      }
      
      public function set summonMonsterId(param1:int) : void
      {
         this.hasField$0 = this.hasField$0 | 1;
         this.summon_monster_id$field = param1;
      }
      
      public function get summonMonsterId() : int
      {
         return this.summon_monster_id$field;
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc3_:* = undefined;
         if(this.hasSummonMonsterId)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,1);
            WriteUtils.write$TYPE_INT32(param1,this.summon_monster_id$field);
         }
         var _loc2_:uint = 0;
         while(_loc2_ < this.rewardList.length)
         {
            WriteUtils.writeTag(param1,WireType.LENGTH_DELIMITED,2);
            WriteUtils.write$TYPE_MESSAGE(param1,this.rewardList[_loc2_]);
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