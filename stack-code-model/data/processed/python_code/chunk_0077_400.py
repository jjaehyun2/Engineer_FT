package plugins.as3 {
import core.base.CoreBaseClass;
import core.base.CoreBaseClassFactory;
import core.base.CoreCallback;
import core.context.CoreContext;
import core.service.CoreServiceContainer;
import core.utils.Log;

import flash.display.NativeWindow;
import flash.display.NativeWindowInitOptions;
import flash.display.NativeWindowInitOptions;

/**
 * @author varadig
 */
public class GuiNativeWindow extends NativeWindow {

    protected static var nameIndex:int = 0;
    protected var namePrefix:String = "object";

    private var _name:String;


    public function GuiNativeWindow(initOptions:NativeWindowInitOptions) {
        super(initOptions);
        this._name = this.generateName();
        CoreBaseClassFactory.construct(this);
    }

    public var sc:CoreServiceContainer;
    public var context:CoreContext;
    public var callbacks:Array = [];

    public function get name():String {
        return this._name as String;
    }

    public function serviceAddCallback(params:Array):void {
        CoreBaseClassFactory.serviceAddCallback(this, params);
    }

    public function serviceAddCallbacks(params:Array):void {
        CoreBaseClassFactory.serviceAddCallbacks(this, params);
    }

    public function serviceRemoveCallback(params:Array):void {
        CoreBaseClassFactory.serviceRemoveCallback(this, params);
    }

    public function serviceRemoveCallbacks(params:Array):void {
        CoreBaseClassFactory.serviceRemoveCallbacks(this, params);
    }


    public function createCallBack(group:String):CoreCallback {
        return CoreBaseClassFactory.createCallBack(this, group);
    }

    protected function log(...message):void {
        Log.add(message);
//        CoreBaseClassFactory.log(this, message);
    }

    private function generateName():String {
        return (this.namePrefix + GuiNativeWindow.nameIndex++) as String;
    }

}
}