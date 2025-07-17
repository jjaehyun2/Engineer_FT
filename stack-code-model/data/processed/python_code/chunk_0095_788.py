package org.openapitools.client.model {

import org.openapitools.common.ListWrapper;
import org.openapitools.client.model.Fills;
import org.openapitools.client.model.OrdStatus;

    public class OrderExecutionReportAllOfList implements ListWrapper {
        // This declaration below of _OrderExecutionReport_allOf_obj_class is to force flash compiler to include this class
        private var _orderExecutionReportAllOf_obj_class: org.openapitools.client.model.OrderExecutionReportAllOf = null;
        [XmlElements(name="orderExecutionReportAllOf", type="org.openapitools.client.model.OrderExecutionReportAllOf")]
        public var orderExecutionReportAllOf: Array = new Array();

        public function getList(): Array{
            return orderExecutionReportAllOf;
        }

}

}