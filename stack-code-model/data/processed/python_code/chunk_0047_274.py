/**
 * ReplicateAdCopyList.as
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

    public class ReplicateAdCopyList extends ArrayCollection
    {
        /**
         * Constructor - initializes the array collection based on a source array
         */
        
        public function ReplicateAdCopyList(source:Array = null)
        {
            super(source);
        }
        
        
        public function addReplicateEntityAt(item:ReplicateEntity,index:int):void {
            addItemAt(item,index);
        }
            
        public function addReplicateEntity(item:ReplicateEntity):void {
            addItem(item);
        } 

        public function getReplicateEntityAt(index:int):ReplicateEntity {
            return getItemAt(index) as ReplicateEntity;
        }
                
        public function getReplicateEntityIndex(item:ReplicateEntity):int {
            return getItemIndex(item);
        }
                            
        public function setReplicateEntityAt(item:ReplicateEntity,index:int):void {
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