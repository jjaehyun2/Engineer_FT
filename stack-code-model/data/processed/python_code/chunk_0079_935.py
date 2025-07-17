package com.github.asyncmc.mojang.sessions.flash.model {

import org.openapitools.common.ListWrapper;

    public class PlayerSkinMetadataList implements ListWrapper {
        // This declaration below of _PlayerSkinMetadata_obj_class is to force flash compiler to include this class
        private var _playerSkinMetadata_obj_class: com.github.asyncmc.mojang.sessions.flash.model.PlayerSkinMetadata = null;
        [XmlElements(name="playerSkinMetadata", type="com.github.asyncmc.mojang.sessions.flash.model.PlayerSkinMetadata")]
        public var playerSkinMetadata: Array = new Array();

        public function getList(): Array{
            return playerSkinMetadata;
        }

}

}