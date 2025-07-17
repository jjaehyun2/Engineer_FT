package org.openapitools.client.model {


    [XmlRootNode(name="PipelineActivityartifacts")]
    public class PipelineActivityartifacts {
                [XmlElement(name="name")]
        public var name: String = null;
                [XmlElement(name="size")]
        public var size: Number = 0;
                [XmlElement(name="url")]
        public var url: String = null;
                [XmlElement(name="_class")]
        public var class: String = null;

    public function toString(): String {
        var str: String = "PipelineActivityartifacts: ";
        str += " (name: " + name + ")";
        str += " (size: " + size + ")";
        str += " (url: " + url + ")";
        str += " (class: " + class + ")";
        return str;
    }

}

}