package
{
    import flash.display.Sprite;
    import flash.events.Event;
    import flash.events.TimerEvent;
    import flash.system.Security;
    import flash.utils.Timer;

    public class Creative extends Sprite implements IVPAID
    {
        private var _adLinear:Boolean = true;
        private var _adExpanded:Boolean = false;
        private var _adVolumeEnabled:Boolean = true;
        private var _adVolume:Number = 1.0; // in [0,1] or -1
        private var _adDuration:Number = 10;
        private var _timePlayed:Number;
        private var _timeStarted:Date;
        private var _paused:Boolean;
        private var _progressState:Number;
        private var _timer:Timer;

        public function Creative()
        {
            Console.log("\n============================================================\n\tFlash VPAID Player Tester\n\tVersion 1.0.0\n\n\tLearn more at http://github.com/ldgabbay/flash-vpaid-player-tester\n============================================================\n");

            Security.allowDomain("*");
            Security.allowInsecureDomain("*");

            this.mouseEnabled = false;
        }

        private function dispatchVPAID(eventType:String, data:Object=null):void
        {
            Console.log("sending event: " + eventType);

            this.dispatchEvent(new VPAIDEvent(eventType, data));
        }

        private function getTimeRemaining():Number
        {
            return Math.max(0, this._adDuration - this._timePlayed - (this._paused ? 0 : (new Date()).time - this._timeStarted.time) * 0.001);
        }

        private function onTimer(evt:TimerEvent):void
        {
            var timeRemaining:Number = this.getTimeRemaining();

            if ((this._progressState === 0) && (timeRemaining <= 0.75 * this._adDuration))
            {
                this.dispatchVPAID(VPAIDEvent.AdVideoFirstQuartile);
                this._progressState = 1;
            }
            if ((this._progressState === 1) && (timeRemaining <= 0.5 * this._adDuration))
            {
                this.dispatchVPAID(VPAIDEvent.AdVideoMidpoint);
                this._progressState = 2;
            }
            if ((this._progressState === 2) && (timeRemaining <= 0.25 * this._adDuration))
            {
                this.dispatchVPAID(VPAIDEvent.AdVideoThirdQuartile);
                this._progressState = 3;
            }
            if ((this._progressState === 3) && (timeRemaining === 0))
            {
                this.dispatchVPAID(VPAIDEvent.AdVideoComplete);
                this.dispatchVPAID(VPAIDEvent.AdStopped);
                this._progressState = 4;

                this._timer.stop();
            }
        }

        public function getVPAID():Object
        {
            Console.log("getVPAID");

            return this;
        }

        public function handshakeVersion(playerVPAIDVersion:String):String
        {
            Console.log("handshakeVersion");
            Console.log("    playerVPAIDVersion = " + playerVPAIDVersion);

            return "1.0";
        }

        public function initAd(initWidth:Number, initHeight:Number, viewMode:String, desiredBitrate:Number, creativeData:String, environmentVars:String):void
        {
            Console.log("initAd");
            Console.log("    initWidth = " + initWidth);
            Console.log("    initHeight = " + initHeight);
            Console.log("    viewMode = " + viewMode);
            Console.log("    desiredBitrate = " + desiredBitrate);
            Console.log("    creativeData = " + creativeData);
            Console.log("    environmentVars = " + environmentVars);

            this.dispatchVPAID(VPAIDEvent.AdLoaded);
        }

        public function resizeAd(width:Number, height:Number, viewMode:String):void
        {
            Console.log("resizeAd");
            Console.log("    width = " + width);
            Console.log("    height = " + height);
            Console.log("    viewMode = " + viewMode);
        }

        public function startAd():void
        {
            Console.log("startAd");

            this._timePlayed = 0.0;
            this._timeStarted = new Date();
            this._paused = false;
            this._progressState = 0;
            this.dispatchVPAID(VPAIDEvent.AdStarted);
            this.dispatchVPAID(VPAIDEvent.AdImpression);
            this.dispatchVPAID(VPAIDEvent.AdVideoStart);

            this._timer = new Timer(100, 0);
            this._timer.addEventListener(TimerEvent.TIMER, onTimer);
            this._timer.start();
        }

        public function stopAd():void
        {
            Console.log("stopAd");

            this.dispatchVPAID(VPAIDEvent.AdStopped);
        }

        public function pauseAd():void
        {
            Console.log("pauseAd");

            if (!this._paused)
            {
                this._paused = true;
                this._timePlayed += ((new Date()).time - this._timeStarted.time) * 0.001;
                this.dispatchVPAID(VPAIDEvent.AdPaused);
            }
        }

        public function resumeAd():void
        {
            Console.log("resumeAd");

            if (this._paused)
            {
                this._paused = false;
                this._timeStarted = new Date();
                this.dispatchVPAID(VPAIDEvent.AdPlaying);
            }
        }

        public function expandAd():void
        {
            Console.log("expandAd");
        }

        public function collapseAd():void
        {
            Console.log("collapseAd");
        }

        public function get adLinear():Boolean
        {
            Console.log("get adLinear -> " + this._adLinear);

            return this._adLinear;
        }

        public function get adExpanded():Boolean
        {
            Console.log("get adExpanded -> " + this._adExpanded);

            return this._adExpanded;
        }

        public function get adRemainingTime():Number
        {
            var retval:Number = this.getTimeRemaining();

            Console.log("get adRemainingTime -> " + retval);

            return retval;
        }

        public function get adVolume():Number
        {
            var retval:Number = this._adVolumeEnabled ? this._adVolume : -1;

            Console.log("get adVolume -> " + retval);

            return retval;
        }

        public function set adVolume(value:Number):void
        {
            Console.log("set adVolume <- " + value);

            if (this._adVolumeEnabled)
            {
                this._adVolume = value;
                this.dispatchVPAID(VPAIDEvent.AdVolumeChange);
            }
        }
    }
}