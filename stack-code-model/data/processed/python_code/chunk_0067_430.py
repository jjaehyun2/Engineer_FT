package qin.freeViewer{
	public class ConfigObject {
		public var mode_num:Number = 0;
		//这个属性指明了打开文件后是一次生成全部页面，以后切换显示（0），还是预排版后显示一页生成一页（1）。
		public var velAlphaUpperBound_num:Number = 1;
		//这个属性指明了用于表示力度的减字透明度的最高值。
		public var velAlphaLowerBound_num:Number = 0.1;
		//这个属性指明了用于表示力度的减字透明度的最低值。
	}
}