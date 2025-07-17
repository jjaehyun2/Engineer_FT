package flash.display {
    import flash.events.EventDispatcher;

    public class DisplayObject extends EventDispatcher {
        public function DisplayObject() {
        }

        private var _htmlElement:HTMLElement = null;

        internal function set htmlElement(n:HTMLElement):void {
            _htmlElement = n;
            _htmlElement['__displayObject'] = this;
        }

        public function get htmlElement():HTMLElement {
            return _htmlElement;
        }

        public function get stage():Stage {
            return parent ? parent.stage : null;
        }

        private var _parent:DisplayObjectContainer = null;

        public function get parent():DisplayObjectContainer {
            return _parent;
        }

        internal function setParent(v:DisplayObjectContainer):void {
            _parent = v;
        }

        internal static function getRelatedDisplayObjectOfHtmlElement(e:HTMLElement):DisplayObject {
            return e['__displayObject'];
        }

        private var _name:String = "";

        public function set name(v:String):void {
            _name = v;
        }

        public function get name():String {
            return _name;
        }

        private var _x:Number = 0;

        public function get x():Number {
            return _x;
        }

        public function set x(v:Number):void {
            htmlElement.style.transform = "translateX(" + v + "px)";
            _x = v;
        }

        private var _y:Number = 0;

        public function get y():Number {
            return _y;
        }

        public function set y(v:Number):void {
            htmlElement.style.transform = "translateY(" + v + "px)";
            _y = v;
        }

        private var _z:Number = 0;

        public function get z():Number {
            return _z;
        }

        public function set z(v:Number):void {
            _z = v;
            htmlElement.style.transform = "translateZ(" + v + "px)";
        }
    }
}