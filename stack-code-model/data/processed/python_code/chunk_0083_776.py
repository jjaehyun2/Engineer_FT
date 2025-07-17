package flash.events
{
/**
 * @author a.vorobev 2017-12-18
 */
public class IMEEvent extends Event
{
      public function IMEEvent(type:String, bubbles:Boolean = false, cancelable:Boolean = false)
      {
         super(type,bubbles,cancelable);
      }
}
}