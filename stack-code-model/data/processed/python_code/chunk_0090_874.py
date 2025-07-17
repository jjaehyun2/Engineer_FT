package org.openapitools.client.model {


    [XmlRootNode(name="BalanceData")]
    public class BalanceData {
        /* Exchange currency code. */
        [XmlElement(name="asset_id_exchange")]
        public var assetIdExchange: String = null;
        /* CoinAPI currency code. */
        [XmlElement(name="asset_id_coinapi")]
        public var assetIdCoinapi: String = null;
        /* Value of the current total currency balance on the exchange. */
        [XmlElement(name="balance")]
        public var balance: Number = 0.0;
        /* Value of the current available currency balance on the exchange that can be used as collateral. */
        [XmlElement(name="available")]
        public var available: Number = 0.0;
        /* Value of the current locked currency balance by the exchange. */
        [XmlElement(name="locked")]
        public var locked: Number = 0.0;
        /* Source of the last modification.  */
        [XmlElement(name="last_updated_by")]
        public var lastUpdatedBy: String = null;
        /* Current exchange rate to the USD for the single unit of the currency.  */
        [XmlElement(name="rate_usd")]
        public var rateUsd: Number = 0.0;
        /* Value of the current total traded. */
        [XmlElement(name="traded")]
        public var traded: Number = 0.0;

    public function toString(): String {
        var str: String = "BalanceData: ";
        str += " (assetIdExchange: " + assetIdExchange + ")";
        str += " (assetIdCoinapi: " + assetIdCoinapi + ")";
        str += " (balance: " + balance + ")";
        str += " (available: " + available + ")";
        str += " (locked: " + locked + ")";
        str += " (lastUpdatedBy: " + lastUpdatedBy + ")";
        str += " (rateUsd: " + rateUsd + ")";
        str += " (traded: " + traded + ")";
        return str;
    }

}

}