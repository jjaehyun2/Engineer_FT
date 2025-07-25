/*
 Copfeathers.themesTheme Josh Tynjala

 Permission is hereby granted, free of charge, to any person
 obtaining a copy of this software and associated documentation
 files (the "Software"), to deal in the Software without
 restriction, including without limitation the rights to use,
 copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the
 Software is furnished to do so, subject to the following
 conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
 */
package feathers.themes
{
	import feathers.controls.Alert;
	import feathers.controls.Button;
	import feathers.controls.ButtonGroup;
	import feathers.controls.Callout;
	import feathers.controls.Check;
	import feathers.controls.GroupedList;
	import feathers.controls.Header;
	import feathers.controls.ImageLoader;
	import feathers.controls.Label;
	import feathers.controls.List;
	import feathers.controls.NumericStepper;
	import feathers.controls.PageIndicator;
	import feathers.controls.Panel;
	import feathers.controls.PanelScreen;
	import feathers.controls.PickerList;
	import feathers.controls.ProgressBar;
	import feathers.controls.Radio;
	import feathers.controls.Screen;
	import feathers.controls.ScrollContainer;
	import feathers.controls.ScrollScreen;
	import feathers.controls.ScrollText;
	import feathers.controls.SimpleScrollBar;
	import feathers.controls.Slider;
	import feathers.controls.TabBar;
	import feathers.controls.TextInput;
	import feathers.controls.ToggleSwitch;
	import feathers.controls.popups.CalloutPopUpContentManager;
	import feathers.controls.popups.VerticalCenteredPopUpContentManager;
	import feathers.controls.renderers.BaseDefaultItemRenderer;
	import feathers.controls.renderers.DefaultGroupedListHeaderOrFooterRenderer;
	import feathers.controls.renderers.DefaultGroupedListItemRenderer;
	import feathers.controls.renderers.DefaultListItemRenderer;
	import feathers.controls.text.BitmapFontTextRenderer;
	import feathers.controls.text.StageTextTextEditor;
	import feathers.core.DisplayListWatcher;
	import feathers.core.FeathersControl;
	import feathers.core.PopUpManager;
	import feathers.display.Scale9Image;
	import feathers.layout.HorizontalLayout;
	import feathers.layout.VerticalLayout;
	import feathers.skins.SmartDisplayObjectStateValueSelector;
	import feathers.skins.StandardIcons;
	import feathers.system.DeviceCapabilities;
	import feathers.text.BitmapFontTextFormat;
	import feathers.textures.Scale3Textures;
	import feathers.textures.Scale9Textures;
	import feathers.utils.math.roundToNearest;

	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.errors.IllegalOperationError;
	import flash.geom.Rectangle;
	import flash.text.TextFormat;
	import flash.text.TextFormatAlign;
	import flash.utils.getQualifiedClassName;

	import starling.core.Starling;
	import starling.display.DisplayObject;
	import starling.display.DisplayObjectContainer;
	import starling.display.Image;
	import starling.display.Quad;
	import starling.events.Event;
	import starling.text.BitmapFont;
	import starling.text.TextField;
	import starling.textures.Texture;
	import starling.textures.TextureAtlas;
	import starling.textures.TextureSmoothing;
	import starling.utils.AssetManager;

	[Event(name="complete",type="starling.events.Event")]

	/**
	 * The "Minimal" theme for mobile Feathers apps.
	 *
	 * <p>This version of the theme requires loading assets at runtime. To use
	 * embedded assets, see <code>MinimalMobileTheme</code> instead.</p>
	 *
	 * <p>To use this theme, the following files must be included when packaging
	 * your app:</p>
	 * <ul>
	 *     <li>images/minimal.png</li>
	 *     <li>images/minimal.xml</li>
	 *     <li>fonts/pf_ronda_seven.fnt</li>
	 * </ul>
	 *
	 * @see http://wiki.starling-framework.org/feathers/theme-assets
	 */
	public class MinimalMobileThemeWithAssetManager extends DisplayListWatcher
	{
		public static const COMPONENT_NAME_PICKER_LIST_ITEM_RENDERER:String = "feathers-mobile-picker-list-item-renderer";
		public static const FONT_NAME:String = "PF Ronda Seven";

		protected static const THEME_NAME_HORIZONTAL_SLIDER_MINIMUM_TRACK:String = "metal-works-mobile-horizontal-slider-minimum-track";
		protected static const THEME_NAME_VERTICAL_SLIDER_MINIMUM_TRACK:String = "metal-works-mobile-vertical-slider-minimum-track";

		protected static const ATLAS_NAME:String = "minimal";
		protected static const FONT_TEXTURE_NAME:String = "pf_ronda_seven_0";

		protected static const SCALE_9_GRID:Rectangle = new Rectangle(9, 9, 2, 2);
		protected static const BUTTON_SCALE_9_GRID:Rectangle = new Rectangle(5, 5, 1, 1);
		protected static const BUTTON_DOWN_SCALE_9_GRID:Rectangle = new Rectangle(9, 9, 1, 1);
		protected static const SCROLLBAR_THUMB_SCALE_9_GRID:Rectangle = new Rectangle(1, 1, 2, 2);
		protected static const TAB_SCALE_9_GRID:Rectangle = new Rectangle(25, 21, 1, 1);
		protected static const HEADER_SCALE_9_GRID:Rectangle = new Rectangle(0, 5, 3, 1);
		protected static const LIST_ITEM_SCALE_9_GRID:Rectangle = new Rectangle(5, 5, 1, 1);
		protected static const BACK_BUTTON_SCALE_REGION1:int = 30;
		protected static const BACK_BUTTON_SCALE_REGION2:int = 1;
		protected static const FORWARD_BUTTON_SCALE_REGION1:int = 9;
		protected static const FORWARD_BUTTON_SCALE_REGION2:int = 1;

		protected static const BACKGROUND_COLOR:uint = 0xf3f3f3;
		protected static const LIST_BACKGROUND_COLOR:uint = 0xf8f8f8;
		protected static const LIST_HEADER_BACKGROUND_COLOR:uint = 0xeeeeee;
		protected static const PRIMARY_TEXT_COLOR:uint = 0x666666;
		protected static const DISABLED_TEXT_COLOR:uint = 0x999999;
		protected static const MODAL_OVERLAY_COLOR:uint = 0x666666;
		protected static const MODAL_OVERLAY_ALPHA:Number = 0.8;

		protected static const ORIGINAL_DPI_IPHONE_RETINA:int = 326;
		protected static const ORIGINAL_DPI_IPAD_RETINA:int = 264;

		protected static function textRendererFactory():BitmapFontTextRenderer
		{
			const renderer:BitmapFontTextRenderer = new BitmapFontTextRenderer();
			//since it's a pixel font, we don't want to smooth it.
			renderer.smoothing = TextureSmoothing.NONE;
			return renderer;
		}

		protected static function textEditorFactory():StageTextTextEditor
		{
			return new StageTextTextEditor();
		}

		protected static function popUpOverlayFactory():DisplayObject
		{
			const quad:Quad = new Quad(100, 100, MODAL_OVERLAY_COLOR);
			quad.alpha = MODAL_OVERLAY_ALPHA;
			return quad;
		}

		public function MinimalMobileThemeWithAssetManager(assets:Object = null, assetManager:AssetManager = null, container:DisplayObjectContainer = null, scaleToDPI:Boolean = true)
		{
			if(!container)
			{
				container = Starling.current.stage;
			}
			super(container);
			this._scaleToDPI = scaleToDPI;
			this.processSource(assets, assetManager);
		}

		protected var _originalDPI:int;

		public function get originalDPI():int
		{
			return this._originalDPI;
		}

		protected var _scaleToDPI:Boolean;

		public function get scaleToDPI():Boolean
		{
			return this._scaleToDPI;
		}

		/**
		 * A subclass may embed the theme's assets and override this setter to
		 * return the class that creates the bitmap used for the texture atlas.
		 */
		protected function get atlasImageClass():Class
		{
			return null;
		}

		/**
		 * A subclass may embed the theme's assets and override this setter to
		 * return the class that creates the XML used for the texture atlas.
		 */
		protected function get atlasXMLClass():Class
		{
			return null;
		}

		/**
		 * A subclass may embed the theme's assets and override this setter to
		 * return the class that creates the XML used for the bitmap font.
		 */
		protected function get fontXMLClass():Class
		{
			return null;
		}

		protected var assetManager:AssetManager;
		protected var scale:Number;
		protected var fontSize:int;
		protected var headingFontSize:int;
		protected var detailFontSize:int;
		protected var inputFontSize:int;

		protected var atlas:TextureAtlas;
		protected var atlasTexture:Texture;

		protected var buttonUpSkinTextures:Scale9Textures;
		protected var buttonDownSkinTextures:Scale9Textures;
		protected var buttonDisabledSkinTextures:Scale9Textures;
		protected var buttonSelectedSkinTextures:Scale9Textures;
		protected var buttonSelectedDisabledSkinTextures:Scale9Textures;
		protected var buttonCallToActionUpSkinTextures:Scale9Textures;
		protected var buttonDangerUpSkinTextures:Scale9Textures;
		protected var buttonDangerDownSkinTextures:Scale9Textures;
		protected var buttonBackUpSkinTextures:Scale3Textures;
		protected var buttonBackDownSkinTextures:Scale3Textures;
		protected var buttonBackDisabledSkinTextures:Scale3Textures;
		protected var buttonForwardUpSkinTextures:Scale3Textures;
		protected var buttonForwardDownSkinTextures:Scale3Textures;
		protected var buttonForwardDisabledSkinTextures:Scale3Textures;

		protected var tabDownSkinTextures:Scale9Textures;
		protected var tabSelectedSkinTextures:Scale9Textures;
		protected var tabSelectedDisabledSkinTextures:Scale9Textures;

		protected var thumbSkinTextures:Scale9Textures;
		protected var thumbDisabledSkinTextures:Scale9Textures;

		protected var scrollBarThumbSkinTextures:Scale9Textures;

		protected var insetBackgroundSkinTextures:Scale9Textures;
		protected var insetBackgroundDisabledSkinTextures:Scale9Textures;

		protected var dropDownArrowTexture:Texture;
		protected var searchIconTexture:Texture;

		protected var listItemUpTextures:Scale9Textures;
		protected var listItemDownTextures:Scale9Textures;
		protected var listItemSelectedTextures:Scale9Textures;
		protected var pickerListItemSelectedIconTexture:Texture;

		protected var headerSkinTextures:Scale9Textures;

		protected var popUpBackgroundSkinTextures:Scale9Textures;
		protected var calloutTopArrowSkinTexture:Texture;
		protected var calloutBottomArrowSkinTexture:Texture;
		protected var calloutLeftArrowSkinTexture:Texture;
		protected var calloutRightArrowSkinTexture:Texture;

		protected var checkIconTexture:Texture;
		protected var checkDisabledIconTexture:Texture;
		protected var checkSelectedIconTexture:Texture;
		protected var checkSelectedDisabledIconTexture:Texture;

		protected var radioIconTexture:Texture;
		protected var radioDisabledIconTexture:Texture;
		protected var radioSelectedIconTexture:Texture;
		protected var radioSelectedDisabledIconTexture:Texture;

		protected var pageIndicatorNormalSkinTexture:Texture;
		protected var pageIndicatorSelectedSkinTexture:Texture;

		protected var primaryTextFormat:BitmapFontTextFormat;
		protected var disabledTextFormat:BitmapFontTextFormat;
		protected var headingTextFormat:BitmapFontTextFormat;
		protected var headingDisabledTextFormat:BitmapFontTextFormat;
		protected var detailTextFormat:BitmapFontTextFormat;
		protected var detailDisabledTextFormat:BitmapFontTextFormat;

		override public function dispose():void
		{
			if(this.root)
			{
				this.root.removeEventListener(Event.ADDED_TO_STAGE, root_addedToStageHandler);
			}
			if(this.atlas)
			{
				this.atlas.dispose();
				this.atlas = null;
				//no need to dispose the atlas texture because the atlas will do that
				this.atlasTexture = null;
			}
			if(this.assetManager)
			{
				this.assetManager.removeTextureAtlas(ATLAS_NAME);
			}
			super.dispose();
		}

		protected function initializeRoot():void
		{
			if(this.root != this.root.stage)
			{
				return;
			}

			this.root.stage.color = BACKGROUND_COLOR;
			Starling.current.nativeStage.color = BACKGROUND_COLOR;
		}

		protected function atlasTexture_onRestore():void
		{
			var AtlasImageClass:Class = this.atlasImageClass;
			var atlasBitmapData:BitmapData = Bitmap(new AtlasImageClass()).bitmapData;
			this.atlasTexture.root.uploadBitmapData(atlasBitmapData);
			atlasBitmapData.dispose();
		}

		protected function assetManager_onProgress(progress:Number):void
		{
			if(progress < 1)
			{
				return;
			}
			this.initialize();
			this.dispatchEventWith(Event.COMPLETE);
		}

		protected function processSource(assets:Object, assetManager:AssetManager):void
		{
			if(assets)
			{
				this.assetManager = assetManager;
				if(!this.assetManager)
				{
					this.assetManager = new AssetManager(Starling.contentScaleFactor);
				}
				//add a trailing slash, if needed
				if(assets is String)
				{
					var assetsDirectoryName:String = assets as String;
					if(assetsDirectoryName.lastIndexOf("/") != assetsDirectoryName.length - 1)
					{
						assets = assetsDirectoryName + "/";
					}
					this.assetManager.enqueue(assets + "images/minimal.xml");
					this.assetManager.enqueue(assets + "images/minimal.png");
					this.assetManager.enqueue(assets + "fonts/pf_ronda_seven.fnt");
				}
				else if(getQualifiedClassName(assets) == "flash.filesystem::File" && assets["isDirectory"])
				{
					this.assetManager.enqueue(assets["resolvePath"]("images/minimal.xml"));
					this.assetManager.enqueue(assets["resolvePath"]("images/minimal.png"));
					this.assetManager.enqueue(assets["resolvePath"]("fonts/pf_ronda_seven.fnt"));
				}
				else
				{
					this.assetManager.enqueue(assets);
				}
				this.assetManager.loadQueue(assetManager_onProgress);
			}
			else
			{
				var AtlasImageClass:Class = this.atlasImageClass;
				var AtlasXMLClass:Class = this.atlasXMLClass;
				var FontXMLClass:Class = this.fontXMLClass;
				if(AtlasImageClass && AtlasXMLClass && FontXMLClass)
				{
					var atlasBitmapData:BitmapData = Bitmap(new AtlasImageClass()).bitmapData;
					this.atlasTexture = Texture.fromBitmapData(atlasBitmapData, false);
					this.atlasTexture.root.onRestore = this.atlasTexture_onRestore;
					atlasBitmapData.dispose();
					this.atlas = new TextureAtlas(atlasTexture, XML(new AtlasXMLClass()));

					var bitmapFont:BitmapFont = new BitmapFont(this.atlas.getTexture(FONT_TEXTURE_NAME), XML(new FontXMLClass()));
					TextField.registerBitmapFont(bitmapFont, FONT_NAME);

					this.initialize();
					this.dispatchEventWith(Event.COMPLETE);
				}
				else
				{
					throw new Error("Asset path or embedded assets not found. Theme not loaded.")
				}
			}
		}

		protected function initialize():void
		{
			if(!this.atlas)
			{
				if(this.assetManager)
				{
					this.atlas = this.assetManager.getTextureAtlas(ATLAS_NAME);
				}
				else
				{
					throw new IllegalOperationError("Atlas not loaded.");
				}
			}

			this.initializeScale();
			this.initializeTextures();
			this.initializeFonts();
			this.initializeGlobals();

			if(this.root.stage)
			{
				this.initializeRoot();
			}
			else
			{
				this.root.addEventListener(Event.ADDED_TO_STAGE, root_addedToStageHandler);
			}

			this.setInitializers();
		}

		protected function initializeGlobals():void
		{
			PopUpManager.overlayFactory = popUpOverlayFactory;
			Callout.stagePaddingTop = Callout.stagePaddingRight = Callout.stagePaddingBottom =
				Callout.stagePaddingLeft = 16 * this.scale;

			FeathersControl.defaultTextRendererFactory = textRendererFactory;
			FeathersControl.defaultTextEditorFactory = textEditorFactory;
		}

		protected function initializeScale():void
		{
			var scaledDPI:int = DeviceCapabilities.dpi / Starling.contentScaleFactor;
			if(this._scaleToDPI)
			{
				if(DeviceCapabilities.isTablet(Starling.current.nativeStage))
				{
					this._originalDPI = ORIGINAL_DPI_IPAD_RETINA;
				}
				else
				{
					this._originalDPI = ORIGINAL_DPI_IPHONE_RETINA;
				}
			}
			else
			{
				this._originalDPI = scaledDPI;
			}
			//our min scale is 0.25 because lines in the graphics are four
			//pixels wide and this will keep them crisp.
			this.scale = Math.max(0.25, scaledDPI / this._originalDPI);
		}

		protected function initializeTextures():void
		{
			this.buttonUpSkinTextures = new Scale9Textures(this.atlas.getTexture("button-up-skin"), BUTTON_SCALE_9_GRID);
			this.buttonDownSkinTextures = new Scale9Textures(this.atlas.getTexture("button-down-skin"), BUTTON_DOWN_SCALE_9_GRID);
			this.buttonDisabledSkinTextures = new Scale9Textures(this.atlas.getTexture("button-disabled-skin"), BUTTON_SCALE_9_GRID);
			this.buttonSelectedSkinTextures = new Scale9Textures(this.atlas.getTexture("button-selected-skin"), BUTTON_DOWN_SCALE_9_GRID);
			this.buttonSelectedDisabledSkinTextures = new Scale9Textures(this.atlas.getTexture("button-selected-disabled-skin"), BUTTON_DOWN_SCALE_9_GRID);
			this.buttonCallToActionUpSkinTextures = new Scale9Textures(this.atlas.getTexture("button-call-to-action-up-skin"), BUTTON_SCALE_9_GRID);
			this.buttonDangerUpSkinTextures = new Scale9Textures(this.atlas.getTexture("button-danger-up-skin"), BUTTON_SCALE_9_GRID);
			this.buttonDangerDownSkinTextures = new Scale9Textures(this.atlas.getTexture("button-danger-down-skin"), BUTTON_DOWN_SCALE_9_GRID);
			this.buttonBackUpSkinTextures = new Scale3Textures(this.atlas.getTexture("button-back-up-skin"), BACK_BUTTON_SCALE_REGION1, BACK_BUTTON_SCALE_REGION2, Scale3Textures.DIRECTION_HORIZONTAL);
			this.buttonBackDownSkinTextures = new Scale3Textures(this.atlas.getTexture("button-back-down-skin"), BACK_BUTTON_SCALE_REGION1, BACK_BUTTON_SCALE_REGION2, Scale3Textures.DIRECTION_HORIZONTAL);
			this.buttonBackDisabledSkinTextures = new Scale3Textures(this.atlas.getTexture("button-back-disabled-skin"), BACK_BUTTON_SCALE_REGION1, BACK_BUTTON_SCALE_REGION2, Scale3Textures.DIRECTION_HORIZONTAL);
			this.buttonForwardUpSkinTextures = new Scale3Textures(this.atlas.getTexture("button-forward-up-skin"), FORWARD_BUTTON_SCALE_REGION1, FORWARD_BUTTON_SCALE_REGION2, Scale3Textures.DIRECTION_HORIZONTAL);
			this.buttonForwardDownSkinTextures = new Scale3Textures(this.atlas.getTexture("button-forward-down-skin"), FORWARD_BUTTON_SCALE_REGION1, FORWARD_BUTTON_SCALE_REGION2, Scale3Textures.DIRECTION_HORIZONTAL);
			this.buttonForwardDisabledSkinTextures = new Scale3Textures(this.atlas.getTexture("button-forward-disabled-skin"), FORWARD_BUTTON_SCALE_REGION1, FORWARD_BUTTON_SCALE_REGION2, Scale3Textures.DIRECTION_HORIZONTAL);

			this.tabDownSkinTextures = new Scale9Textures(this.atlas.getTexture("tab-down-skin"), TAB_SCALE_9_GRID);
			this.tabSelectedSkinTextures = new Scale9Textures(this.atlas.getTexture("tab-selected-skin"), TAB_SCALE_9_GRID);
			this.tabSelectedDisabledSkinTextures = new Scale9Textures(this.atlas.getTexture("tab-selected-disabled-skin"), TAB_SCALE_9_GRID);

			this.thumbSkinTextures = new Scale9Textures(this.atlas.getTexture("thumb-skin"), SCALE_9_GRID);
			this.thumbDisabledSkinTextures = new Scale9Textures(this.atlas.getTexture("thumb-disabled-skin"), SCALE_9_GRID);

			this.scrollBarThumbSkinTextures = new Scale9Textures(this.atlas.getTexture("scrollbar-thumb-skin"), SCROLLBAR_THUMB_SCALE_9_GRID);

			this.insetBackgroundSkinTextures = new Scale9Textures(this.atlas.getTexture("inset-background-skin"), SCALE_9_GRID);
			this.insetBackgroundDisabledSkinTextures = new Scale9Textures(this.atlas.getTexture("inset-background-disabled-skin"), SCALE_9_GRID);

			this.dropDownArrowTexture = this.atlas.getTexture("drop-down-arrow");
			this.searchIconTexture = this.atlas.getTexture("search-icon");

			this.listItemUpTextures = new Scale9Textures(this.atlas.getTexture("list-item-up"), LIST_ITEM_SCALE_9_GRID);
			this.listItemDownTextures = new Scale9Textures(this.atlas.getTexture("list-item-down"), LIST_ITEM_SCALE_9_GRID);
			this.listItemSelectedTextures = new Scale9Textures(this.atlas.getTexture("list-item-selected"), LIST_ITEM_SCALE_9_GRID);
			this.pickerListItemSelectedIconTexture = this.atlas.getTexture("picker-list-item-selected-icon");

			this.headerSkinTextures = new Scale9Textures(this.atlas.getTexture("header-skin"), HEADER_SCALE_9_GRID);

			this.popUpBackgroundSkinTextures = new Scale9Textures(this.atlas.getTexture("callout-background-skin"), BUTTON_SCALE_9_GRID);
			this.calloutTopArrowSkinTexture = this.atlas.getTexture("callout-arrow-top");
			this.calloutBottomArrowSkinTexture = this.atlas.getTexture("callout-arrow-bottom");
			this.calloutLeftArrowSkinTexture = this.atlas.getTexture("callout-arrow-left");
			this.calloutRightArrowSkinTexture = this.atlas.getTexture("callout-arrow-right");

			this.checkIconTexture = this.atlas.getTexture("check-icon");
			this.checkDisabledIconTexture = this.atlas.getTexture("check-disabled-icon");
			this.checkSelectedIconTexture = this.atlas.getTexture("check-selected-icon");
			this.checkSelectedDisabledIconTexture = this.atlas.getTexture("check-selected-disabled-icon");

			this.radioIconTexture = this.atlas.getTexture("radio-icon");
			this.radioDisabledIconTexture = this.atlas.getTexture("radio-disabled-icon");
			this.radioSelectedIconTexture = this.atlas.getTexture("radio-selected-icon");
			this.radioSelectedDisabledIconTexture = this.atlas.getTexture("radio-selected-disabled-icon");

			this.pageIndicatorNormalSkinTexture = this.atlas.getTexture("page-indicator-normal-skin");
			this.pageIndicatorSelectedSkinTexture = this.atlas.getTexture("page-indicator-selected-skin");

			StandardIcons.listDrillDownAccessoryTexture = this.atlas.getTexture("list-accessory-drill-down-icon");
		}

		protected function initializeFonts():void
		{
			//since it's a pixel font, we want a multiple of the original size,
			//which, in this case, is 8.
			this.fontSize = Math.max(4, roundToNearest(24 * this.scale, 8));
			this.headingFontSize = Math.max(4, roundToNearest(32 * this.scale, 8));
			this.detailFontSize = Math.max(4, roundToNearest(16 * this.scale, 8));
			this.inputFontSize = 26 * this.scale;

			this.primaryTextFormat = new BitmapFontTextFormat(FONT_NAME, this.fontSize, PRIMARY_TEXT_COLOR);
			this.disabledTextFormat = new BitmapFontTextFormat(FONT_NAME, this.fontSize, DISABLED_TEXT_COLOR);
			this.headingTextFormat = new BitmapFontTextFormat(FONT_NAME, this.headingFontSize, PRIMARY_TEXT_COLOR);
			this.headingDisabledTextFormat = new BitmapFontTextFormat(FONT_NAME, this.headingFontSize, DISABLED_TEXT_COLOR);
			this.detailTextFormat = new BitmapFontTextFormat(FONT_NAME, this.detailFontSize, PRIMARY_TEXT_COLOR);
			this.detailDisabledTextFormat = new BitmapFontTextFormat(FONT_NAME, this.detailFontSize, DISABLED_TEXT_COLOR);
		}

		protected function setInitializers():void
		{
			//screens
			this.setInitializerForClassAndSubclasses(Screen, screenInitializer);
			this.setInitializerForClassAndSubclasses(PanelScreen, panelScreenInitializer);
			this.setInitializerForClassAndSubclasses(ScrollScreen, scrollScreenInitializer);

			//alert
			this.setInitializerForClass(Alert, alertInitializer);
			this.setInitializerForClass(Header, panelHeaderInitializer, Alert.DEFAULT_CHILD_NAME_HEADER);
			this.setInitializerForClass(ButtonGroup, alertButtonGroupInitializer, Alert.DEFAULT_CHILD_NAME_BUTTON_GROUP);
			this.setInitializerForClass(BitmapFontTextRenderer, alertMessageInitializer, Alert.DEFAULT_CHILD_NAME_MESSAGE);

			//button
			this.setInitializerForClass(Button, buttonInitializer);
			this.setInitializerForClass(Button, buttonCallToActionInitializer, Button.ALTERNATE_NAME_CALL_TO_ACTION_BUTTON);
			this.setInitializerForClass(Button, buttonQuietInitializer, Button.ALTERNATE_NAME_QUIET_BUTTON);
			this.setInitializerForClass(Button, buttonDangerInitializer, Button.ALTERNATE_NAME_DANGER_BUTTON);
			this.setInitializerForClass(Button, buttonBackInitializer, Button.ALTERNATE_NAME_BACK_BUTTON);
			this.setInitializerForClass(Button, buttonForwardInitializer, Button.ALTERNATE_NAME_FORWARD_BUTTON);

			//button group
			this.setInitializerForClass(ButtonGroup, buttonGroupInitializer);
			this.setInitializerForClass(Button, buttonGroupButtonInitializer, ButtonGroup.DEFAULT_CHILD_NAME_BUTTON);

			//callout
			this.setInitializerForClass(Callout, calloutInitializer);

			//check
			this.setInitializerForClass(Check, checkInitializer);

			//grouped list (see also: item renderers)
			this.setInitializerForClass(GroupedList, groupedListInitializer);
			this.setInitializerForClass(GroupedList, groupedListInsetInitializer, GroupedList.ALTERNATE_NAME_INSET_GROUPED_LIST);

			//header
			this.setInitializerForClass(Header, headerInitializer);

			//item renderers for lists
			this.setInitializerForClass(DefaultListItemRenderer, itemRendererInitializer);
			this.setInitializerForClass(DefaultListItemRenderer, pickerListItemRendererInitializer, COMPONENT_NAME_PICKER_LIST_ITEM_RENDERER);
			this.setInitializerForClass(DefaultGroupedListItemRenderer, itemRendererInitializer);

			//header and footer renderers for grouped list
			this.setInitializerForClass(DefaultGroupedListHeaderOrFooterRenderer, headerOrFooterRendererInitializer);
			this.setInitializerForClass(DefaultGroupedListHeaderOrFooterRenderer, insetHeaderOrFooterRendererInitializer, GroupedList.ALTERNATE_CHILD_NAME_INSET_HEADER_RENDERER);
			this.setInitializerForClass(DefaultGroupedListHeaderOrFooterRenderer, insetHeaderOrFooterRendererInitializer, GroupedList.ALTERNATE_CHILD_NAME_INSET_FOOTER_RENDERER);

			//label
			this.setInitializerForClass(Label, labelInitializer);
			this.setInitializerForClass(Label, headingLabelInitializer, Label.ALTERNATE_NAME_HEADING);
			this.setInitializerForClass(Label, detailLabelInitializer, Label.ALTERNATE_NAME_DETAIL);

			//list (see also: item renderers)
			this.setInitializerForClass(List, listInitializer);

			//numeric stepper
			this.setInitializerForClass(NumericStepper, numericStepperInitializer);
			this.setInitializerForClass(TextInput, numericStepperTextInputInitializer, NumericStepper.DEFAULT_CHILD_NAME_TEXT_INPUT);

			//page indicator
			this.setInitializerForClass(PageIndicator, pageIndicatorInitializer);

			//panel
			this.setInitializerForClass(Panel, panelInitializer);
			this.setInitializerForClass(Header, panelHeaderInitializer, Panel.DEFAULT_CHILD_NAME_HEADER);

			//picker list (see also: item renderers)
			this.setInitializerForClass(PickerList, pickerListInitializer);
			this.setInitializerForClass(Button, pickerListButtonInitializer, PickerList.DEFAULT_CHILD_NAME_BUTTON);
			this.setInitializerForClass(List, nothingInitializer, PickerList.DEFAULT_CHILD_NAME_LIST);

			//progress bar
			this.setInitializerForClass(ProgressBar, progressBarInitializer);

			//radio
			this.setInitializerForClass(Radio, radioInitializer);

			//scroll container
			//we don't need an initializer for the ScrollContainer class without
			//a name because it has no background skin and the scroll bars have
			//separate initializers
			this.setInitializerForClass(ScrollContainer, scrollContainerToolbarInitializer, ScrollContainer.ALTERNATE_NAME_TOOLBAR);

			//scroll text
			this.setInitializerForClass(ScrollText, scrollTextInitializer);
			this.setInitializerForClass(BitmapFontTextRenderer, itemRendererAccessoryLabelInitializer, BaseDefaultItemRenderer.DEFAULT_CHILD_NAME_ACCESSORY_LABEL);
			this.setInitializerForClass(BitmapFontTextRenderer, itemRendererIconLabelInitializer, BaseDefaultItemRenderer.DEFAULT_CHILD_NAME_ICON_LABEL);

			//simple scroll bar
			this.setInitializerForClass(Button, simpleScrollBarThumbInitializer, SimpleScrollBar.DEFAULT_CHILD_NAME_THUMB);

			//slider
			this.setInitializerForClass(Slider, sliderInitializer);
			this.setInitializerForClass(Button, sliderThumbInitializer, Slider.DEFAULT_CHILD_NAME_THUMB);
			this.setInitializerForClass(Button, horizontalSliderMinimumTrackInitializer, THEME_NAME_HORIZONTAL_SLIDER_MINIMUM_TRACK);
			this.setInitializerForClass(Button, verticalSliderMinimumTrackInitializer, THEME_NAME_VERTICAL_SLIDER_MINIMUM_TRACK);

			//tab bar
			this.setInitializerForClass(Button, tabInitializer, TabBar.DEFAULT_CHILD_NAME_TAB);

			//text input
			this.setInitializerForClass(TextInput, textInputInitializer);
			this.setInitializerForClass(TextInput, searchTextInputInitializer, TextInput.ALTERNATE_NAME_SEARCH_TEXT_INPUT);

			//toggle switch
			this.setInitializerForClass(ToggleSwitch, toggleSwitchInitializer);
			this.setInitializerForClass(Button, toggleSwitchThumbInitializer, ToggleSwitch.DEFAULT_CHILD_NAME_THUMB);
			this.setInitializerForClass(Button, toggleSwitchOnTrackInitializer, ToggleSwitch.DEFAULT_CHILD_NAME_ON_TRACK);
		}

		protected function pageIndicatorNormalSymbolFactory():DisplayObject
		{
			const symbol:ImageLoader = new ImageLoader();
			symbol.source = this.pageIndicatorNormalSkinTexture;
			symbol.textureScale = this.scale;
			return symbol;
		}

		protected function pageIndicatorSelectedSymbolFactory():DisplayObject
		{
			const symbol:ImageLoader = new ImageLoader();
			symbol.source = this.pageIndicatorSelectedSkinTexture;
			symbol.textureScale = this.scale;
			return symbol;
		}

		protected function imageLoaderFactory():ImageLoader
		{
			const image:ImageLoader = new ImageLoader();
			image.smoothing = TextureSmoothing.NONE;
			image.textureScale = this.scale;
			return image;
		}

		protected function nothingInitializer(target:DisplayObject):void
		{
			//if this is assigned as an initializer, chances are the target will
			//be a subcomponent of something. the initializer for this
			//component's parent is probably handing the initializing for the
			//target too.
		}

		protected function screenInitializer(screen:Screen):void
		{
			screen.originalDPI = this._originalDPI;
		}

		protected function panelScreenInitializer(screen:PanelScreen):void
		{
			screen.originalDPI = this._originalDPI;
		}

		protected function scrollScreenInitializer(screen:ScrollScreen):void
		{
			screen.originalDPI = this._originalDPI;
		}

		protected function labelInitializer(label:Label):void
		{
			label.textRendererProperties.textFormat = this.primaryTextFormat;
			label.textRendererProperties.disabledTextFormat = this.disabledTextFormat;
		}

		protected function headingLabelInitializer(label:Label):void
		{
			label.textRendererProperties.textFormat = this.headingTextFormat;
			label.textRendererProperties.disabledTextFormat = this.headingDisabledTextFormat;
		}

		protected function detailLabelInitializer(label:Label):void
		{
			label.textRendererProperties.textFormat = this.detailTextFormat;
			label.textRendererProperties.disabledTextFormat = this.detailDisabledTextFormat;
		}

		protected function itemRendererAccessoryLabelInitializer(renderer:BitmapFontTextRenderer):void
		{
			renderer.textFormat = this.primaryTextFormat;
		}

		protected function itemRendererIconLabelInitializer(renderer:BitmapFontTextRenderer):void
		{
			renderer.textFormat = this.primaryTextFormat;
		}

		protected function alertMessageInitializer(renderer:BitmapFontTextRenderer):void
		{
			renderer.wordWrap = true;
			renderer.textFormat = this.primaryTextFormat;
		}

		protected function scrollTextInitializer(text:ScrollText):void
		{
			text.textFormat = new TextFormat("PF Ronda Seven,Roboto,Helvetica,Arial,_sans", this.fontSize, PRIMARY_TEXT_COLOR);
			text.paddingTop = text.paddingBottom = text.paddingLeft = 32 * this.scale;
			text.paddingRight = 36 * this.scale;
		}

		protected function baseButtonInitializer(button:Button):void
		{
			button.defaultLabelProperties.textFormat = this.primaryTextFormat;
			button.disabledLabelProperties.textFormat = this.disabledTextFormat;
			button.selectedDisabledLabelProperties.textFormat = this.disabledTextFormat;

			button.paddingTop = button.paddingBottom = 8 * this.scale;
			button.paddingLeft = button.paddingRight = 16 * this.scale;
			button.gap = 12 * this.scale;
			button.minWidth = 66 * this.scale;
			button.minHeight = 66 * this.scale;
			button.minTouchWidth = button.minTouchHeight = 88 * this.scale;
		}

		protected function buttonInitializer(button:Button):void
		{
			const skinSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			skinSelector.defaultValue = this.buttonUpSkinTextures;
			skinSelector.defaultSelectedValue = this.buttonSelectedSkinTextures;
			skinSelector.setValueForState(this.buttonDownSkinTextures, Button.STATE_DOWN, false);
			skinSelector.setValueForState(this.buttonDownSkinTextures, Button.STATE_DOWN, true);
			skinSelector.setValueForState(this.buttonDisabledSkinTextures, Button.STATE_DISABLED, false);
			skinSelector.setValueForState(this.buttonSelectedDisabledSkinTextures, Button.STATE_DISABLED, true);
			skinSelector.displayObjectProperties =
			{
				width: 66 * this.scale,
				height: 66 * this.scale,
				textureScale: this.scale
			};
			button.stateToSkinFunction = skinSelector.updateValue;
			this.baseButtonInitializer(button);
		}

		protected function buttonCallToActionInitializer(button:Button):void
		{
			const skinSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			skinSelector.defaultValue = this.buttonCallToActionUpSkinTextures;
			skinSelector.setValueForState(this.buttonDownSkinTextures, Button.STATE_DOWN, false);
			skinSelector.setValueForState(this.buttonDisabledSkinTextures, Button.STATE_DISABLED, false);
			skinSelector.displayObjectProperties =
			{
				width: 66 * this.scale,
				height: 66 * this.scale,
				textureScale: this.scale
			};
			button.stateToSkinFunction = skinSelector.updateValue;
			this.baseButtonInitializer(button);
		}

		protected function buttonQuietInitializer(button:Button):void
		{
			const skinSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			skinSelector.defaultValue = null;
			skinSelector.defaultSelectedValue = this.buttonSelectedSkinTextures;
			skinSelector.setValueForState(this.buttonDownSkinTextures, Button.STATE_DOWN, false);
			skinSelector.setValueForState(this.buttonDownSkinTextures, Button.STATE_DOWN, true);
			skinSelector.setValueForState(this.buttonDisabledSkinTextures, Button.STATE_DISABLED, false);
			skinSelector.setValueForState(this.buttonSelectedDisabledSkinTextures, Button.STATE_DISABLED, true);
			skinSelector.displayObjectProperties =
			{
				width: 66 * this.scale,
				height: 66 * this.scale,
				textureScale: this.scale
			};
			button.stateToSkinFunction = skinSelector.updateValue;
			this.baseButtonInitializer(button);
		}

		protected function buttonDangerInitializer(button:Button):void
		{
			const skinSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			skinSelector.defaultValue = this.buttonDangerUpSkinTextures;
			skinSelector.setValueForState(this.buttonDangerDownSkinTextures, Button.STATE_DOWN, false);
			skinSelector.setValueForState(this.buttonDisabledSkinTextures, Button.STATE_DISABLED, false);
			skinSelector.displayObjectProperties =
			{
				width: 66 * this.scale,
				height: 66 * this.scale,
				textureScale: this.scale
			};
			button.stateToSkinFunction = skinSelector.updateValue;
			this.baseButtonInitializer(button);
		}

		protected function buttonBackInitializer(button:Button):void
		{
			const skinSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			skinSelector.defaultValue = this.buttonBackUpSkinTextures;
			skinSelector.setValueForState(this.buttonBackDownSkinTextures, Button.STATE_DOWN, false);
			skinSelector.setValueForState(this.buttonBackDisabledSkinTextures, Button.STATE_DISABLED, false);
			skinSelector.displayObjectProperties =
			{
				width: 66 * this.scale,
				height: 66 * this.scale,
				textureScale: this.scale
			};
			button.stateToSkinFunction = skinSelector.updateValue;
			this.baseButtonInitializer(button);
			button.paddingLeft = 38 * this.scale;
		}

		protected function buttonForwardInitializer(button:Button):void
		{
			const skinSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			skinSelector.defaultValue = this.buttonForwardUpSkinTextures;
			skinSelector.setValueForState(this.buttonForwardDownSkinTextures, Button.STATE_DOWN, false);
			skinSelector.setValueForState(this.buttonForwardDisabledSkinTextures, Button.STATE_DISABLED, false);
			skinSelector.displayObjectProperties =
			{
				width: 66 * this.scale,
				height: 66 * this.scale,
				textureScale: this.scale
			};
			button.stateToSkinFunction = skinSelector.updateValue;
			this.baseButtonInitializer(button);
			button.paddingRight = 38 * this.scale
		}

		protected function buttonGroupButtonInitializer(button:Button):void
		{
			const skinSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			skinSelector.defaultValue = this.buttonUpSkinTextures;
			skinSelector.defaultSelectedValue = this.buttonSelectedSkinTextures;
			skinSelector.setValueForState(this.buttonDownSkinTextures, Button.STATE_DOWN, false);
			skinSelector.setValueForState(this.buttonDownSkinTextures, Button.STATE_DOWN, true);
			skinSelector.setValueForState(this.buttonSelectedSkinTextures, Button.STATE_DISABLED, false);
			skinSelector.setValueForState(this.buttonSelectedDisabledSkinTextures, Button.STATE_DISABLED, true);
			skinSelector.displayObjectProperties =
			{
				width: 88 * this.scale,
				height: 88 * this.scale,
				textureScale: this.scale
			};
			button.stateToSkinFunction = skinSelector.updateValue;

			button.defaultLabelProperties.textFormat = this.primaryTextFormat;
			button.disabledLabelProperties.textFormat = this.disabledTextFormat;
			button.selectedDisabledLabelProperties.textFormat = this.disabledTextFormat;

			button.paddingTop = button.paddingBottom = 8 * this.scale;
			button.paddingLeft = button.paddingRight = 16 * this.scale;
			button.gap = 12 * this.scale;
			button.minWidth = 88 * this.scale;
			button.minHeight = 88 * this.scale;
			button.minTouchWidth = button.minTouchHeight = 88 * this.scale;
		}

		protected function tabInitializer(tab:Button):void
		{
			const skinSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			skinSelector.defaultValue = this.headerSkinTextures;
			skinSelector.defaultSelectedValue = this.tabSelectedSkinTextures;
			skinSelector.setValueForState(this.tabDownSkinTextures, Button.STATE_DOWN, false);
			skinSelector.setValueForState(this.tabSelectedDisabledSkinTextures, Button.STATE_DISABLED, true);
			skinSelector.displayObjectProperties =
			{
				width: 88 * this.scale,
				height: 88 * this.scale,
				textureScale: this.scale
			};
			tab.stateToSkinFunction = skinSelector.updateValue;

			tab.defaultLabelProperties.textFormat = this.primaryTextFormat;
			tab.disabledLabelProperties.textFormat = this.disabledTextFormat;
			tab.selectedDisabledLabelProperties.textFormat = this.disabledTextFormat;

			tab.iconPosition = Button.ICON_POSITION_TOP;
			tab.paddingTop = tab.paddingRight = tab.paddingBottom =
				tab.paddingLeft = 28 * this.scale;
			tab.gap = 12 * this.scale;
			tab.minWidth = tab.minHeight = 88 * this.scale;
			tab.minTouchWidth = tab.minTouchHeight = 88 * this.scale;
		}

		protected function simpleScrollBarThumbInitializer(thumb:Button):void
		{
			const defaultSkin:Scale9Image = new Scale9Image(scrollBarThumbSkinTextures, this.scale);
			defaultSkin.width = 8 * this.scale;
			defaultSkin.height = 8 * this.scale;
			thumb.defaultSkin = defaultSkin;

			thumb.minTouchWidth = thumb.minTouchHeight = 12 * this.scale;
		}

		protected function buttonGroupInitializer(group:ButtonGroup):void
		{
			group.minWidth = 560 * this.scale;
			group.gap = 16 * this.scale;
		}

		protected function alertButtonGroupInitializer(group:ButtonGroup):void
		{
			group.direction = ButtonGroup.DIRECTION_VERTICAL;
			group.horizontalAlign = ButtonGroup.HORIZONTAL_ALIGN_JUSTIFY;
			group.verticalAlign = ButtonGroup.VERTICAL_ALIGN_JUSTIFY;
			group.gap = 14 * this.scale;
			group.paddingTop = 14 * this.scale;
			group.paddingRight = 14 * this.scale;
			group.paddingBottom = 14 * this.scale;
			group.paddingLeft = 14 * this.scale;
		}

		protected function sliderInitializer(slider:Slider):void
		{
			slider.trackLayoutMode = Slider.TRACK_LAYOUT_MODE_SINGLE;

			if(slider.direction == Slider.DIRECTION_VERTICAL)
			{
				slider.customMinimumTrackName = THEME_NAME_VERTICAL_SLIDER_MINIMUM_TRACK;
			}
			else //horizontal
			{
				slider.customMinimumTrackName = THEME_NAME_HORIZONTAL_SLIDER_MINIMUM_TRACK;
			}
		}

		protected function horizontalSliderMinimumTrackInitializer(track:Button):void
		{
			var sliderTrackDefaultSkin:Scale9Image = new Scale9Image(insetBackgroundSkinTextures, this.scale);
			sliderTrackDefaultSkin.width = 198 * this.scale;
			sliderTrackDefaultSkin.height = 66 * this.scale;
			track.defaultSkin = sliderTrackDefaultSkin;
		}

		protected function verticalSliderMinimumTrackInitializer(track:Button):void
		{
			var sliderTrackDefaultSkin:Scale9Image = new Scale9Image(insetBackgroundSkinTextures, this.scale);
			sliderTrackDefaultSkin.width = 66 * this.scale;
			sliderTrackDefaultSkin.height = 198 * this.scale;
			track.defaultSkin = sliderTrackDefaultSkin;
		}

		protected function sliderThumbInitializer(thumb:Button):void
		{
			var skinSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			skinSelector.defaultValue = this.thumbSkinTextures;
			skinSelector.defaultSelectedValue = this.thumbDisabledSkinTextures;
			skinSelector.displayObjectProperties =
			{
				width: 66 * this.scale,
				height: 66 * this.scale,
				textureScale: this.scale
			};
			thumb.stateToSkinFunction = skinSelector.updateValue;
			thumb.minTouchWidth = thumb.minTouchHeight = 88 * this.scale;
		}

		protected function numericStepperInitializer(stepper:NumericStepper):void
		{
			stepper.buttonLayoutMode = NumericStepper.BUTTON_LAYOUT_MODE_SPLIT_HORIZONTAL;
			stepper.incrementButtonLabel = "+";
			stepper.decrementButtonLabel = "-";
		}

		protected function toggleSwitchInitializer(toggleSwitch:ToggleSwitch):void
		{
			toggleSwitch.trackLayoutMode = ToggleSwitch.TRACK_LAYOUT_MODE_SINGLE;

			toggleSwitch.defaultLabelProperties.textFormat = this.primaryTextFormat;
			toggleSwitch.disabledLabelProperties.textFormat = this.disabledTextFormat;
		}

		protected function toggleSwitchOnTrackInitializer(track:Button):void
		{
			const skinSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			skinSelector.defaultValue = this.insetBackgroundSkinTextures;
			skinSelector.defaultSelectedValue = this.insetBackgroundDisabledSkinTextures;
			skinSelector.displayObjectProperties =
			{
				width: 148 * this.scale,
				height: 66 * this.scale,
				textureScale: this.scale
			};
			track.stateToSkinFunction = skinSelector.updateValue;
			track.minTouchWidth = track.minTouchHeight = 88 * this.scale;
		}

		protected function toggleSwitchThumbInitializer(thumb:Button):void
		{
			const skinSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			skinSelector.defaultValue = this.thumbSkinTextures;
			skinSelector.defaultSelectedValue = this.thumbDisabledSkinTextures;
			skinSelector.displayObjectProperties =
			{
				width: 66 * this.scale,
				height: 66 * this.scale,
				textureScale: this.scale
			};
			thumb.stateToSkinFunction = skinSelector.updateValue;
			thumb.minTouchWidth = thumb.minTouchHeight = 88 * this.scale;
		}

		protected function checkInitializer(check:Check):void
		{
			const iconSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			iconSelector.defaultValue = this.checkIconTexture;
			iconSelector.defaultSelectedValue = this.checkSelectedIconTexture;
			iconSelector.setValueForState(this.checkDisabledIconTexture, Button.STATE_DISABLED, false);
			iconSelector.setValueForState(this.checkSelectedDisabledIconTexture, Button.STATE_DISABLED, true);
			iconSelector.displayObjectProperties =
			{
				scaleX: this.scale,
				scaleY: this.scale
			};
			check.stateToIconFunction = iconSelector.updateValue;

			check.defaultLabelProperties.textFormat = this.primaryTextFormat;
			check.disabledLabelProperties.textFormat = this.disabledTextFormat;
			check.selectedDisabledLabelProperties.textFormat = this.disabledTextFormat;

			check.gap = 12 * this.scale;
			check.minTouchWidth = check.minTouchHeight = 88 * this.scale;
			check.horizontalAlign = Button.HORIZONTAL_ALIGN_LEFT;
			check.verticalAlign = Button.VERTICAL_ALIGN_MIDDLE;
		}

		protected function radioInitializer(radio:Radio):void
		{
			const iconSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			iconSelector.defaultValue = this.radioIconTexture;
			iconSelector.defaultSelectedValue = this.radioSelectedIconTexture;
			iconSelector.setValueForState(this.radioDisabledIconTexture, Button.STATE_DISABLED, false);
			iconSelector.setValueForState(this.radioSelectedDisabledIconTexture, Button.STATE_DISABLED, true);
			iconSelector.displayObjectProperties =
			{
				scaleX: this.scale,
				scaleY: this.scale
			};
			radio.stateToIconFunction = iconSelector.updateValue;

			radio.defaultLabelProperties.textFormat = this.primaryTextFormat;
			radio.disabledLabelProperties.textFormat = this.disabledTextFormat;
			radio.selectedDisabledLabelProperties.textFormat = this.disabledTextFormat;

			radio.gap = 12 * this.scale;
			radio.minTouchWidth = radio.minTouchHeight = 88 * this.scale;
			radio.horizontalAlign = Button.HORIZONTAL_ALIGN_LEFT;
			radio.verticalAlign = Button.VERTICAL_ALIGN_MIDDLE;
		}

		protected function itemRendererInitializer(renderer:BaseDefaultItemRenderer):void
		{
			const skinSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			skinSelector.defaultValue = this.listItemUpTextures;
			skinSelector.defaultSelectedValue = this.listItemSelectedTextures;
			skinSelector.setValueForState(this.listItemDownTextures, Button.STATE_DOWN, false);
			skinSelector.displayObjectProperties =
			{
				width: 88 * this.scale,
				height: 88 * this.scale,
				textureScale: this.scale
			};
			renderer.stateToSkinFunction = skinSelector.updateValue;

			renderer.defaultLabelProperties.textFormat = this.primaryTextFormat;
			renderer.disabledLabelProperties.textFormat = this.disabledTextFormat;
			renderer.selectedDisabledLabelProperties.textFormat = this.disabledTextFormat;

			renderer.paddingTop = renderer.paddingBottom = 11 * this.scale;
			renderer.paddingLeft = renderer.paddingRight = 16 * this.scale;
			renderer.horizontalAlign = Button.HORIZONTAL_ALIGN_LEFT;
			renderer.minWidth = renderer.minHeight = 88 * this.scale;

			renderer.gap = 10 * this.scale;
			renderer.iconPosition = Button.ICON_POSITION_LEFT;
			renderer.accessoryGap = Number.POSITIVE_INFINITY;
			renderer.accessoryPosition = BaseDefaultItemRenderer.ACCESSORY_POSITION_RIGHT;

			renderer.accessoryLoaderFactory = this.imageLoaderFactory;
			renderer.iconLoaderFactory = this.imageLoaderFactory;
		}

		protected function pickerListItemRendererInitializer(renderer:BaseDefaultItemRenderer):void
		{
			const skinSelector:SmartDisplayObjectStateValueSelector = new SmartDisplayObjectStateValueSelector();
			skinSelector.defaultValue = this.listItemUpTextures;
			skinSelector.setValueForState(this.listItemDownTextures, Button.STATE_DOWN, false);
			skinSelector.displayObjectProperties =
			{
				width: 88 * this.scale,
				height: 88 * this.scale,
				textureScale: this.scale
			};
			renderer.stateToSkinFunction = skinSelector.updateValue;

			const defaultSelectedIcon:ImageLoader = new ImageLoader();
			defaultSelectedIcon.source = this.pickerListItemSelectedIconTexture;
			defaultSelectedIcon.textureScale = this.scale;
			defaultSelectedIcon.snapToPixels = true;
			renderer.defaultSelectedIcon = defaultSelectedIcon;

			var frame:Rectangle = this.pickerListItemSelectedIconTexture.frame;
			if(frame)
			{
				var iconWidth:Number = frame.width;
				var iconHeight:Number = frame.height;
			}
			else
			{
				iconWidth = this.pickerListItemSelectedIconTexture.width;
				iconHeight = this.pickerListItemSelectedIconTexture.height;
			}
			const defaultIcon:Quad = new Quad(iconWidth, iconHeight, 0xff00ff);
			defaultIcon.alpha = 0;
			renderer.defaultIcon = defaultIcon;

			renderer.defaultLabelProperties.textFormat = this.primaryTextFormat;
			renderer.disabledLabelProperties.textFormat = this.disabledTextFormat;
			renderer.selectedDisabledLabelProperties.textFormat = this.disabledTextFormat;

			renderer.paddingTop = renderer.paddingBottom = 11 * this.scale;
			renderer.paddingLeft = renderer.paddingRight = 16 * this.scale;
			renderer.horizontalAlign = Button.HORIZONTAL_ALIGN_LEFT;
			renderer.minWidth = renderer.minHeight = 88 * this.scale;

			renderer.iconPosition = Button.ICON_POSITION_RIGHT;
			renderer.gap = Number.POSITIVE_INFINITY;

			renderer.accessoryLoaderFactory = this.imageLoaderFactory;
			renderer.iconLoaderFactory = this.imageLoaderFactory;
		}

		protected function headerOrFooterRendererInitializer(renderer:DefaultGroupedListHeaderOrFooterRenderer):void
		{
			const backgroundSkin:Quad = new Quad(44 * this.scale, 44 * this.scale, LIST_HEADER_BACKGROUND_COLOR);
			renderer.backgroundSkin = backgroundSkin;

			renderer.contentLabelProperties.textFormat = this.primaryTextFormat;

			renderer.paddingTop = renderer.paddingBottom = 6 * this.scale;
			renderer.paddingLeft = renderer.paddingRight = 24 * this.scale;
			renderer.minWidth = renderer.minHeight = 44 * this.scale;

			renderer.contentLoaderFactory = this.imageLoaderFactory;
		}

		protected function insetHeaderOrFooterRendererInitializer(renderer:DefaultGroupedListHeaderOrFooterRenderer):void
		{
			renderer.contentLabelProperties.textFormat = this.primaryTextFormat;

			renderer.paddingTop = renderer.paddingBottom = 6 * this.scale;
			renderer.paddingLeft = renderer.paddingRight = 24 * this.scale;
			renderer.minWidth = renderer.minHeight = 66 * this.scale;

			renderer.contentLoaderFactory = this.imageLoaderFactory;
		}

		protected function listInitializer(list:List):void
		{
			const backgroundSkin:Quad = new Quad(88 * this.scale, 88 * this.scale, LIST_BACKGROUND_COLOR);
			list.backgroundSkin = backgroundSkin;
		}

		protected function groupedListInitializer(list:GroupedList):void
		{
			const backgroundSkin:Quad = new Quad(88 * this.scale, 88 * this.scale, LIST_BACKGROUND_COLOR);
			list.backgroundSkin = backgroundSkin;
		}

		protected function groupedListInsetInitializer(list:GroupedList):void
		{
			list.headerRendererName = GroupedList.ALTERNATE_CHILD_NAME_INSET_HEADER_RENDERER;
			list.footerRendererName = GroupedList.ALTERNATE_CHILD_NAME_INSET_FOOTER_RENDERER;

			const layout:VerticalLayout = new VerticalLayout();
			layout.useVirtualLayout = true;
			layout.padding = 24 * this.scale;
			layout.paddingTop = 4 * this.scale;
			layout.gap = 0;
			layout.horizontalAlign = VerticalLayout.HORIZONTAL_ALIGN_JUSTIFY;
			layout.verticalAlign = VerticalLayout.VERTICAL_ALIGN_TOP;
			list.layout = layout;
		}

		protected function pickerListInitializer(list:PickerList):void
		{
			if(DeviceCapabilities.isTablet(Starling.current.nativeStage))
			{
				list.popUpContentManager = new CalloutPopUpContentManager();
			}
			else
			{
				const centerStage:VerticalCenteredPopUpContentManager = new VerticalCenteredPopUpContentManager();
				centerStage.marginTop = centerStage.marginRight = centerStage.marginBottom =
					centerStage.marginLeft = 16 * this.scale;
				list.popUpContentManager = centerStage;
			}

			const layout:VerticalLayout = new VerticalLayout();
			layout.verticalAlign = VerticalLayout.VERTICAL_ALIGN_BOTTOM;
			layout.horizontalAlign = VerticalLayout.HORIZONTAL_ALIGN_JUSTIFY;
			layout.useVirtualLayout = true;
			layout.gap = 0;
			layout.paddingTop = layout.paddingRight = layout.paddingBottom =
				layout.paddingLeft = 0;
			list.listProperties.layout = layout;
			list.listProperties.verticalScrollPolicy = List.SCROLL_POLICY_ON;

			if(DeviceCapabilities.isTablet(Starling.current.nativeStage))
			{
				list.listProperties.minWidth = 560 * this.scale;
				list.listProperties.maxHeight = 528 * this.scale;
			}
			else
			{
				const backgroundSkin:Scale9Image = new Scale9Image(popUpBackgroundSkinTextures, this.scale);
				backgroundSkin.width = 20 * this.scale;
				backgroundSkin.height = 20 * this.scale;
				list.listProperties.backgroundSkin = backgroundSkin;
				list.listProperties.paddingTop = list.listProperties.paddingRight =
					list.listProperties.paddingBottom = list.listProperties.paddingLeft = 4 * this.scale;
			}

			list.listProperties.itemRendererName = COMPONENT_NAME_PICKER_LIST_ITEM_RENDERER;
		}

		protected function pickerListButtonInitializer(button:Button):void
		{
			//we're going to expand on the standard button styles
			this.buttonInitializer(button);

			const defaultIcon:Image = new Image(dropDownArrowTexture);
			defaultIcon.scaleX = defaultIcon.scaleY = this.scale;
			button.defaultIcon = defaultIcon;
			button.gap = Number.POSITIVE_INFINITY, //fill as completely as possible
				button.iconPosition = Button.ICON_POSITION_RIGHT;
			button.horizontalAlign =  Button.HORIZONTAL_ALIGN_LEFT;
		}

		protected function headerInitializer(header:Header):void
		{
			header.minWidth = 88 * this.scale;
			header.minHeight = 88 * this.scale;
			header.paddingTop = header.paddingRight = header.paddingBottom =
				header.paddingLeft = 14 * this.scale;
			header.gap = 8 * this.scale;
			header.titleGap = 12 * this.scale;
			const backgroundSkin:Scale9Image = new Scale9Image(headerSkinTextures, this.scale);
			backgroundSkin.width = 88 * this.scale;
			backgroundSkin.height = 88 * this.scale;
			header.backgroundSkin = backgroundSkin;

			header.titleProperties.textFormat = this.primaryTextFormat;
			header.titleProperties.disabledTextFormat = this.disabledTextFormat;
		}

		protected function panelHeaderInitializer(header:Header):void
		{
			header.minWidth = 88 * this.scale;
			header.minHeight = 88 * this.scale;
			header.paddingTop = header.paddingBottom = 18 * this.scale;
			header.paddingLeft = header.paddingRight = 14 * this.scale;
			header.gap = 8 * this.scale;
			header.titleGap = 12 * this.scale;

			const backgroundSkin:Scale9Image = new Scale9Image(popUpBackgroundSkinTextures, this.scale);
			backgroundSkin.width = 88 * this.scale;
			backgroundSkin.height = 88 * this.scale;
			header.backgroundSkin = backgroundSkin;

			header.titleProperties.textFormat = this.primaryTextFormat;
			header.titleProperties.disabledTextFormat = this.disabledTextFormat;
		}

		protected function baseTextInputInitializer(input:TextInput):void
		{
			input.minWidth = input.minHeight = 66 * this.scale;
			input.minTouchWidth = input.minTouchHeight = 66 * this.scale;
			input.gap = 8 * this.scale;
			input.paddingTop = 14 * this.scale;
			input.paddingBottom = 8 * this.scale;
			input.paddingLeft = input.paddingRight = 16 * this.scale;
			input.textEditorProperties.fontFamily = "_sans";
			input.textEditorProperties.fontSize = this.inputFontSize;
			input.textEditorProperties.color = PRIMARY_TEXT_COLOR;

			const backgroundSkin:Scale9Image = new Scale9Image(insetBackgroundSkinTextures, this.scale);
			backgroundSkin.width = 264 * this.scale;
			backgroundSkin.height = 66 * this.scale;
			input.backgroundSkin = backgroundSkin;

			const backgroundDisabledSkin:Scale9Image = new Scale9Image(insetBackgroundDisabledSkinTextures, this.scale);
			backgroundDisabledSkin.width = 264 * this.scale;
			backgroundDisabledSkin.height = 66 * this.scale;
			input.backgroundDisabledSkin = backgroundDisabledSkin;

			input.promptProperties.textFormat = this.primaryTextFormat;
			input.promptProperties.disabledTextFormat = this.disabledTextFormat;
		}

		protected function textInputInitializer(input:TextInput):void
		{
			this.baseTextInputInitializer(input);
		}

		protected function searchTextInputInitializer(input:TextInput):void
		{
			this.baseTextInputInitializer(input);

			var searchIcon:ImageLoader = new ImageLoader();
			searchIcon.source = this.searchIconTexture;
			searchIcon.snapToPixels = true;
			input.defaultIcon = searchIcon;
		}

		protected function numericStepperTextInputInitializer(input:TextInput):void
		{
			input.minWidth = input.minHeight = 66 * this.scale;
			input.minTouchWidth = input.minTouchHeight = 66 * this.scale;
			input.gap = 12 * this.scale;
			input.paddingTop = input.paddingBottom = 14 * this.scale;
			input.paddingLeft = input.paddingRight = 16 * this.scale;
			input.isEditable = false;
			input.textEditorProperties.fontFamily = "_sans";
			input.textEditorProperties.fontSize = this.inputFontSize;
			input.textEditorProperties.color = PRIMARY_TEXT_COLOR;
			input.textEditorProperties.textAlign = TextFormatAlign.CENTER;

			const backgroundSkin:Scale9Image = new Scale9Image(insetBackgroundSkinTextures, this.scale);
			backgroundSkin.width = 66 * this.scale;
			backgroundSkin.height = 66 * this.scale;
			input.backgroundSkin = backgroundSkin;

			const backgroundDisabledSkin:Scale9Image = new Scale9Image(insetBackgroundDisabledSkinTextures, this.scale);
			backgroundDisabledSkin.width = 66 * this.scale;
			backgroundDisabledSkin.height = 66 * this.scale;
			input.backgroundDisabledSkin = backgroundDisabledSkin;
		}

		protected function pageIndicatorInitializer(pageIndicator:PageIndicator):void
		{
			pageIndicator.normalSymbolFactory = this.pageIndicatorNormalSymbolFactory;
			pageIndicator.selectedSymbolFactory = this.pageIndicatorSelectedSymbolFactory;
			pageIndicator.gap = 12 * this.scale;
			pageIndicator.paddingTop = pageIndicator.paddingRight = pageIndicator.paddingBottom =
				pageIndicator.paddingLeft = 12 * this.scale;
			pageIndicator.minTouchWidth = pageIndicator.minTouchHeight = 44 * this.scale;
		}

		protected function progressBarInitializer(progress:ProgressBar):void
		{
			const backgroundSkin:Scale9Image = new Scale9Image(insetBackgroundSkinTextures, this.scale);
			backgroundSkin.width = (progress.direction == ProgressBar.DIRECTION_HORIZONTAL ? 264 : 22) * this.scale;
			backgroundSkin.height = (progress.direction == ProgressBar.DIRECTION_HORIZONTAL ? 22 : 264) * this.scale;
			progress.backgroundSkin = backgroundSkin;

			const backgroundDisabledSkin:Scale9Image = new Scale9Image(insetBackgroundDisabledSkinTextures, this.scale);
			backgroundDisabledSkin.width = (progress.direction == ProgressBar.DIRECTION_HORIZONTAL ? 264 : 22) * this.scale;
			backgroundDisabledSkin.height = (progress.direction == ProgressBar.DIRECTION_HORIZONTAL ? 22 : 264) * this.scale;
			progress.backgroundDisabledSkin = backgroundDisabledSkin;

			const fillSkin:Scale9Image = new Scale9Image(buttonUpSkinTextures, this.scale);
			fillSkin.width = 12 * this.scale;
			fillSkin.height = 12 * this.scale;
			progress.fillSkin = fillSkin;

			const fillDisabledSkin:Scale9Image = new Scale9Image(buttonDisabledSkinTextures, this.scale);
			fillDisabledSkin.width = 12 * this.scale;
			fillDisabledSkin.height = 12 * this.scale;
			progress.fillDisabledSkin = fillDisabledSkin;
		}

		protected function calloutInitializer(callout:Callout):void
		{
			callout.minWidth = 20 * this.scale;
			callout.minHeight = 20 * this.scale;
			callout.paddingTop = callout.paddingRight = callout.paddingBottom =
				callout.paddingLeft = 12 * this.scale;
			const backgroundSkin:Scale9Image = new Scale9Image(popUpBackgroundSkinTextures, this.scale);
			backgroundSkin.width = 20 * this.scale;
			backgroundSkin.height = 20 * this.scale;
			callout.backgroundSkin = backgroundSkin;

			const topArrowSkin:Image = new Image(calloutTopArrowSkinTexture);
			topArrowSkin.scaleX = topArrowSkin.scaleY = this.scale;
			callout.topArrowSkin = topArrowSkin;
			callout.topArrowGap = -8 * this.scale;

			const bottomArrowSkin:Image = new Image(calloutBottomArrowSkinTexture);
			bottomArrowSkin.scaleX = bottomArrowSkin.scaleY = this.scale;
			callout.bottomArrowSkin = bottomArrowSkin;
			callout.bottomArrowGap = -8 * this.scale;

			const leftArrowSkin:Image = new Image(calloutLeftArrowSkinTexture);
			leftArrowSkin.scaleX = leftArrowSkin.scaleY = this.scale;
			callout.leftArrowSkin = leftArrowSkin;
			callout.leftArrowGap = -8 * this.scale;

			const rightArrowSkin:Image = new Image(calloutRightArrowSkinTexture);
			rightArrowSkin.scaleX = rightArrowSkin.scaleY = this.scale;
			callout.rightArrowSkin = rightArrowSkin;
			callout.rightArrowGap = -8 * this.scale;
		}

		protected function panelInitializer(panel:Panel):void
		{
			const backgroundSkin:Scale9Image = new Scale9Image(popUpBackgroundSkinTextures, this.scale);
			backgroundSkin.width = 20 * this.scale;
			backgroundSkin.height = 20 * this.scale;
			panel.backgroundSkin = backgroundSkin;

			panel.paddingTop = panel.paddingRight = panel.paddingBottom =
				panel.paddingLeft = 14 * this.scale;
		}

		protected function alertInitializer(alert:Alert):void
		{
			const backgroundSkin:Scale9Image = new Scale9Image(this.popUpBackgroundSkinTextures, this.scale);
			backgroundSkin.width = 20 * this.scale;
			backgroundSkin.height = 20 * this.scale;
			alert.backgroundSkin = backgroundSkin;

			alert.paddingTop = alert.paddingBottom = 16 * this.scale;
			alert.paddingLeft = alert.paddingRight = 32 * this.scale;
			alert.gap = 32 * this.scale;

			alert.maxWidth = alert.maxHeight = 560 * this.scale;
		}

		protected function scrollContainerToolbarInitializer(container:ScrollContainer):void
		{
			if(!container.layout)
			{
				const layout:HorizontalLayout = new HorizontalLayout();
				layout.paddingTop = layout.paddingRight = layout.paddingBottom =
					layout.paddingLeft = 14 * this.scale;
				layout.gap = 8 * this.scale;
				container.layout = layout;
			}

			container.minWidth = 88 * this.scale;
			container.minHeight = 88 * this.scale;

			const backgroundSkin:Scale9Image = new Scale9Image(headerSkinTextures, this.scale);
			backgroundSkin.width = 88 * this.scale;
			backgroundSkin.height = 88 * this.scale;
			container.backgroundSkin = backgroundSkin;
		}

		protected function root_addedToStageHandler(event:Event):void
		{
			this.initializeRoot();
		}
	}
}