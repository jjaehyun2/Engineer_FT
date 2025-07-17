package jp.coremind.view.layout
{
    import flash.geom.Rectangle;
    
    import jp.coremind.view.abstract.IBox;
    
    public class Layout
    {
        public static const EQUAL_PARENT_TL:Layout = new Layout();
        public static const ATLAS_CENTER:Layout = new Layout(
                new Align().parentStandard(.5).childStandard(-.5),
                new Align().parentStandard(.5).childStandard(-.5))
        
        private var
            _width:Size,
            _height:Size,
            _horizontalAlign:Align,
            _verticalAlign:Align;
        
        public function Layout(
            horizontalAlign:Align = null,
            verticalAlign:Align = null,
            width:Size = null,
            height:Size = null)
        {
            _horizontalAlign = horizontalAlign || Align.LEFT;
            _verticalAlign   = verticalAlign   || Align.TOP;
            _width  = width  || Size.PARENT_EQUAL;
            _height = height || Size.PARENT_EQUAL;
        }
        
        public function clone():Layout
        {
            return new Layout(
                _horizontalAlign.clone(),
                _verticalAlign.clone(),
                _width.clone(),
                _height.clone());
        }
        
        public function applyDisplayObject(displayObject:IBox, actualParentWidth:int, actualParentHeight:int):void
        {
            displayObject.width  = _width.calc(actualParentWidth);
            displayObject.height = _height.calc(actualParentHeight);
            displayObject.x      = _horizontalAlign.calc(actualParentWidth, displayObject.width);
            displayObject.y      = _verticalAlign.calc(actualParentHeight, displayObject.height);
        }
        
        /**
         * このレイアウトオブジェクトで定義されている相対サイズ、相対ポジションを
         * actualParentWidth, actualParentHeightパラメータを元に算出し結果をRectangleオブジェクトとして返す.
         * rectパラメータが指定されている場合、そのオブジェクトに算出結果を反映して返す。
         */
        public function exportRectangle(
            actualParentWidth:int,
            actualParentHeight:int,
            rect:Rectangle = null):Rectangle
        {
            rect = rect || new Rectangle();
            
            var w:Number = _width.calc(actualParentWidth);
            var h:Number = _height.calc(actualParentHeight);
            
            rect.setTo(
                _horizontalAlign.calc(actualParentWidth, w),
                _verticalAlign.calc(actualParentHeight, h),
                w,
                h);
            
            return rect;
        }
        
        public function get width():Size
        {
            return _width;
        }

        public function get height():Size
        {
            return _height;
        }

        public function get horizontalAlign():Align
        {
            return _horizontalAlign;
        }

        public function get verticalAlign():Align
        {
            return _verticalAlign;
        }
    }
}