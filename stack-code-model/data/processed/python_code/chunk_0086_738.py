package serverProto.findBack
{
   import com.netease.protobuf.Message;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_UINT32;
   import com.netease.protobuf.WireType;
   import com.netease.protobuf.WritingBuffer;
   import com.netease.protobuf.WriteUtils;
   import flash.utils.IDataInput;
   import com.netease.protobuf.ReadUtils;
   import flash.errors.IOError;
   
   public final class ProtoFindBackReq extends Message
   {
      
      public static const TYPE:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.findBack.ProtoFindBackReq.type","type",1 << 3 | WireType.VARINT);
      
      public static const WAY:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.findBack.ProtoFindBackReq.way","way",2 << 3 | WireType.VARINT);
       
      public var type:uint;
      
      public var way:uint;
      
      public function ProtoFindBackReq()
      {
         super();
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc2_:* = undefined;
         WriteUtils.writeTag(param1,WireType.VARINT,1);
         WriteUtils.write$TYPE_UINT32(param1,this.type);
         WriteUtils.writeTag(param1,WireType.VARINT,2);
         WriteUtils.write$TYPE_UINT32(param1,this.way);
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