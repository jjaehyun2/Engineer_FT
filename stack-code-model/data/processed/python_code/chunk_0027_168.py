package com.hurlant.math {
    import com.hurlant.math.*;

    class MontgomeryReduction implements IReduction {

        private var um:int;
        private var mp:int;
        private var mph:int;
        private var mpl:int;
        private var mt2:int;
        private var m:BigInteger;

        public function MontgomeryReduction(_arg1:BigInteger){
            this.m = _arg1;
            mp = _arg1.invDigit();
            mpl = (mp & 32767);
            mph = (mp >> 15);
            um = ((1 << (BigInteger.DB - 15)) - 1);
            mt2 = (2 * _arg1.t);
        }
        public function mulTo(_arg1:BigInteger, _arg2:BigInteger, _arg3:BigInteger):void{
            _arg1.multiplyTo(_arg2, _arg3);
            reduce(_arg3);
        }
        public function revert(_arg1:BigInteger):BigInteger{
            var _local2:BigInteger;
            _local2 = new BigInteger();
            _arg1.copyTo(_local2);
            reduce(_local2);
            return (_local2);
        }
        public function convert(_arg1:BigInteger):BigInteger{
            var _local2:BigInteger;
            _local2 = new BigInteger();
            _arg1.abs().dlShiftTo(m.t, _local2);
            _local2.divRemTo(m, null, _local2);
            if ((((_arg1.s < 0)) && ((_local2.compareTo(BigInteger.ZERO) > 0)))){
                m.subTo(_local2, _local2);
            };
            return (_local2);
        }
        public function reduce(_arg1:BigInteger):void{
            var _local2:int;
            var _local3:int;
            var _local4:int;
            while (_arg1.t <= mt2) {
                var _local5 = _arg1.t++;
                _arg1.a[_local5] = 0;
            };
            _local2 = 0;
            while (_local2 < m.t) {
                _local3 = (_arg1.a[_local2] & 32767);
                _local4 = (((_local3 * mpl) + ((((_local3 * mph) + ((_arg1.a[_local2] >> 15) * mpl)) & um) << 15)) & BigInteger.DM);
                _local3 = (_local2 + m.t);
                _arg1.a[_local3] = (_arg1.a[_local3] + m.am(0, _local4, _arg1, _local2, 0, m.t));
                while (_arg1.a[_local3] >= BigInteger.DV) {
                    _arg1.a[_local3] = (_arg1.a[_local3] - BigInteger.DV);
                    _local5 = _arg1.a;
                    ++_local3;
                    var _local6 = _local3;
                    var _local7 = (_local5[_local6] + 1);
                    _local5[_local6] = _local7;
                };
                _local2++;
            };
            _arg1.clamp();
            _arg1.drShiftTo(m.t, _arg1);
            if (_arg1.compareTo(m) >= 0){
                _arg1.subTo(m, _arg1);
            };
        }
        public function sqrTo(_arg1:BigInteger, _arg2:BigInteger):void{
            _arg1.squareTo(_arg2);
            reduce(_arg2);
        }

    }
}//package com.hurlant.math