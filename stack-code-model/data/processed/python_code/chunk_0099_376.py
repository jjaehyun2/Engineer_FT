package org.openapitools.client.model {

import org.openapitools.common.ListWrapper;
import org.openapitools.client.model.OrdSide;
import org.openapitools.client.model.OrdType;
import org.openapitools.client.model.TimeInForce;

    public class OrderNewSingleRequestList implements ListWrapper {
        // This declaration below of _OrderNewSingleRequest_obj_class is to force flash compiler to include this class
        private var _orderNewSingleRequest_obj_class: org.openapitools.client.model.OrderNewSingleRequest = null;
        [XmlElements(name="orderNewSingleRequest", type="org.openapitools.client.model.OrderNewSingleRequest")]
        public var orderNewSingleRequest: Array = new Array();

        public function getList(): Array{
            return orderNewSingleRequest;
        }

}

}