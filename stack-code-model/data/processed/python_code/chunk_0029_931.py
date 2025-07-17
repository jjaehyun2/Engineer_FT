package com.github.mortido.sqcity.models
{
    public class Building
    {
        public static const NO_ID:int = -1;

        public function Building(x:int, y:int, buildingType:BuildingType, id:int = NO_ID, currentProduction:Production = null, productionFinishTime:Date = null)
        {
            _x = x;
            _y = y;
            _id = id;
            _type = buildingType;
            _currentProduction = currentProduction;
            _productionFinishTime = productionFinishTime;
        }

        private var _x:int;
        private var _y:int;
        private var _id:int;
        private var _type:BuildingType;
        private var _currentProduction:Production;
        private var _productionFinishTime:Date;

        public function set x(value:int):void
        {
            _x = value;
        }

        public function set y(value:int):void
        {
            _y = value;
        }

        public function get x():int
        {
            return _x;
        }

        public function get y():int
        {
            return _y;
        }

        public function get id():int
        {
            return _id;
        }

        public function get type():BuildingType
        {
            return _type;
        }

        public function get currentProduction():Production
        {
            return _currentProduction;
        }

        public function set currentProduction(value:Production):void
        {
            _currentProduction = value;
        }

        public function get productionFinishTime():Date
        {
            return _productionFinishTime;
        }

        public function set productionFinishTime(value:Date):void
        {
            _productionFinishTime = value;
        }
    }
}