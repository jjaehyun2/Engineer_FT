/**
 * User: booster
 * Date: 14/08/14
 * Time: 16:50
 */
package plugs.inputs {
import plugs.IOutput;
import plugs.outputs.IntOutput;
import plugs.outputs.NumberOutput;

public class NumberInput extends AbstractInput {
    public function NumberInput(name:String = null) {
        super(name);
    }

    override public function canConnect(output:IOutput):Boolean {
        return output is IntOutput || output is NumberOutput;
    }
}
}