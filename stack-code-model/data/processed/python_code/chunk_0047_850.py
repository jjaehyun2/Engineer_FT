package com.github.asyncmc.mojang.authentication.flash.model {


    [XmlRootNode(name="UsernamePassword")]
    public class UsernamePassword {
        /* The Mojang account e-mail or username. Never store it. */
        [XmlElement(name="username")]
        public var username: String = null;
        /* The Mojang account password, never store it. */
        [XmlElement(name="password")]
        public var password: String = null;

    public function toString(): String {
        var str: String = "UsernamePassword: ";
        str += " (username: " + username + ")";
        str += " (password: " + password + ")";
        return str;
    }

}

}