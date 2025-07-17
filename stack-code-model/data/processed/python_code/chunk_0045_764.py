/**
 * Created by ricardo_neves at bytesfromouterspace.com on 28/02/2015.
 */
package com.bytesfromouterspace.stockbrokers.controller {
    import com.bytesfromouterspace.stockbrokers.model.StockShareModel;

    public class StockShareController {

        private var model:StockShareModel;

        public function StockShareController(model:StockShareModel) {
            this.model = model;
        }

        public function influence(value:Number):void {
            model.setMarketInfluence(value);
        }

        public function sellToMarket(quantity:int):void {
            model.requestSell(quantity);
        }

        public function buyFromMarket(quantity:int):void {
            model.requestBuy(quantity);
        }

        public function requestFocus():void {
            
        }
    }
}