package com.lowoui_as.sample.chapter
{
	import com.greensock.easing.*;
	import com.greensock.TweenLite;
	import com.lowoui_as.config.ConfigLang;
	import com.lowoui_as.core.UIMovie;
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	import flash.text.TextField;

	public class ChapterCon extends UIMovie
	{
		private var charpterIndicatorArr:Vector.<Object>;

		//mc instance reference object
		private var __title:TextField;
		private var __charpterSelectCon:MovieClip;
		private var __btnPrev:Object;
		private var __btnNext:Object;

		//mouse drag event
		private const dragAccuracy:uint = 200;
		private var   beginX      :Number;
		private var   _beginX     :Number;
		private var   endX        :Number;
		private var   _endX       :Number;
		private var   deltaX      :int;
		private var   isMouseDrag :Boolean;

		private const maxCharpter:uint = 6;
		private var currCharpterIdx:int;

		public function ChapterCon()
		{
			super(0, 0, 0, 0, 1, 1);
		}

		override protected function initialize()
		{
			super.initialize();

			beScale        = false;
			beDrag         = false;
			be3DTransform  = false;
			beBlurFilter   = true;

			charpterIndicatorArr = new Vector.<Object>();
			isMouseDrag = false;

			__title             = this["title"];
			__charpterSelectCon = this["charpterSelectCon"];
			__btnPrev           = this["btnPrev"];
			__btnNext           = this["btnNext"];

			for (var j:int = 0; j < maxCharpter; j++)
			{ charpterIndicatorArr.push(this["c" + (j + 1)]); }

			charpterIndicatorArr[1].gotoAndStop(2);
			__charpterSelectCon.updateShow(0);

			__title.text = ConfigLang.Type.Charpters_Title;
			__btnPrev.addEventListener(MouseEvent.CLICK, onChangeCharpter);
			__btnNext.addEventListener(MouseEvent.CLICK, onChangeCharpter);

			this.visible = false;
		}

		override protected function addedToStage(evt:Event = null) : void
		{
			super.addedToStage(null);

			stage.addEventListener(MouseEvent.MOUSE_DOWN, onStageDown);
			stage.addEventListener(KeyboardEvent.KEY_DOWN, onKeyPress);
		}

		public function disableStageEvents()
		{
			stage.removeEventListener(MouseEvent.MOUSE_DOWN, onStageDown);
			stage.removeEventListener(KeyboardEvent.KEY_DOWN, onKeyPress);
		}

		private function onKeyPress(e:KeyboardEvent):void
		{
			trace(e.keyCode);
			switch (e.keyCode)
			{
				case 37:
					moveCharpter(1);
					break;
				case 39:
					moveCharpter(-1);
					break;
				case 13:
					if(this["root"].isOpenCharpterSelect){__charpterSelectCon.openCharpterDetail();}
					else if(this["root"].isOpenCharpterDetail) { this["root"]["charpterDetailCon"].closeView();}
					break;
				default:
			}
		}

		private function onStageDown(e:MouseEvent):void
		{
			isMouseDrag = true;
			beginX = mouseX;
			_beginX = mouseX;
			stage.addEventListener(MouseEvent.MOUSE_UP, onStageUp);
			stage.addEventListener(MouseEvent.MOUSE_MOVE, onStageMove);

			__charpterSelectCon._isDrag = false;
		}

		private function onStageMove(e:MouseEvent):void
		{
			if (isMouseDrag)
			{
				_endX = mouseX;
				deltaX = int(_endX - _beginX);
				_beginX = _endX;

				__charpterSelectCon.updatePos(deltaX);

				__charpterSelectCon._isDrag = true;
			}
		}

		private function onStageUp(e:MouseEvent):void
		{
			if (isMouseDrag)
			{
				isMouseDrag = false;
				endX = mouseX;
				stage.removeEventListener(MouseEvent.MOUSE_UP, onStageUp);
				stage.removeEventListener(MouseEvent.MOUSE_MOVE, onStageMove);

				var mIdx:int = Math.abs((endX - beginX)/dragAccuracy);
				endX - beginX > 0?mIdx = 0 - mIdx:mIdx;
				moveCharpter(mIdx);
			}
		}

		override public function updateDataView()
		{
			//send request
			//AS2US.InitializeSceneWidget("Charpters","CharpterSelectList");
		}

		override protected function movieIn()
		{
			super.movieIn();

			this.z = -500;
			this.alpha = 0;
			TweenLite.to(this, 1, { delay:0, z:0, alpha:1, ease:Strong.easeInOut } );
		}

		override protected function movieOut()
		{
			super.movieOut();
			TweenLite.to(this, 0.5, { delay:0, z: -500, alpha:0, ease:Strong.easeOut } );
		}

		private function onChangeCharpter(e:MouseEvent):void
		{
			if (e.currentTarget.name == "btnPrev")      { moveCharpter(1); }
			else if (e.currentTarget.name == "btnNext") { moveCharpter(-1); }
		}

		private function moveCharpter(dir:int):void
		{
			currCharpterIdx += dir;
			if (dir < 0)      { currCharpterIdx < 0?currCharpterIdx = 0:currCharpterIdx; }
			else if (dir > 0) { currCharpterIdx >maxCharpter-1?currCharpterIdx = maxCharpter-1:currCharpterIdx; }

			__charpterSelectCon.updateShow(currCharpterIdx);
			updateIndicator(currCharpterIdx);
		}

		private function updateIndicator(idx:uint):void
		{
			for each (var obj:Object in charpterIndicatorArr)
			{obj.gotoAndStop(1); }

			charpterIndicatorArr[idx].gotoAndStop(2);
		}
	}
}