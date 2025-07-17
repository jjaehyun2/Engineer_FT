package com.hurlant.math {
    import com.hurlant.math.*;

    class BarrettReduction implements IReduction {

        private var r2:BigInteger;
        private var q3:BigInteger;
        private var mu:BigInteger;
        private var m:BigInteger;

        public function BarrettReduction(_arg1:BigInteger){
            r2 = new BigInteger();
            q3 = new BigInteger();
            BigInteger.ONE.dlShiftTo((2 * _arg1.t), r2);
            mu = r2.divide(_arg1);
            this.m = _arg1;
        }
        public function reduce(_arg1:BigInteger):void{
            var _local2:BigInteger;
            _local2 = (_arg1 as BigInteger);
            _local2.drShiftTo((m.t - 1), r2);
            if (_local2.t > (m.t + 1)){
                _local2.t = (m.t + 1);
                _local2.clamp();
            };
            mu.multiplyUpperTo(r2, (m.t + 1), q3);
            m.multiplyLowerTo(q3, (m.t + 1), r2);
            while (_local2.compareTo(r2) < 0) {
                _local2.dAddOffset(1, (m.t + 1));
            };
            _local2.subTo(r2, _local2);
            while (_local2.compareTo(m) >= 0) {
                _local2.subTo(m, _local2);
            };
        }
        public function revert(_arg1:BigInteger):BigInteger{
            return (_arg1);
        }
        public function convert(_arg1:BigInteger):BigInteger{
            var _local2:BigInteger;
            if ((((_arg1.s < 0)) || ((_arg1.t > (2 * m.t))))){
                return (_arg1.mod(m));
            };
            if (_arg1.compareTo(m) < 0){
                return (_arg1);
            };
            _local2 = new BigInteger();
            _arg1.copyTo(_local2);
            reduce(_local2);
            return (_local2);
        }
        public function sqrTo(_arg1:BigInteger, _arg2:BigInteger):void{
            _arg1.squareTo(_arg2);
            reduce(_arg2);
        }
        public function mulTo(_arg1:BigInteger, _arg2:BigInteger, _arg3:BigInteger):void{
            _arg1.multiplyTo(_arg2, _arg3);
            reduce(_arg3);
        }

    }
}//package com.hurlant.math