package as3lib.js
{
	import flash.external.ExternalInterface;
	/**
	 * 获取浏览器的信息（包括系统分辨率）
	 */
	public class BrowerInfoJS
	{
		private static var jsXML:XML =   
			<script>   
			<![CDATA[   
				//函数：获取尺寸
				function(){
					var winWidth = 0;
					var winHeight = 0;
					//获取窗口宽度 
					if (window.innerWidth)winWidth = window.innerWidth; 
					else if ((document.body) && (document.body.clientWidth))winWidth = document.body.clientWidth; 
					//获取窗口高度
					if (window.innerHeight)winHeight = window.innerHeight;
					else if ((document.body) && (document.body.clientHeight))winHeight = document.body.clientHeight; 
					//通过深入Document内部对body进行检测，获取窗口大小
					if (document.documentElement && document.documentElement.clientHeight && document.documentElement.clientWidth){
						winHeight = document.documentElement.clientHeight;
						winWidth = document.documentElement.clientWidth;
					}
					//结果输出至两个文本框
					return winWidth+","+winHeight;
			   }
			]]>   
			</script>;
		
		//返回浏览器内窗口宽度
		public static function getWidth():Number{
			var str:String=ExternalInterface.call(jsXML);
			return Number(str.split(",")[0]);
		}
		//返回浏览器内窗口高度
		public static function getHeight():Number{
			var str:String=ExternalInterface.call(jsXML);
			return Number(str.split(",")[1]);
		}
//		s += " 网页可见区域宽："+ document.body.clientWidth+"\n";    
//		s += " 网页可见区域高："+ document.body.clientHeight+"\n";    
//		s += " 网页可见区域宽："+ document.body.offsetWidth + " (包括边线和滚动条的宽)"+"\n";    
//		s += " 网页可见区域高："+ document.body.offsetHeight + " (包括边线的宽)"+"\n";    
//		s += " 网页正文全文宽："+ document.body.scrollWidth+"\n";    
//		s += " 网页正文全文高："+ document.body.scrollHeight+"\n";    
//		s += " 网页被卷去的高(ff)："+ document.body.scrollTop+"\n";    
//		s += " 网页被卷去的高(ie)："+ document.documentElement.scrollTop+"\n";    
//		s += " 网页被卷去的左："+ document.body.scrollLeft+"\n";    
//		s += " 网页正文部分上："+ window.screenTop+"\n";    
//		s += " 网页正文部分左："+ window.screenLeft+"\n";    
//		s += " 屏幕分辨率的高："+ window.screen.height+"\n";    
//		s += " 屏幕分辨率的宽："+ window.screen.width+"\n";    
//		s += " 屏幕可用工作区高度："+ window.screen.availHeight+"\n";    
//		s += " 屏幕可用工作区宽度："+ window.screen.availWidth+"\n";    
//		s += " 你的屏幕设置是 "+ window.screen.colorDepth +" 位彩色"+"\n";    
//		s += " 你的屏幕设置 "+ window.screen.deviceXDPI +" 像素/英寸"+"\n";   
	}
}