package kabam.rotmg.messaging.impl.outgoing {
import flash.utils.IDataOutput;

public class PlayerText extends OutgoingMessage {


    public function PlayerText(id:uint, callback:Function) {
        this.text_ = "";
        super(id, callback);
    }
    public var text_:String;

    override public function writeToOutput(data:IDataOutput):void {
        data.writeUTF(this.text_);
    }

    override public function toString():String {
        return formatToString("PLAYERTEXT", "text_");
    }
}
}