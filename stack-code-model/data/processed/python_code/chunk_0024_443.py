package com.github.asyncmc.mojang.sessions.flash.model {

import org.openapitools.common.ListWrapper;
import com.github.asyncmc.mojang.sessions.flash.model.PlayerSkinURL;
import com.github.asyncmc.mojang.sessions.flash.model.PlayerTextureURL;

    public class PlayerTextureList implements ListWrapper {
        // This declaration below of _PlayerTexture_obj_class is to force flash compiler to include this class
        private var _playerTexture_obj_class: com.github.asyncmc.mojang.sessions.flash.model.PlayerTexture = null;
        [XmlElements(name="playerTexture", type="com.github.asyncmc.mojang.sessions.flash.model.PlayerTexture")]
        public var playerTexture: Array = new Array();

        public function getList(): Array{
            return playerTexture;
        }

}

}