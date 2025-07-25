package com.roleobject.loader
{
	import flash.events.Event;
	import flash.net.URLLoaderDataFormat;
	
	/**
	 * 加载扩展类
	 * @author 王明凡
	 */
	public class ExtendLoader extends BasicLoader
	{
		
		public static const MEL_BYTEARRAY:String="mel_bytearray";
		
		public static const MEL_LOADERINFO:String="mel_loaderinfo";
		
		/**
		 * 加载类型
		 * 1.MEL_BYTEARRAY
		 * 2.MEL_LOADERINFO
		 * @default 
		 */
		private var type:String;
		
		public function ExtendLoader()
		{

		}
		/**
		 * 根据加载方式进行夹杂
		 * @param url
		 * @param type
		 * @param format
		 */
		public function extendOnLoaderURL(url:String,type:String=MEL_BYTEARRAY,format:String=URLLoaderDataFormat.BINARY):void
		{
			this.type=type;
			super.onLoaderURL(url,format);
		}
		/**
		 * 重写父类加载完成
		 * @param e
		 */
		override protected function onURLLoaderComplete(e:Event):void
		{
			if(type==MEL_BYTEARRAY)
			{
				super.onURLLoaderComplete(e);
			}
			else
			{
				byte=this.urlLD.data;
				super.onLoaderByte(byte);
			}
		}
		/**
		 * 重写父类垃圾清理
		 */
		override public function clear():void
		{
			type=null;
			super.clear();
		}
	}
}