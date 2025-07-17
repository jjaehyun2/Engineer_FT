package kitaec.view.dish {
import kitaec.controls.comboboxes.AutoPopulatedValueComboBox;
import kitaec.view.*;

import kitaec.services.DishServices;
import kitaec.services.SupplierService;
import kitaec.view.dish.popup.AddDishPopUp;
import kitaec.vo.dish.DishVO;
import kitaec.vo.supplier.SupplierVO;

import mx.controls.Alert;

import mx.events.CloseEvent;
import mx.events.FlexEvent;
import mx.managers.PopUpManager;


import spark.components.DataGrid;
import spark.events.IndexChangeEvent;


public class DishesViewBase extends BaseView {
    public function DishesViewBase() {
    }

    public var dishesDg:DataGrid;
    public var supplierCb:AutoPopulatedValueComboBox;
    private var addDishPopUp:AddDishPopUp;



    override protected function onShow(event:FlexEvent):void {
        loadSuppliers();
    }

    protected function loadSuppliers():void {
        var supplierService:SupplierService = new SupplierService();
        supplierService.callBackFunction = getDishes;
        supplierService.getSupplierList();
    }

    private function getDishes():void
    {
        var dishService:DishServices = new DishServices();
        var supplierId:int =  (supplierCb.selectedItem as SupplierVO).supplierId;
        dishService.getDishes(supplierId);
    }

    protected function showAddDishPopup():void
    {
        if (!addDishPopUp)
        {
            addDishPopUp = new AddDishPopUp();
            addDishPopUp.addEventListener(CloseEvent.CLOSE, addDishBtnClose);
        }
        addDishPopUp.supplierId = supplierCb.selectedItem['supplierId'] as int;
        addDishPopUp.isSaveBtnEnabled = false;
        PopUpManager.addPopUp(addDishPopUp, this, true);
        PopUpManager.centerPopUp(addDishPopUp);
    }

    protected function addDishBtnClose(evt:CloseEvent):void
    {
        refresh();
        PopUpManager.removePopUp(addDishPopUp);
    }

    protected function refresh():void
    {
        loadSuppliers();
    }

    protected function onUpdateDish():void
    {
        if (!addDishPopUp)
        {
            addDishPopUp = new AddDishPopUp();

            addDishPopUp.addEventListener(CloseEvent.CLOSE, addDishBtnClose);
        }
        addDishPopUp.isSaveBtnEnabled = true;
        PopUpManager.addPopUp(addDishPopUp, this, true);
        PopUpManager.centerPopUp(addDishPopUp);
        addDishPopUp.supplierId = supplierCb.selectedItem['supplierId'] as int;
        addDishPopUp.currentDish = dishesDg.selectedItem as DishVO;
    }

    protected function onDeleteDish():void
    {
    }

    protected function onSupplierChange(event:IndexChangeEvent):void
    {
        getDishes();
    }
}
}