package 
{

import mx.core.IFlexModuleFactory;
import mx.core.mx_internal;
import mx.styles.CSSCondition;
import mx.styles.CSSSelector;
import mx.styles.CSSStyleDeclaration;
import mx.styles.IStyleManager2;
import mx.utils.ObjectUtil;
import spark.skins.spark.FocusSkin;
import mx.core.UITextField;
import spark.skins.spark.ImageSkin;
import mx.skins.halo.ToolTipBorder;
import spark.skins.spark.DefaultButtonSkin;
import spark.skins.spark.ButtonSkin;
import spark.components.supportClasses.ListItemDragProxy;
import spark.skins.spark.SkinnableContainerSkin;
import spark.skins.spark.SkinnableDataContainerSkin;
import mx.skins.halo.DefaultDragImage;
import spark.skins.spark.DataGridSkin;
import spark.skins.spark.ErrorSkin;
import spark.skins.spark.VScrollBarSkin;
import spark.skins.spark.HScrollBarSkin;
import spark.skins.spark.ListSkin;
import spark.skins.spark.TextAreaSkin;
import spark.skins.spark.ScrollerSkin;
import spark.skins.spark.ApplicationSkin;
import mx.skins.halo.HaloFocusRect;
import spark.skins.spark.ListDropIndicator;
import mx.skins.halo.BusyCursor;
[ExcludeClass]

public class _FlexGrocer_Styles
{
    [Embed(_resolvedSource='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$Assets.swf', symbol='cursorStretch', source='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$Assets.swf', original='Assets.swf', _line='65', _pathsep='true', _file='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/spark.swc$defaults.css')]
    private static var _embed_css_Assets_swf__70569616_cursorStretch_1469755830:Class;
    [Embed(_resolvedSource='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$Assets.swf', symbol='mx.skins.cursor.DragMove', source='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$Assets.swf', original='Assets.swf', _line='208', _pathsep='true', _file='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$defaults.css')]
    private static var _embed_css_Assets_swf__70569616_mx_skins_cursor_DragMove_810132749:Class;
    [Embed(_resolvedSource='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$Assets.swf', symbol='mx.skins.cursor.DragLink', source='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$Assets.swf', original='Assets.swf', _line='207', _pathsep='true', _file='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$defaults.css')]
    private static var _embed_css_Assets_swf__70569616_mx_skins_cursor_DragLink_810107174:Class;
    [Embed(_resolvedSource='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$Assets.swf', symbol='mx.skins.cursor.DragCopy', source='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$Assets.swf', original='Assets.swf', _line='205', _pathsep='true', _file='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$defaults.css')]
    private static var _embed_css_Assets_swf__70569616_mx_skins_cursor_DragCopy_809845169:Class;
    [Embed(_resolvedSource='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$Assets.swf', symbol='mx.skins.cursor.DragReject', source='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$Assets.swf', original='Assets.swf', _line='209', _pathsep='true', _file='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$defaults.css')]
    private static var _embed_css_Assets_swf__70569616_mx_skins_cursor_DragReject_677407365:Class;
    [Embed(_resolvedSource='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$Assets.swf', symbol='mx.skins.cursor.BusyCursor', source='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$Assets.swf', original='Assets.swf', _line='194', _pathsep='true', _file='C:/Program Files (x86)/Adobe/Adobe Flash Builder 4.6/sdks/4.6.0/frameworks/libs/framework.swc$defaults.css')]
    private static var _embed_css_Assets_swf__70569616_mx_skins_cursor_BusyCursor_491665735:Class;
    public static function init(fbs:IFlexModuleFactory):void
    {
        var styleManager:IStyleManager2 = fbs.getImplementation("mx.styles::IStyleManager2") as IStyleManager2;
        

        var conditions:Array = null;
        var condition:CSSCondition = null;
        var selector:CSSSelector = null;
        var style:CSSStyleDeclaration;
        var effects:Array;
        
        var mergedStyle:CSSStyleDeclaration;

        
        //
        // spark.components.Application
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.Application", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.Application");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.backgroundColor = 0xffffff;
                this.skinClass = spark.skins.spark.ApplicationSkin;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.Button
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.Button", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.Button");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.skinClass = spark.skins.spark.ButtonSkin;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }

        //
        // spark.components.Button.emphasized
        //
        selector = null;
        conditions = null;
        conditions = [];
        condition = new CSSCondition("class", "emphasized");
        conditions.push(condition); 
        selector = new CSSSelector("spark.components.Button", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.Button.emphasized");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.skinClass = spark.skins.spark.DefaultButtonSkin;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.DataGrid
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.DataGrid", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.DataGrid");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.stretchCursor = _embed_css_Assets_swf__70569616_cursorStretch_1469755830;
                this.skinClass = spark.skins.spark.DataGridSkin;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.GridColumnHeaderGroup
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.GridColumnHeaderGroup", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.GridColumnHeaderGroup");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.separatorAffordance = 5;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.HScrollBar
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.HScrollBar", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.HScrollBar");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.skinClass = spark.skins.spark.HScrollBarSkin;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.Image
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.Image", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.Image");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.smoothingQuality = "default";
                this.skinClass = spark.skins.spark.ImageSkin;
                this.showErrorSkin = false;
                this.enableLoadingState = false;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.List
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.List", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.List");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.dragIndicatorClass = spark.components.supportClasses.ListItemDragProxy;
                this.skinClass = spark.skins.spark.ListSkin;
                this.dropIndicatorSkin = spark.skins.spark.ListDropIndicator;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.RichEditableText
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.RichEditableText", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.RichEditableText");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.layoutDirection = "ltr";
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.Scroller
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.Scroller", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.Scroller");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.skinClass = spark.skins.spark.ScrollerSkin;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.SkinnableDataContainer
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.SkinnableDataContainer", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.SkinnableDataContainer");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.skinClass = spark.skins.spark.SkinnableDataContainerSkin;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.supportClasses.SkinnableComponent
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.supportClasses.SkinnableComponent", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.supportClasses.SkinnableComponent");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.focusSkin = spark.skins.spark.FocusSkin;
                this.errorSkin = spark.skins.spark.ErrorSkin;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.SkinnableContainer
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.SkinnableContainer", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.SkinnableContainer");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.skinClass = spark.skins.spark.SkinnableContainerSkin;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.supportClasses.SkinnableTextBase:normalWithPrompt
        //
        selector = null;
        conditions = null;
        conditions = [];
        condition = new CSSCondition("pseudo", "normalWithPrompt");
        conditions.push(condition); 
        selector = new CSSSelector("spark.components.supportClasses.SkinnableTextBase", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.supportClasses.SkinnableTextBase:normalWithPrompt");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.color = 0xbababa;
                this.fontStyle = "italic";
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }

        //
        // spark.components.supportClasses.SkinnableTextBase:disabledWithPrompt
        //
        selector = null;
        conditions = null;
        conditions = [];
        condition = new CSSCondition("pseudo", "disabledWithPrompt");
        conditions.push(condition); 
        selector = new CSSSelector("spark.components.supportClasses.SkinnableTextBase", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.supportClasses.SkinnableTextBase:disabledWithPrompt");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.color = 0xbababa;
                this.fontStyle = "italic";
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.supportClasses.TextBase
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.supportClasses.TextBase", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.supportClasses.TextBase");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.layoutDirection = "ltr";
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.TextArea
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.TextArea", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.TextArea");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.paddingTop = 5;
                this.skinClass = spark.skins.spark.TextAreaSkin;
                this.paddingLeft = 3;
                this.paddingBottom = 3;
                this.paddingRight = 3;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // spark.components.VScrollBar
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("spark.components.VScrollBar", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("spark.components.VScrollBar");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.skinClass = spark.skins.spark.VScrollBarSkin;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // global
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("global", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("global");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.lineHeight = "120%";
                this.unfocusedTextSelectionColor = 0xe8e8e8;
                this.kerning = "default";
                this.caretColor = 0x0167ff;
                this.iconColor = 0x111111;
                this.verticalScrollPolicy = "auto";
                this.horizontalAlign = "left";
                this.filled = true;
                this.showErrorTip = true;
                this.textDecoration = "none";
                this.columnCount = "auto";
                this.liveDragging = true;
                this.dominantBaseline = "auto";
                this.fontThickness = 0;
                this.focusBlendMode = "normal";
                this.blockProgression = "tb";
                this.buttonColor = 0x6f7777;
                this.indentation = 17;
                this.autoThumbVisibility = true;
                this.textAlignLast = "start";
                this.paddingTop = 0;
                this.textAlpha = 1.0;
                this.chromeColor = 0xcccccc;
                this.rollOverColor = 0xcedbef;
                this.bevel = true;
                this.fontSize = 12;
                this.shadowColor = 0xeeeeee;
                this.columnGap = 20;
                this.paddingLeft = 0;
                this.paragraphEndIndent = 0;
                this.fontWeight = "normal";
                this.indicatorGap = 14;
                this.focusSkin = mx.skins.halo.HaloFocusRect;
                this.breakOpportunity = "auto";
                this.leading = 2;
                this.symbolColor = 0x000000;
                this.renderingMode = "cff";
                this.iconPlacement = "left";
                this.borderThickness = 1;
                this.paragraphStartIndent = 0;
                this.layoutDirection = "ltr";
                this.contentBackgroundColor = 0xffffff;
                this.backgroundSize = "auto";
                this.paragraphSpaceAfter = 0;
                this.borderColor = 0x696969;
                this.shadowDistance = 2;
                this.stroked = false;
                this.digitWidth = "default";
                this.verticalAlign = "top";
                this.ligatureLevel = "common";
                this.firstBaselineOffset = "auto";
                this.fillAlphas = [0.6, 0.4, 0.75, 0.65];
                this.version = "4.0.0";
                this.shadowDirection = "center";
                this.fontLookup = "embeddedCFF";
                this.lineBreak = "toFit";
                this.repeatInterval = 35;
                this.openDuration = 1;
                this.paragraphSpaceBefore = 0;
                this.fontFamily = "Arial";
                this.paddingBottom = 0;
                this.strokeWidth = 1;
                this.lineThrough = false;
                this.textFieldClass = mx.core.UITextField;
                this.alignmentBaseline = "useDominantBaseline";
                this.trackingLeft = 0;
                this.verticalGridLines = true;
                this.fontStyle = "normal";
                this.dropShadowColor = 0x000000;
                this.accentColor = 0x0099ff;
                this.backgroundImageFillMode = "scale";
                this.selectionColor = 0xa8c6ee;
                this.borderWeight = 1;
                this.focusRoundedCorners = "tl tr bl br";
                this.paddingRight = 0;
                this.borderSides = "left top right bottom";
                this.disabledIconColor = 0x999999;
                this.textJustify = "interWord";
                this.focusColor = 0x70b2ee;
                this.borderVisible = true;
                this.selectionDuration = 250;
                this.typographicCase = "default";
                this.highlightAlphas = [0.3, 0];
                this.fillColor = 0xffffff;
                this.showErrorSkin = true;
                this.textRollOverColor = 0;
                this.rollOverOpenDelay = 200;
                this.digitCase = "default";
                this.shadowCapColor = 0xd5dddd;
                this.inactiveTextSelectionColor = 0xe8e8e8;
                this.backgroundAlpha = 1.0;
                this.justificationRule = "auto";
                this.roundedBottomCorners = true;
                this.dropShadowVisible = false;
                this.softKeyboardEffectDuration = 150;
                this.trackingRight = 0;
                this.fillColors = [0xffffff, 0xcccccc, 0xffffff, 0xeeeeee];
                this.horizontalGap = 8;
                this.borderCapColor = 0x919999;
                this.leadingModel = "auto";
                this.selectionDisabledColor = 0xdddddd;
                this.closeDuration = 50;
                this.embedFonts = false;
                this.letterSpacing = 0;
                this.focusAlpha = 0.55;
                this.borderAlpha = 1.0;
                this.baselineShift = 0;
                this.focusedTextSelectionColor = 0xa8c6ee;
                this.fontSharpness = 0;
                this.modalTransparencyDuration = 100;
                this.justificationStyle = "auto";
                this.contentBackgroundAlpha = 1;
                this.borderStyle = "inset";
                this.textRotation = "auto";
                this.fontAntiAliasType = "advanced";
                this.errorColor = 0xfe0000;
                this.direction = "ltr";
                this.cffHinting = "horizontalStem";
                this.horizontalGridLineColor = 0xf7f7f7;
                this.locale = "en";
                this.cornerRadius = 2;
                this.modalTransparencyColor = 0xdddddd;
                this.disabledAlpha = 0.5;
                this.textIndent = 0;
                this.verticalGridLineColor = 0xd5dddd;
                this.themeColor = 0x70b2ee;
                this.tabStops = null;
                this.modalTransparency = 0.5;
                this.smoothScrolling = true;
                this.columnWidth = "auto";
                this.textAlign = "start";
                this.horizontalScrollPolicy = "auto";
                this.textSelectedColor = 0;
                this.interactionMode = "mouse";
                this.whiteSpaceCollapse = "collapse";
                this.fontGridFitType = "pixel";
                this.horizontalGridLines = false;
                this.fullScreenHideControlsDelay = 3000;
                this.useRollOver = true;
                this.repeatDelay = 500;
                this.focusThickness = 2;
                this.verticalGap = 6;
                this.disabledColor = 0xaab3b3;
                this.modalTransparencyBlur = 3;
                this.slideDuration = 300;
                this.color = 0x000000;
                this.fixedThumbSize = false;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }

        //
        // .errorTip
        //
        selector = null;
        conditions = null;
        conditions = [];
        condition = new CSSCondition("class", "errorTip");
        conditions.push(condition); 
        selector = new CSSSelector("", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration(".errorTip");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.fontWeight = "bold";
                this.borderStyle = "errorTipRight";
                this.paddingTop = 4;
                this.borderColor = 0xce2929;
                this.color = 0xffffff;
                this.fontSize = 10;
                this.shadowColor = 0x000000;
                this.paddingLeft = 4;
                this.paddingBottom = 4;
                this.paddingRight = 4;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }

        //
        // .headerDragProxyStyle
        //
        selector = null;
        conditions = null;
        conditions = [];
        condition = new CSSCondition("class", "headerDragProxyStyle");
        conditions.push(condition); 
        selector = new CSSSelector("", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration(".headerDragProxyStyle");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.fontWeight = "bold";
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // mx.managers.CursorManager
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("mx.managers.CursorManager", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("mx.managers.CursorManager");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.busyCursor = mx.skins.halo.BusyCursor;
                this.busyCursorBackground = _embed_css_Assets_swf__70569616_mx_skins_cursor_BusyCursor_491665735;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // mx.managers.DragManager
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("mx.managers.DragManager", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("mx.managers.DragManager");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.copyCursor = _embed_css_Assets_swf__70569616_mx_skins_cursor_DragCopy_809845169;
                this.moveCursor = _embed_css_Assets_swf__70569616_mx_skins_cursor_DragMove_810132749;
                this.rejectCursor = _embed_css_Assets_swf__70569616_mx_skins_cursor_DragReject_677407365;
                this.linkCursor = _embed_css_Assets_swf__70569616_mx_skins_cursor_DragLink_810107174;
                this.defaultDragImageSkin = mx.skins.halo.DefaultDragImage;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }



        
        //
        // mx.controls.ToolTip
        //
        selector = null;
        conditions = null;
        conditions = null;
        selector = new CSSSelector("mx.controls.ToolTip", conditions, selector);
        mergedStyle = styleManager.getMergedStyleDeclaration("mx.controls.ToolTip");
        style = new CSSStyleDeclaration(selector, styleManager, mergedStyle == null);

        if (style.defaultFactory == null)
        {
            style.defaultFactory = function():void
            {
                this.borderStyle = "toolTip";
                this.paddingTop = 2;
                this.borderColor = 0x919999;
                this.backgroundColor = 0xffffcc;
                this.borderSkin = mx.skins.halo.ToolTipBorder;
                this.cornerRadius = 2;
                this.fontSize = 10;
                this.paddingLeft = 4;
                this.paddingBottom = 2;
                this.backgroundAlpha = 0.95;
                this.paddingRight = 4;
            };
        }



        if (mergedStyle != null && 
            (mergedStyle.defaultFactory == null ||
            ObjectUtil.compare(new style.defaultFactory(), new mergedStyle.defaultFactory())))
        {
            styleManager.setStyleDeclaration(style.mx_internal::selectorString, style, false);
        }


    }
}

}