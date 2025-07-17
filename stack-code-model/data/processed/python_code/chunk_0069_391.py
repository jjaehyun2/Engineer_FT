/**
 * Created by bslote on 3/28/15.
 */
package pw.fractal.vbm.sequence
{
    import pw.fractal.vbm.iterator.IIterator;

    public interface ISequence extends IIterator
    {
        function getElement(index:int):Object;
        function getRelativeElement(index:int):Object;
        function getSubsequence(startIndex:int, length:int):Array;
        function get sequence():Object;
        function get name():String;
        function get direction():String;
        function set direction(value:String):void;
    }
}