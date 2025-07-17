package com.github.asyncmc.mojang.api.flash.model {

import org.openapitools.common.ListWrapper;

    public class SecurityAnswerIdList implements ListWrapper {
        // This declaration below of _SecurityAnswerId_obj_class is to force flash compiler to include this class
        private var _securityAnswerId_obj_class: com.github.asyncmc.mojang.api.flash.model.SecurityAnswerId = null;
        [XmlElements(name="securityAnswerId", type="com.github.asyncmc.mojang.api.flash.model.SecurityAnswerId")]
        public var securityAnswerId: Array = new Array();

        public function getList(): Array{
            return securityAnswerId;
        }

}

}