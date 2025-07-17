package kabam.rotmg.messaging.impl.outgoing {
import flash.utils.IDataOutput;

public class CreateGuild extends OutgoingMessage {

    public function CreateGuild(param1:uint, param2:Function) {
        super(param1, param2);
    }
    public var name_:String;

    override public function writeToOutput(param1:IDataOutput):void {
        param1.writeUTF(this.name_);
    }

    override public function toString():String {
        return formatToString("CREATEGUILD", "name_");
    }
}
}