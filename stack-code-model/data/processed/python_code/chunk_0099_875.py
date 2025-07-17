package flash.events
{
    import flash.net.drm.*;

    public class DRMDeviceGroupEvent extends Event
    {
        private var m_deviceGroup:DRMDeviceGroup;
        public static const ADD_TO_DEVICE_GROUP_COMPLETE:String = "addToDeviceGroupComplete";
        public static const REMOVE_FROM_DEVICE_GROUP_COMPLETE:String = "removeFromDeviceGroupComplete";

        public function DRMDeviceGroupEvent(param1:String, param2:Boolean = false, param3:Boolean = false, param4:DRMDeviceGroup = null)
        {
            super(param1, param2, param3);
            this.m_deviceGroup = param4;
            return;
        }// end function

        public function set deviceGroup(param1:DRMDeviceGroup)
        {
            this.m_deviceGroup = param1;
            return;
        }// end function

        public function get deviceGroup() : DRMDeviceGroup
        {
            return this.m_deviceGroup;
        }// end function

        override public function clone() : Event
        {
            return new DRMDeviceGroupEvent(type, bubbles, cancelable, this.m_deviceGroup);
        }// end function

        override public function toString() : String
        {
            return formatToString("DRMDeviceGroupEvent", "type", "bubbles", "cancelable", "eventPhase", "deviceGroup");
        }// end function

    }
}