package com
{
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	
	import lzm.starling.STLStarup;
	
	public class MainStartup extends STLStarup
	{
		public function MainStartup()
		{
			super();
			
			// 支持 autoOrient
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.color = 0x333333;
			stage.frameRate = 60;
			
			initStarling(GameMainClass,stage.fullScreenWidth,true);// 这里如果打pc包要修改显示分辨率调试
		}
	}
}