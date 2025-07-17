package com.github.asyncmc.mojang.api.flash.model {

import com.github.asyncmc.mojang.api.flash.model.SecurityAnswerId;
import com.github.asyncmc.mojang.api.flash.model.SecurityQuestion;

    [XmlRootNode(name="SecurityChallenge")]
    public class SecurityChallenge {
                [XmlElement(name="question")]
        public var question: SecurityQuestion = NaN;
                [XmlElement(name="answer")]
        public var answer: SecurityAnswerId = NaN;

    public function toString(): String {
        var str: String = "SecurityChallenge: ";
        str += " (question: " + question + ")";
        str += " (answer: " + answer + ")";
        return str;
    }

}

}