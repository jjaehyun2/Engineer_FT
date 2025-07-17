package kitaec.services {

import flash.events.Event;

import kitaec.common.CommonConst;
import kitaec.common.ObjectUtil;
import kitaec.vo.supplier.SupplierVO;

import mx.collections.ArrayCollection;

public class SupplierService extends BaseService {

    // GET SUPPLIER LIST
    public function getSupplierList():void {
        this.url = CommonConst.SUPPLIER_SERVICE ;
        this.request = { action:"get_supplier_list" };
        this.addEventListener(BaseService.SUCCESS_EVENT, onGetSupplierListResult);
        this.send();
    }

    private function onGetSupplierListResult(event:Event):void {
        if (result.status == RESPONSE_STATUS_OK) {
            model.suppliers = ObjectUtil.convertResultList(new ArrayCollection(result.data), SupplierVO);
            callBack();
        }
    }


}
}