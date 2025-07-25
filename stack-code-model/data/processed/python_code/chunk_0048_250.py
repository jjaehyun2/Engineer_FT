package kabam.rotmg.messaging.impl.incoming {
import flash.utils.IDataInput;

public class BuyResult extends IncomingMessage {

    public static const UNKNOWN_ERROR_BRID:int = -1;

    public static const SUCCESS_BRID:int = 0;

    public static const INVALID_CHARACTER_BRID:int = 1;

    public static const ITEM_NOT_FOUND_BRID:int = 2;

    public static const NOT_ENOUGH_GOLD_BRID:int = 3;

    public static const INVENTORY_FULL_BRID:int = 4;

    public static const TOO_LOW_RANK_BRID:int = 5;

    public static const NOT_ENOUGH_FAME_BRID:int = 6;

    public static const PET_FEED_SUCCESS_BRID:int = 7;

    public static const TOO_MANY_RESETS_TODAY:int = 10;

    public function BuyResult(param1:uint, param2:Function) {
        super(param1, param2);
    }
    public var result_:int;
    public var resultString_:String;

    override public function parseFromInput(param1:IDataInput):void {
        this.result_ = param1.readInt();
        this.resultString_ = param1.readUTF();
    }

    override public function toString():String {
        return formatToString("BUYRESULT", "result_", "resultString_");
    }
}
}