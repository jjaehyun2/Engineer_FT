/**
 * VERSION: 1.851
 * DATE: 2011-04-29
 * AS3
 * UPDATES AND DOCS AT: http://www.greensock.com/loadermax/
 **/
package com.greensock.loading.display {
	import fl.core.UIComponent;

	import com.greensock.loading.core.LoaderItem;

	import flash.display.DisplayObject;
	import flash.display.DisplayObjectContainer;
	import flash.display.Loader;
	import flash.display.LoaderInfo;
	import flash.display.Sprite;
	import flash.geom.Matrix;
	import flash.geom.Rectangle;
/**
 * A container for visual content that is loaded by any of the following: ImageLoaders, SWFLoaders, 
 * or VideoLoaders which is to be used in Flex. It is essentially a UIComponent that has a <code>loader</code> 
 * property for easily referencing the original loader, as well as several other useful properties for 
 * controling the placement of <code>rawContent</code> and the way it is scaled to fit (if at all). That way, 
 * you can add a FlexContentDisplay to the display list or populate an array with as many as you want and then if 
 * you ever need to unload() the content or reload it or figure out its url, etc., you can reference your 
 * FlexContentDisplay's <code>loader</code> property like <code>myContent.loader.url</code> or 
 * <code>(myContent.loader as SWFLoader).getClass("com.greensock.TweenLite");</code>. For
 * <br /><br />
 * 
 * <strong>IMPORTANT</strong>: In order for the LoaderMax loaders to use FlexContentDisplay instead of 
 * the regular ContentDisplay class, you must set the <code>LoaderMax.contentDisplayClass</code> property 
 * to FlexContentDisplay once like:
 * @example Example AS3 code:<listing version="3.0">
 import com.greensock.loading.~~;
 import com.greensock.loading.display.~~;
 
 LoaderMax.contentDisplayClass = FlexContentDisplay;
 </listing>
 * 
 * After that, all ImageLoaders, SWFLoaders, and VideoLoaders will return FlexContentDisplay objects 
 * as their <code>content</code> instead of regular ContentDisplay objects. <br /><br />
 * 
 * <b>Copyright 2011, GreenSock. All rights reserved.</b> This work is subject to the terms in <a href="http://www.greensock.com/terms_of_use.html">http://www.greensock.com/terms_of_use.html</a> or for corporate Club GreenSock members, the software agreement that was issued with the corporate membership.
 * 
 * @author Jack Doyle, jack@greensock.com
 */	
	public class FlexContentDisplay extends UIComponent {
		/** @private **/
		protected static var _transformProps:Object = {x:1, y:1, z:1, rotationX:1, rotationY:1, rotationZ:1, scaleX:1, scaleY:1, rotation:1, alpha:1, visible:true, blendMode:"normal", centerRegistration:false, crop:false, scaleMode:"stretch", hAlign:"center", vAlign:"center"};
		/** @private **/
		protected var _loader:LoaderItem;
		/** @private **/
		protected var _rawContent:DisplayObject;
		/** @private **/
		protected var _centerRegistration:Boolean;
		/** @private **/
		protected var _crop:Boolean;
		/** @private **/
		protected var _scaleMode:String = "stretch";
		/** @private **/
		protected var _hAlign:String = "center";
		/** @private **/
		protected var _vAlign:String = "center";
		/** @private **/
		protected var _bgColor:uint;
		/** @private **/
		protected var _bgAlpha:Number = 0;
		/** @private **/
		protected var _fitWidth:Number;
		/** @private **/
		protected var _fitHeight:Number;
		/** @private only used when crop is true - works around bugs in Flash with the way it reports getBounds() on objects with a scrollRect. **/
		protected var _cropContainer:Sprite;
		
		/** @private A place to reference an object that should be protected from gc - this is used in VideoLoader in order to protect the NetStream object when the loader is disposed. **/
		public var gcProtect:*;
		/** Arbitrary data that you can associate with the FlexContentDisplay instance. For example, you could set <code>data</code> to be an object containing various other properties or set it to an index number related to an array in your application. It is completely optional and arbitrary. **/
		public var data:*;
		
		/**
		 * Constructor
		 * 
		 * @param loader The Loader object that will populate the FlexContentDisplay's <code>rawContent</code>.
		 */
		public function FlexContentDisplay(loader:LoaderItem) {
			super();
			this.loader = loader;
		}
		/**
		 * Removes the FlexContentDisplay from the display list (if necessary), dumps the <code>rawContent</code>,
		 * and calls <code>unload()</code> and <code>dispose()</code> on the loader (unless you define otherwise with 
		 * the optional parameters). This essentially destroys the FlexContentDisplay and makes it eligible for garbage 
		 * collection internally, although if you added any listeners manually, you should remove them as well.
		 * 
		 * @param unloadLoader If <code>true</code>, <code>unload()</code> will be called on the loader. It is <code>true</code> by default.
		 * @param disposeLoader If <code>true</code>, <code>dispose()</code> will be called on the loader. It is <code>true</code> by default.
		 */
		public function dispose(unloadLoader:Boolean=true, disposeLoader:Boolean=true):void {
			if (this.parent != null) {
				if (this.parent.hasOwnProperty("removeElement")) {
					(this.parent as Object).removeElement(this);
				} else {
					this.parent.removeChild(this);
				}
			}
			this.rawContent = null;
			this.gcProtect = null;
			if (_loader != null) {
				if (unloadLoader) {
					_loader.unload();
				}
				if (disposeLoader) {
					_loader.dispose(false);
					_loader = null;
				}
			}
		}
		
		/** @private **/
		protected function _update():void {
			var left:Number = (_centerRegistration && _fitWidth > 0) ? _fitWidth / -2 : 0;
			var top:Number = (_centerRegistration && _fitHeight > 0) ? _fitHeight / -2 : 0;
			graphics.clear();
			if (_fitWidth > 0 && _fitHeight > 0) {
				graphics.beginFill(_bgColor, _bgAlpha);
				graphics.drawRect(left, top, _fitWidth, _fitHeight);
				graphics.endFill();
			}
			if (_rawContent == null) {
				measure();
				return;
			}
			var mc:DisplayObject = _rawContent;
			var contentWidth:Number =  mc.width;
			var contentHeight:Number = mc.height;
			
			if (_loader.hasOwnProperty("getClass")) { //for SWFLoaders, use loaderInfo.width/height so that everything is based on the stage size, not the bounding box of the DisplayObjects that happen to be on the stage (which could be much larger or smaller than the swf's stage)
				var m:Matrix = mc.transform.matrix;
				var loaderInfo:LoaderInfo = (mc is Loader) ? Object(mc).contentLoaderInfo : mc.loaderInfo;
				contentWidth = loaderInfo.width * Math.abs(m.a) + loaderInfo.height * Math.abs(m.b);
				contentHeight = loaderInfo.width * Math.abs(m.c) + loaderInfo.height * Math.abs(m.d);
			}
			
			if (_fitWidth > 0 && _fitHeight > 0) {
				var w:Number = _fitWidth;
				var h:Number = _fitHeight;
				
				var wGap:Number = w - contentWidth;
				var hGap:Number = h - contentHeight;
				
				if (_scaleMode != "none") {
					var displayRatio:Number = w / h;
					var contentRatio:Number = contentWidth / contentHeight;
					if ((contentRatio < displayRatio && _scaleMode == "proportionalInside") || (contentRatio > displayRatio && _scaleMode == "proportionalOutside")) {
						w = h * contentRatio;
					}
					if ((contentRatio > displayRatio && _scaleMode == "proportionalInside") || (contentRatio < displayRatio && _scaleMode == "proportionalOutside")) {
						h = w / contentRatio;
					}
					
					if (_scaleMode != "heightOnly") {
						mc.width *= w / contentWidth;
						wGap = _fitWidth - w;
					} 
					if (_scaleMode != "widthOnly") {
						mc.height *= h / contentHeight;
						hGap = _fitHeight - h;
					}
				}
				
				if (_hAlign == "left") {
					wGap = 0;
				} else if (_hAlign != "right") {
					wGap /= 2;
				}
				if (_vAlign == "top") {
					hGap = 0;
				} else if (_vAlign != "bottom") {
					hGap /= 2;
				}
				
				if (_crop) {
					//due to bugs in the way Flash reports getBounds() on objects with a scrollRect, we need to just wrap the rawContent in a container and apply the scrollRect to the container. 
					if (_cropContainer == null || mc.parent != _cropContainer) {
						_cropContainer = new Sprite();
						this.addChildAt(_cropContainer, this.getChildIndex(mc));
						_cropContainer.addChild(mc);
					}
					_cropContainer.x = left;
					_cropContainer.y = top;
					_cropContainer.scrollRect = new Rectangle(0, 0, _fitWidth, _fitHeight);
					mc.x = wGap;
					mc.y = hGap;
				} else {
					if (_cropContainer != null) {
						this.addChildAt(mc, this.getChildIndex(_cropContainer));
						_cropContainer = null;
					}
					mc.x = left + wGap;
					mc.y = top + hGap;
				}
				
			} else {
				mc.x = (_centerRegistration) ? contentWidth / -2 : 0;
				mc.y = (_centerRegistration) ? contentHeight / -2 : 0;
			}
			measure();
		}
		
		override protected function measure():void {
			var bounds:Rectangle = this.getBounds(this);
			this.explicitWidth = bounds.width;
			this.explicitHeight = bounds.height;
			if (this.parent) {
				bounds = this.getBounds(this.parent);
				this.width = bounds.width;
				this.height = bounds.height;
			}
			super.measure();
		}
		
//---- GETTERS / SETTERS -------------------------------------------------------------------------

		/** 
		 * The width to which the <code>rawContent</code> should be fit according to the FlexContentDisplay's <code>scaleMode</code>
		 * (this width is figured before rotation, scaleX, and scaleY). When a "width" property is defined in the loader's <code>vars</code>
		 * property/parameter, it is automatically applied to this <code>fitWidth</code> property. For example, the following code will
		 * set the loader's FlexContentDisplay <code>fitWidth</code> to 100:<code><br /><br />
		 * 
		 * var loader:ImageLoader = new ImageLoader("photo.jpg", {width:100, height:80, container:this});</code>
		 * 
		 * @see #fitHeight
		 * @see #scaleMode
		 **/
		public function get fitWidth():Number {
			return _fitWidth;
		}
		public function set fitWidth(value:Number):void {
			_fitWidth = value;
			_update();
		}
		
		/** 
		 * The height to which the <code>rawContent</code> should be fit according to the FlexContentDisplay's <code>scaleMode</code>
		 * (this height is figured before rotation, scaleX, and scaleY). When a "height" property is defined in the loader's <code>vars</code>
		 * property/parameter, it is automatically applied to this <code>fitHeight</code> property. For example, the following code will
		 * set the loader's FlexContentDisplay <code>fitHeight</code> to 80:<code><br /><br />
		 * 
		 * var loader:ImageLoader = new ImageLoader("photo.jpg", {width:100, height:80, container:this});</code>
		 * 
		 * @see #fitWidth
		 * @see #scaleMode
		 **/
		public function get fitHeight():Number {
			return _fitHeight;
		}
		public function set fitHeight(value:Number):void {
			_fitHeight = value;
			_update();
		}
		
		/** 
		 * When the FlexContentDisplay's <code>fitWidth</code> and <code>fitHeight</code> properties are defined (or <code>width</code> 
		 * and <code>height</code> in the loader's <code>vars</code> property/parameter), the <code>scaleMode</code> controls how 
		 * the <code>rawContent</code> will be scaled to fit the area. The following values are recognized (you may use the 
		 * <code>com.greensock.layout.ScaleMode</code> constants if you prefer):
		 * <ul>
		 * 		<li><code>"stretch"</code> (the default) - The <code>rawContent</code> will fill the width/height exactly.</li>
		 * 		<li><code>"proportionalInside"</code> - The <code>rawContent</code> will be scaled proportionally to fit inside the area defined by the width/height</li>
		 * 		<li><code>"proportionalOutside"</code> - The <code>rawContent</code> will be scaled proportionally to completely fill the area, allowing portions of it to exceed the bounds defined by the width/height.</li>
		 * 		<li><code>"widthOnly"</code> - Only the width of the <code>rawContent</code> will be adjusted to fit.</li>
		 * 		<li><code>"heightOnly"</code> - Only the height of the <code>rawContent</code> will be adjusted to fit.</li>
		 * 		<li><code>"none"</code> - No scaling of the <code>rawContent</code> will occur.</li>
		 * </ul> 
		 **/
		public function get scaleMode():String {
			return _scaleMode;
		}
		public function set scaleMode(value:String):void {
			if (value == "none" && _rawContent != null) {
				_rawContent.scaleX = _rawContent.scaleY = 1;
			}
			_scaleMode = value;
			_update();
		}
		
		/** 
		 * If <code>true</code>, the FlexContentDisplay's registration point will be placed in the center of the <code>rawContent</code> 
		 * which can be useful if, for example, you want to animate its scale and have it grow/shrink from its center. 
		 * @see #scaleMode
		 **/
		public function get centerRegistration():Boolean {
			return _centerRegistration;
		}
		public function set centerRegistration(value:Boolean):void {
			_centerRegistration = value;
			_update();
		}
		
		/** 
		 * When the FlexContentDisplay's <code>fitWidth</code> and <code>fitHeight</code> properties are defined (or <code>width</code> 
		 * and <code>height</code> in the loader's <code>vars</code> property/parameter), setting <code>crop</code> to 
		 * <code>true</code> will cause the <code>rawContent</code> to be cropped within that area (by applying a <code>scrollRect</code> 
		 * for maximum performance). This is typically useful when the <code>scaleMode</code> is <code>"proportionalOutside"</code> 
		 * or <code>"none"</code> so that any parts of the <code>rawContent</code> that exceed the dimensions defined by 
		 * <code>fitWidth</code> and <code>fitHeight</code> are visually chopped off. Use the <code>hAlign</code> and 
		 * <code>vAlign</code> properties to control the vertical and horizontal alignment within the cropped area. 
		 * 
		 * @see #scaleMode
		 **/
		public function get crop():Boolean {
			return _crop;
		}
		public function set crop(value:Boolean):void {
			_crop = value;
			_update();
		}
		
		/** 
		 * When the FlexContentDisplay's <code>fitWidth</code> and <code>fitHeight</code> properties are defined (or <code>width</code> 
		 * and <code>height</code> in the loader's <code>vars</code> property/parameter), the <code>hAlign</code> determines how 
		 * the <code>rawContent</code> is horizontally aligned within that area. The following values are recognized (you may use the 
		 * <code>com.greensock.layout.AlignMode</code> constants if you prefer):
		 * <ul>
		 * 		<li><code>"center"</code> (the default) - The <code>rawContent</code> will be centered horizontally in the FlexContentDisplay</li>
		 * 		<li><code>"left"</code> - The <code>rawContent</code> will be aligned with the left side of the FlexContentDisplay</li>
		 * 		<li><code>"right"</code> - The <code>rawContent</code> will be aligned with the right side of the FlexContentDisplay</li>
		 * </ul> 
		 * @see #scaleMode
		 * @see #vAlign
		 **/
		public function get hAlign():String {
			return _hAlign;
		}
		public function set hAlign(value:String):void {
			_hAlign = value;
			_update();
		}
		
		/** 
		 * When the FlexContentDisplay's <code>fitWidth</code> and <code>fitHeight</code> properties are defined (or <code>width</code> 
		 * and <code>height</code> in the loader's <code>vars</code> property/parameter), the <code>vAlign</code> determines how 
		 * the <code>rawContent</code> is vertically aligned within that area. The following values are recognized (you may use the 
		 * <code>com.greensock.layout.AlignMode</code> constants if you prefer):
		 * <ul>
		 * 		<li><code>"center"</code> (the default) - The <code>rawContent</code> will be centered vertically in the FlexContentDisplay</li>
		 * 		<li><code>"top"</code> - The <code>rawContent</code> will be aligned with the top of the FlexContentDisplay</li>
		 * 		<li><code>"bottom"</code> - The <code>rawContent</code> will be aligned with the bottom of the FlexContentDisplay</li>
		 * </ul> 
		 * @see #scaleMode
		 * @see #hAlign
		 **/
		public function get vAlign():String {
			return _vAlign;
		}
		public function set vAlign(value:String):void {
			_vAlign = value;
			_update();
		}
		
		/** 
		 * When the FlexContentDisplay's <code>fitWidth</code> and <code>fitHeight</code> properties are defined (or <code>width</code> 
		 * and <code>height</code> in the loader's <code>vars</code> property/parameter), a rectangle will be drawn inside the 
		 * FlexContentDisplay object immediately in order to ease the development process (for example, you can add <code>ROLL_OVER/ROLL_OUT</code>
		 * event listeners immediately). It is transparent by default, but you may define a <code>bgAlpha</code> if you prefer. 
		 * @see #bgAlpha
		 * @see #fitWidth
		 * @see #fitHeight
		 **/
		public function get bgColor():uint {
			return _bgColor;
		}
		public function set bgColor(value:uint):void {
			_bgColor = value;
			_update();
		}
		
		/** 
		 * Controls the alpha of the rectangle that is drawn when the FlexContentDisplay's <code>fitWidth</code> and <code>fitHeight</code> 
		 * properties are defined (or <code>width</code> and <code>height</code> in the loader's <code>vars</code> property/parameter). 
		 * @see #bgColor
		 * @see #fitWidth
		 * @see #fitHeight
		 **/
		public function get bgAlpha():Number {
			return _bgAlpha;
		}
		public function set bgAlpha(value:Number):void {
			_bgAlpha = value;
			_update();
		}
		
		
		/** The raw content which can be a Bitmap, a MovieClip, a Loader, or a Video depending on the type of loader associated with the FlexContentDisplay. **/
		public function get rawContent():* {
			return _rawContent;
		}
		
		public function set rawContent(value:*):void {
			if (_rawContent != null && _rawContent != value) {
				if (_rawContent.parent == this) {
					removeChild(_rawContent);
				} else if (_cropContainer != null && _rawContent.parent == _cropContainer) {
					_cropContainer.removeChild(_rawContent);
					removeChild(_cropContainer);
					_cropContainer = null;
				}
			}
			_rawContent = value as DisplayObject;
			if (_rawContent == null) {
				return;
			}
			addChildAt(_rawContent as DisplayObject, 0);
			_update();
		}
		
		/** The loader whose rawContent populates this FlexContentDisplay. If you get the loader's <code>content</code>, it will return this FlexContentDisplay object. **/
		public function get loader():LoaderItem {
			return _loader;
		}
		
		public function set loader(value:LoaderItem):void {
			_loader = value;
			if (value == null) {
				return;
			} else if (!_loader.hasOwnProperty("setContentDisplay")) {
				throw new Error("Incompatible loader used for a FlexContentDisplay");
			}
			this.name = _loader.name;
			var type:String;
			for (var p:String in _transformProps) {
				if (p in _loader.vars) {
					type = typeof(_transformProps[p]);
					this[p] = (type == "number") ? Number(_loader.vars[p]) : (type == "string") ? String(_loader.vars[p]) : Boolean(_loader.vars[p]);
				}
			}
			_bgColor = uint(_loader.vars.bgColor);
			_bgAlpha = ("bgAlpha" in _loader.vars) ? Number(_loader.vars.bgAlpha) : ("bgColor" in _loader.vars) ? 1 : 0;
			_fitWidth = ("fitWidth" in _loader.vars) ? Number(_loader.vars.fitWidth) : Number(_loader.vars.width);
			_fitHeight = ("fitHeight" in _loader.vars) ? Number(_loader.vars.fitHeight) : Number(_loader.vars.height);
			_update();
			if (_loader.vars.container is DisplayObjectContainer) {
				if (_loader.vars.container.hasOwnProperty("addElement")) {
					(_loader.vars.container as Object).addElement(this);
				} else {
					(_loader.vars.container as DisplayObjectContainer).addChild(this);
				}
			}
			if (_loader.content != this) {
				(_loader as Object).setContentDisplay(this);
			}
			this.rawContent = (_loader as Object).rawContent;
		}
	}
}