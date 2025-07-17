package view {
	import config.ConfigUtil;
	import events.LayoutEvent;
	import flash.display.Graphics;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.MouseEvent;
	import flash.text.TextField;
	import model.YuanJian;
	import model.YuanJianManager;
	
	/**
	 * ...
	 * @author hongjie
	 */
	public final class YuanJianQu extends Sprite {
		
		private var _w:int;
		
		private var _h:int;
		
		private var _yuanJianContainer:Sprite;
		
		private var _yuanJianSelected:Vector.<YuanJian> = new Vector.<YuanJian>();
		
		private var _startCheckMoved:Boolean;
		
		private var _mouseDownX:Number;
		
		private var _mouseDownY:Number;
		
		public function YuanJianQu(width:int, height:int) {
			super();
			_w = width;
			_h = height;
			
			var g:Graphics = this.graphics;
			g.lineStyle(1, 0xff0000);
			g.moveTo(0, 0);
			g.lineTo(width - 1, 0);
			g.lineTo(width - 1, height);
			g.lineTo(0, height);
			g.lineTo(0, 0);
			
			g.beginFill(0xff0000, 0);
			g.drawRect(0, 0, width, height);
			g.endFill();
			
			_yuanJianContainer = new Sprite();
			addChild(_yuanJianContainer);
			g = _yuanJianContainer.graphics;
			g.beginFill(0xff0000, 0);
			g.drawRect(0, 0, width, height - 60);
			g.endFill();
			
			const mask:Shape = new Shape();
			mask.graphics.beginFill(0, 0);
			mask.graphics.drawRect(0, 0, width, height - 60);
			mask.graphics.endFill();
			addChild(mask);
			_yuanJianContainer.mask = mask;
			
			//var btn:Sprite = createBtn('垂直线槽', 0x5b9bd5);
			//btn.y = ((60 - 30) >> 1) + height - 60;
			//btn.addEventListener(MouseEvent.MOUSE_DOWN, _onStartDragVXianCao);
			//addChild(btn);
			//
			//btn = createBtn('水平线槽', 0x5b9bd5);
			//btn.x = 70;
			//btn.y = ((60 - 30) >> 1) + height - 60;
			//btn.addEventListener(MouseEvent.MOUSE_DOWN, _onStartDragHXianCao);
			//addChild(btn);
			//
			//btn = createBtn('轨道', 0xffc000, 30);
			//btn.x = 140;
			//btn.y = ((60 - 30) >> 1) + height - 60;
			//btn.addEventListener(MouseEvent.MOUSE_DOWN, _onStartDragGuiDao);
			//addChild(btn);
			//
			//btn = createBtn('虚拟轨道', 0xffc000);
			//btn.x = 180;
			//btn.y = ((60 - 30) >> 1) + height - 60;
			//btn.addEventListener(MouseEvent.MOUSE_DOWN, _onStartDragJiaGuiDao);
			//addChild(btn);
			//
			//btn = createBtn('卡扣', 0x00b050, 30);
			//btn.x = 250;
			//btn.y = ((60 - 30) >> 1) + height - 60;
			//btn.addEventListener(MouseEvent.MOUSE_DOWN, _onStartDragKaKou);
			//addChild(btn);
			
			ConfigUtil.instance.addEventListener(LayoutEvent.IMPORT_XML_OK, _onReset);
			
			this.addEventListener(MouseEvent.MOUSE_WHEEL, _onMouseWheel);
			_yuanJianContainer.addEventListener(MouseEvent.MOUSE_DOWN, _onContainerMouseDown);
			_yuanJianContainer.addEventListener(MouseEvent.MOUSE_MOVE, _onContainerMouseMoved);
		}
		
		public function addYuanJian(yuanJian:YuanJian):void {
			_yuanJianContainer.addChild(yuanJian);
		}
		
		public static function createBtn(name:String, bgColor:int = 0x9dc3e6, w:int = 60):Sprite {
			var btn:Sprite = new Sprite();
			const g:Graphics = btn.graphics;
			g.beginFill(bgColor);
			g.drawRect(0, 0, w, 30);
			g.endFill();
			var tf:TextField = new TextField();
			tf.mouseEnabled = false;
			tf.text = name;
			tf.textColor = 0xffffff;
			tf.x = (w - tf.textWidth) >> 1;
			tf.y = (30 - tf.textHeight) >> 1;
			tf.width = w;
			tf.height = 30;
			btn.addChild(tf);
			return btn;
		}
		
		private function _onReset(e:LayoutEvent):void {
			_yuanJianContainer.removeChildren();
			
			var x:int = 0, y:int = 0, gap:int = 10, maxY:int = 0, maxH:int = 0;
			var yuanJian:YuanJian;
			for (var i:int = 0; i < YuanJianManager.instance.itemArr.length; i++) {
				yuanJian = YuanJianManager.instance.itemArr[i];
				if (x + yuanJian.reallyWidth > _w) {
					x = 0;
					maxH = 0;
					y = maxY + gap;
				}
				yuanJian.x = x;
				yuanJian.y = y;
				yuanJian.yuanJianX = x;
				yuanJian.yuanJianY = y;
				//yuanJian.addEventListener(MouseEvent.MOUSE_DOWN, _onStartDrag);
				yuanJian.addEventListener(MouseEvent.CLICK, _onYuanJianClicked);
				_yuanJianContainer.addChild(yuanJian);
				x += yuanJian.reallyWidth + gap;
				maxY = yuanJian.reallyHeight + yuanJian.y > maxY ? yuanJian.reallyHeight + yuanJian.y : maxY;
				maxH = maxH > yuanJian.reallyHeight ? maxH : yuanJian.reallyHeight;
			}
			
			var containerHeight:int = maxY + maxH;
			if (containerHeight > _h - 60) {
				// 需要缩小
				var scale:Number = (_h - 60) / containerHeight;
				_yuanJianContainer.scaleX = scale;
				_yuanJianContainer.scaleY = scale;
			} else {
				_yuanJianContainer.scaleX = 1;
				_yuanJianContainer.scaleY = 1;
			}
			this.dispatchEvent(new LayoutEvent(LayoutEvent.YUAN_JIAN_QU_INITED, e.xml, null, false, null, e.layoutXML));
		}
		
		private function _onYuanJianClicked(e:MouseEvent):void {
			const yuanJian:YuanJian = e.currentTarget as YuanJian;
			if (yuanJian.parent == _yuanJianContainer) {
				if (!yuanJian.isSelected) {
					yuanJian.isSelected = true;
					if (!e.ctrlKey) {
						for (var i:int = 0; i < _yuanJianSelected.length; i++) {
							_yuanJianSelected[i].isSelected = false;
						}
						_yuanJianSelected.length = 0;
					}
					_yuanJianSelected.push(yuanJian);
				} else {
					yuanJian.isSelected = false;
					for (i = 0; i < _yuanJianSelected.length; i++) {
						if (_yuanJianSelected[i] == yuanJian) {
							_yuanJianSelected.splice(i, 1);
						}
					}
				}
			}
		}
		
		//private function _onStartDrag(e:MouseEvent):void {
		//const yuanJian:YuanJian = e.currentTarget as YuanJian;
		//if (yuanJian.parent == _yuanJianContainer) {
		//dispatchEvent(new LayoutEvent(LayoutEvent.START_TO_DTAG_YUAN_JIAN, null, yuanJian));
		//}
		//}
		
		//private function _onStartDragVXianCao(e:MouseEvent):void {
		//dispatchEvent(new LayoutEvent(LayoutEvent.START_TO_DTAG_V_XIAN_CAO));
		//}
		//
		//private function _onStartDragHXianCao(e:MouseEvent):void {
		//dispatchEvent(new LayoutEvent(LayoutEvent.START_TO_DTAG_H_XIAN_CAO));
		//}
		//
		//private function _onStartDragGuiDao(e:MouseEvent):void {
		//dispatchEvent(new LayoutEvent(LayoutEvent.START_TO_DTAG_GUI_DAO));
		//}
		//
		//private function _onStartDragJiaGuiDao(e:MouseEvent):void {
		//dispatchEvent(new LayoutEvent(LayoutEvent.START_TO_DTAG_JIA_GUI_DAO));
		//}
		//
		//private function _onStartDragKaKou(e:MouseEvent):void {
		//dispatchEvent(new LayoutEvent(LayoutEvent.START_TO_DTAG_KA_KOU));
		//}
		
		private function _onMouseWheel(evt:MouseEvent):void {
			if (evt.delta < 0) {
				//向下滚动
				if (_yuanJianContainer.scaleX > .2) {
					_yuanJianContainer.scaleX -= .05;
					_yuanJianContainer.scaleY -= .05;
				}
			} else {
				if (_yuanJianContainer.scaleX < 1) {
					_yuanJianContainer.scaleX += .05;
					_yuanJianContainer.scaleY += .05;
				}
			}
		}
		
		private function _onContainerMouseMoved(e:MouseEvent):void {
			if (_startCheckMoved && e.buttonDown) {
				if (_yuanJianSelected.length > 0) {
					if (Math.abs(e.stageY - _mouseDownY) > 10 && Math.abs(e.stageX - _mouseDownX) > 10) {
						dispatchEvent(new LayoutEvent(LayoutEvent.START_TO_DTAG_YUAN_JIAN, null, null, false, null, null, _yuanJianSelected.slice()));
						_yuanJianSelected.length = 0;
						_startCheckMoved = false;	
					}
				}
			}
		}
		
		private function _onContainerMouseDown(e:MouseEvent):void {
			_startCheckMoved = true;
			_mouseDownX = e.stageX;
			_mouseDownY = e.stageY;
		}
	
	}

}