class mx.video.SMILManager
{
    var _owner, _url, xml, xmlOnLoad, baseURLAttr, videoTags, width, height;
    function SMILManager(owner)
    {
        _owner = owner;
    } // End of the function
    function connectXML(url)
    {
        _url = this.fixURL(url);
        xml = new XML();
        xml.onLoad = mx.utils.Delegate.create(this, xmlOnLoad);
        xml.load(_url);
        return (false);
    } // End of the function
    function fixURL(origURL)
    {
        if (origURL.substr(0, 5).toLowerCase() == "http:" || origURL.substr(0, 6).toLowerCase() == "https:")
        {
            var _loc2 = origURL.indexOf("?") >= 0 ? ("&") : ("?");
            return (origURL + _loc2 + "FLVPlaybackVersion=" + mx.video.SMILManager.shortVersion);
        } // end if
        return (origURL);
    } // End of the function
    null[] = (Error)() == null ? (null, throw , function (success)
    {
        try
        {
            if (!success)
            {
                _owner.helperDone(this, false);
            }
            else
            {
                baseURLAttr = new Array();
                videoTags = new Array();
                var _loc2 = xml.firstChild;
                var _loc6 = false;
                while (_loc2 != null)
                {
                    if (_loc2.nodeType == mx.video.SMILManager.ELEMENT_NODE)
                    {
                        _loc6 = true;
                        if (_loc2.nodeName.toLowerCase() == "smil")
                        {
                            break;
                        } // end if
                    } // end if
                    _loc2 = _loc2.nextSibling;
                } // end while
                if (!_loc6)
                {
                    throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "URL: \"" + _url + "\" No root node found; if url is for an flv it must have .flv extension and take no parameters");
                }
                else if (_loc2 == null)
                {
                    throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "URL: \"" + _url + "\" Root node not smil");
                } // end else if
                var _loc5 = false;
                for (var _loc4 = 0; _loc4 < _loc2.childNodes.length; ++_loc4)
                {
                    var _loc3 = _loc2.childNodes[_loc4];
                    if (_loc3.nodeType != mx.video.SMILManager.ELEMENT_NODE)
                    {
                        continue;
                    } // end if
                    if (_loc3.nodeName.toLowerCase() == "head")
                    {
                        this.parseHead(_loc3);
                        continue;
                    } // end if
                    if (_loc3.nodeName.toLowerCase() == "body")
                    {
                        _loc5 = true;
                        this.parseBody(_loc3);
                        continue;
                    } // end if
                    throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "URL: \"" + _url + "\" Tag " + _loc3.nodeName + " not supported in " + _loc2.nodeName + " tag.");
                } // end of for
                if (!_loc5)
                {
                    throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "URL: \"" + _url + "\" Tag body is required.");
                } // end if
                _owner.helperDone(this, true);
            } // end else if
        } // End of try
        catch ()
        {
        } // End of catch
    }) : (var err = (Error)(), _owner.helperDone(this, false), throw err, "xmlOnLoad");
    function parseHead(parentNode)
    {
        var _loc4 = false;
        for (var _loc3 = 0; _loc3 < parentNode.childNodes.length; ++_loc3)
        {
            var _loc2 = parentNode.childNodes[_loc3];
            if (_loc2.nodeType != mx.video.SMILManager.ELEMENT_NODE)
            {
                continue;
            } // end if
            if (_loc2.nodeName.toLowerCase() == "meta")
            {
                for (var _loc6 in _loc2.attributes)
                {
                    if (_loc6.toLowerCase() == "base")
                    {
                        baseURLAttr.push(_loc2.attributes[_loc6]);
                        continue;
                    } // end if
                    throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "URL: \"" + _url + "\" Attribute " + _loc6 + " not supported in " + _loc2.nodeName + " tag.");
                } // end of for...in
                continue;
            } // end if
            if (_loc2.nodeName.toLowerCase() == "layout")
            {
                if (!_loc4)
                {
                    this.parseLayout(_loc2);
                    _loc4 = true;
                    
                } // end if
                continue;
            } // end if
        } // end of for
    } // End of the function
    function parseLayout(parentNode)
    {
        for (var _loc3 = 0; _loc3 < parentNode.childNodes.length; ++_loc3)
        {
            var _loc2 = parentNode.childNodes[_loc3];
            if (_loc2.nodeType != mx.video.SMILManager.ELEMENT_NODE)
            {
                continue;
            } // end if
            if (_loc2.nodeName.toLowerCase() == "root-layout")
            {
                for (var _loc5 in _loc2.attributes)
                {
                    if (_loc5.toLowerCase() == "width")
                    {
                        width = Number(_loc2.attributes[_loc5]);
                        continue;
                    } // end if
                    if (_loc5.toLowerCase() == "height")
                    {
                        height = Number(_loc2.attributes[_loc5]);
                        continue;
                    } // end if
                } // end of for...in
                if (isNaN(width) || width < 0 || isNaN(height) || height < 0)
                {
                    throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "URL: \"" + _url + "\" Tag " + _loc2.nodeName + " requires attributes id, width and height.  Width and height must be numbers greater than or equal to 0.");
                } // end if
                width = Math.round(width);
                height = Math.round(height);
                return;
                continue;
            } // end if
        } // end of for
    } // End of the function
    function parseBody(parentNode)
    {
        var _loc6 = 0;
        for (var _loc3 = 0; _loc3 < parentNode.childNodes.length; ++_loc3)
        {
            var _loc2 = parentNode.childNodes[_loc3];
            if (_loc2.nodeType != mx.video.SMILManager.ELEMENT_NODE)
            {
                continue;
            } // end if
            if (++_loc6 > 1)
            {
                throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "URL: \"" + _url + "\" Tag " + parentNode.nodeName + " is required to contain exactly one tag.");
            } // end if
            if (_loc2.nodeName.toLowerCase() == "switch")
            {
                this.parseSwitch(_loc2);
                continue;
            } // end if
            if (_loc2.nodeName.toLowerCase() == "video" || _loc2.nodeName.toLowerCase() == "ref")
            {
                var _loc5 = this.parseVideo(_loc2);
                videoTags.push(_loc5);
                continue;
            } // end if
        } // end of for
        if (videoTags.length < 1)
        {
            throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "URL: \"" + _url + "\" At least one video of ref tag is required.");
        } // end if
    } // End of the function
    function parseSwitch(parentNode)
    {
        for (var _loc4 = 0; _loc4 < parentNode.childNodes.length; ++_loc4)
        {
            var _loc5 = parentNode.childNodes[_loc4];
            if (_loc5.nodeType != mx.video.SMILManager.ELEMENT_NODE)
            {
                continue;
            } // end if
            if (_loc5.nodeName.toLowerCase() == "video" || _loc5.nodeName.toLowerCase() == "ref")
            {
                var _loc3 = this.parseVideo(_loc5);
                if (_loc3.bitrate == undefined)
                {
                    videoTags.push(_loc3);
                }
                else
                {
                    var _loc6 = false;
                    for (var _loc2 = 0; _loc2 < videoTags.length; ++_loc2)
                    {
                        if (videoTags[_loc2].bitrate == undefined || _loc3.bitrate < videoTags[_loc4].bitrate)
                        {
                            _loc6 = true;
                            videoTags.splice(_loc2, 0, videoTags);
                            break;
                        } // end if
                    } // end of for
                    if (!_loc6)
                    {
                        videoTags.push(_loc3);
                    } // end if
                } // end else if
                continue;
            } // end if
        } // end of for
    } // End of the function
    function parseVideo(node)
    {
        var _loc3 = new Object();
        for (var _loc4 in node.attributes)
        {
            if (_loc4.toLowerCase() == "src")
            {
                _loc3.src = node.attributes[_loc4];
                continue;
            } // end if
            if (_loc4.toLowerCase() == "system-bitrate")
            {
                _loc3.bitrate = Number(node.attributes[_loc4]);
                continue;
            } // end if
            if (_loc4.toLowerCase() == "dur")
            {
                _loc3.dur = this.parseTime(node.attributes[_loc4]);
                continue;
            } // end if
        } // end of for...in
        if (_loc3.src == undefined)
        {
            throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "URL: \"" + _url + "\" Attribute src is required in " + node.nodeName + " tag.");
        } // end if
        return (_loc3);
    } // End of the function
    function parseTime(timeStr)
    {
        var _loc4 = 0;
        var _loc3 = timeStr.split(":");
        if (_loc3.length < 1 || _loc3.length > 3)
        {
            throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "Invalid dur value: " + timeStr);
        } // end if
        for (var _loc1 = 0; _loc1 < _loc3.length; ++_loc1)
        {
            var _loc2 = Number(_loc3[_loc1]);
            if (isNaN(_loc2))
            {
                throw new mx.video.VideoError(mx.video.VideoError.INVALID_XML, "Invalid dur value: " + timeStr);
            } // end if
            _loc4 = _loc4 * 60;
            _loc4 = _loc4 + _loc2;
        } // end of for
        return (_loc4);
    } // End of the function
    static var version = "1.0.1.10";
    static var shortVersion = "1.0.1";
    static var ELEMENT_NODE = 1;
} // End of Class