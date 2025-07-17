class oxylus.afsmg.background extends MovieClip
    {
        var bg, grad;
        function background () {
            super();
            bg = bg;
            grad.up._y = -4;
            loadStageResize();
            caurina.transitions.Tweener.addTween(this, {_alpha:100, time:0.5, transition:"linear"});
        }
        function resize(_arg3, _arg2) {
            grad.up._width = (grad.down._width = _arg3 + 4);
            grad.down._y = Math.round((_arg2 - grad.down._height) + 4);
            backgroundResize(_arg3, _arg2);
        }
        function onResize() {
            resize(Stage.width, Stage.height);
        }
        function loadStageResize() {
            Stage.addListener(this);
            this.onResize();
        }
        function backgroundResize(_arg5, _arg9) {
            var _local2 = 0;
            var _local3 = 0;
            if ((bg._width < _arg5) || (bg._height < _arg9)) {
                var _local4 = 1;
                while (bg["copy" + _local4]) {
                    bg["copy" + _local4].removeMovieClip();
                    _local4++;
                }
                do {
                    if (_local2 >= _arg5) { 
                        break;
                    }
                    bgIdx++;
                    _local2 = _local2 + bg.copy._width;
                    var _local6 = bg.copy.duplicateMovieClip("copy" + bgIdx, bg.getNextHighestDepth(), {_x:_local2, _y:_local3});
                    if (_local2 >= _arg5) {
                        _local2 = -bg.copy._width;
                        _local3 = _local3 + bg.copy._height;
                    }
                } while  (_local3 <= _arg9);
            }
        }
        var bgIdx = 0;
    }