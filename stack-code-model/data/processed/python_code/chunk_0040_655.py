package com.syamgot.as3.util
{
	/**
	 * Stack クラスは、先入後出(LIFO)機能を提供する Collection クラスの派生クラスです.
	 * 
	 * @author syamgot
	 */
	public class Stack extends Collection implements ICollection
	{
		
		/**
		 * 新しい Stack インスタンスを作成します.
		 */
		public function Stack()
		{
			super();	
		}
		
		/**
		 * スタックの先頭のオブジェクトを削除し、そのオブジェクトを関数の値として返します.
		 * @return 
		 */
		public function pop():Object
		{
			var obj:Object = super.getAt(0);
			super.removeAt(0);
			return obj;
		}
		
		/**
		 * スタックの先頭にあるオブジェクトを返します.
		 * @return 
		 */
		public function peek():Object
		{
			return super.getAt(0);
		}
		
		/**
		 *  スタックの最後にオブジェクトを追加します.
		 * @param item
		 */
		public function push(item:Object):Stack 
		{
			super.add(item);	
			return this;
		}
		
	}
}