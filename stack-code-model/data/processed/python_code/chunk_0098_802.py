/**
 * Created by Luca.
 */
package com.jucasoft.flexjs.test.nestedobjects {
import com.jucasoft.flexjs.main.person.vo.Person;
import com.jucasoft.flexjs.main.person.vo.PersonBuilder;

public class TestNestedObjects {
    public function TestNestedObjects() {
        trace('TestNestedObjects.TestNestedObjects()');
        test();
    }

    public function test():void {
        trace('TestNestedObjects.test()');
        trace('Person: ' + Person(new PersonBuilder().newInstance()).toString());
        trace('Person: ' + Person(new PersonBuilder().newInstance()).toString());
        trace('Person: ' + Person(new PersonBuilder().newInstance()).toString());
        trace('Person: ' + Person(new PersonBuilder().newInstance()).toString());
    }
}
}