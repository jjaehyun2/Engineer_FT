package com.github.asyncmc.mojang.api.flash.model {

import org.openapitools.common.ListWrapper;
import com.github.asyncmc.mojang.api.flash.model.OrderStatistic;

    public class OrderStatisticsRequestList implements ListWrapper {
        // This declaration below of _OrderStatisticsRequest_obj_class is to force flash compiler to include this class
        private var _orderStatisticsRequest_obj_class: com.github.asyncmc.mojang.api.flash.model.OrderStatisticsRequest = null;
        [XmlElements(name="orderStatisticsRequest", type="com.github.asyncmc.mojang.api.flash.model.OrderStatisticsRequest")]
        public var orderStatisticsRequest: Array = new Array();

        public function getList(): Array{
            return orderStatisticsRequest;
        }

}

}