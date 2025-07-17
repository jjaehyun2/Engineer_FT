package framework.view.pages.reservationCreate.parts
{
    import flash.events.Event;
    import flash.events.MouseEvent;
    
    import framework.view.pages.reservationCreate.component.dataGrid.ReservationCalendar;
    import framework.view.pages.reservationCreate.data.ReservationCalendarModel;
    
    import mx.binding.utils.ChangeWatcher;
    import mx.controls.advancedDataGridClasses.AdvancedDataGridItemRenderer;
    import mx.formatters.NumberFormatter;
    
    import services.vo.frontend.ReservationCalendarCellVO;

    public class ReservationCalendarViewItemRenderer extends AdvancedDataGridItemRenderer
    {
        public static const RCVIR_COLOR_COLUMN_SELECTED:uint = 0xCCCCCC;
        public static const RCVIR_COLOR_CELL_SELECTED:uint = 0x33CCFF;
        public static const RCVIR_COLOR_NOT_ENOUGHT_ROOM:uint = 0x990000;
        public static const RCVIR_COLOR_NO_HIGHTLIGHT:uint = 0xFFFFFF;

        private const RCVIR_FRACTIONAL_SELECTION_ERROR:int = 10;

        protected var _oParentTable:ReservationCalendar;
        protected var _sDataField:String;
        protected var _iRoomCount:int;
        protected var _oFormatter:NumberFormatter;
        protected var _sValue:String;
        protected var _iColor:uint;

        private var _changeWatcher:ChangeWatcher;

        public function ReservationCalendarViewItemRenderer()
        {
            super();

            addEventListener(Event.ADDED, hadleInstanceAdded);
            addEventListener(MouseEvent.MOUSE_DOWN, handleMouseDown);

            _changeWatcher = ChangeWatcher.watch(ReservationCalendarModel.instance, "enableColumnSelection", handleColumnSelectionChange);

           // toolTip = "Test Message: More information about cell";

            initializeShowProperties();
        }

        private function hadleInstanceAdded(event:Event):void
        {
            _oParentTable = findParentTable(this.parent);
            _sDataField = styleName.dataField;
            _oFormatter = styleName.formatter;
        }

        private function handleColumnSelectionChange(event:Event):void
        {
            if (ReservationCalendarModel.instance.enableColumnSelection)
            {
                addEventListener(MouseEvent.ROLL_OVER, handleMouseRollOver);
            }
            else
            {
                removeEventListener(MouseEvent.ROLL_OVER, handleMouseRollOver);
            }
        }

        private function handleMouseRollOver(event:MouseEvent):void
        {
            ReservationCalendarModel.instance.lastSelectedColumnIndex = listData.columnIndex;
            ReservationCalendarModel.instance.calendarIsUpdated = false;
        }

        private function handleMouseDown(event:MouseEvent):void
        {
            addEventListener(MouseEvent.MOUSE_UP, handleMouseUp);
            addEventListener(MouseEvent.ROLL_OUT, handleMouseRollOut);
        }

        private function handleMouseUp(event:MouseEvent):void
        {
            removeEventListener(MouseEvent.MOUSE_UP, handleMouseUp);
            removeEventListener(MouseEvent.ROLL_OUT, handleMouseRollOut);
        }

        private function handleMouseRollOut(event:MouseEvent):void
        {
            stage.addEventListener(MouseEvent.MOUSE_UP, handleStageMouseUp);

            removeEventListener(MouseEvent.MOUSE_UP, handleMouseUp);
            removeEventListener(MouseEvent.ROLL_OUT, handleMouseRollOut);

            ReservationCalendarModel.instance.firstSelectedColumnIndex = listData.columnIndex;
            ReservationCalendarModel.instance.enableColumnSelection = true;
        }

        private function handleStageMouseUp(event:MouseEvent):void
        {
            ReservationCalendarModel.instance.enableColumnSelection = false;

            stage.removeEventListener(MouseEvent.MOUSE_UP, handleStageMouseUp);
        }

        private function findParentTable(parentContainer:Object):ReservationCalendar
        {
            if (parentContainer == null)
            {
                return null;
            }

            if (parentContainer is ReservationCalendar)
            {
                return (parentContainer as ReservationCalendar);
            }
            else
            {
                return findParentTable(parentContainer.parent);
            }
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
	            if (data.hasOwnProperty(_sDataField))
	            {
	                if (data[_sDataField] is ReservationCalendarCellVO)
	                {
	
	                	if(data.hasOwnProperty("children") && data.children.length > 0)
	                	{
	                		var sumBedType:int;
	                		for(var i:int = 0;i<data.children.length;i++)
	                		{
	                			sumBedType += (data.children[i][_sDataField] as ReservationCalendarCellVO).iEmptyCount;
	                		}
	                		_sValue = "Free: " + sumBedType.toString();
	                		_iRoomCount = sumBedType;
	                	}
	                	else
	                	{
	                    	_sValue = _oFormatter.format((data[_sDataField] as ReservationCalendarCellVO).fPriceOne) + " | " + (data[_sDataField] as ReservationCalendarCellVO).iEmptyCount;
	                 		_iRoomCount = (data[_sDataField] as ReservationCalendarCellVO).iEmptyCount;                 	
	                 	}
	                    if((data[_sDataField] as ReservationCalendarCellVO).iPackageRateId > 0)
	                    {
	                    	_sValue += "\n";
	                    	_sValue += (data[_sDataField] as ReservationCalendarCellVO).bPriceIsPerStay ? "PPS" : "PPN";
	                    }
	                }
	            }
	         }
        }

        override public function validateProperties():void
        {
            super.validateProperties();

            text = _sValue;

            if (ReservationCalendarModel.instance.selectedColumnDataFieldList.contains(_sDataField))
            {
                background = true;
                ReservationCalendarModel.instance.isNotEnoughRooms = false;

                _iColor = RCVIR_COLOR_COLUMN_SELECTED;

                if (_iRoomCount <= 0)
                {
                    _iColor = RCVIR_COLOR_NOT_ENOUGHT_ROOM;
                }

                /* var arr:ArrayCollection = ReservationCalendarModel.instance.selectedItemDataFieldList;

                if(arr.length > 0)
                {
	                var isContain:Boolean = arr.contains(_sDataField);
	                var selRow:int = ReservationCalendarModel.instance.selectedRow
	                var isRow:Boolean = (listData.rowIndex == ReservationCalendarModel.instance.selectedRow);
                } */

                if (ReservationCalendarModel.instance.selectedItemDataFieldList.contains(_sDataField) && listData.rowIndex == ReservationCalendarModel.instance.selectedRow)
                {
                	//if(_iColor == RCVIR_COLOR_NOT_ENOUGHT_ROOM) ReservationCalendarModel.instance.isNotEnoughRooms = true;

                    _iColor = RCVIR_COLOR_CELL_SELECTED;
                }
            }

            backgroundColor = _iColor;
        }

        override public function set data(value:Object):void
        {
            super.data = value;
			
            getValueFromData(value);
        }
    }
}