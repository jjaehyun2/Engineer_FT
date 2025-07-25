/*
 *  Copyright: (c) 2016. Turtsevich Alexander
 *
 *  Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.html
 *
 *  https://github.com/kemsky/stream
 */

package com.kemsky
{
    import mx.collections.IList;

    /**
     * Global function that creates Stream objects
     * @param rest objects used as source for Stream
     * @return created Stream object
     * @example
     * <pre>
     *     var s:Stream = $(1, 2, 3);
     *     var s:Stream = $([1, 2, 3]);
     *     var s:Stream = $(new ArrayCollection([1, 2, 3]));
     *     var s:Stream = $(new ArrayList([1, 2, 3]));
     *     var s:Stream = $(new Stream([1, 2, 3]));
     *
     *     //All expressions are equivalent to:
     *     var s:Stream = new Stream([1, 2, 3])
     * </pre>
     */
    public function $(...rest):Stream
    {
        if (rest.length == 0)
        {
            //empty $
            return new Stream();
        }
        else if (rest.length == 1)
        {
            var arg:* = rest[0];

            if (arg is Array)
            {
                //$ from array
                return new Stream((arg as Array).concat());
            }
            else if (arg is Vector.<*> || arg is Vector.<Number> || arg is Vector.<int> || arg is Vector.<uint>)
            {
                var a:Array = [];
                for (var i:int = 0; i < arg.length; i++)
                {
                    a[i] = arg[i];
                }
                return new Stream(a);
            }
            else if (arg is IList)
            {
                //$ from list
                return new Stream(arg.toArray());
            }
            else if(arg is XML)
            {
                var xm:Array = [];
                for each(var xml:XML in (arg as XML).children())
                {
                    xm.push(xml);
                }
                return new Stream(xm);
            }
            else if(arg is XMLList)
            {
                var x:Array = [];
                for each(var xmlItem:XML in arg)
                {
                    x.push(xmlItem);
                }
                return new Stream(x);
            }
            else if(arg == null || arg === undefined)
            {
                //ignore empty arg
                return new Stream();
            }
            else
            {
                //$ from one item
                return new Stream([arg]);
            }
        }

        //$ from argument list
        return new Stream(rest.concat());
    }
}