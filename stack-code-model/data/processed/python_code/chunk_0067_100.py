package com.syamgot.as3.quadtree 
{
	
	/**
	 * 空間(Cell)クラス
	 * 
	 * 
	 * OFTをスタックするリストを持つ。
	 * Cellは最初に追加されたOFTを知っている。
	 * 
	 * OFTは自身が含まれたリストを持つCellから、自主的に
	 * 逸脱することが出来るが、OFTは逸脱することを
	 * Cellに伝える必要があり、Cellはその際に実行する関数を持つ。
	 * 
	 * @author syamgot
	 * 
	 */
	public class Cell 
	{
		
		/**
		 * 
		 * 
		 */
		public function Cell():void
		{
			_latestOft = null;
		}
		
		/**
		 * OFTインスタンスを追加する
		 * 
		 * @param oft
		 * @return 
		 * 
		 */
		public function push(oft:Object4Tree):Boolean 
		{
			// 無効なオブジェクトは登録しない
			// 二重登録チェック
			if (oft == null || oft.cell == this) {
				return false;
			}
			
			// 新規/更新処理
			if (_latestOft == null) {
				_latestOft = oft;
			}
			else {
				oft.next = _latestOft;
				_latestOft.prev = oft;
				_latestOft = oft;
			}
			
			// 
			oft.cell = this;
			
			return true;
		}
		
		/**
		 * 
		 * OFTから抜ける通知を受け取る.
		 * 
		 * OFTは自主的に所属する空間から抜けることが
		 * 出来る。空間は、抜けるOTFが最新のものであ
		 * れば、その次のOFTを最新のものとして登録する。
		 * 
		 * @param oft
		 * @return 
		 * 
		 */
		public function onRemove(oft:Object4Tree):Boolean 
		{
			if (_latestOft == oft && _latestOft != null) {
				_latestOft = _latestOft.next;
			}
			return true;
		}
		
		private var _latestOft:Object4Tree;

		/**
		 * 最後に追加されたOFT
		 * 
		 */
		public function get latestOft():Object4Tree
		{
			return _latestOft;
		}


	}
}