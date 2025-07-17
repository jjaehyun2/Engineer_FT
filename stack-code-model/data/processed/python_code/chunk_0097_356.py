package serverProto.fight
{
   import com.netease.protobuf.Message;
   import com.netease.protobuf.fieldDescriptors.FieldDescriptor$TYPE_MESSAGE;
   import com.netease.protobuf.fieldDescriptors.RepeatedFieldDescriptor$TYPE_UINT32;
   import com.netease.protobuf.WireType;
   import serverProto.formationBase.ProtoTeamFormationInfo;
   import com.netease.protobuf.WritingBuffer;
   import com.netease.protobuf.WriteUtils;
   import flash.utils.IDataInput;
   import com.netease.protobuf.ReadUtils;
   import flash.errors.IOError;
   
   public final class ProtoInsertPreFightBroadcast extends Message
   {
      
      public static const PLAYER_TEAM:FieldDescriptor$TYPE_MESSAGE = new FieldDescriptor$TYPE_MESSAGE("serverProto.fight.ProtoInsertPreFightBroadcast.player_team","playerTeam",1 << 3 | WireType.LENGTH_DELIMITED,ProtoTeamFormationInfo);
      
      public static const CAN_STAND_POS:RepeatedFieldDescriptor$TYPE_UINT32 = new RepeatedFieldDescriptor$TYPE_UINT32("serverProto.fight.ProtoInsertPreFightBroadcast.can_stand_pos","canStandPos",2 << 3 | WireType.VARINT);
       
      public var playerTeam:ProtoTeamFormationInfo;
      
      [ArrayElementType("uint")]
      public var canStandPos:Array;
      
      public function ProtoInsertPreFightBroadcast()
      {
         this.canStandPos = [];
         super();
      }
      
      override final function writeToBuffer(param1:WritingBuffer) : void
      {
         var _loc3_:* = undefined;
         WriteUtils.writeTag(param1,WireType.LENGTH_DELIMITED,1);
         WriteUtils.write$TYPE_MESSAGE(param1,this.playerTeam);
         var _loc2_:uint = 0;
         while(_loc2_ < this.canStandPos.length)
         {
            WriteUtils.writeTag(param1,WireType.VARINT,2);
            WriteUtils.write$TYPE_UINT32(param1,this.canStandPos[_loc2_]);
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