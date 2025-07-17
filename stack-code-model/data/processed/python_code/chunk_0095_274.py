package com.lowoui_as.core
{
	import com.greensock.TweenLite;
	import com.greensock.easing.*;
	import com.lowoui_as.events.MovieEvent;
	import com.lowoui_as.utils.Filters;
	import com.lowoui_as.utils.FrameByLable;
	import flash.display.MovieClip;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.geom.Rectangle;

	[Event(name = "movieIn", type = "com.lowoui_as.events.MovieEvent")]
	[Event(name = "movieOut", type = "com.lowoui_as.events.MovieEvent")]

	/**
	* GFx 3Di Transform Supported
	*/
	public class UIMovie extends MovieClip
	{
		protected var thisWidth       : Number;
		protected var thisHeight      : Number;
		protected var stageWidth      : Number;
		protected var stageHeight     : Number;

		//permitted operation:
		protected var beScale         : Boolean;
		protected var beDrag          : Boolean;
		protected var be3DTransform   : Boolean;
		protected var beBlurFilter    : Boolean;
		protected var beMovieView     : Boolean;
        protected var initialized     : Boolean;
		protected var isFirstInit     : Boolean;
		public    var isActiveState      : Boolean;
		protected var stagePressed    : Boolean;

		private var blurValue         : Number;
        private var posInfo           : Object;

		//3DTransform
		private var panel:Object;
		private var zScale:Number;
		private var brot:Boolean;
		private var ox:Number;
		private var oy:Number;
		private var orx:Number;
		private var ory:Number;

		public function UIMovie(top:int,right:int,bottom:int,left:int,centeru:int,centerv:int)
		{
			posInfo = {"top":top, "right":right, "bottom":bottom, "left":left, "centerU":centeru, "centerV":centerv};

			initialize();

			if (stage) { addedToStage(null); }
			else       { addEventListener(Event.ADDED_TO_STAGE, addedToStage, false, 0, true); }
		}
		protected function initialize()
		{
            //Original width determines the width at 100% with original contents.
            //_originalWidth = super.width / super.scaleX;
            //_originalHeight = super.height / super.scaleY;

			thisWidth     = this.width;
			thisHeight    = this.height;

			beScale       = false;
			beDrag        = false;
			be3DTransform = false;
			beBlurFilter  = false;
			beMovieView   = false;
			isActiveState = true;
			isFirstInit   = true;

			beMovieView = checkBeCloseView();
			if (beMovieView)
			{
				/**
				 * frame script
				 *
				 * "movie_in"
				 * "movie_stay"
				 * "moive_out"
				 */
				this.addFrameScript(0, firstFrame);
				this.addFrameScript(FrameByLable.labelFrame(this, "movie_in") - 1, inFrame);
				this.addFrameScript(3, updateView);//???why swf content is loaded completely when it get the third frame.
				this.addFrameScript(FrameByLable.labelFrame(this, "movie_stay") - 1, stayFrame);
				this.addFrameScript(this.totalFrames - 1, lastFrame);
			}

			this.addEventListener(MouseEvent.MOUSE_DOWN, onBtnDown);

			//default to open and initialize this movieClip
			//initializeView();
        }
		public function checkBeCloseView() : Boolean
		{
			return (FrameByLable.labelFrame(this, "movie_stay") != 0);
		}
		protected function addedToStage(evt:Event = null) : void
		{
			removeEventListener(Event.ADDED_TO_STAGE, addedToStage, false);

			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align     = StageAlign.TOP_LEFT;

			stage.addEventListener(Event.RESIZE, resizeStage);
			resizeStage();

			if(be3DTransform){init();}
		}

		private function onBtnDown(e:MouseEvent) : void
		{
			if (beDrag)
			{
				var rect:Rectangle = new Rectangle(0, 0, stageWidth, stageHeight);
				this.startDrag(false, rect);
				this.addEventListener(MouseEvent.MOUSE_UP, onBtnUp);
			}
		}
		private function onBtnUp(e:MouseEvent) : void
		{
			this.stopDrag();
			checkPosition();

			this.removeEventListener(MouseEvent.MOUSE_UP, onBtnUp);
		}
		private function resizeStage()
		{
			stageWidth = stage.stageWidth;
			stageHeight = stage.stageHeight;
			resetPos(posInfo);
		}
		public function resetPos(posInfo:Object) : void
		{
			if (posInfo.top == 0 && posInfo.right == 0 && posInfo.bottom == 0 && posInfo.left == 0 && posInfo.centerU == 0 && posInfo.centerV == 0)
			{
				return;
			}
			var _posX:int = 0;
			var _posY:int = 0;

			if (posInfo.top!=0 && posInfo.left!=0)
			{
				_posX = posInfo.left == 1?0:posInfo.left;
				_posY = posInfo.top == 1?0:posInfo.top;
			}
			else if (posInfo.top!=0 && posInfo.right!=0)
			{
				_posX = stageWidth - (posInfo.right == 1?0:posInfo.right);
				_posY = posInfo.top == 1?0:posInfo.top;
			}
			else if (posInfo.bottom!=0 && posInfo.left!=0)
			{
				_posX = posInfo.left == 1?0:posInfo.left;
				_posY = stageHeight - (posInfo.bottom == 1?0:posInfo.bottom);
			}
			else if (posInfo.bottom!=0 && posInfo.right!=0)
			{
				_posX = stageWidth - (posInfo.right == 1?0:posInfo.right);
				_posY = stageHeight - (posInfo.bottom == 1?0:posInfo.bottom);
			}
			else if (posInfo.centerU!=0 && posInfo.centerV!=0)
			{
				_posX = stageWidth / 2 + (posInfo.centerU == 1?0:posInfo.centerU);
				_posY = stageHeight / 2 + (posInfo.centerV == 1?0:posInfo.centerV);
			}
			else if (posInfo.centerU!=0 && posInfo.top!=0)
			{
				_posX = stageWidth / 2 + (posInfo.centerU == 1?0:posInfo.centerU);
				_posY = posInfo.top == 1?0:posInfo.top;
			}
			else if (posInfo.centerU!=0 && posInfo.bottom!=0)
			{
				_posX = stageWidth / 2 + (posInfo.centerU == 1?0:posInfo.centerU);
				_posY = stageHeight - (posInfo.bottom == 1?0:posInfo.bottom);
			}
			else if (posInfo.centerV!=0 && posInfo.left!=0)
			{
				_posX = posInfo.left == 1?0:posInfo.left;
				_posY = stageHeight / 2 + (posInfo.centerV == 1?0:posInfo.centerV);
			}
			else if (posInfo.centerV!=0 && posInfo.right!=0)
			{
				_posX = stageWidth - (posInfo.right == 1?0:posInfo.right);
				_posY = stageHeight / 2 + (posInfo.centerV == 1?0:posInfo.centerV);
			}

			if(isFirstInit)
			{
				this.x = _posX;
				this.y = _posY;
				isFirstInit = false;
			}
			else
			{
				TweenLite.to(this, 0.3, { x:_posX, y:_posY, ease:Sine.easeOut } );
			}
		}

		protected function checkPosition()
		{
			this.x > stageWidth - this.width / 2   ? this.x = stageWidth - this.width / 2     : this.x;
			this.x < this.width / 2                ? this.x = this.width / 2                  : this.x;
			this.y > stageHeight - this.height / 2 ? this.y = (stageHeight - this.height / 2) : this.y;
			this.y < this.height / 2               ? this.y = this.height / 2                 : this.y;
		}

		protected function firstFrame()
		{
			this.stop();
		}
		protected function updateView()
		{
			updateDataView();
		}
		protected function inFrame()
		{
			//updateDataView();
		}
		protected function stayFrame()
		{
			this.stop();
		}
		protected function lastFrame()
		{
			this.stop();
			this.visible = false;
			//disableStageEvents();
		}
		public function updateDataView()
		{
		}

		protected function movieOut()
		{
			trace(":::::::::::::movieOut");
			this.gotoAndPlay("movie_out");
		}
		protected function movieIn()
		{
			if (!this.visible) { this.visible = true; }
			trace(":::::::::::::movieIn");
			this.gotoAndPlay("movie_in");

			dispatchEvent(new MovieEvent(MovieEvent.MOVIE_IN,true));
		}


		/**
		 * ------------------------------------
		 * control object's data and show state
		 * ------------------------------------
		 */
		public function initializeView()
		{
			openView();
		}
		public function openView()
		{
			movieIn();
		}
		public function closeView()
		{
			movieOut();
		}
		public function activeView()
		{
			if (this.visible&&!isActiveState)
			{
				enableEvent();
				setActiveState();

				isActiveState = true;
			}
		}
		public function inactiveView()
		{
			if (this.visible&&isActiveState)
			{
				disableEvent();
				setInactiveState();

				isActiveState = false;
			}
		}
		public function enableEvent()
		{
			this.mouseChildren = true;
			this.mouseEnabled = true;
		}
		public function disableEvent()
		{
			this.mouseChildren = false;
			this.mouseEnabled = false;
		}


		private function setInactiveState()
		{
			//trace("beBlurFilter:" + beBlurFilter + "/" + "beScale:" + beScale);
			var _z:int;
			if (!beScale)         { _z = 0; }
			else
			{
				if (beBlurFilter) { _z = 200; }
				else              { _z = 500; }
			}

			if (!beBlurFilter)
			{
				TweenLite.to(this, 0.5, { z:_z, alpha:0.3, ease:Strong.easeOut } );
			}
			else
			{
				blurValue = 1;
				TweenLite.to(this, 0.5, { z:_z, ease:Strong.easeOut, onUpdate:setUpdateToBlur, onComplete:setFilterBlur } );
			}
		}
		private function setActiveState()
		{
			if (!beBlurFilter)
				TweenLite.to(this, 0.3, { z:0, alpha:1, ease:Strong.easeOut } );
			else
				TweenLite.to(this, 0.3, { z:0, ease:Strong.easeOut, onUpdate:setUpdateToClear, onComplete:setFilterClear } );
		}
		private function setUpdateToBlur()
		{
			blurValue += 0.2;
			Filters.setBlurFilter(this, blurValue);
		}
		private function setFilterBlur():void
		{
		}
		private function setUpdateToClear():void
		{
			if (blurValue > 1)
			{
				blurValue -= 0.2;
				Filters.setBlurFilter(this, blurValue);
			}
			else
			{
				blurValue = 0;
				Filters.setBlurFilter(this, blurValue);
				return;
			}
		}
		private function setFilterClear()
		{
			blurValue = 0;
			Filters.setBlurFilter(this, blurValue);
		}

		private function init()
		{
			// _global.gfxExtensions = true;
			// Tween.init();

			panel = this;
			//panel.bg.gotoAndPlay("open");

			zScale = 3;

			brot = false;
			ox = 0;
			oy = 0;
			orx = 0;
			ory = 0;

			stage.addEventListener(MouseEvent.MOUSE_MOVE, handleMouseMove, false, 0, true);
			stage.addEventListener(MouseEvent.MOUSE_DOWN, handleMouseDown, false, 0, true);
			stage.addEventListener(MouseEvent.MOUSE_UP, handleMouseUp, false, 0, true);
		}

		private function handleMouseMove(event:MouseEvent):void
		{
			if (brot) calcRotations();
		}

		private function handleMouseDown(event:MouseEvent)
		{
			brot = true;
			ox = root.mouseX;
			oy = root.mouseY;
			orx = -panel.rotationY;
			ory = panel.rotationX;

			stageDrag(true);
		}

		private function handleMouseUp(event:MouseEvent)
		{
			brot = false;

			stageDrag(false);
		}

		////////////////////////////////////////////////////////////////////////////
		// 3D Transformation code
		////////////////////////////////////////////////////////////////////////////
		private function calcRotations():void
		{
			var rotX:Number = orx + ((root.mouseX - ox) / 1024) * 90;
			var rotY:Number = ory + ((root.mouseY - oy) / 1024) * 90;

			panel.rotationY = -rotX;
			panel.rotationX = rotY;
		}

		private function stageDrag(bool:Boolean) : void
		{
			stagePressed = bool;
			//if (bool){object3DOut();}
		}
	}
}