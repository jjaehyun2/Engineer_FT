package org.openapitools.client.model {

import org.openapitools.client.model.PositionData;

    [XmlRootNode(name="Position")]
    public class Position {
        /* Exchange identifier used to identify the routing destination. */
        [XmlElement(name="exchange_id")]
        public var exchangeId: String = null;
                // This declaration below of _data_obj_class is to force flash compiler to include this class
        private var _data_obj_class: Array = null;
        [XmlElementWrapper(name="data")]
        [XmlElements(name="data", type="Array")]
                public var data: Array = new Array();

    public function toString(): String {
        var str: String = "Position: ";
        str += " (exchangeId: " + exchangeId + ")";
        str += " (data: " + data + ")";
        return str;
    }

}

}