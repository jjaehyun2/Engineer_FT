package serverProto.activity
{
   import com.netease.protobuf.Message;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_MESSAGE;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_UINT32;
   import com.netease.protobuf.fieldDescriptors.RepeatedFieldDescriptor$TYPE_MESSAGE;
   import com.netease.protobuf.WireType;
   import serverProto.inc.ProtoRetInfo;
   import com.netease.protobuf.WritingBuffer;
   import com.netease.protobuf.WriteUtils;
   import flash.utils.IDataInput;
   import com.netease.protobuf.ReadUtils;
   import flash.errors.IOError;
   
   public final class ProtoTabardMaterialBuyRsp extends Message
   {
      
      public static const RET:FieldDescriptor$TYPE_MESSAGE = new FieldDescriptor$TYPE_MESSAGE("serverProto.activity.ProtoTabardMaterialBuyRsp.ret","ret",1 << 3 | WireType.LENGTH_DELIMITED,ProtoRetInfo);
      
      public static const BEGIN_TIME:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.activity.ProtoTabardMaterialBuyRsp.begin_time","beginTime",2 << 3 | WireType.VARINT);
      
      public static const END_TIME:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.activity.ProtoTabardMaterialBuyRsp.end_time","endTime",3 << 3 | WireType.VARINT);
      
      public static const BOXES:RepeatedFieldDescriptor$TYPE_MESSAGE = new RepeatedFieldDescriptor$TYPE_MESSAGE("serverProto.activity.ProtoTabardMaterialBuyRsp.boxes","boxes",4 << 3 | WireType.LENGTH_DELIMITED,ProtoTabardMateriaBuylBox);
      
      public static const TOTAL_GOLDINGOT:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.activity.ProtoTabardMaterialBuyRsp.total_goldingot","totalGoldingot",5 << 3 | WireType.VARINT);
       
      private var ret$field:ProtoRetInfo;
      
      private var begin_time$field:uint;
      
      private var hasField$0:uint = 0;
      
      private var end_time$field:uint;
      
      [ArrayElementType("serverProto.activity.ProtoTabardMateriaBuylBox")]
      public var boxes:Array;
      
      private var total_goldingot$field:uint;
      
      public function ProtoTabardMaterialBuyRsp()
      {
         this.boxes = [];
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
      
      public function clearBeginTime() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967294E9;
         this.begin_time$field = new uint();
      }
      
      public function get hasBeginTime() : Boolean
      {
         return (this.hasField$0 & 1) != 0;
      }
      
      public function set beginTime(param1:uint) : void
      {
         this.hasField$0 = this.hasField$0 | 1;
         this.begin_time$field = param1;
      }
      
      public function get beginTime() : uint
      {
         return this.begin_time$field;
      }
      
      public function clearEndTime() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967293E9;
         this.end_time$field = new uint();
      }
      
      public function get hasEndTime() : Boolean
      {
         return (this.hasField$0 & 2) != 0;
      }
      
      public function set endTime(param1:uint) : void
      {
         this.hasField$0 = this.hasField$0 | 2;
         this.end_time$field = param1;
      }
      
      public function get endTime() : uint
      {
         return this.end_time$field;
      }
      
      public function clearTotalGoldingot() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967291E9;
         this.total_goldingot$field = new uint();
      }
      
      public function get hasTotalGoldingot() : Boolean
      {
         return (this.hasField$0 & 4) != 0;
      }
      
      public function set totalGoldingot(param1:uint) : void
      {
         this.hasField$0 = this.hasField$0 | 4;
         this.total_goldingot$field = param1;
      }
      
      public function get totalGoldingot() : uint
      {
         return this.total_goldingot$field;
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc3_:* = undefined;
         if(this.hasRet)
         {
            WriteUtils.writeTag(param1,WireType.LENGTH_DELIMITED,1);
            WriteUtils.write$TYPE_MESSAGE(param1,this.ret$field);
         }
         if(this.hasBeginTime)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,2);
            WriteUtils.write$TYPE_UINT32(param1,this.begin_time$field);
         }
         if(this.hasEndTime)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,3);
            WriteUtils.write$TYPE_UINT32(param1,this.end_time$field);
         }
         var _loc2_:uint = 0;
         while(_loc2_ < this.boxes.length)
         {
            WriteUtils.writeTag(param1,WireType.LENGTH_DELIMITED,4);
            WriteUtils.write$TYPE_MESSAGE(param1,this.boxes[_loc2_]);
            _loc2_++;
         }
         if(this.hasTotalGoldingot)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,5);
            WriteUtils.write$TYPE_UINT32(param1,this.total_goldingot$field);
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
          * Error type: IndexOutOfBoundsException (Index: 5, Size: 5)
          */
         throw new flash.errors.IllegalOperationError("Not decompiled due to error");
      }
   }
}