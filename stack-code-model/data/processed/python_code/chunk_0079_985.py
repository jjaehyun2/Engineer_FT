/**
 *  Starling Builder
 *  Copyright 2015 SGN Inc. All Rights Reserved.
 *
 *  This program is free software. You can redistribute and/or modify it in
 *  accordance with the terms of the accompanying license agreement.
 */
package starlingbuilder.editor.ui
{
    import feathers.controls.renderers.IListItemRenderer;
    import feathers.controls.text.TextBlockTextRenderer;
    import feathers.core.ITextRenderer;

    import flash.geom.Point;

    import starlingbuilder.editor.UIEditorApp;
    import starlingbuilder.editor.data.TemplateData;
    import starlingbuilder.editor.helper.DragToCanvasHelper;
    import starlingbuilder.editor.helper.UIComponentHelper;
    import starlingbuilder.engine.util.ParamUtil;

    import feathers.controls.List;
    import feathers.data.ListCollection;
    import feathers.layout.AnchorLayout;
    import feathers.layout.AnchorLayoutData;

    import starling.events.Event;
    import starling.utils.AssetManager;

    public class CommonTab extends SearchableTab
    {
        private var _assetManager:AssetManager;

        private var _list:List;

        protected var _supportedTypes:Array;

        public function CommonTab()
        {
            _assetManager = UIEditorApp.instance.assetManager;

            createPickerList();


            var anchorLayoutData:AnchorLayoutData = new AnchorLayoutData();
            anchorLayoutData.top = 25;
            anchorLayoutData.bottom = 0;
            this.layoutData = anchorLayoutData;

            layout = new AnchorLayout();

            createTopContainer();

            listAssets();
        }

        protected function createPickerList():void
        {
            //"container" tag is for back-compat
            _supportedTypes = TemplateData.getSupportedComponent("common").concat(TemplateData.getSupportedComponent("container"));
        }

        private function onListChange(event:Event):void
        {
            if (_list.selectedIndex != -1)
            {
                create(_list.selectedItem.label);

                _list.selectedIndex = -1;
            }
        }

        public function create(label:String, position:Point = null):void
        {
            var cls:String = label;
            var name:String = ParamUtil.getDisplayObjectName(cls);

            var editorData:Object = {cls:cls, name:name};

            if (position)
            {
                editorData.x = position.x;
                editorData.y = position.y;
            }

            UIComponentHelper.createComponent(editorData);
        }

        private function listAssets():void
        {
            _list = new List();
            _list.isFocusEnabled = false;

            _list.width = 330;
            _list.height = 800;
            _list.selectedIndex = -1;
            _list.itemRendererFactory = listItemRenderer;
            _list.itemRendererProperties.labelFactory = function():ITextRenderer
            {
                var textRenderer:TextBlockTextRenderer = new TextBlockTextRenderer();
                textRenderer.wordWrap = true;
                return textRenderer;
            }
            _list.itemRendererProperties.height = 50;

            _list.addEventListener(Event.CHANGE, onListChange);

            var anchorLayoutData:AnchorLayoutData = new AnchorLayoutData();
            anchorLayoutData.top = 0;
            anchorLayoutData.bottom = 0;
            anchorLayoutData.topAnchorDisplayObject = _searchTextInput;
            _list.layoutData = anchorLayoutData;

            addChild(_list);

            updateData();
        }

        private function updateData():void
        {
            var data:ListCollection = new ListCollection();

            var text:String = _searchTextInput.text.toLocaleLowerCase();

            var supportedTypes:Array;
            if (text.length)
            {
                supportedTypes = _supportedTypes.filter(function(value:String, index:int, arr:Array):Boolean{
                    return value.toLowerCase().indexOf(text) != -1;
                });
            }
            else
            {
                supportedTypes = _supportedTypes;
            }

            for each (var name:String in supportedTypes)
            {
                data.push({label: name});
            }

            _list.dataProvider = data;
        }

        protected function listItemRenderer():IListItemRenderer
        {
            return new ComponentItemRenderer(DragToCanvasHelper.COMMON_TAB);
        }

        override protected function onSearch(event:Event):void
        {
            updateData();
        }
    }
}