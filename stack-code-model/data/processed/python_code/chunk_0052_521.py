package com.github.asyncmc.mojang.api.flash.model {

import com.github.asyncmc.mojang.api.flash.model.SkinModel;
import flash.filesystem.File;

    [XmlRootNode(name="UploadSkinRequest")]
    public class UploadSkinRequest {
                [XmlElement(name="model")]
        public var model: SkinModel = NaN;
        /* The skin image in PNG format */
        [XmlElement(name="file")]
        public var file: File = null;

    public function toString(): String {
        var str: String = "UploadSkinRequest: ";
        str += " (model: " + model + ")";
        str += " (file: " + file + ")";
        return str;
    }

}

}