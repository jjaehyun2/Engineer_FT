/*
Feathers
Copyright 2012-2016 Bowler Hat LLC. All Rights Reserved.

This program is free software. You can redistribute and/or modify it in
accordance with the terms of the accompanying license agreement.
*/
package feathers.controls
{
	import feathers.core.FeathersControl;
	import feathers.core.IFeathersControl;
	import feathers.core.IMeasureDisplayObject;
	import feathers.core.IValidating;
	import feathers.layout.Direction;
	import feathers.skins.IStyleProvider;
	import feathers.utils.math.clamp;
	import feathers.utils.skins.resetFluidChildDimensionsForMeasurement;

	import starling.display.DisplayObject;

	/**
	 * The primary background to display in the progress bar. The background
	 * skin is displayed below the fill skin, and the fill skin is affected
	 * by the padding, and the background skin may be seen around the edges.
	 *
	 * <p>The original width or height of the background skin will be one
	 * of the values used to calculate the width or height of the progress
	 * bar, if the <code>width</code> and <code>height</code> properties are
	 * not set explicitly. The fill skin and padding values will also be
	 * used.</p>
	 *
	 * <p>If the background skin is a Feathers component, the
	 * <code>minWidth</code> or <code>minHeight</code> properties will be
	 * one of the values used to calculate the width or height of the
	 * progress bar. If the background skin is a regular Starling display
	 * object, the original width and height of the display object will be
	 * used to calculate the minimum dimensions instead.</p>
	 *
	 * <p>In the following example, the progress bar is given a background
	 * skin:</p>
	 *
	 * <listing version="3.0">
	 * progress.backgroundSkin = new Image( texture );</listing>
	 *
	 * @default null
	 * 
	 * @see #style:backgroundDisabledSkin
	 * @see #style:fillSkin
	 */
	[Style(name="backgroundSkin",type="starling.display.DisplayObject")]

	/**
	 * A background to display when the progress bar is disabled.
	 *
	 * <p>In the following example, the progress bar is given a disabled
	 * background skin:</p>
	 *
	 * <listing version="3.0">
	 * progress.backgroundDisabledSkin = new Image( texture );</listing>
	 *
	 * @default null
	 *
	 * @see #style:backgroundSkin
	 * @see #style:fillDisabledSkin
	 */
	[Style(name="backgroundDisabledSkin",type="starling.display.DisplayObject")]

	/**
	 * Determines the direction that the progress bar fills. When this value
	 * changes, the progress bar's width and height values do not change
	 * automatically.
	 *
	 * <p>In the following example, the direction is set to vertical:</p>
	 *
	 * <listing version="3.0">
	 * progress.direction = Direction.VERTICAL;</listing>
	 *
	 * @default feathers.layout.Direction.HORIZONTAL
	 *
	 * @see feathers.layout.Direction#HORIZONTAL
	 * @see feathers.layout.Direction#VERTICAL
	 */
	[Style(name="direction",type="String")]

	/**
	 * The primary fill to display in the progress bar. The fill skin is
	 * displayed over the background skin, with padding around the edges of
	 * the fill skin to reveal the background skin behind.
	 *
	 * <p>Note: The size of the <code>fillSkin</code>, at the time that it
	 * is passed to the setter, will be used used as the size of the fill
	 * when the progress bar is set to the minimum value. In other words,
	 * if the fill of a horizontal progress bar with a value from 0 to 100
	 * should be virtually invisible when the value is 0, then the
	 * <code>fillSkin</code> should have a width of 0 when you pass it in.
	 * On the other hand, if you're using an <code>Image</code> with a
	 * <code>scale9Grid</code> as the skin, it may require a minimum width
	 * before the image parts begin to overlap. In that case, the
	 * <code>Image</code> instance passed to the <code>fillSkin</code>
	 * setter should have a <code>width</code> value that is the same as
	 * that minimum width value where the image parts do not overlap.</p>
	 *
	 * <p>In the following example, the progress bar is given a fill
	 * skin:</p>
	 *
	 * <listing version="3.0">
	 * progress.fillSkin = new Image( texture );</listing>
	 *
	 * @default null
	 *
	 * @see #style:fillDisabledSkin
	 * @see #style:backgroundSkin
	 */
	[Style(name="fillSkin",type="starling.display.DisplayObject")]

	/**
	 * A fill to display when the progress bar is disabled.
	 *
	 * <p>In the following example, the progress bar is given a disabled fill
	 * skin:</p>
	 *
	 * <listing version="3.0">
	 * progress.fillDisabledSkin = new Image( texture );</listing>
	 *
	 * @default null
	 *
	 * @see #style:fillSkin
	 * @see #style:backgroundDisabledSkin
	 */
	[Style(name="fillDisabledSkin",type="starling.display.DisplayObject")]

	/**
	 * Quickly sets all padding properties to the same value. The
	 * <code>padding</code> getter always returns the value of
	 * <code>paddingTop</code>, but the other padding values may be
	 * different.
	 *
	 * <p>In the following example, the padding is set to 20 pixels:</p>
	 *
	 * <listing version="3.0">
	 * progress.padding = 20;</listing>
	 *
	 * @default 0
	 *
	 * @see #style:paddingTop
	 * @see #style:paddingRight
	 * @see #style:paddingBottom
	 * @see #style:paddingLeft
	 */
	[Style(name="padding",type="Number")]

	/**
	 * The minimum space, in pixels, between the progress bar's top edge and
	 * the progress bar's content.
	 *
	 * <p>In the following example, the top padding is set to 20 pixels:</p>
	 *
	 * <listing version="3.0">
	 * progress.paddingTop = 20;</listing>
	 *
	 * @default 0
	 *
	 * @see #style:padding
	 */
	[Style(name="paddingTop",type="Number")]

	/**
	 * The minimum space, in pixels, between the progress bar's right edge
	 * and the progress bar's content.
	 *
	 * <p>In the following example, the right padding is set to 20 pixels:</p>
	 *
	 * <listing version="3.0">
	 * progress.paddingRight = 20;</listing>
	 *
	 * @default 0
	 *
	 * @see #style:padding
	 */
	[Style(name="paddingRight",type="Number")]

	/**
	 * The minimum space, in pixels, between the progress bar's bottom edge
	 * and the progress bar's content.
	 *
	 * <p>In the following example, the bottom padding is set to 20 pixels:</p>
	 *
	 * <listing version="3.0">
	 * progress.paddingBottom = 20;</listing>
	 *
	 * @default 0
	 *
	 * @see #style:padding
	 */
	[Style(name="paddingBottom",type="Number")]

	/**
	 * The minimum space, in pixels, between the progress bar's left edge
	 * and the progress bar's content.
	 *
	 * <p>In the following example, the left padding is set to 20 pixels:</p>
	 *
	 * <listing version="3.0">
	 * progress.paddingLeft = 20;</listing>
	 *
	 * @default 0
	 *
	 * @see #style:padding
	 */
	[Style(name="paddingLeft",type="Number")]

	/**
	 * Displays the progress of a task over time. Non-interactive.
	 *
	 * <p>The following example creates a progress bar:</p>
	 *
	 * <listing version="3.0">
	 * var progress:ProgressBar = new ProgressBar();
	 * progress.minimum = 0;
	 * progress.maximum = 100;
	 * progress.value = 20;
	 * this.addChild( progress );</listing>
	 *
	 * @see ../../../help/progress-bar.html How to use the Feathers ProgressBar component
	 */
	public class ProgressBar extends FeathersControl
	{
		/**
		 * @private
		 * DEPRECATED: Replaced by <code>feathers.layout.Direction.HORIZONTAL</code>.
		 *
		 * <p><strong>DEPRECATION WARNING:</strong> This constant is deprecated
		 * starting with Feathers 3.0. It will be removed in a future version of
		 * Feathers according to the standard
		 * <a target="_top" href="../../../help/deprecation-policy.html">Feathers deprecation policy</a>.</p>
		 */
		public static const DIRECTION_HORIZONTAL:String = "horizontal";

		/**
		 * @private
		 * DEPRECATED: Replaced by <code>feathers.layout.Direction.VERTICAL</code>.
		 *
		 * <p><strong>DEPRECATION WARNING:</strong> This constant is deprecated
		 * starting with Feathers 3.0. It will be removed in a future version of
		 * Feathers according to the standard
		 * <a target="_top" href="../../../help/deprecation-policy.html">Feathers deprecation policy</a>.</p>
		 */
		public static const DIRECTION_VERTICAL:String = "vertical";

		/**
		 * The default <code>IStyleProvider</code> for all <code>ProgressBar</code>
		 * components.
		 *
		 * @default null
		 * @see feathers.core.FeathersControl#styleProvider
		 */
		public static var globalStyleProvider:IStyleProvider;

		/**
		 * Constructor.
		 */
		public function ProgressBar()
		{
			super();
		}

		/**
		 * @private
		 */
		override protected function get defaultStyleProvider():IStyleProvider
		{
			return ProgressBar.globalStyleProvider;
		}

		/**
		 * @private
		 */
		protected var _direction:String = Direction.HORIZONTAL;

		[Inspectable(type="String",enumeration="horizontal,vertical")]
		/**
		 * @private
		 */
		public function get direction():String
		{
			return this._direction;
		}

		/**
		 * @private
		 */
		public function set direction(value:String):void
		{
			if(this.processStyleRestriction(arguments.callee))
			{
				return;
			}
			if(this._direction === value)
			{
				return;
			}
			this._direction = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var _value:Number = 0;

		/**
		 * The value of the progress bar, between the minimum and maximum.
		 *
		 * <p>In the following example, the value is set to 12:</p>
		 *
		 * <listing version="3.0">
		 * progress.minimum = 0;
		 * progress.maximum = 100;
		 * progress.value = 12;</listing>
		 *
		 * @default 0
		 *
		 * @see #minimum
		 * @see #maximum
		 */
		public function get value():Number
		{
			return this._value;
		}

		/**
		 * @private
		 */
		public function set value(newValue:Number):void
		{
			newValue = clamp(newValue, this._minimum, this._maximum);
			if(this._value == newValue)
			{
				return;
			}
			this._value = newValue;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var _minimum:Number = 0;

		/**
		 * The progress bar's value will not go lower than the minimum.
		 *
		 * <p>In the following example, the minimum is set to 0:</p>
		 *
		 * <listing version="3.0">
		 * progress.minimum = 0;
		 * progress.maximum = 100;
		 * progress.value = 12;</listing>
		 *
		 * @default 0
		 *
		 * @see #value
		 * @see #maximum
		 */
		public function get minimum():Number
		{
			return this._minimum;
		}

		/**
		 * @private
		 */
		public function set minimum(value:Number):void
		{
			if(this._minimum == value)
			{
				return;
			}
			this._minimum = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var _maximum:Number = 1;

		/**
		 * The progress bar's value will not go higher than the maximum.
		 *
		 * <p>In the following example, the maximum is set to 100:</p>
		 *
		 * <listing version="3.0">
		 * progress.minimum = 0;
		 * progress.maximum = 100;
		 * progress.value = 12;</listing>
		 *
		 * @default 1
		 *
		 * @see #value
		 * @see #minimum
		 */
		public function get maximum():Number
		{
			return this._maximum;
		}

		/**
		 * @private
		 */
		public function set maximum(value:Number):void
		{
			if(this._maximum == value)
			{
				return;
			}
			this._maximum = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var _explicitBackgroundWidth:Number;

		/**
		 * @private
		 */
		protected var _explicitBackgroundHeight:Number;

		/**
		 * @private
		 */
		protected var _explicitBackgroundMinWidth:Number;

		/**
		 * @private
		 */
		protected var _explicitBackgroundMinHeight:Number;

		/**
		 * @private
		 */
		protected var _explicitBackgroundMaxWidth:Number;

		/**
		 * @private
		 */
		protected var _explicitBackgroundMaxHeight:Number;

		/**
		 * @private
		 */
		protected var currentBackground:DisplayObject;

		/**
		 * @private
		 */
		protected var _backgroundSkin:DisplayObject;

		/**
		 * @private
		 */
		public function get backgroundSkin():DisplayObject
		{
			return this._backgroundSkin;
		}

		/**
		 * @private
		 */
		public function set backgroundSkin(value:DisplayObject):void
		{
			if(this.processStyleRestriction(arguments.callee))
			{
				if(value !== null)
				{
					value.dispose();
				}
				return;
			}
			if(this._backgroundSkin === value)
			{
				return;
			}
			if(this._backgroundSkin && this._backgroundSkin != this._backgroundDisabledSkin)
			{
				this.removeChild(this._backgroundSkin);
			}
			this._backgroundSkin = value;
			if(this._backgroundSkin && this._backgroundSkin.parent != this)
			{
				this._backgroundSkin.visible = false;
				this.addChildAt(this._backgroundSkin, 0);
			}
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _backgroundDisabledSkin:DisplayObject;

		/**
		 * @private
		 */
		public function get backgroundDisabledSkin():DisplayObject
		{
			return this._backgroundDisabledSkin;
		}

		/**
		 * @private
		 */
		public function set backgroundDisabledSkin(value:DisplayObject):void
		{
			if(this.processStyleRestriction(arguments.callee))
			{
				if(value !== null)
				{
					value.dispose();
				}
				return;
			}
			if(this._backgroundDisabledSkin === value)
			{
				return;
			}
			if(this._backgroundDisabledSkin && this._backgroundDisabledSkin != this._backgroundSkin)
			{
				this.removeChild(this._backgroundDisabledSkin);
			}
			this._backgroundDisabledSkin = value;
			if(this._backgroundDisabledSkin && this._backgroundDisabledSkin.parent != this)
			{
				this._backgroundDisabledSkin.visible = false;
				this.addChildAt(this._backgroundDisabledSkin, 0);
			}
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 * The width of the first fill skin that was displayed.
		 */
		protected var _originalFillWidth:Number = NaN;

		/**
		 * @private
		 * The width of the first fill skin that was displayed.
		 */
		protected var _originalFillHeight:Number = NaN;

		/**
		 * @private
		 */
		protected var currentFill:DisplayObject;

		/**
		 * @private
		 */
		protected var _fillSkin:DisplayObject;

		/**
		 * @private
		 */
		public function get fillSkin():DisplayObject
		{
			return this._fillSkin;
		}

		/**
		 * @private
		 */
		public function set fillSkin(value:DisplayObject):void
		{
			if(this.processStyleRestriction(arguments.callee))
			{
				if(value !== null)
				{
					value.dispose();
				}
				return;
			}
			if(this._fillSkin === value)
			{
				return;
			}
			if(this._fillSkin && this._fillSkin != this._fillDisabledSkin)
			{
				this.removeChild(this._fillSkin);
			}
			this._fillSkin = value;
			if(this._fillSkin && this._fillSkin.parent != this)
			{
				this._fillSkin.visible = false;
				this.addChild(this._fillSkin);
			}
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _fillDisabledSkin:DisplayObject;

		/**
		 * @private
		 */
		public function get fillDisabledSkin():DisplayObject
		{
			return this._fillDisabledSkin;
		}

		/**
		 * @private
		 */
		public function set fillDisabledSkin(value:DisplayObject):void
		{
			if(this.processStyleRestriction(arguments.callee))
			{
				if(value !== null)
				{
					value.dispose();
				}
				return;
			}
			if(this._fillDisabledSkin === value)
			{
				return;
			}
			if(this._fillDisabledSkin && this._fillDisabledSkin != this._fillSkin)
			{
				this.removeChild(this._fillDisabledSkin);
			}
			this._fillDisabledSkin = value;
			if(this._fillDisabledSkin && this._fillDisabledSkin.parent != this)
			{
				this._fillDisabledSkin.visible = false;
				this.addChild(this._fillDisabledSkin);
			}
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		public function get padding():Number
		{
			return this._paddingTop;
		}

		/**
		 * @private
		 */
		public function set padding(value:Number):void
		{
			this.paddingTop = value;
			this.paddingRight = value;
			this.paddingBottom = value;
			this.paddingLeft = value;
		}

		/**
		 * @private
		 */
		protected var _paddingTop:Number = 0;

		/**
		 * @private
		 */
		public function get paddingTop():Number
		{
			return this._paddingTop;
		}

		/**
		 * @private
		 */
		public function set paddingTop(value:Number):void
		{
			if(this.processStyleRestriction(arguments.callee))
			{
				return;
			}
			if(this._paddingTop === value)
			{
				return;
			}
			this._paddingTop = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _paddingRight:Number = 0;

		/**
		 * @private
		 */
		public function get paddingRight():Number
		{
			return this._paddingRight;
		}

		/**
		 * @private
		 */
		public function set paddingRight(value:Number):void
		{
			if(this.processStyleRestriction(arguments.callee))
			{
				return;
			}
			if(this._paddingRight === value)
			{
				return;
			}
			this._paddingRight = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _paddingBottom:Number = 0;

		/**
		 * @private
		 */
		public function get paddingBottom():Number
		{
			return this._paddingBottom;
		}

		/**
		 * @private
		 */
		public function set paddingBottom(value:Number):void
		{
			if(this.processStyleRestriction(arguments.callee))
			{
				return;
			}
			if(this._paddingBottom === value)
			{
				return;
			}
			this._paddingBottom = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		protected var _paddingLeft:Number = 0;

		/**
		 * @private
		 */
		public function get paddingLeft():Number
		{
			return this._paddingLeft;
		}

		/**
		 * @private
		 */
		public function set paddingLeft(value:Number):void
		{
			if(this.processStyleRestriction(arguments.callee))
			{
				return;
			}
			if(this._paddingLeft === value)
			{
				return;
			}
			this._paddingLeft = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		/**
		 * @private
		 */
		override protected function draw():void
		{
			var stylesInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_STYLES);
			var stateInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_STATE);
			var sizeInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_SIZE);

			if(stylesInvalid || stateInvalid)
			{
				this.refreshBackground();
				this.refreshFill();
			}

			this.autoSizeIfNeeded();

			this.layoutChildren();
			
			if(this.currentBackground is IValidating)
			{
				IValidating(this.currentBackground).validate();
			}
			if(this.currentFill is IValidating)
			{
				IValidating(this.currentFill).validate();
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
		 * <p>Calls <code>saveMeasurements()</code> to set up the
		 * <code>actualWidth</code> and <code>actualHeight</code> member
		 * variables used for layout.</p>
		 *
		 * <p>Meant for internal use, and subclasses may override this function
		 * with a custom implementation.</p>
		 */
		protected function autoSizeIfNeeded():Boolean
		{
			var needsWidth:Boolean = this._explicitWidth !== this._explicitWidth; //isNaN
			var needsHeight:Boolean = this._explicitHeight !== this._explicitHeight; //isNaN
			var needsMinWidth:Boolean = this._explicitMinWidth !== this._explicitMinWidth; //isNaN
			var needsMinHeight:Boolean = this._explicitMinHeight !== this._explicitMinHeight; //isNaN
			if(!needsWidth && !needsHeight && !needsMinWidth && !needsMinHeight)
			{
				return false;
			}

			var measureBackground:IMeasureDisplayObject = this.currentBackground as IMeasureDisplayObject;
			resetFluidChildDimensionsForMeasurement(this.currentBackground,
				this._explicitWidth, this._explicitHeight,
				this._explicitMinWidth, this._explicitMinHeight,
				this._explicitMaxWidth, this._explicitMaxHeight,
				this._explicitBackgroundWidth, this._explicitBackgroundHeight,
				this._explicitBackgroundMinWidth, this._explicitBackgroundMinHeight,
				this._explicitBackgroundMaxWidth, this._explicitBackgroundMaxHeight);
			if(this.currentBackground is IValidating)
			{
				IValidating(this.currentBackground).validate();
			}
			if(this.currentFill is IValidating)
			{
				IValidating(this.currentFill).validate();
			}
			
			//minimum dimensions
			var newMinWidth:Number = this._explicitMinWidth;
			if(needsMinWidth)
			{
				if(measureBackground !== null)
				{
					newMinWidth = measureBackground.minWidth;
				}
				else if(this.currentBackground !== null)
				{
					newMinWidth = this._explicitBackgroundMinWidth;
				}
				else
				{
					newMinWidth = 0;
				}
				var fillMinWidth:Number = this._originalFillWidth;
				if(this.currentFill is IFeathersControl)
				{
					fillMinWidth = IFeathersControl(this.currentFill).minWidth;
				}
				fillMinWidth += this._paddingLeft + this._paddingRight;
				if(fillMinWidth > newMinWidth)
				{
					newMinWidth = fillMinWidth;
				}
			}
			var newMinHeight:Number = this._explicitMinHeight;
			if(needsMinHeight)
			{
				if(measureBackground !== null)
				{
					newMinHeight = measureBackground.minHeight;
				}
				else if(this.currentBackground !== null)
				{
					newMinHeight = this._explicitBackgroundMinHeight;
				}
				else
				{
					newMinHeight = 0;
				}
				var fillMinHeight:Number = this._originalFillHeight;
				if(this.currentFill is IFeathersControl)
				{
					fillMinHeight = IFeathersControl(this.currentFill).minHeight;
				}
				fillMinHeight += this._paddingTop + this._paddingBottom;
				if(fillMinHeight > newMinHeight)
				{
					newMinHeight = fillMinHeight;
				}
			}

			//current dimensions
			var newWidth:Number = this._explicitWidth;
			if(needsWidth)
			{
				if(this.currentBackground !== null)
				{
					newWidth = this.currentBackground.width;
				}
				else
				{
					newWidth = 0;
				}
				var fillWidth:Number = this._originalFillWidth + this._paddingLeft + this._paddingRight;
				if(fillWidth > newWidth)
				{
					newWidth = fillWidth;
				}
			}
			var newHeight:Number = this._explicitHeight;
			if(needsHeight)
			{
				if(this.currentBackground !== null)
				{
					newHeight = this.currentBackground.height;
				}
				else
				{
					newHeight = 0;
				}
				var fillHeight:Number = this._originalFillHeight + this._paddingTop + this._paddingBottom;
				if(fillHeight > newHeight)
				{
					newHeight = fillHeight;
				}
			}
			
			return this.saveMeasurements(newWidth, newHeight, newMinWidth, newMinHeight);
		}

		/**
		 * @private
		 */
		protected function refreshBackground():void
		{
			this.currentBackground = this._backgroundSkin;
			if(this._backgroundDisabledSkin !== null)
			{
				if(this._isEnabled)
				{
					this._backgroundDisabledSkin.visible = false;
				}
				else
				{
					this.currentBackground = this._backgroundDisabledSkin;
					if(this._backgroundSkin !== null)
					{
						this._backgroundSkin.visible = false;
					}
				}
			}
			if(this.currentBackground !== null)
			{
				this.currentBackground.visible = true;
				if(this.currentBackground is IFeathersControl)
				{
					IFeathersControl(this.currentBackground).initializeNow();
				}
				if(this.currentBackground is IMeasureDisplayObject)
				{
					var measureSkin:IMeasureDisplayObject = IMeasureDisplayObject(this.currentBackground);
					this._explicitBackgroundWidth = measureSkin.explicitWidth;
					this._explicitBackgroundHeight = measureSkin.explicitHeight;
					this._explicitBackgroundMinWidth = measureSkin.explicitMinWidth;
					this._explicitBackgroundMinHeight = measureSkin.explicitMinHeight;
					this._explicitBackgroundMaxWidth = measureSkin.explicitMaxWidth;
					this._explicitBackgroundMaxHeight = measureSkin.explicitMaxHeight;
				}
				else
				{
					this._explicitBackgroundWidth = this.currentBackground.width;
					this._explicitBackgroundHeight = this.currentBackground.height;
					this._explicitBackgroundMinWidth = this._explicitBackgroundWidth;
					this._explicitBackgroundMinHeight = this._explicitBackgroundHeight;
					this._explicitBackgroundMaxWidth = this._explicitBackgroundWidth;
					this._explicitBackgroundMaxHeight = this._explicitBackgroundHeight;
				}
			}
		}

		/**
		 * @private
		 */
		protected function refreshFill():void
		{
			this.currentFill = this._fillSkin;
			if(this._fillDisabledSkin)
			{
				if(this._isEnabled)
				{
					this._fillDisabledSkin.visible = false;
				}
				else
				{
					this.currentFill = this._fillDisabledSkin;
					if(this._backgroundSkin)
					{
						this._fillSkin.visible = false;
					}
				}
			}
			if(this.currentFill)
			{
				if(this.currentFill is IValidating)
				{
					IValidating(this.currentFill).validate();
				}
				if(this._originalFillWidth !== this._originalFillWidth) //isNaN
				{
					this._originalFillWidth = this.currentFill.width;
				}
				if(this._originalFillHeight !== this._originalFillHeight) //isNaN
				{
					this._originalFillHeight = this.currentFill.height;
				}
				this.currentFill.visible = true;
			}
		}

		/**
		 * @private
		 */
		protected function layoutChildren():void
		{
			if(this.currentBackground)
			{
				this.currentBackground.width = this.actualWidth;
				this.currentBackground.height = this.actualHeight;
			}

			if(this._minimum === this._maximum)
			{
				var percentage:Number = 1;
			}
			else
			{
				percentage = (this._value - this._minimum) / (this._maximum - this._minimum);
				if(percentage < 0)
				{
					percentage = 0;
				}
				else if(percentage > 1)
				{
					percentage = 1;
				}
			}
			if(this._direction === Direction.VERTICAL)
			{
				this.currentFill.width = this.actualWidth - this._paddingLeft - this._paddingRight;
				this.currentFill.height = Math.round(this._originalFillHeight + percentage * (this.actualHeight - this._paddingTop - this._paddingBottom - this._originalFillHeight));
				this.currentFill.x = this._paddingLeft;
				this.currentFill.y = this.actualHeight - this._paddingBottom - this.currentFill.height;
			}
			else //horizontal
			{
				this.currentFill.width = Math.round(this._originalFillWidth + percentage * (this.actualWidth - this._paddingLeft - this._paddingRight - this._originalFillWidth));
				this.currentFill.height = this.actualHeight - this._paddingTop - this._paddingBottom;
				this.currentFill.x = this._paddingLeft;
				this.currentFill.y = this._paddingTop;
			}
		}
	}
}