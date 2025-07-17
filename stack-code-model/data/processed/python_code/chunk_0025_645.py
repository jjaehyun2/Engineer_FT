    class oxylus.afsmg.thumb extends MovieClip
    {
        var enabled, icon, settings, myTooltip, _parent, mcl, node, ref, loader, image, dispatchEvent, stroke, over, _visible;
        function thumb () {
            super();
            mx.events.EventDispatcher.initialize(this);
            enabled = false;
            icon._visible = false;
            settings = new Object();
            myTooltip = oxylus.Tooltip03.Tooltip.attach(_parent._parent._parent);
            mcl = new MovieClipLoader();
            mcl.addListener(this);
        }
        function setNode(_arg3, _arg2) {
            node = _arg3;
            settings = _arg2;
            ref._width = settings.thumbWidth + 10;
            ref._height = settings.thumbHeight + 10;
            loader._x = Math.round(ref._width / 2);
            loader._y = Math.round(ref._height / 2);
            mcl.loadClip(node.attributes.thumb, image);
        }
        function onLoadStart(mc) {
            caurina.transitions.Tweener.addTween(loader, {_alpha:100, time:0.2, transition:"linear"});
        }
        function onLoadProgress(mc, bytesLoaded, bytesTotal) {
        }
        function onLoadComplete(mc) {
        }
        function onLoadInit(_arg6) {
            oxylus.Utils.getImage(_arg6, true);
            _arg6._width = loader._width - 2;
            _arg6._height = loader._height - 2;
            _arg6._x = loader._x + 1;
            _arg6._y = loader._y + 1;
            caurina.transitions.Tweener.addTween(_arg6, {_alpha:100, _height:settings.thumbHeight, _width:settings.thumbWidth, _x:5, _y:5, time:0.5, transition:"easeOutQuart", onUpdate:ascb.util.Proxy.create(this, updateStroke, _arg6), onComplete:ascb.util.Proxy.create(this, thisLoaded)});
            caurina.transitions.Tweener.addTween(loader, {_alpha:0, delay:0.3, time:0.5, transition:"easeOutQuad", onComplete:ascb.util.Proxy.create(this, stopSpin)});
            dispatchEvent({target:this, type:"thumbLoaded", mc:this});
            var _local3 = node.attributes.image;
            var _local2 = _local3.split(".");
            var _local4 = "Photo:";
            if (_local2[_local2.length - 1] == "flv") {
                _local4 = "Video:";
            }
            myTooltip.setCustomVars({myTexts:String((_local4 + "<new_line>") + node.attributes.title), myFonts:"a|a", myColors:"0xf6f6f6|0x929292", mySizes:"12|8", myVerticalSpaces:"2|-2|-2|-2", textXPos:0, farX:0, strokeColor:"0x434343", strokeAlpha:100, strokeWidth:1, backgroundColor:"0x2d2d2d|0x3e3e3e|0x565656", backgroundAlpha:100, backgroundRadius:2, backgroundWidth:10, backgroundHeight:0, addShadow:"true", shadowAngleInDegrees:90, shadowDistance:2, shadowColor:"0x000000", shadowAlpha:"0.10", shadowBlurX:"6", shadowBlurY:"6", shadowStrength:"3", shadowQuality:"3", tipOrientation:"bottom", tipWidth:7, tipHeight:16, tipInclination:3.5, tipX:70, XDistanceFromCursor:-10, YDistanceFromCursor:-10, alignHoriz:"right", alignVerti:"top", stageToleranceX:0, stageToleranceY:10}, _parent._parent._parent);
        }
        function stopSpin() {
            loader.spin.stop();
            loader.removeMovieClip();
            var _local3 = node.attributes.image;
            var _local2 = _local3.split(".");
            if (_local2[_local2.length - 1] == "flv") {
                icon._x = Math.round((settings.thumbWidth / 2) - (icon._width / 2));
                icon._y = Math.round((settings.thumbHeight / 2) - (icon._height / 2));
                icon._x = icon._x + 5;
                icon._y = icon._y + 5;
                icon._visible = true;
            }
        }
        function thisLoaded() {
            loaded = 1;
            enabled = true;
        }
        function updateStroke(_arg2) {
            stroke._x = _arg2._x - 5;
            stroke._y = _arg2._y - 5;
            stroke._width = _arg2._width + 10;
            stroke._height = _arg2._height + 10;
            stroke._alpha = _arg2._alpha;
            over._width = _arg2._width + 8;
            over._height = _arg2._height + 8;
        }
        function onLoadError(pMc, _arg6, _arg5) {
            trace(">> errorCode: " + _arg6);
            trace(">> httpStatus: " + _arg5);
            _visible = false;
            dispatchEvent({target:this, type:"thumbLoaded", mc:this});
        }
        function onRollOver() {
            if (loaded == 1) {
                caurina.transitions.Tweener.addTween(over, {_alpha:100, time:0.3, transition:"easeOutQuad"});
                caurina.transitions.Tweener.addTween(stroke.nWhite, {_alpha:0, time:0.3, transition:"easeOutQuad"});
                myTooltip.show({animationTime:0.3, animationType:"linear", stay:0});
            }
        }
        function onRollOut() {
            if (loaded == 1) {
                caurina.transitions.Tweener.addTween(over, {_alpha:0, time:0.3, transition:"easeOutQuad"});
                caurina.transitions.Tweener.addTween(stroke.nWhite, {_alpha:100, time:0.3, transition:"easeOutQuad"});
                myTooltip.hide({animationTime:0.3, animationType:"linear"});
            }
        }
        function onRelease() {
            this.onRollOut();
            dispatchEvent({target:this, type:"thumbReleased", mc:this});
        }
        function drawOval(_arg1, _arg3, _arg4, _arg2, _arg6, _arg5, _arg7) {
            _arg1.clear();
            _arg1.beginFill(_arg6, _arg5);
            if (_arg7 == 1) {
                _arg1.lineStyle(1, 16777215, _arg5, true);
            }
            _arg1.moveTo(_arg2, 0);
            _arg1.lineTo(_arg3 - _arg2, 0);
            _arg1.curveTo(_arg3, 0, _arg3, _arg2);
            _arg1.lineTo(_arg3, _arg4 - _arg2);
            _arg1.curveTo(_arg3, _arg4, _arg3 - _arg2, _arg4);
            _arg1.lineTo(_arg2, _arg4);
            _arg1.curveTo(0, _arg4, 0, _arg4 - _arg2);
            _arg1.lineTo(0, _arg2);
            _arg1.curveTo(0, 0, _arg2, 0);
            _arg1.endFill();
        }
        var loaded = 0;
    }