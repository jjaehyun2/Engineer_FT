/**
 * Created by bslote on 3/29/15.
 */
package pw.fractal.vbm.iterator
{
    import flash.errors.IllegalOperationError;

    public class AbstractIterator implements IIterator
    {
        protected var _index:int;

        public function AbstractIterator()
        {
            _index = 0;
        }

        public function reset():void
        {
            _index = 0;
        }

        public function get position():int
        {
            return _index;
        }

        public function set position(value:int):void
        {
            if (_index != value)
            {
                _index = value;
            }
        }

        public function next():Object
        {
            throw new IllegalOperationError("next() implementation must be provided by subclass");
        }

        public function prev():Object
        {
            throw new IllegalOperationError("prev() implementation must be provided by subclass");
        }

        public function hasNext():Boolean
        {
            throw new IllegalOperationError("hasNext() implementation must be provided by subclass");
        }
    }
}