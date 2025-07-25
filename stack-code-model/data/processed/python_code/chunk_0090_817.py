package com.ankamagames.dofus.network.messages.game.context
{
   import com.ankamagames.dofus.network.types.game.context.EntityMovementInformations;
   import com.ankamagames.jerakine.network.CustomDataWrapper;
   import com.ankamagames.jerakine.network.ICustomDataInput;
   import com.ankamagames.jerakine.network.ICustomDataOutput;
   import com.ankamagames.jerakine.network.INetworkMessage;
   import com.ankamagames.jerakine.network.NetworkMessage;
   import com.ankamagames.jerakine.network.utils.FuncTree;
   import flash.utils.ByteArray;
   
   public class GameContextMoveElementMessage extends NetworkMessage implements INetworkMessage
   {
      
      public static const protocolId:uint = 5628;
       
      
      private var _isInitialized:Boolean = false;
      
      public var movement:EntityMovementInformations;
      
      private var _movementtree:FuncTree;
      
      public function GameContextMoveElementMessage()
      {
         this.movement = new EntityMovementInformations();
         super();
      }
      
      override public function get isInitialized() : Boolean
      {
         return this._isInitialized;
      }
      
      override public function getMessageId() : uint
      {
         return 5628;
      }
      
      public function initGameContextMoveElementMessage(movement:EntityMovementInformations = null) : GameContextMoveElementMessage
      {
         this.movement = movement;
         this._isInitialized = true;
         return this;
      }
      
      override public function reset() : void
      {
         this.movement = new EntityMovementInformations();
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
         this.serializeAs_GameContextMoveElementMessage(output);
      }
      
      public function serializeAs_GameContextMoveElementMessage(output:ICustomDataOutput) : void
      {
         this.movement.serializeAs_EntityMovementInformations(output);
      }
      
      public function deserialize(input:ICustomDataInput) : void
      {
         this.deserializeAs_GameContextMoveElementMessage(input);
      }
      
      public function deserializeAs_GameContextMoveElementMessage(input:ICustomDataInput) : void
      {
         this.movement = new EntityMovementInformations();
         this.movement.deserialize(input);
      }
      
      public function deserializeAsync(tree:FuncTree) : void
      {
         this.deserializeAsyncAs_GameContextMoveElementMessage(tree);
      }
      
      public function deserializeAsyncAs_GameContextMoveElementMessage(tree:FuncTree) : void
      {
         this._movementtree = tree.addChild(this._movementtreeFunc);
      }
      
      private function _movementtreeFunc(input:ICustomDataInput) : void
      {
         this.movement = new EntityMovementInformations();
         this.movement.deserializeAsync(this._movementtree);
      }
   }
}