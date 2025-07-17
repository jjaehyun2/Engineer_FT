package serverProto.activity
{
   import com.netease.protobuf.Message;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_MESSAGE;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_UINT32;
   import com.netease.protobuf.WireType;
   import serverProto.inc.ProtoRetInfo;
   import com.netease.protobuf.WritingBuffer;
   import com.netease.protobuf.WriteUtils;
   import flash.utils.IDataInput;
   import com.netease.protobuf.ReadUtils;
   import flash.errors.IOError;
   
   public final class ProtoMergeServerAwardRsp extends Message
   {
      
      public static const RET:FieldDescriptor$TYPE_MESSAGE = new FieldDescriptor$TYPE_MESSAGE("serverProto.activity.ProtoMergeServerAwardRsp.ret","ret",1 << 3 | WireType.LENGTH_DELIMITED,ProtoRetInfo);
      
      public static const TAB_IDX:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.activity.ProtoMergeServerAwardRsp.tab_idx","tabIdx",2 << 3 | WireType.VARINT);
      
      public static const BOX_ID:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.activity.ProtoMergeServerAwardRsp.box_id","boxId",3 << 3 | WireType.VARINT);
      
      public static const AWARD_STATUS:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.activity.ProtoMergeServerAwardRsp.award_status","awardStatus",4 << 3 | WireType.VARINT);
       
      private var ret$field:ProtoRetInfo;
      
      private var tab_idx$field:uint;
      
      private var hasField$0:uint = 0;
      
      private var box_id$field:uint;
      
      private var award_status$field:uint;
      
      public function ProtoMergeServerAwardRsp()
      {
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
      
      public function clearTabIdx() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967294E9;
         this.tab_idx$field = new uint();
      }
      
      public function get hasTabIdx() : Boolean
      {
         return (this.hasField$0 & 1) != 0;
      }
      
      public function set tabIdx(param1:uint) : void
      {
         this.hasField$0 = this.hasField$0 | 1;
         this.tab_idx$field = param1;
      }
      
      public function get tabIdx() : uint
      {
         return this.tab_idx$field;
      }
      
      public function clearBoxId() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967293E9;
         this.box_id$field = new uint();
      }
      
      public function get hasBoxId() : Boolean
      {
         return (this.hasField$0 & 2) != 0;
      }
      
      public function set boxId(param1:uint) : void
      {
         this.hasField$0 = this.hasField$0 | 2;
         this.box_id$field = param1;
      }
      
      public function get boxId() : uint
      {
         return this.box_id$field;
      }
      
      public function clearAwardStatus() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967291E9;
         this.award_status$field = new uint();
      }
      
      public function get hasAwardStatus() : Boolean
      {
         return (this.hasField$0 & 4) != 0;
      }
      
      public function set awardStatus(param1:uint) : void
      {
         this.hasField$0 = this.hasField$0 | 4;
         this.award_status$field = param1;
      }
      
      public function get awardStatus() : uint
      {
         return this.award_status$field;
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc2_:* = undefined;
         if(this.hasRet)
         {
            WriteUtils.writeTag(param1,WireType.LENGTH_DELIMITED,1);
            WriteUtils.write$TYPE_MESSAGE(param1,this.ret$field);
         }
         if(this.hasTabIdx)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,2);
            WriteUtils.write$TYPE_UINT32(param1,this.tab_idx$field);
         }
         if(this.hasBoxId)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,3);
            WriteUtils.write$TYPE_UINT32(param1,this.box_id$field);
         }
         if(this.hasAwardStatus)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,4);
            WriteUtils.write$TYPE_UINT32(param1,this.award_status$field);
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
          * Error type: IndexOutOfBoundsException (Index: 4, Size: 4)
          */
         throw new flash.errors.IllegalOperationError("Not decompiled due to error");
      }
   }
}