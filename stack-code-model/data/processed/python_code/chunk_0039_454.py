/**
 * User: booster
 * Date: 15/08/14
 * Time: 10:03
 */
package plugs.providers {
import medkit.collection.ArrayList;
import medkit.collection.List;

import plugs.Connection;
import plugs.IOutput;
import plugs.IProvider;
import plugs.error.PullingDataNotSupportedError;
import plugs.error.PushingDataNotSupportedError;

public class AbstractProvider implements IProvider {
    protected var _outputs:List = new ArrayList();
    protected var _name:String;

    public function AbstractProvider(name:String = null) {
        _name = name;
    }

    public function get outputs():List { return _outputs; }
    public function get name():String { return _name; }

    public function pushData(connection:Connection = null):void { throw new PushingDataNotSupportedError(); }
    public function requestPullData(outputConnection:Connection):* { throw new PullingDataNotSupportedError(); }

    protected function addOutput(output:IOutput):void {
        _outputs.add(output);

        output.provider = this;
    }

    protected function removeOutput(output:IOutput):void {
        output.provider = null;

        _outputs.remove(output);
    }
}
}