package {
    import flash.events.*;
    import flash.external.ExternalInterface;
    import flash.media.SoundTransform;
    import flash.net.NetConnection;
    import flash.net.NetStream;
    import flash.net.URLRequest;
    import flash.utils.Timer;

    public class MP4Core extends BaseCore {
        private var nc:NetConnection;
        private var ns:NetStream;
        private var canPlayThrough:Boolean = false;
        private var isSeeking:Boolean = false;
        private var seekingTimer:Timer = new Timer(100, 0);

        override public function init(e:Event = null):void {
            super.init();

            seekingTimer.addEventListener(TimerEvent.TIMER, onSeekingTimer);

            if (ExternalInterface.available) {
                reset();
                nc = new NetConnection();
                nc.addEventListener(NetStatusEvent.NET_STATUS, onNetStatus);
                ExternalInterface.addCallback('f_load', f_load);
                ExternalInterface.addCallback('f_play', f_play);
                ExternalInterface.addCallback('f_pause', f_pause);
                ExternalInterface.addCallback('f_stop', f_stop);
                ExternalInterface.addCallback('getData', getData);
                ExternalInterface.addCallback('setData', setData);
                callOnLoad();
            }
        }

        private function seeking(active:Boolean):void {
            if (active) {
                isSeeking = true;
                seekingTimer.start();
            } else {
                isSeeking = false;
                seekingTimer.stop();
            }
        }

        private function connectStream():void {
            var customClient:Object = new Object();
            customClient.onMetaData = onMetaData;
            ns = new NetStream(nc);
            ns.addEventListener(NetStatusEvent.NET_STATUS, onNetStatus);
            ns.client = customClient;
            ns.soundTransform = stf;
            ns.play(_url);
            ns.pause();
        }

        // 事件含义可参考: http://help.adobe.com/zh_CN/AS2LCR/Flash_10.0/help.html?content=00001409.html
        private function onNetStatus(e:NetStatusEvent):void {
            // 实测发现，Play.Start会先于Buffer.Full触发，
            // 因此这段时间可认为是onProgress做些buffering
            switch (e.info.code) {
                // nc.connect后触发
                case 'NetConnection.Connect.Success':
                    connectStream();
                    break;
                case 'NetStream.Play.Start':
                    setState(State.BUFFERING);
                    onPlayTimer();
                    break;
                case 'NetStream.Buffer.Full':
                    setState(State.PLAYING);
                case 'NetStream.Play.Stop':
                    onPlayTimer();
                    // jPlayer: Check if media is at the end (or close) otherwise this was due to download bandwidth stopping playback. ie., Download is not fast enough.
                    if (_length && Math.abs(_length - _position) < 150) { // Testing found 150ms worked best for M4A files, where playHead(99.9) caused a stuck state due to firing with ~116ms left to play.// Testing found 150ms worked best for M4A files, where playHead(99.9) caused a stuck state due to firing with ~116ms left to play.
                        onPlayComplete();
                    }
                    break;
                case 'NetStream.Seek.InvalidTime':
                    onPlayComplete();
                    break;
                case 'NetStream.Play.StreamNotFound':
                    handleErr();
                    break;
            }
        }

        private function onMetaData(meta:Object):void {
            // Only available via Meta Data.
            _length = meta.duration * 1000;
        }

        private function onProgress():void {
            _bytesTotal = ns.bytesTotal;
            _bytesLoaded = ns.bytesLoaded;
            _loadedPct = Math.round(100 * _bytesLoaded / _bytesTotal) / 100;

            if (_loadedPct === 1 && !canPlayThrough) {
                canPlayThrough = true;
                setState(State.CANPLAYTHROUGH);
            }
        }

        private function onSeekingTimer(e:TimerEvent):void {
            if (_length) {
                if (_pausePosition > _length) {
                    seeking(false);
                    f_play();
                } else {
                    var seekPct:Number = Math.floor(100 * _pausePosition / _length) / 100;
                    if (seekPct <= _loadedPct) {
                        seeking(false);
                        // 注意换算单位，seek的参数是秒，而position则是毫秒
                        ns.seek(_pausePosition / 1000);
                        ns.resume();
                    }
                }
            }
        }

        override protected function onPlayTimer(e:TimerEvent = null):void {
            if (ns) {
                updatePostion(ns.time * 1000);
            }
            if (!canPlayThrough) {
                onProgress();
            }
        }

        override public function setVolume(v:uint):Boolean {
            var success:Boolean = super.setVolume(v);
            if (success && ns) {
                ns.soundTransform = stf;
            }
            return success;
        }

        override public function reset():void {
            seeking(false);
            canPlayThrough = false;
            if (ns) {
                ns.removeEventListener(NetStatusEvent.NET_STATUS, onNetStatus);
                ns = null;
            }
        }

        override public function f_load(url:String):void {
            f_stop();
            try {
                ns && ns.close();
            } catch (err:Error) {
            } finally {
                reset();
            }
            _url = url;
            nc.connect(null);
            setState(State.PREBUFFER);
        }

        override public function f_play(p:Number = 0):void {
            if (!_url) {
                return;
            }

            super.f_play(p);

            if (!p && _pausePosition) {
                p = _pausePosition;
            }

            try {
                ns.pause();
                if (p !== 0) {
                    seeking(true);
                    _pausePosition = p;
                } else {
                    ns.resume();
                }
            } catch (err:Error) {
                return handleErr(err);
            }
        }

        override public function f_pause():void {
            if (ns) {
                f_stop(ns.time * 1000);
            }
        }

        override public function f_stop(p:Number = -1):void {
            super.f_stop(p);
            seeking(false);
            // 判断ns是否存在是因为ns在load方法调用时才被延迟初始化
            if (ns) {
                ns.pause();
            }
        }
    }
}