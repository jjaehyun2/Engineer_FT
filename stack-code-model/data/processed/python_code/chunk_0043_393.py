package kitaec.services {
import flash.events.Event;

import kitaec.common.CommonConst;
import kitaec.common.ObjectUtil;
import kitaec.vo.DateVO;
import kitaec.vo.offer.OfferTimeVO;
import kitaec.vo.offer.OfferVO;

import mx.collections.ArrayCollection;

public class OfferService extends BaseService {

    public static const GET_OFFER_LIST_ACTION:String = "get_offer_list";
    public static const GET_OFFER_DAY_LIST_ACTION:String = "get_offer_day_list";
    public static const GET_OFFER_TIME_LIST_ACTION:String = "get_offer_time_list";

    // GET OFFER LIST
    public function getOfferList(supplierId:int, locationId:int, date:Number, time:int):void {
        this.url = CommonConst.OFFER_SERVICE ;
        this.request = { action:GET_OFFER_LIST_ACTION,
                            supplier_id: supplierId,
                            location_id: locationId,
                            date: date,
                            time: time };
        this.addEventListener(BaseService.SUCCESS_EVENT, onGetOfferListResult);
        this.send();
    }

    private function onGetOfferListResult(event:Event):void {
        if (result.status == RESPONSE_STATUS_OK) {
            model.offerList = ObjectUtil.convertResultList(new ArrayCollection(result.data), OfferVO);
        }
    }

    // GET OFFER DAY LIST
    public function getOfferDayList(supplierId:int, locationId:int):void {
        this.url = CommonConst.OFFER_SERVICE ;
        this.request = { action:GET_OFFER_DAY_LIST_ACTION, supplier_id: supplierId, location_id: locationId };
        this.addEventListener(BaseService.SUCCESS_EVENT, onGetOfferDayListResult);
        this.send();
    }

    private function onGetOfferDayListResult(event:Event):void {
        if (result.status == RESPONSE_STATUS_OK) {
            model.offerDateList = ObjectUtil.convertResultList(new ArrayCollection(result.data), DateVO);
            callBack();
        }
        /*model.offerDayList = [
            {rangeEnd:new Date(1397088000000), rangeStart:new Date(1397088000000)},
            {rangeEnd:new Date(1397174400000), rangeStart:new Date(1397174400000)},
            {rangeEnd:new Date(1397433600000), rangeStart:new Date(1397433600000)}
        ];*///ObjectUtil.convertList(new ArrayCollection(result.result ), OfferVO);
    }


    // GET OFFER TIME LIST
    public function getOfferTimeList(supplierId:int, locationId:int, selectedDate:Number):void {
        this.url = CommonConst.OFFER_SERVICE ;
        this.request = { action:GET_OFFER_TIME_LIST_ACTION, supplier_id: supplierId, location_id: locationId, date:selectedDate };
        this.addEventListener(BaseService.SUCCESS_EVENT, onGetOfferTimeListResult);
        this.send();
    }

    private function onGetOfferTimeListResult(event:Event):void {
        if(result.status == RESPONSE_STATUS_OK) {
            model.offerTimeList = ObjectUtil.convertResultList(new ArrayCollection(result.data), OfferTimeVO);
            callBack();
        }
    }
}
}