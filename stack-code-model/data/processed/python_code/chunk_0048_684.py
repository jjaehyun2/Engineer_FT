package skein.binding
{
import skein.binding.core.MethodSource;
import skein.binding.core.PropertyDestination;

public function getter(site:Object, method:String, params:Array = null):MethodSource
{
    return new MethodSource(site, method, params);
}
}