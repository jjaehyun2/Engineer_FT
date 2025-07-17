/**
 *  Starling Builder
 *  Copyright 2015 SGN Inc. All Rights Reserved.
 *
 *  This program is free software. You can redistribute and/or modify it in
 *  accordance with the terms of the accompanying license agreement.
 */
package starlingbuilder.editor.ui
{
    import starlingbuilder.util.menu.BaseMenu;

    import flash.display.NativeMenu;
    import flash.ui.Keyboard;

    public class MainMenu extends BaseMenu
    {
        public static const FILE:String = "File";
        public static const EDIT:String = "Edit";
        public static const VIEW:String = "View";
        public static const OPTION:String = "Option";
        public static const WORKSPACE:String = "Workspace";
        public static const LOCALIZATION:String = "Localization";
        public static const HELP:String = "Help";

        public static const NEW:String = "New";
        public static const OPEN:String = "Open";
        public static const OPEN_RECENT:String = "Open recent";
        public static const SAVE:String = "Save";
        public static const SAVE_AS:String = "Save as";
        public static const LOAD_EXTERNAL:String = "Load external";
        public static const CHOOSE_WORKSPACE:String = "Choose workspace";
        public static const RELOAD:String = "Reload";
        public static const TEST:String = "Test";
        public static const TEST_GAME:String = "Test Game";
        public static const QUIT:String = "Quit";

        public static const UNDO:String = "Undo";
        public static const REDO:String = "Redo";

        public static const GROUP_WITH_SPRITE:String = "Group with Sprite";
        public static const GROUP_WITH_LAYOUTGROUP:String = "Group with LayoutGroup";
        public static const UNGROUP:String = "Ungroup";

        public static const CUT:String = "Cut";
        public static const COPY:String = "Copy";
        public static const PASTE:String = "Paste";
        public static const DUPLICATE:String = "Duplicate";
        public static const DESELECT:String = "Deselect";
        public static const DELETE:String = "Delete";
        public static const MOVE_UP:String = "Move Up";
        public static const MOVE_DOWN:String = "Move Down";

        public static const ZOOM_IN:String = "Zoom In";
        public static const ZOOM_OUT:String = "Zoom Out";
        public static const RESET_ZOOM:String = "Reset Zoom";
        public static const CANVAS_SNAPSHOT:String = "Canvas Snapshot"

        public static const SHOW_TEXT_BORDER:String = "Show text border";
        public static const SNAP_PIXEL:String = "Snap pixel";
        public static const RESIZABLE_BOX:String = "Resizable box";

        public static const OPEN_WORKSPACE:String = "Open workspace";
        public static const EDIT_TEMPLATE:String = "Edit template override";
        public static const DELETE_TEMPLATE:String = "Delete template override";
        public static const SETTING:String = "Setting";
        public static const WORKSPACE_SETTING:String = "Workspace Setting";

        public static const DOCUMENTATION:String = "Documentation";
        public static const GITHUB_PAGE:String = "Github Page";
        public static const ABOUT:String = "About";
        public static const CHECK_FOR_UPDATE:String = "Check for update";

        public static const FILE_MENU:Array = [
            {"label":NEW, "key":"n"},
            {"label":OPEN, "key":"o"},
            {"label":OPEN_RECENT, "menu":true},
            {"label":SAVE, "key":"s"},
            {"label":SAVE_AS},
            {"label":LOAD_EXTERNAL, "key":"l"},
            {"separator":true},
            {"label":CHOOSE_WORKSPACE},
            {"label":RELOAD},
            {"separator":true},
            {"label":TEST, "key":"t"},
            {"label":TEST_GAME, "key":"T"},
            {"separator":true},
            {"label":SETTING}
        ]

        public static const EDIT_MENU:Array = [
            {"label":UNDO, "key":"z", "disabled":true},
            {"label":REDO, "key":"Z", "disabled":true},
            {"separator":true},
            {"label":CUT, "key":"x"},
            {"label":COPY, "key":"c"},
            {"label":PASTE, "key":"v"},
            {"label":DUPLICATE, "key":"d"},
            {"label":DESELECT},
            {"label":DELETE},
            {"separator":true},
            {"label":MOVE_UP, "key":"["},
            {"label":MOVE_DOWN, "key":"]"},
            {"separator":true},
            {"label":GROUP_WITH_SPRITE, "key":"g"},
            {"label":GROUP_WITH_LAYOUTGROUP, "key":"G"},
            {"label":UNGROUP, "key":"u"},
        ]

        public static const VIEW_MENU:Array = [
            {"label":ZOOM_IN, "key":"+"},
            {"label":ZOOM_OUT, "key":"-"},
            {"label":RESET_ZOOM, "key":"0"},
            {"label":CANVAS_SNAPSHOT}
        ]

        public static const OPTION_MENU:Array = [
            {"label":SHOW_TEXT_BORDER},
            {"label":SNAP_PIXEL},
            {"label":RESIZABLE_BOX}
        ]

        public static const WORKSPACE_MENU:Array = [
            {"label":WORKSPACE_SETTING},
            {"separator":true},
            {"label":OPEN_WORKSPACE},
            {"label":EDIT_TEMPLATE},
            {"label":DELETE_TEMPLATE}
        ]

        public static const HELP_MENU:Array = [
            {"label":DOCUMENTATION},
            {"label":GITHUB_PAGE},
            {"label":CHECK_FOR_UPDATE},
            {"label":ABOUT},
        ]

        private static var _instance:MainMenu;

        public function MainMenu():void
        {
            super();

            if (!_instance)
            {
                _instance = this;
            }
            else
            {
                throw new Error("Menu already created!");
            }
        }

        override protected function createRootMenu():void
        {
            _rootMenu = new NativeMenu();
            createSubMenu(FILE_MENU, FILE);
            createSubMenu(EDIT_MENU, EDIT);
            createSubMenu(VIEW_MENU, VIEW);
            createSubMenu(OPTION_MENU, OPTION);
            createSubMenu(WORKSPACE_MENU, WORKSPACE);
        }

        public static function get instance():MainMenu
        {
            return _instance;
        }
    }
}