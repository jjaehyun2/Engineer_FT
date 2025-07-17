package org.avManager.model.data
{
	public class SQLData
	{
		
		protected var _id:int;
		
		protected var _name:String;
		
		protected var _needInsert:Boolean;
		
		protected var _needUpdate:Boolean;
		
		protected var _needDelete:Boolean;
		
		public function SQLData(id:int)
		{
			_id = id;
		}

		public function get id():int
		{
			return _id;
		}
		
		[SQLData(cloName="NAME")]
		public function get name():String
		{
			return _name;
		}
		
		[Bindable]
		public function set name(value:String):void
		{
			_name = value;
			this.needUpdate = true;
		}

		public function get needInsert():Boolean
		{
			return _needInsert;
		}

		public function set needInsert(value:Boolean):void
		{
			_needInsert = value;
		}

		public function get needUpdate():Boolean
		{
			return _needUpdate;
		}

		public function set needUpdate(value:Boolean):void
		{
			_needUpdate = value;
		}

		public function get needDelete():Boolean
		{
			return _needDelete;
		}

		public function set needDelete(value:Boolean):void
		{
			_needDelete = value;
		}


	}
}