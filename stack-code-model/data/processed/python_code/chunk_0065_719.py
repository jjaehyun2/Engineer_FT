package view {
	import adobe.utils.CustomActions;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.DisplayObjectContainer;
	import flash.display.Sprite;
	import model.YuanJian;
	
	/**
	 * ...
	 * @author hongjie
	 */
	public final class DragingBitmap extends Bitmap {
		
		public static const V_XIAN_CAO_W:int = 20;
		
		public static const V_XIAN_CAO_H:int = 100;
		
		public static const H_XIAN_CAO_W:int = 100;
		
		public static const H_XIAN_CAO_H:int = 20;
		
		public static const GUI_DAO_W:int = 100;
		
		public static const GUI_DAO_H:int = 20;
		
		public static const KA_KOU_W:int = 20;
		
		public static const KA_KOU_H:int = 30;
		
		//private var _yuanJian:YuanJian;
		
		private var _yuanJianArr:Vector.<YuanJian>;
		
		/**
		 * 0是垂直的线槽
		 * 1是水平的线槽
		 * 2是轨道
		 * 3是卡扣
		 */
		private var _subType:int = -1;
		
		private var _vXianCaoBtn:Sprite;
		
		private var _hXianCao:Sprite;
		
		private var _guiDao:Sprite;
		
		private var _kaKou:Sprite;
		
		private var _jiaGuiDao:Sprite;
		
		public function DragingBitmap() {
			super();
		}
		
		//public function get yuanJian():YuanJian {
		//return _yuanJian;
		//}
		//
		//public function set yuanJian(value:YuanJian):void {
		//subType = -1;
		//_yuanJian = value;
		//if (this.bitmapData) {
		//this.bitmapData.dispose();
		//this.bitmapData = null;
		//}
		//this.bitmapData = new BitmapData(_yuanJian.reallyWidth, _yuanJian.reallyHeight, true, 0);
		//this.bitmapData.draw(_yuanJian);
		//}
		
		public function get subType():int {
			return _subType;
		}
		
		public function set subType(value:int):void {
			_subType = value;
			if (this.bitmapData) {
				this.bitmapData.dispose();
				this.bitmapData = null;
			}
			if (_subType == Enum.V_XIAN_CAO) {
				this.bitmapData = new BitmapData(V_XIAN_CAO_W, V_XIAN_CAO_H, true, 0);
				this.bitmapData.draw(_createVXianCao());
			} else if (_subType == Enum.H_XIAN_CAO) {
				this.bitmapData = new BitmapData(H_XIAN_CAO_W, H_XIAN_CAO_H, true, 0);
				this.bitmapData.draw(_createHXianCao());
			} else if (_subType == Enum.GUI_DAO) {
				this.bitmapData = new BitmapData(GUI_DAO_W, GUI_DAO_H, true, 0);
				this.bitmapData.draw(_createGuiDao());
			} else if (_subType == Enum.KA_KOU) {
				this.bitmapData = new BitmapData(KA_KOU_W, KA_KOU_H, true, 0);
				this.bitmapData.draw(_createKaKou());
			} else if (_subType == Enum.JIA_GUI_DAO) {
				this.bitmapData = new BitmapData(100, 20, true, 0);
				this.bitmapData.draw(_createJiaGuiDao());
			}
		}
		
		public function get yuanJianArr():Vector.<YuanJian> {
			return _yuanJianArr;
		}
		
		public function set yuanJianArr(value:Vector.<YuanJian>):void {
			subType = -1;
			_yuanJianArr = value;
			if (this.bitmapData) {
				this.bitmapData.dispose();
				this.bitmapData = null;
			}
			const tmpSprite:Sprite = new Sprite();
			var oldParent:Vector.<DisplayObjectContainer> = new Vector.<DisplayObjectContainer>(), oldX:Vector.<Number> = new Vector.<Number>(), oldY:Vector.<Number> = new Vector.<Number>();
			var oldIsSelected:Vector.<Boolean> = new Vector.<Boolean>();
			var w:int = 0, h:int = 0;
			var yuanJian:YuanJian;
			ScaleLine.instance.visible = false;
			for (var i:int = 0; i < value.length; i++) {
				yuanJian = value[i];
				yuanJian.isSelected = false;
				
				oldParent[i] = yuanJian.parent;
				oldX[i] = yuanJian.x;
				oldY[i] = yuanJian.y;
				oldIsSelected[i] = yuanJian.isSelected;
				yuanJian.isSelected = false;
				yuanJian.parent.removeChild(yuanJian);
				yuanJian.x = w;
				yuanJian.y = 0;
				tmpSprite.addChild(yuanJian);
				
				
				w += yuanJian.reallyWidth;
				h = yuanJian.reallyHeight > h ? yuanJian.reallyHeight : h;
			}
			this.bitmapData = new BitmapData(w, h, true, 0);
			this.bitmapData.draw(tmpSprite);
			for (i = 0; i < value.length; i++) {
				yuanJian = value[i];
				yuanJian.x = oldX[i];
				yuanJian.y = oldY[i];
				yuanJian.isSelected = oldIsSelected[i];
				oldParent[i].addChild(yuanJian);
			}
			ScaleLine.instance.visible = true;
		}
		
		private function _createVXianCao():Sprite {
			if (!_vXianCaoBtn) {
				_vXianCaoBtn = new Sprite();
				_vXianCaoBtn.graphics.beginFill(0x5b9bd5);
				_vXianCaoBtn.graphics.drawRect(0, 0, V_XIAN_CAO_W, V_XIAN_CAO_H);
				_vXianCaoBtn.graphics.endFill();
			}
			return _vXianCaoBtn;
		}
		
		private function _createHXianCao():Sprite {
			if (!_hXianCao) {
				_hXianCao = new Sprite();
				_hXianCao.graphics.beginFill(0x5b9bd5);
				_hXianCao.graphics.drawRect(0, 0, H_XIAN_CAO_W, H_XIAN_CAO_H);
				_hXianCao.graphics.endFill();
			}
			return _hXianCao;
		}
		
		private function _createGuiDao():Sprite {
			if (!_guiDao) {
				_guiDao = new Sprite();
				_guiDao.graphics.beginFill(0xffc000);
				_guiDao.graphics.drawRect(0, 0, GUI_DAO_W, GUI_DAO_H);
				_guiDao.graphics.endFill();
			}
			return _guiDao;
		}
		
		private function _createKaKou():Sprite {
			if (!_kaKou) {
				_kaKou = new Sprite();
				_kaKou.graphics.beginFill(0x00b050);
				_kaKou.graphics.drawRect(0, 0, KA_KOU_W, KA_KOU_H);
				_kaKou.graphics.endFill();
			}
			return _kaKou;
		}
		
		private function _createJiaGuiDao():Sprite {
			if (!_jiaGuiDao) {
				_jiaGuiDao = new Sprite();
				_jiaGuiDao.graphics.beginFill(0xff3600);
				_jiaGuiDao.graphics.drawRect(0, 0, 100, 20);
				_jiaGuiDao.graphics.endFill();
			}
			return _jiaGuiDao;
		}
	}

}