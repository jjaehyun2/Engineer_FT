/**
 * GetAllAccountsResponse.as
 * This file was auto-generated from WSDL by the Apache Axis2 generator modified by Adobe
 * Any change made to this file will be overwritten when the code is re-generated.
 */
package com.macys.marketing.sema{
    import mx.utils.ObjectProxy;
    import mx.collections.ArrayCollection;
    import mx.collections.IList;
    import mx.collections.ICollectionView;
    import mx.rpc.soap.types.*;
    /**
     * Typed array collection
     */

    public class GetAllAccountsResponse extends ArrayCollection
    {
        /**
         * Constructor - initializes the array collection based on a source array
         */
        
        public function GetAllAccountsResponse(source:Array = null)
        {
            super(source);
        }
        
        
        public function addAccountResponseAt(item:AccountResponse,index:int):void {
            addItemAt(item,index);
        }
            
        public function addAccountResponse(item:AccountResponse):void {
            addItem(item);
        } 

        public function getAccountResponseAt(index:int):AccountResponse {
            return getItemAt(index) as AccountResponse;
        }
                
        public function getAccountResponseIndex(item:AccountResponse):int {
            return getItemIndex(item);
        }
                            
        public function setAccountResponseAt(item:AccountResponse,index:int):void {
            setItemAt(item,index);
        }

        public function asIList():IList {
            return this as IList;
        }
        
        public function asICollectionView():ICollectionView {
            return this as ICollectionView;
        }
    }
}