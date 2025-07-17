package kitaec.services {
import flash.events.Event;

import kitaec.common.CommonConst;
import kitaec.common.ObjectUtil;
import kitaec.controller.event.NotifyEvent;
import kitaec.vo.order.OrderOfferInfoVO;
import kitaec.vo.order.OrderVO;

import mx.collections.ArrayCollection;

public class OrderService extends BaseService {

    // GET ORDER LIST
    public function getOrderList(supplierId:int, locationId:int, date:Number, time:int):void {
        this.url = CommonConst.ORDER_SERVICE;
        this.request = { action:"get_order_list",
                            supplier_id: supplierId,
                            location_id: locationId,
                            date: date,
                            time: time };
        this.addEventListener(BaseService.SUCCESS_EVENT, onGetOrderListResult);
        this.send();
    }

    private function onGetOrderListResult(event:Event):void {
        if (result.status == RESPONSE_STATUS_OK) {
            model.orderList = ObjectUtil.convertResultList(new ArrayCollection(result.data), OrderVO);
            if(model.orderList.length == 0) {
                controller.dispatchEvent(new NotifyEvent("ничего не найдено"));
            }
        }
    }

    // GET OFFER LIST
    public function getOfferList(orderId:int):void {
        this.url = CommonConst.ORDER_SERVICE;
        this.request = { action:"get_offer_list_by_order_id", order_id: orderId };
        this.addEventListener(BaseService.SUCCESS_EVENT, onGetOfferListByOrderIdResult);
        this.send();
    }

    private function onGetOfferListByOrderIdResult(event:Event):void {
        if (result.status == RESPONSE_STATUS_OK) {
            model.orderOfferList = ObjectUtil.convertResultList(new ArrayCollection(result.data), OrderOfferInfoVO);
            callBack();
        }
    }

    // CREATE ORDER
    public function createOrder(order:OrderVO, offerList:ArrayCollection):void {
        var orderForCreate:Object = ObjectUtil.convertRequestObject(order, {"offer_list":  ObjectUtil.convertRequestList(offerList)});
        this.url = CommonConst.ORDER_SERVICE;
        this.request = { action:"create_order", order:JSON.stringify(orderForCreate)};
        this.addEventListener(BaseService.SUCCESS_EVENT, createOrderResult);
        this.send();
    }

    private function createOrderResult(event:Event):void {
        if (result.status == RESPONSE_STATUS_OK) {
            model.orderForEdit.orderId = int(result.data);
            controller.dispatchEvent(new NotifyEvent("Заказ создан"));
            callBack();
        } else if (result.status == RESPONSE_STATUS_ERROR){
            controller.dispatchEvent(new NotifyEvent(result.msg, NotifyEvent.TYPE_ERROR));
        }
    }

    // UPDATE ORDER
    public function updateOrder(order:OrderVO, offerList:ArrayCollection):void {
        var orderForUpdate:Object = ObjectUtil.convertRequestObject(order, {"offer_list":  ObjectUtil.convertRequestList(offerList)});
        this.url = CommonConst.ORDER_SERVICE;
        this.request = { action:"update_order", order:JSON.stringify(orderForUpdate)};
        this.addEventListener(BaseService.SUCCESS_EVENT, updateOrderResult);
        this.send();
    }

    private function updateOrderResult(event:Event):void {
        if (result.status == RESPONSE_STATUS_OK) {
            controller.dispatchEvent(new NotifyEvent("Заказ обновлён"));
            callBack();
        } else if (result.status == RESPONSE_STATUS_ERROR){
            controller.dispatchEvent(new NotifyEvent(result.msg, NotifyEvent.TYPE_ERROR));
        }
    }
}
}