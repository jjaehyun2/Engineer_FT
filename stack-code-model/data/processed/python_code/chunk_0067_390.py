dynamic class tm.utils.XMLParser
{
    var _caller;
    var _data;
    var _onCompleteCallback;
    var _url;
    var _xml;

    function XMLParser()
    {
        this._data = new Object();
    }

    function load(url, caller, callback, killCache)
    {
        this._url = url;
        this._caller = caller;
        this._onCompleteCallback = callback;
        this._xml = new XML();
        this._xml.ignoreWhite = true;
        this._xml.onLoad = tm.utils.Delegate.create(this, this.xmlLoadHandler);
        var __reg2 = killCache == true ? "?cacheKiller=" + String((new Date()).getTime()) : "";
        this._xml.load(this._url + __reg2);
    }

    function xmlLoadHandler(success)
    {
        if (success) 
        {
            var __reg2 = this._xml.firstChild.firstChild;
            var __reg7 = this._xml.firstChild.lastChild;
            this._xml.firstChild.obj = this._data;
            while (__reg2) 
            {
                if (__reg2.nodeName == null && __reg2.nodeType == 3) 
                {
                    __reg2.parentNode.obj.value = tm.utils.Utils.searchAndReplace(__reg2.nodeValue, "\r\n", "");
                }
                else 
                {
                    var __reg4 = {};
                    for (var __reg6 in __reg2.attributes) 
                    {
                        __reg4[__reg6] = __reg2.attributes[__reg6];
                    }
                    var __reg5 = __reg2.parentNode.obj;
                    if (__reg5[__reg2.nodeName] == undefined) 
                    {
                        __reg5[__reg2.nodeName] = [];
                    }
                    __reg2.obj = __reg4;
                    __reg5[__reg2.nodeName].push(__reg4);
                }
                if (__reg2.childNodes.length > 0) 
                {
                    __reg2 = __reg2.childNodes[0];
                }
                else 
                {
                    var __reg3 = __reg2;
                    while (__reg3.nextSibling == undefined && __reg3.parentNode != undefined) 
                    {
                        __reg3 = __reg3.parentNode;
                    }
                    __reg2 = __reg3.nextSibling;
                    if (__reg3 == __reg7) 
                    {
                        __reg2 = undefined;
                    }
                }
            }
            this._onCompleteCallback.call(this._caller, true, this._data);
            return;
        }
        this._onCompleteCallback.call(this._caller, false);
    }

}