package jp.coremind.view.implement.flash.buildin
{
    import flash.geom.Point;
    import flash.text.TextField;
    
    import jp.coremind.view.abstract.IDisplayObject;
    import jp.coremind.view.abstract.IDisplayObjectContainer;
    
    public class TextField extends flash.text.TextField implements IDisplayObject
    {
        public function TextField()
        {
            super();
        }
        
        public function get parentDisplay():IDisplayObjectContainer
        {
            return parent as IDisplayObjectContainer;
        }
        
        public function toGlobalPoint(localPoint:Point, resultPoint:Point = null):Point
        {
            var p:Point = localToGlobal(localPoint);
            if (resultPoint)
            {
                resultPoint.setTo(p.x, p.y);
                return resultPoint;
            }
            else return p;
        }
        
        public function toLocalPoint(globalPoint:Point, resultPoint:Point = null):Point
        {
            var p:Point = globalToLocal(globalPoint);
            if (resultPoint)
            {
                resultPoint.setTo(p.x, p.y);
                return resultPoint;
            }
            else return p;
        }
        
        public function enablePointerDeviceControl():void
        {
            mouseEnabled = true;
        }
        
        public function disablePointerDeviceControl():void
        {
            mouseEnabled = false;
        }
    }
}