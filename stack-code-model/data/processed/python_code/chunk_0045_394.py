/**
 * Created by ricardo_neves at bytesfromouterspace.com on 28/02/2015.
 */
package com.bytesfromouterspace.stockbrokers.controller {
    import com.bytesfromouterspace.stockbrokers.event.BonusEvent;
    import com.bytesfromouterspace.stockbrokers.event.GameEvent;
    import com.bytesfromouterspace.stockbrokers.event.ReputationStatusEvent;
    import com.bytesfromouterspace.stockbrokers.model.TurnModel;

    import flash.events.TimerEvent;

    import flash.utils.Timer;

    public class TurnControler {

        private var _model:TurnModel;
        private var _tmr:Timer;
        private var _tickDuration:Number = 0.1;

        public function TurnControler(model:TurnModel) {
            this._model = model;
            _tmr = new Timer(_tickDuration * 1000);
            _tmr.addEventListener(TimerEvent.TIMER, onTick);
            model.addEventListener(GameEvent.GAME_OVER, onGameOver);
        }

        private function onGameOver(event:GameEvent):void {
            if(_tmr) {
                _tmr.reset();
            }
        }

        private function onTick(event:TimerEvent):void {
            _model.decrease(_tickDuration);
        }

        public function start():void {
            _model.startTurn();
            _tmr.start();
        }

        public function handleLevelUp(event:ReputationStatusEvent):void {
            _model.resets++;
        }

        public function handleBonus(event:BonusEvent):void {
            _model.bonus(event.bonusCategory);
        }

        public function resetTimer():void {
            _model.doReset();
        }

        public function resume():void {
            _tmr.start();
        }

        public function pause():void {
            _tmr.stop();
        }
    }
}