/*
 * @author Ryan C. Knaggs
 * @date 11/2/2009
 * The Error_View class is designed
 * to display any error that may occur
 * upon any file that is required for
 * running this application
 */

package views
{
	import flash.events.MouseEvent;
	import flash.geom.Point;
	
	import libs.vo.GlobalsVO;
	
	import mx.containers.Canvas;
	import mx.controls.Image;
	import mx.controls.ToolTip;
	import mx.managers.PopUpManager;
	import mx.managers.SystemManager;
	
	
	
	public class Error_View
	{
		
		
		
		private var _errorContainer:Canvas;
		private var _asset:Object;
		private var _errorMsg:String;
		private var _toolTip:ToolTip;
		
		
		
		
		public function Error_View(asset:Object,errorMsg:String) {
			this._asset = asset;
			this._errorMsg = errorMsg;
			_asset.addEventListener(MouseEvent.MOUSE_OVER,onToolTip);
			_asset.addEventListener(MouseEvent.MOUSE_MOVE,onToolTip);
			_asset.addEventListener(MouseEvent.MOUSE_OUT,onToolTip);
			_toolTip = null;
		}
		
		
		
		
		public function onToolTip(e:MouseEvent):void {
			switch(e.type) {
				case MouseEvent.MOUSE_OVER :
					var app:Object = GlobalsVO.getGlobal(GlobalsVO.APPLICATION);
					
					if(_toolTip != null) {
						PopUpManager.removePopUp(_toolTip);
					}
					
					_errorContainer = new Canvas();
					app.addChild(_errorContainer);
					var image:Image = e.currentTarget as Image;
					_toolTip = PopUpManager.createPopUp(_errorContainer,ToolTip) as ToolTip;
					_toolTip.text = _errorMsg;
					positionToolTip(e);
				break;
				
				
				case MouseEvent.MOUSE_MOVE :
					positionToolTip(e);
				break;
				
				case MouseEvent.MOUSE_OUT :
					if(_toolTip != null) {
						PopUpManager.removePopUp(_toolTip);
						_toolTip = null;
					}
				break;
				
			}
		}
		
		
		
		
		private function positionToolTip(e:MouseEvent):void {
			try {
				var pt:Point = new Point(e.localX, e.localY);
           		pt = e.target.localToGlobal(pt);
           		// Position the tooltip next to the mouse
				_toolTip.x = pt.x + 10;
				_toolTip.y = pt.y - 5;
			} catch(e:Error){}
		}
	}
}