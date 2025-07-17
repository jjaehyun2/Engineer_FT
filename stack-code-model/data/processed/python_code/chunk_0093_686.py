class mx.video.FLVPlayback extends MovieClip
{
    var _autoPlay, _autoRewind, _autoSize, _bufferTime, _contentPath, _cuePoints, _idleTimeout, _isLive, _aspectRatio, _seekToPrevOffset, _playheadUpdateInterval, _progressInterval, _totalTime, _transform, _volume, _skinAutoHide, _bufferingBarHides, _height, __height, _prevHeight, _origHeight, _width, __width, _prevWidth, _origWidth, _scaleX, _scaleY, _xscale, _yscale, _preSeekTime, _firstStreamReady, _firstStreamShown, _activeVP, _visibleVP, _topVP, _vp, _vpState, _cpMgr, boundingBox_mc, preview_mc, __get__width, __get__height, __get__x, __get__y, dispatchEvent, __get__scaleX, __get__scaleY, __get__scrubbing, _uiMgr, __set__autoPlay, __set__totalTime, __set__isLive, __set__contentPath, __get__playheadPercentage, __set__visibleVideoPlayerIndex, __set__activeVideoPlayerIndex, __get__activeVideoPlayerIndex, __get__autoPlay, __get__autoRewind, __get__autoSize, __get__ncMgr, __get__bitrate, _bufferingBar, __get__bufferingBar, __get__bufferingBarHidesAndDisablesOthers, _backButton, __get__backButton, __get__bufferTime, __get__contentPath, __get__cuePoints, _forwardButton, __get__forwardButton, __get__idleTimeout, __get__isLive, __get__maintainAspectRatio, _muteButton, __get__muteButton, _pauseButton, __get__pauseButton, _playButton, __get__playButton, __get__playheadTime, __get__playheadUpdateInterval, _playPauseButton, __get__playPauseButton, __get__progressInterval, __get__seekBar, _seekBar, _seekBarInterval, __get__seekBarInterval, _seekBarScrubTolerance, __get__seekBarScrubTolerance, __get__seekToPrevOffset, _skin, __get__skin, __get__skinAutoHide, __get__transform, _stopButton, __get__stopButton, __get__totalTime, __get__version_1_0_1, _visible, __get__visible, __get__visibleVideoPlayerIndex, __get__volume, _volumeBar, __get__volumeBar, _volumeBarInterval, __get__volumeBarInterval, _volumeBarScrubTolerance, __get__volumeBarScrubTolerance, _x, _y, attachMovie, createEmptyMovieClip, __get__state, __set__autoRewind, __set__autoSize, __set__backButton, __set__bitrate, __set__bufferTime, __get__buffering, __set__bufferingBar, __set__bufferingBarHidesAndDisablesOthers, __get__bytesLoaded, __get__bytesTotal, __set__cuePoints, __set__forwardButton, __set__height, __set__idleTimeout, __get__isRTMP, __set__maintainAspectRatio, __get__metadata, __get__metadataLoaded, __set__muteButton, __set__pauseButton, __get__paused, __set__playButton, __set__playPauseButton, __set__playheadPercentage, __set__playheadTime, __set__playheadUpdateInterval, __get__playing, __get__preferredHeight, __get__preferredWidth, __set__progressInterval, __set__scaleX, __set__scaleY, __set__seekBar, __set__seekBarInterval, __set__seekBarScrubTolerance, __set__seekToPrevOffset, __set__skin, __set__skinAutoHide, __get__stateResponsive, __set__stopButton, __get__stopped, __set__transform, __set__version_1_0_1, __set__visible, __set__volume, __set__volumeBar, __set__volumeBarInterval, __set__volumeBarScrubTolerance, __set__width, __set__x, __set__y;
    function FLVPlayback()
    {
        super();
        mx.events.EventDispatcher.initialize(this);
        if (_autoPlay == undefined)
        {
            _autoPlay = true;
        } // end if
        if (_autoRewind == undefined)
        {
            _autoRewind = true;
        } // end if
        if (_autoSize == undefined)
        {
            _autoSize = false;
        } // end if
        if (_bufferTime == undefined)
        {
            _bufferTime = 1.000000E-001;
        } // end if
        if (_contentPath == undefined)
        {
            _contentPath = "";
        } // end if
        if (_cuePoints == undefined)
        {
            _cuePoints = null;
        } // end if
        if (_idleTimeout == undefined)
        {
            _idleTimeout = mx.video.VideoPlayer.DEFAULT_IDLE_TIMEOUT_INTERVAL;
        } // end if
        if (_isLive == undefined)
        {
            _isLive = false;
        } // end if
        if (_aspectRatio == undefined)
        {
            _aspectRatio = true;
        } // end if
        if (_seekToPrevOffset == undefined)
        {
            _seekToPrevOffset = mx.video.FLVPlayback.SEEK_TO_PREV_OFFSET_DEFAULT;
        } // end if
        if (_playheadUpdateInterval == undefined)
        {
            _playheadUpdateInterval = mx.video.VideoPlayer.DEFAULT_UPDATE_PROGRESS_INTERVAL;
        } // end if
        if (_progressInterval == undefined)
        {
            _progressInterval = mx.video.VideoPlayer.DEFAULT_UPDATE_TIME_INTERVAL;
        } // end if
        if (_totalTime == undefined)
        {
            _totalTime = 0;
        } // end if
        if (_transform == undefined)
        {
            _transform = null;
        } // end if
        if (_volume == undefined)
        {
            _volume = 100;
        } // end if
        if (_skinAutoHide == undefined)
        {
            _skinAutoHide = false;
        } // end if
        if (_bufferingBarHides == undefined)
        {
            _bufferingBarHides = false;
        } // end if
        _origHeight = _prevHeight = __height = _height;
        _origWidth = _prevWidth = __width = _width;
        _scaleX = 100;
        _scaleY = 100;
        _xscale = 100;
        _yscale = 100;
        _preSeekTime = -1;
        _firstStreamReady = false;
        _firstStreamShown = false;
        this.createUIManager();
        _activeVP = 0;
        _visibleVP = 0;
        _topVP = 0;
        _vp = new Array();
        _vpState = new Array();
        _cpMgr = new Array();
        this.createVideoPlayer(0);
        _vp[0].visible = false;
        _vp[0].volume = 0;
        boundingBox_mc._visible = false;
        boundingBox_mc.unloadMovie();
        delete this.boundingBox_mc;
        if (_global.isLivePreview)
        {
            this.createLivePreviewMovieClip();
            this.setSize(__width, __height);
        } // end if
        _cpMgr[0].processCuePointsProperty(_cuePoints);
        delete this._cuePoints;
        _cuePoints = null;
    } // End of the function
    function setSize(w, h)
    {
        if (_global.isLivePreview)
        {
            if (preview_mc == undefined)
            {
                this.createLivePreviewMovieClip();
            } // end if
            preview_mc.box_mc._width = w;
            preview_mc.box_mc._height = h;
            if (preview_mc.box_mc._width < preview_mc.icon_mc._width || preview_mc.box_mc._height < preview_mc.icon_mc._height)
            {
                preview_mc.icon_mc._visible = false;
            }
            else
            {
                preview_mc.icon_mc._visible = true;
                preview_mc.icon_mc._x = (preview_mc.box_mc._width - preview_mc.icon_mc._width) / 2;
                preview_mc.icon_mc._y = (preview_mc.box_mc._height - preview_mc.icon_mc._height) / 2;
            } // end if
        } // end else if
        if (w == this.__get__width() && h == this.__get__height())
        {
            return;
        } // end if
        _prevWidth = __width = w;
        _prevHeight = __height = h;
        for (var _loc3 = 0; _loc3 < _vp.length; ++_loc3)
        {
            if (_vp[_loc3] != undefined)
            {
                _vp[_loc3].setSize(w, h);
            } // end if
        } // end of for
        this.dispatchEvent({type: "resize", x: this.__get__x(), y: this.__get__y(), width: w, height: h});
    } // End of the function
    function setScale(xs, ys)
    {
        if (xs == this.__get__scaleX() && ys == this.__get__scaleY())
        {
            return;
        } // end if
        _scaleX = xs;
        _scaleY = ys;
        for (var _loc2 = 0; _loc2 < _vp.length; ++_loc2)
        {
            if (_vp[_loc2] != undefined)
            {
                _vp[_loc2].setSize(_origWidth * xs / 100, _origHeight * ys / 100);
            } // end if
        } // end of for
        this.dispatchEvent({type: "resize", x: this.__get__x(), y: this.__get__y(), width: this.__get__width(), height: this.__get__height()});
    } // End of the function
    function handleEvent(e)
    {
        var _loc3 = e.state;
        if (e.state != undefined && e.target._name == _visibleVP && this.__get__scrubbing())
        {
            _loc3 = mx.video.FLVPlayback.SEEKING;
        } // end if
        if (e.type == "metadataReceived")
        {
            _cpMgr[e.target._name].processFLVCuePoints(e.info.cuePoints);
            this.dispatchEvent({type: e.type, info: e.info, vp: e.target._name});
        }
        else if (e.type == "cuePoint")
        {
            if (_cpMgr[e.target._name].isFLVCuePointEnabled(e.info))
            {
                this.dispatchEvent({type: e.type, info: e.info, vp: e.target._name});
            } // end if
        }
        else if (e.type == "rewind")
        {
            this.dispatchEvent({type: e.type, auto: true, state: _loc3, playheadTime: e.playheadTime, vp: e.target._name});
            _cpMgr[e.target._name].resetASCuePointIndex(e.playheadTime);
        }
        else if (e.type == "resize")
        {
            this.dispatchEvent({type: e.type, x: this.__get__x(), y: this.__get__y(), width: this.__get__width(), height: this.__get__height(), auto: true, vp: e.target._name});
            _prevWidth = __width;
            _prevHeight = __height;
        }
        else if (e.type == "playheadUpdate")
        {
            this.dispatchEvent({type: e.type, state: _loc3, playheadTime: e.playheadTime, vp: e.target._name});
            if (_preSeekTime >= 0 && e.target.state != mx.video.FLVPlayback.SEEKING)
            {
                var _loc5 = _preSeekTime;
                _preSeekTime = -1;
                _cpMgr[e.target._name].resetASCuePointIndex(e.playheadTime);
                this.dispatchEvent({type: "seek", state: _loc3, playheadTime: e.playheadTime, vp: e.target._name});
                if (_loc5 < e.playheadTime)
                {
                    this.dispatchEvent({type: "fastForward", state: _loc3, playheadTime: e.playheadTime, vp: e.target._name});
                }
                else if (_loc5 > e.playheadTime)
                {
                    this.dispatchEvent({type: "rewind", auto: false, state: _loc3, playheadTime: e.playheadTime, vp: e.target._name});
                } // end if
            } // end else if
            _cpMgr[e.target._name].dispatchASCuePoints();
        }
        else if (e.type == "stateChange")
        {
            var _loc4 = e.target._name;
            if (_loc4 == _visibleVP && this.__get__scrubbing())
            {
                return;
            } // end if
            if (e.state == mx.video.VideoPlayer.RESIZING)
            {
                return;
            } // end if
            if (_vpState[_loc4].prevState == mx.video.FLVPlayback.LOADING && _vpState[_loc4].autoPlay && e.state == mx.video.FLVPlayback.STOPPED)
            {
                return;
            } // end if
            _vpState[_loc4].prevState = e.state;
            this.dispatchEvent({type: e.type, state: _loc3, playheadTime: e.playheadTime, vp: e.target._name});
            if (_vp[e.target._name].state != _loc3)
            {
                return;
            } // end if
            switch (_loc3)
            {
                case mx.video.FLVPlayback.BUFFERING:
                {
                    this.dispatchEvent({type: "buffering", state: _loc3, playheadTime: e.playheadTime, vp: e.target._name});
                    break;
                } 
                case mx.video.FLVPlayback.PAUSED:
                {
                    this.dispatchEvent({type: "paused", state: _loc3, playheadTime: e.playheadTime, vp: e.target._name});
                    break;
                } 
                case mx.video.FLVPlayback.PLAYING:
                {
                    this.dispatchEvent({type: "playing", state: _loc3, playheadTime: e.playheadTime, vp: e.target._name});
                    break;
                } 
                case mx.video.FLVPlayback.STOPPED:
                {
                    this.dispatchEvent({type: "stopped", state: _loc3, playheadTime: e.playheadTime, vp: e.target._name});
                    break;
                } 
            } // End of switch
        }
        else if (e.type == "progress")
        {
            this.dispatchEvent({type: e.type, bytesLoaded: e.bytesLoaded, bytesTotal: e.bytesTotal, vp: e.target._name});
        }
        else if (e.type == "ready")
        {
            _loc4 = e.target._name;
            if (!_firstStreamReady)
            {
                if (_loc4 == _visibleVP)
                {
                    _firstStreamReady = true;
                    if (_uiMgr.__get__skinReady() && !_firstStreamShown)
                    {
                        _uiMgr.__set__visible(true);
                        this.showFirstStream();
                    } // end if
                } // end if
            }
            else if (_firstStreamShown && _loc3 == mx.video.FLVPlayback.STOPPED && _vpState[_loc4].autoPlay)
            {
                _vp[_loc4].play();
            } // end else if
            this.dispatchEvent({type: e.type, state: _loc3, playheadTime: e.playheadTime, vp: e.target._name});
        }
        else if (e.type == "close" || e.type == "complete")
        {
            this.dispatchEvent({type: e.type, state: _loc3, playheadTime: e.playheadTime, vp: e.target._name});
        } // end else if
    } // End of the function
    function load(contentPath, totalTime, isLive)
    {
        if (_vp[_activeVP] == undefined)
        {
            return;
        } // end if
        if (contentPath == undefined || contentPath == null || contentPath == "")
        {
            return;
        } // end if
        this.__set__autoPlay(false);
        if (totalTime != undefined)
        {
            this.__set__totalTime(totalTime);
        } // end if
        if (isLive != undefined)
        {
            this.__set__isLive(isLive);
        } // end if
        this.__set__contentPath(contentPath);
    } // End of the function
    function play(contentPath, totalTime, isLive)
    {
        if (_vp[_activeVP] == undefined)
        {
            return;
        } // end if
        if (contentPath == undefined)
        {
            _vp[_activeVP].play();
        }
        else
        {
            this.__set__autoPlay(true);
            if (totalTime != undefined)
            {
                this.__set__totalTime(totalTime);
            } // end if
            if (isLive != undefined)
            {
                this.__set__isLive(isLive);
            } // end if
            this.__set__contentPath(contentPath);
        } // end else if
    } // End of the function
    function pause()
    {
        if (_vp[_activeVP] == undefined)
        {
            return;
        } // end if
        _vp[_activeVP].pause();
    } // End of the function
    function stop()
    {
        if (_vp[_activeVP] == undefined)
        {
            return;
        } // end if
        _vp[_activeVP].stop();
    } // End of the function
    function seek(time)
    {
        if (_vp[_activeVP] == undefined)
        {
            return;
        } // end if
        _preSeekTime = playheadTime;
        _vp[_activeVP].seek(time);
    } // End of the function
    function seekSeconds(time)
    {
        this.seek(time);
    } // End of the function
    function seekPercent(percent)
    {
        if (_vp[_activeVP] == undefined)
        {
            return;
        } // end if
        if (percent < 0 || percent > 100 || _vp[_activeVP].totalTime == undefined || _vp[_activeVP].totalTime == null || _vp[_activeVP].totalTime <= 0)
        {
            throw new mx.video.VideoError(mx.video.VideoError.INVALID_SEEK);
        } // end if
        this.seek(_vp[_activeVP].totalTime * percent / 100);
    } // End of the function
    function get playheadPercentage()
    {
        if (_vp[_activeVP].totalTime == undefined || _vp[_activeVP].totalTime == null || _vp[_activeVP].totalTime <= 0)
        {
            return;
        } // end if
        return (_vp[_activeVP].playheadTime / _vp[_activeVP].totalTime * 100);
    } // End of the function
    function set playheadPercentage(percent)
    {
        this.seekPercent(percent);
        //return (this.playheadPercentage());
        null;
    } // End of the function
    function seekToNavCuePoint(timeNameOrCuePoint)
    {
        var _loc3;
        switch (typeof(timeNameOrCuePoint))
        {
            case "string":
            {
                _loc3 = {name: timeNameOrCuePoint};
                break;
            } 
            case "number":
            {
                _loc3 = {time: timeNameOrCuePoint};
                break;
            } 
            case "object":
            {
                _loc3 = timeNameOrCuePoint;
                break;
            } 
        } // End of switch
        if (_loc3.name == null || _loc3.name == undefined || typeof(_loc3.name) != "string")
        {
            this.seekToNextNavCuePoint(_loc3.time);
            return;
        } // end if
        if (isNaN(_loc3.time))
        {
            _loc3.time = 0;
        } // end if
        for (var _loc2 = this.findNearestCuePoint(timeNameOrCuePoint, mx.video.FLVPlayback.NAVIGATION); _loc2 != null && (_loc2.time < _loc3.time || !this.isFLVCuePointEnabled(_loc2)); _loc2 = this.findNextCuePointWithName(_loc2))
        {
        } // end of for
        if (_loc2 == null)
        {
            throw new mx.video.VideoError(mx.video.VideoError.INVALID_SEEK);
        } // end if
        this.seek(_loc2.time);
    } // End of the function
    function seekToNextNavCuePoint(time)
    {
        if (_vp[_activeVP] == undefined)
        {
            return;
        } // end if
        if (isNaN(time) || time < 0)
        {
            time = _vp[_activeVP].playheadTime + 1.000000E-003;
        } // end if
        var _loc3;
        _loc3 = this.findNearestCuePoint(time, mx.video.FLVPlayback.NAVIGATION);
        if (_loc3 == null)
        {
            this.seek(_vp[_activeVP].totalTime);
            return;
        } // end if
        var _loc2 = _loc3.index;
        if (_loc3.time < time)
        {
        } // end if
        for (var ++_loc2; _loc2 < _loc3.array.length && !this.isFLVCuePointEnabled(_loc3.array[_loc2]); ++_loc2)
        {
        } // end of for
        if (_loc2 >= _loc3.array.length)
        {
            var _loc5 = _vp[_activeVP].totalTime;
            if (_loc3.array[_loc3.array.length - 1].time > _loc5)
            {
                _loc5 = _loc3.array[_loc3.array.length - 1];
            } // end if
            this.seek(_loc5);
        }
        else
        {
            this.seek(_loc3.array[_loc2].time);
        } // end else if
    } // End of the function
    function seekToPrevNavCuePoint(time)
    {
        if (_vp[_activeVP] == undefined)
        {
            return;
        } // end if
        if (isNaN(time) || time < 0)
        {
            time = _vp[_activeVP].playheadTime;
        } // end if
        var _loc3 = this.findNearestCuePoint(time, mx.video.FLVPlayback.NAVIGATION);
        if (_loc3 == null)
        {
            this.seek(0);
            return;
        } // end if
        for (var _loc2 = _loc3.index; _loc2 >= 0 && (!this.isFLVCuePointEnabled(_loc3.array[_loc2]) || _loc3.array[_loc2].time >= time - _seekToPrevOffset); --_loc2)
        {
        } // end of for
        if (_loc2 < 0)
        {
            this.seek(0);
        }
        else
        {
            this.seek(_loc3.array[_loc2].time);
        } // end else if
    } // End of the function
    function addASCuePoint(timeOrCuePoint, name, parameters)
    {
        return (_cpMgr[_activeVP].addASCuePoint(timeOrCuePoint, name, parameters));
    } // End of the function
    function removeASCuePoint(timeNameOrCuePoint)
    {
        return (_cpMgr[_activeVP].removeASCuePoint(timeNameOrCuePoint));
    } // End of the function
    function findCuePoint(timeNameOrCuePoint, type)
    {
        switch (type)
        {
            case "event":
            {
                return (_cpMgr[_activeVP].getCuePoint(_cpMgr[_activeVP].eventCuePoints, false, timeNameOrCuePoint));
            } 
            case "navigation":
            {
                return (_cpMgr[_activeVP].getCuePoint(_cpMgr[_activeVP].navCuePoints, false, timeNameOrCuePoint));
            } 
            case "flv":
            {
                return (_cpMgr[_activeVP].getCuePoint(_cpMgr[_activeVP].flvCuePoints, false, timeNameOrCuePoint));
            } 
            case "actionscript":
            {
                return (_cpMgr[_activeVP].getCuePoint(_cpMgr[_activeVP].asCuePoints, false, timeNameOrCuePoint));
            } 
            case "all":
        } // End of switch
        return (_cpMgr[_activeVP].getCuePoint(_cpMgr[_activeVP].allCuePoints, false, timeNameOrCuePoint));
    } // End of the function
    function findNearestCuePoint(timeNameOrCuePoint, type)
    {
        switch (type)
        {
            case "event":
            {
                return (_cpMgr[_activeVP].getCuePoint(_cpMgr[_activeVP].eventCuePoints, true, timeNameOrCuePoint));
            } 
            case "navigation":
            {
                return (_cpMgr[_activeVP].getCuePoint(_cpMgr[_activeVP].navCuePoints, true, timeNameOrCuePoint));
            } 
            case "flv":
            {
                return (_cpMgr[_activeVP].getCuePoint(_cpMgr[_activeVP].flvCuePoints, true, timeNameOrCuePoint));
            } 
            case "actionscript":
            {
                return (_cpMgr[_activeVP].getCuePoint(_cpMgr[_activeVP].asCuePoints, true, timeNameOrCuePoint));
            } 
            case "all":
        } // End of switch
        return (_cpMgr[_activeVP].getCuePoint(_cpMgr[_activeVP].allCuePoints, true, timeNameOrCuePoint));
    } // End of the function
    function findNextCuePointWithName(cuePoint)
    {
        return (_cpMgr[_activeVP].getNextCuePointWithName(cuePoint));
    } // End of the function
    function setFLVCuePointEnabled(enabled, timeNameOrCuePoint)
    {
        return (_cpMgr[_activeVP].setFLVCuePointEnabled(enabled, timeNameOrCuePoint));
    } // End of the function
    function isFLVCuePointEnabled(timeNameOrCuePoint)
    {
        return (_cpMgr[_activeVP].isFLVCuePointEnabled(timeNameOrCuePoint));
    } // End of the function
    function getNextHighestDepth()
    {
        var _loc2 = super.getNextHighestDepth();
        return (_loc2 < 1000 ? (1000) : (_loc2));
    } // End of the function
    function bringVideoPlayerToFront(index)
    {
        if (index == _topVP || _vp[index] == undefined)
        {
            return;
        } // end if
        _vp[_topVP].swapDepths(_vp[index].getDepth());
        _topVP = index;
    } // End of the function
    function getVideoPlayer(index)
    {
        return (_vp[index]);
    } // End of the function
    function closeVideoPlayer(index)
    {
        if (_vp[index] == undefined)
        {
            return;
        } // end if
        if (index == 0)
        {
            throw new mx.video.VideoError(mx.video.VideoError.DELETE_DEFAULT_PLAYER);
        } // end if
        if (_visibleVP == index)
        {
            this.__set__visibleVideoPlayerIndex(0);
        } // end if
        if (_activeVP == index)
        {
            this.__set__activeVideoPlayerIndex(0);
        } // end if
        _vp[index].close();
        _vp[index].unloadMovie();
        delete _vp[index];
        _vp[index] = undefined;
    } // End of the function
    function get activeVideoPlayerIndex()
    {
        return (_activeVP);
    } // End of the function
    function set activeVideoPlayerIndex(i)
    {
        if (_activeVP == i)
        {
            return;
        } // end if
        if (_vp[_activeVP].onEnterFrame != undefined)
        {
            this.doContentPathConnect();
        } // end if
        _activeVP = i;
        if (_vp[_activeVP] == undefined)
        {
            this.createVideoPlayer(_activeVP);
            _vp[_activeVP].visible = false;
            _vp[_activeVP].volume = 0;
        } // end if
        //return (this.activeVideoPlayerIndex());
        null;
    } // End of the function
    function get autoPlay()
    {
        if (_vpState[_activeVP] == undefined)
        {
            return (_autoPlay);
        } // end if
        return (_vpState[_activeVP].autoPlay);
    } // End of the function
    function set autoPlay(flag)
    {
        if (_activeVP == 0 || _activeVP == undefined)
        {
            _autoPlay = flag;
        } // end if
        _vpState[_activeVP].autoPlay = flag;
        //return (this.autoPlay());
        null;
    } // End of the function
    function get autoRewind()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (_autoRewind);
        } // end if
        return (_vp[_activeVP].autoRewind);
    } // End of the function
    function set autoRewind(flag)
    {
        if (_activeVP == 0 || _activeVP == undefined)
        {
            _autoRewind = flag;
        } // end if
        _vp[_activeVP].autoRewind = flag;
        //return (this.autoRewind());
        null;
    } // End of the function
    function get autoSize()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (_autoSize);
        } // end if
        return (_vp[_activeVP].autoSize);
    } // End of the function
    function set autoSize(flag)
    {
        if (_activeVP == 0 || _activeVP == undefined)
        {
            _autoSize = flag;
        } // end if
        _vp[_activeVP].autoSize = flag;
        //return (this.autoSize());
        null;
    } // End of the function
    function get bitrate()
    {
        //return (this.ncMgr().getBitrate());
    } // End of the function
    function set bitrate(b)
    {
        this.__get__ncMgr().setBitrate(b);
        //return (this.bitrate());
        null;
    } // End of the function
    function get buffering()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (false);
        } // end if
        return (_vp[_activeVP].state == mx.video.FLVPlayback.BUFFERING);
    } // End of the function
    function get bufferingBar()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _bufferingBar = _uiMgr.getControl(mx.video.UIManager.BUFFERING_BAR);
        } // end if
        return (_bufferingBar);
    } // End of the function
    function set bufferingBar(s)
    {
        _bufferingBar = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.setControl(mx.video.UIManager.BUFFERING_BAR, s);
        } // end if
        //return (this.bufferingBar());
        null;
    } // End of the function
    function get bufferingBarHidesAndDisablesOthers()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _bufferingBarHides = _uiMgr.bufferingBarHidesAndDisablesOthers;
        } // end if
        return (_bufferingBarHides);
    } // End of the function
    function set bufferingBarHidesAndDisablesOthers(b)
    {
        _bufferingBarHides = b;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.__set__bufferingBarHidesAndDisablesOthers(b);
        } // end if
        //return (this.bufferingBarHidesAndDisablesOthers());
        null;
    } // End of the function
    function get backButton()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _backButton = _uiMgr.getControl(mx.video.UIManager.BACK_BUTTON);
        } // end if
        return (_backButton);
    } // End of the function
    function set backButton(s)
    {
        _backButton = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.setControl(mx.video.UIManager.BACK_BUTTON, s);
        } // end if
        //return (this.backButton());
        null;
    } // End of the function
    function get bufferTime()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (_bufferTime);
        } // end if
        return (_vp[_activeVP].bufferTime);
    } // End of the function
    function set bufferTime(aTime)
    {
        if (_activeVP == 0 || _activeVP == undefined)
        {
            _bufferTime = aTime;
        } // end if
        _vp[_activeVP].bufferTime = aTime;
        //return (this.bufferTime());
        null;
    } // End of the function
    function get bytesLoaded()
    {
        return (_vp[_activeVP].bytesLoaded);
    } // End of the function
    function get bytesTotal()
    {
        return (_vp[_activeVP].bytesTotal);
    } // End of the function
    function get contentPath()
    {
        if (_vp[_activeVP] == undefined || _vp[_activeVP].onEnterFrame != undefined)
        {
            return (_contentPath);
        } // end if
        return (_vp[_activeVP].url);
    } // End of the function
    function set contentPath(url)
    {
        if (_global.isLivePreview)
        {
            return;
        } // end if
        if (_vp[_activeVP] == undefined)
        {
            if (url == _contentPath)
            {
                return;
            } // end if
            _contentPath = url;
        }
        else
        {
            if (_vp[_activeVP].url == url)
            {
                return;
            } // end if
            _vpState[_activeVP].minProgressPercent = undefined;
            if (_vp[_activeVP].onEnterFrame != undefined)
            {
                delete _vp[_activeVP].onEnterFrame;
                _vp[_activeVP].onEnterFrame = undefined;
            } // end if
            _cpMgr[_activeVP].reset();
            if (_vpState[_activeVP].autoPlay && _firstStreamShown)
            {
                _vp[_activeVP].play(url, _vpState[_activeVP].isLive, _vpState[_activeVP].totalTime);
            }
            else
            {
                _vp[_activeVP].load(url, _vpState[_activeVP].isLive, _vpState[_activeVP].totalTime);
            } // end else if
            _vpState[_activeVP].isLiveSet = false;
            _vpState[_activeVP].totalTimeSet = false;
        } // end else if
        //return (this.contentPath());
        null;
    } // End of the function
    function set cuePoints(cp)
    {
        if (_cuePoints != undefined)
        {
            return;
        } // end if
        _cuePoints = cp;
        //return (this.cuePoints());
        null;
    } // End of the function
    function get forwardButton()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _forwardButton = _uiMgr.getControl(mx.video.UIManager.FORWARD_BUTTON);
        } // end if
        return (_forwardButton);
    } // End of the function
    function set forwardButton(s)
    {
        _forwardButton = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.setControl(mx.video.UIManager.FORWARD_BUTTON, s);
        } // end if
        //return (this.forwardButton());
        null;
    } // End of the function
    function get height()
    {
        if (_global.isLivePreview)
        {
            return (__height);
        } // end if
        if (_vp[_visibleVP] != undefined)
        {
            __height = _vp[_visibleVP].height;
        } // end if
        return (__height);
    } // End of the function
    function set height(h)
    {
        this.setSize(this.__get__width(), h);
        //return (this.height());
        null;
    } // End of the function
    function get idleTimeout()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (_idleTimeout);
        } // end if
        return (_vp[_activeVP].idleTimeout);
    } // End of the function
    function set idleTimeout(aTime)
    {
        if (_activeVP == 0 || _activeVP == undefined)
        {
            _idleTimeout = aTime;
        } // end if
        _vp[_activeVP].idleTimeout = aTime;
        //return (this.idleTimeout());
        null;
    } // End of the function
    function get isRTMP()
    {
        if (_global.isLivePreview)
        {
            return (true);
        } // end if
        if (_vp[_activeVP] == undefined)
        {
            return;
        } // end if
        return (_vp[_activeVP].isRTMP);
    } // End of the function
    function get isLive()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (_isLive);
        }
        else if (_vpState[_activeVP].isLiveSet)
        {
            return (_vpState[_activeVP].isLive);
        }
        else
        {
            return (_vp[_activeVP].isLive);
        } // end else if
    } // End of the function
    function set isLive(flag)
    {
        if (_activeVP == 0 || _activeVP == undefined)
        {
            _isLive = flag;
        } // end if
        _vpState[_activeVP].isLive = flag;
        _vpState[_activeVP].isLiveSet = true;
        //return (this.isLive());
        null;
    } // End of the function
    function get maintainAspectRatio()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (_aspectRatio);
        } // end if
        return (_vp[_activeVP].maintainAspectRatio);
    } // End of the function
    function set maintainAspectRatio(flag)
    {
        if (_activeVP == 0 || _activeVP == undefined)
        {
            _aspectRatio = flag;
        } // end if
        _vp[_activeVP].maintainAspectRatio = flag;
        //return (this.maintainAspectRatio());
        null;
    } // End of the function
    function get metadata()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (null);
        } // end if
        return (_vp[_activeVP].metadata);
    } // End of the function
    function get metadataLoaded()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (false);
        } // end if
        return (_cpMgr[_activeVP].metadataLoaded);
    } // End of the function
    function get muteButton()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _muteButton = _uiMgr.getControl(mx.video.UIManager.MUTE_BUTTON);
        } // end if
        return (_muteButton);
    } // End of the function
    function set muteButton(s)
    {
        _muteButton = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.setControl(mx.video.UIManager.MUTE_BUTTON, s);
        } // end if
        //return (this.muteButton());
        null;
    } // End of the function
    function get ncMgr()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (null);
        } // end if
        return (_vp[_activeVP].ncMgr);
    } // End of the function
    function get pauseButton()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _pauseButton = _uiMgr.getControl(mx.video.UIManager.PAUSE_BUTTON);
        } // end if
        return (_pauseButton);
    } // End of the function
    function set pauseButton(s)
    {
        _pauseButton = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.setControl(mx.video.UIManager.PAUSE_BUTTON, s);
        } // end if
        //return (this.pauseButton());
        null;
    } // End of the function
    function get paused()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (false);
        } // end if
        return (_vp[_activeVP].state == mx.video.FLVPlayback.PAUSED);
    } // End of the function
    function get playButton()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _playButton = _uiMgr.getControl(mx.video.UIManager.PLAY_BUTTON);
        } // end if
        return (_playButton);
    } // End of the function
    function set playButton(s)
    {
        _playButton = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.setControl(mx.video.UIManager.PLAY_BUTTON, s);
        } // end if
        //return (this.playButton());
        null;
    } // End of the function
    function get playheadTime()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (0);
        } // end if
        return (_vp[_activeVP].playheadTime);
    } // End of the function
    function set playheadTime(position)
    {
        this.seek(position);
        //return (this.playheadTime());
        null;
    } // End of the function
    function get playheadUpdateInterval()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (_playheadUpdateInterval);
        } // end if
        return (_vp[_activeVP].playheadUpdateInterval);
    } // End of the function
    function set playheadUpdateInterval(aTime)
    {
        if (_activeVP == 0 || _activeVP == undefined)
        {
            _playheadUpdateInterval = aTime;
        } // end if
        _cpMgr[_activeVP].playheadUpdateInterval = aTime;
        _vp[_activeVP].playheadUpdateInterval = aTime;
        //return (this.playheadUpdateInterval());
        null;
    } // End of the function
    function get playing()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (false);
        } // end if
        return (_vp[_activeVP].state == mx.video.FLVPlayback.PLAYING);
    } // End of the function
    function get playPauseButton()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _playPauseButton = _uiMgr.getControl(mx.video.UIManager.PLAY_PAUSE_BUTTON);
        } // end if
        return (_playPauseButton);
    } // End of the function
    function set playPauseButton(s)
    {
        _playPauseButton = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.setControl(mx.video.UIManager.PLAY_PAUSE_BUTTON, s);
        } // end if
        //return (this.playPauseButton());
        null;
    } // End of the function
    function get preferredHeight()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (0);
        } // end if
        return (_vp[_activeVP].videoHeight);
    } // End of the function
    function get preferredWidth()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (0);
        } // end if
        return (_vp[_activeVP].videoWidth);
    } // End of the function
    function get progressInterval()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (_progressInterval);
        } // end if
        return (_vp[_activeVP].progressInterval);
    } // End of the function
    function set progressInterval(aTime)
    {
        if (_activeVP == 0 || _activeVP == undefined)
        {
            _progressInterval = aTime;
        } // end if
        _vp[_activeVP].progressInterval = aTime;
        //return (this.progressInterval());
        null;
    } // End of the function
    function get scaleX()
    {
        if (_vp[_visibleVP] != undefined)
        {
            _scaleX = _vp[_visibleVP].width / _origWidth * 100;
        } // end if
        return (_scaleX);
    } // End of the function
    function set scaleX(xs)
    {
        this.setScale(xs, this.__get__scaleY());
        //return (this.scaleX());
        null;
    } // End of the function
    function get scaleY()
    {
        if (_vp[_visibleVP] != undefined)
        {
            _scaleY = _vp[_visibleVP].height / _origHeight * 100;
        } // end if
        return (_scaleY);
    } // End of the function
    function set scaleY(ys)
    {
        this.setScale(this.__get__scaleX(), ys);
        //return (this.scaleY());
        null;
    } // End of the function
    function get scrubbing()
    {
        var _loc2 = this.__get__seekBar();
        if (_loc2 == undefined || _loc2.isDragging == undefined)
        {
            return (false);
        } // end if
        return (_loc2.isDragging);
    } // End of the function
    function get seekBar()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _seekBar = _uiMgr.getControl(mx.video.UIManager.SEEK_BAR);
        } // end if
        return (_seekBar);
    } // End of the function
    function set seekBar(s)
    {
        _seekBar = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.setControl(mx.video.UIManager.SEEK_BAR, s);
        } // end if
        //return (this.seekBar());
        null;
    } // End of the function
    function get seekBarInterval()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _seekBarInterval = _uiMgr.seekBarInterval;
        } // end if
        return (_seekBarInterval);
    } // End of the function
    function set seekBarInterval(s)
    {
        _seekBarInterval = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.__set__seekBarInterval(_seekBarInterval);
        } // end if
        //return (this.seekBarInterval());
        null;
    } // End of the function
    function get seekBarScrubTolerance()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _seekBarScrubTolerance = _uiMgr.seekBarScrubTolerance;
        } // end if
        return (_seekBarScrubTolerance);
    } // End of the function
    function set seekBarScrubTolerance(s)
    {
        _seekBarScrubTolerance = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.__set__seekBarScrubTolerance(_seekBarScrubTolerance);
        } // end if
        //return (this.seekBarScrubTolerance());
        null;
    } // End of the function
    function get seekToPrevOffset()
    {
        return (_seekToPrevOffset);
    } // End of the function
    function set seekToPrevOffset(s)
    {
        _seekToPrevOffset = s;
        //return (this.seekToPrevOffset());
        null;
    } // End of the function
    function get skin()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _skin = _uiMgr.skin;
        } // end if
        return (_skin);
    } // End of the function
    function set skin(s)
    {
        _skin = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.__set__skin(s);
        } // end if
        //return (this.skin());
        null;
    } // End of the function
    function get skinAutoHide()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _skinAutoHide = _uiMgr.skinAutoHide;
        } // end if
        return (_skinAutoHide);
    } // End of the function
    function set skinAutoHide(b)
    {
        if (_global.isLivePreview)
        {
            return;
        } // end if
        _skinAutoHide = b;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.__set__skinAutoHide(b);
        } // end if
        //return (this.skinAutoHide());
        null;
    } // End of the function
    function get transform()
    {
        return (_transform);
    } // End of the function
    function set transform(s)
    {
        _transform = s;
        if (_vp[_activeVP] != undefined)
        {
            _vp[_activeVP].transform = _transform;
        } // end if
        //return (this.transform());
        null;
    } // End of the function
    function get state()
    {
        if (_global.isLivePreview)
        {
            return (mx.video.FLVPlayback.STOPPED);
        } // end if
        if (_vp[_activeVP] == undefined)
        {
            return (mx.video.FLVPlayback.DISCONNECTED);
        } // end if
        if (_activeVP == _visibleVP && this.__get__scrubbing())
        {
            return (mx.video.FLVPlayback.SEEKING);
        } // end if
        var _loc3 = _vp[_activeVP].state;
        if (_loc3 == mx.video.VideoPlayer.RESIZING)
        {
            return (mx.video.FLVPlayback.LOADING);
        } // end if
        if (_vpState[_activeVP].prevState == mx.video.FLVPlayback.LOADING && _vpState[_activeVP].autoPlay && _loc3 == mx.video.FLVPlayback.STOPPED)
        {
            return (mx.video.FLVPlayback.LOADING);
        } // end if
        return (_loc3);
    } // End of the function
    function get stateResponsive()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (false);
        } // end if
        return (_vp[_activeVP].stateResponsive);
    } // End of the function
    function get stopButton()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _stopButton = _uiMgr.getControl(mx.video.UIManager.STOP_BUTTON);
        } // end if
        return (_stopButton);
    } // End of the function
    function set stopButton(s)
    {
        _stopButton = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.setControl(mx.video.UIManager.STOP_BUTTON, s);
        } // end if
        //return (this.stopButton());
        null;
    } // End of the function
    function get stopped()
    {
        if (_vp[_activeVP] == undefined)
        {
            return (false);
        } // end if
        return (_vp[_activeVP].state == mx.video.FLVPlayback.STOPPED);
    } // End of the function
    function get totalTime()
    {
        if (_global.isLivePreview)
        {
            return (1);
        } // end if
        if (_vp[_activeVP] == undefined)
        {
            return (_totalTime);
        }
        else if (_vpState[_activeVP].totalTimeSet)
        {
            return (_vpState[_activeVP].totalTime);
        }
        else
        {
            return (_vp[_activeVP].totalTime);
        } // end else if
    } // End of the function
    function set totalTime(aTime)
    {
        if (_activeVP == 0 || _activeVP == undefined)
        {
            _totalTime = aTime;
        } // end if
        _vpState[_activeVP].totalTime = aTime;
        _vpState[_activeVP].totalTimeSet = true;
        //return (this.totalTime());
        null;
    } // End of the function
    function get version_1_0_1()
    {
        return ("");
    } // End of the function
    function set version_1_0_1(v)
    {
        //return (this.version_1_0_1());
        null;
    } // End of the function
    function get visible()
    {
        return (_visible);
    } // End of the function
    function set visible(v)
    {
        _visible = v;
        //return (this.visible());
        null;
    } // End of the function
    function get visibleVideoPlayerIndex()
    {
        return (_visibleVP);
    } // End of the function
    function set visibleVideoPlayerIndex(i)
    {
        if (_visibleVP == i)
        {
            return;
        } // end if
        var _loc2 = _visibleVP;
        if (_vp[i] == undefined)
        {
            this.createVideoPlayer(i);
        } // end if
        var _loc5 = _vp[i].height != _vp[_visibleVP].height || _vp[i].width != _vp[_visibleVP].width;
        _vp[_visibleVP].visible = false;
        _vp[_visibleVP].volume = 0;
        _visibleVP = i;
        if (_firstStreamShown)
        {
            _uiMgr.setupSkinAutoHide(_loc2);
            _vp[_visibleVP].visible = true;
            if (!this.__get__scrubbing())
            {
                _vp[_visibleVP].volume = _volume;
            } // end if
        }
        else if (_vp[_visibleVP].stateResponsive && _vp[_visibleVP].state != mx.video.FLVPlayback.DISCONNECTED && _uiMgr.__get__skinReady())
        {
            _uiMgr.__set__visible(true);
            _uiMgr.setupSkinAutoHide(_loc2);
            _firstStreamReady = true;
            this.showFirstStream();
        } // end else if
        if (_vp[_loc2].height != _vp[_visibleVP].height || _vp[_loc2].width != _vp[_visibleVP].width)
        {
            this.dispatchEvent({type: "resize", x: this.__get__x(), y: this.__get__y(), width: this.__get__width(), height: this.__get__height(), auto: false, vp: _visibleVP});
        } // end if
        _uiMgr.handleEvent({type: "stateChange", state: _vp[_visibleVP].state, vp: _visibleVP});
        _uiMgr.handleEvent({type: "playheadUpdate", playheadTime: _vp[_visibleVP].playheadTime, vp: _visibleVP});
        if (_vp[_visibleVP].isRTMP)
        {
            _uiMgr.handleEvent({type: "ready", vp: _visibleVP});
        }
        else
        {
            _uiMgr.handleEvent({type: "progress", bytesLoaded: _vp[_visibleVP].bytesLoaded, bytesTotal: _vp[_visibleVP].bytesTotal, vp: _visibleVP});
        } // end else if
        //return (this.visibleVideoPlayerIndex());
        null;
    } // End of the function
    function get volume()
    {
        return (_volume);
    } // End of the function
    function set volume(aVol)
    {
        if (_volume == aVol)
        {
            return;
        } // end if
        _volume = aVol;
        if (!this.__get__scrubbing())
        {
            _vp[_visibleVP].volume = _volume;
        } // end if
        this.dispatchEvent({type: "volumeUpdate", volume: aVol});
        //return (this.volume());
        null;
    } // End of the function
    function get volumeBar()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _volumeBar = _uiMgr.getControl(mx.video.UIManager.VOLUME_BAR);
        } // end if
        return (_volumeBar);
    } // End of the function
    function set volumeBar(s)
    {
        _volumeBar = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.setControl(mx.video.UIManager.VOLUME_BAR, s);
        } // end if
        //return (this.volumeBar());
        null;
    } // End of the function
    function get volumeBarInterval()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _volumeBarInterval = _uiMgr.volumeBarInterval;
        } // end if
        return (_volumeBarInterval);
    } // End of the function
    function set volumeBarInterval(s)
    {
        _volumeBarInterval = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.__set__volumeBarInterval(_volumeBarInterval);
        } // end if
        //return (this.volumeBarInterval());
        null;
    } // End of the function
    function get volumeBarScrubTolerance()
    {
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _volumeBarScrubTolerance = _uiMgr.volumeBarScrubTolerance;
        } // end if
        return (_volumeBarScrubTolerance);
    } // End of the function
    function set volumeBarScrubTolerance(s)
    {
        _volumeBarScrubTolerance = s;
        if (_uiMgr != null && _uiMgr != undefined)
        {
            _uiMgr.__set__volumeBarScrubTolerance(_volumeBarScrubTolerance);
        } // end if
        //return (this.volumeBarScrubTolerance());
        null;
    } // End of the function
    function get width()
    {
        if (_global.isLivePreview)
        {
            return (__width);
        } // end if
        if (_vp[_visibleVP] != undefined)
        {
            __width = _vp[_visibleVP].width;
        } // end if
        return (__width);
    } // End of the function
    function set width(w)
    {
        this.setSize(w, this.__get__height());
        //return (this.width());
        null;
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
    function createVideoPlayer(index)
    {
        if (_global.isLivePreview)
        {
            return;
        } // end if
        var _loc4 = this.__get__width();
        var _loc5 = this.__get__height();
        _vp[index] = (mx.video.VideoPlayer)(this.attachMovie("VideoPlayer", String(index), mx.video.FLVPlayback.VP_DEPTH_OFFSET + index));
        _vp[index].setSize(_loc4, _loc5);
        _topVP = index;
        _vp[index].autoRewind = _autoRewind;
        _vp[index].autoSize = _autoSize;
        _vp[index].bufferTime = _bufferTime;
        _vp[index].idleTimeout = _idleTimeout;
        _vp[index].maintainAspectRatio = _aspectRatio;
        _vp[index].playheadUpdateInterval = _playheadUpdateInterval;
        _vp[index].progressInterval = _progressInterval;
        _vp[index].transform = _transform;
        _vp[index].volume = _volume;
        if (index == 0)
        {
            _vpState[index] = {id: index, isLive: _isLive, isLiveSet: true, totalTime: _totalTime, totalTimeSet: true, autoPlay: _autoPlay};
            if (_contentPath != null && _contentPath != undefined && _contentPath != "")
            {
                _vp[index].onEnterFrame = mx.utils.Delegate.create(this, doContentPathConnect);
            } // end if
        }
        else
        {
            _vpState[index] = {id: index, isLive: false, isLiveSet: true, totalTime: 0, totalTimeSet: true, autoPlay: false};
        } // end else if
        _vp[index].addEventListener("resize", this);
        _vp[index].addEventListener("close", this);
        _vp[index].addEventListener("complete", this);
        _vp[index].addEventListener("cuePoint", this);
        _vp[index].addEventListener("playheadUpdate", this);
        _vp[index].addEventListener("progress", this);
        _vp[index].addEventListener("metadataReceived", this);
        _vp[index].addEventListener("stateChange", this);
        _vp[index].addEventListener("ready", this);
        _vp[index].addEventListener("rewind", this);
        _cpMgr[index] = new mx.video.CuePointManager(this, index);
        _cpMgr[index].playheadUpdateInterval = _playheadUpdateInterval;
    } // End of the function
    function createUIManager()
    {
        _uiMgr = new mx.video.UIManager(this);
        _uiMgr.__set__visible(false);
        if (_backButton != undefined && _backButton != null)
        {
            _uiMgr.setControl(mx.video.UIManager.BACK_BUTTON, _backButton);
        } // end if
        if (_bufferingBar != undefined && _bufferingBar != null)
        {
            _uiMgr.setControl(mx.video.UIManager.BUFFERING_BAR, _bufferingBar);
        } // end if
        _uiMgr.__set__bufferingBarHidesAndDisablesOthers(_bufferingBarHides);
        if (_forwardButton != undefined && _forwardButton != null)
        {
            _uiMgr.setControl(mx.video.UIManager.FORWARD_BUTTON, _forwardButton);
        } // end if
        if (_pauseButton != undefined && _pauseButton != null)
        {
            _uiMgr.setControl(mx.video.UIManager.PAUSE_BUTTON, _pauseButton);
        } // end if
        if (_playButton != undefined && _playButton != null)
        {
            _uiMgr.setControl(mx.video.UIManager.PLAY_BUTTON, _playButton);
        } // end if
        if (_playPauseButton != undefined && _playPauseButton != null)
        {
            _uiMgr.setControl(mx.video.UIManager.PLAY_PAUSE_BUTTON, _playPauseButton);
        } // end if
        if (_stopButton != undefined && _stopButton != null)
        {
            _uiMgr.setControl(mx.video.UIManager.STOP_BUTTON, _stopButton);
        } // end if
        if (_seekBar != undefined && _seekBar != null)
        {
            _uiMgr.setControl(mx.video.UIManager.SEEK_BAR, _seekBar);
        } // end if
        if (_seekBarInterval != undefined && _seekBarInterval != null)
        {
            _uiMgr.__set__seekBarInterval(_seekBarInterval);
        } // end if
        if (_seekBarScrubTolerance != undefined && _seekBarScrubTolerance != null)
        {
            _uiMgr.__set__seekBarScrubTolerance(_seekBarScrubTolerance);
        } // end if
        if (_skin != undefined && _skin != null)
        {
            _uiMgr.__set__skin(_skin);
        } // end if
        if (_skinAutoHide != undefined && _skinAutoHide != null)
        {
            _uiMgr.__set__skinAutoHide(_skinAutoHide);
        } // end if
        if (_muteButton != undefined && _muteButton != null)
        {
            _uiMgr.setControl(mx.video.UIManager.MUTE_BUTTON, _muteButton);
        } // end if
        if (_volumeBar != undefined && _volumeBar != null)
        {
            _uiMgr.setControl(mx.video.UIManager.VOLUME_BAR, _volumeBar);
        } // end if
        if (_volumeBarInterval != undefined && _volumeBarInterval != null)
        {
            _uiMgr.__set__volumeBarInterval(_volumeBarInterval);
        } // end if
        if (_volumeBarScrubTolerance != undefined && _volumeBarScrubTolerance != null)
        {
            _uiMgr.__set__volumeBarScrubTolerance(_volumeBarScrubTolerance);
        } // end if
    } // End of the function
    function createLivePreviewMovieClip()
    {
        preview_mc = this.createEmptyMovieClip("preview_mc", 10);
        preview_mc.createEmptyMovieClip("box_mc", 10);
        preview_mc.box_mc.beginFill(0);
        preview_mc.box_mc.moveTo(0, 0);
        preview_mc.box_mc.lineTo(0, 100);
        preview_mc.box_mc.lineTo(100, 100);
        preview_mc.box_mc.lineTo(100, 0);
        preview_mc.box_mc.lineTo(0, 0);
        preview_mc.box_mc.endFill();
        preview_mc.attachMovie("Icon", "icon_mc", 20);
    } // End of the function
    function doContentPathConnect()
    {
        delete _vp[0].onEnterFrame;
        _vp[0].onEnterFrame = undefined;
        if (_global.isLivePreview)
        {
            return;
        } // end if
        if (_vpState[0].autoPlay && _firstStreamShown)
        {
            _vp[0].play(_contentPath, _isLive, _totalTime);
        }
        else
        {
            _vp[0].load(_contentPath, _isLive, _totalTime);
        } // end else if
        _vpState[0].isLiveSet = false;
        _vpState[0].totalTimeSet = false;
    } // End of the function
    function showFirstStream()
    {
        _firstStreamShown = true;
        _vp[_visibleVP].visible = true;
        if (!this.__get__scrubbing())
        {
            _vp[_visibleVP].volume = _volume;
        } // end if
        for (var _loc2 = 0; _loc2 < _vp.length; ++_loc2)
        {
            if (_vp[_loc2] != undefined && _vp[_loc2].state == mx.video.FLVPlayback.STOPPED && _vpState[_loc2].autoPlay)
            {
                _vp[_loc2].play();
            } // end if
        } // end of for
    } // End of the function
    function _scrubStart()
    {
        var _loc2 = this.__get__playheadTime();
        _vp[_visibleVP].volume = 0;
        this.dispatchEvent({type: "stateChange", state: mx.video.FLVPlayback.SEEKING, playheadTime: _loc2, vp: _visibleVP});
        this.dispatchEvent({type: "scrubStart", state: mx.video.FLVPlayback.SEEKING, playheadTime: _loc2});
    } // End of the function
    function _scrubFinish()
    {
        var _loc3 = this.__get__playheadTime();
        var _loc2 = this.__get__state();
        _vp[_visibleVP].volume = _volume;
        if (_loc2 != mx.video.FLVPlayback.SEEKING)
        {
            this.dispatchEvent({type: "stateChange", state: _loc2, playheadTime: _loc3, vp: _visibleVP});
        } // end if
        this.dispatchEvent({type: "scrubFinish", state: _loc2, playheadTime: _loc3});
    } // End of the function
    function skinError(message)
    {
        if (_firstStreamReady && !_firstStreamShown)
        {
            this.showFirstStream();
        } // end if
        this.dispatchEvent({type: "skinError", message: message});
    } // End of the function
    function skinLoaded()
    {
        if (_firstStreamReady)
        {
            _uiMgr.__set__visible(true);
            if (!_firstStreamShown)
            {
                this.showFirstStream();
            } // end if
        }
        else if (_contentPath == undefined || _contentPath == null || _contentPath == "")
        {
            _uiMgr.__set__visible(true);
        } // end else if
        this.dispatchEvent({type: "skinLoaded"});
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
    static var ALL = "all";
    static var EVENT = "event";
    static var NAVIGATION = "navigation";
    static var FLV = "flv";
    static var ACTIONSCRIPT = "actionscript";
    static var VP_DEPTH_OFFSET = 100;
    static var SEEK_TO_PREV_OFFSET_DEFAULT = 1;
} // End of Class