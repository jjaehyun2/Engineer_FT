package com.ankamagames.dofus.network.messages.game.friend
{
   import com.ankamagames.dofus.network.ProtocolTypeManager;
   import com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation;
   import com.ankamagames.jerakine.network.CustomDataWrapper;
   import com.ankamagames.jerakine.network.ICustomDataInput;
   import com.ankamagames.jerakine.network.ICustomDataOutput;
   import com.ankamagames.jerakine.network.INetworkMessage;
   import com.ankamagames.jerakine.network.NetworkMessage;
   import com.ankamagames.jerakine.network.utils.FuncTree;
   import flash.utils.ByteArray;
   
   public class FriendJoinRequestMessage extends NetworkMessage implements INetworkMessage
   {
      
      public static const protocolId:uint = 535;
       
      
      private var _isInitialized:Boolean = false;
      
      public var target:AbstractPlayerSearchInformation;
      
      private var _targettree:FuncTree;
      
      public function FriendJoinRequestMessage()
      {
         this.target = new AbstractPlayerSearchInformation();
         super();
      }
      
      override public function get isInitialized() : Boolean
      {
         return this._isInitialized;
      }
      
      override public function getMessageId() : uint
      {
         return 535;
      }
      
      public function initFriendJoinRequestMessage(target:AbstractPlayerSearchInformation = null) : FriendJoinRequestMessage
      {
         this.target = target;
         this._isInitialized = true;
         return this;
      }
      
      override public function reset() : void
      {
         this.target = new AbstractPlayerSearchInformation();
         this._isInitialized = false;
      }
      
      override public function pack(output:ICustomDataOutput) : void
      {
         var data:ByteArray = new ByteArray();
         this.serialize(new CustomDataWrapper(data));
         writePacket(output,this.getMessageId(),data);
      }
      
      override public function unpack(input:ICustomDataInput, length:uint) : void
      {
         this.deserialize(input);
      }
      
      override public function unpackAsync(input:ICustomDataInput, length:uint) : FuncTree
      {
         var tree:FuncTree = new FuncTree();
         tree.setRoot(input);
         this.deserializeAsync(tree);
         return tree;
      }
      
      public function serialize(output:ICustomDataOutput) : void
      {
         this.serializeAs_FriendJoinRequestMessage(output);
      }
      
      public function serializeAs_FriendJoinRequestMessage(output:ICustomDataOutput) : void
      {
         output.writeShort(this.target.getTypeId());
         this.target.serialize(output);
      }
      
      public function deserialize(input:ICustomDataInput) : void
      {
         this.deserializeAs_FriendJoinRequestMessage(input);
      }
      
      public function deserializeAs_FriendJoinRequestMessage(input:ICustomDataInput) : void
      {
         var _id1:uint = input.readUnsignedShort();
         this.target = ProtocolTypeManager.getInstance(AbstractPlayerSearchInformation,_id1);
         this.target.deserialize(input);
      }
      
      public function deserializeAsync(tree:FuncTree) : void
      {
         this.deserializeAsyncAs_FriendJoinRequestMessage(tree);
      }
      
      public function deserializeAsyncAs_FriendJoinRequestMessage(tree:FuncTree) : void
      {
         this._targettree = tree.addChild(this._targettreeFunc);
      }
      
      private function _targettreeFunc(input:ICustomDataInput) : void
      {
         var _id:uint = input.readUnsignedShort();
         this.target = ProtocolTypeManager.getInstance(AbstractPlayerSearchInformation,_id);
         this.target.deserializeAsync(this._targettree);
      }
   }
}