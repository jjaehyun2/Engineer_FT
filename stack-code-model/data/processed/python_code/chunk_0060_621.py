/**
 * Created by varadig on 28/11/14.
 */
package com.greensock {
import core.base.CoreBaseClassFactory;
import core.base.CoreCallback;
import core.context.CoreContext;
import core.service.CoreServiceContainer;

public class CoreTimelineLite extends TimelineLite {
	public var sc:CoreServiceContainer;
	public var context:CoreContext;
	public var callbacks:Array = [];
	private var _name:String;
	protected static var nameIndex:int = 0;
	protected var namePrefix:String = "core.timeline.lite";

	public function CoreTimelineLite(vars:Object = null) {
		super(vars);
		this._name = this.generateName();
		CoreBaseClassFactory.construct(this);

	}


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
		CoreBaseClassFactory.log(this, message);
	}

	private function generateName():String {
		return (this.namePrefix + CoreTimelineLite.nameIndex++) as String;
	}


}
}