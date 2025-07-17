package org.openapitools.client.model {

import org.openapitools.common.ListWrapper;

    public class TimeInForceList implements ListWrapper {
        // This declaration below of _TimeInForce_obj_class is to force flash compiler to include this class
        private var _timeInForce_obj_class: org.openapitools.client.model.TimeInForce = null;
        [XmlElements(name="timeInForce", type="org.openapitools.client.model.TimeInForce")]
        public var timeInForce: Array = new Array();

        public function getList(): Array{
            return timeInForce;
        }

}

}