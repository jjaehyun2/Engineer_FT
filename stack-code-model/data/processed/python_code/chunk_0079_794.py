package com.github.asyncmc.mojang.api.flash.model {

import org.openapitools.common.ListWrapper;

    public class SkinModelList implements ListWrapper {
        // This declaration below of _SkinModel_obj_class is to force flash compiler to include this class
        private var _skinModel_obj_class: com.github.asyncmc.mojang.api.flash.model.SkinModel = null;
        [XmlElements(name="skinModel", type="com.github.asyncmc.mojang.api.flash.model.SkinModel")]
        public var skinModel: Array = new Array();

        public function getList(): Array{
            return skinModel;
        }

}

}