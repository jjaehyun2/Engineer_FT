package framework.view.pages.reservationCreate.component.dataGrid
{
	import framework.model.AppModelLocator;
	
	import mx.collections.ArrayCollection;
	import mx.controls.AdvancedDataGrid;
	import mx.controls.advancedDataGridClasses.AdvancedDataGridColumn;
	import mx.formatters.DateFormatter;
	import mx.formatters.NumberBaseRoundType;
	import mx.formatters.NumberFormatter;

	public class AvailableRoomsCalendar extends AdvancedDataGrid
	{
   		[Bindable]
    	public var model:AppModelLocator = AppModelLocator.getInstance();
    	[Bindable]
    	public var showRowCount:int;

        public static const RCV_NUMBER_OF_SHOWN_DAYS:int = 14;
        private const RCV_DAY_UNIX_TIME:Number = 86400;
      
        protected var _aCalendarData:ArrayCollection;
        protected var _dDateFrom:Date;
        protected var _dDateTo:Date;
        protected var _dDateArrival:Date;
        protected var _dDateDeparture:Date;        
        private var _oDateFormatter:DateFormatter;
        private var _oItemFormatter:NumberFormatter;
        
          	
		public function AvailableRoomsCalendar()
		{
			super();
			showHeaders = false;
			
            _oDateFormatter = new DateFormatter();
            _oDateFormatter.formatString = "DD / MMM";

            _oItemFormatter = new NumberFormatter();
            _oItemFormatter.rounding = NumberBaseRoundType.NEAREST;
            _oItemFormatter.precision = 2;
            _oItemFormatter.useNegativeSign = false;
            _oItemFormatter.useThousandsSeparator = false;		
            
            draggableColumns = false;
		}
		
		override public function set dataProvider(value:Object):void
        {
            super.dataProvider = value;
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
        		else
        		{
        			trace("Available Rooms Calendar row count = 0");
        		}
        	}
        }
        

   
		 
        public function set dateArrival(value:Date):void
        {
            _dDateArrival = value;
        }

        public function set dateDeparture(value:Date):void
        {
            _dDateDeparture = value;
        }       

        private function defineDateFrom():void
        {
            if (_dDateArrival == null)
            {
                _dDateFrom = null;
                return;
            }
            _dDateFrom = new Date(_dDateArrival.time);
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
        
        private function columnLabelFunction(item:Object, column:AdvancedDataGridColumn):String
        {
        	var result:String;
        	switch(column.dataField)
        	{
        		case "name":
        			if(item["name"].toString() == "def")
        			{
        				result = "Occ. DEF";
        			}
        			else if(item["name"].toString() == "def_ten")
        			{
        				result = "Occ. DEF/TEN";
        			}
        			else if(item["name"].toString() == "aval")
        			{
        				result = "Available Rooms";
        			}
         			else if(item["name"].toString() == "arriv")
        			{
        				result = "Arrival Rooms";
        			}       			
         			else if(item["name"].toString() == "dep")
        			{
        				result = "Departures";
        			}        			
          			else if(item["name"].toString() == "grp_def")
        			{
        				result = "Groups DEF";
        			}         			
          			else if(item["name"].toString() == "grp_ten")
        			{
        				result = "Groups TEN";
        			}        			
        		break;
        		default:
        			if(	item["name"].toString() == "def" || 
        				item["name"].toString() == "def_ten")
        			{
        				result = item[column.dataField].toString() + "%";	
        			}
        			else
        			{
        				result = item[column.dataField].toString();
        			}
        		break; 
        	}
        		
        	return result;
        }		
        
    		
		protected function buildColumns():void
        {
           var columnList:Array = [];
            var adgColumn:AdvancedDataGridColumn;

            adgColumn = new AdvancedDataGridColumn();
            adgColumn.dataField = "name";
            adgColumn.labelFunction = columnLabelFunction;
            adgColumn.width = 150;

            columnList.push(adgColumn);

            defineDateFrom();
            defineDateTo();

            if (_dDateFrom != null && _dDateTo != null)
            {
                var dDateCurrent:Date = new Date(_dDateFrom.time);
                var i:int = 0;

                while(dDateCurrent < _dDateTo)
                {
                    i++;
                    var cell:Object = _aCalendarData[0]["d"+i];
                   
                    adgColumn = new AdvancedDataGridColumn();
                    
                    
                    adgColumn.dataField = "d" + i.toString();
                    adgColumn.labelFunction = columnLabelFunction;
                    //adgColumn.formatter = _oItemFormatter;                    
                    //adgColumn.columnDate = new Date(dDateCurrent.time);

                    columnList.push(adgColumn);
                    dDateCurrent.seconds += RCV_DAY_UNIX_TIME;
                }
            }

            columns = columnList;	 
        }		
	}
}