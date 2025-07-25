/*
 *  Copyright: (c) 2016. Turtsevich Alexander
 *
 *  Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.html
 *
 *  https://github.com/kemsky/stream
 */

package com.kemsky.filters
{
    import com.kemsky.Stream;
    import com.kemsky.support.StreamError;

    /**
     * Creates function that extracts named property from value
     * @param name name of the property or method (nested properties are supported: 'prop.prop1.prop2' or any collection of strings)
     * @return function function that extracts named property or method from value
     */
    public function member(name:*):Function
    {
        if(name == null || name === undefined)
        {
            throw new StreamError("Parameter 'name' must be not null");
        }

        var path:Array = null;

        if(name is String)
        {
            path = name.split(".");
        }
        else
        {
            var members:Stream = Stream.from(name);

            if(!members.every(type(_, String)))
            {
                throw new StreamError("Parameter 'name' must contain only String items");
            }

            path = members.array();
        }

        var p1:String = path.length > 0 ? path[0]: undefined;
        var p2:String = path.length > 1 ? path[1]: undefined;
        var p3:String = path.length > 2 ? path[2]: undefined;
        var p4:String = path.length > 3 ? path[3]: undefined;
        var p5:String = path.length > 4 ? path[4]: undefined;

        switch (path.length)
        {
            case 1:
                return function (item:*):*
                {
                    return item != null && item.hasOwnProperty(p1) ? item[p1] : undefined;
                };
            case 2:
                return function (item:*):*
                {
                    var result:* = undefined;
                    try
                    {
                        result = item[p1][p2];
                    }
                    catch(e:Error){}
                    return result;
                };
            case 3:
                return function (item:*):*
                {
                    var result:* = undefined;
                    try
                    {
                        result = item[p1][p2][p3];
                    }
                    catch(e:Error){}
                    return result;
                };
            case 4:
                return function (item:*):*
                {
                    var result:* = undefined;
                    try
                    {
                        result = item[p1][p2][p3][p4];
                    }
                    catch(e:Error){}
                    return result;
                };
            case 5:
                return function (item:*):*
                {
                    var result:* = undefined;
                    try
                    {
                        result = item[p1][p2][p3][p4][p5];
                    }
                    catch(e:Error){}
                    return result;
                };
        }

        throw new StreamError("Property is too deep: '" + name + "', maximum nesting is 5");
    }
}