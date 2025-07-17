package com.syamgot.as3.quadtree 
{
	import flash.display.DisplayObject;

	/**
	 * ObjectForTree クラス.
	 * 
	 * 4分木に登録するObject4Treeクラスは、表示オブジェクト、登録されている空間への
	 * 参照、自分の前後のObject4Treeインスタンスへの参照を持つ.
	 * 
	 * OFTは自主的に空間から抜ける事ができる.この際、所属する空間に自らが抜けることを通知する.
	 * 
	 * @author syamgot
	 * 
	 */
	public class Object4Tree 
	{
		
		/**
		 * 新しい Object4Tree インスタンスを生成します.
		 * 
		 * @param circle
		 * 
		 */
		public function Object4Tree(display:DisplayObject):void 
		{
			_display 	= display;
			_cell 		= null;
			_prev 		= null;
			_next 		= null;
		}
		
		/**
		 * 空間から削除する
		 * 
		 * @return 
		 * 
		 */
		public function remove():Boolean
		{

			// 
			if (cell == null) {
				return false;
			}

			// 
			cell.onRemove(this);
			
			// 
			if (prev != null) {
				prev.next = next;
			}
			if (next != null) {
				next.prev = prev;
			}
			
			// 
			prev = null;
			next = null;
			cell = null;
			
			return true;
		}
		
		private var _cell:Cell;

		/**
		 * 登録空間
		 * 
		 */
		public function get cell():Cell
		{
			return _cell;
		}

		/**
		 * @private
		 */
		public function set cell(value:Cell):void
		{
			_cell = value;
		}

		
		private var _display:DisplayObject;

		/**
		 * 表示オブジェクト
		 * 
		 */
		public function get display():DisplayObject
		{
			return _display;
		}

		/**
		 * @private
		 */
		public function set display(value:DisplayObject):void
		{
			_display = value;
		}

		
		private var _prev:Object4Tree;

		/**
		 * 前のObject4Treeインスタンス
		 * 
		 */
		public function get prev():Object4Tree
		{
			return _prev;
		}

		/**
		 * @private
		 */
		public function set prev(value:Object4Tree):void
		{
			_prev = value;
		}

		
		private var _next:Object4Tree;

		/**
		 * 次のObject4Treeインスタンス
		 * 
		 */
		public function get next():Object4Tree
		{
			return _next;
		}

		/**
		 * @private
		 */
		public function set next(value:Object4Tree):void
		{
			_next = value;
		}

		
	}
}