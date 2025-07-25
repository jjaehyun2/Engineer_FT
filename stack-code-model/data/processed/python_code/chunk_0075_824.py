package net.psykosoft.psykopaint2.core.views.components.slider
{

	import com.greensock.TweenLite;
	import com.greensock.easing.Strong;
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Sprite;
	import flash.display.Stage;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.geom.Matrix;
	
	import net.psykosoft.psykopaint2.base.ui.components.NavigationButton;
	import net.psykosoft.psykopaint2.core.managers.gestures.GestureManager;
	import net.psykosoft.psykopaint2.core.views.components.previews.AbstractPreview;
	import net.psykosoft.psykopaint2.core.views.components.previews.PreviewIconFactory;
	

	public class SliderButton extends Sprite
	{
		// Declared in Flash.
		public var button:NavigationButton;
		//public var leftEar:Sprite;
		//public var rightEar:Sprite;
		public var previewHolder:Sprite;
		private var sliderbar:SliderButtonEarSlide;
		public var sliderframe:Sprite;

		//private var _rightEarOpenX:Number;
		//private var _leftEarOpenX:Number;
		private var _previewHolderOpenY:Number;
		
		private var _labelText:String;
		private var _defaultLabelText:String;
		private var _previewID:String;
		private var _value:Number;
		private var _sliding:Boolean;
		private var _stage:Stage;
		//private var _earContainer:Sprite;
		private var _ratio:Number;
		private var _minValue:Number = 0;
		private var _maxValue:Number = 1;
		private var _valueRange:Number = 1;
		private var _labelMode:int = 1;
		private var _digits:int = 0;
		private var _earContainerX:Number = 0;
		private var _mouseDownX:Number;
		private var _changeEvt:Event;
		private var _earContainerXOnMouseDown:Number = 0;
		
		private var _minSet:Boolean;
		private var _maxSet:Boolean;
		private var _delayedUpdate:Boolean;
		
		
		private var _valueHasChanged:Boolean;
		private var _hidePreviewAfterOpening:Boolean;
		private var _previewIcon:AbstractPreview;
		
		private var state:int;
		
		private const EAR_MOTION_RANGE:Number = 70;
		private const EAR_ANIMATION_TIME:Number = 0.2;
		private const PREVIEW_ANIMATION_TIME:Number = 0.2;
		private const PREVIEW_ICON_OFFSET_X:Number = 64;
		private const PREVIEW_ICON_OFFSET_Y:Number = 64;
		
		public static var LABEL_VALUE:int = 0;
		public static var LABEL_PERCENT:int = 1;
		public static var LABEL_DEGREES:int = 2;
		
		private static var STATE_CLOSED:int = 0;
		private static var STATE_OPENING:int = 1;
		private static var STATE_CLOSING:int = 2;
		private static var STATE_OPEN:int = 3;
		private static var STATE_SLIDING:int = 4;

		public function SliderButton() {
			super();
			setup();
			addEventListener( Event.ADDED_TO_STAGE, onAddedToStage );
		}

		public function dispose():void {

			stopSliding();
			killEarTweens();
			killPreviewTweens();
			//_earContainer.removeEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
			sliderbar.removeEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
			
			button.removeEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
			button.dispose();
			removeEventListener( Event.ENTER_FRAME, onEnterFrame );
			if( _stage ) {
				_stage.removeEventListener( MouseEvent.MOUSE_UP, onStageMouseUp );
				_stage.removeEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
				_stage = null;
			}
			_minSet = _maxSet = false;
			
		}

		// ----------------------------
		// Construction/destruction.
		// ----------------------------

		private function setup():void {

			_minSet = _maxSet = false;
			_value = _ratio = 0;

			_changeEvt = new Event( Event.CHANGE );

			/*
			_leftEarOpenX = leftEar.x;
			_rightEarOpenX = rightEar.x;

			leftEar.x = 0;
			rightEar.x = 0;
			*/
			
			
			_previewHolderOpenY = previewHolder.y;

			/*
			_earContainer = new Sprite();
			_earContainer.visible = false;
			_earContainer.addChild( rightEar );
			_earContainer.addChild( leftEar );
			addChildAt( _earContainer, 0 );
		*/
			
		
			sliderbar = new SliderButtonEarSlide();
			//sliderbar.graphics.beginBitmapFill( new SliderButtonSlide() as BitmapData, new Matrix(0.5,0,0,0.5,-160),false,true );
			//sliderbar.graphics.drawRect(-160,0,321,115);
			//sliderbar.graphics.endFill();
			
			//sliderbar.scale9Grid = new Rectangle(50, 10,321 -100, 115 -20);
			sliderbar.displayWidth = 160;
			sliderbar.x = 0;
			sliderbar.y = -115 * 0.5;
			addChildAt( sliderbar,0 );
			
			button.labelText = "";
			button.addChildAt(sliderframe,1);
			
			
			
			_valueHasChanged = false;
			
			
			
		}

		private function postSetupAfterStageIsAvailable():void {
			_stage = stage;
			button.addEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
			//_earContainer.addEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
			sliderbar.addEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
			
			state = STATE_CLOSED;
			
		}

		// -----------------------
		// Label.
		// -----------------------

		public function updateLabelFromValue():void {
			switch( _labelMode ) {
				case LABEL_VALUE:
					button.labelText = formatLabel( value);
					break;
				case LABEL_PERCENT:
					button.labelText = formatLabel(  _ratio * 100, "%" );
					break;
				case LABEL_DEGREES:
					button.labelText = formatLabel(  value, "°" );
					break;
			}
		}

		private function formatLabel( value:Number, suffix:String = "" ):String {
			return String( int( value * Math.pow( 10, _digits ) + 0.5 ) / Math.pow( 10, _digits ) ) + suffix;
		}

		// -----------------------
		// Enterframe.
		// -----------------------

		private function startSliding():void {
			if( _sliding ) return;
			if( !hasEventListener( Event.ENTER_FRAME ) ) {
				
				addEventListener( Event.ENTER_FRAME, onEnterFrame );
			}
			//updateLabelFromValue();
			_sliding = true;
			_valueHasChanged = false;
		}

		private function stopSliding():void {
			if( !_sliding ) return;
			if( hasEventListener( Event.ENTER_FRAME ) ) {
				removeEventListener( Event.ENTER_FRAME, onEnterFrame );
			}
			
			_sliding = false;
		}

		private function update():void {
			//if( !_sliding ) return;
			updateEarsFromMouse();
			updateRatioFromEars();
			updateValueFromRatio();
			//updateLabelFromValue();
			updatePreviewIconFromRatio();
			dispatchEvent( _changeEvt );
		}

		// -----------------------
		// Conversions.
		// -----------------------

		private function updateEarsFromMouse():void {
			var dx:Number = mouseX - _mouseDownX;
			_valueHasChanged ||= (dx != 0);
			_earContainerX = _earContainerXOnMouseDown + dx;
			if( _earContainerX < -EAR_MOTION_RANGE ) _earContainerX = -EAR_MOTION_RANGE;
			if( _earContainerX >  EAR_MOTION_RANGE ) _earContainerX =  EAR_MOTION_RANGE;
			//_earContainer.x = _earContainerX;
			sliderbar.x = _earContainerX;
			
		}

		private function updateRatioFromEars():void {
			_ratio = 0.5 * ( _earContainerX / EAR_MOTION_RANGE ) + 0.5;
			if ( _ratio < 0 || _ratio > 1 )
			{
				throw("ButtSlider ratio is wrong",_ratio);
			}
		}

		private function updateRatioFromValue():void {
			if (_minSet && _maxSet ) _ratio = ( _value - _minValue ) / _valueRange;
			if ( _ratio < 0 || _ratio > 1 )
			{
				throw("ButtSlider ratio is wrong",_ratio);
			}
		}

		private function updateValueFromRatio():void {
			if (_minSet && _maxSet ) _value = _ratio * _valueRange + _minValue;
		}

		private function updateEarsFromRatio():void {
			//_earContainer.x = _earContainerX = EAR_MOTION_RANGE * ( 2 * _ratio - 1 );
			 _earContainerX = EAR_MOTION_RANGE * ( 2 * _ratio - 1 );
			 if ( state == STATE_CLOSED )  sliderbar.x = 0;
			 if ( state == STATE_OPEN )  sliderbar.x = _earContainerX;
			
		}
		
		private function updatePreviewIconFromRatio():void {
			if ( _previewIcon ) _previewIcon.ratio = _ratio;
		}

		// -----------------------
		// Tweens.
		// -----------------------

		private function showEars():void {
			state = STATE_OPENING;
			killEarTweens();
			//_earContainer.visible = true;
			//TweenLite.to( leftEar, EAR_ANIMATION_TIME, { x: _leftEarOpenX, ease: Strong.easeOut, onComplete: onEarsShowComplete  } );
			//TweenLite.to( rightEar, EAR_ANIMATION_TIME, { x: _rightEarOpenX, ease: Strong.easeOut } );
			//TweenLite.to( _earContainer, EAR_ANIMATION_TIME, { x: _earContainerX, ease: Strong.easeOut } );
			TweenLite.to( sliderbar, EAR_ANIMATION_TIME, { x: _earContainerX, displayWidth:321,ease: Strong.easeOut, onComplete: onEarsShowComplete  } );
			
			button.removeEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
			//_earContainer.removeEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
			sliderbar.removeEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
			_stage.addEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
			
		}

		private function hideEars():void {
			state = STATE_CLOSING;
			killEarTweens();
			//TweenLite.to( leftEar, EAR_ANIMATION_TIME, { x: 0, ease: Strong.easeIn, onComplete: onEarsHideComplete } );
			//TweenLite.to( rightEar, EAR_ANIMATION_TIME, { x: 0, ease: Strong.easeIn } );
			//TweenLite.to( _earContainer, EAR_ANIMATION_TIME, { x: 0, ease: Strong.easeIn } );
			TweenLite.to( sliderbar, EAR_ANIMATION_TIME, { x: 0, displayWidth:160, ease: Strong.easeIn, onComplete: onEarsHideComplete } );
			
			button.addEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
			//_earContainer.addEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
			sliderbar.addEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
			
			_stage.removeEventListener( MouseEvent.MOUSE_DOWN, onBtnMouseDown );
		}
		
		private function onEarsHideComplete():void {
			//_earContainer.visible = false;
			state = STATE_CLOSED;
			button.labelText = _defaultLabelText;
			
		}
		
		private function onEarsShowComplete():void {
			//showPreviewHolder();
			state = STATE_OPEN;
			
			
		}
		
		private function killEarTweens():void {
			//TweenLite.killTweensOf( leftEar );
			//TweenLite.killTweensOf( rightEar );
			//TweenLite.killTweensOf( _earContainer );
			TweenLite.killTweensOf( sliderbar );
		}
		
		private function showPreviewHolder():void {
			killPreviewTweens();
			_hidePreviewAfterOpening = false;
			button.showIcon( false );
			previewHolder.visible = true;
			TweenLite.to( previewHolder, PREVIEW_ANIMATION_TIME, { y: _previewHolderOpenY - 120, ease: Strong.easeOut, onComplete: onPreviewShowComplete } );
			_previewIcon.x = PREVIEW_ICON_OFFSET_X;
			_previewIcon.y = PREVIEW_ICON_OFFSET_Y;
			previewHolder.addChild(_previewIcon);
			
			
		}
		
		private function onPreviewShowComplete():void {
			if ( _hidePreviewAfterOpening ) {
				stopSliding();
				hidePreviewHolder();
			}
		}
		
		private function hidePreviewHolder():void {
			killPreviewTweens();
			TweenLite.to( previewHolder, PREVIEW_ANIMATION_TIME, { y: _previewHolderOpenY, ease: Strong.easeIn, onComplete: onPreviewHideComplete } );
		}

		private function onPreviewHideComplete():void {
			_previewIcon.x = 0;
			_previewIcon.y = 0;
			
			button.addChildAt(_previewIcon,1);
			
			previewHolder.visible = false;
			button.showIcon( true );
			hideEars();
		}
		
		private function killPreviewTweens():void {
			TweenLite.killTweensOf( previewHolder );
		}
		
		private function updateFromValue():void
		{
			if ( _minSet &&  value < _minValue ) value = minValue;
			if ( _maxSet && value > _maxValue ) value = maxValue;
			
			updateRatioFromValue();
			updateEarsFromRatio();
			updatePreviewIconFromRatio();
			dispatchEvent( _changeEvt );
		}

		// ---------------------------------------------------------------------
		// Interface.
		// ---------------------------------------------------------------------

		public function get selected():Boolean {
			return button.selected;
		}

		public function set selected( value:Boolean ):void {
			button.selected = value;
		}

		public function get selectable():Boolean {
			return button.selectable;
		}

		public function set selectable( value:Boolean ):void {
			button.selectable = value;
		}

		public function get iconBitmap():Bitmap {
			return button.iconBitmap;
		}

		public function set iconBitmap( value:Bitmap ):void {
			button.iconBitmap = value;
		}

		public function get iconType():String {
			return button.iconType;
		}

		public function set iconType( value:String ):void {
			button.iconType = value;
		}
		
		
		public function get previewID():String {
			return _previewID;
		}
		
		public function set previewID( value:String ):void {
			_previewID = value;
			
			if ( _previewIcon != null && _previewIcon.parent != null)
			{
				_previewIcon.parent.removeChild(_previewIcon);
				_previewIcon = null;
			}
			_previewIcon = PreviewIconFactory.getPreviewIcon(previewID);
			_previewIcon.mouseEnabled = _previewIcon.mouseChildren = false;
			_previewIcon.x = 0;
			_previewIcon.y = 0;
			_previewIcon.scaleX = _previewIcon.scaleY = 0.5;
			_previewIcon.ratio = _ratio;
			button.addChildAt(_previewIcon,1);
			
		}

		public function get id():String {
			return button.id;
		}

		public function set id( value:String ):void {
			button.id = value;
		}

		public function get labelMode():int {
			return _labelMode;
		}

		public function set labelMode( value:int ):void {
			_labelMode = value;
		}

		public function set minValue( minValue:Number ):void {
			_minValue = minValue;
			value
			_minSet = true;
			if ( _minSet && _maxSet )
			{
				_valueRange = _maxValue - _minValue;
				if ( _delayedUpdate )
				{
					_delayedUpdate = false;
					updateFromValue();
				} else {
					updateRatioFromValue();
				}
			} else {
				_delayedUpdate = true;
			}
		}

		public function set maxValue( maxValue:Number ):void {
			_maxValue = maxValue;
			_maxSet = true;
			if ( _minSet && _maxSet )
			{
				_valueRange = _maxValue - _minValue;
				if ( _delayedUpdate )
				{
					_delayedUpdate = false;
					updateFromValue();
				} else {
					updateRatioFromValue();
				}
			} else {
				_delayedUpdate = true;
			}
		}

		public function get labelText():String {
			return _labelText;
		}

		public function set labelText( value:String ):void {
			_labelText = value;
			button.labelText = value;
		}
		
		public function get defaultLabelText():String {
			return _defaultLabelText;
		}
		
		public function set defaultLabelText( value:String ):void {
			_defaultLabelText = value;
		}

		public function set value( value:Number ):void {
			_value = value;
			if ( _minSet && _maxSet )
			{
				updateFromValue();
			} else {
				_delayedUpdate = true;
			}
		}

		public function get value():Number {
			return _value;
		}

		public function get digits():int {
			return _digits;
		}

		public function set digits( value:int ):void {
			_digits = value;
		}

		// ---------------------------------------------------------------------
		// Event listeners.
		// ---------------------------------------------------------------------

		private function onEnterFrame( event:Event ):void {
			update();
		}

		private function onAddedToStage( event:Event ):void {
			removeEventListener( Event.ADDED_TO_STAGE, onAddedToStage );
			
			postSetupAfterStageIsAvailable();
		}

		private function onBtnMouseDown( event:MouseEvent ):void {
			
			GestureManager.gesturesEnabled = false;
			
			_mouseDownX = mouseX;
			_earContainerXOnMouseDown = _earContainerX;
			_stage.addEventListener( MouseEvent.MOUSE_UP, onStageMouseUp );
			switch ( state )
			{
				case STATE_CLOSED:
					showEars();
					showPreviewHolder();
					startSliding();
					
				break;
				case STATE_OPEN:
					//var isOnSlider:Boolean = _earContainer.hitTestPoint(stage.mouseX, stage.mouseY,true);
					var isOnSlider:Boolean = sliderbar.hitTestPoint(_stage.mouseX, _stage.mouseY,true);
					if ( isOnSlider ) startSliding();
					else {
						hidePreviewHolder();
					}
				break;
			}
			
		}

		private function onStageMouseUp( event:MouseEvent ):void {
			
			GestureManager.gesturesEnabled = true;
			
			_stage.removeEventListener( MouseEvent.MOUSE_UP, onStageMouseUp );
			if ( state != STATE_OPENING )
			{
				stopSliding();
				hidePreviewHolder();
			} else {
				_hidePreviewAfterOpening = true;
			}
			/*
			switch ( state )
			{
				
				case STATE_OPEN:
					stopSliding();
					if ( !_valueHasChanged && sliderbar.hitTestPoint(_stage.mouseX, _stage.mouseY,true))
					{
						if ( Math.abs(sliderbar.mouseX) > 25 )
						{
							if ( sliderbar.mouseX < 0 )
							{
								_ratio -= 0.02;
								if ( _ratio < 0 ) _ratio = 0;
							} else {
								_ratio += 0.02;
								if ( _ratio > 1 ) _ratio = 1;
							}
							updateValueFromRatio();
							updateEarsFromRatio();
						}
					}
					break;
				
				case STATE_OPENING:
					
					stopSliding();
					break;
				
			}
			*/
		}
	}
}