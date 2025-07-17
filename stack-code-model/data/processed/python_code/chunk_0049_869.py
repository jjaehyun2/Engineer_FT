/**
 * User: booster
 * Date: 14/08/14
 * Time: 11:06
 */
package plugs.outputs {
import medkit.collection.ArrayList;
import medkit.collection.List;

import plugs.IOutput;

import plugs.IProvider;

import plugs.IInput;

public class AbstractOutput implements IOutput {
    protected var _provider:IProvider;
    protected var _connections:List = new ArrayList();
    private var _name:String;

    public function AbstractOutput(name:String = null) {
        _name = name;
    }

    public function get provider():IProvider { return _provider; }
    public function set provider(value:IProvider):void { _provider = value; }

    public function get connections():List { return _connections; }

    public function get name():String { return _name; }

    public function canConnect(input:IInput):Boolean { throw new Error("abstract method"); }

    public function toString():String { return _name != null ? _name : ""; }
}
}