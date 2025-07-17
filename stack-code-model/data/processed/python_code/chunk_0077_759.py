package serverProto.activity
{
   import com.netease.protobuf.Message;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_UINT32;
   import com.netease.protobuf.WireType;
   import com.netease.protobuf.WritingBuffer;
   import com.netease.protobuf.WriteUtils;
   import flash.utils.IDataInput;
   import com.netease.protobuf.ReadUtils;
   import flash.errors.IOError;
   
   public final class ProtoNewOpenServiceTab extends Message
   {
      
      public static const TAB_IDX:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.activity.ProtoNewOpenServiceTab.tab_idx","tabIdx",1 << 3 | WireType.VARINT);
      
      public static const TAB_STATUS:FieldDescriptor$TYPE_UINT32 = new FieldDescriptor$TYPE_UINT32("serverProto.activity.ProtoNewOpenServiceTab.tab_status","tabStatus",2 << 3 | WireType.VARINT);
       
      private var tab_idx$field:uint;
      
      private var hasField$0:uint = 0;
      
      private var tab_status$field:uint;
      
      public function ProtoNewOpenServiceTab()
      {
         super();
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
      
      public function clearTabStatus() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967293E9;
         this.tab_status$field = new uint();
      }
      
      public function get hasTabStatus() : Boolean
      {
         return (this.hasField$0 & 2) != 0;
      }
      
      public function set tabStatus(param1:uint) : void
      {
         this.hasField$0 = this.hasField$0 | 2;
         this.tab_status$field = param1;
      }
      
      public function get tabStatus() : uint
      {
         return this.tab_status$field;
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc2_:* = undefined;
         if(this.hasTabIdx)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,1);
            WriteUtils.write$TYPE_UINT32(param1,this.tab_idx$field);
         }
         if(this.hasTabStatus)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,2);
            WriteUtils.write$TYPE_UINT32(param1,this.tab_status$field);
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