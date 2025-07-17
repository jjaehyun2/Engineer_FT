package 
{
    public class Controller
    {
        public static function listenToChildren(view:*, childNames:Array, methodName:String, owner:*):void
        {
            for (var c:int = 0; c < childNames.length; c++) 
            {
                var name:String = childNames[c];
                var child:* = view[name];
                View.listenToOverAndDown(child, methodName, owner);
            }
        }

        public static function isObject(value:*):Boolean
        {
            return "object" === typeof(value);
        }

        /**
         * @param   changes     What is different as nested hashes.
         */
        public static function visit(parent:*, changes:Object, boundFunction:Function):void
        {
            for (var key:String in changes)
            {
                var change:* = changes[key];
                var child:* = parent[key];
                child = boundFunction(child, key, change);
                if (isObject(change))
                {
                    visit(child, change, boundFunction);
                }
                else
                {
                    if ("x" === key)
                    {
                        View.setPositionX(parent, change);
                    }
                    else if ("y" === key)
                    {
                        View.setPositionY(parent, change);
                    }
                    else if ("visible" === key)
                    {
                        View.setVisible(parent, change);
                    }
                }
            }
        }

        public static function setStates(parent:*, changes:Object, boundFunction:Function, boundArgument:*=undefined):void
        {
            for (var key:String in changes)
            {
                var change:* = changes[key];
                var child:* = parent[key];
                if (isObject(change))
                {
                    setStates(child, change, boundFunction, boundArgument);
                }
                else
                {
                    if (undefined !== boundArgument)
                    {
                        boundFunction(child, change, boundArgument);
                    }
                    else
                    {
                        boundFunction(child, change);
                    }
                }
            }
        }
    }
}