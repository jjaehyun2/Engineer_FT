package com.github.asyncmc.mojang.api.flash.model {

import org.openapitools.common.ListWrapper;
import com.github.asyncmc.mojang.api.flash.model.SkinModel;

    public class ChangeSkinRequestList implements ListWrapper {
        // This declaration below of _ChangeSkinRequest_obj_class is to force flash compiler to include this class
        private var _changeSkinRequest_obj_class: com.github.asyncmc.mojang.api.flash.model.ChangeSkinRequest = null;
        [XmlElements(name="changeSkinRequest", type="com.github.asyncmc.mojang.api.flash.model.ChangeSkinRequest")]
        public var changeSkinRequest: Array = new Array();

        public function getList(): Array{
            return changeSkinRequest;
        }

}

}