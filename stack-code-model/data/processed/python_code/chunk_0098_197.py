
//Created by Action Script Viewer - http://www.buraks.com/asv
    class mx.video.SMILManager
    {
        var _owner, _url, xml, baseURLAttr, videoTags, width, height;
        function SMILManager (_arg2) {
            _owner = _arg2;
        }
        function connectXML(_arg2) {
            _url = _arg2;
            xml = new XML();
            xml.onLoad = mx.utils.Delegate.create(this, xmlOnLoad);
            xml.load(_arg2);
            return(false);
        }
        function xmlOnLoad(_arg6) {
            try {
                if (!_arg6) {
                    _owner.helperDone(this, false);
                } else {
                    baseURLAttr = new Array();
                    videoTags = new Array();
                    var _local4 = xml.firstChild;
                    if (_local4.nodeName == null) {
                        throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, ("URL: \"" + _url) + "\" No root node found; if file is an flv it must have .flv extension");
                    } else if (_local4.nodeName.toLowerCase() != "smil") {
                        throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, (("URL: \"" + _url) + "\" Root node not smil: ") + _local4.nodeName);
                    }
                    var _local5 = false;
                    var _local3 = 0;
                    while (_local3 < _local4.childNodes.length) {
                        var _local2 = _local4.childNodes[_local3];
                        if (_local2.nodeType != ELEMENT_NODE) {
                        } else if (_local2.nodeName.toLowerCase() == "head") {
                            parseHead(_local2);
                        } else if (_local2.nodeName.toLowerCase() == "body") {
                            _local5 = true;
                            parseBody(_local2);
                        } else {
                            throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, ((((("URL: \"" + _url) + "\" Tag ") + _local2.nodeName) + " not supported in ") + _local4.nodeName) + " tag.");
                        }
                        _local3++;
                    }
                    if (!_local5) {
                        throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, ("URL: \"" + _url) + "\" Tag body is required.");
                    }
                    _owner.helperDone(this, true);
                }
            } catch(err:Error) {
                _owner.helperDone(this, false);
                throw err;
            }
        }
        function parseHead(_arg5) {
            var _local4 = false;
            var _local3 = 0;
            while (_local3 < _arg5.childNodes.length) {
                var _local2 = _arg5.childNodes[_local3];
                if (_local2.nodeType != ELEMENT_NODE) {
                } else if (_local2.nodeName.toLowerCase() == "meta") {
                    for (var _local6 in _local2.attributes) {
                        if (_local6.toLowerCase() == "base") {
                            baseURLAttr.push(_local2.attributes[_local6]);
                        } else {
                            throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, ((((("URL: \"" + _url) + "\" Attribute ") + _local6) + " not supported in ") + _local2.nodeName) + " tag.");
                        }
                    }
                } else if (_local2.nodeName.toLowerCase() == "layout") {
                    if (!_local4) {
                        parseLayout(_local2);
                        _local4 = true;
                    }
                }
                _local3++;
            }
        }
        function parseLayout(_arg4) {
            var _local3 = 0;
            while (_local3 < _arg4.childNodes.length) {
                var _local2 = _arg4.childNodes[_local3];
                if (_local2.nodeType != ELEMENT_NODE) {
                } else if (_local2.nodeName.toLowerCase() == "root-layout") {
                    for (var _local5 in _local2.attributes) {
                        if (_local5.toLowerCase() == "width") {
                            width = Number(_local2.attributes[_local5]);
                        } else if (_local5.toLowerCase() == "height") {
                            height = Number(_local2.attributes[_local5]);
                        }
                    }
                    if (((isNaN(width) || (width < 0)) || (isNaN(height))) || (height < 0)) {
                        throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, ((("URL: \"" + _url) + "\" Tag ") + _local2.nodeName) + " requires attributes id, width and height.  Width and height must be numbers greater than or equal to 0.");
                    }
                    width = Math.round(width);
                    height = Math.round(height);
                    return(undefined);
                }
                _local3++;
            }
        }
        function parseBody(_arg4) {
            var _local6 = 0;
            var _local3 = 0;
            while (_local3 < _arg4.childNodes.length) {
                var _local2 = _arg4.childNodes[_local3];
                if (_local2.nodeType != ELEMENT_NODE) {
                } else {
                    _local6++;
                    if (_local6 > 1) {
                        throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, ((("URL: \"" + _url) + "\" Tag ") + _arg4.nodeName) + " is required to contain exactly one tag.");
                    }
                    if (_local2.nodeName.toLowerCase() == "switch") {
                        parseSwitch(_local2);
                    } else if ((_local2.nodeName.toLowerCase() == "video") || (_local2.nodeName.toLowerCase() == "ref")) {
                        var _local5 = parseVideo(_local2);
                        videoTags.push(_local5);
                    }
                }
                _local3++;
            }
            if (videoTags.length < 1) {
                throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, ("URL: \"" + _url) + "\" At least one video of ref tag is required.");
            }
        }
        function parseSwitch(_arg7) {
            var _local4 = 0;
            while (_local4 < _arg7.childNodes.length) {
                var _local5 = _arg7.childNodes[_local4];
                if (_local5.nodeType != ELEMENT_NODE) {
                } else if ((_local5.nodeName.toLowerCase() == "video") || (_local5.nodeName.toLowerCase() == "ref")) {
                    var _local3 = parseVideo(_local5);
                    if (_local3.bitrate == undefined) {
                        videoTags.push(_local3);
                    } else {
                        var _local6 = false;
                        var _local2 = 0;
                        while (_local2 < videoTags.length) {
                            if ((videoTags[_local2].bitrate == undefined) || (_local3.bitrate < videoTags[_local4].bitrate)) {
                                _local6 = true;
                                videoTags.splice(_local2, 0, videoTags);
                                break;
                            }
                            _local2++;
                        }
                        if (!_local6) {
                            videoTags.push(_local3);
                        }
                    }
                }
                _local4++;
            }
        }
        function parseVideo(_arg2) {
            var _local3 = new Object();
            for (var _local4 in _arg2.attributes) {
                if (_local4.toLowerCase() == "src") {
                    _local3.src = _arg2.attributes[_local4];
                } else if (_local4.toLowerCase() == "system-bitrate") {
                    _local3.bitrate = Number(_arg2.attributes[_local4]);
                } else if (_local4.toLowerCase() == "dur") {
                    _local3.dur = Number(_arg2.attributes[_local4]);
                }
            }
            if (_local3.src == undefined) {
                throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, ((("URL: \"" + _url) + "\" Attribute src is required in ") + _arg2.nodeName) + " tag.");
            }
            return(_local3);
        }
        static var version = "1.0.0.103";
        static var ELEMENT_NODE = 1;
    }