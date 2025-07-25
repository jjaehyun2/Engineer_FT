package kabam.rotmg.dailyLogin.model {
public class CalendarDayModel {

    public function CalendarDayModel(param1:int, param2:int, param3:int, param4:int, param5:Boolean, param6:String) {
        super();
        this._dayNumber = param1;
        this._itemID = param2;
        this._gold = param3;
        this._isClaimed = param5;
        this._quantity = param4;
        this._calendarType = param6;
    }

    private var _dayNumber:int;

    public function get dayNumber():int {
        return this._dayNumber;
    }

    public function set dayNumber(param1:int):void {
        this._dayNumber = param1;
    }

    private var _quantity:int;

    public function get quantity():int {
        return this._quantity;
    }

    public function set quantity(param1:int):void {
        this._quantity = param1;
    }

    private var _itemID:int;

    public function get itemID():int {
        return this._itemID;
    }

    public function set itemID(param1:int):void {
        this._itemID = param1;
    }

    private var _gold:int;

    public function get gold():int {
        return this._gold;
    }

    public function set gold(param1:int):void {
        this._gold = param1;
    }

    private var _isClaimed:Boolean;

    public function get isClaimed():Boolean {
        return this._isClaimed;
    }

    public function set isClaimed(param1:Boolean):void {
        this._isClaimed = param1;
    }

    private var _isCurrent:Boolean;

    public function get isCurrent():Boolean {
        return this._isCurrent;
    }

    public function set isCurrent(param1:Boolean):void {
        this._isCurrent = param1;
    }

    private var _claimKey:String = "";

    public function get claimKey():String {
        return this._claimKey;
    }

    public function set claimKey(param1:String):void {
        this._claimKey = param1;
    }

    private var _calendarType:String = "";

    public function get calendarType():String {
        return this._calendarType;
    }

    public function set calendarType(param1:String):void {
        this._calendarType = param1;
    }

    public function toString():String {
        return "Day " + this._dayNumber + ", item: " + this._itemID + " x" + this._quantity;
    }
}
}