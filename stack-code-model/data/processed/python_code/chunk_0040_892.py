    class oxylus.afsmg.popup extends MovieClip
    {
        var _visible, holder, a, bg, navigation, next, prev, title, titleMask, line, picture, stroke, loader, img, ref, vid, ht, html, mask, scroller, bar, stick, close, mcl, dispatchEvent, popupMode, node, obj, removeMovieClip, _x, _y, ScrollArea, ScrollButton, Content, ContentMask, HitZone, getNextHighestDepth, totalHeight, scrollable, viewHeight, ScrollHeight, onEnterFrame;
        function popup () {
            super();
            mx.events.EventDispatcher.initialize(this);
            _visible = false;
            holder = a.holder;
            bg = a.bg;
            navigation = a.navigation;
            next = navigation.next;
            next.over._alpha = 0;
            prev = navigation.prev;
            prev.over._alpha = 0;
            title = holder.title;
            title.txt.autoSize = true;
            titleMask = title.mask;
            title.cacheAsBitmap = true;
            titleMask.cacheAsBitmap = true;
            title.setMask(titleMask);
            line = holder.line;
            picture = holder.picture;
            stroke = picture.stroke;
            loader = picture.loader;
            img = picture.img;
            ref = picture.ref;
            vid = holder.vid;
            ht = holder.ht;
            html = ht.html;
            oxylus.Utils.initMhtf(html.txt, false);
            mask = ht.mask;
            scroller = ht.scroller;
            bar = scroller.bar;
            stick = scroller.stick;
            html.setMask(mask);
            stick._height = mask._height;
            close = holder.close;
            close.onPress = ascb.util.Proxy.create(this, closeThis);
            close.onRollOver = ascb.util.Proxy.create(this, closeOnRollOver);
            close.onRollOut = ascb.util.Proxy.create(this, closeOnRollOut);
            next.onRollOver = ascb.util.Proxy.create(this, nextOnRollOver);
            next.onRollOut = ascb.util.Proxy.create(this, nextOnRollOut);
            next.onPress = ascb.util.Proxy.create(this, nextOnPress);
            prev.onRollOver = ascb.util.Proxy.create(this, prevOnRollOver);
            prev.onRollOut = ascb.util.Proxy.create(this, prevOnRollOut);
            prev.onPress = ascb.util.Proxy.create(this, prevOnPress);
            mcl = new MovieClipLoader();
            mcl.addListener(this);
            buildNavigation();
            buildBackground();
        }
        function nextOnPress() {
            dispatchEvent({target:this, type:"popupNext", mc:this});
            if (videoPresent == 1) {
                vid.a.videoKill();
            }
        }
        function prevOnPress() {
            dispatchEvent({target:this, type:"popupPrev", mc:this});
            if (videoPresent == 1) {
                vid.a.videoKill();
            }
        }
        function nextOnRollOver() {
            caurina.transitions.Tweener.addTween(next.over, {_alpha:100, time:0.2, transition:"linear"});
        }
        function nextOnRollOut() {
            caurina.transitions.Tweener.addTween(next.over, {_alpha:0, time:0.2, transition:"linear"});
        }
        function prevOnRollOver() {
            caurina.transitions.Tweener.addTween(prev.over, {_alpha:100, time:0.2, transition:"linear"});
        }
        function prevOnRollOut() {
            caurina.transitions.Tweener.addTween(prev.over, {_alpha:0, time:0.2, transition:"linear"});
        }
        function closeOnRollOver() {
            caurina.transitions.Tweener.addTween(close.over, {_alpha:100, time:0.2, transition:"linear"});
            caurina.transitions.Tweener.addTween(close.over.a, {_rotation:180, time:0.2, transition:"linear"});
            caurina.transitions.Tweener.addTween(close.normal.a, {_rotation:180, time:0.2, transition:"linear"});
        }
        function closeOnRollOut() {
            caurina.transitions.Tweener.addTween(close.over, {_alpha:0, time:0.2, transition:"linear"});
            caurina.transitions.Tweener.addTween(close.over.a, {_rotation:0, time:0.2, transition:"linear"});
            caurina.transitions.Tweener.addTween(close.normal.a, {_rotation:0, time:0.2, transition:"linear"});
        }
        function closeThis() {
            _global.popPresent = 0;
            if (popupMode == 1) {
                hidePrev();
            } else {
                hideNext();
            }
            if (videoPresent == 1) {
                vid.a.videoKill();
            }
            dispatchEvent({target:this, type:"closePopup"});
        }
        function setNode(_arg5, _arg4, settings_) {
            _global.popPresent = 1;
            popupMode = _arg4;
            node = _arg5;
            if (popupMode == 1) {
                a._x = Stage.width;
            } else {
                a._x = -Stage.width;
            }
            title.txt.text = node.attributes.title;
            titleMask._height = 2 * title._height;
            var _local3 = node.firstChild.nodeValue;
            html.txt.htmlText = _local3;
            if (_local3 == undefined) {
                html._visible = false;
            }
            loadStageResize();
            _visible = true;
            if (!node.nextSibling) {
                next.enabled = false;
                next._alpha = 50;
            }
            if (!node.previousSibling) {
                prev.enabled = false;
                prev._alpha = 50;
            }
            this.show();
        }
        function loadPicture() {
            var _local3 = node.attributes.image;
            var _local2 = _local3.split(".");
            if ((((_local2[_local2.length - 1] == "flv") || (_local2[_local2.length - 1] == "mov")) || (_local2[_local2.length - 1] == "mp4")) || (_local2[_local2.length - 1] == "h264")) {
                videoPresent = 1;
                obj = new Object();
                obj.width = tw - 60;
                obj.height = (th - 80) - 140;
                obj.movie = _local3;
                obj.title = node.attributes.videoTitle;
                obj.videosize = 0;
                obj.buffer = 1;
                obj.volume = 10;
                obj.autoplay = false;
                obj.repeat = false;
                obj.smoothing = true;
                obj.fullscreen = true;
                vid.a.setTheObject(obj);
                this.onResize();
                img._visible = false;
            } else {
                videoPresent = 0;
                mcl.loadClip(_local3, img);
                vid._visible = false;
            }
            trace("Video status: " + videoPresent);
        }
        function onLoadInit(_arg5) {
            oxylus.Utils.getImage(_arg5, true);
            loaded = 1;
            init = 1;
            this.onResize();
            caurina.transitions.Tweener.addTween(img, {_alpha:100, time:0.5, transition:"linear"});
            caurina.transitions.Tweener.addTween(stroke, {_alpha:100, time:0.5, transition:"linear"});
            loaderRemove();
        }
        function loaderRemove() {
            loader.spin.stop();
            loader._visible = false;
            loader.removeMovieClip();
        }
        function show() {
            oxylus.Utils.setMcBlur(a, blurAmountX, blurAmountY, 1);
            caurina.transitions.Tweener.addTween(a, {_x:0, _Blur_blurX:0, _Blur_blurY:0, time:animationTime, transition:animationType, rounded:true, onComplete:ascb.util.Proxy.create(this, loadPicture)});
        }
        function hideNext() {
            caurina.transitions.Tweener.addTween(a, {_x:Stage.width, _Blur_blurX:blurAmountX, _Blur_blurY:blurAmountY, time:animationTime, transition:animationType, rounded:true, onComplete:ascb.util.Proxy.create(this, removeMe)});
        }
        function hidePrev() {
            caurina.transitions.Tweener.addTween(a, {_x:-Stage.width, _Blur_blurX:blurAmountX, _Blur_blurY:blurAmountY, time:animationTime, transition:animationType, rounded:true, onComplete:ascb.util.Proxy.create(this, removeMe)});
        }
        function removeMe() {
            this.removeMovieClip();
        }
        function buildBackground() {
            drawOval(bg, tw, th, 6, 0, 90);
        }
        function buildNavigation() {
            drawOval(navigation.bg, tw + 80, 196, 6, 0, 80);
            next._x = Math.round((navigation.bg._width - next._width) - 8);
            prev._x = 8;
            next._y = (prev._y = Math.round((navigation.bg._height / 2) - (next._height / 2)));
            addShadow(navigation.bg);
            navigation._x = Math.round((bg._width / 2) - (navigation._width / 2));
            navigation._y = Math.round((bg._height / 2) - (navigation._height / 2));
        }
        function resize(_arg14, _arg13) {
            tw = _arg14;
            th = _arg13;
            var _local5 = tw - 60;
            var _local6 = (th - 80) - 140;
            if (init == 0) {
                if (videoPresent == 1) {
                    vid.a.resizeEZ(_local5, _local6);
                }
                if (caurina.transitions.Tweener.isTweening(loader)) {
                    tweensFinished();
                }
                loader._x = Math.round((_local5 / 2) - (loader._width / 2));
                loader._y = Math.round((_local6 / 2) - (loader._height / 2));
                if (loaded == 1) {
                    var _local2 = oxylus.Utils.getDims("fit", img._width, img._height, _local5 - 4, _local6 - 4, true);
                    img._width = _local2.w;
                    img._height = _local2.h;
                    img._x = 2;
                    img._y = 2;
                    _local2.w = _local2.w + 4;
                    _local2.h = _local2.h + 4;
                    stroke._width = _local2.w;
                    stroke._height = _local2.h;
                    stroke._x = 0;
                    stroke._y = 0;
                } else {
                    var _local2 = new Object();
                    _local2.w = _local5;
                    _local2.h = _local6;
                }
                tw = _local2.w + 60;
                th = (_local2.h + 80) + 140;
                titleMask._width = tw - 90;
                line._width = tw - 34;
                close._x = titleMask._width;
                ht._y = Math.round(((th - 27) - 100) - 24);
                mask._width = Math.round(tw - 60);
                html.txt._width = Math.round(mask._width - 30);
                scroller._x = Math.round(mask._width - scroller._width);
                ScrollBox();
                updateContentPosition();
                if (scroller._visible == false) {
                    th = (th - 100) + html._height;
                }
                if (html._visible == false) {
                    th = th - 40;
                }
                buildBackground();
                buildNavigation();
                _x = Math.round((Stage.width / 2) - (bg._width / 2));
                _y = Math.round((Stage.height / 2) - (bg._height / 2));
            } else {
                var _local4 = 0.7;
                var _local3 = "easeOutQuart";
                caurina.transitions.Tweener.addTween(loader, {_x:Math.round((_local5 / 2) - (loader._width / 2)), _y:Math.round((_local6 / 2) - (loader._height / 2)), time:_local4, transition:_local3, rounded:true});
                var _local2 = oxylus.Utils.getDims("fit", img._width, img._height, _local5 - 4, _local6 - 4, true);
                img._width = _local2.w;
                img._height = _local2.h;
                img._x = ((_local5 / 2) - (_local2.w / 2)) + 2;
                img._y = ((_local6 / 2) - (_local2.h / 2)) + 2;
                caurina.transitions.Tweener.addTween(img, {_x:2, _y:2, time:_local4, transition:_local3, rounded:true});
                _local2.w = _local2.w + 4;
                _local2.h = _local2.h + 4;
                stroke._width = _local2.w;
                stroke._height = _local2.h;
                stroke._x = (_local5 / 2) - (_local2.w / 2);
                stroke._y = (_local6 / 2) - (_local2.h / 2);
                caurina.transitions.Tweener.addTween(stroke, {_x:0, _y:0, time:_local4, transition:_local3, rounded:true});
                tw = _local2.w + 60;
                th = (_local2.h + 80) + 140;
                caurina.transitions.Tweener.addTween(titleMask, {_width:tw - 90, time:_local4, transition:_local3, rounded:true});
                caurina.transitions.Tweener.addTween(line, {_width:tw - 34, time:_local4, transition:_local3, rounded:true});
                caurina.transitions.Tweener.addTween(close, {_x:tw - 90, time:_local4, transition:_local3, rounded:true});
                caurina.transitions.Tweener.addTween(ht, {_y:Math.round(((th - 27) - 100) - 24), time:_local4, transition:_local3, rounded:true});
                caurina.transitions.Tweener.addTween(mask, {_width:Math.round(tw - 60), time:_local4, transition:_local3, rounded:true});
                caurina.transitions.Tweener.addTween(html.txt, {_width:Math.round((tw - 60) - 30), time:_local4, transition:_local3, rounded:true, onUpdate:ascb.util.Proxy.create(this, updateOthersByHtml), onComplete:ascb.util.Proxy.create(this, tweensFinished)});
                caurina.transitions.Tweener.addTween(scroller, {_x:Math.round((tw - 60) - scroller._width), time:_local4, transition:_local3, rounded:true});
            }
        }
        function killTweens() {
            caurina.transitions.Tweener.removeTweens(this);
            caurina.transitions.Tweener.removeTweens(scroller);
            caurina.transitions.Tweener.removeTweens(html.txt);
            caurina.transitions.Tweener.removeTweens(mask);
            caurina.transitions.Tweener.removeTweens(ht);
            caurina.transitions.Tweener.removeTweens(close);
            caurina.transitions.Tweener.removeTweens(line);
            caurina.transitions.Tweener.removeTweens(titleMask);
            caurina.transitions.Tweener.removeTweens(loader);
        }
        function tweensFinished() {
            init = 0;
            killTweens();
        }
        function updateOthersByHtml() {
            ScrollBox();
            updateContentPosition();
            if (scroller._visible == false) {
                var _local4 = html._height - 100;
            } else {
                var _local4 = 0;
            }
            var _local3 = (html.txt._width + 60) + 30;
            var _local2 = (((ht._y + 27) + 100) + 16) + _local4;
            if (html._visible == false) {
                _local2 = _local2 - 32;
            }
            drawOval(bg, _local3, _local2, 6, 0, 90);
            drawOval(navigation.bg, _local3 + 80, 196, 6, 0, 80);
            next._x = Math.round((navigation.bg._width - next._width) - 8);
            prev._x = 8;
            next._y = (prev._y = Math.round((navigation.bg._height / 2) - (next._height / 2)));
            addShadow(navigation.bg);
            navigation._x = Math.round((_local3 / 2) - (navigation._width / 2));
            navigation._y = Math.round((_local2 / 2) - (navigation._height / 2));
            _x = Math.round((Stage.width / 2) - (_local3 / 2));
            _y = Math.round((Stage.height / 2) - (_local2 / 2));
        }
        function onResize() {
            if ((Stage.width - 200) > 800) {
                var _local2 = 800;
            } else {
                var _local2 = Stage.width - 200;
            }
            if ((Stage.height - 60) > 800) {
                var _local3 = 800;
            } else {
                var _local3 = Stage.height - 60;
            }
            if (_local2 < 400) {
                var _local2 = 400;
            }
            if (_local3 < 500) {
                var _local3 = 500;
            }
            resize(_local2, _local3);
        }
        function loadStageResize() {
            Stage.addListener(this);
            this.onResize();
        }
        function drawOval(_arg1, _arg3, _arg4, _arg2, _arg6, _arg5) {
            _arg1.clear();
            _arg1.beginFill(_arg6, _arg5);
            _arg1.lineStyle(1, 2434341, _arg5, true);
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
        function addShadow(_arg14) {
            var _local6 = 1;
            var _local8 = 45;
            var _local7 = 0;
            var _local4 = 0.25;
            var _local3 = 6;
            var _local2 = 6;
            var _local12 = 3;
            var _local10 = 3;
            var _local11 = false;
            var _local13 = false;
            var _local9 = false;
            var _local5 = new flash.filters.DropShadowFilter(_local6, _local8, _local7, _local4, _local3, _local2, _local12, _local10, _local11, _local13, _local9);
            var _local1 = new Array();
            _local1.push(_local5);
            _arg14.filters = _local1;
        }
        function ScrollBox() {
            ScrollArea = stick;
            ScrollButton = bar;
            Content = html;
            ContentMask = mask;
            HitZone = ContentMask.duplicateMovieClip("_hitzone_", getNextHighestDepth());
            HitZone._alpha = 0;
            HitZone._width = ContentMask._width;
            HitZone._height = ContentMask._height;
            Content.setMask(ContentMask);
            ScrollArea.onPress = ascb.util.Proxy.create(this, startScroll);
            ScrollArea.onRelease = (ScrollArea.onReleaseOutside = ascb.util.Proxy.create(this, stopScroll));
            totalHeight = Content._height;
            scrollable = false;
            updateScrollbar();
            Mouse.addListener(this);
            ScrollButton.onRollOver = ascb.util.Proxy.create(this, barOnRollOver);
            ScrollButton.onRollOut = ascb.util.Proxy.create(this, barOnRollOut);
            ScrollButton.onPress = ascb.util.Proxy.create(this, startScroll);
            ScrollButton.onRelease = (ScrollButton.onReleaseOutside = ascb.util.Proxy.create(this, stopScroll));
        }
        function updateScrollbar() {
            viewHeight = ContentMask._height;
            var _local2 = viewHeight / totalHeight;
            if (_local2 >= 1) {
                scrollable = false;
                scroller._alpha = 0;
                ScrollArea.enabled = false;
                ScrollButton._y = 0;
                Content._y = 0;
                scroller._visible = false;
            } else {
                scrollable = true;
                ScrollButton._visible = true;
                ScrollArea.enabled = true;
                ScrollButton._y = 0;
                scroller._alpha = 100;
                ScrollHeight = ScrollArea._height - ScrollButton._height;
                if (ScrollButton._height > ScrollArea._height) {
                    scrollable = false;
                    scroller._alpha = 0;
                    ScrollArea.enabled = false;
                    ScrollButton._y = 0;
                    Content._y = 0;
                }
                scroller._alpha = 100;
                scroller._visible = true;
            }
        }
        function startScroll() {
            var _local4 = !ScrollButton.hitTest(_level0._xmouse, _level0._ymouse, true);
            var _local3 = ScrollButton._x;
            if (_local4) {
                var _local2 = ScrollButton._parent._ymouse - (ScrollButton._height / 2);
                ((_local2 < 0) ? (_local2 = 0) : (((_local2 > ScrollHeight) ? (_local2 = ScrollHeight) : null)));
                ScrollButton._y = _local2;
            }
            ScrollButton.startDrag(false, _local3, 0, _local3, ScrollHeight);
            ScrollButton.onMouseMove = ascb.util.Proxy.create(this, updateContentPosition);
            updateContentPosition();
        }
        function stopScroll() {
            ScrollButton.stopDrag();
            delete ScrollButton.onMouseMove;
            barOnRollOut();
        }
        function updateContentPosition() {
            if (scrollable == true) {
                var contentPos = ((viewHeight - totalHeight) * (ScrollButton._y / ScrollHeight));
                onEnterFrame = function () {
                    if (Math.abs(this.Content._y - contentPos) < 1) {
                        this.Content._y = contentPos;
                        delete this.onEnterFRame;
                        return(undefined);
                    }
                    this.Content._y = this.Content._y + ((contentPos - this.Content._y) / 4);
                };
            } else {
                Content._y = 0;
                delete Content.onEnterFRame;
            }
        }
        function scrollDown() {
            var _local2 = ScrollButton._y + (ScrollButton._height / 4);
            if (_local2 > ScrollHeight) {
                _local2 = ScrollHeight;
            }
            ScrollButton._y = _local2;
            updateContentPosition();
        }
        function scrollUp() {
            var _local2 = ScrollButton._y - (ScrollButton._height / 4);
            if (_local2 < 0) {
                _local2 = 0;
            }
            ScrollButton._y = _local2;
            updateContentPosition();
        }
        function onMouseWheel(_arg3) {
            if (!HitZone.hitTest(_level0._xmouse, _level0._ymouse, true)) {
                return(undefined);
            }
            var _local2 = _arg3 / Math.abs(_arg3);
            if (_local2 < 0) {
                scrollDown();
            } else {
                scrollUp();
            }
        }
        function barOnRollOver() {
            caurina.transitions.Tweener.addTween(bar, {_alpha:60, time:0.15, transition:"linear"});
        }
        function barOnRollOut() {
            caurina.transitions.Tweener.addTween(bar, {_alpha:35, time:0.15, transition:"linear"});
        }
        var videoPresent = 0;
        var init = 0;
        var loaded = 0;
        var tw = 500;
        var th = 500;
        var blurAmountX = 40;
        var blurAmountY = 0;
        var animationTime = 0.5;
        var animationType = "easeOutQuart";
    }