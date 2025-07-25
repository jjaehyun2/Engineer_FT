////////////////////////////////////////////////////////////////////////////////
//
//  Licensed to the Apache Software Foundation (ASF) under one or more
//  contributor license agreements.  See the NOTICE file distributed with
//  this work for additional information regarding copyright ownership.
//  The ASF licenses this file to You under the Apache License, Version 2.0
//  (the "License"); you may not use this file except in compliance with
//  the License.  You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
//
////////////////////////////////////////////////////////////////////////////////


package mx.automation.delegates.flashflexkit
{ 
    import flash.display.DisplayObject;
    
    import mx.automation.Automation;
    import mx.automation.IAutomationObject;
    import mx.automation.IAutomationObjectHelper;
    import mx.core.IUIComponent;
    import mx.core.mx_internal;
    import mx.flash.ContainerMovieClip;
    use namespace mx_internal;
    
    [Mixin]
    /**
     * 
     *  Defines methods and properties required to perform instrumentation for the 
     *  ContainerMovieClip control.
     * 
     *  @see mx.flash.ContainerMovieClip
     *
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */ 
    public class  ContainerMovieClipAutomationImpl  extends UIMovieClipAutomationImpl 
    {  
        include "../../../core/Version.as";
        
        //--------------------------------------------------------------------------
        //
        //  Class methods
        //
        //--------------------------------------------------------------------------
        
        /**
         *  Registers the delegate class for a component class with automation manager.
         *  
         *  @param root The SystemManger of the application.
         *  
         *  @langversion 3.0
         *  @playerversion Flash 9
         *  @playerversion AIR 1.1
         *  @productversion Flex 3
         */
        public static function init(root:DisplayObject):void
        {
            Automation.registerDelegateClass(ContainerMovieClip, ContainerMovieClipAutomationImpl);
        }   
        
        //--------------------------------------------------------------------------
        //
        //  Constructor
        //
        //--------------------------------------------------------------------------
        
        /**
         *  Constructor.
         * @param obj Panel object to be automated.     
         *  
         *  @langversion 3.0
         *  @playerversion Flash 9
         *  @playerversion AIR 1.1
         *  @productversion Flex 3
         */
        public function ContainerMovieClipAutomationImpl(obj:ContainerMovieClip)
        {
            super(obj);
            recordClick = true;
        }
        
        
        /**
         *  @private
         *  storage for the owner component
         */
        protected function get containerMovieClip():ContainerMovieClip
        {
            return movieClip as ContainerMovieClip;
        }
        
        //--------------------------------------------------------------------------
        //
        //  Overridden properties
        //
        //--------------------------------------------------------------------------
        
        //----------------------------------
        //  automationName
        //----------------------------------
        
        /**
         *  @private
         */
        override public function get automationName():String
        {
            return super.automationName;
        }
        
        /**
         *  @private
         */
        override public function get automationValue():Array
        {
            return [ automationName ];
        }
        
        //----------------------------------
        //  numAutomationChildren
        //----------------------------------
        
        /**
         *  @private
         */
        override public function get numAutomationChildren():int
        {
            // Always the Flash container can have only one child which is the 
            // Flex ContentHolder. It is always like this.
            // So there is only automationChild for the ContainerMovieClip 
            return 1;
        }
        
        //--------------------------------------------------------------------------
        //
        //  Overridden methods
        //
        //--------------------------------------------------------------------------
        
        /**
         *  @private
         */
        override public function getAutomationChildAt(index:int):IAutomationObject
        {
            // there is only one AutomationChild for the CotnainerMoovieClip
            // which is FlexContentHolder
            // there is no mehtod to get this directly. Content reurns the flex object 
            // which is added to the FlexContentHolder. So we need to get the child by 
            // getting the parent of the the content.
            // once we have a direct method in UIMovieClip to get the FlexContent holder
            // we need to call that
            if (index == 0)
            {
                var contentObj:IUIComponent = containerMovieClip.content as IUIComponent;
                return contentObj.parent as IAutomationObject;
            }
            
            return null;
        }
        
        /**
         *  @private
         */
        override public function getAutomationChildren():Array
        {
            // there is only one AutomationChild for the CotnainerMoovieClip
            // which is FlexContentHolder
            // there is no mehtod to get this directly. Content reurns the flex object 
            // which is added to the FlexContentHolder. So we need to get the child by 
            // getting the parent of the the content.
            // once we have a direct method in UIMovieClip to get the FlexContent holder
            // we need to call that
            var contentObj:IUIComponent = containerMovieClip.content as IUIComponent;
            return [contentObj.parent as IAutomationObject];
        }
        
        /**
         *  @private
         */
        override public function createAutomationIDPart(child:IAutomationObject):Object
        {
            var help:IAutomationObjectHelper = Automation.automationObjectHelper;
            return help.helpCreateIDPart(uiAutomationObject, child);
        }
        
        /**
         *  @private
         */
        override public function createAutomationIDPartWithRequiredProperties(child:IAutomationObject, properties:Array):Object
        {
            var help:IAutomationObjectHelper = Automation.automationObjectHelper;
            return help.helpCreateIDPartWithRequiredProperties(uiAutomationObject, child,properties);
        }
        
        /**
         *  @private
         */
        override public function resolveAutomationIDPart(part:Object):Array
        {
            var help:IAutomationObjectHelper = Automation.automationObjectHelper;
            return help.helpResolveIDPart(uiAutomationObject, part);
        }
    }
}