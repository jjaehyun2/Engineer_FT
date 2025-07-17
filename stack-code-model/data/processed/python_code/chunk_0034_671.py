/**
 * Created by singuerinc on 09/05/2014.
 */
package signals {
import org.osflash.signals.PrioritySignal;

public class ChangeAlphaSignal extends PrioritySignal {

  public function ChangeAlphaSignal() {
    super(Number);
  }

  public var alpha:Number;

  override public function dispatch(...valueObjects):void {
    this.alpha = valueObjects[0];
    super.dispatch.apply(this, valueObjects);
  }
}
}