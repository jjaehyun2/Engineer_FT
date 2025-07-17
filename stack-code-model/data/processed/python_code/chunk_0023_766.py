package framework.view.pages.reservationCreate.component.dataGrid
{
    import flash.events.Event;
    
    import framework.model.AppModelLocator;
    import framework.view.pages.reservationCreate.data.ReservationCalendarModel;
    import framework.view.pages.reservationCreate.events.ReservationCalendarEvent;
    import framework.view.pages.reservationCreate.parts.ReservationCalendarViewColumn;
    import framework.view.pages.reservationCreate.parts.ReservationCalendarViewGroupItemRenderer;
    import framework.view.pages.reservationCreate.parts.ReservationCalendarViewItemRenderer;
    
    import mx.binding.utils.ChangeWatcher;
    import mx.collections.ArrayCollection;
    import mx.collections.HierarchicalData;
    import mx.controls.AdvancedDataGrid;
    import mx.controls.advancedDataGridClasses.AdvancedDataGridColumn;
    import mx.core.ClassFactory;
    import mx.events.ListEvent;
    import mx.formatters.DateFormatter;
    import mx.formatters.NumberBaseRoundType;
    import mx.formatters.NumberFormatter;
    
    import services.vo.GlobalSettings;
    import services.vo.frontend.ReservationCalendarCellVO;
    import mx.collections.HierarchicalCollectionView;
    import flash.events.MouseEvent;

    [Event(name="calendarItemClickEvent", type="framework.view.pages.reservationCreate.events.ReservationCalendarEvent")]

    public class ReservationCalendar extends AdvancedDataGrid
    {

    	[Bindable]
    	public var model:AppModelLocator = AppModelLocator.getInstance();
    	[Bindable]
    	public var showRowCount:int;
    	
        public static const RCV_ROOM_TYPE_COLUMN_DATA_FIELD:String = "name";
        public static const RCV_NUMBER_OF_SHOWN_DAYS:int = 14;

        private const RCV_DAY_UNIX_TIME:Number = 86400;

        protected var _aCalendarData:ArrayCollection;
        protected var _dDateFrom:Date;
        protected var _dDateTo:Date;
        protected var _dDateArrival:Date;
        protected var _dDateDeparture:Date;
        private var _oDateFormatter:DateFormatter;
        private var _oItemFormatter:NumberFormatter;

        private var _changeWatcher:ChangeWatcher;

        public function ReservationCalendar()
        {
            super();


            _oDateFormatter = new DateFormatter();
            _oDateFormatter.formatString = "DD / MMM";


            _oItemFormatter = new NumberFormatter();
            _oItemFormatter.rounding = NumberBaseRoundType.NEAREST;
            _oItemFormatter.precision = 2;
            _oItemFormatter.useNegativeSign = false;
            _oItemFormatter.useThousandsSeparator = false;

            itemRenderer = new ClassFactory(ReservationCalendarViewItemRenderer);
            groupItemRenderer = new ClassFactory(ReservationCalendarViewGroupItemRenderer);
            draggableColumns = false;
            selectionMode = "multipleCells";

            _changeWatcher = ChangeWatcher.watch(ReservationCalendarModel.instance, "calendarIsUpdated", handleColumnSelectionChange);
            addEventListener(ListEvent.ITEM_CLICK, onItemSelect);
        }

        public function isNeedNewData(dDateArrival:Date, dDateDeparture:Date):Boolean
        {
            if (dDateArrival < this._dDateFrom || dDateDeparture >= this._dDateTo)
            {
                return true;
            }
            return false;
        }

        public function updateColumnsSelection():void
        {
            var dDateCurrent:Date = new Date(_dDateFrom.time);
            var i:int = 1;

            ReservationCalendarModel.instance.selectedColumnDataFieldList.removeAll();

            while(dDateCurrent < _dDateTo)
            {
                if (dDateCurrent >= _dDateArrival && dDateCurrent <= _dDateDeparture)
                {
                    (columns[i] as ReservationCalendarViewColumn).bIsSelected = true;

                    ReservationCalendarModel.instance.selectedColumnDataFieldList.addItem(columns[i].dataField);
                }
                else
                {
                    (columns[i] as ReservationCalendarViewColumn).bIsSelected = false;
                }

                i++;
                dDateCurrent.seconds += RCV_DAY_UNIX_TIME;
            }
        }

        public function getFirstDate():Date
        {
        	return (columns[1] as ReservationCalendarViewColumn).columnDate;
        }

        public function getLastDate():Date
        {
        	return (columns[columns.length-1] as ReservationCalendarViewColumn).columnDate;
        }

        protected function buildColumns():void
        {
            var columnList:Array = [];
            var adgColumn:ReservationCalendarViewColumn;
            var reservationCalendarModel:ReservationCalendarModel = ReservationCalendarModel.instance;

            adgColumn = new ReservationCalendarViewColumn("Room type");
            adgColumn.dataField = RCV_ROOM_TYPE_COLUMN_DATA_FIELD;
            adgColumn.width = 150;

            columnList.push(adgColumn);

            defineDateFrom();
            defineDateTo();

            reservationCalendarModel.selectedColumnDataFieldList.removeAll();

            if (_dDateFrom != null && _dDateTo != null)
            {
                var dDateCurrent:Date = new Date(_dDateFrom.time);
                var i:int = 0;

                while(dDateCurrent < _dDateTo)
                {
                    i++;
                    var cell:ReservationCalendarCellVO = _aCalendarData[0]["d"+i];
                    var eventName:String = cell.sEvent; 
                    
                    adgColumn = new ReservationCalendarViewColumn(_oDateFormatter.format(dDateCurrent) + "\n" + GlobalSettings.daysShort[dDateCurrent.getDay()],eventName);
                    //adgColumn = new ReservationCalendarViewColumn(_oDateFormatter.format(dDateCurrent));
                    
                    adgColumn.dataField = "d" + i.toString();
                    adgColumn.formatter = _oItemFormatter;
                    adgColumn.columnDate = new Date(dDateCurrent.time);

                    if (dDateCurrent >= _dDateArrival && dDateCurrent <= _dDateDeparture)
                    {
                        adgColumn.bIsSelected = true;

                        ReservationCalendarModel.instance.firstSelectedColumnIndex = (ReservationCalendarModel.instance.firstSelectedColumnIndex == 0) ?
                        															  i : ReservationCalendarModel.instance.firstSelectedColumnIndex;

                        reservationCalendarModel.selectedColumnDataFieldList.addItem(adgColumn.dataField);
                    }
                    else
                    {
                    	ReservationCalendarModel.instance.lastSelectedColumnIndex = (ReservationCalendarModel.instance.lastSelectedColumnIndex == 0) ?
                    																 i - 1 : ReservationCalendarModel.instance.lastSelectedColumnIndex;

                        adgColumn.bIsSelected = false;
                    }

                    columnList.push(adgColumn);
                    dDateCurrent.seconds += RCV_DAY_UNIX_TIME;
                }
            }

            columns = columnList;
        }

        protected function handleColumnSelectionChange(event:Event):void
        {
            if (!ReservationCalendarModel.instance.calendarIsUpdated)
            {
                var firstIndex:int = Math.min(ReservationCalendarModel.instance.firstSelectedColumnIndex, ReservationCalendarModel.instance.lastSelectedColumnIndex);
                var lastIndex:int = Math.max(ReservationCalendarModel.instance.firstSelectedColumnIndex, ReservationCalendarModel.instance.lastSelectedColumnIndex);

                ReservationCalendarModel.instance.selectedColumnDataFieldList.removeAll();

                for(var i:int = 0; i < columns.length; i++)
                {
                    if (i >= firstIndex && i <= lastIndex)
                    {
                        columns[i].bIsSelected = true;
                        if(i == firstIndex)
                        {
                        	(columns[i] as AdvancedDataGridColumn).setStyle("headerStyleName","reservationFirstColumnHeader");
                        }

                        if(i > firstIndex && i < lastIndex)
                        {
                        	(columns[i] as AdvancedDataGridColumn).setStyle("headerStyleName","reservationMiddleColumnHeader");
                        }

                        if(i == lastIndex)
                        {
                        	(columns[i] as AdvancedDataGridColumn).setStyle("headerStyleName","reservationLastColumnHeader");
                        }
                        ReservationCalendarModel.instance.selectedColumnDataFieldList.addItem(columns[i].dataField);
                    }
                    else
                    {
                        columns[i].bIsSelected = false;

                       	(columns[i] as AdvancedDataGridColumn).setStyle("headerStyleName","");
                    }
                }

                ReservationCalendarModel.instance.selectedItemDataFieldList.removeAll();
                selectedCells = [];

                invalidateList();

                ReservationCalendarModel.instance.calendarIsUpdated = true;

                var rcEvent:ReservationCalendarEvent = new ReservationCalendarEvent(ReservationCalendarEvent.RCE_COLUMN_SELECTION_CHANGED);

                rcEvent.startDate = (columns[firstIndex] as ReservationCalendarViewColumn).columnDate;
				rcEvent.endDate = (columns[lastIndex] as ReservationCalendarViewColumn).columnDate;

                dispatchEvent(rcEvent);
            }
        }
        override public function expandItem(item:Object, open:Boolean, animate:Boolean=false, dispatchEvent:Boolean=false, cause:Event=null):void
        {
        	super.expandItem(item, open, animate, dispatchEvent, cause);
        	calculateHeight();
        }

		private function calculateHeight():void
		{
            if(super.dataProvider is HierarchicalCollectionView)
            {
            	showRowCount = (super.dataProvider as HierarchicalCollectionView).length;
            	invalidateDisplayList();
            }			
		}

        protected function onItemSelect(event:ListEvent):void
        {
        	if(event.columnIndex == 0) return;

        	/*  || event.columnIndex < ReservationCalendarModel.instance.firstSelectedColumnIndex ||
        	event.columnIndex > ReservationCalendarModel.instance.lastSelectedColumnIndex */

            var resultArray:ArrayCollection = new ArrayCollection();
            var selectedCellIndexList:Array = [];
            var columnIsFound:Boolean = false;
            var currentColumn:ReservationCalendarViewColumn;
            var currentData:ReservationCalendarCellVO;

            ReservationCalendarModel.instance.selectedRow = event.rowIndex;
            ReservationCalendarModel.instance.selectedItemDataFieldList.removeAll();

            for(var i:int = 1; i < columns.length; i++)
            {
                currentColumn = columns[i] as ReservationCalendarViewColumn;
                currentData = event.itemRenderer.data[(columns[i] as ReservationCalendarViewColumn).dataField] as ReservationCalendarCellVO;

               /*  if(currentColumn.bIsSelected && (event.itemRenderer.data["d" + i] as ReservationCalendarCellVO).iEmptyCount == 0)
                {
                	Alert.show("Such number of rooms is not available for the selected days");
                	return;
                } */
                if(currentColumn.bIsSelected)
                {
                	 ReservationCalendarModel.instance.selectedItemDataFieldList.addItem(columns[i].dataField);
                }

                if ( currentColumn.bIsSelected) //currentData.iEmptyCount >= _iNeedRoomCount &&
                {
                    resultArray.addItem(currentData);
                    selectedCellIndexList.push({rowIndex:event.rowIndex, columnIndex:i});
                    //ReservationCalendarModel.instance.selectedItemDataFieldList.addItem(columns[i].dataField);



                    if (i == event.columnIndex)
                    {
                        columnIsFound = true;
                    }
                }
                else
                {
                    if (!columnIsFound)
                    {
                        resultArray.removeAll();
                        /* ReservationCalendarModel.instance.selectedItemDataFieldList.removeAll();
                        selectedCellIndexList.splice(0, selectedCellIndexList.length); */
                    }
                    else
                    {
                        break;
                    }
                }
            }

            if (!columnIsFound)
            {
                /* resultArray.removeAll();
                ReservationCalendarModel.instance.selectedItemDataFieldList.removeAll();
                selectedCellIndexList.splice(0, selectedCellIndexList.length); */
            }

            var sArr:ArrayCollection = ReservationCalendarModel.instance.selectedItemDataFieldList;

            selectedCells = selectedCellIndexList;

            invalidateList();

            var firstIndex:int = Math.min(ReservationCalendarModel.instance.firstSelectedColumnIndex, ReservationCalendarModel.instance.lastSelectedColumnIndex);
            var lastIndex:int = Math.max(ReservationCalendarModel.instance.firstSelectedColumnIndex, ReservationCalendarModel.instance.lastSelectedColumnIndex);
            var rcEvent:ReservationCalendarEvent = new ReservationCalendarEvent(ReservationCalendarEvent.RCE_ITEM_CLICK);

            rcEvent.cellData = event.itemRenderer.data["d" + event.columnIndex];
            rcEvent.bedTypeNameFull = event.itemRenderer.data["fullName"];
			rcEvent.bedTypeName = event.itemRenderer.data["name"];
			rcEvent.roomTypeName = event.itemRenderer.data.hasOwnProperty("typeName") ? event.itemRenderer.data["typeName"] : event.itemRenderer.data["name"];
			
            if(event.itemRenderer.data.hasOwnProperty("qualityId"))
            {
            	rcEvent.qualityId = int(event.itemRenderer.data["qualityId"]);
            }
            else
            {
            	var resData:ArrayCollection = model.reservationModule.aCalendar;

            	for(var k:int=0;k<resData.length;k++)
            	{
            		try {
	            		for(var j:int=0;j<(resData[k].children as Array).length;j++)
	            		{
	            			if(resData[k].children[j] == event.itemRenderer.data)
	            			{
	            				rcEvent.qualityId = int(resData[k]["qualityId"]);
	            				break;
	            			}
	            		}
	            	}catch(e:Error){}
            	}

            }

			rcEvent.startDate = (columns[firstIndex] as ReservationCalendarViewColumn).columnDate;
			rcEvent.endDate = (columns[lastIndex] as ReservationCalendarViewColumn).columnDate;

			/* var roomCountInFirstColumn:int = (event.itemRenderer.data[(columns[firstIndex] as ReservationCalendarViewColumn).dataField] as ReservationCalendarCellVO).iEmptyCount;
			var roomCountInLastColumn:int = (event.itemRenderer.data[(columns[lastIndex] as ReservationCalendarViewColumn).dataField] as ReservationCalendarCellVO).iEmptyCount;
			rcEvent.isAllOk = (roomCountInFirstColumn >= _iNeedRoomCount && roomCountInLastColumn >= _iNeedRoomCount); */

            rcEvent.selectedData = resultArray;

            dispatchEvent(rcEvent);
        }

        private function defineDateFrom():void
        {
            if (_dDateArrival == null)
            {
                _dDateFrom = null;

                return;
            }

            _dDateFrom = new Date(_dDateArrival.time);
            //_dDateFrom.seconds -= _dDateArrival.day * RCV_DAY_UNIX_TIME
        }

        private function defineDateTo():void
        {
            if (_dDateFrom == null)
            {
                _dDateTo = null;

                return;
            }

            _dDateTo = new Date(_dDateArrival.time);
            _dDateTo.seconds += RCV_NUMBER_OF_SHOWN_DAYS * RCV_DAY_UNIX_TIME;
        }

	override protected function updateDisplayList(unscaledWidth:Number, unscaledHeight:Number):void
	{
		super.updateDisplayList(unscaledWidth, unscaledHeight);
		height = (showRowCount * rowHeight) + 50;
	}

        override public function set dataProvider(value:Object):void
        {
            super.dataProvider = new HierarchicalData(value);
            showRowCount = 0;
            if(value != null)
            {
            	if(value is ArrayCollection)
            	{            		
            		showRowCount = (value as ArrayCollection).length;            		
            	}
            }
        }

        public function set aCalendarData(value:ArrayCollection):void
        {
        	if(value != null)
        	{
        		if(value.length > 0)
        		{
		            _aCalendarData = value;
		
		            buildColumns();
		
		            dataProvider = _aCalendarData;
		
		            invalidateList();
		         }
        	}
        	calculateHeight();
        }

        public function set dateArrival(value:Date):void
        {
            _dDateArrival = value;
        }


        public function set dateDeparture(value:Date):void
        {
            _dDateDeparture = value;
        }
    }
}