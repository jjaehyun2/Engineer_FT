package com.company.assembleegameclient.ui.icons {
import flash.display.BitmapData;

public class IconButtonFactory {


    public function IconButtonFactory() {
        super();
    }

    public function create(_arg_1:BitmapData, _arg_2:String, _arg_3:String, _arg_4:String, _arg_5:int = 0):IconButton {
        var _local6:IconButton = new IconButton(_arg_1, _arg_2, _arg_3, _arg_4, _arg_5);
        return _local6;
    }
}
}