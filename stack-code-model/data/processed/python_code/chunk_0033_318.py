package org.openapitools.client.model {

import org.openapitools.common.ListWrapper;
import org.openapitools.client.model.BalanceData;

    public class BalanceList implements ListWrapper {
        // This declaration below of _Balance_obj_class is to force flash compiler to include this class
        private var _balance_obj_class: org.openapitools.client.model.Balance = null;
        [XmlElements(name="balance", type="org.openapitools.client.model.Balance")]
        public var balance: Array = new Array();

        public function getList(): Array{
            return balance;
        }

}

}