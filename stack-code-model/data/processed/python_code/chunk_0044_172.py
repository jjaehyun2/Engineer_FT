package serverProto.activity
{
   import com.netease.protobuf.Message;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_INT32;
   import com.netease.protobuf.WireType;
   import com.netease.protobuf.WritingBuffer;
   import com.netease.protobuf.WriteUtils;
   import flash.utils.IDataInput;
   import com.netease.protobuf.ReadUtils;
   import flash.errors.IOError;
   
   public final class ProtoLanternInfo extends Message
   {
      
      public static const ID:FieldDescriptor$TYPE_INT32 = new FieldDescriptor$TYPE_INT32("serverProto.activity.ProtoLanternInfo.id","id",1 << 3 | WireType.VARINT);
      
      public static const STATE:FieldDescriptor$TYPE_INT32 = new FieldDescriptor$TYPE_INT32("serverProto.activity.ProtoLanternInfo.state","state",2 << 3 | WireType.VARINT);
       
      private var id$field:int;
      
      private var hasField$0:uint = 0;
      
      private var state$field:int;
      
      public function ProtoLanternInfo()
      {
         super();
      }
      
      public function clearId() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967294E9;
         this.id$field = new int();
      }
      
      public function get hasId() : Boolean
      {
         return (this.hasField$0 & 1) != 0;
      }
      
      public function set id(param1:int) : void
      {
         this.hasField$0 = this.hasField$0 | 1;
         this.id$field = param1;
      }
      
      public function get id() : int
      {
         return this.id$field;
      }
      
      public function clearState() : void
      {
         this.hasField$0 = this.hasField$0 & 4.294967293E9;
         this.state$field = new int();
      }
      
      public function get hasState() : Boolean
      {
         return (this.hasField$0 & 2) != 0;
      }
      
      public function set state(param1:int) : void
      {
         this.hasField$0 = this.hasField$0 | 2;
         this.state$field = param1;
      }
      
      public function get state() : int
      {
         return this.state$field;
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc2_:* = undefined;
         if(this.hasId)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,1);
            WriteUtils.write$TYPE_INT32(param1,this.id$field);
         }
         if(this.hasState)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,2);
            WriteUtils.write$TYPE_INT32(param1,this.state$field);
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