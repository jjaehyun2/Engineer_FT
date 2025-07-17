package h2olib.control.headerRenderer
{
    import mx.controls.dataGridClasses.DataGridColumn;

    [Bindable]
    public dynamic class FilterObject extends Object 
    {
        private var list:Array = new Array();

        private var columns:Array = new Array();

        private var sortCol:int = -1;

        private var _direction:int = 1;

        /**
         * Constructor.
         */
        public function FilterObject() 
        {
            super();
        }

        /**
         * restore filtering element value
         */
        public function restoreElement(object:DataGridColumn):Object 
        {
            var i:int = columns.indexOf(object);
            if (i >= 0) 
            {
                if(list[i]) 
                {
                    return(list[i]);
                }
            }
            return null;
        }

        /**
         * saving filtering element value
         */
        public function saveElement(object:DataGridColumn, value:Object):void 
        {
            var i:int = columns.indexOf(object);
            if (i >= 0) 
            {
                if(list[i]) 
                {
                    if(value) 
                    {
                        list[i] = value;
                    } 
                    else 
                    {
                        list[i] = null;
                    }
                }
                else 
                {
                    if(value) 
                    {
                        list[i] = new Object();
                        list[i] = value;
                    }
                }
            } 
            else 
            {
                this.columns.push(object);
                i = columns.indexOf(object);
                list[i] = new Object();
                list[i] = value;
            }
        }

        /**
         * add new column to array
         */
        public function addColumn(object:DataGridColumn):void 
        {
            var i:int = columns.indexOf(object);
            if(i<0) 
            {
                columns.push(object);
            }
        }

        /**
         * returns position of asked column
        */
        public function getColumnPos(object:DataGridColumn):int 
        {
            return columns.indexOf(object);
        }

        /**
         * return true if element is active
         */
        public function isFocused(object:DataGridColumn):Boolean 
        {
            if ((this["focus"] != null) &&
                (this["focus"] == getColumnPos(object))) 
            {
                return true;
            }
            return false;
        }

        /**
         * save focused element index
         */
        public function saveFocus(object:DataGridColumn):void 
        {
            this["focus"] = new Object();
            this["focus"] = getColumnPos(object);
        }

        /**
         * clear focus data
         */
        public function clearFocus():void 
        {
            if (this["focus"])
                this["focus"] = null;
        }

        private var _i:int=0;

        public function getFirstColumn():DataGridColumn 
        {
            _i=0;
            if (columns.length > 0) 
            {
                while((columns[_i] == null) && (columns.length > _i)) 
                {
                    _i++;
                }
                return this.columns[_i];
            }
            return null;
        }

        public function getNextColumn():DataGridColumn 
        {
            _i++;
            if (columns.length > _i) 
            {
                while((columns[_i] == null) && (columns.length > _i)) 
                {
                    _i++;
                }
                return this.columns[_i];
            }
            return null;
        }

        public function clearData():void 
        {
            this.list = new Array();
        }

        public function direction(object:DataGridColumn):int 
        {
            return _direction;
        }

        public function sortable(object:DataGridColumn):Boolean 
        {
            return sortCol == columns.indexOf(object);
        }

        public function sortColumn(object:DataGridColumn):void 
        {
            if (sortCol<0 || sortCol!=columns.indexOf(object)) 
            {
                sortCol=columns.indexOf(object);
                _direction = object.sortDescending ? 1 : -1;
            } 
            
            else if (sortCol == columns.indexOf(object)) {
                _direction *= -1;
            }
        }
    }
}