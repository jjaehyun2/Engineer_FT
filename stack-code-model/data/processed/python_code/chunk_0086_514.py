package org.openapitools.client.model {

import org.openapitools.client.model.PipelineRunartifacts;

    [XmlRootNode(name="PipelineRun")]
    public class PipelineRun {
                [XmlElement(name="_class")]
        public var class: String = null;
                // This declaration below of _artifacts_obj_class is to force flash compiler to include this class
        private var _artifacts_obj_class: Array = null;
        [XmlElementWrapper(name="artifacts")]
        [XmlElements(name="artifacts", type="Array")]
                public var artifacts: Array = new Array();
                [XmlElement(name="durationInMillis")]
        public var durationInMillis: Number = 0;
                [XmlElement(name="estimatedDurationInMillis")]
        public var estimatedDurationInMillis: Number = 0;
                [XmlElement(name="enQueueTime")]
        public var enQueueTime: String = null;
                [XmlElement(name="endTime")]
        public var endTime: String = null;
                [XmlElement(name="id")]
        public var id: String = null;
                [XmlElement(name="organization")]
        public var organization: String = null;
                [XmlElement(name="pipeline")]
        public var pipeline: String = null;
                [XmlElement(name="result")]
        public var result: String = null;
                [XmlElement(name="runSummary")]
        public var runSummary: String = null;
                [XmlElement(name="startTime")]
        public var startTime: String = null;
                [XmlElement(name="state")]
        public var state: String = null;
                [XmlElement(name="type")]
        public var type: String = null;
                [XmlElement(name="commitId")]
        public var commitId: String = null;

    public function toString(): String {
        var str: String = "PipelineRun: ";
        str += " (class: " + class + ")";
        str += " (artifacts: " + artifacts + ")";
        str += " (durationInMillis: " + durationInMillis + ")";
        str += " (estimatedDurationInMillis: " + estimatedDurationInMillis + ")";
        str += " (enQueueTime: " + enQueueTime + ")";
        str += " (endTime: " + endTime + ")";
        str += " (id: " + id + ")";
        str += " (organization: " + organization + ")";
        str += " (pipeline: " + pipeline + ")";
        str += " (result: " + result + ")";
        str += " (runSummary: " + runSummary + ")";
        str += " (startTime: " + startTime + ")";
        str += " (state: " + state + ")";
        str += " (type: " + type + ")";
        str += " (commitId: " + commitId + ")";
        return str;
    }

}

}