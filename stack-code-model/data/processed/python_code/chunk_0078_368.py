
//Created by Action Script Viewer - http://www.buraks.com/asv
    class mx.video.VideoPlayer extends MovieClip
    {
        var _state, _cachedState, _bufferState, _cachedPlayheadTime, _metadata, _startingPlay, _invalidSeekTime, _invalidSeekRecovery, _currentPos, _atEnd, _cmdQueue, _readyDispatched, _autoResizeDone, _lastUpdateTime, _sawSeekNotify, _updateTimeIntervalID, _updateTimeInterval, _updateProgressIntervalID, _updateProgressInterval, _idleTimeoutIntervalID, _idleTimeoutInterval, _autoResizeIntervalID, _rtmpDoStopAtEndIntervalID, _rtmpDoSeekIntervalID, _httpDoSeekIntervalID, _httpDoSeekCount, _finishAutoResizeIntervalID, _delayedBufferingIntervalID, _delayedBufferingInterval, _isLive, _autoSize, _aspectRatio, _autoPlay, _autoRewind, _bufferTime, _volume, _sound, __visible, _hiddenForResize, _hiddenForResizeMetadataDelay, _contentPath, _video, _ncMgr, _ns, attachAudio, _prevVideoWidth, _prevVideoHeight, _streamLength, _videoWidth, _videoHeight, dispatchEvent, _x, _y, _visible, _hiddenRewindPlayheadTime, ncMgrClassName, _height, _width;
        function VideoPlayer () {
            super();
            mx.events.EventDispatcher.initialize(this);
            _state = DISCONNECTED;
            _cachedState = _state;
            _bufferState = BUFFER_EMPTY;
            _cachedPlayheadTime = 0;
            _metadata = null;
            _startingPlay = false;
            _invalidSeekTime = false;
            _invalidSeekRecovery = false;
            _currentPos = 0;
            _atEnd = false;
            _cmdQueue = new Array();
            _readyDispatched = false;
            _autoResizeDone = false;
            _lastUpdateTime = -1;
            _sawSeekNotify = false;
            _updateTimeIntervalID = 0;
            _updateTimeInterval = DEFAULT_UPDATE_TIME_INTERVAL;
            _updateProgressIntervalID = 0;
            _updateProgressInterval = DEFAULT_UPDATE_PROGRESS_INTERVAL;
            _idleTimeoutIntervalID = 0;
            _idleTimeoutInterval = DEFAULT_IDLE_TIMEOUT_INTERVAL;
            _autoResizeIntervalID = 0;
            _rtmpDoStopAtEndIntervalID = 0;
            _rtmpDoSeekIntervalID = 0;
            _httpDoSeekIntervalID = 0;
            _httpDoSeekCount = 0;
            _finishAutoResizeIntervalID = 0;
            _delayedBufferingIntervalID = 0;
            _delayedBufferingInterval = HTTP_DELAYED_BUFFERING_INTERVAL;
            if (_isLive == undefined) {
                _isLive = false;
            }
            if (_autoSize == undefined) {
                _autoSize = false;
            }
            if (_aspectRatio == undefined) {
                _aspectRatio = true;
            }
            if (_autoPlay == undefined) {
                _autoPlay = true;
            }
            if (_autoRewind == undefined) {
                _autoRewind = true;
            }
            if (_bufferTime == undefined) {
                _bufferTime = 0.1;
            }
            if (_volume == undefined) {
                _volume = 100;
            }
            _sound = new Sound(this);
            _sound.setVolume(_volume);
            __visible = true;
            _hiddenForResize = false;
            _hiddenForResizeMetadataDelay = 0;
            _contentPath = "";
        }
        function setSize(_arg3, _arg2) {
            if (((_arg3 == _video._width) && (_arg2 == _video._height)) || (_autoSize)) {
                return(undefined);
            }
            _video._width = _arg3;
            _video._height = _arg2;
            if (_aspectRatio) {
                startAutoResize();
            }
        }
        function setScale(_arg3, _arg2) {
            if (((_arg3 == _video._xscale) && (_arg2 == _video._yscale)) || (_autoSize)) {
                return(undefined);
            }
            _video._xscale = _arg3;
            _video._yscale = _arg2;
            if (_aspectRatio) {
                startAutoResize();
            }
        }
        function play(_arg2, _arg3, _arg4) {
            if ((_arg2 != null) && (_arg2 != undefined)) {
                if (_state == EXEC_QUEUED_CMD) {
                    _state = _cachedState;
                } else if (!stateResponsive) {
                    queueCmd(PLAY, _arg2, _arg3, _arg4);
                    return(undefined);
                } else {
                    execQueuedCmds();
                }
                _autoPlay = true;
                _load(_arg2, _arg3, _arg4);
                return(undefined);
            }
            if (!isXnOK()) {
                if (((((_state == CONNECTION_ERROR) || (_ncMgr == null)) || (_ncMgr == undefined)) || (_ncMgr.getNetConnection() == null)) || (_ncMgr.getNetConnection() == undefined)) {
                    throw new mx.video.VideoError(mx.video.VideoError.NO_CONNECTION);
                } else {
                    flushQueuedCmds();
                    queueCmd(PLAY);
                    setState(LOADING);
                    _cachedState = LOADING;
                    _ncMgr.reconnect();
                    return(undefined);
                }
            } else if (_state == EXEC_QUEUED_CMD) {
                _state = _cachedState;
            } else if (!stateResponsive) {
                queueCmd(PLAY);
                return(undefined);
            } else {
                execQueuedCmds();
            }
            if ((_ns == null) || (_ns == undefined)) {
                _createStream();
                _video.attachVideo(_ns);
                attachAudio(_ns);
            }
            switch (_state) {
                case BUFFERING : 
                    if (_ncMgr.isRTMP()) {
                        _play(0);
                        if (_atEnd) {
                            _atEnd = false;
                            _currentPos = 0;
                            setState(REWINDING);
                        } else if (_currentPos > 0) {
                            _seek(_currentPos);
                            _currentPos = 0;
                        }
                    }
                case PLAYING : 
                    return(undefined);
                case STOPPED : 
                    if (_ncMgr.isRTMP()) {
                        if (_isLive) {
                            _play(-1);
                            setState(BUFFERING);
                        } else {
                            _play(0);
                            if (_atEnd) {
                                _atEnd = false;
                                _currentPos = 0;
                                _state = BUFFERING;
                                setState(REWINDING);
                            } else if (_currentPos > 0) {
                                _seek(_currentPos);
                                _currentPos = 0;
                                setState(BUFFERING);
                            } else {
                                setState(BUFFERING);
                            }
                        }
                    } else {
                        _pause(false);
                        if (_atEnd) {
                            _atEnd = false;
                            _seek(0);
                            _state = BUFFERING;
                            setState(REWINDING);
                        } else if (_bufferState == BUFFER_EMPTY) {
                            setState(BUFFERING);
                        } else {
                            setState(PLAYING);
                        }
                    }
                    break;
                case PAUSED : 
                    _pause(false);
                    if (!_ncMgr.isRTMP()) {
                        if (_bufferState == BUFFER_EMPTY) {
                            setState(BUFFERING);
                        } else {
                            setState(PLAYING);
                        }
                    } else {
                        setState(BUFFERING);
                    }
                    break;
            }
        }
        function load(_arg2, _arg3, _arg4) {
            if ((_arg2 == null) || (_arg2 == undefined)) {
                throw new Error("null url sent to VideoPlayer.load");
            }
            if (_state == EXEC_QUEUED_CMD) {
                _state = _cachedState;
            } else if (!stateResponsive) {
                queueCmd(LOAD, _arg2, _arg3, _arg4);
                return(undefined);
            } else {
                execQueuedCmds();
            }
            _autoPlay = false;
            _load(_arg2, _arg3, _arg4);
        }
        function _load(_arg5, _arg3, _arg4) {
            _prevVideoWidth = videoWidth;
            if (_prevVideoWidth == undefined) {
                _prevVideoWidth = _video.width;
                if (_prevVideoWidth == undefined) {
                    _prevVideoWidth = 0;
                }
            }
            _prevVideoHeight = videoHeight;
            if (_prevVideoHeight == undefined) {
                _prevVideoHeight = _video.height;
                if (_prevVideoHeight == undefined) {
                    _prevVideoHeight = 0;
                }
            }
            _autoResizeDone = false;
            _cachedPlayheadTime = 0;
            _bufferState = BUFFER_EMPTY;
            _metadata = null;
            _startingPlay = false;
            _invalidSeekTime = false;
            _invalidSeekRecovery = false;
            _isLive = ((_arg3 == undefined) ? false : (_arg3));
            _contentPath = _arg5;
            _currentPos = 0;
            _streamLength = _arg4;
            _atEnd = false;
            _videoWidth = undefined;
            _videoHeight = undefined;
            _readyDispatched = false;
            _lastUpdateTime = -1;
            _sawSeekNotify = false;
            clearInterval(_updateTimeIntervalID);
            _updateTimeIntervalID = 0;
            clearInterval(_updateProgressIntervalID);
            _updateProgressIntervalID = 0;
            clearInterval(_idleTimeoutIntervalID);
            _idleTimeoutIntervalID = 0;
            clearInterval(_autoResizeIntervalID);
            _autoResizeIntervalID = 0;
            clearInterval(_rtmpDoStopAtEndIntervalID);
            _rtmpDoStopAtEndIntervalID = 0;
            clearInterval(_rtmpDoSeekIntervalID);
            _rtmpDoSeekIntervalID = 0;
            clearInterval(_httpDoSeekIntervalID);
            _httpDoSeekIntervalID = 0;
            clearInterval(_finishAutoResizeIntervalID);
            _finishAutoResizeIntervalID = 0;
            clearInterval(_delayedBufferingIntervalID);
            _delayedBufferingIntervalID = 0;
            closeNS(false);
            if ((_ncMgr == null) || (_ncMgr == undefined)) {
                createINCManager();
            }
            var _local2 = _ncMgr.connectToURL(_contentPath);
            setState(LOADING);
            _cachedState = LOADING;
            if (_local2) {
                _createStream();
                _setUpStream();
            }
            if (!_ncMgr.isRTMP()) {
                clearInterval(_updateProgressIntervalID);
                _updateProgressIntervalID = setInterval(this, "doUpdateProgress", _updateProgressInterval);
            }
        }
        function pause() {
            if (!isXnOK()) {
                if (((((_state == CONNECTION_ERROR) || (_ncMgr == null)) || (_ncMgr == undefined)) || (_ncMgr.getNetConnection() == null)) || (_ncMgr.getNetConnection() == undefined)) {
                    throw new mx.video.VideoError(mx.video.VideoError.NO_CONNECTION);
                } else {
                    return(undefined);
                }
            } else if (_state == EXEC_QUEUED_CMD) {
                _state = _cachedState;
            } else if (!stateResponsive) {
                queueCmd(PAUSE);
                return(undefined);
            } else {
                execQueuedCmds();
            }
            if ((((_state == PAUSED) || (_state == STOPPED)) || (_ns == null)) || (_ns == undefined)) {
                return(undefined);
            }
            _pause(true);
            setState(PAUSED);
        }
        function stop() {
            if (!isXnOK()) {
                if (((((_state == CONNECTION_ERROR) || (_ncMgr == null)) || (_ncMgr == undefined)) || (_ncMgr.getNetConnection() == null)) || (_ncMgr.getNetConnection() == undefined)) {
                    throw new mx.video.VideoError(mx.video.VideoError.NO_CONNECTION);
                } else {
                    return(undefined);
                }
            } else if (_state == EXEC_QUEUED_CMD) {
                _state = _cachedState;
            } else if (!stateResponsive) {
                queueCmd(STOP);
                return(undefined);
            } else {
                execQueuedCmds();
            }
            if (((_state == STOPPED) || (_ns == null)) || (_ns == undefined)) {
                return(undefined);
            }
            if (_ncMgr.isRTMP()) {
                if (_autoRewind && (!_isLive)) {
                    _currentPos = 0;
                    _play(0, 0);
                    _state = STOPPED;
                    setState(REWINDING);
                } else {
                    closeNS(true);
                    setState(STOPPED);
                }
            } else {
                _pause(true);
                if (_autoRewind) {
                    _seek(0);
                    _state = STOPPED;
                    setState(REWINDING);
                } else {
                    setState(STOPPED);
                }
            }
        }
        function seek(_arg2) {
            if (_invalidSeekTime) {
                return(undefined);
            }
            if (isNaN(_arg2) || (_arg2 < 0)) {
                throw new mx.video.VideoError(mx.video.VideoError.INVALID_SEEK);
            }
            if (!isXnOK()) {
                if (((((_state == CONNECTION_ERROR) || (_ncMgr == null)) || (_ncMgr == undefined)) || (_ncMgr.getNetConnection() == null)) || (_ncMgr.getNetConnection() == undefined)) {
                    throw new mx.video.VideoError(mx.video.VideoError.NO_CONNECTION);
                } else {
                    flushQueuedCmds();
                    queueCmd(SEEK, null, false, _arg2);
                    setState(LOADING);
                    _cachedState = LOADING;
                    _ncMgr.reconnect();
                    return(undefined);
                }
            } else if (_state == EXEC_QUEUED_CMD) {
                _state = _cachedState;
            } else if (!stateResponsive) {
                queueCmd(SEEK, null, false, _arg2);
                return(undefined);
            } else {
                execQueuedCmds();
            }
            if ((_ns == null) || (_ns == undefined)) {
                _createStream();
                _video.attachVideo(_ns);
                attachAudio(_ns);
            }
            if (_atEnd && (_arg2 < playheadTime)) {
                _atEnd = false;
            }
            switch (_state) {
                case PLAYING : 
                    _state = BUFFERING;
                case BUFFERING : 
                case PAUSED : 
                    _seek(_arg2);
                    setState(SEEKING);
                    break;
                case STOPPED : 
                    if (_ncMgr.isRTMP()) {
                        _play(0);
                        _pause(true);
                    }
                    _seek(_arg2);
                    _state = PAUSED;
                    setState(SEEKING);
                    break;
            }
        }
        function close() {
            closeNS(true);
            if (((_ncMgr != null) && (_ncMgr != undefined)) && (_ncMgr.isRTMP())) {
                _ncMgr.close();
            }
            setState(DISCONNECTED);
            dispatchEvent({type:"close", state:_state, playheadTime:playheadTime});
        }
        function get x() {
            return(_x);
        }
        function set x(_arg2) {
            _x = _arg2;
            //return(x);
        }
        function get y() {
            return(_y);
        }
        function set y(_arg2) {
            _y = _arg2;
            //return(y);
        }
        function get scaleX() {
            return(_video._xscale);
        }
        function set scaleX(_arg2) {
            setScale(_arg2, scaleY);
            //return(scaleX);
        }
        function get scaleY() {
            return(_video._yscale);
        }
        function set scaleY(_arg2) {
            setScale(scaleX, _arg2);
            //return(scaleY);
        }
        function get width() {
            return(_video._width);
        }
        function set width(_arg2) {
            setSize(_arg2, _video._height);
            //return(width);
        }
        function get height() {
            return(_video._height);
        }
        function set height(_arg2) {
            setSize(_video._width, _arg2);
            //return(height);
        }
        function get videoWidth() {
            if (_readyDispatched) {
                _videoWidth = _video.width;
            }
            return(_videoWidth);
        }
        function get videoHeight() {
            if (_readyDispatched) {
                _videoHeight = _video.height;
            }
            return(_videoHeight);
        }
        function get visible() {
            if (!_hiddenForResize) {
                __visible = _visible;
            }
            return(__visible);
        }
        function set visible(_arg2) {
            __visible = _arg2;
            if (!_hiddenForResize) {
                _visible = __visible;
            }
            //return(visible);
        }
        function get autoSize() {
            return(_autoSize);
        }
        function set autoSize(_arg2) {
            if (_autoSize != _arg2) {
                _autoSize = _arg2;
                if (_autoSize) {
                    startAutoResize();
                }
            }
            //return(autoSize);
        }
        function get maintainAspectRatio() {
            return(_aspectRatio);
        }
        function set maintainAspectRatio(_arg2) {
            if (_aspectRatio != _arg2) {
                _aspectRatio = _arg2;
                if (_aspectRatio && (!_autoSize)) {
                    startAutoResize();
                }
            }
            //return(maintainAspectRatio);
        }
        function get autoRewind() {
            return(_autoRewind);
        }
        function set autoRewind(_arg2) {
            _autoRewind = _arg2;
            //return(autoRewind);
        }
        function get playheadTime() {
            var _local2 = (((_ns == null) || (_ns == undefined)) ? (_currentPos) : (_ns.time));
            if (_metadata.audiodelay != undefined) {
                _local2 = _local2 - _metadata.audiodelay;
                if (_local2 < 0) {
                    _local2 = 0;
                }
            }
            return(_local2);
        }
        function set playheadTime(_arg2) {
            this.seek(_arg2);
            //return(playheadTime);
        }
        function get url() {
            return(_contentPath);
        }
        function get volume() {
            return(_volume);
        }
        function set volume(_arg2) {
            _volume = _arg2;
            if (!_hiddenForResize) {
                _sound.setVolume(_volume);
            }
            //return(volume);
        }
        function get transform() {
            return(_sound.getTransform());
        }
        function set transform(_arg2) {
            _sound.setTransform(_arg2);
            //return(transform);
        }
        function get isRTMP() {
            if ((_ncMgr == null) || (_ncMgr == undefined)) {
                return(undefined);
            }
            return(_ncMgr.isRTMP());
        }
        function get isLive() {
            return(_isLive);
        }
        function get state() {
            return(_state);
        }
        function get stateResponsive() {
            switch (_state) {
                case DISCONNECTED : 
                case STOPPED : 
                case PLAYING : 
                case PAUSED : 
                case BUFFERING : 
                    return(true);
            }
            return(false);
        }
        function get bytesLoaded() {
            if (((_ns == null) || (_ns == undefined)) || (_ncMgr.isRTMP())) {
                return(-1);
            }
            return(_ns.bytesLoaded);
        }
        function get bytesTotal() {
            if (((_ns == null) || (_ns == undefined)) || (_ncMgr.isRTMP())) {
                return(-1);
            }
            return(_ns.bytesTotal);
        }
        function get totalTime() {
            return(_streamLength);
        }
        function get bufferTime() {
            return(_bufferTime);
        }
        function set bufferTime(_arg2) {
            _bufferTime = _arg2;
            if ((_ns != null) && (_ns != undefined)) {
                _ns.setBufferTime(_bufferTime);
            }
            //return(bufferTime);
        }
        function get idleTimeout() {
            return(_idleTimeoutInterval);
        }
        function set idleTimeout(_arg2) {
            _idleTimeoutInterval = _arg2;
            if (_idleTimeoutIntervalID > 0) {
                clearInterval(_idleTimeoutIntervalID);
                _idleTimeoutIntervalID = setInterval(this, "doIdleTimeout", _idleTimeoutInterval);
            }
            //return(idleTimeout);
        }
        function get playheadUpdateInterval() {
            return(_updateTimeInterval);
        }
        function set playheadUpdateInterval(_arg2) {
            _updateTimeInterval = _arg2;
            if (_updateTimeIntervalID > 0) {
                clearInterval(_updateTimeIntervalID);
                _updateTimeIntervalID = setInterval(this, "doUpdateTime", _updateTimeInterval);
            }
            //return(playheadUpdateInterval);
        }
        function get progressInterval() {
            return(_updateProgressInterval);
        }
        function set progressInterval(_arg2) {
            _updateProgressInterval = _arg2;
            if (_updateProgressIntervalID > 0) {
                clearInterval(_updateProgressIntervalID);
                _updateProgressIntervalID = setInterval(this, "doUpdateProgress", _updateProgressInterval);
            }
            //return(progressInterval);
        }
        function get ncMgr() {
            if ((_ncMgr == null) || (_ncMgr == undefined)) {
                createINCManager();
            }
            return(_ncMgr);
        }
        function get metadata() {
            return(_metadata);
        }
        function doUpdateTime() {
            var _local2 = playheadTime;
            switch (_state) {
                case STOPPED : 
                case PAUSED : 
                case DISCONNECTED : 
                case CONNECTION_ERROR : 
                    clearInterval(_updateTimeIntervalID);
                    _updateTimeIntervalID = 0;
                    break;
            }
            if (_lastUpdateTime != _local2) {
                dispatchEvent({type:"playheadUpdate", state:_state, playheadTime:_local2});
                _lastUpdateTime = _local2;
            }
        }
        function doUpdateProgress() {
            if ((_ns == null) || (_ns == undefined)) {
                return(undefined);
            }
            if ((_ns.bytesTotal >= 0) && (_ns.bytesTotal >= 0)) {
                dispatchEvent({type:"progress", bytesLoaded:_ns.bytesLoaded, bytesTotal:_ns.bytesTotal});
            }
            if (((_state == DISCONNECTED) || (_state == CONNECTION_ERROR)) || (_ns.bytesLoaded == _ns.bytesTotal)) {
                clearInterval(_updateProgressIntervalID);
                _updateProgressIntervalID = 0;
            }
        }
        function rtmpOnStatus(_arg2) {
            if (_state == CONNECTION_ERROR) {
                return(undefined);
            }
            switch (_arg2.code) {
                case "NetStream.Play.Stop" : 
                    if (_startingPlay) {
                        return(undefined);
                    }
                    switch (_state) {
                        case RESIZING : 
                            if (_hiddenForResize) {
                                finishAutoResize();
                            }
                            break;
                        case LOADING : 
                        case STOPPED : 
                        case PAUSED : 
                            break;
                        default : 
                            if ((_bufferState == BUFFER_EMPTY) || (_bufferTime <= 0.1)) {
                                _cachedPlayheadTime = playheadTime;
                                clearInterval(_rtmpDoStopAtEndIntervalID);
                                _rtmpDoStopAtEndIntervalID = setInterval(this, "rtmpDoStopAtEnd", RTMP_DO_STOP_AT_END_INTERVAL);
                            } else if (_bufferState == BUFFER_FULL) {
                                _bufferState = BUFFER_FULL_SAW_PLAY_STOP;
                            }
                            break;
                    }
                    break;
                case "NetStream.Buffer.Empty" : 
                    switch (_bufferState) {
                        case BUFFER_FULL_SAW_PLAY_STOP : 
                            rtmpDoStopAtEnd(true);
                            break;
                        case BUFFER_FULL : 
                            if (_state == PLAYING) {
                                setState(BUFFERING);
                            }
                            break;
                        default : 
                            break;
                    }
                    _bufferState = BUFFER_EMPTY;
                    break;
                case "NetStream.Buffer.Flush" : 
                case "NetStream.Buffer.Full" : 
                    if (_sawSeekNotify && (_state == SEEKING)) {
                        _bufferState = BUFFER_EMPTY;
                        setStateFromCachedState();
                        doUpdateTime();
                    }
                    switch (_bufferState) {
                        case BUFFER_EMPTY : 
                            if (!_hiddenForResize) {
                                if (((_state == LOADING) && (_cachedState == PLAYING)) || (_state == BUFFERING)) {
                                    setState(PLAYING);
                                } else if (_cachedState == BUFFERING) {
                                    _cachedState = PLAYING;
                                }
                            }
                            _bufferState = BUFFER_FULL;
                            break;
                        default : 
                            break;
                    }
                    break;
                case "NetStream.Pause.Notify" : 
                    if ((_state == RESIZING) && (_hiddenForResize)) {
                        finishAutoResize();
                    }
                    break;
                case "NetStream.Play.Start" : 
                    clearInterval(_rtmpDoStopAtEndIntervalID);
                    _rtmpDoStopAtEndIntervalID = 0;
                    _bufferState = BUFFER_EMPTY;
                    if (_startingPlay) {
                        _startingPlay = false;
                        _cachedPlayheadTime = playheadTime;
                    } else if (_state == PLAYING) {
                        setState(BUFFERING);
                    }
                    break;
                case "NetStream.Play.Reset" : 
                    clearInterval(_rtmpDoStopAtEndIntervalID);
                    _rtmpDoStopAtEndIntervalID = 0;
                    if (_state == REWINDING) {
                        clearInterval(_rtmpDoSeekIntervalID);
                        _rtmpDoSeekIntervalID = 0;
                        if ((playheadTime == 0) || (playheadTime < _cachedPlayheadTime)) {
                            setStateFromCachedState();
                        } else {
                            _cachedPlayheadTime = playheadTime;
                            _rtmpDoSeekIntervalID = setInterval(this, "rtmpDoSeek", RTMP_DO_SEEK_INTERVAL);
                        }
                    }
                    break;
                case "NetStream.Seek.Notify" : 
                    if (playheadTime != _cachedPlayheadTime) {
                        setStateFromCachedState();
                        doUpdateTime();
                    } else {
                        _sawSeekNotify = true;
                        if (_rtmpDoSeekIntervalID == 0) {
                            _rtmpDoSeekIntervalID = setInterval(this, "rtmpDoSeek", RTMP_DO_SEEK_INTERVAL);
                        }
                    }
                    break;
                case "Netstream.Play.UnpublishNotify" : 
                    break;
                case "Netstream.Play.PublishNotify" : 
                    break;
                case "NetStream.Play.StreamNotFound" : 
                    if (!_ncMgr.connectAgain()) {
                        setState(CONNECTION_ERROR);
                    }
                    break;
                case "NetStream.Play.Failed" : 
                case "NetStream.Failed" : 
                    setState(CONNECTION_ERROR);
                    break;
            }
        }
        function httpOnStatus(_arg2) {
            switch (_arg2.code) {
                case "NetStream.Play.Stop" : 
                    clearInterval(_delayedBufferingIntervalID);
                    _delayedBufferingIntervalID = 0;
                    if (_invalidSeekTime) {
                        _invalidSeekTime = false;
                        _invalidSeekRecovery = true;
                        setState(_cachedState);
                        this.seek(playheadTime);
                    } else {
                        switch (_state) {
                            case PLAYING : 
                            case BUFFERING : 
                            case SEEKING : 
                                httpDoStopAtEnd();
                                break;
                        }
                    }
                    break;
                case "NetStream.Seek.InvalidTime" : 
                    if (_invalidSeekRecovery) {
                        _invalidSeekTime = false;
                        _invalidSeekRecovery = false;
                        setState(_cachedState);
                        this.seek(0);
                    } else {
                        _invalidSeekTime = true;
                    }
                    break;
                case "NetStream.Buffer.Empty" : 
                    _bufferState = BUFFER_EMPTY;
                    if (_state == PLAYING) {
                        clearInterval(_delayedBufferingIntervalID);
                        _delayedBufferingIntervalID = setInterval(this, "doDelayedBuffering", _delayedBufferingInterval);
                    }
                    break;
                case "NetStream.Buffer.Full" : 
                case "NetStream.Buffer.Flush" : 
                    clearInterval(_delayedBufferingIntervalID);
                    _delayedBufferingIntervalID = 0;
                    _bufferState = BUFFER_FULL;
                    if (!_hiddenForResize) {
                        if (((_state == LOADING) && (_cachedState == PLAYING)) || (_state == BUFFERING)) {
                            setState(PLAYING);
                        } else if (_cachedState == BUFFERING) {
                            _cachedState = PLAYING;
                        }
                    }
                    break;
                case "NetStream.Seek.Notify" : 
                    _invalidSeekRecovery = false;
                    switch (_state) {
                        case SEEKING : 
                        case REWINDING : 
                            if (_httpDoSeekIntervalID == 0) {
                                _httpDoSeekCount = 0;
                                _httpDoSeekIntervalID = setInterval(this, "httpDoSeek", HTTP_DO_SEEK_INTERVAL);
                            }
                            break;
                    }
                    break;
                case "NetStream.Play.StreamNotFound" : 
                    setState(CONNECTION_ERROR);
                    break;
            }
        }
        function ncConnected() {
            if ((((_ncMgr == null) || (_ncMgr == undefined)) || (_ncMgr.getNetConnection() == null)) || (_ncMgr.getNetConnection() == undefined)) {
                setState(CONNECTION_ERROR);
            } else {
                _createStream();
                _setUpStream();
            }
        }
        function ncReconnected() {
            if ((((_ncMgr == null) || (_ncMgr == undefined)) || (_ncMgr.getNetConnection() == null)) || (_ncMgr.getNetConnection() == undefined)) {
                setState(CONNECTION_ERROR);
            } else {
                _ns = null;
                _state = STOPPED;
                execQueuedCmds();
            }
        }
        function onMetaData(_arg2) {
            if (_metadata != null) {
                return(undefined);
            }
            _metadata = _arg2;
            if (((_streamLength == undefined) || (_streamLength == null)) || (_streamLength <= 0)) {
                _streamLength = _arg2.duration;
            }
            if (isNaN(_videoWidth) || (_videoWidth <= 0)) {
                _videoWidth = _arg2.width;
            }
            if (isNaN(_videoHeight) || (_videoHeight <= 0)) {
                _videoHeight = _arg2.height;
            }
            dispatchEvent({type:"metadataReceived", info:_arg2});
        }
        function onCuePoint(_arg2) {
            if ((!_hiddenForResize) || ((!isNaN(_hiddenRewindPlayheadTime)) && (playheadTime < _hiddenRewindPlayheadTime))) {
                dispatchEvent({type:"cuePoint", info:_arg2});
            }
        }
        function setState(_arg3) {
            if (_arg3 == _state) {
                return(undefined);
            }
            _hiddenRewindPlayheadTime = undefined;
            _cachedState = _state;
            _cachedPlayheadTime = playheadTime;
            _state = _arg3;
            var _local2 = _state;
            dispatchEvent({type:"stateChange", state:_local2, playheadTime:playheadTime});
            if (!_readyDispatched) {
                switch (_local2) {
                    case STOPPED : 
                    case PLAYING : 
                    case PAUSED : 
                    case BUFFERING : 
                        _readyDispatched = true;
                        dispatchEvent({type:"ready", state:_local2, playheadTime:playheadTime});
                        break;
                }
            }
            switch (_cachedState) {
                case REWINDING : 
                    dispatchEvent({type:"rewind", state:_local2, playheadTime:playheadTime});
                    if (_ncMgr.isRTMP() && (_local2 == STOPPED)) {
                        closeNS();
                    }
                    break;
                default : 
            }
            switch (_local2) {
                case STOPPED : 
                case PAUSED : 
                    if (_ncMgr.isRTMP() && (_idleTimeoutIntervalID == 0)) {
                        _idleTimeoutIntervalID = setInterval(this, "doIdleTimeout", _idleTimeoutInterval);
                    }
                    break;
                case SEEKING : 
                case REWINDING : 
                    _bufferState = BUFFER_EMPTY;
                case PLAYING : 
                case BUFFERING : 
                    if (_updateTimeIntervalID == 0) {
                        _updateTimeIntervalID = setInterval(this, "doUpdateTime", _updateTimeInterval);
                    }
                case LOADING : 
                case RESIZING : 
                    clearInterval(_idleTimeoutIntervalID);
                    _idleTimeoutIntervalID = 0;
                    break;
            }
            execQueuedCmds();
        }
        function setStateFromCachedState() {
            switch (_cachedState) {
                case PLAYING : 
                case PAUSED : 
                    setState(_cachedState);
                    break;
                case BUFFERING : 
                    if (_bufferState == BUFFER_EMPTY) {
                        setState(BUFFERING);
                    } else {
                        setState(_cachedState);
                    }
                    break;
                default : 
                    setState(STOPPED);
                    break;
            }
        }
        function createINCManager() {
            if ((ncMgrClassName == null) || (ncMgrClassName == undefined)) {
                ncMgrClassName = DEFAULT_INCMANAGER;
            }
            var ncMgrConstructor = eval (this.ncMgrClassName);
            _ncMgr = new ncMgrConstructor();
            _ncMgr.setVideoPlayer(this);
        }
        function rtmpDoStopAtEnd(_arg4) {
            if (_rtmpDoStopAtEndIntervalID > 0) {
                switch (_state) {
                    case DISCONNECTED : 
                    case CONNECTION_ERROR : 
                        clearInterval(_rtmpDoStopAtEndIntervalID);
                        _rtmpDoStopAtEndIntervalID = 0;
                        return(undefined);
                }
                if (_arg4 || (_cachedPlayheadTime == playheadTime)) {
                    clearInterval(_rtmpDoStopAtEndIntervalID);
                    _rtmpDoStopAtEndIntervalID = 0;
                } else {
                    _cachedPlayheadTime = playheadTime;
                    return(undefined);
                }
            }
            _bufferState = BUFFER_EMPTY;
            _atEnd = true;
            setState(STOPPED);
            if (_state != STOPPED) {
                return(undefined);
            }
            doUpdateTime();
            if (_state != STOPPED) {
                return(undefined);
            }
            dispatchEvent({type:"complete", state:_state, playheadTime:playheadTime});
            if (_state != STOPPED) {
                return(undefined);
            }
            if ((_autoRewind && (!_isLive)) && (playheadTime != 0)) {
                _atEnd = false;
                _currentPos = 0;
                _play(0, 0);
                setState(REWINDING);
            } else {
                closeNS();
            }
        }
        function rtmpDoSeek() {
            if ((_state != REWINDING) && (_state != SEEKING)) {
                clearInterval(_rtmpDoSeekIntervalID);
                _rtmpDoSeekIntervalID = 0;
                _sawSeekNotify = false;
            } else if (playheadTime != _cachedPlayheadTime) {
                clearInterval(_rtmpDoSeekIntervalID);
                _rtmpDoSeekIntervalID = 0;
                _sawSeekNotify = false;
                setStateFromCachedState();
                doUpdateTime();
            }
        }
        function httpDoStopAtEnd() {
            _atEnd = true;
            if (((_streamLength == undefined) || (_streamLength == null)) || (_streamLength <= 0)) {
                _streamLength = _ns.time;
            }
            _pause(true);
            setState(STOPPED);
            if (_state != STOPPED) {
                return(undefined);
            }
            doUpdateTime();
            if (_state != STOPPED) {
                return(undefined);
            }
            dispatchEvent({type:"complete", state:_state, playheadTime:playheadTime});
            if (_state != STOPPED) {
                return(undefined);
            }
            if (_autoRewind) {
                _atEnd = false;
                _pause(true);
                _seek(0);
                setState(REWINDING);
            }
        }
        function httpDoSeek() {
            var _local2 = (_state == REWINDING) || (_state == SEEKING);
            if ((_local2 && (_httpDoSeekCount < HTTP_DO_SEEK_MAX_COUNT)) && ((_cachedPlayheadTime == playheadTime) || (_invalidSeekTime))) {
                _httpDoSeekCount++;
                return(undefined);
            }
            _httpDoSeekCount = 0;
            clearInterval(_httpDoSeekIntervalID);
            _httpDoSeekIntervalID = 0;
            if (!_local2) {
                return(undefined);
            }
            setStateFromCachedState();
            if (_invalidSeekTime) {
                _invalidSeekTime = false;
                _invalidSeekRecovery = true;
                this.seek(playheadTime);
            } else {
                doUpdateTime();
            }
        }
        function closeNS(_arg2) {
            if ((_ns != null) && (_ns != undefined)) {
                if (_arg2) {
                    clearInterval(_updateTimeIntervalID);
                    _updateTimeIntervalID = 0;
                    doUpdateTime();
                    _currentPos = _ns.time;
                }
                delete _ns.onStatus;
                _ns.onStatus = null;
                _ns.close();
                _ns = null;
            }
        }
        function doDelayedBuffering() {
            switch (_state) {
                case LOADING : 
                case RESIZING : 
                    break;
                case PLAYING : 
                    clearInterval(_delayedBufferingIntervalID);
                    _delayedBufferingIntervalID = 0;
                    setState(BUFFERING);
                    break;
                default : 
                    clearInterval(_delayedBufferingIntervalID);
                    _delayedBufferingIntervalID = 0;
                    break;
            }
        }
        function _pause(_arg2) {
            _ns.pause(_arg2);
        }
        function _play() {
            _startingPlay = true;
            switch (arguments.length) {
                case 0 : 
                    _ns.play(_ncMgr.getStreamName(), (_isLive ? -1 : 0), -1);
                    break;
                case 1 : 
                    _ns.play(_ncMgr.getStreamName(), (_isLive ? -1 : (arguments[0])), -1);
                    break;
                case 2 : 
                    _ns.play(_ncMgr.getStreamName(), (_isLive ? -1 : (arguments[0])), arguments[1]);
                    break;
                default : 
                    throw new Error("bad args to _play");
            }
        }
        function _seek(_arg2) {
            if ((_metadata.audiodelay != undefined) && ((_arg2 + _metadata.audiodelay) < _streamLength)) {
                _arg2 = _arg2 + _metadata.audiodelay;
            }
            _ns.seek(_arg2);
            _invalidSeekTime = false;
            _bufferState = BUFFER_EMPTY;
            _sawSeekNotify = false;
        }
        function isXnOK() {
            if (_state == LOADING) {
                return(true);
            }
            if (_state == CONNECTION_ERROR) {
                return(false);
            }
            if (_state != DISCONNECTED) {
                if (((((_ncMgr == null) || (_ncMgr == undefined)) || (_ncMgr.getNetConnection() == null)) || (_ncMgr.getNetConnection() == undefined)) || (!_ncMgr.getNetConnection().isConnected)) {
                    setState(DISCONNECTED);
                    return(false);
                }
                return(true);
            }
            return(false);
        }
        function startAutoResize() {
            switch (_state) {
                case DISCONNECTED : 
                case CONNECTION_ERROR : 
                    return(undefined);
            }
            _autoResizeDone = false;
            if ((stateResponsive && (_videoWidth != undefined)) && (_videoHeight != undefined)) {
                doAutoResize();
            } else {
                clearInterval(_autoResizeIntervalID);
                _autoResizeIntervalID = setInterval(this, "doAutoResize", AUTO_RESIZE_INTERVAL);
            }
        }
        function doAutoResize() {
            if (_autoResizeIntervalID > 0) {
                switch (_state) {
                    case RESIZING : 
                    case LOADING : 
                        break;
                    case DISCONNECTED : 
                    case CONNECTION_ERROR : 
                        clearInterval(_autoResizeIntervalID);
                        _autoResizeIntervalID = 0;
                        return(undefined);
                    default : 
                        if (stateResponsive) { 
                            break;
                        }
                        return(undefined);
                }
                if ((((_video.width != _prevVideoWidth) || (_video.height != _prevVideoHeight)) || (_bufferState >= BUFFER_FULL)) || (_ns.time > AUTO_RESIZE_PLAYHEAD_TIMEOUT)) {
                    if ((_hiddenForResize && (_metadata == null)) && (_hiddenForResizeMetadataDelay < AUTO_RESIZE_METADATA_DELAY_MAX)) {
                        _hiddenForResizeMetadataDelay++;
                        return(undefined);
                    }
                    _videoWidth = _video.width;
                    _videoHeight = _video.height;
                    clearInterval(_autoResizeIntervalID);
                    _autoResizeIntervalID = 0;
                } else {
                    return(undefined);
                }
            }
            if (((!_autoSize) && (!_aspectRatio)) || (_autoResizeDone)) {
                setState(_cachedState);
                return(undefined);
            }
            _autoResizeDone = true;
            if (_autoSize) {
                _video._width = _videoWidth;
                _video._height = _videoHeight;
            } else if (_aspectRatio) {
                var _local3 = (_videoWidth * height) / _videoHeight;
                var _local2 = (_videoHeight * width) / _videoWidth;
                if (_local2 < height) {
                    _video._height = _local2;
                } else if (_local3 < width) {
                    _video._width = _local3;
                }
            }
            if (_hiddenForResize) {
                _hiddenRewindPlayheadTime = playheadTime;
                if (_state == LOADING) {
                    _cachedState = PLAYING;
                }
                if (!_ncMgr.isRTMP()) {
                    _pause(true);
                    _seek(0);
                    clearInterval(_finishAutoResizeIntervalID);
                    _finishAutoResizeIntervalID = setInterval(this, "finishAutoResize", FINISH_AUTO_RESIZE_INTERVAL);
                } else if (!_isLive) {
                    _currentPos = 0;
                    _play(0, 0);
                    setState(RESIZING);
                } else if (_autoPlay) {
                    clearInterval(_finishAutoResizeIntervalID);
                    _finishAutoResizeIntervalID = setInterval(this, "finishAutoResize", FINISH_AUTO_RESIZE_INTERVAL);
                } else {
                    finishAutoResize();
                }
            } else {
                dispatchEvent({type:"resize", x:_x, y:_y, width:_width, height:_height});
            }
        }
        function finishAutoResize() {
            clearInterval(_finishAutoResizeIntervalID);
            _finishAutoResizeIntervalID = 0;
            if (stateResponsive) {
                return(undefined);
            }
            _visible = __visible;
            _sound.setVolume(_volume);
            _hiddenForResize = false;
            dispatchEvent({type:"resize", x:_x, y:_y, width:_width, height:_height});
            if (_autoPlay) {
                if (_ncMgr.isRTMP()) {
                    if (!_isLive) {
                        _currentPos = 0;
                        _play(0);
                    }
                    if (_state == RESIZING) {
                        setState(LOADING);
                        _cachedState = PLAYING;
                    }
                } else {
                    _pause(false);
                    _cachedState = PLAYING;
                }
            } else {
                setState(STOPPED);
            }
        }
        function _createStream() {
            _ns = new NetStream(_ncMgr.getNetConnection());
            _ns.mc = this;
            if (_ncMgr.isRTMP()) {
                _ns.onStatus = function (_arg2) {
                    this.mc.rtmpOnStatus(_arg2);
                };
            } else {
                _ns.onStatus = function (_arg2) {
                    this.mc.httpOnStatus(_arg2);
                };
            }
            _ns.onMetaData = function (_arg2) {
                this.mc.onMetaData(_arg2);
            };
            _ns.onCuePoint = function (_arg2) {
                this.mc.onCuePoint(_arg2);
            };
            _ns.setBufferTime(_bufferTime);
        }
        function _setUpStream() {
            _video.attachVideo(_ns);
            attachAudio(_ns);
            if ((!isNaN(_ncMgr.getStreamLength())) && (_ncMgr.getStreamLength() >= 0)) {
                _streamLength = _ncMgr.getStreamLength();
            }
            if ((!isNaN(_ncMgr.getStreamWidth())) && (_ncMgr.getStreamWidth() >= 0)) {
                _videoWidth = _ncMgr.getStreamWidth();
            } else {
                _videoWidth = undefined;
            }
            if ((!isNaN(_ncMgr.getStreamHeight())) && (_ncMgr.getStreamHeight() >= 0)) {
                _videoHeight = _ncMgr.getStreamHeight();
            } else {
                _videoHeight = undefined;
            }
            if (((_autoSize || (_aspectRatio)) && (_videoWidth != undefined)) && (_videoHeight != undefined)) {
                _prevVideoWidth = undefined;
                _prevVideoHeight = undefined;
                doAutoResize();
            }
            if (((!_autoSize) && (!_aspectRatio)) || ((_videoWidth != undefined) && (_videoHeight != undefined))) {
                if (_autoPlay) {
                    if (!_ncMgr.isRTMP()) {
                        _cachedState = BUFFERING;
                        _play();
                    } else if (_isLive) {
                        _cachedState = BUFFERING;
                        _play(-1);
                    } else {
                        _cachedState = BUFFERING;
                        _play(0);
                    }
                } else {
                    _cachedState = STOPPED;
                    if (_ncMgr.isRTMP()) {
                        _play(0, 0);
                    } else {
                        _play();
                        _pause(true);
                        _seek(0);
                    }
                }
            } else {
                _hiddenForResize = true;
                _hiddenForResizeMetadataDelay = 0;
                __visible = _visible;
                _visible = false;
                _volume = _sound.getVolume();
                _sound.setVolume(0);
                _play(0);
                if (_currentPos > 0) {
                    _seek(_currentPos);
                    _currentPos = 0;
                }
            }
            clearInterval(_autoResizeIntervalID);
            _autoResizeIntervalID = setInterval(this, "doAutoResize", AUTO_RESIZE_INTERVAL);
        }
        function doIdleTimeout() {
            clearInterval(_idleTimeoutIntervalID);
            _idleTimeoutIntervalID = 0;
            this.close();
        }
        function flushQueuedCmds() {
            while (_cmdQueue.length > 0) {
                _cmdQueue.pop();
            }
        }
        function execQueuedCmds() {
            while (((_cmdQueue.length > 0) && (stateResponsive || (_state == CONNECTION_ERROR))) && (((_cmdQueue[0].url != null) && (_cmdQueue[0].url != undefined)) || ((_state != DISCONNECTED) && (_state != CONNECTION_ERROR)))) {
                var _local2 = _cmdQueue.shift();
                _cachedState = _state;
                _state = EXEC_QUEUED_CMD;
                switch (_local2.type) {
                    case PLAY : 
                        this.play(_local2.url, _local2.isLive, _local2.time);
                        break;
                    case LOAD : 
                        this.load(_local2.url, _local2.isLive, _local2.time);
                        break;
                    case PAUSE : 
                        this.pause();
                        break;
                    case STOP : 
                        this.stop();
                        break;
                    case SEEK : 
                        this.seek(_local2.time);
                        break;
                }
            }
        }
        function queueCmd(_arg5, _arg4, _arg3, _arg2) {
            _cmdQueue.push({type:_arg5, url:_arg4, isLive:false, time:_arg2});
        }
        static var version = "1.0.0.103";
        static var DISCONNECTED = "disconnected";
        static var STOPPED = "stopped";
        static var PLAYING = "playing";
        static var PAUSED = "paused";
        static var BUFFERING = "buffering";
        static var LOADING = "loading";
        static var CONNECTION_ERROR = "connectionError";
        static var REWINDING = "rewinding";
        static var SEEKING = "seeking";
        static var RESIZING = "resizing";
        static var EXEC_QUEUED_CMD = "execQueuedCmd";
        static var BUFFER_EMPTY = "bufferEmpty";
        static var BUFFER_FULL = "bufferFull";
        static var BUFFER_FULL_SAW_PLAY_STOP = "bufferFullSawPlayStop";
        static var DEFAULT_INCMANAGER = "mx.video.NCManager";
        static var DEFAULT_UPDATE_TIME_INTERVAL = 250;
        static var DEFAULT_UPDATE_PROGRESS_INTERVAL = 250;
        static var DEFAULT_IDLE_TIMEOUT_INTERVAL = 300000;
        static var AUTO_RESIZE_INTERVAL = 100;
        static var AUTO_RESIZE_PLAYHEAD_TIMEOUT = 0.5;
        static var AUTO_RESIZE_METADATA_DELAY_MAX = 5;
        static var FINISH_AUTO_RESIZE_INTERVAL = 250;
        static var RTMP_DO_STOP_AT_END_INTERVAL = 500;
        static var RTMP_DO_SEEK_INTERVAL = 100;
        static var HTTP_DO_SEEK_INTERVAL = 250;
        static var HTTP_DO_SEEK_MAX_COUNT = 4;
        static var CLOSE_NS_INTERVAL = 0.25;
        static var HTTP_DELAYED_BUFFERING_INTERVAL = 100;
        static var PLAY = 0;
        static var LOAD = 1;
        static var PAUSE = 2;
        static var STOP = 3;
        static var SEEK = 4;
    }