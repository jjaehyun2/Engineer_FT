package com.github.mortido.sqcity.ui.gamefield
{
    import as3isolib.display.IsoView;

    public class BaseFieldState implements FieldState
    {
        private var _field:GameField;
        private var _view:IsoView;

        protected function get field():GameField
        {
            return _field;
        }

        protected function get view():IsoView
        {
            return _view;
        }

        public function setup(cityField:GameField):void
        {
            _field = cityField;
            _view = _field.view;
        }

        public function release():void
        {
            _field = null;
            _view = null;
        }
    }
}