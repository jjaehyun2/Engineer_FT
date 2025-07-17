package com.github.asyncmc.mojang.sessions.flash.model {

import com.github.asyncmc.mojang.sessions.flash.model.ByteArray;

    [XmlRootNode(name="PlayerProfileProperty")]
    public class PlayerProfileProperty {
        /* The property name */
        [XmlElement(name="name")]
        public var name: String = null;
        /* The serialized property value in base64. */
        [XmlElement(name="value")]
        public var value: ByteArray = null;
        /* signed data using Yggdrasil&#39;s private key */
        [XmlElement(name="signature")]
        public var signature: ByteArray = null;

    public function toString(): String {
        var str: String = "PlayerProfileProperty: ";
        str += " (name: " + name + ")";
        str += " (value: " + value + ")";
        str += " (signature: " + signature + ")";
        return str;
    }

}

}