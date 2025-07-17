package com.syamgot.as3.quadtree 
{

	/**
	 * 線形4分木管理クラス
	 * 
	 * 四分木空間分割による衝突判定対象となる表示オブジェクトの検索
	 * 
	 * 
	 * @see http://marupeke296.com/COL_2D_No9_QuadTree_Imp.html
	 * @author syamgot
	 * 
	 */
	public class Liner4TreeManager 
	{
		
		/**
		 * 
		 * @param depth
		 * 
		 */
		public function Liner4TreeManager(depth:int):void
		{
		}
		
		/**
		 * 初期化
		 * 
		 * @param level
		 * @param left
		 * @param top
		 * @param right
		 * @param bottom
		 * @return 
		 * 
		 */
		public function initialize(level:uint, left:Number, top:Number, right:Number, bottom:Number):Boolean
		{
			
			// 
			_numCellByLevels = new Array(level + 1);
			
			// 各レベルでの空間数を算出
			_numCellByLevels[0] = 1;
			for (var i:uint = 1; i <= level+1; i++) {
				_numCellByLevels[i] = _numCellByLevels[i - 1] * 4;
			}
			
			// 指定レベルの配列作成
			_numCell = (_numCellByLevels[level+1] - 1) / 3;	// 等比級数の和
			_cells = new Array(_numCell);
			for (var i:uint = 0; i < _cells.length; i++) {
				_cells[i] = null;
			}
			
			// 有効領域の設定
			_left 		= left;
			_top 		= top;
			_width 		= right - left;
			_height 	= bottom - top;
			_unitWidth 	= _width / (1 << level);
			_unitHeight = _height / (1 << level);

			// 最深空間レベルの保持
			_level = level;

			return true;
		}
		
		/**
		 * OFTを空間に登録する
		 * 
		 * オブジェクトの境界範囲からモートン番号を算出し、空間に登録する。
		 * 空間がない場合は、作成する。
		 * 
		 * @param left
		 * @param top
		 * @param right
		 * @param bottom
		 * @param oft
		 * @return 
		 * 
		 */
		public function regist(left:Number, top:Number, right:Number, bottom:Number, oft:Object4Tree):Boolean
		{
			// 
			var element:uint = getMortonNumber(left, top, right, bottom);
			
			// 
			if (element < _numCell){
				if (_cells[element] == null) {
					this.createCell(element);
				}
				var cell:Cell = _cells[element];
				return cell.push(oft);
			}
			return false;
		}
		
		/**
		 * 空間を作成する
		 * 
		 * 引数のモートン番号の空間と、その親もsン剤しなければ作成する
		 * 
		 * @param element
		 * 
		 */
		public function createCell(element:uint):void
		{
			while (_cells[element] == null) {

				// 
				_cells[element] = new Cell();
				
				// ルート空間を作成の場合は親がいないので終了
				if (element == 0) {
					break;
				}
				
				// 親のモートン番号へ移動
				element = (element - 1) >> 2;
				if (element >= _numCell) {
					break;
				}
			}
		}
		
		/**
		 * モートン番号を取得する.
		 * 
		 * @param left
		 * @param top
		 * @param right
		 * @param bottom
		 * @see http://marupeke296.com/COL_2D_No8_QuadTree.html
		 * @return 
		 * 
		 */
		public function getMortonNumber(left:Number, top:Number, right:Number, bottom:Number):uint
		{
			// 最深レベルにおける各軸位置を算出
			var lt:uint = this.GetPointToElementNumber(left, top);
			var rb:uint = this.GetPointToElementNumber(right, bottom );
			
			// 空間番号の排他的論理和から所属レベルを算出(何ビットシフトするか)
			var def:uint = rb ^ lt;
			var hiLevel:uint = 0;
			for(var i:uint = 0; i < _level; i++) {
				var check:uint = (def >> (i * 2)) & 0x3;
				if(check != 0) {
					hiLevel = i + 1;
				}
			}
			
			// 最深レベルにおけるモートン番号(右下座標のモートン番号に直前で算出したシフト実行)
			var space_num:uint = rb >> (hiLevel * 2);
			
			// 上位レベルのモートン番号合計値
			var add_num:uint = (_numCellByLevels[_level - hiLevel] - 1) / 3;
			
			// 線形配列番号のためにルートからの通算モートン番号に変換
			space_num += add_num;
			
			// 
			if(space_num > _numCell) {
				return 0xffffffff;
			}
			
			return space_num;			
		}
		
		/**
		 * 更新処理
		 * 
		 * 衝突判定対象のオブジェクトのリストを更新する
		 * 
		 * @param list
		 * 
		 */
		public function update():void
		{
			// 
			if (_cells[0] == null) {
				return;
			}
			
			// 
			_collistionObjects = new Array();
			var stack:Array = new Array();
			this._getCollisionList(0, _collistionObjects, stack);
			stack = null;

		}

		
		/**
		 * 衝突判定対象のオブジェクトのリストを作成する
		 * 
		 * @param element
		 * @param list
		 * @param stack
		 * 
		 */
		private function _getCollisionList(element:uint, list:Array, stack:Array):void
		{
			// 空間内でオブジェクト同士の衝突リストを作成
			var i:uint;
			var cell:Cell = _cells[element];
			var oft1:Object4Tree = cell.latestOft;
			while (oft1 != null) {
				var oft2:Object4Tree = oft1.next;
				while (oft2 != null) {
					// 衝突リストを作成
					list.push(oft1.display);
					list.push(oft2.display);
					oft2 = oft2.next;
				}
				
				// 衝突スタックとの衝突リスト作成
				for (i = 0; i < stack.length; i++) {
					list.push(oft1.display);
					list.push(stack[i]);
				}
				
				// 次のオブジェクト
				oft1 = oft1.next;
			}
			
			// 子空間へ移動
			var is_child:Boolean = false;
			var obj_num:int = 0;
			var next_element:int = 0;
			for (i = 0; i < 4; i++) {
				next_element = element * 4 + 1 + i;
				if (next_element < _numCell && _cells[next_element]) {
					if (!is_child) {
						// 登録オブジェクトをスタックに追加
						oft1 = cell.latestOft;
						while (oft1 != null) {
							stack.push(oft1.display);
							obj_num++;
							oft1 = oft1.next;
						}
					}
					is_child = true;
					this._getCollisionList(next_element, list, stack);
				}
			}
			
			// スタックからオブジェクトを外す
			if (is_child) {
				for (i = 0; i < obj_num; i++) {
					stack.pop();
				}
			}
		}
		
		/**
		 * ビット分割
		 * 
		 * @param n
		 * @return 
		 * 
		 */
		public function bitSeparate32(n:int):int
		{
			n = (n|(n<<8)) & 0x00ff00ff;
			n = (n|(n<<4)) & 0x0f0f0f0f;
			n = (n|(n<<2)) & 0x33333333;
			return (n|(n<<1)) & 0x55555555;
		}
		
		/**
		 * モートン空間番号取得
		 * 
		 * @param x
		 * @param y
		 * @return 
		 * 
		 */
		public function get2DMortonNumber(x:uint, y:uint):uint
		{
			return (bitSeparate32(x) | (bitSeparate32(y)<<1));
		}
		
		/**
		 * 座標から線形4分木要素番号変換
		 * 
		 * @param x
		 * @param y
		 * @return 
		 * 
		 */
		public function GetPointToElementNumber(x:Number, y:Number):uint
		{
			return get2DMortonNumber((uint)((x - _left) / _unitWidth), (uint)((y - _top) / _unitHeight));
		}

		/**
		 * @inheritDoc
		 */
		public function toString():void
		{
			
		}
		
		private var _collistionObjects:Array;

		/**
		 * 衝突判定対象のオブジェクトの配列
		 */
		public function get collistionObjects():Array
		{
			return _collistionObjects;
		}
		
		// 設定されたレベルの空間数
		public var _numCell:uint;
		
		// 
		// 有効領域
		// 
		private var _left:Number;
		private var _top:Number;
		private var _width:Number;
		private var _height:Number;
	
		// 
		// 空間単位の幅・高さ
		// 
		private var _unitWidth:Number;
		private var _unitHeight:Number;
		
		// 空間配列
		private var _cells:Array;

		// 空間レベル
		private var _level:uint;
		
		// レベル毎の空間数
		private var _numCellByLevels:Array;
		
	}
}