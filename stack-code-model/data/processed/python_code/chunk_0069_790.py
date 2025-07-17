package serverProto.ninjaSystem
{
   import com.netease.protobuf.Message;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_UINT32;
   import com.netease.protobuf.WireType;
   import com.netease.protobuf.WritingBuffer;
   import com.netease.protobuf.WriteUtils;
   import flash.utils.IDataInput;
   import com.netease.protobuf.ReadUtils;
   import flash.errors.IOError;
   
   public final class ProtoSecondAwakenRequest extends Message
   {
      
      public static const NINJA_SEQUENCE:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.ninjaSystem.ProtoSecondAwakenRequest.ninja_sequence","ninjaSequence",1 << 3 | WireType.VARINT);
      
      public static const SKILL_ID:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.ninjaSystem.ProtoSecondAwakenRequest.skill_id","skillId",2 << 3 | WireType.VARINT);
       
      public var ninjaSequence:uint;
      
      public var skillId:uint;
      
      public function ProtoSecondAwakenRequest()
      {
         super();
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc2_:* = undefined;
         WriteUtils.writeTag(param1,WireType.VARINT,1);
         WriteUtils.write$TYPE_UINT32(param1,this.ninjaSequence);
         WriteUtils.writeTag(param1,WireType.VARINT,2);
         WriteUtils.write$TYPE_UINT32(param1,this.skillId);
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