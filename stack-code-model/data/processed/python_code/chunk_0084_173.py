package com.videojs.events{

    import flash.events.Event;

    public class VideoJSEvent extends Event{

        public static const STAGE_RESIZE:String = "VideoJSEvent.STAGE_RESIZE";
        public static const BACKGROUND_COLOR_SET:String = "VideoJSEvent.BACKGROUND_COLOR_SET";
        public static const FULL_SCREEN_CHANGE:String = "VideoJSEvent.FULL_SCREEN_CHANGE";
        public static const CONTROLS_SET:String = "VideoJSEvent.CONTROLS_SET";
        public static const POSTER_SET:String = "VideoJSEvent.POSTER_SET";

        // a flexible container object for whatever data needs to be attached to any of these events
        private var _data:Object;

        public function VideoJSEvent(pType:String, pData:Object = null){
            super(pType, true, false);
            _data = pData;
        }

        public function get data():Object {
            return _data;
        }

    }
}