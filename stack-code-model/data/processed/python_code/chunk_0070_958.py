package my.patterns {
public class Dog extends Mammal {
    override public function say():String
    {
        return super.say() + " Woof-woof-woof\r\n";
    }

    override public function init():void
    {
        super.init();
        this.name = "A dog";
    }

    override protected function get avatarName():String
    {
        return "dog";
    }
}
}