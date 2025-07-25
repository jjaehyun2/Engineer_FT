/*
Feathers
Copyright 2012-2014 Joshua Tynjala. All Rights Reserved.

This program is free software. You can redistribute and/or modify it in
accordance with the terms of the accompanying license agreement.
*/
package feathers.controls.text
{
	import feathers.core.FeathersControl;
	import feathers.core.ITextRenderer;
	import feathers.skins.IStyleProvider;

	import flash.display.BitmapData;
	import flash.display.DisplayObjectContainer;
	import flash.display.Sprite;
	import flash.display3D.Context3DProfile;
	import flash.filters.BitmapFilter;
	import flash.geom.Matrix;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.text.engine.ContentElement;
	import flash.text.engine.ElementFormat;
	import flash.text.engine.FontDescription;
	import flash.text.engine.SpaceJustifier;
	import flash.text.engine.TabStop;
	import flash.text.engine.TextBaseline;
	import flash.text.engine.TextBlock;
	import flash.text.engine.TextElement;
	import flash.text.engine.TextJustifier;
	import flash.text.engine.TextLine;
	import flash.text.engine.TextLineValidity;
	import flash.text.engine.TextRotation;

	import starling.core.RenderSupport;
	import starling.core.Starling;
	import starling.display.Image;
	import starling.textures.ConcreteTexture;
	import starling.textures.Texture;
	import starling.utils.getNextPowerOfTwo;

	/**
	 * Renders text with a native <code>flash.text.engine.TextBlock</code> from
	 * Flash Text Engine (FTE), and draws it to <code>BitmapData</code> to
	 * convert to Starling textures. Textures are completely managed by this
	 * component, and they will be automatically disposed when the component is
	 * disposed.
	 *
	 * <p>For longer passages of text, this component will stitch together
	 * multiple individual textures both horizontally and vertically, as a grid,
	 * if required. This may require quite a lot of texture memory, possibly
	 * exceeding the limits of some mobile devices, so use this component with
	 * caution when displaying a lot of text.</p>
	 *
	 * @see http://wiki.starling-framework.org/feathers/text-renderers
	 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/engine/TextBlock.html flash.text.engine.TextBlock
	 */
	public class TextBlockTextRenderer extends FeathersControl implements ITextRenderer
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
		 * @private
		 */
		private static var HELPER_TEXT_LINES:Vector.<TextLine> = new <TextLine>[];

		/**
		 * @private
		 * This is enforced by the runtime.
		 */
		protected static const MAX_TEXT_LINE_WIDTH:Number = 1000000;

		/**
		 * @private
		 */
		protected static const LINE_FEED:String = "\n";

		/**
		 * @private
		 */
		protected static const CARRIAGE_RETURN:String = "\r";

		/**
		 * @private
		 */
		protected static const FUZZY_TRUNCATION_DIFFERENCE:Number = 0.000001;

		/**
		 * The text will be positioned to the left edge.
		 *
		 * @see #textAlign
		 */
		public static const TEXT_ALIGN_LEFT:String = "left";

		/**
		 * The text will be centered horizontally.
		 *
		 * @see #textAlign
		 */
		public static const TEXT_ALIGN_CENTER:String = "center";

		/**
		 * The text will be positioned to the right edge.
		 *
		 * @see #textAlign
		 */
		public static const TEXT_ALIGN_RIGHT:String = "right";

		/**
		 * The default <code>IStyleProvider</code> for all <code>TextBlockTextRenderer</code>
		 * components.
		 *
		 * @default null
		 * @see feathers.core.FeathersControl#styleProvider
		 */
		public static var globalStyleProvider:IStyleProvider;

		/**
		 * Constructor.
		 */
		public function TextBlockTextRenderer()
		{
			super();
			this.isQuickHitAreaEnabled = true;
		}

		/**
		 * The TextBlock instance used to render the text before taking a
		 * texture snapshot.
		 */
		protected var textBlock:TextBlock;

		/**
		 * An image that displays a snapshot of the native <code>TextBlock</code>
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
		protected var _textSnapshotScrollX:Number = 0;

		/**
		 * @private
		 */
		protected var _textSnapshotScrollY:Number = 0;

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
		protected var _textLineContainer:Sprite;

		/**
		 * @private
		 */
		protected var _textLines:Vector.<TextLine> = new <TextLine>[];

		/**
		 * @private
		 */
		protected var _measurementTextLineContainer:Sprite;

		/**
		 * @private
		 */
		protected var _measurementTextLines:Vector.<TextLine> = new <TextLine>[];

		/**
		 * @private
		 */
		protected var _previousContentWidth:Number = NaN;

		/**
		 * @private
		 */
		protected var _previousContentHeight:Number = NaN;

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
		protected var _needsNewTexture:Boolean = false;

		/**
		 * @private
		 */
		protected var _truncationOffset:int = 0;

		/**
		 * @private
		 */
		protected var _textElement:TextElement;

		/**
		 * @private
		 */
		override protected function get defaultStyleProvider():IStyleProvider
		{
			return TextBlockTextRenderer.globalStyleProvider;
		}

		/**
		 * @private
		 */
		protected var _text:String;

		/**
		 * @inheritDoc
		 *
		 * <p>In the following example, the text is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.text = "Lorem ipsum";</listing>
		 *
		 * @default ""
		 */
		public function get text():String
		{
			return this._textElement ? this._text : null;
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
			this._text = value;
			if(!this._textElement)
			{
				this._textElement = new TextElement(value);
			}
			this._textElement.text = value;
			this.content = this._textElement;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var _content:ContentElement;

		/**
		 * Sets the contents of the <code>TextBlock</code> to a complex value
		 * that is more than simple text. If the <code>text</code> property is
		 * set after the <code>content</code> property, the <code>content</code>
		 * property will be replaced with a <code>TextElement</code>.
		 *
		 * <p>In the following example, the content is changed to a
		 * <code>GroupElement</code>:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.content = new GroupElement( element );</listing>
		 *
		 * <p>To simply display a string value, use the <code>text</code> property
		 * instead:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.text = "Lorem Ipsum";</listing>
		 *
		 * @default null
		 *
		 * @see #text
		 */
		public function get content():ContentElement
		{
			return this._content;
		}

		/**
		 * @private
		 */
		public function set content(value:ContentElement):void
		{
			if(this._content == value)
			{
				return;
			}
			if(value is TextElement)
			{
				this._textElement = TextElement(value);
			}
			else
			{
				this._textElement = null;
			}
			this._content = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var _elementFormat:ElementFormat;

		/**
		 * The font and styles used to draw the text. This property will be
		 * ignored if the content is not a <code>TextElement</code> instance.
		 *
		 * <p>In the following example, the element format is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.elementFormat = new ElementFormat( new FontDescription( "Source Sans Pro" ) );</listing>
		 *
		 * @default null
		 *
		 * @see #disabledElementFormat
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/engine/ElementFormat.html flash.text.engine.ElementFormat
		 */
		public function get elementFormat():ElementFormat
		{
			return this._elementFormat;
		}

		/**
		 * @private
		 */
		public function set elementFormat(value:ElementFormat):void
		{
			if(this._elementFormat == value)
			{
				return;
			}
			this._elementFormat = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _disabledElementFormat:ElementFormat;

		/**
		 * The font and styles used to draw the text when the component is
		 * disabled. This property will be ignored if the content is not a
		 * <code>TextElement</code> instance.
		 *
		 * <p>In the following example, the disabled element format is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.isEnabled = false;
		 * textRenderer.disabledElementFormat = new ElementFormat( new FontDescription( "Source Sans Pro" ) );</listing>
		 *
		 * @default null
		 *
		 * @see #elementFormat
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/engine/ElementFormat.html flash.text.engine.ElementFormat
		 */
		public function get disabledElementFormat():ElementFormat
		{
			return this._disabledElementFormat;
		}

		/**
		 * @private
		 */
		public function set disabledElementFormat(value:ElementFormat):void
		{
			if(this._disabledElementFormat == value)
			{
				return;
			}
			this._disabledElementFormat = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _leading:Number = 0;

		/**
		 * The amount of vertical space, in pixels, between lines.
		 *
		 * <p>In the following example, the leading is changed to 20 pixels:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.leading = 20;</listing>
		 *
		 * @default 0
		 */
		public function get leading():Number
		{
			return this._leading;
		}

		/**
		 * @private
		 */
		public function set leading(value:Number):void
		{
			if(this._leading == value)
			{
				return;
			}
			this._leading = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _textAlign:String = TEXT_ALIGN_LEFT;

		/**
		 * The alignment of the text. For justified text, see the
		 * <code>textJustifier</code> property.
		 *
		 * <p>In the following example, the leading is changed to 20 pixels:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.textAlign = TextBlockTextRenderer.TEXT_ALIGN_CENTER;</listing>
		 *
		 * @default TextBlockTextRenderer.TEXT_ALIGN_LEFT
		 *
		 * @see #TEXT_ALIGN_LEFT
		 * @see #TEXT_ALIGN_CENTER
		 * @see #TEXT_ALIGN_RIGHT
		 * @see #textJustifier
		 */
		public function get textAlign():String
		{
			return this._textAlign;
		}

		/**
		 * @private
		 */
		public function set textAlign(value:String):void
		{
			if(this._textAlign == value)
			{
				return;
			}
			this._textAlign = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _wordWrap:Boolean = false;

		/**
		 * Determines if the text wraps to the next line when it reaches the
		 * width of the component.
		 *
		 * <p>In the following example, word wrap is enabled:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.wordWrap = true;</listing>
		 *
		 * @default false
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
		 * @inheritDoc
		 */
		public function get baseline():Number
		{
			if(this._textLines.length == 0)
			{
				return 0;
			}
			return this._textLines[0].ascent;
		}

		/**
		 * @private
		 */
		protected var _applyNonLinearFontScaling:Boolean = true;

		/**
		 * Specifies that you want to enhance screen appearance at the expense
		 * of what-you-see-is-what-you-get (WYSIWYG) print fidelity.
		 *
		 * <p>In the following example, this property is changed to false:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.applyNonLinearFontScaling = false;</listing>
		 *
		 * @default true
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/engine/TextBlock.html#applyNonLinearFontScaling Full description of flash.text.engine.TextBlock.applyNonLinearFontScaling in Adobe's Flash Platform API Reference
		 */
		public function get applyNonLinearFontScaling():Boolean
		{
			return this._applyNonLinearFontScaling;
		}

		/**
		 * @private
		 */
		public function set applyNonLinearFontScaling(value:Boolean):void
		{
			if(this._applyNonLinearFontScaling == value)
			{
				return;
			}
			this._applyNonLinearFontScaling = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _baselineFontDescription:FontDescription;

		/**
		 * The font used to determine the baselines for all the lines created from the block, independent of their content.
		 *
		 * <p>In the following example, the baseline font description is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.baselineFontDescription = new FontDescription( "Source Sans Pro", FontWeight.BOLD );</listing>
		 *
		 * @default null
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/engine/TextBlock.html#baselineFontDescription Full description of flash.text.engine.TextBlock.baselineFontDescription in Adobe's Flash Platform API Reference
		 * @see #baselineFontSize
		 */
		public function get baselineFontDescription():FontDescription
		{
			return this._baselineFontDescription;
		}

		/**
		 * @private
		 */
		public function set baselineFontDescription(value:FontDescription):void
		{
			if(this._baselineFontDescription == value)
			{
				return;
			}
			this._baselineFontDescription = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _baselineFontSize:Number = 12;

		/**
		 * The font size used to calculate the baselines for the lines created
		 * from the block.
		 *
		 * <p>In the following example, the baseline font size is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.baselineFontSize = 20;</listing>
		 *
		 * @default 12
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/engine/TextBlock.html#baselineFontSize Full description of flash.text.engine.TextBlock.baselineFontSize in Adobe's Flash Platform API Reference
		 * @see #baselineFontDescription
		 */
		public function get baselineFontSize():Number
		{
			return this._baselineFontSize;
		}

		/**
		 * @private
		 */
		public function set baselineFontSize(value:Number):void
		{
			if(this._baselineFontSize == value)
			{
				return;
			}
			this._baselineFontSize = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _baselineZero:String = TextBaseline.ROMAN;

		/**
		 * Specifies which baseline is at y=0 for lines created from this block.
		 *
		 * <p>In the following example, the baseline zero is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.baselineZero = TextBaseline.ASCENT;</listing>
		 *
		 * @default TextBaseline.ROMAN
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/engine/TextBlock.html#baselineZero Full description of flash.text.engine.TextBlock.baselineZero in Adobe's Flash Platform API Reference
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/engine/TextBaseline.html flash.text.engine.TextBaseline
		 */
		public function get baselineZero():String
		{
			return this._baselineZero;
		}

		/**
		 * @private
		 */
		public function set baselineZero(value:String):void
		{
			if(this._baselineZero == value)
			{
				return;
			}
			this._baselineZero = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _bidiLevel:int = 0;

		/**
		 * Specifies the bidirectional paragraph embedding level of the text
		 * block.
		 *
		 * <p>In the following example, the bidi level is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.bidiLevel = 1;</listing>
		 *
		 * @default 0
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/engine/TextBlock.html#bidiLevel Full description of flash.text.engine.TextBlock.bidiLevel in Adobe's Flash Platform API Reference
		 */
		public function get bidiLevel():int
		{
			return this._bidiLevel;
		}

		/**
		 * @private
		 */
		public function set bidiLevel(value:int):void
		{
			if(this._bidiLevel == value)
			{
				return;
			}
			this._bidiLevel = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _lineRotation:String = TextRotation.ROTATE_0;

		/**
		 * Rotates the text lines in the text block as a unit.
		 *
		 * <p>In the following example, the line rotation is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.lineRotation = TextRotation.ROTATE_90;</listing>
		 *
		 * @default TextRotation.ROTATE_0
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/engine/TextBlock.html#lineRotation Full description of flash.text.engine.TextBlock.lineRotation in Adobe's Flash Platform API Reference
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/engine/TextRotation.html flash.text.engine.TextRotation
		 */
		public function get lineRotation():String
		{
			return this._lineRotation;
		}

		/**
		 * @private
		 */
		public function set lineRotation(value:String):void
		{
			if(this._lineRotation == value)
			{
				return;
			}
			this._lineRotation = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _tabStops:Vector.<TabStop>;

		/**
		 * Specifies the tab stops for the text in the text block, in the form
		 * of a <code>Vector</code> of <code>TabStop</code> objects.
		 *
		 * <p>In the following example, the tab stops changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.tabStops = new &lt;TabStop&gt;[ new TabStop( TabAlignment.CENTER ) ];</listing>
		 *
		 * @default null
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/engine/TextBlock.html#tabStops Full description of flash.text.engine.TextBlock.tabStops in Adobe's Flash Platform API Reference
		 */
		public function get tabStops():Vector.<TabStop>
		{
			return this._tabStops;
		}

		/**
		 * @private
		 */
		public function set tabStops(value:Vector.<TabStop>):void
		{
			if(this._tabStops == value)
			{
				return;
			}
			this._tabStops = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _textJustifier:TextJustifier = new SpaceJustifier();

		/**
		 * Specifies the <code>TextJustifier</code> to use during line creation.
		 *
		 * <p>In the following example, the text justifier is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.textJustifier = new SpaceJustifier( "en", LineJustification.ALL_BUT_LAST );</listing>
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/engine/TextBlock.html#textJustifier Full description of flash.text.engine.TextBlock.textJustifier in Adobe's Flash Platform API Reference
		 */
		public function get textJustifier():TextJustifier
		{
			return this._textJustifier;
		}

		/**
		 * @private
		 */
		public function set textJustifier(value:TextJustifier):void
		{
			if(this._textJustifier == value)
			{
				return;
			}
			this._textJustifier = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _userData:*;

		/**
		 * Provides a way for the application to associate arbitrary data with
		 * the text block.
		 *
		 * <p>In the following example, the user data is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.userData = { author: "William Shakespeare", title: "Much Ado About Nothing" };</listing>
		 *
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/text/engine/TextBlock.html#userData Full description of flash.text.engine.TextBlock.userData in Adobe's Flash Platform API Reference
		 */
		public function get userData():*
		{
			return this._userData;
		}

		/**
		 * @private
		 */
		public function set userData(value:*):void
		{
			if(this._userData === value)
			{
				return;
			}
			this._userData = value;
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
		 * Native filters to pass to the <code>flash.text.engine.TextLine</code>
		 * instances before creating the texture snapshot.
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
		protected var _truncationText:String = "...";

		/**
		 * The text to display at the end of the label if it is truncated.
		 *
		 * <p>In the following example, the truncation text is changed:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.truncationText = " [more]";</listing>
		 *
		 * @default "..."
		 *
		 * @see #truncateToFit
		 */
		public function get truncationText():String
		{
			return _truncationText;
		}

		/**
		 * @private
		 */
		public function set truncationText(value:String):void
		{
			if(this._truncationText == value)
			{
				return;
			}
			this._truncationText = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var _truncateToFit:Boolean = true;

		/**
		 * If word wrap is disabled, and the text is longer than the width of
		 * the label, the text may be truncated using <code>truncationText</code>.
		 *
		 * <p>This feature may be disabled to improve performance.</p>
		 *
		 * <p>This feature only works when the <code>text</code> property is
		 * set to a string value. If the <code>content</code> property is set
		 * instead, then the content will not be truncated.</p>
		 *
		 * <p>This feature does not currently support the truncation of text
		 * displayed on multiple lines.</p>
		 *
		 * <p>In the following example, truncation is disabled:</p>
		 *
		 * <listing version="3.0">
		 * textRenderer.truncateToFit = false;</listing>
		 *
		 * @default true
		 *
		 * @see #truncationText
		 */
		public function get truncateToFit():Boolean
		{
			return _truncateToFit;
		}

		/**
		 * @private
		 */
		public function set truncateToFit(value:Boolean):void
		{
			if(this._truncateToFit == value)
			{
				return;
			}
			this._truncateToFit = value;
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
			//from being garbage collected, freeing up these things may help
			//ease memory pressure from native filters and other expensive stuff
			this.textBlock = null;
			this._textLineContainer = null;
			this._textLines = null;
			this._measurementTextLineContainer = null;
			this._measurementTextLines = null;
			this._textElement = null;
			this._content = null;

			this._previousContentWidth = NaN;
			this._previousContentHeight = NaN;

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
				if(this._snapToPixels)
				{
					this.getTransformationMatrix(this.stage, HELPER_MATRIX);
					this.textSnapshot.x = this._textSnapshotOffsetX + Math.round(HELPER_MATRIX.tx) - HELPER_MATRIX.tx;
					this.textSnapshot.y = this._textSnapshotOffsetY + Math.round(HELPER_MATRIX.ty) - HELPER_MATRIX.ty;
				}
				else
				{
					this.textSnapshot.x = this._textSnapshotOffsetX;
					this.textSnapshot.y = this._textSnapshotOffsetY;
				}
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
		 * @private
		 */
		override protected function initialize():void
		{
			if(!this.textBlock)
			{
				this.textBlock = new TextBlock();
			}
			if(!this._textLineContainer)
			{
				this._textLineContainer = new Sprite();
			}
			if(!this._measurementTextLineContainer)
			{
				this._measurementTextLineContainer = new Sprite();
			}
		}

		/**
		 * @private
		 */
		override protected function draw():void
		{
			var sizeInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_SIZE);

			this.commit();

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

			if(dataInvalid || stylesInvalid || stateInvalid)
			{
				if(this._textElement)
				{
					if(!this._isEnabled && this._disabledElementFormat)
					{
						this._textElement.elementFormat = this._disabledElementFormat;
					}
					else
					{
						if(!this._elementFormat)
						{
							this._elementFormat = new ElementFormat();
						}
						this._textElement.elementFormat = this._elementFormat;
					}
				}
			}

			if(stylesInvalid)
			{
				this.textBlock.applyNonLinearFontScaling = this._applyNonLinearFontScaling;
				this.textBlock.baselineFontDescription = this._baselineFontDescription;
				this.textBlock.baselineFontSize = this._baselineFontSize;
				this.textBlock.baselineZero = this._baselineZero;
				this.textBlock.bidiLevel = this._bidiLevel;
				this.textBlock.lineRotation = this._lineRotation;
				this.textBlock.tabStops = this._tabStops;
				this.textBlock.textJustifier = this._textJustifier;
				this.textBlock.userData = this._userData;
			}

			if(dataInvalid)
			{
				this.textBlock.content = this._content;
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
			var newWidth:Number = this.explicitWidth;
			var newHeight:Number = this.explicitHeight;
			if(needsWidth)
			{
				newWidth = this._maxWidth;
				if(newWidth > MAX_TEXT_LINE_WIDTH)
				{
					newWidth = MAX_TEXT_LINE_WIDTH;
				}
			}
			if(needsHeight)
			{
				newHeight = this._maxHeight;
			}
			this.refreshTextLines(this._measurementTextLines, this._measurementTextLineContainer, newWidth, newHeight);
			if(needsWidth)
			{
				newWidth = this._measurementTextLineContainer.width;
				if(newWidth > this._maxWidth)
				{
					newWidth = this._maxWidth;
				}
			}
			if(needsHeight)
			{
				newHeight = this._measurementTextLineContainer.height;
				if(newHeight <= 0 && this._elementFormat)
				{
					newHeight = this._elementFormat.fontSize;
				}
			}

			result.x = newWidth;
			result.y = newHeight;

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

			if(sizeInvalid)
			{
				var canUseRectangleTexture:Boolean = Starling.current.profile != Context3DProfile.BASELINE_CONSTRAINED;
				var rectangleSnapshotWidth:Number = this.actualWidth * Starling.contentScaleFactor;
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
				var rectangleSnapshotHeight:Number = this.actualHeight * Starling.contentScaleFactor;
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
				this._needsNewTexture = this._needsNewTexture || !this.textSnapshot || this._snapshotWidth != textureRoot.width || this._snapshotHeight != textureRoot.height;
			}

			//instead of checking sizeInvalid, which will often be triggered by
			//changing maxWidth or something for measurement, we check against
			//the previous actualWidth/Height used for the snapshot.
			if(stylesInvalid || dataInvalid || stateInvalid || this._needsNewTexture ||
				this.actualWidth != this._previousContentWidth ||
				this.actualHeight != this._previousContentHeight)
			{
				this._previousContentWidth = this.actualWidth;
				this._previousContentHeight = this.actualHeight;
				if(this._content)
				{
					this.refreshTextLines(this._textLines, this._textLineContainer, this.actualWidth, this.actualHeight);
					this.refreshSnapshot();
				}
				if(this.textSnapshot)
				{
					this.textSnapshot.visible = this._content !== null;
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
		protected function createTextureOnRestoreCallback(snapshot:Image):void
		{
			var self:TextBlockTextRenderer = this;
			var texture:Texture = snapshot.texture;
			texture.root.onRestore = function():void
			{
				var bitmapData:BitmapData = self.drawTextLinesRegionToBitmapData(
					snapshot.x, snapshot.y, snapshot.width, snapshot.height);
				texture.root.uploadBitmapData(bitmapData);
			};
		}

		/**
		 * @private
		 */
		protected function drawTextLinesRegionToBitmapData(textLinesX:Number, textLinesY:Number,
			bitmapWidth:Number, bitmapHeight:Number, bitmapData:BitmapData = null):BitmapData
		{
			var scaleFactor:Number = Starling.contentScaleFactor;
			var clipWidth:Number = (this.actualWidth * scaleFactor) - textLinesX;
			var clipHeight:Number = (this.actualHeight * scaleFactor) - textLinesY;
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
			HELPER_MATRIX.tx = -textLinesX - this._textSnapshotScrollX;
			HELPER_MATRIX.ty = -textLinesY - this._textSnapshotScrollY;
			HELPER_RECTANGLE.setTo(0, 0, clipWidth, clipHeight);
			bitmapData.draw(this._textLineContainer, HELPER_MATRIX, null, null, HELPER_RECTANGLE);

			var useNativeFilters:Boolean = this._nativeFilters && this._nativeFilters.length > 0 &&
				this._snapshotWidth <= this._maxTextureDimensions && this._snapshotHeight <= this._maxTextureDimensions;
			if(useNativeFilters)
			{
				//check to see if the bitmap data must be resized when the
				//filters are applied.
				this.measureNativeFilters(bitmapData, HELPER_RECTANGLE);
				if(bitmapData.rect.equals(HELPER_RECTANGLE))
				{
					//in the ideal situation, we don't even need to resize the
					//bitmap data.
					this._textSnapshotOffsetX = 0;
					this._textSnapshotOffsetY = 0;
				}
				else
				{
					HELPER_MATRIX.tx -= HELPER_RECTANGLE.x;
					HELPER_MATRIX.ty -= HELPER_RECTANGLE.y;
					var newBitmapData:BitmapData = new BitmapData(HELPER_RECTANGLE.width, HELPER_RECTANGLE.height, true, 0x00ff00ff);
					this._textSnapshotOffsetX = HELPER_RECTANGLE.x;
					this._textSnapshotOffsetY = HELPER_RECTANGLE.y;
					HELPER_RECTANGLE.x = 0;
					HELPER_RECTANGLE.y = 0;
					newBitmapData.draw(this._textLineContainer, HELPER_MATRIX, null, null, HELPER_RECTANGLE);
					bitmapData.dispose();
					bitmapData = newBitmapData;
				}
			}
			else
			{
				this._textSnapshotOffsetX = 0;
				this._textSnapshotOffsetY = 0;
			}
			return bitmapData;
		}

		/**
		 * @private
		 */
		protected function refreshSnapshot():void
		{
			if(this._snapshotWidth == 0 || this._snapshotHeight == 0)
			{
				return;
			}
			var scaleFactor:Number = Starling.contentScaleFactor;
			HELPER_MATRIX.identity();
			HELPER_MATRIX.scale(scaleFactor, scaleFactor);
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
					bitmapData = this.drawTextLinesRegionToBitmapData(xPosition, yPosition,
						currentBitmapWidth, currentBitmapHeight, bitmapData);
					var newTexture:Texture;
					if(!this.textSnapshot || this._needsNewTexture)
					{
						newTexture = Texture.fromBitmapData(bitmapData, false, false, scaleFactor);
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
			this._needsNewTexture = false;
		}

		/**
		 * @private
		 */
		protected function refreshTextLines(textLines:Vector.<TextLine>, textLineParent:DisplayObjectContainer, width:Number, height:Number):void
		{
			if(this._textElement)
			{
				if(this._text)
				{
					this._textElement.text = this._text;
					if(this._text !== null && this._text.charAt(this._text.length - 1) == " ")
					{
						//add an invisible control character because FTE apparently
						//doesn't think that it's important to include trailing
						//spaces in its width measurement.
						this._textElement.text += String.fromCharCode(3);
					}
				}
				else
				{
					//similar to above. this hack ensures that the baseline is
					//measured properly when the text is an empty string.
					this._textElement.text = String.fromCharCode(3);
				}
			}
			HELPER_TEXT_LINES.length = 0;
			var yPosition:Number = 0;
			var lineCount:int = textLines.length;
			var lastLine:TextLine;
			var cacheIndex:int = lineCount;
			for(var i:int = 0; i < lineCount; i++)
			{
				var line:TextLine = textLines[i];
				if(line.validity === TextLineValidity.VALID)
				{
					line.filters = this._nativeFilters;
					lastLine = line;
					textLines[i] = line;
					continue;
				}
				else
				{
					line = lastLine;
					if(lastLine)
					{
						yPosition = lastLine.y;
						//we're using this value in the next loop
						lastLine = null;
					}
					cacheIndex = i;
					break;
				}
			}
			//copy the invalid text lines over to the helper vector so that we
			//can reuse them
			for(; i < lineCount; i++)
			{
				HELPER_TEXT_LINES[int(i - cacheIndex)] = textLines[i];
			}
			textLines.length = cacheIndex;

			if(width >= 0)
			{
				var lineStartIndex:int = 0;
				var canTruncate:Boolean = this._truncateToFit && this._textElement && !this._wordWrap;
				var pushIndex:int = textLines.length;
				var inactiveTextLineCount:int = HELPER_TEXT_LINES.length;
				while(true)
				{
					this._truncationOffset = 0;
					var previousLine:TextLine = line;
					var lineWidth:Number = width;
					if(!this._wordWrap)
					{
						lineWidth = MAX_TEXT_LINE_WIDTH;
					}
					if(inactiveTextLineCount > 0)
					{
						var inactiveLine:TextLine = HELPER_TEXT_LINES[0];
						line = this.textBlock.recreateTextLine(inactiveLine, previousLine, lineWidth, 0, true);
						if(line)
						{
							HELPER_TEXT_LINES.shift();
							inactiveTextLineCount--;
						}
					}
					else
					{
						line = this.textBlock.createTextLine(previousLine, lineWidth, 0, true);
						if(line)
						{
							textLineParent.addChild(line);
						}
					}
					if(!line)
					{
						//end of text
						break;
					}
					var lineLength:int = line.rawTextLength;
					var isTruncated:Boolean = false;
					var difference:Number = 0;
					while(canTruncate && (difference = line.width - width) > FUZZY_TRUNCATION_DIFFERENCE)
					{
						isTruncated = true;
						if(this._truncationOffset == 0)
						{
							//this will quickly skip all of the characters after
							//the maximum width of the line, instead of going
							//one by one.
							var endIndex:int = line.getAtomIndexAtPoint(width, 0);
							if(endIndex >= 0)
							{
								this._truncationOffset = line.rawTextLength - endIndex;
							}
						}
						this._truncationOffset++;
						var truncatedTextLength:int = lineLength - this._truncationOffset;
						//we want to start at this line so that the previous
						//lines don't become invalid.
						this._textElement.text = this._text.substr(lineStartIndex, truncatedTextLength) + this._truncationText;
						var lineBreakIndex:int = this._text.indexOf(LINE_FEED, lineStartIndex);
						if(lineBreakIndex < 0)
						{
							lineBreakIndex = this._text.indexOf(CARRIAGE_RETURN, lineStartIndex);
						}
						if(lineBreakIndex >= 0)
						{
							this._textElement.text += this._text.substr(lineBreakIndex);
						}
						line = this.textBlock.recreateTextLine(line, null, lineWidth, 0, true);
						if(truncatedTextLength <= 0)
						{
							break;
						}
					}
					if(pushIndex > 0)
					{
						yPosition += this._leading;
					}
					yPosition += line.ascent;
					line.y = yPosition;
					yPosition += line.descent;
					line.filters = this._nativeFilters;
					textLines[pushIndex] = line;
					pushIndex++;
					lineStartIndex += lineLength;
				}
			}

			this.alignTextLines(textLines, width, this._textAlign);

			inactiveTextLineCount = HELPER_TEXT_LINES.length;
			for(i = 0; i < inactiveTextLineCount; i++)
			{
				line = HELPER_TEXT_LINES[i];
				textLineParent.removeChild(line);
			}
			HELPER_TEXT_LINES.length = 0;
		}

		/**
		 * @private
		 */
		protected function alignTextLines(textLines:Vector.<TextLine>, width:Number, textAlign:String):void
		{
			var lineCount:int = textLines.length;
			for(var i:int = 0; i < lineCount; i++)
			{
				var line:TextLine = textLines[i];
				if(textAlign == TEXT_ALIGN_CENTER)
				{
					line.x = (width - line.width) / 2;
				}
				else if(textAlign == TEXT_ALIGN_RIGHT)
				{
					line.x = width - line.width;
				}
				else
				{
					line.x = 0;
				}
			}
		}
	}
}