package kitaec.view.dish.popup {

import kitaec.common.CommonConst;
import kitaec.view.BasePopup;
import kitaec.services.DishServices;
import kitaec.vo.dish.DishVO;

import mx.events.ValidationResultEvent;

import mx.validators.StringValidator;


import spark.components.ComboBox;
import spark.components.Image;
import spark.components.TextArea;
import spark.components.TextInput;

public class AddDishPopupBase extends BasePopup {

    public var titleTi:TextInput;
    public var descriptionTa:TextArea;
    public var img:Image;
    public var typeCmb:ComboBox;
    public var priceTi:TextInput;

    public var titleValidator:StringValidator;

    [Bindable]
    public var isSaveBtnEnabled:Boolean;

    private var srv:DishServices;

    [Bindable]
    private var _currentDish:DishVO;

    public var supplierId:int;

    public function AddDishPopupBase() {
    }


    public function set currentDish(dish:DishVO):void
    {
        if (dish)
        {
            _currentDish = dish;
            titleTi.text = dish.name;
            descriptionTa.text = dish.description;
            typeCmb.selectedIndex = dish.type;
            img.source = dish.picture;
            _currentDish.supplierId = dish.supplierId;
            priceTi.text = dish.defaultPrice.toString();
        }
    }

    public function get currentDish():DishVO
    {
        return _currentDish;
    }

    public function saveDish():void {
        srv = new DishServices();
        var dish:DishVO = new DishVO();
        dish.dishId = (currentDish) ? currentDish.dishId : null;
        dish.name = titleTi.text;
        dish.description = descriptionTa.text;
        dish.type = typeCmb.selectedIndex;
        dish.picture = img.source.toString();
        dish.supplierId = supplierId;
        dish.defaultPrice =  Number(priceTi.text);
        var actionStr:String =  (currentDish) ? CommonConst.UPDATE_DISH_ACTION : CommonConst.ADD_DISH_ACTION;
        srv.addEditDish(dish, actionStr);
    }

    protected function validate():void
    {
        if (titleValidator.validate(titleTi.text).type == ValidationResultEvent.VALID)
        {
            isSaveBtnEnabled = true;
        }
        else
        {
            isSaveBtnEnabled = false;
        }
    }

    override public function hide():void
    {
        currentDish = null;
        titleTi.text = "";
        descriptionTa.text = "";
        typeCmb.selectedIndex = 0;
        img.source = "";
        priceTi.text = "";
        super.hide();
    }


    override public function show(modal:Boolean = true):void {
        super.show(modal);

        /*var srv:OfferService = new OfferService();
        srv.getOfferList(1,0,0);*/
    }
}
}