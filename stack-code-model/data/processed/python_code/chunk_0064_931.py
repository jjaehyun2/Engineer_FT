package org.openapitools.client.model {

import org.openapitools.client.model.KeystoreItems;

    [XmlRootNode(name="KeystoreInfo")]
    public class KeystoreInfo {
                // This declaration below of _aliases_obj_class is to force flash compiler to include this class
        private var _aliases_obj_class: Array = null;
        [XmlElementWrapper(name="aliases")]
        [XmlElements(name="aliases", type="Array")]
                public var aliases: Array = new Array();
        /* False if truststore don&#39;t exist */
        [XmlElement(name="exists")]
        public var exists: Boolean = false;

    public function toString(): String {
        var str: String = "KeystoreInfo: ";
        str += " (aliases: " + aliases + ")";
        str += " (exists: " + exists + ")";
        return str;
    }

}

}