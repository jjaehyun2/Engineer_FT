package {
import flash.display.DisplayObject;
import flash.utils.*;
import mx.core.IFlexModuleFactory;
import mx.styles.IStyleManager2;
import mx.events.Request;
import mx.styles.StyleManagerImpl;
import mx.managers.systemClasses.ChildManager;
import mx.core.TextFieldFactory; TextFieldFactory;
import flash.system.*
import spark.accessibility.RichEditableTextAccImpl;
import spark.accessibility.TextBaseAccImpl;
import spark.accessibility.ListAccImpl;
import spark.accessibility.DataGridAccImpl;
import mx.accessibility.UIComponentAccProps;
import spark.accessibility.ButtonBaseAccImpl;
import spark.accessibility.ListBaseAccImpl;
import flash.net.registerClassAlias;
import flash.net.getClassByAlias;
import mx.managers.SystemManagerGlobals;
import mx.resources.ResourceManager;
import mx.collections.ArrayCollection;
import mx.collections.ArrayList;
import mx.messaging.config.ConfigMap;
import mx.messaging.messages.AcknowledgeMessage;
import mx.messaging.messages.AcknowledgeMessageExt;
import mx.messaging.messages.AsyncMessage;
import mx.messaging.messages.AsyncMessageExt;
import mx.messaging.messages.CommandMessage;
import mx.messaging.messages.CommandMessageExt;
import mx.messaging.messages.ErrorMessage;
import mx.messaging.messages.HTTPRequestMessage;
import mx.messaging.messages.MessagePerformanceInfo;
import mx.utils.ObjectProxy;
import mx.effects.EffectManager;
import mx.core.mx_internal;
[ResourceBundle("collections")]
[ResourceBundle("components")]
[ResourceBundle("core")]
[ResourceBundle("effects")]
[ResourceBundle("layout")]
[ResourceBundle("logging")]
[ResourceBundle("messaging")]
[ResourceBundle("rpc")]
[ResourceBundle("skins")]
[ResourceBundle("sparkEffects")]
[ResourceBundle("styles")]
[ResourceBundle("textLayout")]

[Mixin]
public class _FlexGrocer_FlexInit
{
   public function _FlexGrocer_FlexInit()
   {
       super();
   }
   public static function init(fbs:IFlexModuleFactory):void
   {
       new ChildManager(fbs);
       var styleManager:IStyleManager2;
       styleManager = new StyleManagerImpl(fbs);
       EffectManager.mx_internal::registerEffectTrigger("addedEffect", "added");
       EffectManager.mx_internal::registerEffectTrigger("creationCompleteEffect", "creationComplete");
       EffectManager.mx_internal::registerEffectTrigger("focusInEffect", "focusIn");
       EffectManager.mx_internal::registerEffectTrigger("focusOutEffect", "focusOut");
       EffectManager.mx_internal::registerEffectTrigger("hideEffect", "hide");
       EffectManager.mx_internal::registerEffectTrigger("mouseDownEffect", "mouseDown");
       EffectManager.mx_internal::registerEffectTrigger("mouseUpEffect", "mouseUp");
       EffectManager.mx_internal::registerEffectTrigger("moveEffect", "move");
       EffectManager.mx_internal::registerEffectTrigger("removedEffect", "removed");
       EffectManager.mx_internal::registerEffectTrigger("resizeEffect", "resize");
       EffectManager.mx_internal::registerEffectTrigger("rollOutEffect", "rollOut");
       EffectManager.mx_internal::registerEffectTrigger("rollOverEffect", "rollOver");
       EffectManager.mx_internal::registerEffectTrigger("showEffect", "show");
       // trace("Flex accessibility startup: " + Capabilities.hasAccessibility);
       if (Capabilities.hasAccessibility) {
          spark.accessibility.RichEditableTextAccImpl.enableAccessibility();
          spark.accessibility.TextBaseAccImpl.enableAccessibility();
          spark.accessibility.ListAccImpl.enableAccessibility();
          spark.accessibility.DataGridAccImpl.enableAccessibility();
          mx.accessibility.UIComponentAccProps.enableAccessibility();
          spark.accessibility.ButtonBaseAccImpl.enableAccessibility();
          spark.accessibility.ListBaseAccImpl.enableAccessibility();
       }
       // mx.collections.ArrayCollection
       try 
       { 
           if (flash.net.getClassByAlias("flex.messaging.io.ArrayCollection") != mx.collections.ArrayCollection) 
           { 
               flash.net.registerClassAlias("flex.messaging.io.ArrayCollection", mx.collections.ArrayCollection); 
               if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
               { 
                   trace(ResourceManager.getInstance().getString( "core", 
                         "remoteClassMemoryLeak",
                         ["mx.collections.ArrayCollection","FlexGrocer","_FlexGrocer_FlexInit"]));
               } 
           } 
       } 
       catch (e:Error) 
       { 
           flash.net.registerClassAlias("flex.messaging.io.ArrayCollection", mx.collections.ArrayCollection); 
           if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
           { 
               trace(ResourceManager.getInstance().getString( "core", 
                     "remoteClassMemoryLeak",
                     ["mx.collections.ArrayCollection","FlexGrocer","_FlexGrocer_FlexInit"]));
           } 
       } 

       // mx.collections.ArrayList
       try 
       { 
           if (flash.net.getClassByAlias("flex.messaging.io.ArrayList") != mx.collections.ArrayList) 
           { 
               flash.net.registerClassAlias("flex.messaging.io.ArrayList", mx.collections.ArrayList); 
               if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
               { 
                   trace(ResourceManager.getInstance().getString( "core", 
                         "remoteClassMemoryLeak",
                         ["mx.collections.ArrayList","FlexGrocer","_FlexGrocer_FlexInit"]));
               } 
           } 
       } 
       catch (e:Error) 
       { 
           flash.net.registerClassAlias("flex.messaging.io.ArrayList", mx.collections.ArrayList); 
           if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
           { 
               trace(ResourceManager.getInstance().getString( "core", 
                     "remoteClassMemoryLeak",
                     ["mx.collections.ArrayList","FlexGrocer","_FlexGrocer_FlexInit"]));
           } 
       } 

       // mx.messaging.config.ConfigMap
       try 
       { 
           if (flash.net.getClassByAlias("flex.messaging.config.ConfigMap") != mx.messaging.config.ConfigMap) 
           { 
               flash.net.registerClassAlias("flex.messaging.config.ConfigMap", mx.messaging.config.ConfigMap); 
               if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
               { 
                   trace(ResourceManager.getInstance().getString( "core", 
                         "remoteClassMemoryLeak",
                         ["mx.messaging.config.ConfigMap","FlexGrocer","_FlexGrocer_FlexInit"]));
               } 
           } 
       } 
       catch (e:Error) 
       { 
           flash.net.registerClassAlias("flex.messaging.config.ConfigMap", mx.messaging.config.ConfigMap); 
           if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
           { 
               trace(ResourceManager.getInstance().getString( "core", 
                     "remoteClassMemoryLeak",
                     ["mx.messaging.config.ConfigMap","FlexGrocer","_FlexGrocer_FlexInit"]));
           } 
       } 

       // mx.messaging.messages.AcknowledgeMessage
       try 
       { 
           if (flash.net.getClassByAlias("flex.messaging.messages.AcknowledgeMessage") != mx.messaging.messages.AcknowledgeMessage) 
           { 
               flash.net.registerClassAlias("flex.messaging.messages.AcknowledgeMessage", mx.messaging.messages.AcknowledgeMessage); 
               if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
               { 
                   trace(ResourceManager.getInstance().getString( "core", 
                         "remoteClassMemoryLeak",
                         ["mx.messaging.messages.AcknowledgeMessage","FlexGrocer","_FlexGrocer_FlexInit"]));
               } 
           } 
       } 
       catch (e:Error) 
       { 
           flash.net.registerClassAlias("flex.messaging.messages.AcknowledgeMessage", mx.messaging.messages.AcknowledgeMessage); 
           if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
           { 
               trace(ResourceManager.getInstance().getString( "core", 
                     "remoteClassMemoryLeak",
                     ["mx.messaging.messages.AcknowledgeMessage","FlexGrocer","_FlexGrocer_FlexInit"]));
           } 
       } 

       // mx.messaging.messages.AcknowledgeMessageExt
       try 
       { 
           if (flash.net.getClassByAlias("DSK") != mx.messaging.messages.AcknowledgeMessageExt) 
           { 
               flash.net.registerClassAlias("DSK", mx.messaging.messages.AcknowledgeMessageExt); 
               if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
               { 
                   trace(ResourceManager.getInstance().getString( "core", 
                         "remoteClassMemoryLeak",
                         ["mx.messaging.messages.AcknowledgeMessageExt","FlexGrocer","_FlexGrocer_FlexInit"]));
               } 
           } 
       } 
       catch (e:Error) 
       { 
           flash.net.registerClassAlias("DSK", mx.messaging.messages.AcknowledgeMessageExt); 
           if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
           { 
               trace(ResourceManager.getInstance().getString( "core", 
                     "remoteClassMemoryLeak",
                     ["mx.messaging.messages.AcknowledgeMessageExt","FlexGrocer","_FlexGrocer_FlexInit"]));
           } 
       } 

       // mx.messaging.messages.AsyncMessage
       try 
       { 
           if (flash.net.getClassByAlias("flex.messaging.messages.AsyncMessage") != mx.messaging.messages.AsyncMessage) 
           { 
               flash.net.registerClassAlias("flex.messaging.messages.AsyncMessage", mx.messaging.messages.AsyncMessage); 
               if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
               { 
                   trace(ResourceManager.getInstance().getString( "core", 
                         "remoteClassMemoryLeak",
                         ["mx.messaging.messages.AsyncMessage","FlexGrocer","_FlexGrocer_FlexInit"]));
               } 
           } 
       } 
       catch (e:Error) 
       { 
           flash.net.registerClassAlias("flex.messaging.messages.AsyncMessage", mx.messaging.messages.AsyncMessage); 
           if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
           { 
               trace(ResourceManager.getInstance().getString( "core", 
                     "remoteClassMemoryLeak",
                     ["mx.messaging.messages.AsyncMessage","FlexGrocer","_FlexGrocer_FlexInit"]));
           } 
       } 

       // mx.messaging.messages.AsyncMessageExt
       try 
       { 
           if (flash.net.getClassByAlias("DSA") != mx.messaging.messages.AsyncMessageExt) 
           { 
               flash.net.registerClassAlias("DSA", mx.messaging.messages.AsyncMessageExt); 
               if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
               { 
                   trace(ResourceManager.getInstance().getString( "core", 
                         "remoteClassMemoryLeak",
                         ["mx.messaging.messages.AsyncMessageExt","FlexGrocer","_FlexGrocer_FlexInit"]));
               } 
           } 
       } 
       catch (e:Error) 
       { 
           flash.net.registerClassAlias("DSA", mx.messaging.messages.AsyncMessageExt); 
           if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
           { 
               trace(ResourceManager.getInstance().getString( "core", 
                     "remoteClassMemoryLeak",
                     ["mx.messaging.messages.AsyncMessageExt","FlexGrocer","_FlexGrocer_FlexInit"]));
           } 
       } 

       // mx.messaging.messages.CommandMessage
       try 
       { 
           if (flash.net.getClassByAlias("flex.messaging.messages.CommandMessage") != mx.messaging.messages.CommandMessage) 
           { 
               flash.net.registerClassAlias("flex.messaging.messages.CommandMessage", mx.messaging.messages.CommandMessage); 
               if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
               { 
                   trace(ResourceManager.getInstance().getString( "core", 
                         "remoteClassMemoryLeak",
                         ["mx.messaging.messages.CommandMessage","FlexGrocer","_FlexGrocer_FlexInit"]));
               } 
           } 
       } 
       catch (e:Error) 
       { 
           flash.net.registerClassAlias("flex.messaging.messages.CommandMessage", mx.messaging.messages.CommandMessage); 
           if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
           { 
               trace(ResourceManager.getInstance().getString( "core", 
                     "remoteClassMemoryLeak",
                     ["mx.messaging.messages.CommandMessage","FlexGrocer","_FlexGrocer_FlexInit"]));
           } 
       } 

       // mx.messaging.messages.CommandMessageExt
       try 
       { 
           if (flash.net.getClassByAlias("DSC") != mx.messaging.messages.CommandMessageExt) 
           { 
               flash.net.registerClassAlias("DSC", mx.messaging.messages.CommandMessageExt); 
               if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
               { 
                   trace(ResourceManager.getInstance().getString( "core", 
                         "remoteClassMemoryLeak",
                         ["mx.messaging.messages.CommandMessageExt","FlexGrocer","_FlexGrocer_FlexInit"]));
               } 
           } 
       } 
       catch (e:Error) 
       { 
           flash.net.registerClassAlias("DSC", mx.messaging.messages.CommandMessageExt); 
           if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
           { 
               trace(ResourceManager.getInstance().getString( "core", 
                     "remoteClassMemoryLeak",
                     ["mx.messaging.messages.CommandMessageExt","FlexGrocer","_FlexGrocer_FlexInit"]));
           } 
       } 

       // mx.messaging.messages.ErrorMessage
       try 
       { 
           if (flash.net.getClassByAlias("flex.messaging.messages.ErrorMessage") != mx.messaging.messages.ErrorMessage) 
           { 
               flash.net.registerClassAlias("flex.messaging.messages.ErrorMessage", mx.messaging.messages.ErrorMessage); 
               if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
               { 
                   trace(ResourceManager.getInstance().getString( "core", 
                         "remoteClassMemoryLeak",
                         ["mx.messaging.messages.ErrorMessage","FlexGrocer","_FlexGrocer_FlexInit"]));
               } 
           } 
       } 
       catch (e:Error) 
       { 
           flash.net.registerClassAlias("flex.messaging.messages.ErrorMessage", mx.messaging.messages.ErrorMessage); 
           if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
           { 
               trace(ResourceManager.getInstance().getString( "core", 
                     "remoteClassMemoryLeak",
                     ["mx.messaging.messages.ErrorMessage","FlexGrocer","_FlexGrocer_FlexInit"]));
           } 
       } 

       // mx.messaging.messages.HTTPRequestMessage
       try 
       { 
           if (flash.net.getClassByAlias("flex.messaging.messages.HTTPMessage") != mx.messaging.messages.HTTPRequestMessage) 
           { 
               flash.net.registerClassAlias("flex.messaging.messages.HTTPMessage", mx.messaging.messages.HTTPRequestMessage); 
               if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
               { 
                   trace(ResourceManager.getInstance().getString( "core", 
                         "remoteClassMemoryLeak",
                         ["mx.messaging.messages.HTTPRequestMessage","FlexGrocer","_FlexGrocer_FlexInit"]));
               } 
           } 
       } 
       catch (e:Error) 
       { 
           flash.net.registerClassAlias("flex.messaging.messages.HTTPMessage", mx.messaging.messages.HTTPRequestMessage); 
           if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
           { 
               trace(ResourceManager.getInstance().getString( "core", 
                     "remoteClassMemoryLeak",
                     ["mx.messaging.messages.HTTPRequestMessage","FlexGrocer","_FlexGrocer_FlexInit"]));
           } 
       } 

       // mx.messaging.messages.MessagePerformanceInfo
       try 
       { 
           if (flash.net.getClassByAlias("flex.messaging.messages.MessagePerformanceInfo") != mx.messaging.messages.MessagePerformanceInfo) 
           { 
               flash.net.registerClassAlias("flex.messaging.messages.MessagePerformanceInfo", mx.messaging.messages.MessagePerformanceInfo); 
               if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
               { 
                   trace(ResourceManager.getInstance().getString( "core", 
                         "remoteClassMemoryLeak",
                         ["mx.messaging.messages.MessagePerformanceInfo","FlexGrocer","_FlexGrocer_FlexInit"]));
               } 
           } 
       } 
       catch (e:Error) 
       { 
           flash.net.registerClassAlias("flex.messaging.messages.MessagePerformanceInfo", mx.messaging.messages.MessagePerformanceInfo); 
           if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
           { 
               trace(ResourceManager.getInstance().getString( "core", 
                     "remoteClassMemoryLeak",
                     ["mx.messaging.messages.MessagePerformanceInfo","FlexGrocer","_FlexGrocer_FlexInit"]));
           } 
       } 

       // mx.utils.ObjectProxy
       try 
       { 
           if (flash.net.getClassByAlias("flex.messaging.io.ObjectProxy") != mx.utils.ObjectProxy) 
           { 
               flash.net.registerClassAlias("flex.messaging.io.ObjectProxy", mx.utils.ObjectProxy); 
               if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
               { 
                   trace(ResourceManager.getInstance().getString( "core", 
                         "remoteClassMemoryLeak",
                         ["mx.utils.ObjectProxy","FlexGrocer","_FlexGrocer_FlexInit"]));
               } 
           } 
       } 
       catch (e:Error) 
       { 
           flash.net.registerClassAlias("flex.messaging.io.ObjectProxy", mx.utils.ObjectProxy); 
           if (fbs != SystemManagerGlobals.topLevelSystemManagers[0]) 
           { 
               trace(ResourceManager.getInstance().getString( "core", 
                     "remoteClassMemoryLeak",
                     ["mx.utils.ObjectProxy","FlexGrocer","_FlexGrocer_FlexInit"]));
           } 
       } 

       var styleNames:Array = ["lineHeight", "unfocusedTextSelectionColor", "kerning", "caretColor", "showErrorSkin", "digitCase", "inactiveTextSelectionColor", "listAutoPadding", "showErrorTip", "justificationRule", "textDecoration", "dominantBaseline", "fontThickness", "textShadowColor", "trackingRight", "blockProgression", "leadingModel", "listStylePosition", "textAlignLast", "textShadowAlpha", "textAlpha", "letterSpacing", "chromeColor", "rollOverColor", "fontSize", "baselineShift", "focusedTextSelectionColor", "paragraphEndIndent", "fontWeight", "breakOpportunity", "leading", "symbolColor", "renderingMode", "fontSharpness", "paragraphStartIndent", "layoutDirection", "justificationStyle", "wordSpacing", "listStyleType", "contentBackgroundColor", "paragraphSpaceAfter", "contentBackgroundAlpha", "fontAntiAliasType", "textRotation", "errorColor", "cffHinting", "direction", "locale", "backgroundDisabledColor", "digitWidth", "showPromptWhenFocused", "touchDelay", "ligatureLevel", "textIndent", "firstBaselineOffset", "themeColor", "clearFloats", "fontLookup", "tabStops", "paragraphSpaceBefore", "textAlign", "fontFamily", "interactionMode", "lineThrough", "whiteSpaceCollapse", "fontGridFitType", "alignmentBaseline", "trackingLeft", "fontStyle", "dropShadowColor", "accentColor", "selectionColor", "disabledColor", "downColor", "focusColor", "textJustify", "color", "alternatingItemColors", "typographicCase"];

       for (var i:int = 0; i < styleNames.length; i++)
       {
          styleManager.registerInheritingStyle(styleNames[i]);
       }
   }
}  // FlexInit
}  // package