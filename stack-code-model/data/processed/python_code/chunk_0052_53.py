/**
 * Created by bslote on 3/28/15.
 */
package pw.fractal.vbm.sequence
{
    import flash.errors.IllegalOperationError;

    import pw.fractal.vbm.iterator.IIterator;
    import pw.fractal.vbm.iterator.ReverseSequenceIterator;
    import pw.fractal.vbm.iterator.SequenceIterator;

    public class AbstractSequence implements ISequence
    {
        protected var _direction:String;
        protected var _iterator:IIterator;
        protected var _name:String;
        protected var _sequence:Object;

        public function AbstractSequence(sequence:Object, direction:String = SequenceDirection.FORWARD, name:String = "")
        {
            _name = name;
            _sequence = sequence;
            _iterator = new SequenceIterator(this);

            this.direction = direction;
        }

        public function get sequence():Object
        {
            return _sequence;
        }

        public function getElement(index:int):Object
        {
            throw new IllegalOperationError("getElement() implementation must be provided by subclass");
        }

        public function getRelativeElement(index:int):Object
        {
            return getElement(_iterator.position + index);
        }

        public function getSubsequence(startIndex:int, length:int):Array
        {
            var subsequence:Array = [];
            var oldPosition:int = _iterator.position;

            _iterator.position = startIndex - 1;
            while (length--)
            {
                subsequence.push(_iterator.next());
            }

            _iterator.position = oldPosition;

            return subsequence;
        }

        public function get name():String
        {
            return _name;
        }

        public function get direction():String
        {
            return _direction
        }

        public function set direction(value:String):void
        {
            if (value == _direction)
            {
                return;
            }

            var position:int = _iterator.position;

            if (value == SequenceDirection.FORWARD)
            {
                _iterator = new SequenceIterator(this);
            }
            else if (value == SequenceDirection.BACKWARD)
            {
                _iterator = new ReverseSequenceIterator(this);
            }
            else
            {
                throw new IllegalOperationError("Sequence direction must be a valid SequenceDirection");
            }

            _iterator.position = position;
            _direction = value;
        }

        public function reset():void
        {
            _iterator.reset();
        }

        public function next():Object
        {
            return _iterator.next();
        }

        public function prev():Object
        {
            return _iterator.prev();
        }

        public function hasNext():Boolean
        {
            return _iterator.hasNext();
        }

        public function get position():int
        {
            return _iterator.position;
        }

        public function set position(value:int):void
        {
            _iterator.position = value;
        }
    }
}