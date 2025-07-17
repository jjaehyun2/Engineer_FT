package com.lowoui_as.core
{
	import flash.display.MovieClip;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.text.TextField;

	public class UIComponent extends MovieClip
	{
		//_labelHash = generateLabelHash(this);
		protected var thisWidth:Number;
		protected var thisHeight:Number;
		protected var selectedState:Boolean;
		protected var enabledState:Boolean;

		public function UIComponent()
		{
			initialize();

			if (stage) { addedToStage(null); }
			else       { addEventListener(Event.ADDED_TO_STAGE, addedToStage, false, 0, true); }
		}
		protected function addedToStage(evt:Event = null) : void
		{
			removeEventListener(Event.ADDED_TO_STAGE, addedToStage, false);

			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align     = StageAlign.TOP_LEFT;
		}
		protected function initialize(){}

		public function setName(str:String) : void
		{
		}
		public function setSize(wid:uint, hei:uint) : void
		{
		}
		public function setType(str:String) : void
		{
		}
		public function setFocus(bool:Boolean) : void
		{
		}
	}
}