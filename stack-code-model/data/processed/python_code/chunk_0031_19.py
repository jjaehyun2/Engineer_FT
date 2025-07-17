package my.patterns {
public class Duck extends Animal {
    override public function say():String
    {
        return super.say() + " quack-quack-quack\r\n";
    }

    override public function init():void
    {
        super.init();
        this.name = "A duck";
    }
}
}