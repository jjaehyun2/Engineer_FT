package com.github.asyncmc.mojang.sessions.flash.model {

import org.openapitools.common.ListWrapper;
import com.github.asyncmc.mojang.sessions.flash.model.PlayerProfileProperty;

    public class PlayerProfileList implements ListWrapper {
        // This declaration below of _PlayerProfile_obj_class is to force flash compiler to include this class
        private var _playerProfile_obj_class: com.github.asyncmc.mojang.sessions.flash.model.PlayerProfile = null;
        [XmlElements(name="playerProfile", type="com.github.asyncmc.mojang.sessions.flash.model.PlayerProfile")]
        public var playerProfile: Array = new Array();

        public function getList(): Array{
            return playerProfile;
        }

}

}