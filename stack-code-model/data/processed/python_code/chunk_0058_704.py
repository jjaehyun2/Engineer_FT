
//Created by Action Script Viewer - http://www.buraks.com/asv
    class mx.video.NCManager implements mx.video.INCManager
    {
        var _timeoutIntervalId, _tryNCIntervalId, _timeout, _isRTMP, _serverName, _wrappedURL, _portNumber, _appName, _contentPath, _streamName, _streamLength, _streamWidth, _streamHeight, _streams, _autoSenseBW, _payload, _connTypeCounter, _bitrate, _owner, _nc, _protocol, _smilMgr, _ncUri, fallbackServerName, _tryNC;
        function NCManager () {
            initNCInfo();
            initOtherInfo();
            _timeoutIntervalId = 0;
            _tryNCIntervalId = 0;
            _timeout = DEFAULT_TIMEOUT;
        }
        function initNCInfo() {
            _isRTMP = undefined;
            _serverName = undefined;
            _wrappedURL = undefined;
            _portNumber = undefined;
            _appName = undefined;
        }
        function initOtherInfo() {
            _contentPath = undefined;
            _streamName = undefined;
            _streamLength = undefined;
            _streamWidth = undefined;
            _streamHeight = undefined;
            _streams = undefined;
            _autoSenseBW = false;
            _payload = 0;
            _connTypeCounter = 0;
            cleanConns();
        }
        function getTimeout() {
            return(_timeout);
        }
        function setTimeout(_arg2) {
            _timeout = _arg2;
            if (_timeoutIntervalId != 0) {
                clearInterval(_timeoutIntervalId);
                _timeoutIntervalId = setInterval(this, "_onFCSConnectTimeOut", _timeout);
            }
        }
        function getBitrate() {
            return(_bitrate);
        }
        function setBitrate(_arg2) {
            if ((_isRTMP == undefined) || (!_isRTMP)) {
                _bitrate = _arg2;
            }
        }
        function getVideoPlayer() {
            return(_owner);
        }
        function setVideoPlayer(_arg2) {
            _owner = _arg2;
        }
        function getNetConnection() {
            return(_nc);
        }
        function getStreamName() {
            return(_streamName);
        }
        function isRTMP() {
            return(_isRTMP);
        }
        function getStreamLength() {
            return(_streamLength);
        }
        function getStreamWidth() {
            return(_streamWidth);
        }
        function getStreamHeight() {
            return(_streamHeight);
        }
        function connectToURL(_arg4) {
            initOtherInfo();
            _contentPath = _arg4;
            if (((_contentPath == null) || (_contentPath == undefined)) || (_contentPath == "")) {
                throw new mx.video.VideoError(mx.video.VideoError.INVALID_CONTENT_PATH);
            }
            var _local2 = parseURL(_contentPath);
            if ((_local2.streamName == undefined) || (_local2.streamName == "")) {
                throw new mx.video.VideoError(mx.video.VideoError.INVALID_CONTENT_PATH, _arg4);
            }
            if (_local2.isRTMP) {
                var _local3 = canReuseOldConnection(_local2);
                _isRTMP = true;
                _protocol = _local2.protocol;
                _streamName = _local2.streamName;
                _serverName = _local2.serverName;
                _wrappedURL = _local2.wrappedURL;
                _portNumber = _local2.portNumber;
                _appName = _local2.appName;
                if ((((_appName == undefined) || (_appName == "")) || (_streamName == undefined)) || (_streamName == "")) {
                    throw new mx.video.VideoError(mx.video.VideoError.INVALID_CONTENT_PATH, _arg4);
                }
                _autoSenseBW = _streamName.indexOf(",") != -1;
                return(_local3 || (connectRTMP()));
            } else if (_local2.streamName.slice(-4).toLowerCase() == ".flv") {
                var _local3 = canReuseOldConnection(_local2);
                _isRTMP = false;
                _streamName = _local2.streamName;
                return(_local3 || (connectHTTP()));
            } else {
                _smilMgr = new mx.video.SMILManager(this);
                return(_smilMgr.connectXML(_local2.streamName));
            }
        }
        function connectAgain() {
            var _local2 = _appName.indexOf("/");
            if (_local2 < 0) {
                _local2 = _streamName.indexOf("/");
                if (_local2 >= 0) {
                    _appName = _appName + "/";
                    _appName = _appName + _streamName.slice(0, _local2);
                    _streamName = _streamName.slice(_local2 + 1);
                }
                return(false);
            }
            var _local3 = _appName.slice(_local2 + 1);
            _local3 = _local3 + "/";
            _local3 = _local3 + _streamName;
            _streamName = _local3;
            _appName = _appName.slice(0, _local2);
            this.close();
            _payload = 0;
            _connTypeCounter = 0;
            cleanConns();
            connectRTMP();
            return(true);
        }
        function reconnect() {
            if (!_isRTMP) {
                throw new Error("Cannot call reconnect on an http connection");
            }
            _nc.onStatus = function (_arg2) {
                this.mc.reconnectOnStatus(this, _arg2);
            };
            _nc.onBWDone = function () {
                this.mc.onReconnected();
            };
            _nc.connect(_ncUri, false);
        }
        function onReconnected() {
            delete _nc.onStatus;
            delete _nc.onBWDone;
            _owner.ncReconnected();
        }
        function close() {
            if (_nc) {
                _nc.close();
            }
        }
        function helperDone(_arg6, _arg5) {
            if (_arg6 != _smilMgr) {
                return(undefined);
            }
            if (!_arg5) {
                _nc = undefined;
                _owner.ncConnected();
                delete _smilMgr;
                return(undefined);
            }
            _streamWidth = _smilMgr.width;
            _streamHeight = _smilMgr.height;
            var _local2;
            var _local4 = _smilMgr.baseURLAttr[0];
            if ((_local4 != undefined) && (_local4 != "")) {
                _local2 = parseURL(_local4);
                _isRTMP = _local2.isRTMP;
                _streamName = _local2.streamName;
                if (_isRTMP) {
                    _protocol = _local2.protocol;
                    _serverName = _local2.serverName;
                    _portNumber = _local2.portNumber;
                    _wrappedURL = _local2.wrappedURL;
                    _appName = _local2.appName;
                    if ((_appName == undefined) || (_appName == "")) {
                        throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "Base RTMP URL must include application name: " + _local4);
                    }
                    if (_smilMgr.baseURLAttr.length > 1) {
                        _local2 = parseURL(_smilMgr.baseURLAttr[1]);
                        if (_local2.serverName != undefined) {
                            fallbackServerName = _local2.serverName;
                        }
                    }
                }
            }
            _streams = _smilMgr.videoTags;
            var _local3 = 0;
            while (_local3 < _streams.length) {
                _local4 = _streams[_local3].src;
                _local2 = parseURL(_local4);
                if (_isRTMP == undefined) {
                    _isRTMP = _local2.isRTMP;
                    if (_isRTMP) {
                        _protocol = _local2.protocol;
                        if (_streams.length > 1) {
                            throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "Cannot switch between multiple absolute RTMP URLs, must use meta tag base attribute.");
                        }
                        _serverName = _local2.serverName;
                        _portNumber = _local2.portNumber;
                        _wrappedURL = _local2.wrappedURL;
                        _appName = _local2.appName;
                        if ((_appName == undefined) || (_appName == "")) {
                            throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "Base RTMP URL must include application name: " + _local4);
                        }
                    }
                } else if ((((_streamName != undefined) && (_streamName != "")) && (!_local2.isRelative)) && (_streams.length > 1)) {
                    throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "When using meta tag base attribute, cannot use absolute URLs for video or ref tag src attributes.");
                }
                _streams[_local3].parseResults = _local2;
                _local3++;
            }
            _autoSenseBW = _streams.length > 1;
            if (!_autoSenseBW) {
                if (_streamName != undefined) {
                    _streamName = _streamName + _streams[0].parseResults.streamName;
                } else {
                    _streamName = _streams[0].parseResults.streamName;
                }
                _streamLength = _streams[0].dur;
            }
            if (_isRTMP) {
                connectRTMP();
            } else {
                if (_autoSenseBW) {
                    bitrateMatch();
                }
                connectHTTP();
                _owner.ncConnected();
            }
        }
        function bitrateMatch() {
            var _local3;
            if (isNaN(_bitrate)) {
                _local3 = 0;
            } else {
                var _local2 = 0;
                while (_local2 < _streams.length) {
                    if (isNaN(_streams[_local2].bitrate) || (_bitrate <= _streams[_local2].bitrate)) {
                        _local3 = _local2;
                        break;
                    }
                    _local2++;
                }
            }
            if (isNaN(_local3)) {
                throw new mx.video.VideoError(mx.video.VideoError.NO_BITRATE_MATCH);
            }
            if (_streamName != undefined) {
                _streamName = _streamName + _streams[_local3].src;
            } else {
                _streamName = _streams[_local3].src;
            }
            _streamLength = _streams[_local3].dur;
        }
        function parseURL(_arg5) {
            var _local2 = new Object();
            var _local3 = 0;
            var _local4 = _arg5.indexOf(":/", _local3);
            if (_local4 >= 0) {
                _local4 = _local4 + 2;
                _local2.protocol = _arg5.slice(_local3, _local4);
                _local2.isRelative = false;
            } else {
                _local2.isRelative = true;
            }
            if ((_local2.protocol != undefined) && (((_local2.protocol == "rtmp:/") || (_local2.protocol == "rtmpt:/")) || (_local2.protocol == "rtmps:/"))) {
                _local2.isRTMP = true;
                _local3 = _local4;
                if (_arg5.charAt(_local3) == "/") {
                    _local3++;
                    var _local7 = _arg5.indexOf(":", _local3);
                    var _local8 = _arg5.indexOf("/", _local3);
                    if (_local8 < 0) {
                        if (_local7 < 0) {
                            _local2.serverName = _arg5.slice(_local3);
                        } else {
                            _local4 = _local7;
                            _local2.portNumber = _arg5.slice(_local3, _local4);
                            _local3 = _local4 + 1;
                            _local2.serverName = _arg5.slice(_local3);
                        }
                        return(_local2);
                    }
                    if ((_local7 >= 0) && (_local7 < _local8)) {
                        _local4 = _local7;
                        _local2.serverName = _arg5.slice(_local3, _local4);
                        _local3 = _local4 + 1;
                        _local4 = _local8;
                        _local2.portNumber = _arg5.slice(_local3, _local4);
                    } else {
                        _local4 = _local8;
                        _local2.serverName = _arg5.slice(_local3, _local4);
                    }
                    _local3 = _local4 + 1;
                }
                if (_arg5.charAt(_local3) == "?") {
                    var _local9 = _arg5.slice(_local3 + 1);
                    var _local6 = parseURL(_local9);
                    if ((_local6.protocol == undefined) || (!_local6.isRTMP)) {
                        throw new mx.video.VideoError(mx.video.VideoError.INVALID_CONTENT_PATH, _arg5);
                    }
                    _local2.wrappedURL = "?";
                    _local2.wrappedURL = _local2.wrappedURL + _local6.protocol;
                    if (_local6.server != undefined) {
                        _local2.wrappedURL = _local2.wrappedURL + "/";
                        _local2.wrappedURL = _local2.wrappedURL + _local6.server;
                    }
                    if (_local6.wrappedURL != undefined) {
                        _local2.wrappedURL = _local2.wrappedURL + "/?";
                        _local2.wrappedURL = _local2.wrappedURL + _local6.wrappedURL;
                    }
                    _local2.appName = _local6.appName;
                    _local2.streamName = _local6.streamName;
                    return(_local2);
                }
                _local4 = _arg5.indexOf("/", _local3);
                if (_local4 < 0) {
                    _local2.appName = _arg5.slice(_local3);
                    return(_local2);
                }
                _local2.appName = _arg5.slice(_local3, _local4);
                _local3 = _local4 + 1;
                _local4 = _arg5.indexOf("/", _local3);
                if (_local4 < 0) {
                    _local2.streamName = _arg5.slice(_local3);
                    return(_local2);
                }
                _local2.appName = _local2.appName + "/";
                _local2.appName = _local2.appName + _arg5.slice(_local3, _local4);
                _local3 = _local4 + 1;
                _local2.streamName = _arg5.slice(_local3);
            } else {
                _local2.isRTMP = false;
                _local2.streamName = _arg5;
            }
            return(_local2);
        }
        function canReuseOldConnection(_arg2) {
            if ((_nc == undefined) || (_nc == null)) {
                return(false);
            }
            if (!_arg2.isRTMP) {
                if (!_isRTMP) {
                    return(true);
                }
                _owner.close();
                _nc = null;
                initNCInfo();
                return(false);
            }
            if (_isRTMP) {
                if (((((_arg2.serverName == _serverName) && (_arg2.appName == _appName)) && (_arg2.protocol == _protocol)) && (_arg2.portNumber == _portNumber)) && (_arg2.wrappedURL == _wrappedURL)) {
                    return(true);
                }
                _owner.close();
                _nc = null;
            }
            initNCInfo();
            return(false);
        }
        function connectHTTP() {
            _nc = new NetConnection();
            _nc.connect(null);
            return(true);
        }
        function connectRTMP() {
            clearInterval(_timeoutIntervalId);
            _timeoutIntervalId = setInterval(this, "_onFCSConnectTimeOut", _timeout);
            _tryNC = new Array();
            var _local2 = 0;
            while (_local2 < RTMP_CONN.length) {
                _tryNC[_local2] = new NetConnection();
                _tryNC[_local2].mc = this;
                _tryNC[_local2].pending = false;
                _tryNC[_local2].connIndex = _local2;
                _tryNC[_local2].onBWDone = function (_arg2) {
                    this.mc.onConnected(this, _arg2);
                };
                _tryNC[_local2].onBWCheck = function () {
                    return(++this.mc._payload);
                };
                _tryNC[_local2].onStatus = function (_arg2) {
                    this.mc.connectOnStatus(this, _arg2);
                };
                _local2++;
            }
            nextConnect();
            return(false);
        }
        function nextConnect() {
            clearInterval(_tryNCIntervalId);
            _tryNCIntervalId = 0;
            var _local4;
            var _local3;
            if (_connTypeCounter == 0) {
                _local4 = _protocol;
                if (_portNumber != undefined) {
                    _local3 = _portNumber;
                } else {
                    var _local2 = 0;
                    while (_local2 < RTMP_CONN.length) {
                        if (_local4 == RTMP_CONN[_local2].protocol) {
                            _local3 = RTMP_CONN[_local2].port;
                            break;
                        }
                        _local2++;
                    }
                }
            } else {
                _local4 = RTMP_CONN[_connTypeCounter].protocol;
                _local3 = RTMP_CONN[_connTypeCounter].port;
            }
            var _local5 = ((_local4 + ((_serverName == undefined) ? "" : (((("/" + _serverName) + ":") + _local3) + "/"))) + ((_wrappedURL == undefined) ? "" : (_wrappedURL + "/"))) + _appName;
            _tryNC[_connTypeCounter].pending = true;
            _tryNC[_connTypeCounter].connect(_local5, _autoSenseBW);
            if (_connTypeCounter < (RTMP_CONN.length - 1)) {
                _connTypeCounter++;
                _tryNCIntervalId = setInterval(this, "nextConnect", 1500);
            }
        }
        function cleanConns() {
            clearInterval(_tryNCIntervalId);
            _tryNCIntervalId = 0;
            if (_tryNC != undefined) {
                var _local2 = 0;
                while (_local2 < _tryNC.length) {
                    if (_tryNC[_local2] != undefined) {
                        delete _tryNC[_local2].onStatus;
                        if (_tryNC[_local2].pending) {
                            _tryNC[_local2].onStatus = function (_arg2) {
                                this.mc.disconnectOnStatus(this, _arg2);
                            };
                        } else {
                            delete _tryNC[_local2].onStatus;
                            _tryNC[_local2].close();
                        }
                    }
                    delete _tryNC[_local2];
                    _local2++;
                }
                delete _tryNC;
            }
        }
        function tryFallBack() {
            if (((_serverName == fallbackServerName) || (fallbackServerName == undefined)) || (fallbackServerName == null)) {
                delete _nc;
                _nc = undefined;
                _owner.ncConnected();
            } else {
                _connTypeCounter = 0;
                cleanConns();
                _serverName = fallbackServerName;
                connectRTMP();
            }
        }
        function onConnected(_arg7, _arg5) {
            clearInterval(_timeoutIntervalId);
            _timeoutIntervalId = 0;
            delete _arg7.onBWDone;
            delete _arg7.onBWCheck;
            delete _arg7.onStatus;
            _nc = _arg7;
            _ncUri = _nc.uri;
            if (_autoSenseBW) {
                _bitrate = _arg5 * 1024;
                if (_streams != undefined) {
                    bitrateMatch();
                } else if (_streamName.indexOf(",") != -1) {
                    var _local3 = _streamName.split(",");
                    var _local2 = 0;
                    while (_local2 < _local3.length) {
                        var _local4 = stripFrontAndBackWhiteSpace(_local3[_local2]);
                        if ((_local2 + 1) < _local3.length) {
                            if (_arg5 <= Number(_local3[_local2 + 1])) {
                                _streamName = _local4;
                                break;
                            }
                        } else {
                            _streamName = _local4;
                            break;
                        }
                        _local2 = _local2 + 2;
                    }
                }
            }
            if (_streamName.slice(-4).toLowerCase() == ".flv") {
                _streamName = _streamName.slice(0, -4);
            }
            if ((!_owner.__get__isLive()) && (_streamLength == undefined)) {
                var _local6 = new Object();
                _local6.mc = this;
                _local6.onResult = function (_arg2) {
                    this.mc.getStreamLengthResult(_arg2);
                };
                _nc.call("getStreamLength", _local6, _streamName);
            } else {
                _owner.ncConnected();
            }
        }
        function connectOnStatus(_arg2, _arg3) {
            _arg2.pending = false;
            if (_arg3.code == "NetConnection.Connect.Success") {
                _nc = _tryNC[_arg2.connIndex];
                _tryNC[_arg2.connIndex] = undefined;
                cleanConns();
            } else if (((_arg3.code == "NetConnection.Connect.Failed") || (_arg3.code == "NetConnection.Connect.Rejected")) && (_arg2.connIndex == (RTMP_CONN.length - 1))) {
                if (!connectAgain()) {
                    tryFallBack();
                }
            }
        }
        function reconnectOnStatus(target, _arg2) {
            if ((_arg2.code == "NetConnection.Connect.Failed") || (_arg2.code == "NetConnection.Connect.Rejected")) {
                delete _nc;
                _nc = undefined;
                _owner.ncReconnected();
            }
        }
        function disconnectOnStatus(_arg1, _arg2) {
            if (_arg2.code == "NetConnection.Connect.Success") {
                delete _arg1.onStatus;
                _arg1.close();
            }
        }
        function getStreamLengthResult(_arg2) {
            _streamLength = _arg2;
            _owner.ncConnected();
        }
        function _onFCSConnectTimeOut() {
            cleanConns();
            _nc = undefined;
            if (!connectAgain()) {
                _owner.ncConnected();
            }
        }
        static function stripFrontAndBackWhiteSpace(_arg3) {
            var _local1;
            var _local2 = _arg3.length;
            var _local4 = 0;
            var _local5 = _local2;
            _local1 = 0;
            while (_local1 < _local2) {
                switch (_arg3.charCodeAt(_local1)) {
                    case 9 : 
                    case 10 : 
                    case 13 : 
                    case 32 : 
                        break;
                    default : 
                        _local4 = _local1;
                        break;!//outer level
                }
                _local1++;
            }
            _local1 = _local2;
            while (_local1 >= 0) {
                switch (_arg3.charCodeAt(_local1)) {
                    case 9 : 
                    case 10 : 
                    case 13 : 
                    case 32 : 
                        break;
                    default : 
                        _local5 = _local1 + 1;
                        break;!//outer level
                }
                _local1--;
            }
            if (_local5 <= _local4) {
                return("");
            }
            return(_arg3.slice(_local4, _local5));
        }
        static var version = "1.0.0.103";
        var DEFAULT_TIMEOUT = 60000;
        static var RTMP_CONN = [{protocol:"rtmp:/", port:"1935"}, {protocol:"rtmp:/", port:"443"}, {protocol:"rtmpt:/", port:"80"}, {protocol:"rtmps:/", port:"443"}];
    }