package sound.se
{
    import flash.media.*;
    import flash.events.Event;
    import flash.net.URLRequest;

    import sound.se.BaseSESound;

    public class PhaseSE extends BaseSESound

    {

        private static const URL:String = "/public/sound/se/ulse12.mp3";
        private var _url : URLRequest = new URLRequest(URL);
        private var _sound_obj : Sound = new Sound();

        // コンストラクタ
        public function PhaseSE()
        {

        }
        // オーバライド前提
        protected  override function get url():String
        {
            return URL;
        }

        
    }
}