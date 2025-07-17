package flash.ui
{

    final public class ContextMenuClipboardItems extends Object
    {
        private var _cut:Boolean = false;
        private var _copy:Boolean = false;
        private var _paste:Boolean = false;
        private var _clear:Boolean = false;
        private var _selectAll:Boolean = true;

        public function ContextMenuClipboardItems()
        {
            return;
        }// end function

        public function get cut() : Boolean
        {
            return this._cut;
        }// end function

        public function set cut(param1:Boolean) : void
        {
            this._cut = param1;
            return;
        }// end function

        public function get copy() : Boolean
        {
            return this._copy;
        }// end function

        public function set copy(param1:Boolean) : void
        {
            this._copy = param1;
            return;
        }// end function

        public function get paste() : Boolean
        {
            return this._paste;
        }// end function

        public function set paste(param1:Boolean) : void
        {
            this._paste = param1;
            return;
        }// end function

        public function get clear() : Boolean
        {
            return this._clear;
        }// end function

        public function set clear(param1:Boolean) : void
        {
            this._clear = param1;
            return;
        }// end function

        public function get selectAll() : Boolean
        {
            return this._selectAll;
        }// end function

        public function set selectAll(param1:Boolean) : void
        {
            this._selectAll = param1;
            return;
        }// end function

        public function clone() : ContextMenuClipboardItems
        {
            var _loc_1:* = new ContextMenuClipboardItems();
            _loc_1.cut = this.cut;
            _loc_1.copy = this.copy;
            _loc_1.paste = this.paste;
            _loc_1.clear = this.clear;
            _loc_1.selectAll = this.selectAll;
            return _loc_1;
        }// end function

    }
}