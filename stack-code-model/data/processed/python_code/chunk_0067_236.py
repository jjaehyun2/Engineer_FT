package serverProto.secondAwakenItemExchange
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
   
   public final class ProtoSecondAwakenExchangeQueryResp extends Message
   {
      
      public static const RET_INFO:FieldDescriptor$TYPE_MESSAGE = new FieldDescriptor$TYPE_MESSAGE("serverProto.secondAwakenItemExchange.ProtoSecondAwakenExchangeQueryResp.ret_info","retInfo",1 << 3 | WireType.LENGTH_DELIMITED,ProtoRetInfo);
      
      public static const EXCHANGE_ITEM_NUM:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.secondAwakenItemExchange.ProtoSecondAwakenExchangeQueryResp.exchange_item_num","exchangeItemNum",2 << 3 | WireType.VARINT);
       
      public var retInfo:ProtoRetInfo;
      
      private var exchange_item_num$field:uint;
      
      private var hasField$0:uint = 0;
      
      public function ProtoSecondAwakenExchangeQueryResp()
      {
         super();
      }
      
      public function clearExchangeItemNum() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967294E9;
         this.exchange_item_num$field = new uint();
      }
      
      public function get hasExchangeItemNum() : Boolean
      {
         return (this.hasField$0 & 1) != 0;
      }
      
      public function set exchangeItemNum(param1:uint) : void
      {
         this.hasField$0 = this.hasField$0 | 1;
         this.exchange_item_num$field = param1;
      }
      
      public function get exchangeItemNum() : uint
      {
         return this.exchange_item_num$field;
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc2_:* = undefined;
         WriteUtils.writeTag(param1,WireType.LENGTH_DELIMITED,1);
         WriteUtils.write$TYPE_MESSAGE(param1,this.retInfo);
         if(this.hasExchangeItemNum)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,2);
            WriteUtils.write$TYPE_UINT32(param1,this.exchange_item_num$field);
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