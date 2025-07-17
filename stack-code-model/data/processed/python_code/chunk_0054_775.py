package serverProto.user
{
   import com.netease.protobuf.Message;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_UINT32;
   import com.netease.protobuf.WireType;
   import com.netease.protobuf.WritingBuffer;
   import com.netease.protobuf.WriteUtils;
   import flash.utils.IDataInput;
   import com.netease.protobuf.ReadUtils;
   import flash.errors.IOError;
   
   public final class ProtoNewRankTitle extends Message
   {
      
      public static const RANK_ID:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.user.ProtoNewRankTitle.rank_id","rankId",1 << 3 | WireType.VARINT);
      
      public static const TITLE_ID:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.user.ProtoNewRankTitle.title_id","titleId",2 << 3 | WireType.VARINT);
       
      private var rank_id$field:uint;
      
      private var hasField$0:uint = 0;
      
      private var title_id$field:uint;
      
      public function ProtoNewRankTitle()
      {
         super();
      }
      
      public function clearRankId() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967294E9;
         this.rank_id$field = new uint();
      }
      
      public function get hasRankId() : Boolean
      {
         return (this.hasField$0 & 1) != 0;
      }
      
      public function set rankId(param1:uint) : void
      {
         this.hasField$0 = this.hasField$0 | 1;
         this.rank_id$field = param1;
      }
      
      public function get rankId() : uint
      {
         return this.rank_id$field;
      }
      
      public function clearTitleId() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967293E9;
         this.title_id$field = new uint();
      }
      
      public function get hasTitleId() : Boolean
      {
         return (this.hasField$0 & 2) != 0;
      }
      
      public function set titleId(param1:uint) : void
      {
         this.hasField$0 = this.hasField$0 | 2;
         this.title_id$field = param1;
      }
      
      public function get titleId() : uint
      {
         return this.title_id$field;
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc2_:* = undefined;
         if(this.hasRankId)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,1);
            WriteUtils.write$TYPE_UINT32(param1,this.rank_id$field);
         }
         if(this.hasTitleId)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,2);
            WriteUtils.write$TYPE_UINT32(param1,this.title_id$field);
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