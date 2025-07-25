/**
 * Copyright (C) 2010 Rafał Szemraj.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.puremvc.as3.multicore.utilities.fabrication.injection {
    import flash.utils.Dictionary;
    import flash.utils.getQualifiedClassName;

    import org.as3commons.reflect.Field;
    import org.as3commons.reflect.MetaData;
    import org.as3commons.reflect.MetaDataArgument;
    import org.as3commons.reflect.Type;
    import org.puremvc.as3.multicore.utilities.fabrication.patterns.facade.FabricationFacade;

    public class Injector {

        public static const INJECT_PROXY:String = "InjectProxy";
        public static const INJECT_MEDIATOR:String = "InjectMediator";

        private static var CACHED_CONTEXT_INJECTION_DATA:Dictionary = new Dictionary();

        protected var facade:FabricationFacade;
        protected var injectionMetadataTagName:String;

        protected var context:*;

        public function Injector(facade:FabricationFacade, context:*, injectionMetadataTagName:String)
        {
            this.facade = facade;
            this.context = context;
            this.injectionMetadataTagName = injectionMetadataTagName;

        }

        /**
         * Runs injection procedure on given context
         * @return Array of injected field names
         */
        public function inject():Array
        {

            var fieldNames:Array = [];
            var injectionField:InjectionField;
            var contextInjectionDataMarkup:String = getQualifiedClassName(context) + "_" + injectionMetadataTagName;
            var contextInjectionData:Array = CACHED_CONTEXT_INJECTION_DATA[ contextInjectionDataMarkup ] as Array;
            // check if there is already cached injection data for given context type
            if (!contextInjectionData) {

                // there is no cached injection data, so process current class

                contextInjectionData = [];
                var injectionFields:Array = getInjectionFieldsByInjectionType( Type.forInstance(context), injectionMetadataTagName);
                for each(injectionField in injectionFields) {

                    contextInjectionData[ contextInjectionData.length ] = injectionField;
                }
                // save processed injection data in cache
                CACHED_CONTEXT_INJECTION_DATA[ contextInjectionDataMarkup ] = contextInjectionData;
            }

            // make injection on context
            var injectionDataLength:int = contextInjectionData.length;
            for (var i:int = 0; i < injectionDataLength; ++i) {

                var fieldName:String = processSingleField(contextInjectionData[ i ] as InjectionField);
                if (fieldName)
                    fieldNames[ fieldNames.length ] = fieldName;
            }
            return fieldNames;
        }

         /**
         * Returns info about context properties described by injection metatag
         * @param injectionType type of injection ( metatag name )
         * @return Array instance of InjectionField elements
         * @see org.puremvc.as3.multicore.utilities.fabrication.injection.InjectionField
         */
        private function getInjectionFieldsByInjectionType(type:Type, injectionMetadataTagName:String):Array
        {

            var injectionFields:Array = [];
            var fields:Array = type.fields;
            for each(var field:Field in fields) {

                var fieldMetadatas:Array = field.metaData;
                if (fieldMetadatas && fieldMetadatas.length) {

                    for each(var metadata:MetaData in fieldMetadatas) {

                        if (metadata.name == injectionMetadataTagName) {

                            var injectionField:InjectionField = new InjectionField();
                            injectionField.fieldName = field.name;
                            injectionField.elementTypeIsInterface = field.type.isInterface;
                            injectionField.elementClass = field.type.clazz;

                            var nameArgument:MetaDataArgument = metadata.getArgument( "" ) || metadata.getArgument( "name" );
                            if( nameArgument )
                                injectionField.elementName = nameArgument.value;
                            injectionFields.push( injectionField );

                        }

                    }
                }
            }
            return injectionFields;
        }

        /**
         * Checks if element with given name exists and can be injected
         * @param elementName name of element
         * @return <b>true</b> if element with given name exists, otherwise <b>false</b>
         */
        protected function elementExist(elementName:String):Boolean
        {
            throw new Error("Abstract method invocation error");
        }

        /**
         * Returns element with given name for injection
         * @param elementName name of element
         * @param elementClass element class
         * @return instance of element to be injected
         */
        protected function getPatternElementForInjection(elementName:String, elementClass:Class):Object
        {
            throw new Error("Abstract method invocation error");
        }

        /**
         * Function handler invoked when there is no element present with given name
         * @param fieldName name of element
         */
        protected function onNoPatternElementAvaiable(fieldName:String):void
        {

            facade.logger.error("Cannot resolve injection element [ " + fieldName + " ] at [ " + getQualifiedClassName(context) + " ]");
        }

        /**
         * Function handler invoked when filed for injection is typed as interface
         * and there is no given name for injection element
         * @param fieldName name of filed typed as interface
         */
        protected function onUnambiguousPatternElementName(fieldName:String):void
        {


            facade.logger.error("field [ " + fieldName + " ] is typed as interface, so name for [ " + injectionMetadataTagName + " ] MUST be given.");
        }

        /**
         * Returns name of element to be injected
         * @param injectionField field instance to process
         * @param tagName name of injection tag
         */
        protected function getElementName(injectionField:InjectionField):String
        {
            var name:String = injectionField.elementName;
            if (name == null && !injectionField.elementTypeIsInterface)
                name = injectionField.elementClass['NAME'];
            return name;
        }


        private function processSingleField(injectionField:InjectionField):String
        {

            if (context[ injectionField.fieldName ] != null) return null;

            // retrieve element name
            var elementName:String = getElementName(injectionField);
            if (elementName && !elementExist(elementName)) {
                onNoPatternElementAvaiable(injectionField.fieldName);
                return null;
            }
            if (!elementName && injectionField.elementTypeIsInterface) {
                onUnambiguousPatternElementName(injectionField.fieldName);
                return null;
            }
            // put element into cache

            var elementClass:Class = injectionField.elementClass;

            var patternElement:Object = getPatternElementForInjection(elementName, elementClass);
            if (patternElement && patternElement is elementClass)
                context[ injectionField.fieldName ] = patternElement;
            else
                onNoPatternElementAvaiable(elementName);
            return injectionField.fieldName;
        }



    }
}