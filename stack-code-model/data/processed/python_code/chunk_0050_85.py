package framework.view.pages.reservationCreate.events
{
    import flash.events.Event;
    
    import services.vo.frontend.ReservationCalendarCellVO;
    
    import mx.collections.ArrayCollection;

    public class ReservationCalendarEvent extends Event
    {
        public static const RCE_HEADER_CLICK:String = "calendarHeaderClickEvent";
        public static const RCE_HEADER_MOUSE_DOWN:String = "calendarHeaderMouseDownEvent";
        public static const RCE_ITEM_CLICK:String = "calendarItemClickEvent";
        public static const RCE_COLUMN_SELECTION_CHANGED:String = "columnSelectionChangedEvent";
        
        public var bedTypeNameFull:String;
        public var bedTypeName:String;
        public var roomTypeName:String;
        
        public var qualityId:int;
        public var cellData:ReservationCalendarCellVO;
        public var startDate:Date;
        public var endDate:Date;
        public var isAllOk:Boolean;
        
        private var _headerData:Object;
        private var _selectedData:ArrayCollection;
        
        public function ReservationCalendarEvent(type:String, bubbles:Boolean=true)
        {
            super(type, bubbles);
        }
        
        public function get headerData():Object
        {
            return _headerData;
        }
        
        public function get selectedData():ArrayCollection
        {
            return _selectedData;
        }
        
        public function set headerData(value:Object):void
        {
            _headerData = value;
        }
        
        public function set selectedData(value:ArrayCollection):void
        {
            _selectedData = value;
        }
    }
}