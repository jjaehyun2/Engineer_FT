package com.ankamagames.dofus.network.messages.game.inventory.exchanges
{
   import com.ankamagames.jerakine.network.CustomDataWrapper;
   import com.ankamagames.jerakine.network.ICustomDataInput;
   import com.ankamagames.jerakine.network.ICustomDataOutput;
   import com.ankamagames.jerakine.network.INetworkMessage;
   import com.ankamagames.jerakine.network.NetworkMessage;
   import com.ankamagames.jerakine.network.utils.FuncTree;
   import flash.utils.ByteArray;
   
   public class ExchangeStartedMessage extends NetworkMessage implements INetworkMessage
   {
      
      public static const protocolId:uint = 8540;
       
      
      private var _isInitialized:Boolean = false;
      
      public var exchangeType:int = 0;
      
      public function ExchangeStartedMessage()
      {
         super();
      }
      
      override public function get isInitialized() : Boolean
      {
         return this._isInitialized;
      }
      
      override public function getMessageId() : uint
      {
         return 8540;
      }
      
      public function initExchangeStartedMessage(exchangeType:int = 0) : ExchangeStartedMessage
      {
         this.exchangeType = exchangeType;
         this._isInitialized = true;
         return this;
      }
      
      override public function reset() : void
      {
         this.exchangeType = 0;
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
         this.serializeAs_ExchangeStartedMessage(output);
      }
      
      public function serializeAs_ExchangeStartedMessage(output:ICustomDataOutput) : void
      {
         output.writeByte(this.exchangeType);
      }
      
      public function deserialize(input:ICustomDataInput) : void
      {
         this.deserializeAs_ExchangeStartedMessage(input);
      }
      
      public function deserializeAs_ExchangeStartedMessage(input:ICustomDataInput) : void
      {
         this._exchangeTypeFunc(input);
      }
      
      public function deserializeAsync(tree:FuncTree) : void
      {
         this.deserializeAsyncAs_ExchangeStartedMessage(tree);
      }
      
      public function deserializeAsyncAs_ExchangeStartedMessage(tree:FuncTree) : void
      {
         tree.addChild(this._exchangeTypeFunc);
      }
      
      private function _exchangeTypeFunc(input:ICustomDataInput) : void
      {
         this.exchangeType = input.readByte();
      }
   }
}