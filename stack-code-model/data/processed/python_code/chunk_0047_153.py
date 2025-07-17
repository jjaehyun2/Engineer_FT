package my.patterns {
public class GlobalClass {
    public var value:Number;

    public function GlobalClass(enforcer:SingletonEnforcer)
    {
        if(enforcer == null)
            throw new Error("Singleton violation error");
    }

    private static var _instance:GlobalClass;
    public static function getInstance():GlobalClass
    {
        if(_instance == null)
            _instance = new GlobalClass(new SingletonEnforcer());
        return _instance;
    }
}
}

class SingletonEnforcer
{
}