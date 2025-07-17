package view {
	import events.LayoutEvent;
	import flash.display.Graphics;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.filters.GlowFilter;
	import flash.text.TextField;
	import flash.text.TextFieldType;
	import model.Cell;
	import model.GuiDao;
	import model.KaKou;
	import model.XianCao;
	import model.YuanJian;
	
	/**
	 * ...
	 * @author hongjie
	 */
	public final class ShuXingQu extends Sprite {
		
		private var _buJuQu:BuJuQu;
		
		private var _curCell:Cell;
		
		private var _shuxingXianCao:ShuXingXianCao;
		
		private var _shuXingGuiDao:ShuXingGuiDao;
		
		private var _shuXingYuanJian:ShuXingYuanJian;
		
		private var _shuXingKaKou:ShuXingKaKou;
		
		private var _curShuXing:ShuXing;
		
		public function ShuXingQu(width:int, height:int, buJuQu:BuJuQu) {
			super();
			
			const g:Graphics = this.graphics;
			g.beginFill(0, 0);
			g.drawRect(0, 0, width, height);
			g.endFill();
			
			_shuxingXianCao = new ShuXingXianCao(width, height);
			_shuXingGuiDao = new ShuXingGuiDao(width, height);
			_shuXingYuanJian = new ShuXingYuanJian(width, height);
			_shuXingKaKou = new ShuXingKaKou(width, height);
			
			this._buJuQu = buJuQu;
			_buJuQu.addEventListener(LayoutEvent.ADD_GUI_DAO, _onAddGuidao);
			_buJuQu.addEventListener(LayoutEvent.ADD_XIAN_CAO, _onAddXianCao);
			_buJuQu.addEventListener(LayoutEvent.SELECTED_ARR_CHANGED, _onSelectedArrChanged);
			
			ScaleLine.instance.addEventListener(LayoutEvent.UPDATE_CELL, _onUpdateCell)
		}
		
		private function _onSelectedArrChanged(e:LayoutEvent):void {
			setCurCell(_buJuQu.selectedCell);
		}
		
		private function _onAddXianCao(e:LayoutEvent):void {
			setCurCell(_buJuQu.selectedCell);
		}
		
		private function _onAddGuidao(e:LayoutEvent):void {
			setCurCell(_buJuQu.selectedCell);
		}
		
		private function setCurCell(cell:Cell):void {
			this._curCell = cell;
			if (cell) {
				if (cell is XianCao) {
					if (this._curShuXing != _shuxingXianCao) {
						if (this._curShuXing) {
							removeChild(_curShuXing);
						}
						this._curShuXing = _shuxingXianCao;
						addChild(_curShuXing);
					}
				} else if (cell is GuiDao) {
					if (this._curShuXing != _shuXingGuiDao) {
						if (this._curShuXing) {
							removeChild(_curShuXing);
						}
						this._curShuXing = _shuXingGuiDao;
						addChild(_curShuXing);
					}
				} else if (cell is KaKou){
					if (this._curShuXing != _shuXingKaKou) {
						if (this._curShuXing) {
							removeChild(_curShuXing);
						}
						this._curShuXing = _shuXingKaKou;
						addChild(_curShuXing);
					}
				} else if (cell is YuanJian) {
					if (this._curShuXing != _shuXingYuanJian) {
						if (this._curShuXing) {
							removeChild(_curShuXing);
						}
						this._curShuXing = _shuXingYuanJian;
						addChild(_curShuXing);
					}
				}
				_curShuXing.setCurCell(_curCell);
			} else {
				if (this._curShuXing) {
					removeChild(_curShuXing);
				}
				_curShuXing = null;
			}
		}
		
		private function _onUpdateCell(e:LayoutEvent):void {
			const cell:Cell = e.cell;
			if (cell) {
				if (_curCell == cell) {
					_curShuXing.setCurCell(_curCell);
				}
			} else {
				setCurCell(null);
			}
		}
	
	}

}