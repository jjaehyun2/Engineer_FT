package kitaec.services {

import flash.events.Event;

import kitaec.common.CommonConst;
import kitaec.common.ObjectUtil;

import kitaec.model.Model;
import kitaec.vo.dish.DishVO;

import mx.collections.ArrayCollection;

import mx.controls.Alert;

import mx.rpc.events.FaultEvent;

import mx.rpc.events.ResultEvent;

import mx.rpc.http.HTTPService;
import mx.utils.ArrayUtil;

public class DishServices extends BaseService {

    public function getDishes(supplierId:int):void
    {
        this.url = CommonConst.DISH_SERVICE;
        this.addEventListener(BaseService.SUCCESS_EVENT, getDishesResult);
        var obj:Object = new Object();
        obj["supplier_id"] = supplierId;
        obj["action"] = "get_dish_list";
        this.request = obj;
        this.send();
    }

    public function addEditDish(dish:DishVO, actionStr:String):void {
        this.url = CommonConst.DISH_SERVICE;
        var dishJson:String = JSON.stringify(ObjectUtil.convertRequestObject(dish));//JSON.stringify(dish);
        this.request = { action:actionStr, dish: dishJson };
        //Alert.show(dishJson + " отправил - смотри изменения в таблице");
        this.addEventListener(BaseService.SUCCESS_EVENT, addDishResult);
        this.send();
    }

    private function getDishesResult(event:Event):void
    {
        if (result.status == RESPONSE_STATUS_OK)
        {
            model.dishes = ObjectUtil.convertResultList(new ArrayCollection(ArrayUtil.toArray(result.data)), DishVO);
        }
        else
        {
            happenedSomethingWrong(result.result);
        }
    }

    private function addDishResult(event:Event):void
    {
        if (result.status == RESPONSE_STATUS_OK)
        {

            //model.dishes = ObjectUtil.convertList(new ArrayCollection(ArrayUtil.toArray(result.data)), DishVO);
        }
        else
        {
            happenedSomethingWrong(result.result);
        }
    }



    private function happenedSomethingWrong(faultMessage:String):void
    {
         Alert.show(faultMessage);
    }
}
}