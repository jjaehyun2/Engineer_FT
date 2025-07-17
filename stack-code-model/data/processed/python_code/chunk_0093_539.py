package framework.view.pages.reservationCreate.parts
{
	import flash.events.Event;
	
	import mx.controls.advancedDataGridClasses.AdvancedDataGridItemRenderer;
	import mx.events.ListEvent;
	import mx.formatters.NumberFormatter;
	
	[Event (name="onItemDoubleClick", type="")]
	public class GroupReservationCalendarViewItemRenderer extends AdvancedDataGridItemRenderer
	{
        public static const RCVIR_COLOR_COLUMN_SELECTED:uint = 0xCCCCCC;
        public static const RCVIR_COLOR_CELL_SELECTED:uint = 0x33CCFF;
        public static const RCVIR_COLOR_NOT_ENOUGHT_ROOM:uint = 0x990000;
        public static const RCVIR_COLOR_NO_HIGHTLIGHT:uint = 0xFFFFFF;

        private const RCVIR_FRACTIONAL_SELECTION_ERROR:int = 10;
        
        public static const ON_ITEM_DOUBLE_CLICK_EVENT:String = "onItemDoubleClick";
        		
        //protected var _oParentTable:ReservationCalendar;
        protected var _sDataField:String;
        protected var _iRoomCount:int;
        protected var _oFormatter:NumberFormatter;
        protected var _sValue:String;
        protected var _iColor:uint;		
		
		public function GroupReservationCalendarViewItemRenderer()
		{
			super();
			//addEventListener(ListEvent.ITEM_DOUBLE_CLICK, onItemDoubleClick);
			addEventListener(Event.ADDED, hadleInstanceAdded);
		}
		
		/*private function onItemDoubleClick(event:ListEvent):void
		{
			dispatchEvent()
		}*/
		
        override public function set data(value:Object):void
        {
            super.data = value;			
            getValueFromData(value);
        }	
       
        private function hadleInstanceAdded(event:Event):void
        {
            //_oParentTable = findParentTable(this.parent);
            _sDataField = styleName.dataField;
            _oFormatter = styleName.formatter;
        }
 
        private function initializeShowProperties():void
        {
            _sValue = "";
            _iRoomCount = 0;
            _iColor = RCVIR_COLOR_NO_HIGHTLIGHT;

            background = false;
        }
               	
        private function getValueFromData(data:Object):void
        {
            initializeShowProperties();
            
            if(data != null)
            {
	            if(data.hasOwnProperty("children"))
	        	{
		            if( data.children.length > 0)
		            {
		        		var sum:int;
		        		for(var i:int = 0;i<data.children.length;i++)
		        		{
		        			if(data.children[i][_sDataField] != null)
		        			{
		        				sum += data.children[i][_sDataField].value;
		        			}
		        		}
		        		_sValue = sum == 0 ? " - " : sum.toString();
		            }
	        	} 
	        	else if (data.hasOwnProperty(_sDataField))
	            {
	            	if(data[_sDataField] != null)
	            	{
		                if (data[_sDataField].hasOwnProperty("value"))
		                {
							_sValue = data[_sDataField].value;//_oFormatter.format((data[_sDataField] as ReservationCalendarCellVO).fPriceOne) + " | " + (data[_sDataField] as ReservationCalendarCellVO).iEmptyCount;
		                }
		            }
		            else
		            {
		            	_sValue = " - ";
		            }
	            }
            }
        }	
        	
        override public function validateProperties():void
        {
            super.validateProperties();

            text = _sValue;
        }	
	}
}