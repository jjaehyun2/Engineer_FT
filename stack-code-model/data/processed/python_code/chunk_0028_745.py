package com.netease.protobuf.fieldDescriptors
{
   import com.netease.protobuf.FieldDescriptor;
   import flash.utils.IDataInput;
   import com.netease.protobuf.ReadUtils;
   import com.netease.protobuf.WritingBuffer;
   import com.netease.protobuf.WriteUtils;
   
   public final class FieldDescriptorTYPE_FLOAT extends FieldDescriptor
   {
       
      public function FieldDescriptorTYPE_FLOAT(param1:String, param2:String, param3:uint)
      {
         super();
         this.fullName = param1;
         this._name = param2;
         this.tag = param3;
      }
      
      override public function get type() : Class
      {
         return Number;
      }
      
      override public function readSingleField(param1:IDataInput) : *
      {
         return ReadUtils.read$TYPE_FLOAT(param1);
      }
      
      override public function writeSingleField(param1:WritingBuffer, param2:*) : void
      {
         WriteUtils.write$TYPE_FLOAT(param1,param2);
      }
      
      override public function autoSetNull() : void
      {
         if(super.hasOwnProperty("autoSetNull"))
         {
            super.["autoSetNull"]();
         }
      }
   }
}