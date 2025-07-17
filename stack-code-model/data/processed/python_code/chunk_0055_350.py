package com.github.asyncmc.mojang.api.flash.model {


    [XmlRootNode(name="OrderStatisticsResponse")]
    public class OrderStatisticsResponse {
        /* total amount sold */
        [XmlElement(name="total")]
        public var total: Number = 0;
        /* total sold in last 24 hours */
        [XmlElement(name="last24h")]
        public var last24h: Number = 0;
        /* decimal average sales per second */
        [XmlElement(name="saleVelocityPerSeconds")]
        public var saleVelocityPerSeconds: Number = 0.0;

    public function toString(): String {
        var str: String = "OrderStatisticsResponse: ";
        str += " (total: " + total + ")";
        str += " (last24h: " + last24h + ")";
        str += " (saleVelocityPerSeconds: " + saleVelocityPerSeconds + ")";
        return str;
    }

}

}