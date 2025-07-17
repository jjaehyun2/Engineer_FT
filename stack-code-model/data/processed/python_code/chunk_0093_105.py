package h2olib.control {
    import flash.events.Event;
    import flash.events.FocusEvent;
    import flash.events.KeyboardEvent;
    import flash.ui.Keyboard;
    
    import h2olib.control.comboBoxClasses.TooltipListItemRenderer;
    
    import mx.collections.ListCollectionView;
    import mx.controls.ComboBox;
    import mx.core.ClassFactory;
    import mx.core.mx_internal;
    import mx.events.DropdownEvent;
    import mx.events.FlexEvent;
    import mx.events.ListEvent;

    use namespace mx_internal;

    /**
     *  The AdvancedComboBox class is extended implementation of ComboBox control.
     *
     *  It allows to select an item using the provided key value.
     *
     *  Example of using:
     *  <blockquote>
     *  <code><AdvancedComboBox dataProvider="{currencies}" keyField="code" selectedKeyValue="currentUser.preferredCurrencyCode"/></code>
     *  </blockquote>
     *
     *  It also provides more easer way to use item tooltips in dropdown list.
     *  By default tooltip field is 'tooltip'. You can have member 'tooltip' in
     *  your item classes. Otherwise you need to specify <code>tooltipField</code>
     *  manually.
     *
	 * @author Anton Kirzyk / Ramada
	 *
	 * @version $Revision 1.0 $ $Date: 2009/06/24 $
     */
     
  
    public class AdvancedComboBox extends ComboBox 
    {

        /**
         *  Constructor.
         */
        public function AdvancedComboBox() 
        {
            super();

            addEventListener(DropdownEvent.OPEN, dropdownOpenHandler);
            itemRenderer = new ClassFactory(TooltipListItemRenderer);
        }


        //---------------------------------------------
        //  Key field
        //---------------------------------------------

        private var _keyField:String = "id";

        /**
         *  Name of the key field in the items in the <code>dataProvider</code>.
         *  Used to select item by key.
         *
         *  @default Value of <code>labelField</code> property.
         */
        public function get keyField():String 
        {
            return _keyField;
        }

        public function set keyField(value:String):void 
        {
            _keyField = value;
        }

        //---------------------------------------------
        //  Selected key value
        //---------------------------------------------

        private var selectedKeyValueChanged:Boolean;

        private var _selectedKeyValue:Object;

        public function get selectedKeyValue():Object 
        {
            return _selectedKeyValue;
        }

        /**
         *  Selects an item by <code>keyField</code> if it exists in the dataProvider.
         */
        public function set selectedKeyValue(value:Object):void 
        {
            _selectedKeyValue = value;
            selectedKeyValueChanged = true;
            invalidateProperties();
        }

        override public function set selectedIndex(value:int):void 
        {
            if (selectedIndex != value) {
                super.selectedIndex = value;
                if (selectedItem && keyField in selectedItem) 
                {
                    selectedKeyValue = selectedItem[keyField];
                }
            }
        }

        override public function get selectedLabel():String 
        {
            var result:String = super.selectedLabel;
            if (!result.length && editable) 
            {
                return text;
            }
            return result;
        }

        //---------------------------------------------
        //  Data Provider
        //---------------------------------------------

        /**
         * Sets selectedKeyValueChanged before invalidateProperties() call
         *
         * @param value
         *
         */
        override public function set dataProvider(value:Object):void 
        {
            super.dataProvider = value;
            collectionChanged = true;
            selectedKeyValueChanged = true;
        }

        //---------------------------------------------
        //  Prompt
        //---------------------------------------------

        override public function set prompt(value:String):void 
        {
            super.prompt = value;
            selectedIndex = -1;
            promptChanged = true;
            invalidateDisplayList();
        }

        private var promptChanged:Boolean;

        //---------------------------------------------
        //  Prompt format
        //---------------------------------------------

        /** Storage for the promptFormat property */
        private var _promptFormat:String = '<font color="#999999">[prompt]</font>';

        /**
         * A format string to specify how the prompt is displayed.  This is typically
         * an HTML string that can set the font color and style.  Use <code>[prompt]</code>
         * within the string as a replacement token that will be replaced with the actual
         * prompt text.
         *
         * The default value is "&lt;font color="#999999"&gt;[prompt]&lt;/font&gt;"
         */
        public function get promptFormat():String 
        {
            return _promptFormat;
        }

        public function set promptFormat( value:String ):void 
        {
            _promptFormat = value;
            promptFormatChanged = true;

            // Check to see if the replacement code is found in the new format string.
            if (_promptFormat.indexOf("[prompt]") < 0) 
            {
            	
            	
                // TODO
                //: Log error with the logging framework, or just use trace?
                //trace( "PromptingTextInput warning: prompt format does not contain [prompt] replacement code." );
            }

            invalidateDisplayList();
        }

        private var promptFormatChanged:Boolean;

        private var _tooltipField:String = "tooltip";

        /**
         *  Name of the tooltip field of items in the <code>dataProvider</code>.
         *
         *  @default "tooltip"
         */
        public function get tooltipField():String 
        {
            return _tooltipField;
        }

        public function set tooltipField(value:String):void 
        {
            _tooltipField = value;
        }

        //---------------------------------------------
        //  Filtered fields.
        //  Used to filter complex items.
        //---------------------------------------------

        private var _filteredFields:Array;

        public function get filteredFields():Array 
        {
            return _filteredFields;
        }

        public function set filteredFields(value:Array):void 
        {
            _filteredFields = value;
        }

        //----------------------------------
        //  Filter function
        //----------------------------------

        private var _filterFunction:Function = defaultFilterFunction;

        /**
         * Filter function is used to filter items by entered text.
         *
         * @default defaultFilterFunction
         */
        public function set filterFunction(value:Function):void 
        {
            _filterFunction = value;
        }

        public function get filterFunction():Function 
        {
            return _filterFunction;
        }

        private function defaultFilterFunction(item:Object):Boolean 
        {
            var result:Boolean = false;

            if (item && (textInput.text.length > 0)) 
            {
                if (filteredFields) {
                    for (var i:int=0; i<filteredFields.length; i++) 
                    {
                        if (item.hasOwnProperty(filteredFields[i]))
                        {
                            var field:String = (item[filteredFields[i]]as String).slice(0, textInput.text.length).toLowerCase();
                            if (field == textInput.text.toLowerCase()) 
                            {
                                result = true;
                                break;
                            }
                        }
                    }
                } 
                else 
                {
                    result = (textInput.text.toLowerCase() ==
                        itemToLabel(item).slice(0, textInput.text.length).toLowerCase());
                }
            } 
            else
			{
                result = true;
            }

            return result;
        }

        //----------------------------------
        //  Compare function
        //----------------------------------


        private var _compareFunction:Function = defaultCompareFunction;

        /**
         * Compare function used to select an item by key.
         *
         * @default defaultCompareFunction
         */
        public function set compareFunction(value:Function):void 
        {
            _compareFunction = value;
        }

        public function get compareFunction():Function 
        {
            return _compareFunction;
        }


        /**
         * Function is used to select an item by key.
         *
         * @param item
         * @return
         *
         * @see setSelectedItemByKey function
         *
         */
        private function defaultCompareFunction(item:Object):Boolean 
        {
            var result:Boolean = false;

            if ((selectedKeyValue != null) && item && item.hasOwnProperty(keyField)) 
            {
                var value:Object = item[keyField];
                if ((value is String) && (selectedKeyValue is String)) 
                {
                    result = (value as String) == (selectedKeyValue as String);
                } 
                else 
                {
                    result = value == selectedKeyValue;
                }
            }

            return result;
        }

        /**
         * Selects an item by key.
         *
         * Note: Method not dispatches ListEvent.CHANGE if selectedIndex was -1.
         *
         * @return True if succeed.
         */
        private function selectItemByKeyValue():Boolean 
        {
            var result:Boolean = false;
            var prevSelectedIndex:int = selectedIndex;

            if (selectedItem && keyField in selectedItem && selectedItem[keyField] == selectedKeyValue) 
            {
                return true;
            }

            if (selectedKeyValue != null) {
                for (var i:int = 0; i < dataProvider.length; i++) 
                {
                    if (compareFunction(dataProvider[i])) 
                    {
                        result = true;
                        selectedIndex = i;
                        selectedItem = dataProvider[i];
                        textInput.text = dataProvider[i][labelField];
                        break;
                    }
                }
            }

            if (!result) 
            {
                selectedIndex = dataProvider.length && !prompt ? 0 : -1;
            }

            if (prevSelectedIndex != selectedIndex) 
            {
                dispatchEvent(new ListEvent(ListEvent.CHANGE));
            }

            return result;
        }

        /*public function set selectedItemByKeyHash(value:Object):void {
            for (var i:int = 0; i < this.dataProvider.length; i++) {
                if (this.dataProvider[i][keyField] == value[keyField]) {
                    this.selectedIndex = i;
                    break;
                }
            }
        }*/

        /**
         * @default internalTooltipFunction
         */
        public var toolTipFunction:Function = internalToolTipFunction;

        private function dropdownOpenHandler(event:DropdownEvent):void 
        {
            dropdown.showDataTips = true;
            dropdown.dataTipFunction = toolTipFunction;
            collectionChanged = true;
        }

        private function internalToolTipFunction(item:Object):String 
        {
            if (item.hasOwnProperty(tooltipField)) 
            {
                return item[tooltipField];
            }
            return null;
        }

        public function resetSelection():void 
        {
            selectedIndex = -1;
            invalidateProperties();
        }

        private var showingDropdown:Boolean;

        private function changeTextHandler(event:Event):void 
        {

            if (!textInput.text || (textInput.text.length == 0)) 
            {
                dropdown.selectedIndex = -1;
                selectionChanged = false;
                close();
            } else if (collection is ListCollectionView) 
            {
                var list:ListCollectionView = collection as ListCollectionView;
                list.filterFunction = filterFunction;
                list.refresh();
                if (list.length > 0) 
                {
                    selectionChanged = true;

                    if (!showingDropdown) 
                    {
                        showingDropdown = true;
                        open();
                    }
                } 
                else 
                {
                    dropdown.selectedIndex = -1;
                    selectionChanged = false;
                    close();
                }
            } 
            else 
            {
                throw new Error('Only ListCollectionView is supported now.');
            }
        }

        //------------------------------------------
        //
        //  Overriden functions
        //
        //------------------------------------------

        override protected function createChildren():void 
        {
            super.createChildren();

            textInput.addEventListener(Event.CHANGE, changeTextHandler);
        }

        override protected function commitProperties():void 
        {
            super.commitProperties();

            if (selectedKeyValueChanged) 
            {
                selectItemByKeyValue();
                selectedKeyValueChanged = false;
            }

            if (editable) 
            {
                if (promptChanged || promptFormatChanged ||
                        (prompt && (textInput.text == prompt))) 
                {

                    if (focusManager && focusManager.getFocus() == this) 
                    {
                        textInput.text = '';
                        textInput.setSelection(0, 0);
                    } 
                    else 
                    {
                        showHTMLPrompt();
                    }

                    promptChanged = false;
                    promptFormatChanged = false;
                }
            }
            //invalidateDisplayList();
        }

        private var collectionChanged:Boolean;

        override protected function collectionChangeHandler(event:Event):void 
        {
            if (editable) 
            {
                collectionChanged = true;
                invalidateDisplayList();
            } else {
                super.collectionChangeHandler(event);

                if (collection.length == 0) 
                {
                    // set prompt label
                    selectedIndex = -1;
                } 
                else if (selectedKeyValue != null) 
                {
                    selectItemByKeyValue();
                }
            }
        }

        override protected function focusInHandler(event:FocusEvent):void 
        {
            super.focusInHandler(event);

            if (editable) 
            {
                if (prompt && (selectedIndex == -1)) 
                {
                    textInput.htmlText = '<font color="#000000"><b></b></font>';
                    textInput.validateNow();
                }
            }
        }

        override protected function focusOutHandler(event:FocusEvent):void 
        {
            super.focusOutHandler(event);

            if (editable) 
            {
                if (prompt && selectedIndex == -1 && textInput.text == '' ) 
                {
                    showHTMLPrompt();
                }
            }
        }
	
        override protected function updateDisplayList(unscaledWidth:Number, unscaledHeight:Number):void 
        {
            if (!showingDropdown) 
            {
                super.updateDisplayList(unscaledWidth, unscaledHeight);
            }

            if (editable) 
            {
                if (promptChanged || promptFormatChanged ||
                        (prompt && (textInput.text == prompt))) 
                {

                    if (focusManager && focusManager.getFocus() == this) 
                    {
                        textInput.text = '';
                        textInput.setSelection(0, 0);
                    } 
                    else 
                    {
                        showHTMLPrompt();
                    }

                    promptChanged = false;
                    promptFormatChanged = false;
                }
            }

            if (collectionChanged) 
            {
                // Calculate dropdown width and height
                var size:Object = calculatePreferredSizeFromData(collection.length);

                if (dropdown) 
                {
                    dropdown.rowCount = Math.min(collection.length, this.rowCount);
                    dropdown.width = Math.max(this.width, size.width);
                    // Set selected index
                    if (dropdown.selectedIndex == -1) 
                    {
                        dropdown.selectedIndex = 0;
                    }
                }

                collectionChanged = false;
            }
        }

        private function showHTMLPrompt():void 
        {
            textInput.htmlText = promptFormat.replace(/\[prompt\]/g, prompt);
        }

        private var dropdownShown:Boolean;

        override public function open():void 
        {
            //trace('open');
            dropdownShown = true;
            collectionChanged = true;
            super.open();

        }

        override public function close(trigger:Event = null):void 
        {
            //trace('close');
            super.close(trigger);

            if (editable) 
            {
                if (collection.filterFunction != null) 
                {
                    collection.filterFunction = null;
                    collection.refresh();
                    // Set actual index
                    if (selectedIndex >= 0) 
                    {
                        selectedIndex = (collection as ListCollectionView).getItemIndex(selectedItem);
                        dispatchEvent(new ListEvent(ListEvent.CHANGE));
                    }
                }
            }

            showingDropdown = false;
            dropdownShown = false;
        }

        override protected function keyUpHandler(event:KeyboardEvent):void 
        {
            super.keyUpHandler(event);

            if (editable) 
            {
                if (event.keyCode == Keyboard.ESCAPE) 
                {
                    close();
                } 
                else if (event.keyCode == Keyboard.ENTER) 
                {
                    if (editable) 
                    {
                        textInput.getTextField().setSelection(0, textInput.text.length);
                        textInput.getTextField().scrollH = 0;
                    }
                }
            }
        }

        override protected function downArrowButton_buttonDownHandler(event:FlexEvent):void 
        {
            if (editable) {
                // The down arrow should always toggle the visibility of the dropdown.
                if (!isShowingDropdown) 
                {
                    collection.filterFunction = null;
                    collection.refresh();
                }
                collectionChanged = true;
            }
            super.downArrowButton_buttonDownHandler(event);
        }
        
		public function setItemByField(field:String,value:Object):void
		{
			for each(var item:Object in dataProvider)
			{
				if(item != null)
				{
					if(item[field] == value)
					{
						selectedItem = item;
						invalidateProperties();
						break;
					}
				}
			}
			
		}
    }
}