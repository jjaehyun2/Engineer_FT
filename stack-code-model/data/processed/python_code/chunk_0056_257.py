/**
 * Created by Luca.
 */
package com.jucasoft.flexjs.test.inheritance.vo {
public class ClassC extends ClassB {
    public function ClassC() {
    }

    override public function a():void {
        trace('ClassC.a()');
        super.a();
    }
}
}