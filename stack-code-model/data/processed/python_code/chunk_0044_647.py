﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.messaging.impl.ReskinPet

package kabam.rotmg.messaging.impl
{
    import kabam.rotmg.messaging.impl.outgoing.OutgoingMessage;
    import kabam.rotmg.messaging.impl.data.SlotObjectData;
    import flash.utils.IDataOutput;

    public class ReskinPet extends OutgoingMessage 
    {

        public var petInstanceId:int;
        public var pickedNewPetType:int;
        public var item:SlotObjectData = new SlotObjectData();

        public function ReskinPet(_arg_1:uint, _arg_2:Function)
        {
            super(_arg_1, _arg_2);
        }

        override public function writeToOutput(_arg_1:IDataOutput):void
        {
            _arg_1.writeInt(this.petInstanceId);
            _arg_1.writeInt(this.pickedNewPetType);
            this.item.writeToOutput(_arg_1);
        }

        override public function toString():String
        {
            return (formatToString("ENTER_ARENA", "petInstanceId", "pickedNewPetType"));
        }


    }
}//package kabam.rotmg.messaging.impl