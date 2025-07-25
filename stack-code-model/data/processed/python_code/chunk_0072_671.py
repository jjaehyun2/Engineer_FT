/*
Feathers
Copyright 2012-2015 Bowler Hat LLC. All Rights Reserved.

This program is free software. You can redistribute and/or modify it in
accordance with the terms of the accompanying license agreement.
*/
package feathers.controls.text
{
	import feathers.core.FeathersControl;
	import feathers.core.IStateContext;
	import feathers.core.IStateObserver;
	import feathers.core.ITextRenderer;
	import feathers.core.IToggle;
	import feathers.events.FeathersEventType;
	import feathers.skins.IStyleProvider;
	import feathers.utils.geom.matrixToScaleX;
	import feathers.utils.geom.matrixToScaleY;

	import flash.display.BitmapData;
	import flash.display3D.Context3DProfile;
	import flash.filters.BitmapFilter;
	import flash.geom.Matrix;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.text.AntiAliasType;
	import flash.text.GridFitType;
	import flash.text.StyleSheet;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	import flash.text.TextFormat;

	import starling.core.RenderSupport;
	import starling.core.Starling;
	import starling.display.Image;
	import starling.events.Event;
	import starling.textures.ConcreteTexture;
	import starling.textures.Texture;
	import starling.utils.getNextPowerOfTwo;

	/**
	 * Renders text with a native <code>flash.text.TextField</code> and draws
	 * it to <code>BitmapData</code> to convert to Starling textures. Textures
	 * are completely managed by this component, and they will be automatically
	 * disposed when the component is disposed.
	 *
	 * <p>For longer passages of text, this component will stitch together
	 * multiple individual textures both horizontally and vertically, as a grid,
	 * if required. This may require quite a lot of texture memory, possibly
	 * exceeding the limits of some mobile devices, so use this component with
	 * caution when displaying a lot of text.</p>
	 *
	 * @see ../../../help/text-renderers.html Introduction to Feathers text renderers
	 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html flash.text.TextField
	 */
	public class TextFieldTextRenderer extends FeathersControl implements ITextRenderer, IStateObserver
	{
		/**
		 * @private
		 */
		private static const HELPER_POINT:Point = new Point();

		/**
		 * @private
		 */
		private static const HELPER_MATRIX:Matrix = new Matrix();

		/**
		 * @private
		 */
		private static const HELPER_RECTANGLE:Rectangle = new Rectangle();

		/**
		 * The default <code>IStyleProvider</code> for all <code>TextFieldTextRenderer</code>
		 * components.
		 *
		 * @default null
		 * @see feathers.core.FeathersControl#styleProvider
		 */
		public static var globalStyleProvider:IStyleProvider;

		/**
		 * Constructor.
		 */
		public function TextFieldTextRenderer()
		{
			super();
			this.isQuickHitAreaEnabled = true;
		}

		/**
		 * The TextField instance used to render the text before taking a
		 * texture snapshot.
		 */
		protected var textField:TextField;

		/**
		 * An image that displays a snapshot of the native <code>TextField</code>
		 * in the Starling display list when the editor doesn't have focus.
		 */
		protected var textSnapshot:Image;

		/**
		 * If multiple snapshots are needed due to texture size limits, the
		 * snapshots appearing after the first are stored here.
		 */
		protected var textSnapshots:Vector.<Image>;

		/**
		 * @private
		 */
		protected var _textSnapshotOffsetX:Number = 0;

		/**
		 * @private
		 */
		protected var _textSnapshotOffsetY:Number = 0;

		/**
		 * @private
		 */
		protected var _previousActualWidth:Number = NaN;

		/**
		 * @private
		 */
		protected var _previousActualHeight:Number = NaN;

		/**
		 * @private
		 */
		protected var _snapshotWidth:int = 0;

		/**
		 * @private
		 */
		protected var _snapshotHeight:int = 0;

		/**
		 * @private
		 */
		protected var _snapshotVisibleWidth:int = 0;

		/**
		 * @private
		 */
		protected var _snapshotVisibleHeight:int = 0;

		/**
		 * @private
		 */
		protected var _needsNewTexture:Boolean = false;

		/**
		 * @private
		 */
		protected var _hasMeasured:Boolean = false;

		/**
		 * @private
		 */
		override protected function get defaultStyleProvider():IStyleProvider
		{
			return TextFieldTextRenderer.globalStyleProvider;
		}

		/**
		 * @private
		 */
		protected var _text:String = "";

		/**
		 * @inheritDoc
		 *
		 * <p>In the following example, the text is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.text = "Lorem ipsum";</listing>
		 *
		 * @default ""
		 *
		 * @see #isHTML
		 */
		public function get text():String
		{
			return this._text;
		}

		/**
		 * @private
		 */
		public function set text(value:String):void
		{
			if(this._text == value)
			{
				return;
			}
			if(value === null)
			{
				//flash.text.TextField won't accept a null value
				value = "";
			}
			this._text = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var _isHTML:Boolean = false;

		/**
		 * Determines if the TextField should display the text as HTML or not.
		 *
		 * <p>In the following example, the text is displayed as HTML:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.isHTML = true;
		 * textRenderer.text = "&lt;span class='heading'&gt;hello&lt;/span&gt; world!";</listing>
		 *
		 * @default false
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#htmlText flash.text.TextField.htmlText
		 * @see #text
		 */
		public function get isHTML():Boolean
		{
			return this._isHTML;
		}

		/**
		 * @private
		 */
		public function set isHTML(value:Boolean):void
		{
			if(this._isHTML == value)
			{
				return;
			}
			this._isHTML = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var currentTextFormat:TextFormat;

		/**
		 * @private
		 */
		protected var _textFormatForState:Object;

		/**
		 * @private
		 */
		protected var _textFormat:TextFormat;

		/**
		 * The font and styles used to draw the text.
		 *
		 * <p>In the following example, the text format is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.textFormat = new TextFormat( "Source Sans Pro" );</listing>
		 *
		 * @default null
		 *
		 * @see #setTextFormatForState()
		 * @see #disabledTextFormat
		 * @see #selectedTextFormat
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextFormat.html flash.text.TextFormat
		 */
		public function get textFormat():TextFormat
		{
			return this._textFormat;
		}

		/**
		 * @private
		 */
		public function set textFormat(value:TextFormat):void
		{
			if(this._textFormat == value)
			{
				return;
			}
			this._textFormat = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _disabledTextFormat:TextFormat;

		/**
		 * The font and styles used to draw the text when the component is
		 * disabled.
		 *
		 * <p>In the following example, the disabled text format is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.isEnabled = false;
		 * textRenderer.disabledTextFormat = new TextFormat( "Source Sans Pro" );</listing>
		 *
		 * @default null
		 *
		 * @see #textFormat
		 * @see #selectedTextFormat
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextFormat.html flash.text.TextFormat
		 */
		public function get disabledTextFormat():TextFormat
		{
			return this._disabledTextFormat;
		}

		/**
		 * @private
		 */
		public function set disabledTextFormat(value:TextFormat):void
		{
			if(this._disabledTextFormat == value)
			{
				return;
			}
			this._disabledTextFormat = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _selectedTextFormat:TextFormat;

		/**
		 * The font and styles used to draw the text when the
		 * <code>stateContext</code> implements the <code>IToggle</code>
		 * interface, and it is selected.
		 *
		 * <p>In the following example, the selected text format is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.selectedTextFormat = new TextFormat( "Source Sans Pro" );</listing>
		 *
		 * @default null
		 *
		 * @see #stateContext
		 * @see feathers.core.IToggle
		 * @see #textFormat
		 * @see #disabledTextFormat
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextFormat.html flash.text.TextFormat
		 */
		public function get selectedTextFormat():TextFormat
		{
			return this._selectedTextFormat;
		}

		/**
		 * @private
		 */
		public function set selectedTextFormat(value:TextFormat):void
		{
			if(this._selectedTextFormat == value)
			{
				return;
			}
			this._selectedTextFormat = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _styleSheet:StyleSheet;

		/**
		 * The <code>StyleSheet</code> object to pass to the TextField.
		 *
		 * <p>In the following example, a style sheet is applied:</p>
		 *
		 * <listing version="3.0">
		 * var style:StyleSheet = new StyleSheet();
		 * var heading:Object = new Object();
		 * heading.fontWeight = "bold";
		 * heading.color = "#FF0000";
		 *
		 * var body:Object = new Object();
		 * body.fontStyle = "italic";
		 *
		 * style.setStyle(".heading", heading);
		 * style.setStyle("body", body);
		 *
		 * textRenderer.styleSheet = style;
		 * textRenderer.isHTML = true;
		 * textRenderer.text = "&lt;body&gt;&lt;span class='heading'&gt;Hello&lt;/span&gt; World...&lt;/body&gt;";</listing>
		 *
		 * @default null
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#styleSheet Full description of flash.text.TextField.styleSheet in Adobe's Flash Platform API Reference
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/StyleSheet.html flash.text.StyleSheet
		 * @see #isHTML
		 */
		public function get styleSheet():StyleSheet
		{
			return this._styleSheet;
		}

		/**
		 * @private
		 */
		public function set styleSheet(value:StyleSheet):void
		{
			if(this._styleSheet == value)
			{
				return;
			}
			this._styleSheet = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _embedFonts:Boolean = false;

		/**
		 * Determines if the TextField should use an embedded font or not. If
		 * the specified font is not embedded, the text is not displayed.
		 *
		 * <p>In the following example, the font is embedded:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.embedFonts = true;</listing>
		 *
		 * @default false
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#embedFonts Full description of flash.text.TextField.embedFonts in Adobe's Flash Platform API Reference
		 */
		public function get embedFonts():Boolean
		{
			return this._embedFonts;
		}

		/**
		 * @private
		 */
		public function set embedFonts(value:Boolean):void
		{
			if(this._embedFonts == value)
			{
				return;
			}
			this._embedFonts = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @inheritDoc
		 */
		public function get baseline():Number
		{
			if(!this.textField)
			{
				return 0;
			}
			var gutterDimensionsOffset:Number = 0;
			if(this._useGutter)
			{
				gutterDimensionsOffset = 2;
			}
			return gutterDimensionsOffset + this.textField.getLineMetrics(0).ascent;
		}

		/**
		 * @private
		 */
		protected var _wordWrap:Boolean = false;

		/**
		 * @inheritDoc
		 *
		 * <p>In the following example, word wrap is enabled:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.wordWrap = true;</listing>
		 *
		 * @default false
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#wordWrap Full description of flash.text.TextField.wordWrap in Adobe's Flash Platform API Reference
		 */
		public function get wordWrap():Boolean
		{
			return this._wordWrap;
		}

		/**
		 * @private
		 */
		public function set wordWrap(value:Boolean):void
		{
			if(this._wordWrap == value)
			{
				return;
			}
			this._wordWrap = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _snapToPixels:Boolean = true;

		/**
		 * Determines if the text should be snapped to the nearest whole pixel
		 * when rendered. When this is <code>false</code>, text may be displayed
		 * on sub-pixels, which often results in blurred rendering due to
		 * texture smoothing.
		 *
		 * <p>In the following example, the text is not snapped to pixels:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.snapToPixels = false;</listing>
		 *
		 * @default true
		 */
		public function get snapToPixels():Boolean
		{
			return this._snapToPixels;
		}

		/**
		 * @private
		 */
		public function set snapToPixels(value:Boolean):void
		{
			this._snapToPixels = value;
		}

		/**
		 * @private
		 */
		private var _antiAliasType:String = AntiAliasType.ADVANCED;

		/**
		 * The type of anti-aliasing used for this text field, defined as
		 * constants in the <code>flash.text.AntiAliasType</code> class. You can
		 * control this setting only if the font is embedded (with the
		 * <code>embedFonts</code> property set to true).
		 *
		 * <p>In the following example, the anti-alias type is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.antiAliasType = AntiAliasType.NORMAL;</listing>
		 *
		 * @default flash.text.AntiAliasType.ADVANCED
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#antiAliasType Full description of flash.text.TextField.antiAliasType in Adobe's Flash Platform API Reference
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/AntiAliasType.html flash.text.AntiAliasType
		 */
		public function get antiAliasType():String
		{
			return this._antiAliasType;
		}

		/**
		 * @private
		 */
		public function set antiAliasType(value:String):void
		{
			if(this._antiAliasType == value)
			{
				return;
			}
			this._antiAliasType = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		private var _background:Boolean = false;

		/**
		 * Specifies whether the text field has a background fill. Use the
		 * <code>backgroundColor</code> property to set the background color of
		 * a text field.
		 *
		 * <p>In the following example, the background is enabled:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.background = true;
		 * textRenderer.backgroundColor = 0xff0000;</listing>
		 *
		 * @default false
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#background Full description of flash.text.TextField.background in Adobe's Flash Platform API Reference
		 * @see #backgroundColor
		 */
		public function get background():Boolean
		{
			return this._background;
		}

		/**
		 * @private
		 */
		public function set background(value:Boolean):void
		{
			if(this._background == value)
			{
				return;
			}
			this._background = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		private var _backgroundColor:uint = 0xffffff;

		/**
		 * The color of the text field background that is displayed if the
		 * <code>background</code> property is set to <code>true</code>.
		 *
		 * <p>In the following example, the background color is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.background = true;
		 * textRenderer.backgroundColor = 0xff000ff;</listing>
		 *
		 * @default 0xffffff
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#backgroundColor Full description of flash.text.TextField.backgroundColor in Adobe's Flash Platform API Reference
		 * @see #background
		 */
		public function get backgroundColor():uint
		{
			return this._backgroundColor;
		}

		/**
		 * @private
		 */
		public function set backgroundColor(value:uint):void
		{
			if(this._backgroundColor == value)
			{
				return;
			}
			this._backgroundColor = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		private var _border:Boolean = false;

		/**
		 * Specifies whether the text field has a border. Use the
		 * <code>borderColor</code> property to set the border color.
		 *
		 * <p>Note: this property cannot be used when the <code>useGutter</code>
		 * property is set to <code>false</code> (the default value!).</p>
		 *
		 * <p>In the following example, the border is enabled:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.border = true;
		 * textRenderer.borderColor = 0xff0000;</listing>
		 *
		 * @default false
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#border Full description of flash.text.TextField.border in Adobe's Flash Platform API Reference
		 * @see #borderColor
		 */
		public function get border():Boolean
		{
			return this._border;
		}

		/**
		 * @private
		 */
		public function set border(value:Boolean):void
		{
			if(this._border == value)
			{
				return;
			}
			this._border = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		private var _borderColor:uint = 0x000000;

		/**
		 * The color of the text field border that is displayed if the
		 * <code>border</code> property is set to <code>true</code>.
		 *
		 * <p>In the following example, the border color is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.border = true;
		 * textRenderer.borderColor = 0xff00ff;</listing>
		 *
		 * @default 0x000000
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#borderColor Full description of flash.text.TextField.borderColor in Adobe's Flash Platform API Reference
		 * @see #border
		 */
		public function get borderColor():uint
		{
			return this._borderColor;
		}

		/**
		 * @private
		 */
		public function set borderColor(value:uint):void
		{
			if(this._borderColor == value)
			{
				return;
			}
			this._borderColor = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		private var _condenseWhite:Boolean = false;

		/**
		 * A boolean value that specifies whether extra white space (spaces,
		 * line breaks, and so on) in a text field with HTML text is removed.
		 *
		 * <p>In the following example, whitespace is condensed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.condenseWhite = true;</listing>
		 *
		 * @default false
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#condenseWhite Full description of flash.text.TextField.condenseWhite in Adobe's Flash Platform API Reference
		 * @see #isHTML
		 */
		public function get condenseWhite():Boolean
		{
			return this._condenseWhite;
		}

		/**
		 * @private
		 */
		public function set condenseWhite(value:Boolean):void
		{
			if(this._condenseWhite == value)
			{
				return;
			}
			this._condenseWhite = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		private var _displayAsPassword:Boolean = false;

		/**
		 * Specifies whether the text field is a password text field that hides
		 * the input characters using asterisks instead of the actual
		 * characters.
		 *
		 * <p>In the following example, the text is displayed as a password:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.displayAsPassword = true;</listing>
		 *
		 * @default false
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#displayAsPassword Full description of flash.text.TextField.displayAsPassword in Adobe's Flash Platform API Reference
		 */
		public function get displayAsPassword():Boolean
		{
			return this._displayAsPassword;
		}

		/**
		 * @private
		 */
		public function set displayAsPassword(value:Boolean):void
		{
			if(this._displayAsPassword == value)
			{
				return;
			}
			this._displayAsPassword = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		private var _gridFitType:String = GridFitType.PIXEL;

		/**
		 * Determines whether Flash Player forces strong horizontal and vertical
		 * lines to fit to a pixel or subpixel grid, or not at all using the
		 * constants defined in the <code>flash.text.GridFitType</code> class.
		 * This property applies only if the <code>antiAliasType</code> property
		 * of the text field is set to <code>flash.text.AntiAliasType.ADVANCED</code>.
		 *
		 * <p>In the following example, the grid fit type is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.gridFitType = GridFitType.SUBPIXEL;</listing>
		 *
		 * @default flash.text.GridFitType.PIXEL
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#gridFitType Full description of flash.text.TextField.gridFitType in Adobe's Flash Platform API Reference
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/GridFitType.html flash.text.GridFitType
		 * @see #antiAliasType
		 */
		public function get gridFitType():String
		{
			return this._gridFitType;
		}

		/**
		 * @private
		 */
		public function set gridFitType(value:String):void
		{
			if(this._gridFitType == value)
			{
				return;
			}
			this._gridFitType = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		private var _sharpness:Number = 0;

		/**
		 * The sharpness of the glyph edges in this text field. This property
		 * applies only if the <code>antiAliasType</code> property of the text
		 * field is set to <code>flash.text.AntiAliasType.ADVANCED</code>. The
		 * range for <code>sharpness</code> is a number from <code>-400</code>
		 * to <code>400</code>.
		 *
		 * <p>In the following example, the sharpness is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.sharpness = 200;</listing>
		 *
		 * @default 0
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#sharpness Full description of flash.text.TextField.sharpness in Adobe's Flash Platform API Reference
		 * @see #antiAliasType
		 */
		public function get sharpness():Number
		{
			return this._sharpness;
		}

		/**
		 * @private
		 */
		public function set sharpness(value:Number):void
		{
			if(this._sharpness == value)
			{
				return;
			}
			this._sharpness = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		private var _thickness:Number = 0;

		/**
		 * The thickness of the glyph edges in this text field. This property
		 * applies only if the <code>antiAliasType</code> property is set to
		 * <code>flash.text.AntiAliasType.ADVANCED</code>. The range for
		 * <code>thickness</code> is a number from <code>-200</code> to
		 * <code>200</code>.
		 *
		 * <p>In the following example, the thickness is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.thickness = 100;</listing>
		 *
		 * @default 0
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/TextField.html#thickness Full description of flash.text.TextField.thickness in Adobe's Flash Platform API Reference
		 * @see #antiAliasType
		 */
		public function get thickness():Number
		{
			return this._thickness;
		}

		/**
		 * @private
		 */
		public function set thickness(value:Number):void
		{
			if(this._thickness == value)
			{
				return;
			}
			this._thickness = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var _maxTextureDimensions:int = 2048;

		/**
		 * The maximum size of individual textures that are managed by this text
		 * renderer. Must be a power of 2. A larger value will create fewer
		 * individual textures, but a smaller value may use less overall texture
		 * memory by incrementing over smaller powers of two.
		 *
		 * <p>In the following example, the maximum size of the textures is
		 * changed:</p>
		 *
		 * <listing version="3.0">
		 * renderer.maxTextureDimensions = 4096;</listing>
		 *
		 * @default 2048
		 */
		public function get maxTextureDimensions():int
		{
			return this._maxTextureDimensions;
		}

		/**
		 * @private
		 */
		public function set maxTextureDimensions(value:int):void
		{
			//check if we can use rectangle textures or not
			if(Starling.current.profile == Context3DProfile.BASELINE_CONSTRAINED)
			{
				value = getNextPowerOfTwo(value);
			}
			if(this._maxTextureDimensions == value)
			{
				return;
			}
			this._maxTextureDimensions = value;
			this._needsNewTexture = true;
			this.invalidate(INVALIDATION_FLAG_SIZE);
		}

		/**
		 * @private
		 */
		protected var _nativeFilters:Array;

		/**
		 * Native filters to pass to the <code>flash.text.TextField</code>
		 * before creating the texture snapshot.
		 *
		 * <p>In the following example, the native filters are changed:</p>
		 *
		 * <listing version="3.0">
		 * renderer.nativeFilters = [ new GlowFilter() ];</listing>
		 *
		 * @default null
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/display/DisplayObject.html#filters Full description of flash.display.DisplayObject.filters in Adobe's Flash Platform API Reference
		 */
		public function get nativeFilters():Array
		{
			return this._nativeFilters;
		}

		/**
		 * @private
		 */
		public function set nativeFilters(value:Array):void
		{
			if(this._nativeFilters == value)
			{
				return;
			}
			this._nativeFilters = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _useGutter:Boolean = false;

		/**
		 * Determines if the 2-pixel gutter around the edges of the
		 * <code>flash.text.TextField</code> will be used in measurement and
		 * layout. To visually align with other text renderers and text editors,
		 * it is often best to leave the gutter disabled.
		 *
		 * <p>In the following example, the gutter is enabled:</p>
		 *
		 * <listing version="3.0">
		 * textEditor.useGutter = true;</listing>
		 *
		 * @default false
		 */
		public function get useGutter():Boolean
		{
			return this._useGutter;
		}

		/**
		 * @private
		 */
		public function set useGutter(value:Boolean):void
		{
			if(this._useGutter == value)
			{
				return;
			}
			this._useGutter = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _stateContext:IStateContext;

		/**
		 * When the text renderer observes a state context, the text renderer
		 * may change its <code>TextFormat</code> based on the current state of
		 * that context. Typically, a relevant component will automatically
		 * assign itself as the state context of a text renderer, so this
		 * property is typically meant for internal use only.
		 *
		 * @default null
		 *
		 * @see #setTextFormatForState()
		 */
		public function get stateContext():IStateContext
		{
			return this._stateContext;
		}

		/**
		 * @private
		 */
		public function set stateContext(value:IStateContext):void
		{
			if(this._stateContext === value)
			{
				return;
			}
			if(this._stateContext)
			{
				this._stateContext.removeEventListener(FeathersEventType.STATE_CHANGE, stateContext_stateChangeHandler);
			}
			this._stateContext = value;
			if(this._stateContext)
			{
				this._stateContext.addEventListener(FeathersEventType.STATE_CHANGE, stateContext_stateChangeHandler);
			}
			this.invalidate(INVALIDATION_FLAG_STATE);
		}

		/**
		 * @private
		 */
		protected var _lastGlobalScaleX:Number = 0;

		/**
		 * @private
		 */
		protected var _lastGlobalScaleY:Number = 0;

		/**
		 * @private
		 */
		protected var _updateSnapshotOnScaleChange:Boolean = false;

		/**
		 * Refreshes the texture snapshot every time that the text renderer is
		 * scaled. Based on the scale in global coordinates, so scaling the
		 * parent will require a new snapshot.
		 *
		 * <p>Warning: setting this property to true may result in reduced
		 * performance because every change of the scale requires uploading a
		 * new texture to the GPU. Use with caution. Consider setting this
		 * property to false temporarily during animations that modify the
		 * scale.</p>
		 *
		 * <p>In the following example, the snapshot will be updated when the
		 * text renderer is scaled:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.updateSnapshotOnScaleChange = true;</listing>
		 *
		 * @default false
		 */
		public function get updateSnapshotOnScaleChange():Boolean
		{
			return this._updateSnapshotOnScaleChange;
		}

		/**
		 * @private
		 */
		public function set updateSnapshotOnScaleChange(value:Boolean):void
		{
			if(this._updateSnapshotOnScaleChange == value)
			{
				return;
			}
			this._updateSnapshotOnScaleChange = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var _useSnapshotDelayWorkaround:Boolean = false;

		/**
		 * Fixes an issue where <code>flash.text.TextField</code> renders
		 * incorrectly when drawn to <code>BitmapData</code> by waiting one
		 * frame.
		 *
		 * <p>Warning: enabling this workaround may cause slight flickering
		 * after the <code>text</code> property is changed.</p>
		 *
		 * <p>In the following example, the workaround is enabled:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.useSnapshotDelayWorkaround = true;</listing>
		 *
		 * @default false
		 */
		public function get useSnapshotDelayWorkaround():Boolean
		{
			return this._useSnapshotDelayWorkaround;
		}

		/**
		 * @private
		 */
		public function set useSnapshotDelayWorkaround(value:Boolean):void
		{
			if(this._useSnapshotDelayWorkaround == value)
			{
				return;
			}
			this._useSnapshotDelayWorkaround = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		override public function dispose():void
		{
			if(this.textSnapshot)
			{
				this.textSnapshot.texture.dispose();
				this.removeChild(this.textSnapshot, true);
				this.textSnapshot = null;
			}
			if(this.textSnapshots)
			{
				var snapshotCount:int = this.textSnapshots.length;
				for(var i:int = 0; i < snapshotCount; i++)
				{
					var snapshot:Image = this.textSnapshots[i];
					snapshot.texture.dispose();
					this.removeChild(snapshot, true);
				}
				this.textSnapshots = null;
			}
			//this isn't necessary, but if a memory leak keeps the text renderer
			//from being garbage collected, freeing up the text field may help
			//ease major memory pressure from native filters
			this.textField = null;
			
			this.stateContext = null;

			this._previousActualWidth = NaN;
			this._previousActualHeight = NaN;

			this._needsNewTexture = false;
			this._snapshotWidth = 0;
			this._snapshotHeight = 0;

			super.dispose();
		}

		/**
		 * @private
		 */
		override public function render(support:RenderSupport, parentAlpha:Number):void
		{
			if(this.textSnapshot)
			{
				this.getTransformationMatrix(this.stage, HELPER_MATRIX);
				if(this._updateSnapshotOnScaleChange)
				{
					var globalScaleX:Number = matrixToScaleX(HELPER_MATRIX);
					var globalScaleY:Number = matrixToScaleY(HELPER_MATRIX);
					if(globalScaleX != this._lastGlobalScaleX || globalScaleY != this._lastGlobalScaleY)
					{
						//the snapshot needs to be updated because the scale has
						//changed since the last snapshot was taken.
						this.invalidate(INVALIDATION_FLAG_SIZE);
						this.validate();
					}
				}
				var scaleFactor:Number = Starling.current.contentScaleFactor;
				if(!this._nativeFilters || this._nativeFilters.length === 0)
				{
					var offsetX:Number = 0;
					var offsetY:Number = 0;
				}
				else
				{
					offsetX = this._textSnapshotOffsetX / scaleFactor;
					offsetY = this._textSnapshotOffsetY / scaleFactor;
				}
				if(this._snapToPixels)
				{
					offsetX += Math.round(HELPER_MATRIX.tx) - HELPER_MATRIX.tx;
					offsetY += Math.round(HELPER_MATRIX.ty) - HELPER_MATRIX.ty;
				}

				var snapshotIndex:int = -1;
				var totalBitmapWidth:Number = this._snapshotWidth;
				var totalBitmapHeight:Number = this._snapshotHeight;
				var xPosition:Number = offsetX;
				var yPosition:Number = offsetY;
				do
				{
					var currentBitmapWidth:Number = totalBitmapWidth;
					if(currentBitmapWidth > this._maxTextureDimensions)
					{
						currentBitmapWidth = this._maxTextureDimensions;
					}
					do
					{
						var currentBitmapHeight:Number = totalBitmapHeight;
						if(currentBitmapHeight > this._maxTextureDimensions)
						{
							currentBitmapHeight = this._maxTextureDimensions;
						}
						if(snapshotIndex < 0)
						{
							var snapshot:Image = this.textSnapshot;
						}
						else
						{
							snapshot = this.textSnapshots[snapshotIndex];
						}
						snapshot.x = xPosition / scaleFactor;
						snapshot.y = yPosition / scaleFactor;
						if(this._updateSnapshotOnScaleChange)
						{
							snapshot.x /= this._lastGlobalScaleX;
							snapshot.y /= this._lastGlobalScaleX;
						}
						snapshotIndex++;
						yPosition += currentBitmapHeight;
						totalBitmapHeight -= currentBitmapHeight;
					}
					while(totalBitmapHeight > 0)
					xPosition += currentBitmapWidth;
					totalBitmapWidth -= currentBitmapWidth;
					yPosition = offsetY;
					totalBitmapHeight = this._snapshotHeight;
				}
				while(totalBitmapWidth > 0)
			}
			super.render(support, parentAlpha);
		}

		/**
		 * @inheritDoc
		 */
		public function measureText(result:Point = null):Point
		{
			if(!result)
			{
				result = new Point();
			}

			var needsWidth:Boolean = this.explicitWidth !== this.explicitWidth; //isNaN
			var needsHeight:Boolean = this.explicitHeight !== this.explicitHeight; //isNaN
			if(!needsWidth && !needsHeight)
			{
				result.x = this.explicitWidth;
				result.y = this.explicitHeight;
				return result;
			}

			//if a parent component validates before we're added to the stage,
			//measureText() may be called before initialization, so we need to
			//force it.
			if(!this._isInitialized)
			{
				this.initializeInternal();
			}

			this.commit();

			result = this.measure(result);

			return result;
		}

		/**
		 * Sets the <code>TextFormat</code> to be used by the text renderer when
		 * the <code>currentState</code> property of the
		 * <code>stateContext</code> matches the specified state value.
		 *
		 * <p>If an <code>TextFormat</code> is not defined for a specific
		 * state, the value of the <code>textFormat</code> property will be
		 * used instead.</p>
		 *
		 * <p>If the <code>disabledTextFormat</code> property is not
		 * <code>null</code> and the <code>isEnabled</code> property is
		 * <code>false</code>, all other text formats will be ignored.</p>
		 *
		 * @see #stateContext
		 * @see #textFormat
		 */
		public function setTextFormatForState(state:String, textFormat:TextFormat):void
		{
			if(textFormat)
			{
				if(!this._textFormatForState)
				{
					this._textFormatForState = {};
				}
				this._textFormatForState[state] = textFormat;
			}
			else
			{
				delete this._textFormatForState[state];
			}
			//if the context's current state is the state that we're modifying,
			//we need to use the new value immediately.
			if(this._stateContext && this._stateContext.currentState === state)
			{
				this.invalidate(INVALIDATION_FLAG_STATE);
			}
		}

		/**
		 * @private
		 */
		override protected function initialize():void
		{
			if(!this.textField)
			{
				this.textField = new TextField();
				var scaleFactor:Number = Starling.contentScaleFactor;
				this.textField.scaleX = scaleFactor;
				this.textField.scaleY = scaleFactor;
				this.textField.mouseEnabled = this.textField.mouseWheelEnabled = false;
				this.textField.selectable = false;
				this.textField.multiline = true;
			}
		}

		/**
		 * @private
		 */
		override protected function draw():void
		{
			var sizeInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_SIZE);

			this.commit();

			this._hasMeasured = false;
			sizeInvalid = this.autoSizeIfNeeded() || sizeInvalid;

			this.layout(sizeInvalid);
		}

		/**
		 * @private
		 */
		protected function commit():void
		{
			var stylesInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_STYLES);
			var dataInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_DATA);
			var stateInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_STATE);
			
			if(stylesInvalid || stateInvalid)
			{
				this.refreshTextFormat();
			}

			if(stylesInvalid)
			{
				this.textField.antiAliasType = this._antiAliasType;
				this.textField.background = this._background;
				this.textField.backgroundColor = this._backgroundColor;
				this.textField.border = this._border;
				this.textField.borderColor = this._borderColor;
				this.textField.condenseWhite = this._condenseWhite;
				this.textField.displayAsPassword = this._displayAsPassword;
				this.textField.gridFitType = this._gridFitType;
				this.textField.sharpness = this._sharpness;
				this.textField.thickness = this._thickness;
				this.textField.filters = this._nativeFilters;
			}

			if(dataInvalid || stylesInvalid || stateInvalid)
			{
				this.textField.wordWrap = this._wordWrap;
				this.textField.embedFonts = this._embedFonts;
				if(this._styleSheet)
				{
					this.textField.styleSheet = this._styleSheet;
				}
				else
				{
					this.textField.styleSheet = null;
					this.textField.defaultTextFormat = this.currentTextFormat;
				}
				if(this._isHTML)
				{
					this.textField.htmlText = this._text;
				}
				else
				{
					this.textField.text = this._text;
				}
			}
		}

		/**
		 * @private
		 */
		protected function measure(result:Point = null):Point
		{
			if(!result)
			{
				result = new Point();
			}

			var needsWidth:Boolean = this.explicitWidth !== this.explicitWidth; //isNaN
			var needsHeight:Boolean = this.explicitHeight !== this.explicitHeight; //isNaN

			this.textField.autoSize = TextFieldAutoSize.LEFT;
			this.textField.wordWrap = false;

			var scaleFactor:Number = Starling.contentScaleFactor;
			var gutterDimensionsOffset:Number = 4;
			if(this._useGutter)
			{
				gutterDimensionsOffset = 0;
			}

			var newWidth:Number = this.explicitWidth;
			if(needsWidth)
			{
				//yes, this value is never used. this is a workaround for a bug
				//in AIR for iOS where getting the value for textField.width the
				//first time results in an incorrect value, but if you query it
				//again, for some reason, it reports the correct width value.
				var hackWorkaround:Number = this.textField.width;
				newWidth = (this.textField.width / scaleFactor) - gutterDimensionsOffset;
				if(newWidth < this._minWidth)
				{
					newWidth = this._minWidth;
				}
				else if(newWidth > this._maxWidth)
				{
					newWidth = this._maxWidth;
				}
			}
			//and this is a workaround for an issue where flash.text.TextField
			//will wrap the last word when you pass the value returned by the
			//width getter (when TextFieldAutoSize.LEFT is used) to the width
			//setter. In other words, the value technically isn't changing, but
			//TextField behaves differently.
			if(!needsWidth || ((this.textField.width / scaleFactor) - gutterDimensionsOffset) > newWidth)
			{
				this.textField.width = newWidth + gutterDimensionsOffset;
				this.textField.wordWrap = this._wordWrap;
			}
			var newHeight:Number = this.explicitHeight;
			if(needsHeight)
			{
				newHeight = (this.textField.height / scaleFactor) - gutterDimensionsOffset;
				if(newHeight < this._minHeight)
				{
					newHeight = this._minHeight;
				}
				else if(newHeight > this._maxHeight)
				{
					newHeight = this._maxHeight;
				}
			}

			this.textField.autoSize = TextFieldAutoSize.NONE;

			//put the width and height back just in case we measured without
			//a full validation
			this.textField.width = this.actualWidth + gutterDimensionsOffset;
			this.textField.height = this.actualHeight + gutterDimensionsOffset;

			result.x = newWidth;
			result.y = newHeight;

			this._hasMeasured = true;
			return result;
		}

		/**
		 * @private
		 */
		protected function layout(sizeInvalid:Boolean):void
		{
			var stylesInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_STYLES);
			var dataInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_DATA);
			var stateInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_STATE);

			var scaleFactor:Number = Starling.contentScaleFactor;
			var gutterDimensionsOffset:Number = 4;
			if(this._useGutter)
			{
				gutterDimensionsOffset = 0;
			}

			//if measure() isn't called, we need to apply the same workaround
			//for the flash.text.TextField bug with wordWrap.
			if(!this._hasMeasured && this._wordWrap)
			{
				this.textField.autoSize = TextFieldAutoSize.LEFT;
				this.textField.wordWrap = false;
				if(((this.textField.width / scaleFactor) - gutterDimensionsOffset) > this.actualWidth)
				{
					this.textField.wordWrap = true;
				}
				this.textField.autoSize = TextFieldAutoSize.NONE;
				this.textField.width = this.actualWidth + gutterDimensionsOffset;
			}
			if(sizeInvalid)
			{
				this.textField.width = this.actualWidth + gutterDimensionsOffset;
				this.textField.height = this.actualHeight + gutterDimensionsOffset;
				//these are getting put into an int later, so we don't want it
				//to possibly round down and cut off part of the text. 
				var rectangleSnapshotWidth:Number = Math.ceil(this.actualWidth * scaleFactor);
				var rectangleSnapshotHeight:Number = Math.ceil(this.actualHeight * scaleFactor);
				if(this._updateSnapshotOnScaleChange)
				{
					this.getTransformationMatrix(this.stage, HELPER_MATRIX);
					rectangleSnapshotWidth *= matrixToScaleX(HELPER_MATRIX);
					rectangleSnapshotHeight *= matrixToScaleY(HELPER_MATRIX);
				}
				if(rectangleSnapshotWidth >= 1 && rectangleSnapshotHeight >= 1 &&
					this._nativeFilters && this._nativeFilters.length > 0)
				{
					HELPER_MATRIX.identity();
					HELPER_MATRIX.scale(scaleFactor, scaleFactor);
					var bitmapData:BitmapData = new BitmapData(rectangleSnapshotWidth, rectangleSnapshotHeight, true, 0x00ff00ff);
					bitmapData.draw(this.textField, HELPER_MATRIX, null, null, HELPER_RECTANGLE);
					this.measureNativeFilters(bitmapData, HELPER_RECTANGLE);
					bitmapData.dispose();
					bitmapData = null;
					this._textSnapshotOffsetX = HELPER_RECTANGLE.x;
					this._textSnapshotOffsetY = HELPER_RECTANGLE.y;
					rectangleSnapshotWidth = HELPER_RECTANGLE.width;
					rectangleSnapshotHeight = HELPER_RECTANGLE.height;
				}
				var canUseRectangleTexture:Boolean = Starling.current.profile != Context3DProfile.BASELINE_CONSTRAINED;
				if(canUseRectangleTexture)
				{
					if(rectangleSnapshotWidth > this._maxTextureDimensions)
					{
						this._snapshotWidth = int(rectangleSnapshotWidth / this._maxTextureDimensions) * this._maxTextureDimensions + (rectangleSnapshotWidth % this._maxTextureDimensions);
					}
					else
					{
						this._snapshotWidth = rectangleSnapshotWidth;
					}
				}
				else
				{
					if(rectangleSnapshotWidth > this._maxTextureDimensions)
					{
						this._snapshotWidth = int(rectangleSnapshotWidth / this._maxTextureDimensions) * this._maxTextureDimensions + getNextPowerOfTwo(rectangleSnapshotWidth % this._maxTextureDimensions);
					}
					else
					{
						this._snapshotWidth = getNextPowerOfTwo(rectangleSnapshotWidth);
					}
				}
				if(canUseRectangleTexture)
				{
					if(rectangleSnapshotHeight > this._maxTextureDimensions)
					{
						this._snapshotHeight = int(rectangleSnapshotHeight / this._maxTextureDimensions) * this._maxTextureDimensions + (rectangleSnapshotHeight % this._maxTextureDimensions);
					}
					else
					{
						this._snapshotHeight = rectangleSnapshotHeight;
					}
				}
				else
				{
					if(rectangleSnapshotHeight > this._maxTextureDimensions)
					{
						this._snapshotHeight = int(rectangleSnapshotHeight / this._maxTextureDimensions) * this._maxTextureDimensions + getNextPowerOfTwo(rectangleSnapshotHeight % this._maxTextureDimensions);
					}
					else
					{
						this._snapshotHeight = getNextPowerOfTwo(rectangleSnapshotHeight);
					}
				}
				var textureRoot:ConcreteTexture = this.textSnapshot ? this.textSnapshot.texture.root : null;
				this._needsNewTexture = this._needsNewTexture || !this.textSnapshot ||
					(textureRoot && (textureRoot.scale != scaleFactor ||
					this._snapshotWidth != textureRoot.nativeWidth || this._snapshotHeight != textureRoot.nativeHeight));
				this._snapshotVisibleWidth = rectangleSnapshotWidth;
				this._snapshotVisibleHeight = rectangleSnapshotHeight;
			}

			//instead of checking sizeInvalid, which will often be triggered by
			//changing maxWidth or something for measurement, we check against
			//the previous actualWidth/Height used for the snapshot.
			if(stylesInvalid || dataInvalid || stateInvalid || this._needsNewTexture ||
				this.actualWidth != this._previousActualWidth ||
				this.actualHeight != this._previousActualHeight)
			{
				this._previousActualWidth = this.actualWidth;
				this._previousActualHeight = this.actualHeight;
				var hasText:Boolean = this._text.length > 0;
				if(hasText)
				{
					if(this._useSnapshotDelayWorkaround)
					{
						//we need to wait a frame for the TextField to render
						//properly. sometimes two, and this is a known issue.
						this.addEventListener(Event.ENTER_FRAME, enterFrameHandler);
					}
					else
					{
						this.refreshSnapshot();
					}
				}
				if(this.textSnapshot)
				{
					this.textSnapshot.visible = hasText && this._snapshotWidth > 0 && this._snapshotHeight > 0;
				}
			}
		}

		/**
		 * If the component's dimensions have not been set explicitly, it will
		 * measure its content and determine an ideal size for itself. If the
		 * <code>explicitWidth</code> or <code>explicitHeight</code> member
		 * variables are set, those value will be used without additional
		 * measurement. If one is set, but not the other, the dimension with the
		 * explicit value will not be measured, but the other non-explicit
		 * dimension will still need measurement.
		 *
		 * <p>Calls <code>setSizeInternal()</code> to set up the
		 * <code>actualWidth</code> and <code>actualHeight</code> member
		 * variables used for layout.</p>
		 *
		 * <p>Meant for internal use, and subclasses may override this function
		 * with a custom implementation.</p>
		 */
		protected function autoSizeIfNeeded():Boolean
		{
			var needsWidth:Boolean = this.explicitWidth !== this.explicitWidth; //isNaN
			var needsHeight:Boolean = this.explicitHeight !== this.explicitHeight; //isNaN
			if(!needsWidth && !needsHeight)
			{
				return false;
			}

			this.measure(HELPER_POINT);
			return this.setSizeInternal(HELPER_POINT.x, HELPER_POINT.y, false);
		}

		/**
		 * @private
		 */
		protected function measureNativeFilters(bitmapData:BitmapData, result:Rectangle = null):Rectangle
		{
			if(!result)
			{
				result = new Rectangle();
			}
			var resultX:Number = 0;
			var resultY:Number = 0;
			var resultWidth:Number = 0;
			var resultHeight:Number = 0;
			var filterCount:int = this._nativeFilters.length;
			for(var i:int = 0; i < filterCount; i++)
			{
				var filter:BitmapFilter = this._nativeFilters[i];
				var filterRect:Rectangle = bitmapData.generateFilterRect(bitmapData.rect, filter);
				var filterX:Number = filterRect.x;
				var filterY:Number = filterRect.y;
				var filterWidth:Number = filterRect.width;
				var filterHeight:Number = filterRect.height;
				if(resultX > filterX)
				{
					resultX = filterX;
				}
				if(resultY > filterY)
				{
					resultY = filterY;
				}
				if(resultWidth < filterWidth)
				{
					resultWidth = filterWidth;
				}
				if(resultHeight < filterHeight)
				{
					resultHeight = filterHeight;
				}
			}
			result.setTo(resultX, resultY, resultWidth, resultHeight);
			return result;
		}

		/**
		 * @private
		 */
		protected function refreshTextFormat():void
		{
			var textFormat:TextFormat;
			if(this._stateContext && this._textFormatForState)
			{
				var currentState:String = this._stateContext.currentState;
				if(currentState in this._textFormatForState)
				{
					textFormat = TextFormat(this._textFormatForState[currentState]);
				}
			}
			if(!textFormat && !this._isEnabled && this._disabledTextFormat)
			{
				textFormat = this._disabledTextFormat;
			}
			if(!textFormat && this._selectedTextFormat &&
				this._stateContext is IToggle && IToggle(this._stateContext).isSelected)
			{
				textFormat = this._selectedTextFormat;
			}
			if(!textFormat)
			{
				//let's fall back to using Starling's embedded mini font if no
				//text format has been specified
				if(!this._textFormat)
				{
					this._textFormat = new TextFormat();
				}
				textFormat = this._textFormat;
			}
			this.currentTextFormat = textFormat;
		}

		/**
		 * @private
		 */
		protected function createTextureOnRestoreCallback(snapshot:Image):void
		{
			var self:TextFieldTextRenderer = this;
			var texture:Texture = snapshot.texture;
			texture.root.onRestore = function():void
			{
				var scaleFactor:Number = Starling.contentScaleFactor;
				HELPER_MATRIX.identity();
				HELPER_MATRIX.scale(scaleFactor, scaleFactor);
				var bitmapData:BitmapData = self.drawTextFieldRegionToBitmapData(
					snapshot.x, snapshot.y, texture.nativeWidth, texture.nativeHeight);
				texture.root.uploadBitmapData(bitmapData);
				bitmapData.dispose();
			};
		}

		/**
		 * @private
		 */
		protected function drawTextFieldRegionToBitmapData(textFieldX:Number, textFieldY:Number,
			bitmapWidth:Number, bitmapHeight:Number, bitmapData:BitmapData = null):BitmapData
		{
			var scaleFactor:Number = Starling.contentScaleFactor;
			var clipWidth:Number = this._snapshotVisibleWidth - textFieldX;
			var clipHeight:Number = this._snapshotVisibleHeight - textFieldY;
			if(!bitmapData || bitmapData.width != bitmapWidth || bitmapData.height != bitmapHeight)
			{
				if(bitmapData)
				{
					bitmapData.dispose();
				}
				bitmapData = new BitmapData(bitmapWidth, bitmapHeight, true, 0x00ff00ff);
			}
			else
			{
				//clear the bitmap data and reuse it
				bitmapData.fillRect(bitmapData.rect, 0x00ff00ff);
			}
			var gutterPositionOffset:Number = 2 * scaleFactor;
			if(this._useGutter)
			{
				gutterPositionOffset = 0;
			}
			HELPER_MATRIX.tx = -(textFieldX + gutterPositionOffset) - this._textSnapshotOffsetX;
			HELPER_MATRIX.ty = -(textFieldY + gutterPositionOffset) - this._textSnapshotOffsetY;
			HELPER_RECTANGLE.setTo(0, 0, clipWidth, clipHeight);
			bitmapData.draw(this.textField, HELPER_MATRIX, null, null, HELPER_RECTANGLE);
			return bitmapData;
		}

		/**
		 * @private
		 */
		protected function refreshSnapshot():void
		{
			if(this._snapshotWidth <= 0 || this._snapshotHeight <= 0)
			{
				return;
			}
			var scaleFactor:Number = Starling.contentScaleFactor;
			if(this._updateSnapshotOnScaleChange)
			{
				this.getTransformationMatrix(this.stage, HELPER_MATRIX);
				var globalScaleX:Number = matrixToScaleX(HELPER_MATRIX);
				var globalScaleY:Number = matrixToScaleY(HELPER_MATRIX);
			}
			HELPER_MATRIX.identity();
			HELPER_MATRIX.scale(scaleFactor, scaleFactor);
			if(this._updateSnapshotOnScaleChange)
			{
				HELPER_MATRIX.scale(globalScaleX, globalScaleY);
			}
			var totalBitmapWidth:Number = this._snapshotWidth;
			var totalBitmapHeight:Number = this._snapshotHeight;
			var xPosition:Number = 0;
			var yPosition:Number = 0;
			var bitmapData:BitmapData;
			var snapshotIndex:int = -1;
			do
			{
				var currentBitmapWidth:Number = totalBitmapWidth;
				if(currentBitmapWidth > this._maxTextureDimensions)
				{
					currentBitmapWidth = this._maxTextureDimensions;
				}
				do
				{
					var currentBitmapHeight:Number = totalBitmapHeight;
					if(currentBitmapHeight > this._maxTextureDimensions)
					{
						currentBitmapHeight = this._maxTextureDimensions;
					}
					bitmapData = this.drawTextFieldRegionToBitmapData(xPosition, yPosition,
						currentBitmapWidth, currentBitmapHeight, bitmapData);
					var newTexture:Texture;
					if(!this.textSnapshot || this._needsNewTexture)
					{
						//skip Texture.fromBitmapData() because we don't want
						//it to create an onRestore function that will be
						//immediately discarded for garbage collection. 
						newTexture = Texture.empty(bitmapData.width / scaleFactor, bitmapData.height / scaleFactor,
							true, false, false, scaleFactor);
						newTexture.root.uploadBitmapData(bitmapData);
					}
					var snapshot:Image = null;
					if(snapshotIndex >= 0)
					{
						if(!this.textSnapshots)
						{
							this.textSnapshots = new <Image>[];
						}
						else if(this.textSnapshots.length > snapshotIndex)
						{
							snapshot = this.textSnapshots[snapshotIndex]
						}
					}
					else
					{
						snapshot = this.textSnapshot;
					}

					if(!snapshot)
					{
						snapshot = new Image(newTexture);
						this.addChild(snapshot);
					}
					else
					{
						if(this._needsNewTexture)
						{
							snapshot.texture.dispose();
							snapshot.texture = newTexture;
							snapshot.readjustSize();
						}
						else
						{
							//this is faster, if we haven't resized the bitmapdata
							var existingTexture:Texture = snapshot.texture;
							existingTexture.root.uploadBitmapData(bitmapData);
						}
					}
					if(newTexture)
					{
						this.createTextureOnRestoreCallback(snapshot);
					}
					if(snapshotIndex >= 0)
					{
						this.textSnapshots[snapshotIndex] = snapshot;
					}
					else
					{
						this.textSnapshot = snapshot;
					}
					snapshot.x = xPosition / scaleFactor;
					snapshot.y = yPosition / scaleFactor;
					if(this._updateSnapshotOnScaleChange)
					{
						snapshot.scaleX = 1 / globalScaleX;
						snapshot.scaleY = 1 / globalScaleY;
						snapshot.x /= globalScaleX;
						snapshot.y /= globalScaleY;
					}
					snapshotIndex++;
					yPosition += currentBitmapHeight;
					totalBitmapHeight -= currentBitmapHeight;
				}
				while(totalBitmapHeight > 0)
				xPosition += currentBitmapWidth;
				totalBitmapWidth -= currentBitmapWidth;
				yPosition = 0;
				totalBitmapHeight = this._snapshotHeight;
			}
			while(totalBitmapWidth > 0)
			bitmapData.dispose();
			if(this.textSnapshots)
			{
				var snapshotCount:int = this.textSnapshots.length;
				for(var i:int = snapshotIndex; i < snapshotCount; i++)
				{
					snapshot = this.textSnapshots[i];
					snapshot.texture.dispose();
					snapshot.removeFromParent(true);
				}
				if(snapshotIndex == 0)
				{
					this.textSnapshots = null;
				}
				else
				{
					this.textSnapshots.length = snapshotIndex;
				}
			}
			if(this._updateSnapshotOnScaleChange)
			{
				this._lastGlobalScaleX = globalScaleX;
				this._lastGlobalScaleY = globalScaleY;
			}
			this._needsNewTexture = false;
		}

		/**
		 * @private
		 */
		protected function enterFrameHandler(event:Event):void
		{
			this.removeEventListener(Event.ENTER_FRAME, enterFrameHandler);
			this.refreshSnapshot();
		}

		/**
		 * @private
		 */
		protected function stateContext_stateChangeHandler(event:Event):void
		{
			this.invalidate(INVALIDATION_FLAG_STATE);
		}
	}
}