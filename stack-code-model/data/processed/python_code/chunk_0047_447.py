/**
 * Created by ricardo_neves at bytesfromouterspace.com on 28/02/2015.
 */
package com.bytesfromouterspace.stockbrokers.model {

    import com.bytesfromouterspace.stockbrokers.event.StockShareEvent;
    import com.bytesfromouterspace.stockbrokers.event.TransactionEvent;

    import flash.events.Event;

    [Event(name="stockShareChanged", type="com.bytesfromouterspace.stockbrokers.event.StockShareEvent")]
    public class StockShareModel extends BaseModel implements IHistoryModel {

        private var _history:Vector.<Number>;
        public var stockId:int = 0;
        public var startingValue:Number;
        private var _currentValue:Number;
        public var samples:int;
        private var lastSample:Number = 0;
        private var _name:String;
        private var _quantityAvailable:int = 0;
        private var _quantityOwned:int = 0;
        private var _ownedValue:Number = 0;
        private var _delta:Number = 0;
        public var marketModifier:Number = 0;
        private var _totalQuantity:Number = 0;
        private var _focus:Boolean = false;
        private var _locked:Boolean = false;
        private var _generatorInfluenceRatio:Number;
        private var _transactionInfluenceRatio:Number;
        private var _basePriceRatio:Number;

        public function StockShareModel(stockId:int, name:String, rand:Number, generatorInfluenceRatio:Number, transactionInfluenceRatio:Number) {
            super();
            this.stockId = stockId;
            this._name = name;
            this._totalQuantity = generateInitialQuantity();
            this._quantityAvailable = _totalQuantity;
            this.startingValue = int(rand * 100);
            this._generatorInfluenceRatio = generatorInfluenceRatio;
            this._transactionInfluenceRatio = transactionInfluenceRatio;
            this._basePriceRatio = 1 - (generatorInfluenceRatio + transactionInfluenceRatio);
            samples = 0;
            _currentValue = startingValue;
            lastSample = _currentValue;
            _history = new Vector.<Number>();
            _history.push(startingValue);
        }

        private function generateInitialQuantity():int {
            var qtd:int = Math.random() * 3500 + 1000;
            while((qtd % 10) != 0){
                qtd--;
            }
            return qtd;
        }

        public function refresh():void {
            dispatchEvent(new StockShareEvent(StockShareEvent.STOCK_SHARE_CHANGED));
        }

        public function get quantityAvailable():int {
            return _quantityAvailable;
        }

        public function set quantityAvailable(value:int):void {
            _quantityAvailable = value;
            refresh();
        }

        public function get quantityOwned():int {
            return _quantityOwned;
        }

        public function set quantityOwned(value:int):void {
            _quantityOwned = value;
            refresh();
        }

        public function get ownedValue():Number {
            return _ownedValue;
        }

        public function get currentOwnedValue():Number {
            return _quantityOwned * _currentValue;
        }

        public function set ownedValue(value:Number):void {
            _ownedValue = value;
            refresh();
        }

        public function requestSell(quantity:int):void {
            dispatchEvent(new TransactionEvent(stockId, TransactionEvent.TRANSACTION_TYPE_SELL, quantity));
        }

        public function requestBuy(quantity:int):void {
            dispatchEvent(new TransactionEvent(stockId, TransactionEvent.TRANSACTION_TYPE_BUY, quantity));
        }

        public function doBuy(amount:int):void {
            _quantityAvailable -= amount;
            if(_quantityOwned > 0) {
                _ownedValue = (_quantityOwned * _ownedValue + amount * _currentValue) / (_quantityOwned + amount);
            } else {
                _ownedValue = _currentValue;
            }
            _quantityOwned += amount;
            marketModifier += amount / _totalQuantity;
            refresh();
        }

        public function doSell(amount:int):void {
            _quantityAvailable += amount;
            _quantityOwned -= amount;
            refresh();
        }

        public function get marketValue():Number {
            return _currentValue * _totalQuantity;
        }

        public function setMarketInfluence(influence:Number):void {
            var randMod:int = Math.random() > 0.6 ? 1 : -1;
            var lastValue:Number = _history[_history.length - 1];
            var base:Number = lastValue; // * _basePriceRatio;
            var trans:Number = lastValue * _transactionInfluenceRatio * marketModifier * randMod;
            var inf:Number = lastValue * _generatorInfluenceRatio * influence * randMod;
            var newPrice:Number = centRound(base + trans + inf);
            if(marketModifier > 0) {
                marketModifier = marketModifier - 0.1 > 0 ? marketModifier - 0.1 : 0;
            }
            _delta = ((newPrice - lastValue) / lastValue)*100;
            if(stockId == -1) {
                var fields:Array;
                if(_history.length == 1) {
                    fields = ["Turn", "Start", "last", "base", "trans", "inf", "gen", "delta"];
                    trace("|" + fields.join("\t|") + "\t|");
                }
                fields = [_history.length, startingValue.toFixed(2), lastValue.toFixed(2), base.toFixed(2),
                    trans.toFixed(2), inf.toFixed(2), influence.toFixed(2), _delta.toFixed(2)];
                trace("|" + fields.join("\t|") + "\t|");
            }
            //trace(newPrice,"\t",centRound(newPrice));

            currentValue = newPrice;
        }

        private function centRound(num:Number):Number {
            return int(num*100)/100;
        }

        public function get currentValue():Number {
            return _currentValue;
        }

        public function set currentValue(value:Number):void {
            _currentValue = value;
            _locked = (_currentValue < (0.1 * startingValue));
            refresh();
            addToHistory(value);
        }

        public function get locked():Boolean {
            return _locked;
        }

        public function get delta():Number {
            return _delta;
        }

        public function get history():Vector.<Number> {
            return _history;
        }

        public function dispatchHistoryChange():void {
            if(_focus) {
                dispatchEvent(new Event(Event.CHANGE));
            }
        }

        public function set focus(value:Boolean):void {
            _focus = value;
        }

        public function get name():String {
            return _name;
        }

        public function addToHistory(value:Number):void {
            _history.push(value);
            dispatchHistoryChange();
        }
    }
}