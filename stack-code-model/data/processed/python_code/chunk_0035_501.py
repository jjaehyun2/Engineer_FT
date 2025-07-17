package com.lowoui_as.sample.chapter
{
	import com.greensock.easing.*;
	import com.greensock.TweenLite;
	import com.lowoui_as.config.ConfigLang;
	import com.lowoui_as.core.UIMovie;
	import com.lowoui_as.Extension;
	import flash.events.MouseEvent;

	public class ChapterDetailCon extends UIMovie
	{
		private var __btnConfirm:Object;

		public function ChapterDetailCon()
		{
			super(0, 0, 0, 0, 1, 1);
		}

		override protected function initialize()
		{
			super.initialize();

			beScale        = false;
			beDrag         = true;
			be3DTransform  = false;
			beBlurFilter   = false;

			this["title"].text = ConfigLang.Type.Charpters_Name1;
			Extension.setTextDisabled(this["info"]["intro1"]);
			this["info"]["intro1"].htmlText =

			__btnConfirm = this["btnConfirm"];
			__btnConfirm.setName(ConfigLang.Type.Comn_Btn_Close);
			__btnConfirm.addEventListener (MouseEvent.CLICK, onBtn);
			this.visible = false;
		}

		private function onBtn(e:MouseEvent):void
		{
			closeView();
		}

		override protected function movieIn()
		{
			super.movieIn();

			this.z = -200;
			this.alpha = 1;
			TweenLite.to(this, 0.5, { delay:0, z:0, ease:Strong.easeInOut } );

			this["root"]["charptersCon"].inactiveView();
			this["root"].isOpenCharpterDetail = true;
			this["root"].isOpenCharpterSelect = false;
		}

		override protected function movieOut()
		{
			super.movieOut();
			TweenLite.to(this, 0.3, { delay:0, z: 600, alpha:0, ease:Strong.easeOut } );

			this["root"]["charptersCon"].activeView();
			this["root"].isOpenCharpterSelect = true;
			this["root"].isOpenCharpterDetail = false;
		}
	}
}