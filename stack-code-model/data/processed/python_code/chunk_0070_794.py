package flash.events
{
/**
 * @author a.vorobev 2017-12-18
 */
public class StageOrientationEvent extends Event
{
      public function StageOrientationEvent(type:String, bubbles:Boolean = false, cancelable:Boolean = false)
      {
         super(type,bubbles,cancelable);
      }
}
}