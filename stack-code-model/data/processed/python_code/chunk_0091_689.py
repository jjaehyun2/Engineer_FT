package com.github.asyncmc.mojang.api.flash.model {


    [XmlRootNode(name="CurrentPlayerIDs")]
    public class CurrentPlayerIDs {
        /* The player UUID without hyphens */
        [XmlElement(name="id")]
        public var id: String = null;
        /* The current name being used by this player */
        [XmlElement(name="name")]
        public var name: String = null;
        /* If account has not been converted */
        [XmlElement(name="legacy")]
        public var legacy: Boolean = false;
        /* If the player has not puchased the game */
        [XmlElement(name="demo")]
        public var demo: Boolean = false;

    public function toString(): String {
        var str: String = "CurrentPlayerIDs: ";
        str += " (id: " + id + ")";
        str += " (name: " + name + ")";
        str += " (legacy: " + legacy + ")";
        str += " (demo: " + demo + ")";
        return str;
    }

}

}