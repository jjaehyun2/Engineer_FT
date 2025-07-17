package com.unhurdle.spectrum
{
    public class Label extends TextBase
    {
    /**
     * <inject_html>
     * <link rel="stylesheet" href="assets/css/components/label/dist.css">
     * </inject_html>
     * 
     */
        public function Label()
        {
            super();
            color = "grey";
        }
        override protected function getSelector():String{
          return "spectrum-Label";
        }

        private var _color:String;

        /**
         * color can be one of:
         * grey
         * red
         * orange
         * yellow
         * seafoam
         * green
         * blue
         * fuchsia
         * 
         * It can also be:
         * active (blue)
         * inactive (grey)
         * 
         */
        public function get color():String
        {
            return _color;
        }

        [Inspectable(category="General", enumeration="grey,red,orange,yellow,seafoam,green,blue,fuchsia,active,inactive", defaultValue="grey")]
        public function set color(value:String):void
        {
            if(value != _color){
                var newColor:String = valueToSelector(value);
                toggle(newColor, true);
                if(_color){
                    var oldColor:String = valueToSelector(_color);
                    toggle(oldColor, false);
                }
                _color = value;
            }
        }
        private var _size:String;
        
        /**
         * size by default is "normal" or no value
         * It can be set to "large" or "small" as well
         */
        public function get size():String
        {
        	return _size;
        }

        [Inspectable(category="General", enumeration="small,large,normal")]
        public function set size(value:String):void
        {
            if(value != _size){
                switch(value){
                    case "small":
                    case "large":
                    case "normal":
                    case "":
                        break;
                    default:
                        throw new Error("Invalid scale: " + value);
                }
                if(_size){
                    toggle(valueToSelector(_size),false);
                }
                // normal has no selector
                if(value == "small" || value == "large"){
                    toggle(valueToSelector(value),true);
                }
                _size = value;
            }
        }

        override protected function getTag():String{
            return "span";
        }

    }
}