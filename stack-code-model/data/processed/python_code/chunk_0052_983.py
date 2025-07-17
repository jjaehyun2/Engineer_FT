package view.fullcube
{

    import flash.events.Event;

    public class DirectionEvent extends Event
    {

        public static const DIRECTION_EVENT:String = "direction";

        public static const LEFT:String = "LEFT";

        public static const RIGHT:String = "RIGHT";

        public static const TOP:String = "TOP";

        public static const BOTTOM:String = "BOTTOM";

        public var direction:String;

        public var steps:int;

        public var directionType:String;

        public function DirectionEvent(direction:String, steps:int = 1, directionType:String = null)
        {
            super(DirectionEvent.DIRECTION_EVENT, true);
            this.direction = direction;
            this.steps = steps;
            this.directionType = directionType;
        }
    }
}