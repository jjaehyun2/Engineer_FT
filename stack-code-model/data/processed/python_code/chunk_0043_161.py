package h2olib.control.treeGrid
{

    import flash.events.MouseEvent;
    
    import mx.containers.HBox;
    import mx.controls.DataGrid;
    import mx.controls.Image;
    import mx.controls.Label;
    import mx.controls.Spacer;
    import mx.controls.dataGridClasses.DataGridColumn;
    import mx.controls.listClasses.BaseListData;
    import mx.controls.listClasses.IDropInListItemRenderer;
    import mx.core.IToolTip;
    import mx.core.ScrollPolicy;
    import mx.events.ToolTipEvent;
    
    import org.osflex.ITreeGridNode;

    /**
     * Drop-in cell renderer used in the TreeGrid. Displays an open/close
     * icon next to the column text so that children for a node can be viewed.
     */
    public class TreeGridCellRenderer extends HBox
        implements IDropInListItemRenderer 
    {

        /** Number of pixels per indent level */
        private static const INDENT_PIXELS:Number = 15;

        [Embed(source="assets/close.gif")]
        [Bindable]
        public var openIcon:Class;

        [Embed(source="assets/open.gif")]
        [Bindable]
        public var closeIcon:Class;

        /** Number of pixels to indent for each level */
        public var indentPixels:Number = INDENT_PIXELS;

        /** If set, determines the type of tool tip to show */

        private var _toolTipClass:Class;

        public function set toolTipClass(value:Class):void 
        {
            _toolTipClass = value;
            addEventListener(ToolTipEvent.TOOL_TIP_CREATE, createCustomTooltip);
        }

        public function get toolTipClass():Class 
        {
            return _toolTipClass;
        }

        /** Spacer for indentation */
        protected var cSpacer:Spacer;

        /** Icon displayed for toggle open/close */
        protected var cToggleIcon:Image;

        /** Label shown for field */
        protected var cFieldLabel:Label;

        /** List data passed to cell renderer */
        protected var _listData:BaseListData;

        /**
         * Create the renderer.
         */
        public function TreeGridCellRenderer() 
        {
            this.percentWidth = 100;
            this.horizontalScrollPolicy = ScrollPolicy.OFF;
            this.verticalScrollPolicy = ScrollPolicy.OFF;
            this.setStyle("horizontalGap", 0);
            this.setStyle("verticalAlign", "middle");
        }

        /**
         * Setter for listData called on drop-in cell renderer.
         */
        public function set listData(data:BaseListData):void 
        {
            this._listData = data;
        }

        /**
         * Getter for listData called on drop-in cell renderer.
         */
        public function get listData():BaseListData 
        {
            return this._listData;
        }


        override public function set toolTip(value:String):void 
        {
            super.toolTip = value;
        }

        /**
         * Create a custom tooltip if the toolTipComponent field is set.
         */
        protected function createCustomTooltip(event:ToolTipEvent):void 
        {
            event.toolTip = new toolTipClass() as IToolTip;
            event.toolTip.text = toolTip ? toolTip : cFieldLabel.text;
        }

        /**
         * Overrides to create child components.
         */
        override protected function createChildren():void 
        {
            super.createChildren();
            if (cSpacer == null) 
            {
                cSpacer = new Spacer();
                addChild(cSpacer);
            }
            if (cToggleIcon == null) 
            {
                cToggleIcon = new Image();
                cToggleIcon.width = 13;
                cToggleIcon.addEventListener(MouseEvent.CLICK, iconPress);
                addChild(cToggleIcon);
            }
            if (cFieldLabel == null) 
            {
                cFieldLabel = new Label();
                cFieldLabel.percentWidth = 100;
                addChild(cFieldLabel);
            }
        }

        /**
         * Overrides the setter for 'data' to manipulate the image
         * icons and labels.
         */
        override public function set data(data:Object):void 
        {
            if ((data != null) && (data is ITreeGridNode)) 
            {
                super.data = data;
                invalidateProperties();
            }
        }

        override protected function commitProperties():void 
        {
            super.commitProperties();

            if ((data != null) && (data is ITreeGridNode) && listData) 
            {
                var node:ITreeGridNode = ITreeGridNode(data);
                var column:DataGridColumn = (listData.owner as DataGrid).columns[listData.columnIndex];
                var assignedLabel:String = column.itemToLabel(data);

                cSpacer.width = 3 + (node.indentLevel * indentPixels);
                cFieldLabel.htmlText = assignedLabel;
                toolTip = assignedLabel;

                if (node.children.length > 0) 
                {
                    if (node.open == false) 
                    {
                        cToggleIcon.visible = true;
                        cToggleIcon.source = closeIcon;
                    } 
                    else 
                    {
                        cToggleIcon.visible = true;
                        cToggleIcon.source = openIcon;
                    }
                } 
                else 
                {
                    cToggleIcon.visible = false;
                }
            }
        }

        /**
         * Called when the open/close icon is clicked.
         */
        protected function iconPress(event:MouseEvent):void 
        {
            var item:ITreeGridNode = data as ITreeGridNode;
            var itemOpen:Boolean = item.open;
            var nodeEvent:TreeGridNodeEvent;

            item.toggleOpen();
            if (itemOpen == false) 
            {
                nodeEvent = new TreeGridNodeEvent(TreeGridNodeEvent.NODE_OPEN, item);
            } 
            else
            {
                nodeEvent = new TreeGridNodeEvent(TreeGridNodeEvent.NODE_CLOSE, item);
            }
            this.dispatchEvent(nodeEvent);
        }
    }
}