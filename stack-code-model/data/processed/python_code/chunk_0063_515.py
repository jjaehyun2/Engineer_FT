package kabam.rotmg.messaging.impl.incoming {
import flash.utils.IDataInput;

public class CreateSuccess extends IncomingMessage {


    public function CreateSuccess(id:uint, callback:Function) {
        super(id, callback);
    }
    public var objectId_:int;
    public var charId_:int;

    override public function parseFromInput(data:IDataInput):void {
        this.objectId_ = data.readInt();
        this.charId_ = data.readInt();
    }

    override public function toString():String {
        return formatToString("CREATE_SUCCESS", "objectId_", "charId_");
    }
}
}