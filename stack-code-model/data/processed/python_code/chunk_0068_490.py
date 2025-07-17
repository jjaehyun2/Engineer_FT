package com.lowoui_as.sample.chapter
{
	import com.greensock.TweenLite;
	import com.greensock.easing.*;
	import com.lowoui_as.WidgetManager;
	import com.lowoui_as.config.ConfigLang;
	import com.lowoui_as.core.UIMovie;
	import flash.events.MouseEvent;

	public class Manager extends UIMovie
	{
		public var isOpenCharpterSelect:Boolean;
		public var isOpenCharpterDetail:Boolean;

		public var __btnConfirm:Object;
		public var __bg:Object;

		public function Manager()
		{
			super(0, 0, 0, 0, 0, 0);
		}

		override protected function initialize()
		{
			super.initialize();

			isOpenCharpterSelect = false;
			isOpenCharpterDetail = false;

			__btnConfirm = this["btnConfirm"];
			__bg         = this["bg"];


			__btnConfirm.setName(ConfigLang.Type.Comn_Btn_Close);
			__btnConfirm.setSize(120, 30);

			__btnConfirm.addEventListener(MouseEvent.CLICK, onConfirm);

			initializeView();
		}

		override public function updateDataView()
		{
			//AS2US.InitializeSceneWidget("Charpters","Charpters");

			//test
			//var arr:Array = new Array(10);
			//UpdateCharptersList(arr);
		}

		private function onConfirm(e:MouseEvent):void
		{
			closeView();
		}

		override protected function lastFrame()
		{
			super.lastFrame();

			this["charptersCon"].disableStageEvents();
			WidgetManager.ins.UnloadWidget("Charpters");

			WidgetManager.activeWidgetView();
		}

		override protected function movieIn()
		{
			super.movieIn();
			//childrenMcMovie(this,"movie_in");

			this["charptersCon"].openView();
			isOpenCharpterSelect = true;

			__btnConfirm.z = 200;
			__btnConfirm.alpha = 0;
			TweenLite.to(__btnConfirm, 0.5, { delay:0.2, z: 0, alpha:1, ease:Strong.easeOut } );
			__bg.alpha = 0;
			TweenLite.to(__bg, 0.5, { delay:0, z: 0, alpha:1, ease:Strong.easeOut } );

			//WidgetManager.inactiveWidgetView();
		}

		override protected function movieOut()
		{
			super.movieOut();
			//childrenMcMovie(this,"movie_out");
			if (this["charpterDetailCon"].visible)
				this["charpterDetailCon"].closeView();
			this["charptersCon"].closeView();

			TweenLite.to(btnConfirm, 0.3, { delay:0, z:200, alpha:0, ease:Strong.easeOut } );
			TweenLite.to(__bg, 0.5, { delay:0, z: 0, alpha:0, ease:Strong.easeOut } );
		}

		override public function inactiveView()
		{
			super.inactiveView();

			if (this["charpterDetailCon"].visible) this["charpterDetailCon"].inactiveView();
			else this["charptersCon"].inactiveView();
		}

		override public function activeView()
		{
			super.activeView();

			if (this["charpterDetailCon"].visible) this["charpterDetailCon"].activeView();
			else this["charptersCon"].activeView();
		}

		override public function resetPos(posInfo:Object) : void
		{
			//super.resetPos(posInfo);

			TweenLite.to(__btnConfirm, 0.5, { x:stageWidth / 2-120/2, y:stageHeight - 50, alpha:1, ease:Sine.easeOut } );

			__bg.width=stageWidth;
			__bg.height=stageHeight;
			__bg.x=stageWidth/2;
			__bg.y=stageHeight/2;
			TweenLite.to(__bg, 0.3, { alpha:1, ease:Sine.easeOut } );
		}

		public function UpdateCharptersList(cArr:Array) : void
		{
		}
	}
}