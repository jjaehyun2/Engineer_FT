/**
 * Created by Luca.
 */
package com.jucasoft.flexjs.test.singleton.vo {
import com.jucasoft.flexjs.main.person.vo.Person;

public class SingletonDemo {
    private static var instance:SingletonDemo = new SingletonDemo();

    public function SingletonDemo() {
        if (instance) throw new Error("Singleton and can only be accessed through Singleton.getInstance()");
    }

    public static function getInstance():SingletonDemo {
        trace('SingletonDemo.getInstance()');
        return instance;
    }

    public var persona:Person;

}
}