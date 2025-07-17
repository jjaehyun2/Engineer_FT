/**
 * Created by bslote on 3/28/15.
 */
package pw.fractal.vbm.sequence
{
    public class DoublingSequence extends ArraySequence
    {
        public function DoublingSequence(direction:String = SequenceDirection.FORWARD)
        {
            super([1, 2, 4, 8, 7, 5], direction, "Doubling sequence");
        }
    }
}