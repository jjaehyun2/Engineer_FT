package org.swiftsuspenders
{
    import flash.system.ApplicationDomain;
    import flash.utils.Dictionary;
    import flash.utils.Proxy;
    import flash.utils.describeType;
    import flash.utils.getDefinitionByName;
    import flash.utils.getQualifiedClassName;
    
    import org.swiftsuspenders.injectionpoints.ConstructorInjectionPoint;
    import org.swiftsuspenders.injectionpoints.InjectionPoint;
    import org.swiftsuspenders.injectionpoints.MethodInjectionPoint;
    import org.swiftsuspenders.injectionpoints.NoParamsConstructorInjectionPoint;
    import org.swiftsuspenders.injectionpoints.PostConstructInjectionPoint;
    import org.swiftsuspenders.injectionpoints.PropertyInjectionPoint;
    import org.swiftsuspenders.injectionresults.InjectClassResult;
    import org.swiftsuspenders.injectionresults.InjectOtherRuleResult;
    import org.swiftsuspenders.injectionresults.InjectSingletonResult;
    import org.swiftsuspenders.injectionresults.InjectValueResult;

    public class Injector
    {
        /*******************************************************************************************
        *								private properties										   *
        *******************************************************************************************/
        private var m_parentInjector : Injector;
        private var m_applicationDomain:ApplicationDomain;
        private var m_mappings : Dictionary;
        private var m_injectionPointLists : Dictionary;
        private var m_constructorInjectionPoints : Dictionary;
        private var m_attendedToInjectees : Dictionary;
        private var m_xmlMetadata : XML;
        
        
        /*******************************************************************************************
        *								public methods											   *
        *******************************************************************************************/
        public function Injector(xmlConfig : XML = null)
        {
            m_mappings = new Dictionary();
            m_injectionPointLists = new Dictionary();
            m_constructorInjectionPoints = new Dictionary();
            m_attendedToInjectees = new Dictionary(true);
            m_xmlMetadata = xmlConfig;
        }
        
        public function mapValue(whenAskedFor : Class, useValue : Object, named : String = "") : *
        {
            var config : InjectionConfig = getMapping(whenAskedFor, named);
            config.setResult(new InjectValueResult(useValue));
            return config;
        }
        
        public function mapClass(
                whenAskedFor : Class, instantiateClass : Class, named : String = "") : *
        {
            var config : InjectionConfig = getMapping(whenAskedFor, named);
            config.setResult(new InjectClassResult(instantiateClass));
            return config;
        }
        
        public function mapSingleton(whenAskedFor : Class, named : String = "") : *
        {
            return mapSingletonOf(whenAskedFor, whenAskedFor, named);
        }
        
        public function mapSingletonOf(
            whenAskedFor : Class, useSingletonOf : Class, named : String = "") : *
        {
            var config : InjectionConfig = getMapping(whenAskedFor, named);
            config.setResult(new InjectSingletonResult(useSingletonOf));
            return config;
        }
        
        public function mapRule(whenAskedFor : Class, useRule : *, named : String = "") : *
        {
            var config : InjectionConfig = getMapping(whenAskedFor, named);
            config.setResult(new InjectOtherRuleResult(useRule));
            return useRule;
        }
        
        public function getMapping(whenAskedFor : Class, named : String = "") : InjectionConfig
        {
            var requestName : String = getQualifiedClassName(whenAskedFor);
            var config : InjectionConfig = m_mappings[requestName + '#' + named];
            if (!config)
            {
                config = m_mappings[requestName + '#' + named] =
                    new InjectionConfig(whenAskedFor, named);
            }
            return config;
        }
        
        public function injectInto(target : Object) : void
        {
            if (m_attendedToInjectees[target])
            {
                return;
            }
            m_attendedToInjectees[target] = true;
            
            //get injection points or cache them if this target's class wasn't encountered before
            var injectionPoints : Array;
            
            var ctor : Class = getConstructor(target);
            
            injectionPoints = m_injectionPointLists[ctor] || getInjectionPoints(ctor);
            
            var length : int = injectionPoints.length;
            for (var i : int = 0; i < length; i++)
            {
                var injectionPoint : InjectionPoint = injectionPoints[i];
                injectionPoint.applyInjection(target, this);
            }
            
        }
        
        public function instantiate(clazz:Class):*
        {
            var injectionPoint : InjectionPoint = m_constructorInjectionPoints[clazz];
            if (!injectionPoint)
            {
                getInjectionPoints(clazz);
                injectionPoint = m_constructorInjectionPoints[clazz];
            }
            var instance : * = injectionPoint.applyInjection(clazz, this);
            injectInto(instance);
            return instance;
        }
        
        public function unmap(clazz : Class, named : String = "") : void
        {
            var mapping : InjectionConfig = getConfigurationForRequest(clazz, named);
            if (!mapping)
            {
                throw new InjectorError('Error while removing an injector mapping: ' +
                    'No mapping defined for class ' + getQualifiedClassName(clazz) +
                    ', named "' + named + '"');
            }
            mapping.setResult(null);
        }

        public function hasMapping(clazz : Class, named : String = '') : Boolean
        {
            var mapping : InjectionConfig = getConfigurationForRequest(clazz, named);
            if (!mapping)
            {
                return false;
            }
            return mapping.hasResponse(this);
        }

        public function getInstance(clazz : Class, named : String = '') : *
        {
            var mapping : InjectionConfig = getConfigurationForRequest(clazz, named);
            if (!mapping || !mapping.hasResponse(this))
            {
                throw new InjectorError('Error while getting mapping response: ' +
                    'No mapping defined for class ' + getQualifiedClassName(clazz) +
                    ', named "' + named + '"');
            }
            return mapping.getResponse(this);
        }
        
        public function createChildInjector(applicationDomain:ApplicationDomain=null) : Injector
        {
            var injector : Injector = new Injector();
            injector.setApplicationDomain(applicationDomain);
            injector.setParentInjector(this);
            return injector;
        }
        
        public function setApplicationDomain(applicationDomain:ApplicationDomain):void
        {
            m_applicationDomain = applicationDomain;
        }
        
        public function getApplicationDomain():ApplicationDomain
        {
            return m_applicationDomain ? m_applicationDomain : ApplicationDomain.currentDomain;
        }

        public function setParentInjector(parentInjector : Injector) : void
        {
            //restore own map of worked injectees if parent injector is removed
            if (m_parentInjector && !parentInjector)
            {
                m_attendedToInjectees = new Dictionary(true);
            }
            m_parentInjector = parentInjector;
            //use parent's map of worked injectees
            if (parentInjector)
            {
                m_attendedToInjectees = parentInjector.attendedToInjectees;
            }
        }
        
        public function getParentInjector() : Injector
        {
            return m_parentInjector;
        }
        
        
        /*******************************************************************************************
        *								internal methods										   *
        *******************************************************************************************/
        internal function getAncestorMapping(
                whenAskedFor : Class, named : String = null) : InjectionConfig
        {
            var parent : Injector = m_parentInjector;
            while (parent)
            {
                var parentConfig : InjectionConfig =
                    parent.getConfigurationForRequest(whenAskedFor, named, false);
                if (parentConfig && parentConfig.hasOwnResponse())
                {
                    return parentConfig;
                }
                parent = parent.getParentInjector();
            }
            return null;
        }

        internal function get attendedToInjectees() : Dictionary
        {
            return m_attendedToInjectees;
        }

        
        /*******************************************************************************************
        *								private methods											   *
        *******************************************************************************************/
        private function getInjectionPoints(clazz : Class) : Array
        {
            var description : XML = describeType(clazz);
            var injectionPoints : Array = [];
            m_injectionPointLists[clazz] = injectionPoints;
            m_injectionPointLists[description.@name.toString()] = injectionPoints;
            var node : XML;
            
            // This is where we have to wire in the XML...
            if(m_xmlMetadata)
            {
                createInjectionPointsFromConfigXML(description);
                addParentInjectionPoints(description, injectionPoints);
            }
            
            var injectionPoint : InjectionPoint;
            //get constructor injections
            node = description.factory.constructor[0];
            if (node)
            {
                m_constructorInjectionPoints[clazz] = 
                    new ConstructorInjectionPoint(node, clazz, this);
            }
            else
            {
                m_constructorInjectionPoints[clazz] = new NoParamsConstructorInjectionPoint();
            }
            //get injection points for variables
            for each (node in description.factory.*.
                (name() == 'variable' || name() == 'accessor').metadata.(@name == 'Inject'))
            {
                injectionPoint = new PropertyInjectionPoint(node, this);
                injectionPoints.push(injectionPoint);
            }
        
            //get injection points for methods
            for each (node in description.factory.method.metadata.(@name == 'Inject'))
            {
                injectionPoint = new MethodInjectionPoint(node, this);
                injectionPoints.push(injectionPoint);
            }
            
            //get post construct methods
            var postConstructMethodPoints : Array = [];
            for each (node in description.factory.method.metadata.(@name == 'PostConstruct'))
            {
                injectionPoint = new PostConstructInjectionPoint(node, this);
                postConstructMethodPoints.push(injectionPoint);
            }
            if (postConstructMethodPoints.length > 0)
            {
                postConstructMethodPoints.sortOn("order", Array.NUMERIC);
                injectionPoints.push.apply(injectionPoints, postConstructMethodPoints);
            }
            
            return injectionPoints;
        }

        private function getConfigurationForRequest(
            clazz : Class, named : String, traverseAncestors : Boolean = true) : InjectionConfig
        {
            var requestName : String = getQualifiedClassName(clazz);
            var config:InjectionConfig = m_mappings[requestName + '#' + named];
            if(!config && traverseAncestors &&
                m_parentInjector && m_parentInjector.hasMapping(clazz, named))
            {
                config = getAncestorMapping(clazz, named);
            }
            return config;
        }
        
        private function createInjectionPointsFromConfigXML(description : XML) : void
        {
            var node : XML;
            //first, clear out all "Inject" metadata, we want a clean slate to have the result 
            //work the same in the Flash IDE and MXMLC
            for each (node in description..metadata.(@name=='Inject' || @name=='PostConstruct'))
            {
                delete node.parent().metadata.(@name=='Inject' || @name=='PostConstruct')[0];
            }
            
            //now, we create the new injection points based on the given xml file
            var className:String = description.factory.@type;
            for each (node in m_xmlMetadata.type.(@name == className).children())
            {
                var metaNode : XML = <metadata/>;
                if (node.name() == 'postconstruct')
                {
                    metaNode.@name = 'PostConstruct';
                    if (node.@order.length())
                    {
                        metaNode.appendChild(<arg key='order' value={node.@order}/>);
                    }
                }
                else
                {
                    metaNode.@name = 'Inject';
                    if (node.@injectionname.length())
                    {
                        metaNode.appendChild(<arg key='name' value={node.@injectionname}/>);
                    }
                    for each (var arg : XML in node.arg)
                    {
                        metaNode.appendChild(<arg key='name' value={arg.@injectionname}/>);
                    }
                }
                var typeNode : XML;
                if (node.name() == 'constructor')
                {
                    typeNode = description.factory[0];
                }
                else
                {
                    typeNode = description.factory.*.(attribute('name') == node.@name)[0];
                    if (!typeNode)
                    {
                        throw new InjectorError('Error in XML configuration: Class "' + className +
                            '" doesn\'t contain the instance member "' + node.@name + '"');
                    }
                }
                typeNode.appendChild(metaNode);
            }
        }
        
        private function addParentInjectionPoints(description : XML, injectionPoints : Array) : void
        {
            var parentClassName : String = description.factory.extendsClass.@type[0];
            if (!parentClassName)
            {
                return;
            }
            var parentInjectionPoints : Array = m_injectionPointLists[parentClassName] || 
                    getInjectionPoints(Class(getDefinitionByName(parentClassName)));
            injectionPoints.push.apply(injectionPoints, parentInjectionPoints);
        }
    }
}