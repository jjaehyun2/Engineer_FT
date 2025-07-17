/**
 * User: booster
 * Date: 14/08/14
 * Time: 17:22
 */
package plugs.outputs {
import plugs.inputs.BooleanInput;
import plugs.IInput;
import plugs.inputs.IntInput;
import plugs.inputs.NumberInput;

public class BooleanOutput extends AbstractOutput {
    public function BooleanOutput(name:String = null) {
        super(name);
    }

    override public function canConnect(input:IInput):Boolean {
        return input is BooleanInput || input is IntInput || input is NumberInput;
    }
}
}