package my.patterns {
public class AnimalFactory {
    public static function createAnimal(type:Class):Animal
    {
        var a:Animal = new type();
        a.init();
        return a;
    }
}
}