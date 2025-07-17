/**
 *  Starling Builder
 *  Copyright 2015 SGN Inc. All Rights Reserved.
 *
 *  This program is free software. You can redistribute and/or modify it in
 *  accordance with the terms of the accompanying license agreement.
 */
package starlingbuilder.editor.history
{
    import starlingbuilder.editor.UIEditorApp;
    import starlingbuilder.util.history.IHistoryOperation;

    import flash.utils.Dictionary;

    import starling.display.DisplayObject;
    import starling.display.DisplayObjectContainer;

    public class CreateOperation extends SingleHistoryOperation
    {
        protected var _index:int;

        public function CreateOperation(target:Object, paramDict:Dictionary, parent:Object)
        {
            super(OperationType.CREATE, target, paramDict, parent);

            _index = (parent as DisplayObjectContainer).getChildIndex(target as DisplayObject);
        }

        override public function undo():void
        {
            UIEditorApp.instance.documentManager.removeTree(_target as DisplayObject);
        }

        override public function redo():void
        {
            var obj:DisplayObject = _target as DisplayObject;
            var paramDict:Dictionary = _beforeValue as Dictionary;
            var parent:DisplayObjectContainer = _afterValue as DisplayObjectContainer;

            UIEditorApp.instance.documentManager.addTree(obj, paramDict, parent, _index);
        }

        override public function canMergeWith(previousOperation:IHistoryOperation):Boolean
        {
            return false;
        }

        override public function dispose():void
        {
            var obj:DisplayObject = _target as DisplayObject;
            if (obj.stage == null)
                obj.dispose();
        }

        override public function info():String
        {
            return "Create";
        }
    }
}