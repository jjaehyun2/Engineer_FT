package my.patterns {
public class Cat extends Animal {
    override public function say():String
    {
        return super.say() + " meow-meow-meow\r\n";
    }

    override public function init():void
    {
        super.init();
        this.name = "A cat";
    }
}
}