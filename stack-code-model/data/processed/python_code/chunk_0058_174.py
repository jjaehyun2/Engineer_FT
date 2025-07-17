class mx.video.VideoPlayer extends MovieClip
{
    var _state, _cachedState, _bufferState, _sawPlayStop, _cachedPlayheadTime, _metadata, _startingPlay, _invalidSeekTime, _invalidSeekRecovery, _currentPos, _atEnd, _cmdQueue, _readyDispatched, _autoResizeDone, _lastUpdateTime, _sawSeekNotify, _updateTimeIntervalID, _updateTimeInterval, _updateProgressIntervalID, _updateProgressInterval, _idleTimeoutIntervalID, _idleTimeoutInterval, _autoResizeIntervalID, _rtmpDoStopAtEndIntervalID, _rtmpDoSeekIntervalID, _httpDoSeekIntervalID, _httpDoSeekCount, _finishAutoResizeIntervalID, _delayedBufferingIntervalID, _delayedBufferingInterval, _isLive, _autoSize, _aspectRatio, _autoPlay, _autoRewind, _bufferTime, _volume, _sound, __visible, _hiddenForResize, _hiddenForResizeMetadataDelay, _contentPath, _video, __get__stateResponsive, _ncMgr, _ns, attachAudio, _prevVideoWidth, _prevVideoHeight, _streamLength, _videoWidth, _videoHeight, __get__playheadTime, dispatchEvent, _x, __get__x, _y, __get__y, __get__scaleY, __get__scaleX, __get__width, __get__height, _visible, __get__visible, __get__autoSize, __get__maintainAspectRatio, __get__autoRewind, __get__volume, __get__transform, __get__bufferTime, __get__idleTimeout, __get__playheadUpdateInterval, __get__progressInterval, _hiddenRewindPlayheadTime, ncMgrClassName, _width, _height, mc, __set__autoRewind, __set__autoSize, __set__bufferTime, __get__bytesLoaded, __get__bytesTotal, __set__height, __set__idleTimeout, __get__isLive, __get__isRTMP, __set__maintainAspectRatio, __get__metadata, __get__ncMgr, __set__playheadTime, __set__playheadUpdateInterval, __set__progressInterval, __set__scaleX, __set__scaleY, __get__state, __get__totalTime, __set__transform, __get__url, __get__videoHeight, __get__videoWidth, __set__visible, __set__volume, __set__width, __set__x, __set__y;
    function VideoPlayer()
    {
        super();
        mx.events.EventDispatcher.initialize(this);
        _state = mx.video.VideoPlayer.DISCONNECTED;
        _cachedState = _state;
        _bufferState = mx.video.VideoPlayer.BUFFER_EMPTY;
        _sawPlayStop = false;
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
        _updateTimeInterval = mx.video.VideoPlayer.DEFAULT_UPDATE_TIME_INTERVAL;
        _updateProgressIntervalID = 0;
        _updateProgressInterval = mx.video.VideoPlayer.DEFAULT_UPDATE_PROGRESS_INTERVAL;
        _idleTimeoutIntervalID = 0;
        _idleTimeoutInterval = mx.video.VideoPlayer.DEFAULT_IDLE_TIMEOUT_INTERVAL;
        _autoResizeIntervalID = 0;
        _rtmpDoStopAtEndIntervalID = 0;
        _rtmpDoSeekIntervalID = 0;
        _httpDoSeekIntervalID = 0;
        _httpDoSeekCount = 0;
        _finishAutoResizeIntervalID = 0;
        _delayedBufferingIntervalID = 0;
        _delayedBufferingInterval = mx.video.VideoPlayer.HTTP_DELAYED_BUFFERING_INTERVAL;
        if (_isLive == undefined)
        {
            _isLive = false;
        } // end if
        if (_autoSize == undefined)
        {
            _autoSize = false;
        } // end if
        if (_aspectRatio == undefined)
        {
            _aspectRatio = true;
        } // end if
        if (_autoPlay == undefined)
        {
            _autoPlay = true;
        } // end if
        if (_autoRewind == undefined)
        {
            _autoRewind = true;
        } // end if
        if (_bufferTime == undefined)
        {
            _bufferTime = 1.000000E-001;
        } // end if
        if (_volume == undefined)
        {
            _volume = 100;
        } // end if
        _sound = new Sound(this);
        _sound.setVolume(_volume);
        __visible = true;
        _hiddenForResize = false;
        _hiddenForResizeMetadataDelay = 0;
        _contentPath = "";
    } // End of the function
    function setSize(w, h)
    {
        if (w == _video._width && h == _video._height || _autoSize)
        {
            return;
        } // end if
        _video._width = w;
        _video._height = h;
        if (_aspectRatio)
        {
            this.startAutoResize();
        } // end if
    } // End of the function
    function setScale(xs, ys)
    {
        if (xs == _video._xscale && ys == _video._yscale || _autoSize)
        {
            return;
        } // end if
        _video._xscale = xs;
        _video._yscale = ys;
        if (_aspectRatio)
        {
            this.startAutoResize();
        } // end if
    } // End of the function
    function play(url, isLive, totalTime)
    {
        if (url != null && url != undefined)
        {
            if (_state == mx.video.VideoPlayer.EXEC_QUEUED_CMD)
            {
                _state = _cachedState;
            }
            else if (!this.__get__stateResponsive())
            {
                this.queueCmd(mx.video.VideoPlayer.PLAY, url, isLive, totalTime);
                return;
            }
            else
            {
                this.execQueuedCmds();
            } // end else if
            _autoPlay = true;
            this._load(url, isLive, totalTime);
            return;
        } // end if
        if (!this.isXnOK())
        {
            if (_state == mx.video.VideoPlayer.CONNECTION_ERROR || _ncMgr == null || _ncMgr == undefined || _ncMgr.getNetConnection() == null || _ncMgr.getNetConnection() == undefined)
            {
                throw new mx.video.VideoError(mx.video.VideoError.NO_CONNECTION);
            }
            else
            {
                this.flushQueuedCmds();
                this.queueCmd(mx.video.VideoPlayer.PLAY);
                this.setState(mx.video.VideoPlayer.LOADING);
                _cachedState = mx.video.VideoPlayer.LOADING;
                _ncMgr.reconnect();
                return;
            } // end else if
        }
        else if (_state == mx.video.VideoPlayer.EXEC_QUEUED_CMD)
        {
            _state = _cachedState;
        }
        else if (!this.__get__stateResponsive())
        {
            this.queueCmd(mx.video.VideoPlayer.PLAY);
            return;
        }
        else
        {
            this.execQueuedCmds();
        } // end else if
        if (_ns == null || _ns == undefined)
        {
            this._createStream();
            _video.attachVideo(_ns);
            this.attachAudio(_ns);
        } // end if
        switch (_state)
        {
            case mx.video.VideoPlayer.BUFFERING:
            {
                if (_ncMgr.isRTMP())
                {
                    this._play(0);
                    if (_atEnd)
                    {
                        _atEnd = false;
                        _currentPos = 0;
                        this.setState(mx.video.VideoPlayer.REWINDING);
                    }
                    else if (_currentPos > 0)
                    {
                        this._seek(_currentPos);
                        _currentPos = 0;
                    } // end if
                } // end else if
            } 
            case mx.video.VideoPlayer.PLAYING:
            {
                return;
            } 
            case mx.video.VideoPlayer.STOPPED:
            {
                if (_ncMgr.isRTMP())
                {
                    if (_isLive)
                    {
                        this._play(-1);
                        this.setState(mx.video.VideoPlayer.BUFFERING);
                    }
                    else
                    {
                        this._play(0);
                        if (_atEnd)
                        {
                            _atEnd = false;
                            _currentPos = 0;
                            _state = mx.video.VideoPlayer.BUFFERING;
                            this.setState(mx.video.VideoPlayer.REWINDING);
                        }
                        else if (_currentPos > 0)
                        {
                            this._seek(_currentPos);
                            _currentPos = 0;
                            this.setState(mx.video.VideoPlayer.BUFFERING);
                        }
                        else
                        {
                            this.setState(mx.video.VideoPlayer.BUFFERING);
                        } // end else if
                    } // end else if
                }
                else
                {
                    this._pause(false);
                    if (_atEnd)
                    {
                        _atEnd = false;
                        this._seek(0);
                        _state = mx.video.VideoPlayer.BUFFERING;
                        this.setState(mx.video.VideoPlayer.REWINDING);
                    }
                    else if (_bufferState == mx.video.VideoPlayer.BUFFER_EMPTY)
                    {
                        this.setState(mx.video.VideoPlayer.BUFFERING);
                    }
                    else
                    {
                        this.setState(mx.video.VideoPlayer.PLAYING);
                    } // end else if
                } // end else if
                break;
            } 
            case mx.video.VideoPlayer.PAUSED:
            {
                this._pause(false);
                if (!_ncMgr.isRTMP())
                {
                    if (_bufferState == mx.video.VideoPlayer.BUFFER_EMPTY)
                    {
                        this.setState(mx.video.VideoPlayer.BUFFERING);
                    }
                    else
                    {
                        this.setState(mx.video.VideoPlayer.PLAYING);
                    } // end else if
                }
                else
                {
                    this.setState(mx.video.VideoPlayer.BUFFERING);
                } // end else if
                break;
            } 
        } // End of switch
    } // End of the function
    function load(url, isLive, totalTime)
    {
        if (url == null || url == undefined)
        {
            throw new Error("null url sent to VideoPlayer.load");
        } // end if
        if (_state == mx.video.VideoPlayer.EXEC_QUEUED_CMD)
        {
            _state = _cachedState;
        }
        else if (!this.__get__stateResponsive())
        {
            this.queueCmd(mx.video.VideoPlayer.LOAD, url, isLive, totalTime);
            return;
        }
        else
        {
            this.execQueuedCmds();
        } // end else if
        _autoPlay = false;
        this._load(url, isLive, totalTime);
    } // End of the function
    function _load(url, isLive, totalTime)
    {
        _prevVideoWidth = videoWidth;
        if (_prevVideoWidth == undefined)
        {
            _prevVideoWidth = _video.width;
            if (_prevVideoWidth == undefined)
            {
                _prevVideoWidth = 0;
            } // end if
        } // end if
        _prevVideoHeight = videoHeight;
        if (_prevVideoHeight == undefined)
        {
            _prevVideoHeight = _video.height;
            if (_prevVideoHeight == undefined)
            {
                _prevVideoHeight = 0;
            } // end if
        } // end if
        _autoResizeDone = false;
        _cachedPlayheadTime = 0;
        _bufferState = mx.video.VideoPlayer.BUFFER_EMPTY;
        _sawPlayStop = false;
        _metadata = null;
        _startingPlay = false;
        _invalidSeekTime = false;
        _invalidSeekRecovery = false;
        _isLive = isLive == undefined ? (false) : (isLive);
        _contentPath = url;
        _currentPos = 0;
        _streamLength = totalTime;
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
        this.closeNS(false);
        if (_ncMgr == null || _ncMgr == undefined)
        {
            this.createINCManager();
        } // end if
        var _loc2 = _ncMgr.connectToURL(_contentPath);
        this.setState(mx.video.VideoPlayer.LOADING);
        _cachedState = mx.video.VideoPlayer.LOADING;
        if (_loc2)
        {
            this._createStream();
            this._setUpStream();
        } // end if
        if (!_ncMgr.isRTMP())
        {
            clearInterval(_updateProgressIntervalID);
            _updateProgressIntervalID = setInterval(this, "doUpdateProgress", _updateProgressInterval);
        } // end if
    } // End of the function
    function pause()
    {
        if (!this.isXnOK())
        {
            if (_state == mx.video.VideoPlayer.CONNECTION_ERROR || _ncMgr == null || _ncMgr == undefined || _ncMgr.getNetConnection() == null || _ncMgr.getNetConnection() == undefined)
            {
                throw new mx.video.VideoError(mx.video.VideoError.NO_CONNECTION);
            }
            else
            {
                return;
            } // end else if
        }
        else if (_state == mx.video.VideoPlayer.EXEC_QUEUED_CMD)
        {
            _state = _cachedState;
        }
        else if (!this.__get__stateResponsive())
        {
            this.queueCmd(mx.video.VideoPlayer.PAUSE);
            return;
        }
        else
        {
            this.execQueuedCmds();
        } // end else if
        if (_state == mx.video.VideoPlayer.PAUSED || _state == mx.video.VideoPlayer.STOPPED || _ns == null || _ns == undefined)
        {
            return;
        } // end if
        this._pause(true);
        this.setState(mx.video.VideoPlayer.PAUSED);
    } // End of the function
    function stop()
    {
        if (!this.isXnOK())
        {
            if (_state == mx.video.VideoPlayer.CONNECTION_ERROR || _ncMgr == null || _ncMgr == undefined || _ncMgr.getNetConnection() == null || _ncMgr.getNetConnection() == undefined)
            {
                throw new mx.video.VideoError(mx.video.VideoError.NO_CONNECTION);
            }
            else
            {
                return;
            } // end else if
        }
        else if (_state == mx.video.VideoPlayer.EXEC_QUEUED_CMD)
        {
            _state = _cachedState;
        }
        else if (!this.__get__stateResponsive())
        {
            this.queueCmd(mx.video.VideoPlayer.STOP);
            return;
        }
        else
        {
            this.execQueuedCmds();
        } // end else if
        if (_state == mx.video.VideoPlayer.STOPPED || _ns == null || _ns == undefined)
        {
            return;
        } // end if
        if (_ncMgr.isRTMP())
        {
            if (_autoRewind && !_isLive)
            {
                _currentPos = 0;
                this._play(0, 0);
                _state = mx.video.VideoPlayer.STOPPED;
                this.setState(mx.video.VideoPlayer.REWINDING);
            }
            else
            {
                this.closeNS(true);
                this.setState(mx.video.VideoPlayer.STOPPED);
            } // end else if
        }
        else
        {
            this._pause(true);
            if (_autoRewind)
            {
                this._seek(0);
                _state = mx.video.VideoPlayer.STOPPED;
                this.setState(mx.video.VideoPlayer.REWINDING);
            }
            else
            {
                this.setState(mx.video.VideoPlayer.STOPPED);
            } // end else if
        } // end else if
    } // End of the function
    function seek(time)
    {
        if (_invalidSeekTime)
        {
            return;
        } // end if
        if (isNaN(time) || time < 0)
        {
            throw new mx.video.VideoError(mx.video.VideoError.INVALID_SEEK);
        } // end if
        if (!this.isXnOK())
        {
            if (_state == mx.video.VideoPlayer.CONNECTION_ERROR || _ncMgr == null || _ncMgr == undefined || _ncMgr.getNetConnection() == null || _ncMgr.getNetConnection() == undefined)
            {
                throw new mx.video.VideoError(mx.video.VideoError.NO_CONNECTION);
            }
            else
            {
                this.flushQueuedCmds();
                this.queueCmd(mx.video.VideoPlayer.SEEK, null, false, time);
                this.setState(mx.video.VideoPlayer.LOADING);
                _cachedState = mx.video.VideoPlayer.LOADING;
                _ncMgr.reconnect();
                return;
            } // end else if
        }
        else if (_state == mx.video.VideoPlayer.EXEC_QUEUED_CMD)
        {
            _state = _cachedState;
        }
        else if (!this.__get__stateResponsive())
        {
            this.queueCmd(mx.video.VideoPlayer.SEEK, null, false, time);
            return;
        }
        else
        {
            this.execQueuedCmds();
        } // end else if
        if (_ns == null || _ns == undefined)
        {
            this._createStream();
            _video.attachVideo(_ns);
            this.attachAudio(_ns);
        } // end if
        if (_atEnd && time < this.__get__playheadTime())
        {
            _atEnd = false;
        } // end if
        switch (_state)
        {
            case mx.video.VideoPlayer.PLAYING:
            {
                _state = mx.video.VideoPlayer.BUFFERING;
            } 
            case mx.video.VideoPlayer.BUFFERING:
            case mx.video.VideoPlayer.PAUSED:
            {
                this._seek(time);
                this.setState(mx.video.VideoPlayer.SEEKING);
                break;
            } 
            case mx.video.VideoPlayer.STOPPED:
            {
                if (_ncMgr.isRTMP())
                {
                    this._play(0);
                    this._pause(true);
                } // end if
                this._seek(time);
                _state = mx.video.VideoPlayer.PAUSED;
                this.setState(mx.video.VideoPlayer.SEEKING);
                break;
            } 
        } // End of switch
    } // End of the function
    function close()
    {
        this.closeNS(true);
        if (_ncMgr != null && _ncMgr != undefined && _ncMgr.isRTMP())
        {
            _ncMgr.close();
        } // end if
        this.setState(mx.video.VideoPlayer.DISCONNECTED);
        this.dispatchEvent({type: "close", state: _state, playheadTime: this.__get__playheadTime()});
    } // End of the function
    function get x()
    {
        return (_x);
    } // End of the function
    function set x(xpos)
    {
        _x = xpos;
        //return (this.x());
        null;
    } // End of the function
    function get y()
    {
        return (_y);
    } // End of the function
    function set y(ypos)
    {
        _y = ypos;
        //return (this.y());
        null;
    } // End of the function
    function get scaleX()
    {
        return (_video._xscale);
    } // End of the function
    function set scaleX(xs)
    {
        this.setScale(xs, this.__get__scaleY());
        //return (this.scaleX());
        null;
    } // End of the function
    function get scaleY()
    {
        return (_video._yscale);
    } // End of the function
    function set scaleY(ys)
    {
        this.setScale(this.__get__scaleX(), ys);
        //return (this.scaleY());
        null;
    } // End of the function
    function get width()
    {
        return (_video._width);
    } // End of the function
    function set width(w)
    {
        this.setSize(w, _video._height);
        //return (this.width());
        null;
    } // End of the function
    function get height()
    {
        return (_video._height);
    } // End of the function
    function set height(h)
    {
        this.setSize(_video._width, h);
        //return (this.height());
        null;
    } // End of the function
    function get videoWidth()
    {
        if (_readyDispatched)
        {
            _videoWidth = _video.width;
        } // end if
        return (_videoWidth);
    } // End of the function
    function get videoHeight()
    {
        if (_readyDispatched)
        {
            _videoHeight = _video.height;
        } // end if
        return (_videoHeight);
    } // End of the function
    function get visible()
    {
        if (!_hiddenForResize)
        {
            __visible = _visible;
        } // end if
        return (__visible);
    } // End of the function
    function set visible(v)
    {
        __visible = v;
        if (!_hiddenForResize)
        {
            _visible = __visible;
        } // end if
        //return (this.visible());
        null;
    } // End of the function
    function get autoSize()
    {
        return (_autoSize);
    } // End of the function
    function set autoSize(flag)
    {
        if (_autoSize != flag)
        {
            _autoSize = flag;
            if (_autoSize)
            {
                this.startAutoResize();
            } // end if
        } // end if
        //return (this.autoSize());
        null;
    } // End of the function
    function get maintainAspectRatio()
    {
        return (_aspectRatio);
    } // End of the function
    function set maintainAspectRatio(flag)
    {
        if (_aspectRatio != flag)
        {
            _aspectRatio = flag;
            if (_aspectRatio && !_autoSize)
            {
                this.startAutoResize();
            } // end if
        } // end if
        //return (this.maintainAspectRatio());
        null;
    } // End of the function
    function get autoRewind()
    {
        return (_autoRewind);
    } // End of the function
    function set autoRewind(flag)
    {
        _autoRewind = flag;
        //return (this.autoRewind());
        null;
    } // End of the function
    function get playheadTime()
    {
        var _loc2 = _ns == null || _ns == undefined ? (_currentPos) : (_ns.time);
        if (_metadata.audiodelay != undefined)
        {
            _loc2 = _loc2 - _metadata.audiodelay;
            if (_loc2 < 0)
            {
                _loc2 = 0;
            } // end if
        } // end if
        return (_loc2);
    } // End of the function
    function set playheadTime(position)
    {
        this.seek(position);
        //return (this.playheadTime());
        null;
    } // End of the function
    function get url()
    {
        return (_contentPath);
    } // End of the function
    function get volume()
    {
        return (_volume);
    } // End of the function
    function set volume(aVol)
    {
        _volume = aVol;
        if (!_hiddenForResize)
        {
            _sound.setVolume(_volume);
        } // end if
        //return (this.volume());
        null;
    } // End of the function
    function get transform()
    {
        return (_sound.getTransform());
    } // End of the function
    function set transform(s)
    {
        _sound.setTransform(s);
        //return (this.transform());
        null;
    } // End of the function
    function get isRTMP()
    {
        if (_ncMgr == null || _ncMgr == undefined)
        {
            return;
        } // end if
        return (_ncMgr.isRTMP());
    } // End of the function
    function get isLive()
    {
        return (_isLive);
    } // End of the function
    function get state()
    {
        return (_state);
    } // End of the function
    function get stateResponsive()
    {
        switch (_state)
        {
            case mx.video.VideoPlayer.DISCONNECTED:
            case mx.video.VideoPlayer.STOPPED:
            case mx.video.VideoPlayer.PLAYING:
            case mx.video.VideoPlayer.PAUSED:
            case mx.video.VideoPlayer.BUFFERING:
            {
                return (true);
            } 
        } // End of switch
        return (false);
    } // End of the function
    function get bytesLoaded()
    {
        if (_ns == null || _ns == undefined || _ncMgr.isRTMP())
        {
            return (-1);
        } // end if
        return (_ns.bytesLoaded);
    } // End of the function
    function get bytesTotal()
    {
        if (_ns == null || _ns == undefined || _ncMgr.isRTMP())
        {
            return (-1);
        } // end if
        return (_ns.bytesTotal);
    } // End of the function
    function get totalTime()
    {
        return (_streamLength);
    } // End of the function
    function get bufferTime()
    {
        return (_bufferTime);
    } // End of the function
    function set bufferTime(aTime)
    {
        _bufferTime = aTime;
        if (_ns != null && _ns != undefined)
        {
            _ns.setBufferTime(_bufferTime);
        } // end if
        //return (this.bufferTime());
        null;
    } // End of the function
    function get idleTimeout()
    {
        return (_idleTimeoutInterval);
    } // End of the function
    function set idleTimeout(aTime)
    {
        _idleTimeoutInterval = aTime;
        if (_idleTimeoutIntervalID > 0)
        {
            clearInterval(_idleTimeoutIntervalID);
            _idleTimeoutIntervalID = setInterval(this, "doIdleTimeout", _idleTimeoutInterval);
        } // end if
        //return (this.idleTimeout());
        null;
    } // End of the function
    function get playheadUpdateInterval()
    {
        return (_updateTimeInterval);
    } // End of the function
    function set playheadUpdateInterval(aTime)
    {
        _updateTimeInterval = aTime;
        if (_updateTimeIntervalID > 0)
        {
            clearInterval(_updateTimeIntervalID);
            _updateTimeIntervalID = setInterval(this, "doUpdateTime", _updateTimeInterval);
        } // end if
        //return (this.playheadUpdateInterval());
        null;
    } // End of the function
    function get progressInterval()
    {
        return (_updateProgressInterval);
    } // End of the function
    function set progressInterval(aTime)
    {
        _updateProgressInterval = aTime;
        if (_updateProgressIntervalID > 0)
        {
            clearInterval(_updateProgressIntervalID);
            _updateProgressIntervalID = setInterval(this, "doUpdateProgress", _updateProgressInterval);
        } // end if
        //return (this.progressInterval());
        null;
    } // End of the function
    function get ncMgr()
    {
        if (_ncMgr == null || _ncMgr == undefined)
        {
            this.createINCManager();
        } // end if
        return (_ncMgr);
    } // End of the function
    function get metadata()
    {
        return (_metadata);
    } // End of the function
    function doUpdateTime()
    {
        var _loc2 = this.__get__playheadTime();
        switch (_state)
        {
            case mx.video.VideoPlayer.STOPPED:
            case mx.video.VideoPlayer.PAUSED:
            case mx.video.VideoPlayer.DISCONNECTED:
            case mx.video.VideoPlayer.CONNECTION_ERROR:
            {
                clearInterval(_updateTimeIntervalID);
                _updateTimeIntervalID = 0;
                break;
            } 
        } // End of switch
        if (_lastUpdateTime != _loc2)
        {
            this.dispatchEvent({type: "playheadUpdate", state: _state, playheadTime: _loc2});
            _lastUpdateTime = _loc2;
        } // end if
    } // End of the function
    function doUpdateProgress()
    {
        if (_ns == null || _ns == undefined)
        {
            return;
        } // end if
        if (_ns.bytesTotal >= 0 && _ns.bytesTotal >= 0)
        {
            this.dispatchEvent({type: "progress", bytesLoaded: _ns.bytesLoaded, bytesTotal: _ns.bytesTotal});
        } // end if
        if (_state == mx.video.VideoPlayer.DISCONNECTED || _state == mx.video.VideoPlayer.CONNECTION_ERROR || _ns.bytesLoaded == _ns.bytesTotal)
        {
            clearInterval(_updateProgressIntervalID);
            _updateProgressIntervalID = 0;
        } // end if
    } // End of the function
    function rtmpOnStatus(info)
    {
        if (_state == mx.video.VideoPlayer.CONNECTION_ERROR)
        {
            return;
        } // end if
        switch (info.code)
        {
            case "NetStream.Play.Stop":
            {
                if (_startingPlay)
                {
                    return;
                } // end if
                switch (_state)
                {
                    case mx.video.VideoPlayer.RESIZING:
                    {
                        if (_hiddenForResize)
                        {
                            this.finishAutoResize();
                        } // end if
                        break;
                    } 
                    case mx.video.VideoPlayer.LOADING:
                    case mx.video.VideoPlayer.STOPPED:
                    case mx.video.VideoPlayer.PAUSED:
                    {
                        break;
                    } 
                    default:
                    {
                        _sawPlayStop = true;
                        break;
                    } 
                } // End of switch
                break;
            } 
            case "NetStream.Buffer.Empty":
            {
                switch (_bufferState)
                {
                    case mx.video.VideoPlayer.BUFFER_FULL:
                    {
                        if (_sawPlayStop)
                        {
                            this.rtmpDoStopAtEnd(true);
                        }
                        else if (_state == mx.video.VideoPlayer.PLAYING)
                        {
                            this.setState(mx.video.VideoPlayer.BUFFERING);
                        } // end else if
                        break;
                    } 
                } // End of switch
                _bufferState = mx.video.VideoPlayer.BUFFER_EMPTY;
                _sawPlayStop = false;
                break;
            } 
            case "NetStream.Buffer.Flush":
            {
                if (_sawSeekNotify && _state == mx.video.VideoPlayer.SEEKING)
                {
                    _bufferState = mx.video.VideoPlayer.BUFFER_EMPTY;
                    _sawPlayStop = false;
                    this.setStateFromCachedState();
                    this.doUpdateTime();
                } // end if
                if (_sawPlayStop && (_bufferState == mx.video.VideoPlayer.BUFFER_EMPTY || _bufferTime <= 1.000000E-001 && _ns.bufferLength <= 1.000000E-001))
                {
                    _cachedPlayheadTime = playheadTime;
                    clearInterval(_rtmpDoStopAtEndIntervalID);
                    _rtmpDoStopAtEndIntervalID = setInterval(this, "rtmpDoStopAtEnd", mx.video.VideoPlayer.RTMP_DO_STOP_AT_END_INTERVAL);
                } // end if
                switch (_bufferState)
                {
                    case mx.video.VideoPlayer.BUFFER_EMPTY:
                    {
                        if (!_hiddenForResize)
                        {
                            if (_state == mx.video.VideoPlayer.LOADING && _cachedState == mx.video.VideoPlayer.PLAYING || _state == mx.video.VideoPlayer.BUFFERING)
                            {
                                this.setState(mx.video.VideoPlayer.PLAYING);
                            }
                            else if (_cachedState == mx.video.VideoPlayer.BUFFERING)
                            {
                                _cachedState = mx.video.VideoPlayer.PLAYING;
                            } // end if
                        } // end else if
                        _bufferState = mx.video.VideoPlayer.BUFFER_FLUSH;
                        break;
                    } 
                    default:
                    {
                        if (_state == mx.video.VideoPlayer.BUFFERING)
                        {
                            this.setStateFromCachedState();
                        } // end if
                        break;
                    } 
                } // End of switch
                break;
            } 
            case "NetStream.Buffer.Full":
            {
                if (_sawSeekNotify && _state == mx.video.VideoPlayer.SEEKING)
                {
                    _bufferState = mx.video.VideoPlayer.BUFFER_EMPTY;
                    _sawPlayStop = false;
                    this.setStateFromCachedState();
                    this.doUpdateTime();
                } // end if
                switch (_bufferState)
                {
                    case mx.video.VideoPlayer.BUFFER_EMPTY:
                    {
                        _bufferState = mx.video.VideoPlayer.BUFFER_FULL;
                        if (!_hiddenForResize)
                        {
                            if (_state == mx.video.VideoPlayer.LOADING && _cachedState == mx.video.VideoPlayer.PLAYING || _state == mx.video.VideoPlayer.BUFFERING)
                            {
                                this.setState(mx.video.VideoPlayer.PLAYING);
                            }
                            else if (_cachedState == mx.video.VideoPlayer.BUFFERING)
                            {
                                _cachedState = mx.video.VideoPlayer.PLAYING;
                            } // end else if
                            if (_rtmpDoStopAtEndIntervalID != 0)
                            {
                                _sawPlayStop = true;
                                clearInterval(_rtmpDoStopAtEndIntervalID);
                                _rtmpDoStopAtEndIntervalID = 0;
                            } // end if
                        } // end if
                        break;
                    } 
                    case mx.video.VideoPlayer.BUFFER_FLUSH:
                    {
                        _bufferState = mx.video.VideoPlayer.BUFFER_FULL;
                        if (_rtmpDoStopAtEndIntervalID != 0)
                        {
                            _sawPlayStop = true;
                            clearInterval(_rtmpDoStopAtEndIntervalID);
                            _rtmpDoStopAtEndIntervalID = 0;
                        } // end if
                        break;
                    } 
                } // End of switch
                if (_state == mx.video.VideoPlayer.BUFFERING)
                {
                    this.setStateFromCachedState();
                } // end if
                break;
            } 
            case "NetStream.Pause.Notify":
            {
                if (_state == mx.video.VideoPlayer.RESIZING && _hiddenForResize)
                {
                    this.finishAutoResize();
                } // end if
                break;
            } 
            case "NetStream.Unpause.Notify":
            {
                if (_state == mx.video.VideoPlayer.PAUSED)
                {
                    _state = mx.video.VideoPlayer.PLAYING;
                    this.setState(mx.video.VideoPlayer.BUFFERING);
                }
                else
                {
                    _cachedState = mx.video.VideoPlayer.PLAYING;
                } // end else if
                break;
            } 
            case "NetStream.Play.Start":
            {
                clearInterval(_rtmpDoStopAtEndIntervalID);
                _rtmpDoStopAtEndIntervalID = 0;
                _bufferState = mx.video.VideoPlayer.BUFFER_EMPTY;
                _sawPlayStop = false;
                if (_startingPlay)
                {
                    _startingPlay = false;
                    _cachedPlayheadTime = playheadTime;
                }
                else if (_state == mx.video.VideoPlayer.PLAYING)
                {
                    this.setState(mx.video.VideoPlayer.BUFFERING);
                } // end else if
                break;
            } 
            case "NetStream.Play.Reset":
            {
                clearInterval(_rtmpDoStopAtEndIntervalID);
                _rtmpDoStopAtEndIntervalID = 0;
                if (_state == mx.video.VideoPlayer.REWINDING)
                {
                    clearInterval(_rtmpDoSeekIntervalID);
                    _rtmpDoSeekIntervalID = 0;
                    if (this.__get__playheadTime() == 0 || this.__get__playheadTime() < _cachedPlayheadTime)
                    {
                        this.setStateFromCachedState();
                    }
                    else
                    {
                        _cachedPlayheadTime = playheadTime;
                        _rtmpDoSeekIntervalID = setInterval(this, "rtmpDoSeek", mx.video.VideoPlayer.RTMP_DO_SEEK_INTERVAL);
                    } // end if
                } // end else if
                break;
            } 
            case "NetStream.Seek.Notify":
            {
                if (this.__get__playheadTime() != _cachedPlayheadTime)
                {
                    this.setStateFromCachedState();
                    this.doUpdateTime();
                }
                else
                {
                    _sawSeekNotify = true;
                    if (_rtmpDoSeekIntervalID == 0)
                    {
                        _rtmpDoSeekIntervalID = setInterval(this, "rtmpDoSeek", mx.video.VideoPlayer.RTMP_DO_SEEK_INTERVAL);
                    } // end if
                } // end else if
                break;
            } 
            case "Netstream.Play.UnpublishNotify":
            {
                break;
            } 
            case "Netstream.Play.PublishNotify":
            {
                break;
            } 
            case "NetStream.Play.StreamNotFound":
            {
                if (!_ncMgr.connectAgain())
                {
                    this.setState(mx.video.VideoPlayer.CONNECTION_ERROR);
                } // end if
                break;
            } 
            case "NetStream.Play.Failed":
            case "NetStream.Failed":
            {
                this.setState(mx.video.VideoPlayer.CONNECTION_ERROR);
                break;
            } 
        } // End of switch
    } // End of the function
    function httpOnStatus(info)
    {
        switch (info.code)
        {
            case "NetStream.Play.Stop":
            {
                clearInterval(_delayedBufferingIntervalID);
                _delayedBufferingIntervalID = 0;
                if (_invalidSeekTime)
                {
                    _invalidSeekTime = false;
                    _invalidSeekRecovery = true;
                    this.setState(_cachedState);
                    this.seek(this.__get__playheadTime());
                }
                else
                {
                    switch (_state)
                    {
                        case mx.video.VideoPlayer.PLAYING:
                        case mx.video.VideoPlayer.BUFFERING:
                        case mx.video.VideoPlayer.SEEKING:
                        {
                            this.httpDoStopAtEnd();
                            break;
                        } 
                    } // End of switch
                } // end else if
                break;
            } 
            case "NetStream.Seek.InvalidTime":
            {
                if (_invalidSeekRecovery)
                {
                    _invalidSeekTime = false;
                    _invalidSeekRecovery = false;
                    this.setState(_cachedState);
                    this.seek(0);
                }
                else
                {
                    _invalidSeekTime = true;
                } // end else if
                break;
            } 
            case "NetStream.Buffer.Empty":
            {
                _bufferState = mx.video.VideoPlayer.BUFFER_EMPTY;
                if (_state == mx.video.VideoPlayer.PLAYING)
                {
                    clearInterval(_delayedBufferingIntervalID);
                    _delayedBufferingIntervalID = setInterval(this, "doDelayedBuffering", _delayedBufferingInterval);
                } // end if
                break;
            } 
            case "NetStream.Buffer.Full":
            case "NetStream.Buffer.Flush":
            {
                clearInterval(_delayedBufferingIntervalID);
                _delayedBufferingIntervalID = 0;
                _bufferState = mx.video.VideoPlayer.BUFFER_FULL;
                if (!_hiddenForResize)
                {
                    if (_state == mx.video.VideoPlayer.LOADING && _cachedState == mx.video.VideoPlayer.PLAYING || _state == mx.video.VideoPlayer.BUFFERING)
                    {
                        this.setState(mx.video.VideoPlayer.PLAYING);
                    }
                    else if (_cachedState == mx.video.VideoPlayer.BUFFERING)
                    {
                        _cachedState = mx.video.VideoPlayer.PLAYING;
                    } // end if
                } // end else if
                break;
            } 
            case "NetStream.Seek.Notify":
            {
                _invalidSeekRecovery = false;
                switch (_state)
                {
                    case mx.video.VideoPlayer.SEEKING:
                    case mx.video.VideoPlayer.REWINDING:
                    {
                        if (_httpDoSeekIntervalID == 0)
                        {
                            _httpDoSeekCount = 0;
                            _httpDoSeekIntervalID = setInterval(this, "httpDoSeek", mx.video.VideoPlayer.HTTP_DO_SEEK_INTERVAL);
                        } // end if
                        break;
                    } 
                } // End of switch
                break;
            } 
            case "NetStream.Play.StreamNotFound":
            {
                this.setState(mx.video.VideoPlayer.CONNECTION_ERROR);
                break;
            } 
        } // End of switch
    } // End of the function
    function ncConnected()
    {
        if (_ncMgr == null || _ncMgr == undefined || _ncMgr.getNetConnection() == null || _ncMgr.getNetConnection() == undefined)
        {
            this.setState(mx.video.VideoPlayer.CONNECTION_ERROR);
        }
        else
        {
            this._createStream();
            this._setUpStream();
        } // end else if
    } // End of the function
    function ncReconnected()
    {
        if (_ncMgr == null || _ncMgr == undefined || _ncMgr.getNetConnection() == null || _ncMgr.getNetConnection() == undefined)
        {
            this.setState(mx.video.VideoPlayer.CONNECTION_ERROR);
        }
        else
        {
            _ns = null;
            _state = mx.video.VideoPlayer.STOPPED;
            this.execQueuedCmds();
        } // end else if
    } // End of the function
    function onMetaData(info)
    {
        if (_metadata != null)
        {
            return;
        } // end if
        _metadata = info;
        if (_streamLength == undefined || _streamLength == null || _streamLength <= 0)
        {
            _streamLength = info.duration;
        } // end if
        if (isNaN(_videoWidth) || _videoWidth <= 0)
        {
            _videoWidth = info.width;
        } // end if
        if (isNaN(_videoHeight) || _videoHeight <= 0)
        {
            _videoHeight = info.height;
        } // end if
        this.dispatchEvent({type: "metadataReceived", info: info});
    } // End of the function
    function onCuePoint(info)
    {
        if (!_hiddenForResize || !isNaN(_hiddenRewindPlayheadTime) && this.__get__playheadTime() < _hiddenRewindPlayheadTime)
        {
            this.dispatchEvent({type: "cuePoint", info: info});
        } // end if
    } // End of the function
    function setState(s)
    {
        if (s == _state)
        {
            return;
        } // end if
        _hiddenRewindPlayheadTime = undefined;
        _cachedState = _state;
        _cachedPlayheadTime = playheadTime;
        _state = s;
        var _loc2 = _state;
        this.dispatchEvent({type: "stateChange", state: _loc2, playheadTime: this.__get__playheadTime()});
        if (!_readyDispatched)
        {
            switch (_loc2)
            {
                case mx.video.VideoPlayer.STOPPED:
                case mx.video.VideoPlayer.PLAYING:
                case mx.video.VideoPlayer.PAUSED:
                case mx.video.VideoPlayer.BUFFERING:
                {
                    _readyDispatched = true;
                    this.dispatchEvent({type: "ready", state: _loc2, playheadTime: this.__get__playheadTime()});
                    break;
                } 
            } // End of switch
        } // end if
        switch (_cachedState)
        {
            case mx.video.VideoPlayer.REWINDING:
            {
                this.dispatchEvent({type: "rewind", state: _loc2, playheadTime: this.__get__playheadTime()});
                if (_ncMgr.isRTMP() && _loc2 == mx.video.VideoPlayer.STOPPED)
                {
                    this.closeNS();
                } // end if
                break;
            } 
        } // End of switch
        switch (_loc2)
        {
            case mx.video.VideoPlayer.STOPPED:
            case mx.video.VideoPlayer.PAUSED:
            {
                if (_ncMgr.isRTMP() && _idleTimeoutIntervalID == 0)
                {
                    _idleTimeoutIntervalID = setInterval(this, "doIdleTimeout", _idleTimeoutInterval);
                } // end if
                break;
            } 
            case mx.video.VideoPlayer.SEEKING:
            case mx.video.VideoPlayer.REWINDING:
            {
                _bufferState = mx.video.VideoPlayer.BUFFER_EMPTY;
                _sawPlayStop = false;
            } 
            case mx.video.VideoPlayer.PLAYING:
            case mx.video.VideoPlayer.BUFFERING:
            {
                if (_updateTimeIntervalID == 0)
                {
                    _updateTimeIntervalID = setInterval(this, "doUpdateTime", _updateTimeInterval);
                } // end if
            } 
            case mx.video.VideoPlayer.LOADING:
            case mx.video.VideoPlayer.RESIZING:
            {
                clearInterval(_idleTimeoutIntervalID);
                _idleTimeoutIntervalID = 0;
                break;
            } 
        } // End of switch
        this.execQueuedCmds();
    } // End of the function
    function setStateFromCachedState()
    {
        switch (_cachedState)
        {
            case mx.video.VideoPlayer.PLAYING:
            case mx.video.VideoPlayer.PAUSED:
            {
                this.setState(_cachedState);
                break;
            } 
            case mx.video.VideoPlayer.BUFFERING:
            {
                if (_bufferState == mx.video.VideoPlayer.BUFFER_EMPTY)
                {
                    this.setState(mx.video.VideoPlayer.BUFFERING);
                }
                else
                {
                    this.setState(_cachedState);
                } // end else if
                break;
            } 
            default:
            {
                this.setState(mx.video.VideoPlayer.STOPPED);
                break;
            } 
        } // End of switch
    } // End of the function
    function createINCManager()
    {
        if (this.ncMgrClassName == null || this.ncMgrClassName == undefined)
        {
            this.ncMgrClassName = mx.video.VideoPlayer.DEFAULT_INCMANAGER;
        } // end if
        var ncMgrConstructor = eval(this.ncMgrClassName);
        this._ncMgr = new ncMgrConstructor();
        this._ncMgr.setVideoPlayer(this);
    } // End of the function
    function rtmpDoStopAtEnd(force)
    {
        if (_rtmpDoStopAtEndIntervalID > 0)
        {
            switch (_state)
            {
                case mx.video.VideoPlayer.DISCONNECTED:
                case mx.video.VideoPlayer.CONNECTION_ERROR:
                {
                    clearInterval(_rtmpDoStopAtEndIntervalID);
                    _rtmpDoStopAtEndIntervalID = 0;
                    return;
                } 
            } // End of switch
            if (force || _cachedPlayheadTime == this.__get__playheadTime())
            {
                clearInterval(_rtmpDoStopAtEndIntervalID);
                _rtmpDoStopAtEndIntervalID = 0;
            }
            else
            {
                _cachedPlayheadTime = playheadTime;
                return;
            } // end if
        } // end else if
        _bufferState = mx.video.VideoPlayer.BUFFER_EMPTY;
        _sawPlayStop = false;
        _atEnd = true;
        this.setState(mx.video.VideoPlayer.STOPPED);
        if (_state != mx.video.VideoPlayer.STOPPED)
        {
            return;
        } // end if
        this.doUpdateTime();
        if (_state != mx.video.VideoPlayer.STOPPED)
        {
            return;
        } // end if
        this.dispatchEvent({type: "complete", state: _state, playheadTime: this.__get__playheadTime()});
        if (_state != mx.video.VideoPlayer.STOPPED)
        {
            return;
        } // end if
        if (_autoRewind && !_isLive && this.__get__playheadTime() != 0)
        {
            _atEnd = false;
            _currentPos = 0;
            this._play(0, 0);
            this.setState(mx.video.VideoPlayer.REWINDING);
        }
        else
        {
            this.closeNS();
        } // end else if
    } // End of the function
    function rtmpDoSeek()
    {
        if (_state != mx.video.VideoPlayer.REWINDING && _state != mx.video.VideoPlayer.SEEKING)
        {
            clearInterval(_rtmpDoSeekIntervalID);
            _rtmpDoSeekIntervalID = 0;
            _sawSeekNotify = false;
        }
        else if (this.__get__playheadTime() != _cachedPlayheadTime)
        {
            clearInterval(_rtmpDoSeekIntervalID);
            _rtmpDoSeekIntervalID = 0;
            _sawSeekNotify = false;
            this.setStateFromCachedState();
            this.doUpdateTime();
        } // end else if
    } // End of the function
    function httpDoStopAtEnd()
    {
        _atEnd = true;
        if (_streamLength == undefined || _streamLength == null || _streamLength <= 0)
        {
            _streamLength = _ns.time;
        } // end if
        this._pause(true);
        this.setState(mx.video.VideoPlayer.STOPPED);
        if (_state != mx.video.VideoPlayer.STOPPED)
        {
            return;
        } // end if
        this.doUpdateTime();
        if (_state != mx.video.VideoPlayer.STOPPED)
        {
            return;
        } // end if
        this.dispatchEvent({type: "complete", state: _state, playheadTime: this.__get__playheadTime()});
        if (_state != mx.video.VideoPlayer.STOPPED)
        {
            return;
        } // end if
        if (_autoRewind)
        {
            _atEnd = false;
            this._pause(true);
            this._seek(0);
            this.setState(mx.video.VideoPlayer.REWINDING);
        } // end if
    } // End of the function
    function httpDoSeek()
    {
        var _loc2 = _state == mx.video.VideoPlayer.REWINDING || _state == mx.video.VideoPlayer.SEEKING;
        if (_loc2 && _httpDoSeekCount < mx.video.VideoPlayer.HTTP_DO_SEEK_MAX_COUNT && (_cachedPlayheadTime == this.__get__playheadTime() || _invalidSeekTime))
        {
            ++_httpDoSeekCount;
            return;
        } // end if
        _httpDoSeekCount = 0;
        clearInterval(_httpDoSeekIntervalID);
        _httpDoSeekIntervalID = 0;
        if (!_loc2)
        {
            return;
        } // end if
        this.setStateFromCachedState();
        if (_invalidSeekTime)
        {
            _invalidSeekTime = false;
            _invalidSeekRecovery = true;
            this.seek(this.__get__playheadTime());
        }
        else
        {
            this.doUpdateTime();
        } // end else if
    } // End of the function
    function closeNS(updateCurrentPos)
    {
        if (_ns != null && _ns != undefined)
        {
            if (updateCurrentPos)
            {
                clearInterval(_updateTimeIntervalID);
                _updateTimeIntervalID = 0;
                this.doUpdateTime();
                _currentPos = _ns.time;
            } // end if
            delete _ns.onStatus;
            _ns.onStatus = null;
            _ns.close();
            _ns = null;
        } // end if
    } // End of the function
    function doDelayedBuffering()
    {
        switch (_state)
        {
            case mx.video.VideoPlayer.LOADING:
            case mx.video.VideoPlayer.RESIZING:
            {
                break;
            } 
            case mx.video.VideoPlayer.PLAYING:
            {
                clearInterval(_delayedBufferingIntervalID);
                _delayedBufferingIntervalID = 0;
                this.setState(mx.video.VideoPlayer.BUFFERING);
                break;
            } 
            default:
            {
                clearInterval(_delayedBufferingIntervalID);
                _delayedBufferingIntervalID = 0;
                break;
            } 
        } // End of switch
    } // End of the function
    function _pause(doPause)
    {
        clearInterval(_rtmpDoStopAtEndIntervalID);
        _rtmpDoStopAtEndIntervalID = 0;
        _ns.pause(doPause);
    } // End of the function
    function _play()
    {
        clearInterval(_rtmpDoStopAtEndIntervalID);
        _rtmpDoStopAtEndIntervalID = 0;
        _startingPlay = true;
        switch (arguments.length)
        {
            case 0:
            {
                _ns.play(_ncMgr.getStreamName(), _isLive ? (-1) : (0), -1);
                break;
            } 
            case 1:
            {
                _ns.play(_ncMgr.getStreamName(), _isLive ? (-1) : (arguments[0]), -1);
                break;
            } 
            case 2:
            {
                _ns.play(_ncMgr.getStreamName(), _isLive ? (-1) : (arguments[0]), arguments[1]);
                break;
            } 
            default:
            {
                throw new Error("bad args to _play");
            } 
        } // End of switch
    } // End of the function
    function _seek(time)
    {
        clearInterval(_rtmpDoStopAtEndIntervalID);
        _rtmpDoStopAtEndIntervalID = 0;
        if (_metadata.audiodelay != undefined && time + _metadata.audiodelay < _streamLength)
        {
            time = time + _metadata.audiodelay;
        } // end if
        _ns.seek(time);
        _invalidSeekTime = false;
        _bufferState = mx.video.VideoPlayer.BUFFER_EMPTY;
        _sawPlayStop = false;
        _sawSeekNotify = false;
    } // End of the function
    function isXnOK()
    {
        if (_state == mx.video.VideoPlayer.LOADING)
        {
            return (true);
        } // end if
        if (_state == mx.video.VideoPlayer.CONNECTION_ERROR)
        {
            return (false);
        } // end if
        if (_state != mx.video.VideoPlayer.DISCONNECTED)
        {
            if (_ncMgr == null || _ncMgr == undefined || _ncMgr.getNetConnection() == null || _ncMgr.getNetConnection() == undefined || !_ncMgr.getNetConnection().isConnected)
            {
                this.setState(mx.video.VideoPlayer.DISCONNECTED);
                return (false);
            } // end if
            return (true);
        } // end if
        return (false);
    } // End of the function
    function startAutoResize()
    {
        switch (_state)
        {
            case mx.video.VideoPlayer.DISCONNECTED:
            case mx.video.VideoPlayer.CONNECTION_ERROR:
            {
                return;
            } 
        } // End of switch
        _autoResizeDone = false;
        if (this.__get__stateResponsive() && _videoWidth != undefined && _videoHeight != undefined)
        {
            this.doAutoResize();
        }
        else
        {
            clearInterval(_autoResizeIntervalID);
            _autoResizeIntervalID = setInterval(this, "doAutoResize", mx.video.VideoPlayer.AUTO_RESIZE_INTERVAL);
            
        } // end else if
    } // End of the function
    function doAutoResize()
    {
        if (_autoResizeIntervalID > 0)
        {
            switch (_state)
            {
                case mx.video.VideoPlayer.RESIZING:
                case mx.video.VideoPlayer.LOADING:
                {
                    break;
                } 
                case mx.video.VideoPlayer.DISCONNECTED:
                case mx.video.VideoPlayer.CONNECTION_ERROR:
                {
                    clearInterval(_autoResizeIntervalID);
                    _autoResizeIntervalID = 0;
                    return;
                } 
                default:
                {
                    if (!this.__get__stateResponsive())
                    {
                        return;
                    } // end if
                } 
            } // End of switch
            if (_video.width != _prevVideoWidth || _video.height != _prevVideoHeight || _bufferState == mx.video.VideoPlayer.BUFFER_FULL || _bufferState == mx.video.VideoPlayer.BUFFER_FLUSH || _ns.time > mx.video.VideoPlayer.AUTO_RESIZE_PLAYHEAD_TIMEOUT)
            {
                if (_hiddenForResize && _metadata == null && _hiddenForResizeMetadataDelay < mx.video.VideoPlayer.AUTO_RESIZE_METADATA_DELAY_MAX)
                {
                    ++_hiddenForResizeMetadataDelay;
                    return;
                } // end if
                _videoWidth = _video.width;
                _videoHeight = _video.height;
                clearInterval(_autoResizeIntervalID);
                _autoResizeIntervalID = 0;
            }
            else
            {
                return;
            } // end if
        } // end else if
        if (!_autoSize && !_aspectRatio || _autoResizeDone)
        {
            this.setState(_cachedState);
            return;
        } // end if
        _autoResizeDone = true;
        if (_autoSize)
        {
            _video._width = _videoWidth;
            _video._height = _videoHeight;
        }
        else if (_aspectRatio)
        {
            var _loc3 = _videoWidth * this.__get__height() / _videoHeight;
            var _loc2 = _videoHeight * this.__get__width() / _videoWidth;
            if (_loc2 < this.__get__height())
            {
                _video._height = _loc2;
            }
            else if (_loc3 < this.__get__width())
            {
                _video._width = _loc3;
            } // end else if
        } // end else if
        if (_hiddenForResize)
        {
            _hiddenRewindPlayheadTime = playheadTime;
            if (_state == mx.video.VideoPlayer.LOADING)
            {
                _cachedState = mx.video.VideoPlayer.PLAYING;
            } // end if
            if (!_ncMgr.isRTMP())
            {
                this._pause(true);
                this._seek(0);
                clearInterval(_finishAutoResizeIntervalID);
                _finishAutoResizeIntervalID = setInterval(this, "finishAutoResize", mx.video.VideoPlayer.FINISH_AUTO_RESIZE_INTERVAL);
            }
            else if (!_isLive)
            {
                _currentPos = 0;
                this._play(0, 0);
                this.setState(mx.video.VideoPlayer.RESIZING);
            }
            else if (_autoPlay)
            {
                clearInterval(_finishAutoResizeIntervalID);
                _finishAutoResizeIntervalID = setInterval(this, "finishAutoResize", mx.video.VideoPlayer.FINISH_AUTO_RESIZE_INTERVAL);
            }
            else
            {
                this.finishAutoResize();
            } // end else if
        }
        else
        {
            this.dispatchEvent({type: "resize", x: _x, y: _y, width: _width, height: _height});
        } // end else if
    } // End of the function
    function finishAutoResize()
    {
        clearInterval(_finishAutoResizeIntervalID);
        _finishAutoResizeIntervalID = 0;
        if (this.__get__stateResponsive())
        {
            return;
        } // end if
        _visible = __visible;
        _sound.setVolume(_volume);
        _hiddenForResize = false;
        this.dispatchEvent({type: "resize", x: _x, y: _y, width: _width, height: _height});
        if (_autoPlay)
        {
            if (_ncMgr.isRTMP())
            {
                if (!_isLive)
                {
                    _currentPos = 0;
                    this._play(0);
                } // end if
                if (_state == mx.video.VideoPlayer.RESIZING)
                {
                    this.setState(mx.video.VideoPlayer.LOADING);
                    _cachedState = mx.video.VideoPlayer.PLAYING;
                } // end if
            }
            else
            {
                this._pause(false);
                _cachedState = mx.video.VideoPlayer.PLAYING;
            } // end else if
        }
        else
        {
            this.setState(mx.video.VideoPlayer.STOPPED);
        } // end else if
    } // End of the function
    function _createStream()
    {
        _ns = new NetStream(_ncMgr.getNetConnection());
        _ns.mc = this;
        if (_ncMgr.isRTMP())
        {
            _ns.onStatus = function (info)
            {
                mc.rtmpOnStatus(info);
            };
        }
        else
        {
            _ns.onStatus = function (info)
            {
                mc.httpOnStatus(info);
            };
        } // end else if
        _ns.onMetaData = function (info)
        {
            mc.onMetaData(info);
        };
        _ns.onCuePoint = function (info)
        {
            mc.onCuePoint(info);
        };
        _ns.setBufferTime(_bufferTime);
    } // End of the function
    function _setUpStream()
    {
        _video.attachVideo(_ns);
        this.attachAudio(_ns);
        if (!isNaN(_ncMgr.getStreamLength()) && _ncMgr.getStreamLength() >= 0)
        {
            _streamLength = _ncMgr.getStreamLength();
        } // end if
        if (!isNaN(_ncMgr.getStreamWidth()) && _ncMgr.getStreamWidth() >= 0)
        {
            _videoWidth = _ncMgr.getStreamWidth();
        }
        else
        {
            _videoWidth = undefined;
        } // end else if
        if (!isNaN(_ncMgr.getStreamHeight()) && _ncMgr.getStreamHeight() >= 0)
        {
            _videoHeight = _ncMgr.getStreamHeight();
        }
        else
        {
            _videoHeight = undefined;
        } // end else if
        if ((_autoSize || _aspectRatio) && _videoWidth != undefined && _videoHeight != undefined)
        {
            _prevVideoWidth = undefined;
            _prevVideoHeight = undefined;
            this.doAutoResize();
        } // end if
        if (!_autoSize && !_aspectRatio || _videoWidth != undefined && _videoHeight != undefined)
        {
            if (_autoPlay)
            {
                if (!_ncMgr.isRTMP())
                {
                    _cachedState = mx.video.VideoPlayer.BUFFERING;
                    this._play();
                }
                else if (_isLive)
                {
                    _cachedState = mx.video.VideoPlayer.BUFFERING;
                    this._play(-1);
                }
                else
                {
                    _cachedState = mx.video.VideoPlayer.BUFFERING;
                    this._play(0);
                } // end else if
            }
            else
            {
                _cachedState = mx.video.VideoPlayer.STOPPED;
                if (_ncMgr.isRTMP())
                {
                    this._play(0, 0);
                }
                else
                {
                    this._play();
                    this._pause(true);
                    this._seek(0);
                } // end else if
            } // end else if
        }
        else
        {
            if (!_hiddenForResize)
            {
                __visible = _visible;
                _visible = false;
                _volume = _sound.getVolume();
                _sound.setVolume(0);
                _hiddenForResize = true;
            } // end if
            _hiddenForResizeMetadataDelay = 0;
            this._play(0);
            if (_currentPos > 0)
            {
                this._seek(_currentPos);
                _currentPos = 0;
            } // end if
        } // end else if
        clearInterval(_autoResizeIntervalID);
        _autoResizeIntervalID = setInterval(this, "doAutoResize", mx.video.VideoPlayer.AUTO_RESIZE_INTERVAL);
    } // End of the function
    function doIdleTimeout()
    {
        clearInterval(_idleTimeoutIntervalID);
        _idleTimeoutIntervalID = 0;
        this.close();
    } // End of the function
    function flushQueuedCmds()
    {
        while (_cmdQueue.length > 0)
        {
            _cmdQueue.pop();
        } // end while
    } // End of the function
    function execQueuedCmds()
    {
        while (_cmdQueue.length > 0 && (this.__get__stateResponsive() || _state == mx.video.VideoPlayer.CONNECTION_ERROR) && (_cmdQueue[0].url != null && _cmdQueue[0].url != undefined || _state != mx.video.VideoPlayer.DISCONNECTED && _state != mx.video.VideoPlayer.CONNECTION_ERROR))
        {
            var _loc2 = _cmdQueue.shift();
            _cachedState = _state;
            _state = mx.video.VideoPlayer.EXEC_QUEUED_CMD;
            switch (_loc2.type)
            {
                case mx.video.VideoPlayer.PLAY:
                {
                    this.play(_loc2.url, _loc2.isLive, _loc2.time);
                    break;
                } 
                case mx.video.VideoPlayer.LOAD:
                {
                    this.load(_loc2.url, _loc2.isLive, _loc2.time);
                    break;
                } 
                case mx.video.VideoPlayer.PAUSE:
                {
                    this.pause();
                    break;
                } 
                case mx.video.VideoPlayer.STOP:
                {
                    this.stop();
                    break;
                } 
                case mx.video.VideoPlayer.SEEK:
                {
                    this.seek(_loc2.time);
                    break;
                } 
            } // End of switch
        } // end while
    } // End of the function
    function queueCmd(type, url, isLive, time)
    {
        _cmdQueue.push({type: type, url: url, isLive: false, time: time});
    } // End of the function
    static var version = "1.0.1.10";
    static var shortVersion = "1.0.1";
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
    static var BUFFER_FLUSH = "bufferFlush";
    static var DEFAULT_INCMANAGER = "mx.video.NCManager";
    static var DEFAULT_UPDATE_TIME_INTERVAL = 250;
    static var DEFAULT_UPDATE_PROGRESS_INTERVAL = 250;
    static var DEFAULT_IDLE_TIMEOUT_INTERVAL = 300000;
    static var AUTO_RESIZE_INTERVAL = 100;
    static var AUTO_RESIZE_PLAYHEAD_TIMEOUT = 5.000000E-001;
    static var AUTO_RESIZE_METADATA_DELAY_MAX = 5;
    static var FINISH_AUTO_RESIZE_INTERVAL = 250;
    static var RTMP_DO_STOP_AT_END_INTERVAL = 500;
    static var RTMP_DO_SEEK_INTERVAL = 100;
    static var HTTP_DO_SEEK_INTERVAL = 250;
    static var HTTP_DO_SEEK_MAX_COUNT = 4;
    static var CLOSE_NS_INTERVAL = 2.500000E-001;
    static var HTTP_DELAYED_BUFFERING_INTERVAL = 100;
    static var PLAY = 0;
    static var LOAD = 1;
    static var PAUSE = 2;
    static var STOP = 3;
    static var SEEK = 4;
} // End of Class