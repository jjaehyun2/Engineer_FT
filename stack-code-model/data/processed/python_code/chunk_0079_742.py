package org.openapitools.client.model {

import org.openapitools.common.ListWrapper;

    public class OrderCancelAllRequestList implements ListWrapper {
        // This declaration below of _OrderCancelAllRequest_obj_class is to force flash compiler to include this class
        private var _orderCancelAllRequest_obj_class: org.openapitools.client.model.OrderCancelAllRequest = null;
        [XmlElements(name="orderCancelAllRequest", type="org.openapitools.client.model.OrderCancelAllRequest")]
        public var orderCancelAllRequest: Array = new Array();

        public function getList(): Array{
            return orderCancelAllRequest;
        }

}

}