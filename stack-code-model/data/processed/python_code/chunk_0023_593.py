package org.swiftsuspenders.injectionpoints
{
    import flash.utils.describeType;
    
    import org.swiftsuspenders.Injector;
    
    public class ConstructorInjectionPoint extends MethodInjectionPoint
    {
        /*******************************************************************************************
        *								public methods											   *
        *******************************************************************************************/
        public function ConstructorInjectionPoint(node : XML, clazz : Class, injector : Injector)
        {
            /*
              In many cases, the flash player doesn't give us type information for constructors until 
              the class has been instantiated at least once. Therefore, we do just that if we don't get 
              type information for at least one parameter.
             */ 
            if (node.parameter.(@type == '*').length() == node.parameter.@type.length())
            {
                createDummyInstance(node, clazz);
            }
            super(node, injector);
        }
        
        override public function applyInjection(target : Object, injector : Injector) : Object
        {
            var p : Array = gatherParameterValues(target, injector);
            //the only way to implement ctor injections, really!
            switch (p.length)
            {
                case 0 : return (new target());
                case 1 : return (new target(p[0]));
                case 2 : return (new target(p[0], p[1]));
                case 3 : return (new target(p[0], p[1], p[2]));
                case 4 : return (new target(p[0], p[1], p[2], p[3]));
                case 5 : return (new target(p[0], p[1], p[2], p[3], p[4]));
                case 6 : return (new target(p[0], p[1], p[2], p[3], p[4], p[5]));
                case 7 : return (new target(p[0], p[1], p[2], p[3], p[4], p[5], p[6]));
                case 8 : return (new target(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7]));
                case 9 : return (new target(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]));
                case 10 : return (new target(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]));
            }
            return null;
        }

        /*******************************************************************************************
        *								protected methods										   *
        *******************************************************************************************/
        override protected function initializeInjection(node : XML, injector : Injector) : void
        {
            var nameArgs : XMLList = node.parent().metadata.(@name == 'Inject').arg.(@key == 'name');
            methodName = 'constructor';
            
            gatherParameters(node, nameArgs, injector);
        }
        
        /*******************************************************************************************
        *								private methods											   *
        *******************************************************************************************/
        private function createDummyInstance(constructorNode : XML, clazz : Class) : void
        {
            try
            {
                switch (constructorNode.children().length())
                {
                    case 0 : (new clazz()); break;
                    case 1 : (new clazz(null)); break;
                    case 2 : (new clazz(null, null)); break;
                    case 3 : (new clazz(null, null, null)); break;
                    case 4 : (new clazz(null, null, null, null)); break;
                    case 5 : (new clazz(null, null, null, null, null)); break;
                    case 6 : (new clazz(null, null, null, null, null, null)); break;
                    case 7 : (new clazz(null, null, null, null, null, null, null)); break;
                    case 8 : (new clazz(null, null, null, null, null, null, null, null)); break;
                    case 9 : (new clazz(null, null, null, null, null, null, null, null, null)); break;
                    case 10 : (new clazz(null, null, null, null, null, null, null, null, null, null)); break;
                }
            }
            catch (error : Error)
            {
                trace(error);
            }
            constructorNode.setChildren(describeType(clazz).factory.constructor[0].children());
        }
    }
}