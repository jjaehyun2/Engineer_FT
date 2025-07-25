package kabam.rotmg.messaging.impl.incoming {
import flash.utils.IDataInput;

import kabam.rotmg.messaging.impl.data.SlotObjectData;

public class ForgeResponse extends IncomingMessage {
    public var success:Boolean;
    public var results:Vector.<SlotObjectData>;

    public function ForgeResponse(id:uint, callback:Function) {
        this.results = new Vector.<SlotObjectData>();
        super(id, callback);
    }

    override public function parseFromInput(data:IDataInput) : void {
        /*this.success = data.readBoolean();
        this.results.length = 0;
        var resultsLen:int = data.readByte();
        for (var i:int = 0; i < resultsLen; i++)
        this.results.push()*/
    }

    override public function toString() : String {
        return formatToString("FORGE_RESPONSE", "success", "results");
    }
}
}