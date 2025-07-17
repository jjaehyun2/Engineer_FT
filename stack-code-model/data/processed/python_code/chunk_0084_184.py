/**
 *  Starling Builder
 *  Copyright 2015 SGN Inc. All Rights Reserved.
 *
 *  This program is free software. You can redistribute and/or modify it in
 *  accordance with the terms of the accompanying license agreement.
 */
package starlingbuilder.editor.serialize
{
    import starling.events.Event;

    import starlingbuilder.editor.UIEditorApp;
    import starlingbuilder.editor.upgrade.ILayoutConverter;
    import starlingbuilder.editor.upgrade.LayoutConverterV1;
    import starlingbuilder.editor.upgrade.LayoutConverterV2;
    import starlingbuilder.editor.upgrade.LayoutUpgradePolicy;
    import starlingbuilder.util.feathers.popup.InfoPopup;
    import starlingbuilder.util.serialize.IDocumentMediator;

    import flash.filesystem.File;

    public class UIEditorDocumentMediator implements IDocumentMediator
    {
        private var _converter:ILayoutConverter

        public function UIEditorDocumentMediator()
        {
            _converter = new LayoutConverterV2();
        }

        public function read(obj:Object, file:File):void
        {
            if (obj)
            {
                var policy:String = _converter.getUpgradePolicy(obj);

                var popup:InfoPopup;

                if (policy == LayoutUpgradePolicy.CAN_UPGRADE)
                {
                    popup = InfoPopup.show("Your layout version is older than the editor version.\nWould you like to convert to a newer layout version format?", ["OK", "Cancel"]);
                    popup.addEventListener(Event.COMPLETE, function(event:Event):void {
                        if (event.data == 0)
                            obj = _converter.upgrade(obj);

                        UIEditorApp.instance.documentManager.importData(obj, file);
                    })
                }
                else if (policy == LayoutUpgradePolicy.CANNOT_UPGRADE)
                {
                    popup = InfoPopup.show("Your layout version is newer than the editor version.\nYou may need to upgrade the editor to properly load it.", ["OK"])
                    popup.addEventListener(Event.COMPLETE, function(event:Event):void {
                        UIEditorApp.instance.documentManager.importData(obj, file);
                    });
                }
                else
                {
                    UIEditorApp.instance.documentManager.importData(obj, file);
                }
            }
            else
            {
                UIEditorApp.instance.documentManager.clear();
            }
        }

        public function write():Object
        {
            return UIEditorApp.instance.documentManager.export();
        }

        public function get defaultSaveFilename():String
        {
            return "layout.json";
        }
    }
}