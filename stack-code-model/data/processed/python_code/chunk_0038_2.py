/**
 * User: booster
 * Date: 14/08/14
 * Time: 17:22
 */
package plugs.inputs {
import plugs.outputs.BooleanOutput;
import plugs.IOutput;

public class BooleanInput extends AbstractInput {
    public function BooleanInput(name:String = null) {
        super(name);
    }

    override public function canConnect(output:IOutput):Boolean {
        return output is BooleanOutput;
    }
}
}