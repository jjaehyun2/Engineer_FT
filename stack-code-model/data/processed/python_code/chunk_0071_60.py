package as3lib.core.export
{
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.DisplayObject;
	import flash.display.DisplayObjectContainer;
	import flash.geom.Matrix;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.net.FileReference;
	import flash.utils.ByteArray;
	
	import mx.controls.Alert;
	import mx.graphics.codec.IImageEncoder;

	/**
	 * 功能：将Flex组件导出图片(结合矩形Rectangle可做出截屏功能)。
	 * @author gyb
	 * @date：2015-1-20 上午10:34:12
	 * 前提要求是：只支持flash player 10.0以上版本
	 */
	public function exportImg(display:DisplayObject,imgType:String,_imgEncoder:IImageEncoder,rect:Rectangle=null):void
	{   
		var _fr:FileReference;
		_fr = new FileReference();   
		if(_fr.hasOwnProperty("save")) 
		{   
			var _w:Number = rect.width;
			var _h:Number = rect.height;
			var _byteArray:ByteArray;
			var _bmpData:BitmapData;
			var _rectBmpData:BitmapData;
			var _fillRect:Rectangle;
			
			_bmpData = new BitmapData(display.width,display.height,true,0x00FFFF);   
			_bmpData.draw(display); 
			
			_byteArray = _bmpData.getPixels(rect);
			_byteArray.position = 0;
			
			_fillRect=new Rectangle(0, 0, _w,_h);
			
			_rectBmpData = new BitmapData(_w,_h);
			_rectBmpData.setPixels(_fillRect, _byteArray);
			
			var data:ByteArray = _imgEncoder.encode(_rectBmpData);
			var imageName:String  = display.name+imgType;
			_fr.save(data,imageName);   
		} 
		else
		{   
			Alert.show("当前flash player版本不支持此功能,请安装10.0.0以上版本！","提示");   
			
		}   
	} 
}