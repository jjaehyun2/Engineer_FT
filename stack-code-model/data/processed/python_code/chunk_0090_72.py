package feathers.examples.trainTimes.controls
{
	import feathers.controls.Button;
	import feathers.controls.ImageLoader;
	import feathers.controls.Label;
	import feathers.controls.LayoutGroup;
	import feathers.controls.List;
	import feathers.controls.renderers.IListItemRenderer;
	import feathers.core.FeathersControl;
	import feathers.examples.trainTimes.model.StationData;
	import feathers.skins.IStyleProvider;

	import flash.geom.Point;

	import starling.animation.Transitions;
	import starling.animation.Tween;
	import starling.core.Starling;
	import starling.display.Quad;
	import starling.events.Event;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	import starling.textures.Texture;

	public class StationListItemRenderer extends FeathersControl implements IListItemRenderer
	{
		public static const CHILD_STYLE_NAME_STATION_LIST_NAME_LABEL:String = "stationListNameLabel";
		public static const CHILD_STYLE_NAME_STATION_LIST_DETAILS_LABEL:String = "stationListDetailsLabel";
		public static const CHILD_STYLE_NAME_STATION_LIST_ACTION_CONTAINER:String = "stationListActionContainer";
		public static const CHILD_STYLE_NAME_STATION_LIST_CONFIRM_BUTTON:String = "stationListConfirmButton";
		public static const CHILD_STYLE_NAME_STATION_LIST_CANCEL_BUTTON:String = "stationListCancelButton";

		private static const HELPER_POINT:Point = new Point();
		private static const HELPER_TOUCHES_VECTOR:Vector.<Touch> = new <Touch>[];

		private static const DEPART_FROM_TEXT:String = "DEPART FROM";
		private static const DEPARTING_FROM_TEXT:String = "DEPARTING FROM";
		private static const TRAVEL_TO_TEXT:String = "TRAVEL TO";
		private static const QUESTION_MARK:String = "?";

		public static var globalStyleProvider:IStyleProvider;

		protected static function defaultLoaderFactory():ImageLoader
		{
			return new ImageLoader();
		}

		public function StationListItemRenderer()
		{
			this.addEventListener(TouchEvent.TOUCH, touchHandler);
		}

		override protected function get defaultStyleProvider():IStyleProvider
		{
			return StationListItemRenderer.globalStyleProvider;
		}

		protected var background:Quad;
		protected var actionContainer:LayoutGroup;
		protected var confirmButton:Button;
		protected var cancelButton:Button;
		protected var nameLabel:Label;
		protected var detailsLabel:Label;
		protected var icon:ImageLoader;

		protected var _touchPointID:int = -1;

		protected var _data:StationData;

		public function get data():Object
		{
			return this._data;
		}

		public function set data(value:Object):void
		{
			if(this._data == value)
			{
				return;
			}
			this._data = StationData(value);
			this.isSelectionWaitingToBeAnimated = false;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		protected var _index:int = -1;

		public function get index():int
		{
			return this._index;
		}

		public function set index(value:int):void
		{
			this._index = value;
		}

		/**
		 * @private
		 */
		private var _factoryID:String;

		/**
		 * @inheritDoc
		 */
		public function get factoryID():String
		{
			return this._factoryID;
		}

		/**
		 * @private
		 */
		public function set factoryID(value:String):void
		{
			this._factoryID = value;
		}

		protected var _isInDestinationPhase:Boolean = false;

		public function get isInDestinationPhase():Boolean
		{
			return this._isInDestinationPhase;
		}

		public function set isInDestinationPhase(value:Boolean):void
		{
			if(this._isInDestinationPhase == value)
			{
				return;
			}
			this._isInDestinationPhase = value;
			this.invalidate(INVALIDATION_FLAG_SELECTED);
		}

		protected var _owner:List;

		public function get owner():List
		{
			return this._owner;
		}

		public function set owner(value:List):void
		{
			if(this._owner == value)
			{
				return;
			}
			if(this._owner)
			{
				this._owner.removeEventListener(Event.SCROLL, owner_scrollHandler);
			}
			this._owner = value;
			if(this._owner)
			{
				this._owner.addEventListener(Event.SCROLL, owner_scrollHandler);
			}
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		protected var isSelectionWaitingToBeAnimated:Boolean = false;

		protected var _isSelected:Boolean = false;

		public function get isSelected():Boolean
		{
			return this._isSelected;
		}

		public function set isSelected(value:Boolean):void
		{
			if(this._isSelected == value)
			{
				return;
			}
			this._isSelected = value;
			if(this.selectionTween)
			{
				Starling.juggler.remove(this.selectionTween);
				this.selectionTween = null;
			}
			this.isSelectionWaitingToBeAnimated = !this.isInvalid(INVALIDATION_FLAG_DATA) && !this._data.isDepartingFromHere;
			this.invalidate(INVALIDATION_FLAG_SELECTED);
			this.dispatchEventWith(Event.CHANGE);
		}

		protected var _normalIconTexture:Texture;

		public function get normalIconTexture():Texture
		{
			return this._normalIconTexture;
		}

		public function set normalIconTexture(value:Texture):void
		{
			if(this._normalIconTexture == value)
			{
				return;
			}
			this._normalIconTexture = value;
			this.invalidate(INVALIDATION_FLAG_SKIN);
		}

		protected var _selectedIconTexture:Texture;

		public function get selectedIconTexture():Texture
		{
			return this._selectedIconTexture;
		}

		public function set selectedIconTexture(value:Texture):void
		{
			if(this._selectedIconTexture == value)
			{
				return;
			}
			this._selectedIconTexture = value;
			this.invalidate(INVALIDATION_FLAG_SKIN);
		}

		protected var _iconLoaderFactory:Function = defaultLoaderFactory;

		public function get iconLoaderFactory():Function
		{
			return this._iconLoaderFactory;
		}

		public function set iconLoaderFactory(value:Function):void
		{
			if(this._iconLoaderFactory == value)
			{
				return;
			}
			this._iconLoaderFactory = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		protected var _paddingTop:Number = 0;

		public function get paddingTop():Number
		{
			return this._paddingTop;
		}

		public function set paddingTop(value:Number):void
		{
			if(this._paddingTop == value)
			{
				return;
			}
			this._paddingTop = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		protected var _paddingRight:Number = 0;

		public function get paddingRight():Number
		{
			return this._paddingRight;
		}

		public function set paddingRight(value:Number):void
		{
			if(this._paddingRight == value)
			{
				return;
			}
			this._paddingRight = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		protected var _paddingBottom:Number = 0;

		public function get paddingBottom():Number
		{
			return this._paddingBottom;
		}

		public function set paddingBottom(value:Number):void
		{
			if(this._paddingBottom == value)
			{
				return;
			}
			this._paddingBottom = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		protected var _paddingLeft:Number = 0;

		public function get paddingLeft():Number
		{
			return this._paddingLeft;
		}

		public function set paddingLeft(value:Number):void
		{
			if(this._paddingLeft == value)
			{
				return;
			}
			this._paddingLeft = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		protected var _gap:Number = 0;

		public function get gap():Number
		{
			return this._gap;
		}

		public function set gap(value:Number):void
		{
			if(this._gap == value)
			{
				return;
			}
			this._gap = value;
			this.invalidate(INVALIDATION_FLAG_STYLES);
		}

		public var confirmCallback:Function;

		protected var selectionTween:Tween;

		override protected function initialize():void
		{
			this.background = new Quad(10, 10, 0x3b2a41);
			this.background.alpha = 0;
			this.addChild(this.background);

			this.detailsLabel = new Label();
			this.detailsLabel.styleNameList.add(CHILD_STYLE_NAME_STATION_LIST_DETAILS_LABEL);
			this.addChild(this.detailsLabel);

			this.nameLabel = new Label();
			this.nameLabel.styleNameList.add(CHILD_STYLE_NAME_STATION_LIST_NAME_LABEL);
			this.addChild(this.nameLabel);

			this.actionContainer = new LayoutGroup();
			this.actionContainer.styleNameList.add(CHILD_STYLE_NAME_STATION_LIST_ACTION_CONTAINER);
			this.actionContainer.visible = false;
			this.addChild(this.actionContainer);

			this.confirmButton = new Button();
			this.confirmButton.styleNameList.add(CHILD_STYLE_NAME_STATION_LIST_CONFIRM_BUTTON);
			this.confirmButton.addEventListener(Event.TRIGGERED, confirmButton_triggeredHandler);
			this.actionContainer.addChild(this.confirmButton);

			this.cancelButton = new Button();
			this.cancelButton.styleNameList.add(CHILD_STYLE_NAME_STATION_LIST_CANCEL_BUTTON);
			this.cancelButton.addEventListener(Event.TRIGGERED, cancelButton_triggeredHandler);
			this.actionContainer.addChild(this.cancelButton);
		}

		override protected function draw():void
		{
			var dataInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_DATA);
			var selectionInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_SELECTED);
			var stylesInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_STYLES);
			var sizeInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_SIZE);

			if(stylesInvalid)
			{
				this.refreshIcon();
			}

			if(dataInvalid || selectionInvalid || stylesInvalid)
			{
				this.commitData();
			}

			sizeInvalid = this.autoSizeIfNeeded() || sizeInvalid;
			this.layout();
		}

		protected function autoSizeIfNeeded():Boolean
		{
			var needsWidth:Boolean = isNaN(this._explicitWidth);
			var needsHeight:Boolean = isNaN(this._explicitHeight);
			var needsMinWidth:Boolean = isNaN(this._explicitMinWidth);
			var needsMinHeight:Boolean = isNaN(this._explicitMinHeight);
			if(!needsWidth && !needsHeight && !needsMinWidth && !needsMinHeight)
			{
				return false;
			}
			this.icon.validate();
			var newWidth:Number = this._explicitWidth;
			if(needsWidth)
			{
				newWidth = this.icon.width;
				newWidth += this._paddingLeft + this._paddingRight;
			}
			var newHeight:Number = this._explicitHeight;
			if(needsHeight)
			{
				newHeight = this.icon.height;
			}
			var newMinWidth:Number = this._explicitMinWidth;
			if(needsMinWidth)
			{
				newMinWidth = this.icon.width;
				newMinWidth += this._paddingLeft + this._paddingRight;
			}
			var newMinHeight:Number = this._explicitMinHeight;
			if(needsMinHeight)
			{
				newMinHeight = this.icon.height;
			}
			return this.saveMeasurements(newWidth, newHeight, newMinWidth, newMinHeight);
		}

		protected function refreshIcon():void
		{
			if(this.icon)
			{
				this.icon.removeFromParent(true);
			}

			this.icon = ImageLoader(this._iconLoaderFactory());
			this.addChild(this.icon);
		}

		protected function commitData():void
		{
			if(this._owner && this._data)
			{
				var nameLabelText:String = this._data.name;
				if(this._isSelected)
				{
					nameLabelText += QUESTION_MARK;
				}
				this.nameLabel.text = nameLabelText;

				var displayAsSelected:Boolean = this._isSelected || this._data.isDepartingFromHere;
				this.icon.source = displayAsSelected ? this._selectedIconTexture : this._normalIconTexture;

				if(this._data.isDepartingFromHere)
				{
					this.detailsLabel.text = DEPARTING_FROM_TEXT;
				}
				else if(this._isInDestinationPhase)
				{
					this.detailsLabel.text = TRAVEL_TO_TEXT;
				}
				else
				{
					this.detailsLabel.text = DEPART_FROM_TEXT;
				}

				if(!this.isSelectionWaitingToBeAnimated)
				{
					this.background.alpha = displayAsSelected ? 1 : 0;
				}
				if(!this.isSelectionWaitingToBeAnimated || displayAsSelected)
				{
					this.detailsLabel.visible = displayAsSelected;
				}
				//the action container will disappear after the departure
				//station has been selected, so it has different rules
				if(!this._data.isDepartingFromHere && (!this.isSelectionWaitingToBeAnimated || this._isSelected))
				{
					this.actionContainer.visible = this._isSelected;
					this.actionContainer.alpha = this._isSelected ? 1 : 0;
				}
			}
			else
			{
				this.nameLabel.text = null;
				this.detailsLabel.text = null;
				this.actionContainer.visible = false;
				this.background.alpha = 0;
				this.icon.source = null;
			}
		}

		protected function layout():void
		{
			this.background.width = this.actualWidth;
			this.background.height = this.actualHeight;

			this.icon.validate();
			this.icon.x = this._paddingLeft;
			var leftMarginWidth:Number = this._paddingLeft + this.icon.width + this._gap;
			var availableLabelWidth:Number = this.actualWidth - this._paddingRight - leftMarginWidth;
			var availableLabelHeight:Number = this.actualHeight - this._paddingTop - this._paddingBottom;

			this.actionContainer.width = availableLabelWidth;

			this.nameLabel.validate();
			this.detailsLabel.validate();
			this.actionContainer.validate();

			var displayAsSelected:Boolean = this._isSelected || (this._data && this._data.isDepartingFromHere);
			if((displayAsSelected && this.isSelectionWaitingToBeAnimated) ||
				(!displayAsSelected && !this.isSelectionWaitingToBeAnimated))
			{
				this.actionContainer.x = this.actualWidth;
				this.detailsLabel.alpha = 0;
				this.nameLabel.x = leftMarginWidth;
			}
			else
			{
				this.actionContainer.x = this.actualWidth - this.actionContainer.width;
				this.detailsLabel.alpha = 1;
				this.nameLabel.x = leftMarginWidth + (availableLabelWidth - this.nameLabel.width) / 2;
			}
			if(this.isSelectionWaitingToBeAnimated)
			{
				this.isSelectionWaitingToBeAnimated = false;
				this.selectionTween = new Tween(this.nameLabel, 0.35, Transitions.EASE_OUT);
				if(displayAsSelected)
				{
					this.selectionTween.animate("x", leftMarginWidth + (availableLabelWidth - this.nameLabel.width) / 2);
					this.selectionTween.onComplete = selectionTween_onSelectComplete;
				}
				else
				{
					this.selectionTween.animate("x", leftMarginWidth);
					this.selectionTween.onComplete = selectionTween_onDeselectComplete;
				}
				this.selectionTween.onUpdate = selectionTween_onUpdate;
				Starling.juggler.add(this.selectionTween);
			}
			else if(this._data && this._data.isDepartingFromHere && this.actionContainer.visible)
			{
				this.selectionTween = new Tween(this.actionContainer, 0.35, Transitions.EASE_OUT);
				this.selectionTween.fadeTo(0);
				this.selectionTween.onComplete = selectionTween_onConfirmComplete;
				Starling.juggler.add(this.selectionTween);
			}

			this.nameLabel.y = (availableLabelHeight - this.nameLabel.height) / 2;
			this.detailsLabel.x = leftMarginWidth + (availableLabelWidth - this.detailsLabel.width) / 2;
			this.detailsLabel.y = this.nameLabel.y - this.detailsLabel.height + this.detailsLabel.height - this.detailsLabel.baseline;
			this.actionContainer.y = this.actualHeight - this.actionContainer.height;
		}

		protected function selectionTween_onUpdate():void
		{
			var ratio:Number = this.selectionTween.transitionFunc(this.selectionTween.currentTime / this.selectionTween.totalTime);
			if(!this._isSelected)
			{
				ratio = 1 - ratio;
			}
			this.detailsLabel.alpha = this.background.alpha = ratio;
			this.actionContainer.x = this.actualWidth - this.actionContainer.width * ratio;
		}

		protected function selectionTween_onSelectComplete():void
		{
			this.selectionTween = null;
		}

		protected function selectionTween_onDeselectComplete():void
		{
			this.detailsLabel.visible = false;
			this.actionContainer.visible = false;
			this.selectionTween = null;
		}

		protected function selectionTween_onConfirmComplete():void
		{
			this.actionContainer.visible = false;
			this.selectionTween = null;
		}

		protected function touchHandler(event:TouchEvent):void
		{
			if(!this._isEnabled)
			{
				return;
			}

			var touches:Vector.<Touch> = event.getTouches(this, null, HELPER_TOUCHES_VECTOR);
			if(touches.length == 0)
			{
				//end of hover
				return;
			}
			if(this._touchPointID >= 0)
			{
				var touch:Touch;
				for each(var currentTouch:Touch in touches)
				{
					if(currentTouch.id == this._touchPointID)
					{
						touch = currentTouch;
						break;
					}
				}

				if(!touch)
				{
					//end of hover
					HELPER_TOUCHES_VECTOR.length = 0;
					return;
				}

				if(touch.phase == TouchPhase.ENDED)
				{
					this._touchPointID = -1;
					touch.getLocation(this, HELPER_POINT);
					var isInBounds:Boolean = this.hitTest(HELPER_POINT) !== null;
					if(isInBounds)
					{
						if(!this._isSelected && !this._data.isDepartingFromHere)
						{
							this.isSelected = true;
						}
					}
				}
			}
			else //if we get here, we don't have a saved touch ID yet
			{
				for each(touch in touches)
				{
					if(touch.phase == TouchPhase.BEGAN)
					{
						this._touchPointID = touch.id;
						break;
					}
				}
			}
			HELPER_TOUCHES_VECTOR.length = 0;
		}

		protected function owner_scrollHandler(event:Event):void
		{
			this._touchPointID = -1;
		}

		protected function confirmButton_triggeredHandler(event:Event):void
		{
			if(this.confirmCallback == null)
			{
				return;
			}
			this.confirmCallback();
		}

		protected function cancelButton_triggeredHandler(event:Event):void
		{
			this._owner.selectedIndex = -1;
		}
	}
}