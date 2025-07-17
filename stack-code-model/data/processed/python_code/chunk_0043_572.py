/**
 * Created by bslote on 3/28/15.
 */
package pw.fractal.vbm.sequence
{
    public class FunctionSequence extends AbstractSequence
    {
        public function FunctionSequence(sequence:Function, direction:String = SequenceDirection.FORWARD, name:String = "")
        {
            super(sequence, direction, name);
        }

        override public function getElement(index:int):Object
        {
            return _sequence.apply(null, [index]);
        }
    }
}