package com.ankamagames.dofus.network.messages.game.tinsel
{
   import com.ankamagames.jerakine.network.CustomDataWrapper;
   import com.ankamagames.jerakine.network.ICustomDataInput;
   import com.ankamagames.jerakine.network.ICustomDataOutput;
   import com.ankamagames.jerakine.network.INetworkMessage;
   import com.ankamagames.jerakine.network.NetworkMessage;
   import com.ankamagames.jerakine.network.utils.FuncTree;
   import flash.utils.ByteArray;
   
   public class TitleSelectedMessage extends NetworkMessage implements INetworkMessage
   {
      
      public static const protocolId:uint = 8922;
       
      
      private var _isInitialized:Boolean = false;
      
      public var titleId:uint = 0;
      
      public function TitleSelectedMessage()
      {
         super();
      }
      
      override public function get isInitialized() : Boolean
      {
         return this._isInitialized;
      }
      
      override public function getMessageId() : uint
      {
         return 8922;
      }
      
      public function initTitleSelectedMessage(titleId:uint = 0) : TitleSelectedMessage
      {
         this.titleId = titleId;
         this._isInitialized = true;
         return this;
      }
      
      override public function reset() : void
      {
         this.titleId = 0;
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
         this.serializeAs_TitleSelectedMessage(output);
      }
      
      public function serializeAs_TitleSelectedMessage(output:ICustomDataOutput) : void
      {
         if(this.titleId < 0)
         {
            throw new Error("Forbidden value (" + this.titleId + ") on element titleId.");
         }
         output.writeVarShort(this.titleId);
      }
      
      public function deserialize(input:ICustomDataInput) : void
      {
         this.deserializeAs_TitleSelectedMessage(input);
      }
      
      public function deserializeAs_TitleSelectedMessage(input:ICustomDataInput) : void
      {
         this._titleIdFunc(input);
      }
      
      public function deserializeAsync(tree:FuncTree) : void
      {
         this.deserializeAsyncAs_TitleSelectedMessage(tree);
      }
      
      public function deserializeAsyncAs_TitleSelectedMessage(tree:FuncTree) : void
      {
         tree.addChild(this._titleIdFunc);
      }
      
      private function _titleIdFunc(input:ICustomDataInput) : void
      {
         this.titleId = input.readVarUhShort();
         if(this.titleId < 0)
         {
            throw new Error("Forbidden value (" + this.titleId + ") on element of TitleSelectedMessage.titleId.");
         }
      }
   }
}