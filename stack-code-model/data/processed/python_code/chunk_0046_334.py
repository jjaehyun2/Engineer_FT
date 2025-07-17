package com.github.asyncmc.mojang.authentication.flash.model {

import org.openapitools.common.ListWrapper;
import com.github.asyncmc.mojang.authentication.flash.model.AccessKeys;

    public class AuthenticationList implements ListWrapper {
        // This declaration below of _Authentication_obj_class is to force flash compiler to include this class
        private var _authentication_obj_class: com.github.asyncmc.mojang.authentication.flash.model.Authentication = null;
        [XmlElements(name="authentication", type="com.github.asyncmc.mojang.authentication.flash.model.Authentication")]
        public var authentication: Array = new Array();

        public function getList(): Array{
            return authentication;
        }

}

}