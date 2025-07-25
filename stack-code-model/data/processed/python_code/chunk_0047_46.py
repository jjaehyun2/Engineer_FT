package org.yellcorp.lib.format.printf.context
{
/**
 * @private
 */
public class LastArg implements Resolver
{
    private var _value:*;

    public function LastArg()
    {
    }

    public function resolve(context:RenderContext):void
    {
        _value = context.getLastArg();
    }

    public function get value():*
    {
        return _value;
    }
}
}