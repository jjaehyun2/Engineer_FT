package org.avManager.model.sql
{
	import flash.data.SQLConnection;
	import flash.data.SQLResult;
	import flash.data.SQLStatement;
	import flash.events.SQLErrorEvent;
	import flash.events.SQLEvent;
	import flash.utils.ByteArray;
	import flash.utils.describeType;
	
	import org.avManager.model.data.SQLData;
	import org.libra.log4a.Logger;
	import org.libra.utils.bytes.BitmapBytes;

	public class Table
	{
		protected var _tableName:String;
		
		protected var _createSql:String;
		
		protected var _sqlConnection:SQLConnection;
		
		protected var _createStmt:SQLStatement;
		
		protected var _insertStatement:SQLStatement;
		
		protected var _insertCallBack:Function;
		
		protected var _queryStatement:SQLStatement;
		
		protected var _queryCallBack:Function;
		
		protected var _updateStatement:SQLStatement;
		
		protected var _updateCallback:Function;
		
		protected var _deleteStatement:SQLStatement;
		
		protected var _deleteCallback:Function;
		
		public function Table(sqlConnection:SQLConnection)
		{
			_sqlConnection = sqlConnection;
			_insertStatement = new SQLStatement();
			_queryStatement = new SQLStatement();
			_deleteStatement = new SQLStatement();
			_updateStatement = new SQLStatement();
			this.init();
		}
		
		protected function init():void
		{
			_insertStatement.sqlConnection = _sqlConnection;
			_insertStatement.addEventListener(SQLEvent.RESULT, onInsertHandler);
			
			_queryStatement.sqlConnection = _sqlConnection;
			_queryStatement.text = "select * from " + _tableName + " where ID=:id";
			_queryStatement.addEventListener(SQLEvent.RESULT, onQueryHandler);
			
			_deleteStatement.sqlConnection = _sqlConnection;
			_deleteStatement.text = "delete from " + _tableName + " where ID=:id";
			_deleteStatement.addEventListener(SQLEvent.RESULT, onDeleteHandler);
			
			_updateStatement.sqlConnection = _sqlConnection;
			_updateStatement.text = "update " + _tableName + " set where ID=:id";
			_updateStatement.addEventListener(SQLEvent.RESULT, onUpdateHandler);
		}
		
		public function createTable():void{
			_createStmt = new SQLStatement(); 
			_createStmt.sqlConnection = _sqlConnection; 
			_createStmt.text = _createSql;
			_createStmt.addEventListener(SQLEvent.RESULT, onCreateResult); 
			_createStmt.addEventListener(SQLErrorEvent.ERROR, function onCreateError(event:SQLErrorEvent):void{
				Logger.error("创建table" +  _tableName + "失败:Error message:" + event.error.message + "Details:" + event.error.details);
				_createStmt.removeEventListener(SQLErrorEvent.ERROR, onCreateError);
			});
			_createStmt.execute();
		}
		
		public function insert(sqlData:SQLData, callback:Function = null):void{
			_insertCallBack = callback;
		}
		
		public function query(callback:Function, idList:Vector.<int> = null):void{
			this._queryCallBack = callback;
			if(idList){
				var idListStr:String = "(";
				for(var i:int = 0;i < idList.length;i++){
					idListStr += i == 0 ? idList[i] : "," + idList[i];
				}
				idListStr += ")";
				_queryStatement.text = "select * from " + _tableName + " where ID in " + idListStr;
			}else{
				_queryStatement.text = "select * from " + _tableName;
			}
			_queryStatement.execute(); 
		}
		
		public function update(sqlData:SQLData, callback:Function = null):void{
			this._updateCallback = callback;
			_updateStatement.text = "update " + _tableName + " set ";
			
			var keyValStr:String = "";
			var xml:XML = describeType(sqlData);
			//获取到对象getter的xmlList
			var accessorList:XMLList = xml.accessor;
			var accessorXML:XML;
			const l:int = accessorList.length();
			var name:String;
			var metadataXMlList:XMLList;
			var metadataXMlLength:int = 0;
			var putIntoParameters:Boolean = false;
			for(var i:int = 0;i < l;i++){
				accessorXML = accessorList[i];
				name = accessorXML.@name;
				metadataXMlList = accessorXML.metadata;
				metadataXMlLength = metadataXMlList.length();
				for(var j:int = 0; j < metadataXMlLength;j++){
					if(metadataXMlList[j].@name.toString() == "SQLData"){
						var args:XMLList = metadataXMlList[j].arg;
						putIntoParameters = false;
						for each(var arg:XML in args){
							if(arg.@key.toString() == "type"){
								switch(arg.@value.toString()){
									case "BitmapData":
										_updateStatement.parameters["@" + name] = BitmapBytes.bitmapDataToByteArray(sqlData[name]);
										putIntoParameters = true;
										break;
									case "Array":
										var b:ByteArray = new ByteArray();
										b.writeObject(sqlData[name]);
										_updateStatement.parameters["@" + name] = b;
										putIntoParameters = true;
										break;
								}
							}else if(arg.@key.toString() == "cloName"){
								if(keyValStr){
									keyValStr += ", " + arg.@value + " = @" + name;
								}else{
									keyValStr = arg.@value + " = @" + name;
								}
							}
						}
						if(!putIntoParameters)
							_updateStatement.parameters["@" + name] = sqlData[name];
						break;
					}
				}
			}
			_updateStatement.text += keyValStr + " where ID = " + sqlData.id;
			Logger.info("执行更新语句:" + _updateStatement.text);
			_updateStatement.execute();
		}
		
//		public function del(idList:Vector.<int> = null):void{
//			if(idList){
//				var idListStr:String = "(";
//				for(var i:int = 0;i < idList.length;i++){
//					idListStr += i == 0 ? idList[i] : "," + idList[i];
//				}
//				idListStr += ")";
//				_deleteStatement.text = "delete from " + _tableName + " where ID in " + idListStr;
//			}else{
//				_deleteStatement.text = "delete from " + _tableName;
//			}
//			Logger.info("执行删除语句:" + _deleteStatement.text);
//			_deleteStatement.execute(); 
//		}
		
		public function del(id:int, callback:Function = null):void{
			_deleteCallback = callback;
			_deleteStatement.text = "delete from " + _tableName + " where ID = " + id;
			Logger.info("执行删除语句:" + _deleteStatement.text);
			_deleteStatement.execute(); 
		}
		
		protected function onInsertHandler(evt:SQLEvent):void{
			var result:SQLResult = this._insertStatement.getResult();
			if(result.complete){
				if(this._insertCallBack != null) _insertCallBack();
			}
		}
		
		protected function onQueryHandler(evt:SQLEvent):void{
			if(_queryCallBack != null) _queryCallBack(this._queryStatement.getResult().data);
//			if (result.data != null)
//			{
//				var numResults:int = result.data.length;
//				
//				for (var i:int = 0; i < numResults; i++) 
//				{ 
//					var row:Object = result.data[i]; 
//					var output:String = "ID: " + row.ID; 
//					output += "; ACTRESS_ID: " + row.ACTRESS_ID; 
//					output += "; NAME: " + row.NAME;
//					output += "; BIRTHDAY: " + row.BIRTHDAY.fullYear;
//					
//					trace(output); 
//					
//					//					var bmd:BitmapData = BitmapBytes.byteArrayToBitmapData(row.PORTRAIT);
//					//					trace(bmd);
//				} 
//			}
		}
		
		protected function onUpdateHandler(evt:SQLEvent):void{
			if(_updateCallback != null) _updateCallback();
		}
		
		protected function onDeleteHandler(evt:SQLEvent):void{
			var result:SQLResult = this._deleteStatement.getResult();
			Logger.info("删除行数:" + result.rowsAffected);
			if(_deleteCallback != null){
				_deleteCallback();
			}
		}
		
		protected function onCreateResult(event:SQLEvent):void{
			Logger.info("初始化数据库成功" + _tableName);
			_createStmt.removeEventListener(SQLEvent.RESULT, onCreateResult);
			/*
			//				SQLiteManager.instance._actressTable.insert();
			var idList:Vector.<int> = new Vector.<int>();
			idList[0] = 1;
			idList[1] = 14;
			idList[2] = 12;
			SQLiteManager.instance._actressTable.query(idList);
			trace("查好了");
			*/
		}
	}
}