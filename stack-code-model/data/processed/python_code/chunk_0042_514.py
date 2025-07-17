package view {
	import config.ConfigUtil;
	import events.LayoutEvent;
	import flash.display.Graphics;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	import flash.external.ExternalInterface;
	import flash.geom.Point;
	import flash.system.System;
	import flash.text.TextField;
	import flash.ui.Keyboard;
	import model.Cell;
	import model.GuiDao;
	import model.KaKou;
	import model.XianCao;
	import model.YuanJian;
	import model.YuanJianManager;
	
	/**
	 * ...
	 * @author hongjie
	 */
	public final class BuJuQu extends Sprite {
		
		public static var containerScale:Number = 1;
		
		public var selectedYuanJianArr:Vector.<YuanJian> = new Vector.<YuanJian>();
		
		private var _selectedCell:Cell;
		
		private var _guiDaoContainer:Sprite;
		
		private var _xianCaoContainer:Sprite;
		
		private var _container:Sprite;
		
		private var _w:int;
		
		private var _h:int;
		
		private var _viewWidth:int;
		
		private var _viewHeight:int;
		
		private var _isDraging:Boolean;
		
		private var _dragingLastX:int;
		
		private var _dragingLastY:int;
		
		private var _numXianCao:int;
		
		private var _numGuiDao:int;
		
		private var _minScale:Number;
		
		private var _keyPool:KeyPoll;
		
		private var _copyedCell:Cell;
		
		private var _startCheckMoved:Boolean;
		
		public function BuJuQu(width:int, height:int) {
			super();
			_w = width;
			_h = height;
			
			_viewWidth = width;
			_viewHeight = height;
			
			const g:Graphics = this.graphics;
			g.lineStyle(1, 0xff0000);
			g.moveTo(0, 0);
			g.lineTo(width - 1, 0);
			g.lineTo(width - 1, height);
			g.lineTo(0, height);
			g.lineTo(0, 0);
			
			g.beginFill(0xff0000, 0);
			g.drawRect(0, 0, width, height);
			g.endFill();
			
			_container = new Sprite();
			const mask:Shape = new Shape();
			mask.graphics.beginFill(0, 0);
			mask.graphics.drawRect(0, 0, _w, _h);
			mask.graphics.endFill();
			addChild(mask);
			_container.mask = mask;
			addChild(_container);
			
			_xianCaoContainer = new Sprite();
			_container.addChild(_xianCaoContainer);
			_guiDaoContainer = new Sprite();
			_container.addChild(_guiDaoContainer);
			
			ConfigUtil.instance.addEventListener(LayoutEvent.IMPORT_XML_OK, _onReset);
			
			this.addEventListener(MouseEvent.MOUSE_WHEEL, _onMouseWheel);
			
			this.addEventListener(MouseEvent.MOUSE_MOVE, _onMouseMoved);
			this.addEventListener(MouseEvent.MOUSE_UP, _onMouseUp);
			this.addEventListener(MouseEvent.MOUSE_DOWN, _onMouseDown);
			this.addEventListener(MouseEvent.CLICK, _onBuJuClicked);
			
			ScaleLine.instance.addEventListener(LayoutEvent.COPY, _onCopy);
			ScaleLine.instance.addEventListener(LayoutEvent.DELETE, _onDelete);
			
			if (ExternalInterface.available) {
				ExternalInterface.addCallback('autoScale', this.autoScale);
			}
		}
		
		public function addGuiDao(isJiaDe:Boolean, w:int = 50, h:int = 40, x:int = 0, y:int = 0, name:String = null, type:String = '', isDrag:Boolean = false, isCopy:Boolean = false, isInit:Boolean = false):void {
			if (!isCopy) {
				if (isDrag) {
					x = (x - _container.x) / _container.scaleX;
					y = (y - _container.y) / _container.scaleY;
				} else {
					x = x / _container.scaleX;
					y = y / _container.scaleY;
				}
				if (!isInit) {
					// 找到左右最近的线槽，自动调整
					const p:Point = _xianCaoContainer.globalToLocal(new Point(mouseX, mouseY));
					const leftXianCao:XianCao = findNearestXianCao(p.x, p.y, Enum.LEFT);
					const rightXianCao:XianCao = findNearestXianCao(p.x, p.y, Enum.RIGHT);
					x = leftXianCao.x + leftXianCao.reallyWidth;
					w = rightXianCao.x - x;
				}
			}
			var guiDao:GuiDao = new GuiDao(w, h, Enum.H, isJiaDe);
			guiDao.x = x;
			guiDao.y = y;
			guiDao.typeStr = type;
			if (name) {
				guiDao.name = name;
				_numGuiDao = int(name);
			} else {
				guiDao.name = (++_numGuiDao).toString();
			}
			_guiDaoContainer.addChild(guiDao);
			guiDao.addEventListener(LayoutEvent.CLIECKED, _onCellClicked);
			guiDao.addEventListener(LayoutEvent.SHOW_YUAN_JIAN_SHU_XING, _onShowYuanJianShuXing);
			guiDao.addEventListener(LayoutEvent.DELETE, _onDeleteYuanJian);
			
			ScaleLine.instance.parentCell = guiDao;
			
			//_clearSelectedCell();
			//selectedCellArr.push(guiDao);
			if (_selectedCell) {
				_selectedCell.isSelected = false;
			}
			_selectedCell = guiDao;
			guiDao.isSelected = true;
			this.dispatchEvent(new LayoutEvent(LayoutEvent.ADD_GUI_DAO));
		}
		
		public function addXianCao(w:int = 200, h:int = 80, x:int = 0, y:int = 0, dir:int = 0, name:String = null, type:String = '', isDrag:Boolean = false, isCopy:Boolean = false, isInit:Boolean = false):void {
			if (!isCopy) {
				if (isDrag) {
					x = (x - _container.x) / _container.scaleX;
					y = (y - _container.y) / _container.scaleY;
				} else {
					x = x / _container.scaleX;
					y = y / _container.scaleY;
				}
				if (!isInit) {
					// 找到左右最近的线槽，自动调整
					const p:Point = _xianCaoContainer.globalToLocal(new Point(mouseX, mouseY));
					if (dir == Enum.H) {
						const leftXianCao:XianCao = findNearestXianCao(p.x, p.y, Enum.LEFT);
						const rightXianCao:XianCao = findNearestXianCao(p.x, p.y, Enum.RIGHT);
						if (leftXianCao && rightXianCao) {
							x = leftXianCao.x + leftXianCao.reallyWidth;
							w = rightXianCao.x - x;
						}
					} else {
						const topXianCao:XianCao = findNearestXianCao(p.x, p.y, Enum.TOP);
						const bottomXianCao:XianCao = findNearestXianCao(p.x, p.y, Enum.DOWN);
						if (topXianCao && bottomXianCao) {
							y = topXianCao.y + topXianCao.reallyHeight;
							h = bottomXianCao.y - y;
						}
					}
				}
			}
			
			var xianCao:XianCao = new XianCao(w, h, dir);
			xianCao.x = x;
			xianCao.y = y;
			xianCao.typeStr = type;
			xianCao.dir = dir;
			if (name) {
				xianCao.name = name;
				_numXianCao = int(name);
			} else {
				xianCao.name = (++_numXianCao).toString();
			}
			_xianCaoContainer.addChild(xianCao);
			xianCao.addEventListener(LayoutEvent.CLIECKED, _onCellClicked);
			
			ScaleLine.instance.parentCell = xianCao;
			
			//_clearSelectedCell();
			//selectedCellArr.push(xianCao);
			if (_selectedCell) {
				_selectedCell.isSelected = false;
			}
			_selectedCell = xianCao;
			xianCao.isSelected = true;
			this.dispatchEvent(new LayoutEvent(LayoutEvent.ADD_XIAN_CAO));
		}
		
		private function findNearestXianCao(x:int, y:int, dir:int):XianCao {
			var xianCao:XianCao = null;
			var result:XianCao = null;
			var min:int = int.MAX_VALUE;
			if (dir == Enum.TOP) {
				for (var i:int = 0; i < _xianCaoContainer.numChildren; i++) {
					xianCao = _xianCaoContainer.getChildAt(i) as XianCao;
					if (xianCao.dir == Enum.H && xianCao.y + xianCao.reallyHeight < y) {
						if (xianCao.x < x && xianCao.x + xianCao.reallyWidth > x) {
							if (min > y - (xianCao.y + xianCao.reallyHeight)) {
								min = y - (xianCao.y + xianCao.reallyHeight);
								result = xianCao;
							}
						}
					}
				}
			} else if (dir == Enum.RIGHT) {
				for (i = 0; i < _xianCaoContainer.numChildren; i++) {
					xianCao = _xianCaoContainer.getChildAt(i) as XianCao;
					if (xianCao.dir == Enum.V && xianCao.x > x) {
						if (xianCao.y < y && xianCao.y + xianCao.reallyHeight > y) {
							if (min > xianCao.x - x) {
								min = xianCao.x - x;
								result = xianCao;
							}
						}
					}
				}
			} else if (dir == Enum.DOWN) {
				for (i = 0; i < _xianCaoContainer.numChildren; i++) {
					xianCao = _xianCaoContainer.getChildAt(i) as XianCao;
					if (xianCao.dir == Enum.H && xianCao.y > y) {
						if (xianCao.x < x && xianCao.x + xianCao.reallyWidth > x) {
							if (min > xianCao.y - y) {
								min = xianCao.y - y;
								result = xianCao;
							}
						}
					}
				}
			} else if (dir == Enum.LEFT) {
				for (i = 0; i < _xianCaoContainer.numChildren; i++) {
					xianCao = _xianCaoContainer.getChildAt(i) as XianCao;
					if (xianCao.dir == Enum.V && xianCao.x + xianCao.reallyWidth < x) {
						if (xianCao.y < y && xianCao.y + xianCao.reallyHeight > y) {
							if (min > x - (xianCao.x + xianCao.reallyWidth)) {
								min = x - (xianCao.x + xianCao.reallyWidth);
								result = xianCao;
							}
						}
					}
				}
			}
			return result;
		}
		
		public function exportXianCao():String {
			var s:String = '';
			var xianCao:XianCao;
			for (var i:int = 0; i < _xianCaoContainer.numChildren; i++) {
				xianCao = _xianCaoContainer.getChildAt(i) as XianCao;
				s += (s == '' ? '\t\t' : '\n\t\t') + xianCao.toXML();
			}
			return s;
		}
		
		public function exportGuiDao():String {
			var s:String = '';
			var guidao:GuiDao;
			for (var i:int = 0; i < _guiDaoContainer.numChildren; i++) {
				guidao = _guiDaoContainer.getChildAt(i) as GuiDao;
				s += '\n\t\t' + guidao.toXML();
			}
			return s;
		}
		
		public function exportYuanJian():String {
			var s:String = '';
			var guidao:GuiDao;
			for (var i:int = 0; i < _guiDaoContainer.numChildren; i++) {
				guidao = _guiDaoContainer.getChildAt(i) as GuiDao;
				s += guidao.yuanJianToXML();
			}
			return s;
		}
		
		public function initLayout(xml:XML, layoutXML:XML):void {
			var guiDao:GuiDao, yuanJian:YuanJian;
			if (layoutXML) {
				for each (var item:* in layoutXML.items.item) {
					for (var i:int = 0; i < _guiDaoContainer.numChildren; i++) {
						guiDao = _guiDaoContainer.getChildAt(i) as GuiDao;
						if (guiDao.name == item.@pathway) {
							if (item.@name == 'kaKou') {
								yuanJian = new KaKou(item.@w, item.@h, item.@type);
							} else {
								yuanJian = YuanJianManager.instance.getYuanJian(item.@name, item.@code);
								yuanJian.offsetY = item.@offsetY;
							}
							
							guiDao.initYuanJian(yuanJian, item.@x, item.@y);
							if (item.@topItem != undefined) {
								yuanJian.topYuanJian = YuanJianManager.instance.getYuanJian(item.@topItem, item.@topItemCode);
							}
							if (item.@bottomItem != undefined) {
								yuanJian.bottomYuanJian = YuanJianManager.instance.getYuanJian(item.@bottomItem, item.@bottomItemCode);
							}
							break;
						}
					}
				}
			}
		}
		
		//public function removeUnusefulYuanJian(name:String):void {
		//
		//}
		
		private function _onDeleteYuanJian(e:LayoutEvent):void {
			if (e.yuanJian == ScaleLine.instance.parentCell) {
				ScaleLine.instance.parentCell = null;
				_selectedCell = null;
			}
			dispatchEvent(new LayoutEvent(LayoutEvent.RESET_YUAN_JIAN, null, e.yuanJian));
		}
		
		private function _onDelete(evt:LayoutEvent = null):void {
			if (_selectedCell) {
				if (_selectedCell is GuiDao) {
					const guiDao:GuiDao = _selectedCell as GuiDao;
					_guiDaoContainer.removeChild(guiDao);
					guiDao.removeEventListener(LayoutEvent.CLIECKED, _onCellClicked);
					guiDao.removeEventListener(LayoutEvent.SHOW_YUAN_JIAN_SHU_XING, _onShowYuanJianShuXing);
					guiDao.removeEventListener(LayoutEvent.DELETE, _onDeleteYuanJian);
					
					const yuanJianArr:Vector.<YuanJian> = guiDao.removeAllYuanJian();
					for (var i:int = 0; i < yuanJianArr.length; i++) {
						guiDao.removeYuanJian(yuanJianArr[i]);
						dispatchEvent(new LayoutEvent(LayoutEvent.RESET_YUAN_JIAN, null, yuanJianArr[i]));
					}
				} else if (_selectedCell is XianCao) {
					_xianCaoContainer.removeChild(_selectedCell);
					_selectedCell.removeEventListener(LayoutEvent.CLIECKED, _onCellClicked);
				} else if (_selectedCell is YuanJian) {
					deleteYuanJian(_selectedCell as YuanJian);
						//(_selectedCell.parent as GuiDao).removeYuanJian(_selectedCell as YuanJian);
						//dispatchEvent(new LayoutEvent(LayoutEvent.RESET_YUAN_JIAN, null, _selectedCell as YuanJian));
				}
				ScaleLine.instance.parentCell = null;
				_selectedCell = null;
			}
		}
		
		public function deleteYuanJian(yuanJian:YuanJian):void {
			if (yuanJian.parent is GuiDao) {
				(yuanJian.parent as GuiDao).removeYuanJian(yuanJian);
				dispatchEvent(new LayoutEvent(LayoutEvent.RESET_YUAN_JIAN, null, yuanJian));
				if (ScaleLine.instance.parentCell == yuanJian) {
					ScaleLine.instance.parentCell = null;
					_selectedCell = null;
				}
			}
		}
		
		private function _onCopy(e:LayoutEvent = null):void {
			var cell:Cell = e ? _selectedCell : _copyedCell;
			if (cell) {
				const offset:Number = 10;
				if (cell is GuiDao) {
					addGuiDao(false, cell.reallyWidth, cell.reallyHeight, cell.x + offset, cell.y + offset, null, '', false, true);
				} else if (cell is XianCao) {
					addXianCao(cell.reallyWidth, cell.reallyHeight, cell.x + offset, cell.y + offset, (cell as XianCao).dir, null, '', false, true);
				}
			}
			if (!e) {
				new Alert("粘贴成功!").show(this.stage);
			}
		}
		
		private function _onReset(evt:LayoutEvent):void {
			_container.scaleX = 1;
			_container.scaleY = 1;
			containerScale = 1;
			for (var i:int = 0; i < _xianCaoContainer.numChildren; i++) {
				_xianCaoContainer.getChildAt(i).removeEventListener(LayoutEvent.CLIECKED, _onCellClicked);
			}
			this._xianCaoContainer.removeChildren();
			for (i = 0; i < _guiDaoContainer.numChildren; i++) {
				_guiDaoContainer.getChildAt(i).removeEventListener(LayoutEvent.CLIECKED, _onCellClicked);
				_guiDaoContainer.getChildAt(i).removeEventListener(LayoutEvent.SHOW_YUAN_JIAN_SHU_XING, _onShowYuanJianShuXing);
				_guiDaoContainer.getChildAt(i).removeEventListener(LayoutEvent.DELETE, _onDeleteYuanJian);
			}
			_guiDaoContainer.removeChildren();
			
			var a:Array = evt.xml.layout.@size.split(',');
			_w = int(a[0]);
			_h = int(a[1]);
			const g:Graphics = _container.graphics;
			g.clear();
			g.beginFill(0x00f215, .6);
			g.drawRect(0, 0, _w, _h);
			g.endFill();
			
			const layoutXML:XML = evt.layoutXML;
			if (layoutXML) {
				for each (var item:* in layoutXML.layout.trunking) {
					this.addXianCao(item.@w, item.@h, item.@x, item.@y, item.@dir, item.@name, item.@type, false, false, true);
				}
				for each (item in layoutXML.layout.pathway) {
					this.addGuiDao(item.@virtual == 'true', item.@w, item.@h, item.@x, item.@y, item.@name, item.@type, false, false, true);
				}
			} else {
				this.addXianCao(_w, 20, 0, 0, Enum.H, null, '', false, false, true);
				this.addXianCao(20, _h, _w - 20, 0, Enum.V, null, '', false, false, true);
				this.addXianCao(_w, 20, 0, _h - 20, Enum.H, null, '', false, false, true);
				this.addXianCao(20, _h, 0, 0, Enum.V, null, '', false, false, true);
			}
			
			var scale:Number = _viewWidth / _w;
			var h:Number = _h * scale;
			if (h > _viewHeight) {
				scale = _viewHeight / _h;
			}
			_container.scaleX = scale;
			_container.scaleY = scale;
			containerScale = scale;
			
			//if (_h < _w) {
			//this._minScale = _viewHeight / _h;
			//} else {
			//this._minScale = _viewWidth / _w;
			//}
			this._minScale = scale;
			
			if (!this._keyPool) {
				this._keyPool = new KeyPoll(Main.mainScene.stage);
				this._keyPool.addEventListener(KeyboardEvent.KEY_UP, _onKeyUp);
			}
		}
		
		private function _onKeyUp(e:KeyboardEvent):void {
			if (this.stage.focus && this.stage.focus is TextField) {
				return;
			}
			
			if (e.keyCode == Keyboard.DELETE) {
				this._onDelete();
			} else if (e.keyCode == Keyboard.C) {
				if (this._selectedCell) {
					if (_selectedCell is XianCao || _selectedCell is GuiDao) {
						_copyedCell = _selectedCell;
						new Alert("复制成功!").show(this.stage);
					}
				}
			} else if (e.keyCode == Keyboard.V) {
				_onCopy();
			} else if (e.keyCode == Keyboard.W || e.keyCode == Keyboard.UP) {
				ScaleLine.instance.moveUp();
			} else if (e.keyCode == Keyboard.D || e.keyCode == Keyboard.RIGHT) {
				ScaleLine.instance.moveRight();
			} else if (e.keyCode == Keyboard.S || e.keyCode == Keyboard.DOWN) {
				ScaleLine.instance.moveDown();
			} else if (e.keyCode == Keyboard.A || e.keyCode == Keyboard.LEFT) {
				ScaleLine.instance.moveLeft();
			}
		}
		
		private function _onShowYuanJianShuXing(e:LayoutEvent):void {
			cellClicked(e.yuanJian, e.isCtrlKey);
		}
		
		private function _onCellClicked(e:LayoutEvent):void {
			const cell:Cell = e.currentTarget as Cell;
			//if (e.localX < cell.reallyWidth && e.localY < cell.reallyHeight){
			cellClicked(cell);
			e.stopImmediatePropagation();
			//}
		}
		
		private function cellClicked(cell:Cell, isCtrlKey:Boolean = false):void {
			if (cell is YuanJian && isCtrlKey) {
				ScaleLine.instance.parentCell = null;
				if (_selectedCell) {
					_selectedCell.isSelected = false;
					_selectedCell = null;
				}
				
				yuanJian = cell as YuanJian;
				var has:Boolean = false;
				for (i = 0; i < selectedYuanJianArr.length; i++) {
					if (selectedYuanJianArr[i] == yuanJian) {
						selectedYuanJianArr.splice(i, 1);
						yuanJian.isSelected = false;
						has = true;
						break;
					}
				}
				if (!has) {
					yuanJian.isSelected = true;
					selectedYuanJianArr.push(yuanJian);
				}
				return;
			} else {
				for (i = 0; i < selectedYuanJianArr.length; i++) {
					selectedYuanJianArr[i].isSelected = false;
				}
				selectedYuanJianArr.length = 0;
			}
			
			if (_selectedCell) {
				if (_selectedCell == cell) return;
				_selectedCell.isSelected = false;
			}
			_selectedCell = cell;
			_selectedCell.isSelected = true;
			ScaleLine.instance.parentCell = _selectedCell;
			
			// 如果是元件，还要找到距离最近的水平线槽的边距
			if (_selectedCell is YuanJian) {
				var yuanJian:YuanJian = _selectedCell as YuanJian;
				//trace(_container.globalToLocal(yuanJian.guiDao.localToGlobal(new Point(yuanJian.x, yuanJian.y))));
				var yuanJianGlobalY:int = _container.globalToLocal(yuanJian.guiDao.localToGlobal(new Point(yuanJian.x, yuanJian.y))).y;
				var marginTop:int = int.MAX_VALUE;
				var marginBottom:int = int.MAX_VALUE;
				var topXianCao:XianCao;
				var bottomXianCao:XianCao;
				var xianCao:XianCao;
				for (var i:int = 0; i < this._xianCaoContainer.numChildren; i++) {
					xianCao = _xianCaoContainer.getChildAt(i) as XianCao;
					if (xianCao.dir == Enum.H) {
						if (xianCao.y > yuanJianGlobalY) {
							if (xianCao.y - yuanJianGlobalY < marginBottom) {
								marginBottom = xianCao.y - yuanJianGlobalY;
								bottomXianCao = xianCao;
							}
						} else {
							if (yuanJianGlobalY - xianCao.y < marginTop) {
								marginTop = yuanJianGlobalY - xianCao.y;
								topXianCao = xianCao;
							}
						}
					}
				}
				yuanJian.marginTopToXianCao = yuanJianGlobalY - (topXianCao.y + topXianCao.reallyHeight);
				yuanJian.marginBottomToXianCao = bottomXianCao.y - (yuanJianGlobalY + yuanJian.reallyHeight);
			}
			
			this.dispatchEvent(new LayoutEvent(LayoutEvent.SELECTED_ARR_CHANGED));
		}
		
		//private function _clearSelectedCell():void {
		//for (var i:int = 0; i < this.selectedCellArr.length; i++) {
		//this.selectedCellArr[i].isSelected = false;
		//}
		//this.selectedCellArr.length = 0;
		//}
		
		private function _onMouseWheel(evt:MouseEvent):void {
			const lastScale:Number = _container.scaleX;
			if (evt.delta < 0) {
				//向下滚动
				if (_container.scaleX > _minScale) {
					_container.scaleX -= .05;
					_container.scaleY -= .05;
					containerScale = _container.scaleX;
				} else {
					_container.scaleX = _minScale;
					_container.scaleY = _minScale;
					containerScale = _container.scaleX;
				}
			} else {
				if (_container.scaleX < 2) {
					_container.scaleX += .05;
					_container.scaleY += .05;
					if (_container.scaleX > 2) {
						_container.scaleX = 2;
					}
					if (_container.scaleY > 2) {
						_container.scaleY = 2;
					}
					containerScale = _container.scaleX;
				}
			}
			
			const p:Point = _container.globalToLocal(new Point(mouseX, mouseY));
			_container.x += (p.x - 0) * (lastScale - _container.scaleX);
			_container.y += (p.y - 0) * (lastScale - _container.scaleX);
			//if (_container.scaleX == 1 && _container.scaleY == 1) {
			//// do nothing
			//} else {
			//_container.x = p.x * (1 - _container.scaleX);
			//_container.y = p.y * (1 - _container.scaleY);
			//}
		
			//_container.x = _viewWidth / 2 * (1 - _container.scaleX);
			//_container.y = _viewHeight / 2 * (1 - _container.scaleY);
		
			//map_mc.x=mouseX-e.localX*(map_mc.scaleX);
			//map_mc.y=mouseY-e.localY*(map_mc.scaleY);
		}
		
		private function _onMouseUp(evt:MouseEvent):void {
			if (ScaleLine.instance.mouseUped()) {
				evt.stopImmediatePropagation();
			}
			this._isDraging = false;
		}
		
		private function _onMouseDown(e:MouseEvent):void {
			//if (e.target is Cell){
			////const cell:Cell = e.target as Cell;
			////if (e.localX < cell.reallyWidth && e.localY < cell.reallyHeight){
			////return;
			////}
			//}
			_startCheckMoved = true;
			
			const arr:Array = getObjectsUnderPoint(new Point(e.stageX, e.stageY));
			for (var i:int = arr.length - 1; i > -1; i--) {
				if (arr[i] is ScaleRect) {
					ScaleLine.instance.mouseDown(arr[i] as ScaleRect, e.stageX, e.stageY);
					return;
				} else if (arr[i] is Cell) {
					return;
				}
			}
			
			this._isDraging = true;
			_dragingLastX = e.stageX;
			_dragingLastY = e.stageY;
		}
		
		private function _onMouseMoved(evt:MouseEvent):void {
			if (evt.buttonDown) {
				var isOnContainer:Boolean = false;
				var arr:Array = this.getObjectsUnderPoint(new Point(evt.stageX, evt.stageY));
				for (var i:int = 0; i < arr.length; i++) {
					if (arr[i] == _container) {
						isOnContainer = true;
						break;
					}
				}
				if (isOnContainer && !ScaleLine.instance.mouseMoved(evt.stageX, evt.stageY)) {
					if (_isDraging) {
						//_container.x += evt.stageX - _dragingLastX;
						//_container.y += evt.stageY - _dragingLastY;
						//_dragingLastX = evt.stageX;
						//_dragingLastY = evt.stageY;
						_container.x += mouseX - _dragingLastX;
						_container.y += mouseY - _dragingLastY;
						_dragingLastX = mouseX;
						_dragingLastY = mouseY;
					}
				}
				
				if (_startCheckMoved) {
					if (selectedYuanJianArr.length > 0) {
						dispatchEvent(new LayoutEvent(LayoutEvent.START_TO_DTAG_YUAN_JIAN, null, null, false, null, null, selectedYuanJianArr.slice()));
						selectedYuanJianArr.length = 0;
						_startCheckMoved = false;
					}
				}
			}
		}
		
		private function _onBuJuClicked(e:MouseEvent):void {
			const arr:Array = getObjectsUnderPoint(new Point(e.stageX, e.stageY));
			var cell:Cell = null;
			for (var i:int = arr.length - 1; i > -1; i--) {
				if (arr[i] is Cell) {
					cell = arr[i] as Cell;
					break;
				}
			}
			if (cell) {
				cellClicked(cell);
			} else {
				ScaleLine.instance.parentCell = null;
				if (_selectedCell) {
					_selectedCell.isSelected = false;
					_selectedCell = null;
				}
			}
		}
		
		public function get selectedCell():Cell {
			return _selectedCell;
		}
		
		public function get w():int {
			return _w;
		}
		
		public function get h():int {
			return _h;
		}
		
		private function autoScale():void {
			const scale:Number = _h > _w ? _viewHeight / _h : _viewWidth / _w;
			this._container.scaleX = scale;
			this._container.scaleY = scale;
			containerScale = scale;
			_container.x = 0;
			_container.y = 0;
		}
	}

}