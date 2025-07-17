package flash.events
{
    import flash.net.drm.*;
    import flash.utils.*;

    public class DRMMetadataEvent extends Event
    {
        private var m_timestamp:Number;
        private var m_drmMetadata:DRMContentData;
        public static const DRM_METADATA:String = "drmMetadata";

        public function DRMMetadataEvent(param1:String = "drmMetadata", param2:Boolean = false, param3:Boolean = false, param4:ByteArray = null, param5:Number = 0)
        {
            super(param1, param2, param3);
            this.m_drmMetadata = new DRMContentData(param4);
            this.m_timestamp = param5;
            return;
        }// end function

        public function get drmMetadata() : DRMContentData
        {
            return this.m_drmMetadata;
        }// end function

        public function get timestamp() : Number
        {
            return this.m_timestamp;
        }// end function

    }
}