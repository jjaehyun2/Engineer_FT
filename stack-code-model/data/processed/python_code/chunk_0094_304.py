package com.github.asyncmc.mojang.sessions.flash.model {


    [XmlRootNode(name="PlayerSkinMetadata")]
    public class PlayerSkinMetadata {
        /* The player model, currently only \&quot;slim\&quot; (Alex) is valid, for Steve&#39;s model this property must be absent. */
        [XmlElement(name="model")]
        public var model: String = null;

    public function toString(): String {
        var str: String = "PlayerSkinMetadata: ";
        str += " (model: " + model + ")";
        return str;
    }

}

}