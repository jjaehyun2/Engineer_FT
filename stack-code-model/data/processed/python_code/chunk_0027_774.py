/**
 *  Starling Builder
 *  Copyright 2015 SGN Inc. All Rights Reserved.
 *
 *  This program is free software. You can redistribute and/or modify it in
 *  accordance with the terms of the accompanying license agreement.
 */
package starlingbuilder.editor
{
    import starlingbuilder.editor.controller.ComponentRenderSupport;
    import starlingbuilder.editor.controller.DocumentManager;
    import starlingbuilder.editor.controller.LocalizationManager;
    import starlingbuilder.editor.helper.DragHelper;
    import starlingbuilder.editor.helper.SelectHelper;
    import starlingbuilder.editor.themes.MetalWorksDesktopTheme2;

    import starling.display.Sprite;
    import starling.events.EventDispatcher;

    import starlingbuilder.util.AppUpdater;
    import starling.utils.AssetManager;

    import starlingbuilder.util.LogAssetManager;

    public class UIEditorApp extends Sprite
    {
        public static var SWF_VERSION:int;

        private var _assetManager:AssetManager;
        private var _documentManager:DocumentManager;
        private var _localizationManager:LocalizationManager;
        private var _notificationDispatcher:EventDispatcher;

        private var _appUpdater:AppUpdater;

        private static var _instance:UIEditorApp;

        public static function get instance():UIEditorApp
        {
            return _instance;
        }


        public function UIEditorApp()
        {
            _appUpdater = new AppUpdater();

            setup();

            new MetalWorksDesktopTheme2();

            addChild(createEditorScreen());
        }

        private function setup():void
        {
            SelectHelper.setup();
            DragHelper.setup();

            _assetManager = new LogAssetManager();
            _assetManager.numConnections = 100;
            _assetManager.keepFontXmls = true;
            _notificationDispatcher = new EventDispatcher();

            _instance = this;
        }

        public function init():void
        {
            _localizationManager = new LocalizationManager();
            _documentManager = new DocumentManager(_assetManager, _localizationManager);
            ComponentRenderSupport.support = _documentManager;
        }

        public function get assetManager():AssetManager
        {
            return _assetManager;
        }

        public function get documentManager():DocumentManager
        {
            return _documentManager;
        }

        public function get localizationManager():LocalizationManager
        {
            return _localizationManager;
        }

        public function get notificationDispatcher():EventDispatcher
        {
            return _notificationDispatcher;
        }

        protected function createEditorScreen():Sprite
        {
            return new UIEditorScreen();
        }

        public function get appUpdater():AppUpdater
        {
            return _appUpdater;
        }


    }
}