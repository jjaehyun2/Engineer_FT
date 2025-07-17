package framework.view.pages.reservationCreate.parts
{
    import mx.controls.advancedDataGridClasses.AdvancedDataGridColumn;
    import mx.core.ClassFactory;

    public class ReservationCalendarViewColumn extends AdvancedDataGridColumn
    {
        protected var _bIsSelected:Boolean;
        private var _columnDate:Date;

        public function ReservationCalendarViewColumn(columnName:String=null,eventDescription:String = null)
        {
            super(columnName);
            var rcvcHeaderRenderer:ClassFactory = new ClassFactory(ReservationCalendarViewColumnHeaderRenderer);
            if(eventDescription != null && eventDescription != "")
            {
                rcvcHeaderRenderer.properties = {eventDescription:eventDescription};
            }

            headerRenderer = rcvcHeaderRenderer;

            sortable = false;
            _bIsSelected = false;
        }

        public function set columnDate(value:Date):void
        {
            _columnDate = value;
        }

        public function get columnDate():Date
        {
            return _columnDate;
        }

        public function get bIsSelected():Boolean
        {
            return _bIsSelected;
        }

        public function set bIsSelected(value:Boolean):void
        {
            _bIsSelected = value;
        }
    }
}