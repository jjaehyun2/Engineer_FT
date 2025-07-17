package com.github.asyncmc.mojang.authentication.flash.model {


    [XmlRootNode(name="GameProfile")]
    public class GameProfile {
                [XmlElement(name="agent")]
        public var agent: String = null;
                [XmlElement(name="id")]
        public var id: String = null;
                [XmlElement(name="name")]
        public var name: String = null;
                [XmlElement(name="userId")]
        public var userId: String = null;
        /* Unix timestamp in milliseconds */
        [XmlElement(name="createdAt")]
        public var createdAt: Number = 0;
                [XmlElement(name="legacyProfile")]
        public var legacyProfile: Boolean = false;
                [XmlElement(name="suspended")]
        public var suspended: Boolean = false;
                [XmlElement(name="paid")]
        public var paid: Boolean = false;
                [XmlElement(name="migrated")]
        public var migrated: Boolean = false;
                [XmlElement(name="legacy")]
        public var legacy: Boolean = false;

    public function toString(): String {
        var str: String = "GameProfile: ";
        str += " (agent: " + agent + ")";
        str += " (id: " + id + ")";
        str += " (name: " + name + ")";
        str += " (userId: " + userId + ")";
        str += " (createdAt: " + createdAt + ")";
        str += " (legacyProfile: " + legacyProfile + ")";
        str += " (suspended: " + suspended + ")";
        str += " (paid: " + paid + ")";
        str += " (migrated: " + migrated + ")";
        str += " (legacy: " + legacy + ")";
        return str;
    }

}

}