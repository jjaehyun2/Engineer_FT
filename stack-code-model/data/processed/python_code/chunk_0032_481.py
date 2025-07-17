/**
 *  Starling Builder
 *  Copyright 2015 SGN Inc. All Rights Reserved.
 *
 *  This program is free software. You can redistribute and/or modify it in
 *  accordance with the terms of the accompanying license agreement.
 */
package starlingbuilder.editor.controller
{
    import feathers.controls.LayoutGroup;
    import feathers.controls.TextArea;
    import feathers.controls.TextInput;
    import feathers.core.FocusManager;
    import feathers.layout.AnchorLayout;

    import flash.ui.Keyboard;
    import flash.utils.getDefinitionByName;

    import starlingbuilder.editor.Setting;
    import starlingbuilder.editor.UIEditorScreen;
    import starlingbuilder.editor.data.TemplateData;
    import starlingbuilder.editor.data.UIBuilderTemplate;
    import starlingbuilder.editor.events.DocumentEventType;
    import starlingbuilder.editor.helper.AssetMediator;
    import starlingbuilder.editor.helper.BoundingBoxContainer;
    import starlingbuilder.editor.helper.DragHelper;
    import starlingbuilder.editor.helper.DragQuad;
    import starlingbuilder.editor.helper.FileListingHelper;
    import starlingbuilder.editor.helper.SnapshotHelper;
    import starlingbuilder.editor.helper.UIComponentHelper;
    import starlingbuilder.editor.history.CompositeHistoryOperation;
    import starlingbuilder.editor.history.GroupOperation;
    import starlingbuilder.editor.history.UngroupOperation;
    import starlingbuilder.editor.ui.CenterPanel;
    import starlingbuilder.editor.upgrade.LayoutVersion;
    import starlingbuilder.engine.IAssetMediator;
    import starlingbuilder.engine.util.DisplayObjectUtil;
    import starlingbuilder.util.KeyboardWatcher;
    import starlingbuilder.editor.helper.PixelSnapper;
    import starlingbuilder.editor.helper.PixelSnapperData;
    import starlingbuilder.editor.helper.SelectHelper;
    import starlingbuilder.editor.history.CreateOperation;
    import starlingbuilder.editor.history.CutOperation;
    import starlingbuilder.editor.history.DeleteOperation;
    import starlingbuilder.editor.history.MoveLayerOperation;
    import starlingbuilder.editor.history.MoveOperation;
    import starlingbuilder.editor.history.PasteOperation;
    import starlingbuilder.editor.history.PropertyChangeOperation;
    import starlingbuilder.editor.themes.IUIEditorThemeMediator;
    import starlingbuilder.engine.IUIBuilder;
    import starlingbuilder.engine.UIBuilder;
    import starlingbuilder.engine.tween.DefaultTweenBuilder;
    import starlingbuilder.engine.tween.ITweenBuilder;
    import starlingbuilder.engine.util.ParamUtil;
    import starlingbuilder.util.feathers.popup.InfoPopup;
    import starlingbuilder.util.history.HistoryManager;
    import starlingbuilder.util.history.IHistoryOperation;
    import starlingbuilder.util.ui.inspector.PropertyPanel;
    import starlingbuilder.util.ui.inspector.UIMapperEventType;

    import feathers.core.FeathersControl;
    import feathers.core.IFeathersControl;
    import feathers.core.PopUpManager;
    import feathers.data.ListCollection;

    import flash.desktop.Clipboard;
    import flash.desktop.ClipboardFormats;
    import flash.filesystem.File;
    import flash.geom.Point;
    import flash.geom.Rectangle;
    import flash.utils.Dictionary;

    import starling.display.DisplayObject;
    import starling.display.DisplayObjectContainer;
    import starling.display.Image;
    import starling.display.Quad;
    import starling.display.Sprite;
    import starling.events.Event;
    import starling.events.EventDispatcher;
    import starling.text.TextField;
    import starling.utils.AssetManager;

    public class DocumentManager extends EventDispatcher implements IUIEditorThemeMediator, IComponentRenderSupport
    {
        private var _assetManager:AssetManager;
        private var _uiBuilder:IUIBuilder;
        private var _uiBuilderForGame:IUIBuilder;
        private var _assetMediator:AssetMediator;

        private var _historyManager:HistoryManager;

        private var _container:Sprite;

        private var _testContainer:Sprite;

        private var _canvas:Quad;

        private var _canvasContainer:Sprite;

        private var _backgroundContainer:Sprite;

        private var _layoutContainer:LayoutGroup;

        private var _root:DisplayObjectContainer;

        private var _snapContainer:Sprite;

        private var _boundingBoxContainer:BoundingBoxContainer;

        private var _selectManager:SelectManager;

        private var _keyboardWatcher:KeyboardWatcher;

        private var _extraParamsDict:Dictionary;

        private var _dataProvider:ListCollection; //use for listing layout

        private var _snapPixel:Boolean = true;

        private var _showTextBorder:Boolean = false;

        private var _localizationManager:LocalizationManager;

        private var _tweenBuilder:ITweenBuilder;

        private var _setting:Setting;

        private var _collapseMap:Dictionary;

        private var _layoutSearchString:String;

        public function DocumentManager(assetManager:AssetManager, localizationManager:LocalizationManager)
        {
            _assetManager = assetManager;

            _localizationManager = localizationManager;

            _extraParamsDict = new Dictionary();

            _dataProvider = new ListCollection();

            var cls:Class;

            if (UIBuilderTemplate.template.assetMediator)
            {
                try
                {
                    cls = getDefinitionByName(UIBuilderTemplate.template.assetMediator) as Class;
                    _assetMediator = new cls(_assetManager);
                }
                catch (e:Error)
                {
                    InfoPopup.show(e.getStackTrace());
                    _assetMediator = new AssetMediator(_assetManager);
                }
            }
            else
            {
                _assetMediator = new AssetMediator(_assetManager);
            }
            _assetMediator.workspaceDir = UIEditorScreen.instance.workspaceDir;


            if (UIBuilderTemplate.template.tweenBuilder)
            {
                try
                {
                    cls = getDefinitionByName(UIBuilderTemplate.template.tweenBuilder) as Class;
                    _tweenBuilder = new cls();
                }
                catch (e:Error)
                {
                    InfoPopup.show(e.getStackTrace());
                    _tweenBuilder = new DefaultTweenBuilder();
                }
            }
            else
            {
                _tweenBuilder = new DefaultTweenBuilder();
            }

            _uiBuilder = new UIBuilder(_assetMediator, true, TemplateData.editor_template, _localizationManager.localization, _tweenBuilder);
            _uiBuilderForGame = new UIBuilder(_assetMediator, false, TemplateData.editor_template, _localizationManager.localization, _tweenBuilder);

            _canvas = new Quad(100, 100);
            _canvasContainer = new Sprite();
            _canvasContainer.addChild(_canvas);
            SelectHelper.startSelect(_canvas, function(object:DisplayObject):void{

                if (dragMode) return;

                selectObject(null);
            });

            DragQuad.startDrag(_canvas,
                    function():Boolean{
                        return !dragMode;
                    },
                    function(rect:Rectangle):void{

                        if (dragMode) return;

                        FocusManager.focus = UIEditorScreen.instance.centerPanel;
                        _selectManager.selectByRect(rect, _extraParamsDict, uiBuilder);
                    });

            DragHelper.startDrag(_canvas, null, function(obj:DisplayObject, dx:Number, dy:Number):Boolean
            {
                if (dragMode) dragCanvas(dx, dy);
                return true;
            }, null);

            _backgroundContainer = new Sprite();
            _backgroundContainer.touchable = false;
            _layoutContainer = new LayoutGroup();
            _layoutContainer.layout = new AnchorLayout();
            _snapContainer = new Sprite();
            _boundingBoxContainer = new BoundingBoxContainer(this);

            _testContainer = new Sprite();

            PropertyPanel.globalDispatcher.addEventListener(UIMapperEventType.PROPERTY_CHANGE, onPropertyChange);

            _historyManager = new HistoryManager();

            _selectManager = new SelectManager();
            _selectManager.addEventListener(DocumentEventType.SELECTION_CHANGE, onSelectionChanged);

            _keyboardWatcher = new KeyboardWatcher();

            _setting = UIEditorScreen.instance.setting;
            _setting.addEventListener(Event.CHANGE, onSettingChanged);
            _setting.setChanged();

            _collapseMap = new Dictionary();
        }

        public function set container(value:Sprite):void
        {
            _container = value;

            _container.addChild(_canvasContainer);
            _container.addChild(_backgroundContainer);
            _container.addChild(_layoutContainer);
            _container.addChild(_snapContainer);
            _container.addChild(_boundingBoxContainer);

            reset();
        }

        private function setRoot(obj:DisplayObjectContainer, param:Object):void
        {
            if (_root)
            {
                _root.removeFromParent(true);
            }

            _root = obj;
            _layoutContainer.addChild(_root);
            _extraParamsDict[obj] = param;
        }

        private function createRoot():void
        {
            var data:Object = {cls:_setting.rootContainerClass, customParams:{}, params:{name:"root"}};
            var result:Object = _uiBuilder.createUIElement(data);
            setRoot(result.object, result.params);

            var objects:Array = [];
            var obj:DisplayObjectContainer = result.object;
            getObjectsByPreorderTraversal(obj, _extraParamsDict, objects);
            addFrom(obj, result.params, null);
        }

        private function getParent():DisplayObjectContainer
        {
            var obj:Object = selectedObject;

            if (obj)
            {
                if (_uiBuilder.isContainer(_extraParamsDict[obj]))
                {
                    return obj as DisplayObjectContainer;
                }
                else
                {
                    return obj.parent;
                }
            }
            else
            {
                return _root;
            }
        }


        public function addTree(root:DisplayObject, paramDict:Dictionary, parent:DisplayObjectContainer = null, index:int = -1):void
        {
            if (parent == null)
            {
                parent = getParent();
            }

            addFrom(root, paramDict[root], parent, index);

            var container:DisplayObjectContainer = root as DisplayObjectContainer;

            if (container)
            {
                var objects:Array = [];
                getObjectsByPreorderTraversal(container, paramDict, objects);

                for each (var obj:DisplayObject in objects)
                {
                    if (obj !== root)
                        addFrom(obj, paramDict[obj], null);
                }
            }

            selectObject(root);

            setLayerChanged();

            setChanged();
        }

        private function addFrom(obj:DisplayObject, param:Object, parent:DisplayObjectContainer = null, index:int = -1):void
        {
            DragHelper.startDrag(obj, function(object:DisplayObject):void{

                if (dragMode) return;

                FocusManager.focus = UIEditorScreen.instance.centerPanel;

                if (!(selectedObject is DisplayObjectContainer) || !DisplayObjectContainer(selectedObject).contains(object))
                {
                    if (_keyboardWatcher.hasKeyPressed(Keyboard.CONTROL) ||
                            _keyboardWatcher.hasKeyPressed(Keyboard.COMMAND) ||
                            _keyboardWatcher.hasKeyPressed(Keyboard.SHIFT))
                    {
                        if (_selectManager.isSelected(object))
                        {
                            _selectManager.removeSelectObject(object);
                        }
                        else
                        {
                            _selectManager.addSelectObject(object);
                        }
                    }
                    else
                    {
                        if (!_selectManager.isSelected(object))
                            selectObject(object);
                    }
                }
            }, function(obj:DisplayObject, dx:Number, dy:Number):Boolean{

                if (dragMode)
                {
                    dragCanvas(dx, dy);
                    return true;
                }

                dx /= scale;
                dy /= scale;
                return move(dx, dy);
            }, function():void{

                if (dragMode) return;

                endMove();
            });

            //fix exception on TextInput
            if (obj is TextInput)
            {
                (obj as TextInput).isFocusEnabled = false;
                (obj as TextInput).isEnabled = false;
            }

            if (obj is TextField)
            {
                TextField(obj).border = _showTextBorder;
            }

            if ("enabled" in obj && "alphaWhenDisabled" in obj)
            {
                obj["alphaWhenDisabled"] = 1;
                obj["enabled"] = false;
            }

            _extraParamsDict[obj] = param;


            if (isAncestorOf(obj, _root))
            {
                //do nothing
            }
            else if (parent)
            {
                if (index < 0)
                    parent.addChild(obj);
                else
                    parent.addChildAt(obj, index);
            }

            _dataProvider.push({label:obj.name, hidden:!obj.visible, lock:!obj.touchable, obj:obj, layer:getLayerFromObject(obj)});
        }

        private function getLayerFromObject(obj:DisplayObject):int
        {
            return getLayer(_root, obj, 1);
        }

        private function sortDataProvider():void
        {
            var result:Array = [];
            _dataProvider = new ListCollection();

            var obj:DisplayObject;

            if (_layoutSearchString)
            {
                getObjectsByPreorderTraversal(_root, _extraParamsDict, result);
                for each (obj in result)
                {
                    if (obj.name.toLowerCase().indexOf(_layoutSearchString.toLowerCase()) != -1)
                        _dataProvider.push({label:obj.name, hidden:!obj.visible, lock:!obj.touchable, obj:obj, layer:getLayerFromObject(obj), search:true});
                }
            }
            else
            {
                getObjectsByPreorderTraversal(_root, _extraParamsDict, result, _collapseMap);
                for each (obj in result)
                    _dataProvider.push({label:obj.name, hidden:!obj.visible, lock:!obj.touchable, obj:obj, layer:getLayerFromObject(obj), collapse:_collapseMap[obj]});
            }
        }

        private function getObjectsByPreorderTraversal(container:DisplayObjectContainer, paramDict:Dictionary, result:Array, collapseMap:Dictionary = null):void
        {
            if (!container) return;

            result.push(container);

            if (collapseMap && collapseMap[container])
                return;

            var start:int;
            var end:int;
            var step:int;

            if (inverseLayer())
            {
                start = container.numChildren - 1;
                end = -1;
                step = -1;
            }
            else
            {
                start = 0;
                end = container.numChildren;
                step = 1;
            }

            for (var i:int = start; i != end; i += step)
            {
                var child:DisplayObject = container.getChildAt(i);

                if (paramDict[child])
                {
                    if (_uiBuilder.isContainer(paramDict[child]))
                    {
                        getObjectsByPreorderTraversal(child as DisplayObjectContainer, paramDict, result, collapseMap);
                    }
                    else
                    {
                        result.push(child);
                    }
                }
            }
        }

        private function getLayer(container:DisplayObjectContainer, obj:DisplayObject, layer:int):int
        {
            if (container === obj) return 0;

            for (var i:int = 0; i < container.numChildren; ++i)
            {
                var child:DisplayObject = container.getChildAt(i);

                if (child === obj)
                {
                    return layer;
                }
                else if (child is DisplayObjectContainer)
                {
                    var l:int = getLayer(child as DisplayObjectContainer, obj, layer + 1);
                    if (l >= 0)
                    {
                        return l;
                    }
                }
            }

            return -1;
        }

        private function removeFromParam(obj:DisplayObject, paramDict:Dictionary):void
        {
            if (paramDict[obj])
                delete paramDict[obj];

            var container:DisplayObjectContainer = obj as DisplayObjectContainer;

            if (container)
            {
                for (var i:int = 0; i < container.numChildren; ++i)
                {
                    removeFromParam(container.getChildAt(i), paramDict);
                }
            }
        }

        private function recreateFromParam(obj:DisplayObject, paramDict:Dictionary, newDict:Dictionary):void
        {
            if (paramDict[obj])
            {
                newDict[obj] = paramDict[obj];
            }

            var container:DisplayObjectContainer = obj as DisplayObjectContainer;

            if (container)
            {
                for (var i:int = 0; i < container.numChildren; ++i)
                {
                    recreateFromParam(container.getChildAt(i), paramDict, newDict);
                }
            }
        }

        private function endSelect(obj:DisplayObject):void
        {
            SelectHelper.endSelect(obj);

            var container:DisplayObjectContainer = obj as DisplayObjectContainer;

            if (container)
            {
                for (var i:int = 0; i < container.numChildren; ++i)
                {
                    SelectHelper.endSelect(container.getChildAt(i));
                }
            }
        }

        public function removeTree(obj:DisplayObject, last:Boolean = true):void
        {
            var parent:DisplayObjectContainer = obj.parent;

            if (last)
                selectObject(null);

            removeFromParam(obj, _extraParamsDict);
            obj.removeFromParent();
            endSelect(obj);

            if (last)
            {
                setLayerChanged();
                selectParent(parent);
                setChanged();
            }
        }

        private function selectParent(parent:DisplayObjectContainer):void
        {
            while (_extraParamsDict[parent] == null && parent.parent)
            {
                parent = parent.parent;
            }

            if (parent === _root)
                selectObject(null);
            else
                selectObject(parent);
        }

        public function remove():void
        {
            var objects:Array = selectedObjects;

            if (objects.length)
            {
                var ops:Array = [];

                for (var i:int = 0; i < objects.length; ++i)
                {
                    var obj:DisplayObject = objects[i];
                    if (obj === _root) continue;

                    var newDict:Dictionary = new Dictionary();
                    recreateFromParam(obj, _extraParamsDict, newDict);
                    ops.push(new DeleteOperation(obj, newDict, obj.parent));
                    removeTree(obj, i == objects.length - 1);
                }

                _historyManager.add(new CompositeHistoryOperation(ops));
            }
        }



        public function move(dx:Number, dy:Number, ignoreSnapPixel:Boolean = false):Boolean
        {
            //trace("dx:", dx, "dy:", dy);

            if (_selectManager.selectedObjects.length == 0)
                return false;

            var data:PixelSnapperData;

            if (snapPixel && !ignoreSnapPixel)
            {
                _snapContainer.removeChildren(0, -1, true);

                data = PixelSnapper.snap(_selectManager.selectedObjects, selectedObject.parent, _container.parent, new Point(dx, dy));

                if (data)
                {
                    dx = data.deltaX;
                    dy = data.deltaY;
                }
            }

            for each (var obj:DisplayObject in _selectManager.selectedObjects)
            {
                obj.x += dx;
                obj.y += dy;
            }

            recordMoveHistory(dx, dy);

            if (data)
            {
                _snapContainer.x = selectedObject.parent.x;
                _snapContainer.y = selectedObject.parent.y;
                PixelSnapper.drawSnapObjectBound(_snapContainer, data);
                PixelSnapper.drawSnapLine(_snapContainer, data);
            }

            setChanged();

            return !snapPixel || (dx * dx + dy * dy > 0.5);
        }

        public function endMove():void
        {
            _snapContainer.removeChildren(0, -1, true);
        }


        public function moveUp():void
        {
            var obj:DisplayObject = singleSelectedObject;

            if (!obj)
                return;

            var parent:DisplayObjectContainer = obj.parent;

            var index:int = parent.getChildIndex(obj);
            if (index > 0)
            {
                parent.setChildIndex(obj, index - 1);

                _historyManager.add(new MoveLayerOperation(obj, obj.parent, index, index - 1));

                setLayerChanged();

                setChanged();
            }

        }

        public function moveDown():void
        {
            var obj:DisplayObject = singleSelectedObject;

            if (!obj)
                return;

            var parent:DisplayObjectContainer = obj.parent;

            var index:int = parent.getChildIndex(obj);
            if (index < parent.numChildren - 1)
            {
                parent.setChildIndex(obj, index + 1);

                _historyManager.add(new MoveLayerOperation(obj, obj.parent, index, index + 1));

                setLayerChanged();

                setChanged();
            }

        }

        public function selectObject(obj:DisplayObject):void
        {
            _selectManager.selectObject(obj);
        }

        private function onSelectionChanged(event:Event):void
        {
            var obj:DisplayObject = selectedObject;

            if (obj is FeathersControl)
            {
                FeathersControl(obj).invalidate();
            }

            //_boundingBoxContainer.update([_selectedObject]);
            _boundingBoxContainer.update(_selectManager.selectedObjects);

            setChanged();
        }

        private function onPropertyChange(event:Event):void
        {
            var target:Object = event.data.target;

            if (target === _background || target === selectedObject)
            {
                recordPropertyChangeHistory(event);

                setChanged();
            }
        }

        private function recordPropertyChangeHistory(event:Event):void
        {
            var data:Object = event.data;

            if (data.hasOwnProperty("oldValue"))
            {
                var operation:IHistoryOperation = new PropertyChangeOperation(data.target, data.propertyName, data.oldValue, data.target[data.propertyName]);
                _historyManager.add(operation);
            }
        }

        private function recordMoveHistory(dx:Number, dy:Number):void
        {
            var objects:Object = selectedObjects;

            if (objects.length)
            {
                var ops:Array = [];
                for each (var obj:DisplayObject in objects)
                {
                    ops.push(new MoveOperation(obj, dx, dy));
                }

                _historyManager.add(new CompositeHistoryOperation(ops));
            }
        }

        public function get historyManager():HistoryManager
        {
            return _historyManager;
        }

        public function get assetMediator():IAssetMediator
        {
            return _assetMediator;
        }

        public function selectObjectAtIndex(index:int):void
        {
            var item:Object = _dataProvider.getItemAt(index);

            var obj:DisplayObject = item.obj;
            if (obj)
            {
                selectObject(obj);
            }
        }

        public function get selectedIndex():int
        {
            var obj:DisplayObject = selectedObject;

            if (obj)
            {
                for (var i:int = 0; i < _dataProvider.length; ++i)
                {
                    var item:Object = _dataProvider.getItemAt(i);

                    if (item && item.obj === obj)
                    {
                        return i;
                    }
                }
            }

            return -1;
        }

        public function get selectedObject():DisplayObject
        {
            if (_selectManager.selectedObjects.length > 0)
                return _selectManager.selectedObjects[0];
            else
                return null;
        }

        public function get singleSelectedObject():DisplayObject
        {
            if (_selectManager.selectedObjects.length == 1)
                return _selectManager.selectedObjects[0];
            else
                return null;
        }

        public function get selectedObjects():Array
        {
            return _selectManager.selectedObjects;
        }

        public function startTest(forGame:Boolean = false):Sprite
        {
            _testContainer.removeChildren(0, -1, true);

            var data:Object = _uiBuilder.save(_layoutContainer, _extraParamsDict, LayoutVersion.VERSION, TemplateData.editor_template);

            var setting:Object = exportSetting();

            var canvas:Quad = new Quad(canvasSize.x, canvasSize.y);
            canvas.color = canvasColor;
            _testContainer.addChild(canvas);

            if (setting.background)
            {
                _testContainer.addChild(createBackground(setting.background));
            }

            var root:DisplayObject;

            if (forGame)
            {
                root = _uiBuilderForGame.load(data, false).object;
            }
            else
            {
                root = _uiBuilder.load(data, false).object;
            }

            _testContainer.addChild(root);

            return _testContainer;
        }

        public function stopTest():void
        {
            _testContainer.removeChildren(0, -1, true);
        }

        public function export():Object
        {
            return _uiBuilder.save(_layoutContainer, _extraParamsDict, LayoutVersion.VERSION, exportSetting());
        }

        private function exportSetting():Object
        {
            var setting:Object = {};

            if (background)
            {
                setting.background = {name:background.name, x:background.x, y:background.y, width:background.width, height:background.height};
            }

            if (canvasSize)
            {
                setting.canvasSize = {x:_canvasSize.x, y:_canvasSize.y};
            }

            setting.canvasColor = canvasColor;

            saveFlags(setting);

            return setting;
        }

        private function importSetting(setting:Object):void
        {
            if (setting)
            {
                if (setting.background)
                {
                    background = createBackground(setting.background)
                }

                if (setting.canvasSize)
                {
                    canvasSize = new Point(setting.canvasSize.x, setting.canvasSize.y);
                }

                if ("canvasColor" in setting)
                {
                    canvasColor = setting.canvasColor;
                }

                loadFlags(setting);
            }

            setChanged();
        }

        private function createBackground(data:Object):Image
        {
            try
            {
                var image:Image = new Image(_assetMediator.getTexture(data.name));
                image.name = data.name;
                image.x = data.x;
                image.y = data.y;
                image.width = data.width;
                image.height = data.height;
                return image;
            }
            catch (e:Error)
            {
                return null;
            }
        }

        public function importData(data:Object, file:File):void
        {
            _assetMediator.file = file;

            reset();

            var result:Object = _uiBuilder.load(data, false);

            var container:DisplayObjectContainer = result.object;

            var objects:Array = [];

            var obj:DisplayObject;

            getObjectsByPreorderTraversal(container, result.params, objects);

            setRoot(container, result.params[container]);

            //add other objects
            for each (obj in objects)
            {
                addFrom(obj, result.params[obj], null);
            }

            importSetting(result.data.setting);

            setLayerChanged();
            setChanged();
        }

        public function loadExternal(data:Object, file:File):void
        {
            _assetMediator.file = file;

            var name:String = FileListingHelper.stripPostfix(file.name);

            //create a container to hold the external element
            var containerData:Object = {cls:ParamUtil.getClassName(Sprite), customParams:{}, params:{name:name}};
            var containerResult:Object = _uiBuilder.createUIElement(containerData);
            var container:Sprite = containerResult.object;
            var param:Object = containerResult.params;
            _uiBuilder.setExternalSource(param, name);

            //create the external element
            var result:Object = _uiBuilder.load(data);
            var root:DisplayObjectContainer = result.object;
            container.addChild(root);
            param.externalParams = result.params;

            addFrom(container, param, getParent());
        }

        private function reset():void
        {
            selectObject(null);
            _layoutContainer.removeChildren(0, -1, true);
            _snapContainer.removeChildren(0, -1, true);
            _extraParamsDict = new Dictionary();
            _dataProvider = new ListCollection();
            _collapseMap = new Dictionary();

            canvasSize = new Point(_setting.defaultCanvasWidth, _setting.defaultCanvasHeight);
            background = null;
            _historyManager.reset();
        }

        public function clear():void
        {
            reset();
            createRoot();
            refreshLabels();
            setChanged();
        }

        public function createFromData(data:Object):void
        {
            try
            {
                var p:Point;

                var parent:DisplayObjectContainer = getParent();

                if ("x" in data.params && "y" in data.params)
                {
                    var centerPanel:CenterPanel = UIEditorScreen.instance.centerPanel;
                    p = _container.localToGlobal(new Point(centerPanel.horizontalScrollPosition + data.params.x, centerPanel.verticalScrollPosition + data.params.y));
                    p = parent.globalToLocal(new Point(p.x, p.y));
                    data.params.x = p.x;
                    data.params.y = p.y;
                }
                else
                {
                    p = getNewObjectPosition();
                    data.params.x = p.x;
                    data.params.y = p.y;
                }

                var result:Object = _uiBuilder.createUIElement(data);
                var paramDict:Dictionary = new Dictionary();

                var obj:DisplayObject = result.object;
                paramDict[obj] = result.params;

                _historyManager.add(new CreateOperation(obj, paramDict, parent));

                setDefaultPivot(obj);

                addFrom(obj, result.params, parent);

                selectObject(obj);

                setLayerChanged();

                setChanged();
            }
            catch(e:Error)
            {
                InfoPopup.show(e.getStackTrace());
            }
        }

        private function getNewObjectPosition():Point
        {
            var parent:DisplayObjectContainer = getParent();

            if (parent === _root && parent.x == 0 && parent.y == 0)
            {
                var centerPanel:CenterPanel = UIEditorScreen.instance.centerPanel;

                var width:Number = Math.min(centerPanel.width, _canvas.width * scale);
                var height:Number = Math.min(centerPanel.height, _canvas.height * scale);

                return new Point((centerPanel.horizontalScrollPosition + width * 0.5) / scale,
                                (centerPanel.verticalScrollPosition + height * 0.5) / scale);
            }
            else
            {
                return new Point(0, 0);
            }
        }

        public function get dataProvider():ListCollection
        {
            return _dataProvider;
        }

        public function refresh():void
        {
            for (var i:int = 0; i < _dataProvider.length; ++i)
            {
                var item:Object = _dataProvider.getItemAt(i);

                updateHidden(item.obj, item.hidden);
                updateLock(item.obj, item.lock);
            }
        }

        private function updateHidden(obj:DisplayObject, value:Boolean):void
        {
            obj.visible = !value;
        }

        private function updateLock(obj:DisplayObject, value:Boolean):void
        {
            obj.touchable = !value;
        }

        private function refreshLabels():void
        {
            for (var i:int = 0; i < _dataProvider.length; ++i)
            {
                var item:Object = _dataProvider.getItemAt(i);
                var obj:DisplayObject = item.obj;
                item.label = obj.name;
                item.layer = getLayerFromObject(obj);
                item.isContainer = _uiBuilder.isContainer(_extraParamsDict[obj]);
                _dataProvider.updateItemAt(i);
            }
        }

        public function setChanged():void
        {
            refreshLabels();
            dispatchEventWith(DocumentEventType.CHANGE);

            if (_container && _container.parent is FeathersControl)
            {
                (_container.parent as FeathersControl).invalidate();
            }
        }

        public function setLayerChanged():void
        {
            sortDataProvider();
        }

        public function get snapPixel():Boolean
        {
            return _snapPixel;
        }

        public function set snapPixel(value:Boolean):void
        {
            _snapPixel = value;
        }

        public function get showTextBorder():Boolean
        {
            return _showTextBorder;
        }

        public function set showTextBorder(value:Boolean):void
        {
            _showTextBorder = value;

            for (var i:int = 0; i < _dataProvider.length; ++i)
            {
                var textField:TextField = _dataProvider.getItemAt(i).obj as TextField;
                if (textField) textField.border = _showTextBorder;
            }
        }

        private function isAncestorOf(child:DisplayObject, parent:DisplayObject):Boolean
        {
            var p:DisplayObject = child;
            while (p)
            {
                p = p.parent;
                if (p === parent) return true;
            }

            return false;
        }

        public function cut():void
        {
            var obj:DisplayObject;
            var newDict:Dictionary;

            var objects:Array = selectedObjects.concat();

            if (objects.length == 0)
            {
                info("Please select some objects");
                return;
            }
            else if (objects.length == 1)
            {
                obj = objects[0];

                if (_root === obj)
                {
                    info("Can't remove root");
                    return;
                }

                copy();
                newDict = new Dictionary();
                recreateFromParam(obj, _extraParamsDict, newDict);
                _historyManager.add(new CutOperation(obj, newDict, obj.parent));
                removeTree(obj);
            }
            else
            {
                if (!canGroup(objects))
                {
                    InfoPopup.show("Can't cut display objects with different parents");
                    return;
                }

                copy();

                var ops:Array = [];

                for each (obj in objects)
                {
                    newDict = new Dictionary();
                    recreateFromParam(obj, _extraParamsDict, newDict);
                    ops.push(new CutOperation(obj, newDict, obj.parent));
                    removeTree(obj);
                }

                _historyManager.add(new CompositeHistoryOperation(ops));
            }
        }

        public function copy():void
        {
            var obj:DisplayObject;

            var objects:Array = selectedObjects.concat();
            objects.sort(groupSortFunc);

            var data:Object;

            if (objects.length == 0)
            {
                info("Please select some objects");
                return;
            }
            else if (objects.length == 1)
            {
                obj = objects[0];
                data = _uiBuilder.copy(obj, _extraParamsDict);
            }
            else
            {
                if (!canGroup(objects))
                {
                    InfoPopup.show("Can't copy display objects with different parents");
                    return;
                }

                data = _uiBuilder.copy(objects, _extraParamsDict);
            }

            Clipboard.generalClipboard.setData(ClipboardFormats.TEXT_FORMAT, data);
        }

        private function createClipboardDataWrapper(obj:Object):Object
        {
            if (obj is Array)
            {
                return {layout:{
                    children:obj,
                    cls:"starling.display.Sprite",
                    customParams:{}
                }, multiple:true}
            }
            else
            {
                return {layout:obj};
            }
        }

        public function paste():void
        {
            try
            {
                var data:Object = createClipboardDataWrapper(_uiBuilder.paste(Clipboard.generalClipboard.getData(ClipboardFormats.TEXT_FORMAT) as String));

                if (data)
                {
                    var parent:DisplayObjectContainer = getParent();

                    var result:Object = _uiBuilder.load(data, false);
                    var root:DisplayObject = result.object;
                    var paramDict:Dictionary = result.params;

                    var p:Point = getNewObjectPosition();

                    if (data.multiple)
                    {
                        var container:DisplayObjectContainer = root as DisplayObjectContainer;

                        var ops:Array = [];

                        while (container.numChildren > 0)
                        {
                            var obj:DisplayObject = container.getChildAt(0);
                            ops.push(new PasteOperation(obj, paramDict, parent));
                            addTree(obj, paramDict, parent);
                        }

                        _historyManager.add(new CompositeHistoryOperation(ops));
                    }
                    else
                    {
                        root.x = p.x;
                        root.y = p.y;

                        _historyManager.add(new PasteOperation(root, paramDict, parent));

                        addTree(root, paramDict, parent);
                    }
                }
            }
            catch(e:Error)
            {
                info("Invalid Format");
            }
        }

        public function duplicate():void
        {
            if (selectedObject === _root)
            {
                info("Can't duplicate root");
                return;
            }

            if (!canGroup(selectedObjects))
            {
                InfoPopup.show("Can't duplicate display objects with different parents")
                return;
            }

            copy();
            selectObject(selectedObject.parent);
            paste();
        }

        private var _background:DisplayObject;

        public function set background(obj:DisplayObject):void
        {
            if (_background)
            {
                _background.removeFromParent(true);
                _background = null;
            }

            if (obj)
            {
                _background = obj;
                _backgroundContainer.addChild(obj);
            }
        }

        public function get background():DisplayObject
        {
            return _background;
        }


        private function info(text:String):void
        {
            var popup:InfoPopup = new InfoPopup(300, 200);
            popup.title = text;
            popup.buttons = ["OK"];

            PopUpManager.addPopUp(popup);
        }

        public function get enableBoundingBox():Boolean
        {
            return _boundingBoxContainer.enable;
        }

        public function set enableBoundingBox(value:Boolean):void
        {
            _boundingBoxContainer.enable = value;
        }

        private var _canvasSize:Point = new Point();

        public function set canvasSize(value:Point):void
        {
            if (_canvasSize.x != value.x || _canvasSize.y != value.y)
            {
                _canvasSize = value;
            }

            _layoutContainer.width = _canvas.width = canvasSize.x;
            _layoutContainer.height = _canvas.height = canvasSize.y;

            _container.mask = new Quad(canvasSize.x * _canvasContainer.scaleX, canvasSize.y * _canvasContainer.scaleY);

            FeathersControl(_container.parent).invalidate();

            dispatchEventWith(DocumentEventType.CANVAS_CHANGE);
        }

        public function get canvasSize():Point
        {
            return _canvasSize;
        }

        public function get canvasColor():uint
        {
            return _canvas.color;
        }

        public function set canvasColor(value:uint):void
        {
            if (_canvas.color != value)
            {
                _canvas.color = value;
                dispatchEventWith(DocumentEventType.CANVAS_CHANGE);
            }
        }

        public function get container():Sprite
        {
            return _container;
        }

        public function useGameTheme(target:IFeathersControl):Boolean
        {
            //work around to fix theme pollution, not ideal
            var obj:DisplayObject = target as DisplayObject;
            while (obj)
            {
                if (obj is IFeathersControl && IFeathersControl(obj).styleName.indexOf("uiEditor") != -1)
                    return false;
                obj = obj.parent;
            }

            var object:DisplayObject = target as DisplayObject;

            return (container && container.contains(object)) || (_testContainer && _testContainer.contains(object));
        }

        public function get extraParamsDict():Dictionary
        {
            return _extraParamsDict;
        }

        public function get uiBuilder():IUIBuilder
        {
            return _uiBuilder;
        }

        public function get hasFocus():Boolean
        {
            return !(FocusManager.focus is TextInput || FocusManager.focus is TextArea)
        }

        public function get root():DisplayObjectContainer
        {
            return _root;
        }

        public function get scale():Number
        {
            return _layoutContainer.scaleX;
        }

        public function set scale(value:Number):void
        {
            if (scale != value)
            {
                _layoutContainer.scaleX = _layoutContainer.scaleY = value;
                _backgroundContainer.scaleX = _backgroundContainer.scaleY = value;
                _canvasContainer.scaleX = _canvasContainer.scaleY = value;

                FeathersControl(_container.parent).invalidate();

                _container.mask = new Quad(canvasSize.x * _canvasContainer.scaleX, canvasSize.y * _canvasContainer.scaleY);

                _boundingBoxContainer.reload();

                dispatchEventWith(DocumentEventType.CANVAS_CHANGE);
            }
        }

        public function collapse(obj:DisplayObject):void
        {
            if (!_collapseMap[obj])
            {
                _collapseMap[obj] = true;
                setLayerChanged();
                setChanged();
            }
        }

        public function expand(obj:DisplayObject):void
        {
            if (_collapseMap[obj])
            {
                delete _collapseMap[obj];
                setLayerChanged();
                setChanged();
            }
        }

        public function collapseAll():void
        {
            var objects:Array = [];
            getObjectsByPreorderTraversal(_root, _extraParamsDict, objects);

            for each(var obj:DisplayObject in objects)
            {
                _collapseMap[obj] = true;
            }

            setLayerChanged();
            setChanged();
        }

        public function expandAll():void
        {
            _collapseMap = new Dictionary();

            setLayerChanged();
            setChanged();
        }

        private function loadFlags(setting:Object):void
        {
            var objects:Array = [];
            getObjectsByPreorderTraversal(_root, _extraParamsDict, objects);

            var hiddenFlag:String = setting.hidden;
            var lockFlag:String = setting.lock;

            for (var i:int = 0; i < objects.length; ++i)
            {
                if (hiddenFlag) objects[i].visible = (hiddenFlag.charAt(i) != "1");
                if (lockFlag) objects[i].touchable = (lockFlag.charAt(i) != "1");
            }
        }

        private function saveFlags(setting:Object):void
        {
            var objects:Array = [];
            getObjectsByPreorderTraversal(_root, _extraParamsDict, objects);

            delete setting["hidden"];
            delete setting["lock"];

            var hiddenFlag:String = createFlag(objects, "visible");
            var lockFlag:String = createFlag(objects, "touchable");
            if (hiddenFlag) setting["hidden"] = hiddenFlag;
            if (lockFlag) setting["lock"] = lockFlag;
        }

        private function createFlag(objects:Array, field:String):String
        {
            var saved:Boolean = false;

            var flag:String = "";
            for each (var obj:DisplayObject in objects)
            {
                var value:Boolean = !obj[field];
                if (value == true) saved = true;
                flag += value ? "1" : "0";
            }

            return saved ? flag : null;
        }

        private function onSettingChanged():void
        {
            _uiBuilder.prettyData = _setting.prettyJSON;
            setLayerChanged();
            setChanged();
        }


        public function get boundingBoxContainer():BoundingBoxContainer
        {
            return _boundingBoxContainer;
        }

        private function setDefaultPivot(obj:DisplayObject):void
        {
            if (obj.pivotX == 0 && obj.pivotY == 0)
                DisplayObjectUtil.movePivotToAlign(obj, _setting.defaultHorizontalPivot, _setting.defaultVerticalPivot);
        }

        public function snapshot():void
        {
            var sprite:Sprite = new Sprite();

            sprite.addChild(startTest());
            SnapshotHelper.snapshot(sprite, new Point(_canvas.width, _canvas.height), getSnapshotFileName());

            UIEditorScreen.instance.workspaceDir.openWithDefaultApplication();
        }

        public static const DEFAULT_FILENAME:String = "snapshot";
        public static const DEFAULT_EXTENSION:String = ".png";

        private function getSnapshotFileName():String
        {
            var workspace:File = UIEditorScreen.instance.workspaceDir;
            var name:String = DEFAULT_FILENAME + DEFAULT_EXTENSION;

            if (!workspace.resolvePath(name).exists)
                return name;

            for (var i:int = 1;;++i)
            {
                name = DEFAULT_FILENAME + i + DEFAULT_EXTENSION;
                if (!workspace.resolvePath(name).exists)
                    return name;
            }
        }

        public function get keyboardWatcher():KeyboardWatcher
        {
            return _keyboardWatcher;
        }

        public function get selectedIndices():Vector.<int>
        {
            var indices:Vector.<int> = new Vector.<int>();

            for each (var obj:Object in _selectManager.selectedObjects)
            {
                for (var i:int = 0; i < _dataProvider.length; ++i)
                {
                    var item:Object = _dataProvider.getItemAt(i);

                    if (item && item.obj === obj)
                    {
                        indices.push(i);
                        break;
                    }
                }
            }

            return indices;
        }

        public function selectObjectAtIndices(indices:Vector.<int>):void
        {
            if (sameIndices(selectedIndices, indices))
                return;

            var array:Array = [];

            for each (var index:int in indices)
            {
                var obj:DisplayObject = _dataProvider.getItemAt(index).obj;
                array.push(obj);
            }

            _selectManager.selectObjects(array);
        }

        private function sameIndices(indices1:Vector.<int>, indices2:Vector.<int>):Boolean
        {
            if (indices1.length != indices2.length) return false;

            indices1.concat().sort(compare);
            indices2.concat().sort(compare);

            for (var i:int = 0, l:int = indices1.length; i < l; ++i)
            {
                if (indices1[i] != indices2[i]) return false;
            }

            return true;
        }

        private function compare(x:int, y:int):int
        {
            return x - y;
        }

        public function inverseLayer():Boolean
        {
            return _setting.layoutOrder == "Photoshop";
        }

        public function group(cls:Class):void
        {
            var array:Array = selectedObjects.concat();
            array.sort(groupSortFunc);

            if (isRootSelected(array))
            {
                InfoPopup.show("Can't group root");
                return;
            }

            if (!canGroup(array))
            {
                InfoPopup.show("Can't group display objects with different parents")
                return;
            }

            var first:DisplayObject = array[0];
            var parent:DisplayObjectContainer = first.parent;
            var firstIndex:int = parent.getChildIndex(first);

            var data:Object = UIComponentHelper.createDefaultComponentData(ParamUtil.getClassName(cls));

            var container:DisplayObjectContainer = _uiBuilder.createUIElement(data).object;
            container.name = "container";
            parent.addChildAt(container, firstIndex);
            _extraParamsDict[container] = data;

            for each (var obj:DisplayObject in array)
                container.addChild(obj);

            _historyManager.add(new GroupOperation(container, array));

            setLayerChanged();
            setChanged();
        }

        private function isRootSelected(array:Array):Boolean
        {
            return (array.length == 1 && array[0] === _root);
        }

        private function canGroup(array:Array):Boolean
        {
            if (array.length == 0) return false;

            var parent:DisplayObject = array[0].parent;

            for (var i:int = 1; i < array.length; ++i)
            {
                if (array[i].parent !== parent)
                    return false;
            }

            return true;
        }

        private function canUngroup(array:Array):Boolean
        {
            if (array.length == 1)
            {
                var obj:DisplayObject = array[0];
                if (obj is Sprite || obj is LayoutGroup)
                    return true;
            }

            return false;
        }

        public function ungroup():void
        {
            var array:Array = selectedObjects.concat();

            if (isRootSelected(array))
            {
                InfoPopup.show("Can't ungroup root");
                return;
            }

            if (!canUngroup(array))
            {
                InfoPopup.show("Please select a Sprite or LayoutGroup");
                return;
            }

            var container:DisplayObjectContainer = array[0];
            var parent:DisplayObjectContainer = container.parent;
            var index:int = parent.getChildIndex(container);
            container.removeFromParent();

            var children:Array = [];

            while (container.numChildren > 0)
            {
                var obj:DisplayObject = container.getChildAt(container.numChildren - 1);
                children.unshift(obj);
                parent.addChildAt(obj, index);
            }

            _historyManager.add(new UngroupOperation(container, children));

            setLayerChanged();
            setChanged();
        }

        private function groupSortFunc(obj1:DisplayObject, obj2:DisplayObject):int
        {
            return obj1.parent.getChildIndex(obj1) - obj2.parent.getChildIndex(obj2);
        }

        public function get dragMode():Boolean
        {
            return _keyboardWatcher.hasKeyPressed(Keyboard.SPACE);
        }

        public function dragCanvas(dx:Number, dy:Number):void
        {
            var centerPanel:CenterPanel = UIEditorScreen.instance.centerPanel;

            centerPanel.horizontalScrollPosition = Math.min(
                    Math.max(centerPanel.minHorizontalScrollPosition, centerPanel.horizontalScrollPosition - dx),
                    centerPanel.maxHorizontalScrollPosition);

            centerPanel.verticalScrollPosition = Math.min(
                    Math.max(centerPanel.minVerticalScrollPosition, centerPanel.verticalScrollPosition - dy),
                    centerPanel.maxVerticalScrollPosition);
        }

        public function get layoutSearchString():String
        {
            return _layoutSearchString;
        }

        public function set layoutSearchString(value:String):void
        {
            if (_layoutSearchString != value)
            {
                _layoutSearchString = value;
                setLayerChanged();
                setChanged();
            }
        }
    }
}