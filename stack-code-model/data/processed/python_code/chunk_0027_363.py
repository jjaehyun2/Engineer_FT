package com.github.asyncmc.mojang.sessions.flash.model {


    [XmlRootNode(name="PlayerTextureURL")]
    public class PlayerTextureURL {
        /* The URL to the texture, must be in Mojang&#39;s domains. */
        [XmlElement(name="url")]
        public var url: String = null;

    public function toString(): String {
        var str: String = "PlayerTextureURL: ";
        str += " (url: " + url + ")";
        return str;
    }

}

}