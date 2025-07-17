package flash.ui
{
    import flash.display.*;

    final public class ContextMenuItem extends NativeMenuItem
    {

        public function ContextMenuItem(param1:String, param2:Boolean = false, param3:Boolean = true, param4:Boolean = true)
        {
            this.caption = param1;
            this.separatorBefore = param2;
            this.enabled = param3;
            this.visible = param4;
            return;
        }// end function

        public function get caption() : String;

        public function set caption(param1:String) : void;

        public function get separatorBefore() : Boolean;

        public function set separatorBefore(param1:Boolean) : void;

        public function get visible() : Boolean;

        public function set visible(param1:Boolean) : void;

        public function clone() : ContextMenuItem
        {
            var _loc_1:* = new ContextMenuItem(this.caption, this.separatorBefore, this.enabled, this.visible);
            return _loc_1;
        }// end function

    }
}