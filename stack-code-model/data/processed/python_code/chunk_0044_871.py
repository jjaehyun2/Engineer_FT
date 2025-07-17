package h2olib.control.headerRenderer 
{
    import flash.display.DisplayObject;
    import flash.events.FocusEvent;
    import flash.events.MouseEvent;
    
    import mx.collections.ListCollectionView;
    import mx.containers.Canvas;
    import mx.containers.HBox;
    import mx.containers.VBox;
    import mx.controls.DataGrid;
    import mx.controls.Label;
    import mx.controls.TextInput;
    import mx.controls.dataGridClasses.DataGridColumn;
    import mx.core.IFlexDisplayObject;
    import mx.core.UIComponent;

    public class BaseHeaderRenderer extends Canvas
    {
        private var _vbox:VBox;
        private var _label:Label;
        private var _hbox:HBox;

        [Bindable]
        public var sharedData:FilterObject;

        [Bindable]
        public var dataProvider:ListCollectionView;

        public var dataFunction:Function;

        public function BaseHeaderRenderer()
        {
            super();
            this.setStyle("top","0");
            this.setStyle("borderThickness","0");
            if (!this.sharedData) 
            {
                this.sharedData = new FilterObject();
            }

            this.verticalScrollPolicy = "off";
            this.horizontalScrollPolicy = "off";
        }

        public function saveData(value:Object) : void 
        {
            sharedData.saveElement(_column,value);
            sharedData.saveFocus(_column);

            if (!this.dataProvider || (this.dataProvider.filterFunction != filter))
            if ((this.parent != null) &&
                (this.parent.parent is DataGrid) //) {
                && ((this.parent.parent as DataGrid).dataProvider is ListCollectionView)) 
            {

                this.dataProvider = ((this.parent.parent as DataGrid).dataProvider as ListCollectionView);
                if (dataProvider.filterFunction != filter) 
                {
                    dataProvider.filterFunction = filter;
                }
            }
        }

        public function refreshDataProvider():void 
        {
            if (this.dataProvider) 
            {
                dataProvider.refresh();
            }
        }

        private var _focusElement:UIComponent;

        public function set focusElement(value:UIComponent):void 
        {
            this._focusElement = value;

            if (this._focusElement) 
            {
                this._focusElement.addEventListener(FocusEvent.FOCUS_OUT, loseFocusHandler);
            }

            if (sharedData.isFocused(_column)) 
            {
                _focusElement.setFocus();
                if(_focusElement is TextInput) 
                {
                    var len:int = (_focusElement as TextInput).length;
                    (_focusElement as TextInput).setSelection(len,len);
                }
            }
        }

        public function get focusElement():UIComponent 
        {
            return this._focusElement;
        }

        private function loseFocusHandler(event:FocusEvent):void 
        {
            sharedData.clearFocus();
        }

        public function getData():Object 
        {
            return sharedData.restoreElement(_column);
        }

        protected function filter(item:Object):Boolean 
        {
            var isMatched:Boolean = true;

            var col:DataGridColumn = this.sharedData.getFirstColumn();

            while(col != null) {
                if(sharedData.restoreElement(col) != null) 
                {

                    var buf:String = col.itemToLabel(item).toLowerCase();
                    var str:String = (sharedData.restoreElement(col) as String).toLowerCase();
                    if(buf.indexOf(str.toLowerCase())<0) 
                    {
                        isMatched = false;
                    }
                }
                col = this.sharedData.getNextColumn();
            }

            return isMatched;
        }

        private var _column:DataGridColumn;

        override public function get data():Object 
        {
            return _column;
        }

        override public function set data(value:Object):void 
        {
            super.data = value;
            if (value is DataGridColumn) 
            {
                _column = value as DataGridColumn;
                sharedData.addColumn(_column);
            }
        }

        override public function initialize():void 
        {
            super.initialize();

            if(this._label && _column) 
            {
                this._label.text = _column.headerText;
            }

            if ((this.parent != null) &&
            (this.parent.parent is DataGrid) //) {
            && ((this.parent.parent as DataGrid).dataProvider is ListCollectionView))
            {
                this.dataProvider = ((this.parent.parent as DataGrid).dataProvider as ListCollectionView);
            }

            if (_column && sharedData.sortable(_column))
            {
                var sortArrow:IFlexDisplayObject
                            = new BaseSortArrow(sharedData.direction(_column));
                DisplayObject(sortArrow).name = "sortArrow";

                var sortArrowHitArea:UIComponent = new UIComponent();
                sortArrowHitArea.width = 10;
                DisplayObject(sortArrow).y = 3;
                sortArrowHitArea.addChild(DisplayObject(sortArrow));

                this._hbox.addChild(sortArrowHitArea);

                this.verticalScrollPolicy = "off";
                this.horizontalScrollPolicy = "off";
            }
        }

        public function addControlElement(object:UIComponent):void 
        {
            if(!this._vbox) 
            {
                this.percentWidth = 100;
                this._vbox = new VBox();
                this._vbox.percentWidth = 100;
                this._vbox.minWidth=0;

                this._hbox = new HBox();
                this._hbox.percentWidth = 100;
                this._hbox.addEventListener(MouseEvent.MOUSE_UP, labelClickHandler);

                this._label = new Label();
                this._label.percentWidth = 100;



                this._label.setStyle("fontWeight","bold");
                this._label.minWidth = 0;

                object.addEventListener(MouseEvent.MOUSE_UP, clickHandler);
                object.addEventListener(MouseEvent.MOUSE_DOWN, clickHandler);
                object.addEventListener(MouseEvent.MOUSE_MOVE, clickHandler);

                this._vbox.addChild(object);
                this._hbox.addChild(this._label);

                this._vbox.addChild(this._hbox);
                this.addChild(this._vbox);

                focusElement = object;
            }
        }

        private function labelClickHandler(event:MouseEvent):void 
        {
            if (this.parent &&
                this.parent.parent &&
                (this.parent.parent is DataGrid) &&
                (this.parent.parent as DataGrid).sortableColumns &&
                this._column.sortable) 
            {
                sharedData.sortColumn(_column);
            }
        }

        private function clickHandler(event:MouseEvent):void
        {
            event.stopImmediatePropagation();
        }
    }
}