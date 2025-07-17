package com.github.asyncmc.mojang.authentication.flash.model {


    [XmlRootNode(name="Error")]
    public class Error {
                [XmlElement(name="error")]
        public var error: String = null;
                [XmlElement(name="errorMessage")]
        public var errorMessage: String = null;

    public function toString(): String {
        var str: String = "Error: ";
        str += " (error: " + error + ")";
        str += " (errorMessage: " + errorMessage + ")";
        return str;
    }

}

}