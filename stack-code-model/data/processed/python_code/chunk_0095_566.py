package jp.coremind.view.layout
{
    import flash.geom.Rectangle;
    
    import jp.coremind.configure.IElementBluePrint;
    import jp.coremind.core.Application;
    import jp.coremind.storage.ModelReader;
    import jp.coremind.utility.Log;
    import jp.coremind.utility.process.Routine;
    import jp.coremind.view.abstract.IElement;
    import jp.coremind.view.builder.IDisplayObjectBuilder;
    import jp.coremind.view.builder.list.ListElementFactory;

    public class FlexibleLayout implements IListLayout
    {
        private var
            _builderList:Vector.<String>,
            _elementfactory:ListElementFactory, 
            _rect:Rectangle;
        
        public function FlexibleLayout(temporaryRect:Rectangle = null)
        {
            _elementfactory = new ListElementFactory();
            
            _rect = temporaryRect;
            
            _builderList = new <String>[];
        }
        
        public function destroy(withReference:Boolean = false):void
        {
            _builderList.length = 0;
            
            _rect = null;
            
            if (withReference)
                _elementfactory.destroy();
            
            _elementfactory = null;
        }
        
        public function requestElement(actualParentWidth:int, actualParentHeight:int, modelData:*, index:int = -1, length:int = -1):IElement
        {
            return _elementfactory.request(actualParentWidth, actualParentHeight, modelData, index, length);
        }
        
        public function createElement(actualParentWidth:int, actualParentHeight:int, modelData:*, index:int):IElement
        {
            return _elementfactory.create(actualParentWidth, actualParentHeight, modelData, index, length);
        }
        
        public function requestRecycle(modelData:*):void
        {
            _elementfactory.recycle(modelData);
        }
        
        public function refreshCacheKey():void
        {
            _elementfactory.refreshKey();
        }
        
        public function getScrollSizeX(actualParentWidth:Number):Number
        {
            return 1;
        }
        
        public function getScrollSizeY(actualParentHeight:Number):Number
        {
            return 1;
        }
        
        public function hasCache(modelData:*):Boolean
        {
            return _elementfactory.hasElement(modelData);
        }
        
        public function initialize(reader:ModelReader):void
        {
            
        }
        
        public function appendElement(builder:IElementBluePrint):FlexibleLayout
        {
            _builderList.push(builder);
            return this;
        }
        
        public function calcTotalRect(actualParentWidth:int, actualParentHeight:int, length:int = 0):Rectangle
        {
            var temp:Rectangle = _rect;
            var _minX:Number  = 0;
            var _minY:Number  = 0;
            var _maxX:Number = 0;
            var _maxY:Number = 0;
            
            _rect = new Rectangle();
            for (var i:int, len:int = _builderList.length; i < len; i++)
            {
                calcElementRect(actualParentWidth, actualParentHeight, i, length);
                if (_rect.x < _minX)     _minX  = _rect.x;
                if (_rect.y < _minY)     _minY  = _rect.y;
                if (_maxX  < _rect.left) _maxX = _rect.left;
                if (_maxY  < _rect.y)    _maxY = _rect.bottom;
            }
            _rect = temp;
            
            var result:Rectangle = _rect || new Rectangle();
            result.setTo(0, 0, _maxX - _minX, _maxY - _minY);
            
            return result;
        }
        
        public function calcElementRect(actualParentWidth:int, actualParentHeight:int, index:int, length:int = 0):Rectangle
        {
            var builder:IDisplayObjectBuilder = _getBuilder(index);
            var result:Rectangle = _rect || new Rectangle();
            
            if (builder)
                builder.layout.exportRectangle(actualParentWidth, actualParentHeight, result);
            
            return result;
        }
        
        private function _getBuilder(index:int):IDisplayObjectBuilder
        {
            if (0 <= index && index < _builderList.length)
            {
                var bluePrint:IElementBluePrint = Application.configure.elementBluePrint;
                return bluePrint.createBuilder(_builderList[index]);
            }
            else
            {
                Log.error("[FlexibleLayout]", index, " is undefined.");
                return null;
            }
        }
        
        public function getTweenRoutineByAddedStage(modelData:*):Function
        {
            return Routine.SKIP;
        }
        
        public function getTweenRoutineByMoved(modelData:*):Function
        {
            return Routine.SKIP;
        }
        
        public function getTweenRoutineByRemovedStage(modelData:*):Function
        {
            return Routine.SKIP;
        }
    }
}