package com.github.asyncmc.mojang.authentication.flash.model {

import org.openapitools.common.ListWrapper;
import com.github.asyncmc.mojang.authentication.flash.model.AccessKeys;

    public class RefreshRequestList implements ListWrapper {
        // This declaration below of _RefreshRequest_obj_class is to force flash compiler to include this class
        private var _refreshRequest_obj_class: com.github.asyncmc.mojang.authentication.flash.model.RefreshRequest = null;
        [XmlElements(name="refreshRequest", type="com.github.asyncmc.mojang.authentication.flash.model.RefreshRequest")]
        public var refreshRequest: Array = new Array();

        public function getList(): Array{
            return refreshRequest;
        }

}

}