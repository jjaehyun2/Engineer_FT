package freevana.util
{
    // TODO: only import what we actually use
    import flash.net.*;
    import flash.events.*;
    import flash.utils.ByteArray;

    /*
    * @author tirino
    */
    public class Subtitles
    {
        private static var MOVIES_SUBTITLES_BASEURL:String = 'http://sc.cuevana.tv/files/sub/';
        private static var SERIES_SUBTITLES_BASEURL:String = 'http://sc.cuevana.tv/files/s/sub/';
        private static var SUBTITLES_DIR:String = "subtitles";
        private var _settings:Settings;

        public function Subtitles()
        {
            _settings = new Settings();
        }
    }
}