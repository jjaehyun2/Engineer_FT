package as3.depending.spec {
import as3.depending.Providing;
import as3.depending.RelaxedResolver;
import as3.depending.Resolver;

public class ResolverAdapter {
    public var resolver:Resolver;

    public function get relaxedResolver():RelaxedResolver {
        return RelaxedResolver(resolver);
    }

    public final function failNotImplemented(feature:String):void {
        throw new NotImplementedException(this, feature);
    }


    public function specifyTypeForResolver(type:Class):void {
        failNotImplemented("specify a type as resolvable");
    }

    public function specifyImplementationForResolver(definingInterface:Class, implementingClass:Class):void {
        failNotImplemented("specify an implementation as resolvable");
    }

    public function specifyAnImplementingInstanceForResolver(definingInterface:Class, instance:Object):void {
        failNotImplemented("specify an implementing instance as resolvable");
    }

    public function specifyAProviderForResolver(definingInterface:Class, provider:Providing):void {
        failNotImplemented("specify a Provider instance to use for resolving a definition");
    }

    public function specifyAProviderFunctionForResolver(definingInterface:Class, provider:Function):void {
        failNotImplemented( "specify a function as a provider to use for resolving a definition");
    }

    public function specifyConstructorInjectableProtocolForResolver():void {
        failNotImplemented( "specify ConstructorInjectableProtocol as resolvable");
    }

    public function specifyConstructorInjectableProtocolAsImplementationForResolver(definingInterface:Class):void {
        failNotImplemented("specify the implementation ConstructorInjectableProtocol as resolvable");
    }

    public function specifyInlineConstructorInjectableProtocolForResolver():void {
        failNotImplemented("specify an implementation of IResolverSpecProtocol as resolvable that contains a way to inject the resolver");
    }

    public function specifyAValueForResolver(value:Object):void {
        failNotImplemented("specify a value as resolvable");
    }

    public function specifyAValueByIdentifier(identifier:Object, value:Object):void {
        failNotImplemented("specify a value as resolvable by an identifier");
    }

    protected var expectingCachedInstance:Boolean;
    public final function usingInstanceCaching(active:Boolean):ResolverAdapter {
        expectingCachedInstance = active;
        return this;
    }
}
}