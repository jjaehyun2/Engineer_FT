﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.messaging.impl.incoming.pets.DeletePetMessage

package kabam.rotmg.messaging.impl.incoming.pets
{
    import kabam.rotmg.messaging.impl.incoming.IncomingMessage;
    import flash.utils.IDataInput;

    public class DeletePetMessage extends IncomingMessage 
    {

        public var petID:int;

        public function DeletePetMessage(_arg_1:uint, _arg_2:Function)
        {
            super(_arg_1, _arg_2);
        }

        override public function parseFromInput(_arg_1:IDataInput):void
        {
            this.petID = _arg_1.readInt();
        }


    }
}//package kabam.rotmg.messaging.impl.incoming.pets