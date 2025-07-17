package org.openapitools.client.model {

import org.openapitools.client.model.PipelineImpllinks;

    [XmlRootNode(name="PipelineImpl")]
    public class PipelineImpl {
                [XmlElement(name="_class")]
        public var class: String = null;
                [XmlElement(name="displayName")]
        public var displayName: String = null;
                [XmlElement(name="estimatedDurationInMillis")]
        public var estimatedDurationInMillis: Number = 0;
                [XmlElement(name="fullName")]
        public var fullName: String = null;
                [XmlElement(name="latestRun")]
        public var latestRun: String = null;
                [XmlElement(name="name")]
        public var name: String = null;
                [XmlElement(name="organization")]
        public var organization: String = null;
                [XmlElement(name="weatherScore")]
        public var weatherScore: Number = 0;
                [XmlElement(name="_links")]
        public var links: PipelineImpllinks = NaN;

    public function toString(): String {
        var str: String = "PipelineImpl: ";
        str += " (class: " + class + ")";
        str += " (displayName: " + displayName + ")";
        str += " (estimatedDurationInMillis: " + estimatedDurationInMillis + ")";
        str += " (fullName: " + fullName + ")";
        str += " (latestRun: " + latestRun + ")";
        str += " (name: " + name + ")";
        str += " (organization: " + organization + ")";
        str += " (weatherScore: " + weatherScore + ")";
        str += " (links: " + links + ")";
        return str;
    }

}

}