package com.vo
{
	import mx.core.UIComponent;
	
	/**
	 * 消息提示框2
	 * @author 王明凡
	 */
	public class MessageAlert2VO
	{
		//提示消息
		public var msg:String;
		//字体颜色
		public var color:String="#ed0404";
		//x位置
		public var x:int=400;
		//y位置
		public var y:int=50;
		//间隔毫秒
		public var delay:int=3000;
		//指定显示父对象
		public var appUI:UIComponent;
	}
}