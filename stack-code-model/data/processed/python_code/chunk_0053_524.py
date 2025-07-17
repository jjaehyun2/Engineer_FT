package org.avManager.model.sql
{
	import flash.data.SQLConnection;
	import flash.utils.ByteArray;
	
	import org.avManager.model.data.SQLData;
	import org.avManager.model.data.VideoData;
	import org.libra.utils.DateUtil;
	import org.libra.utils.bytes.BitmapBytes;
	
	public final class VideoTable extends Table
	{
		public function VideoTable(sqlConnection:SQLConnection)
		{
			_tableName = "video";
			super(sqlConnection);
		}
		
		override protected function init():void{
			super.init();
			_insertStatement.text = "INSERT INTO " + _tableName + 
				" (NAME, VIDEO_ID, DATE, COVER, COVER_SUB, CLASSIFICATION, TORRENT, ACTRESS) VALUES (@name, @videoID, @date, @cover, @coverSub, @classification, @torrent, @actress)";
			
			var keyList:Vector.<String> = new Vector.<String>();
			keyList[0] = "ID INTEGER PRIMARY KEY AUTOINCREMENT";
			keyList[1] = "NAME NVARCHAR";
			keyList[2] = "VIDEO_ID VARCHAR";
			keyList[3] = "DATE DATE";
			keyList[4] = "COVER BLOB";
			keyList[5] = "COVER_SUB BLOB";
			keyList[6] = "CLASSIFICATION BLOB";
			keyList[7] = "TORRENT VARCHAR";
			keyList[8] = "ACTRESS VARCHAR";
			_createSql = "CREATE TABLE IF NOT EXISTS " + _tableName + " (";
			const l:int = keyList.length;
			for(var i:int = 0;i < l;i++){
				_createSql += i == 0 ? keyList[i] : "," + keyList[i];
			}
			_createSql += ")";
		}
		
		override public function insert(sqlData:SQLData, callback:Function = null):void{
			super.insert(sqlData, callback);
			var videoData:VideoData = sqlData as VideoData;
			_insertStatement.parameters["@name"] = videoData.name;
			_insertStatement.parameters["@videoID"] = videoData.videoID;
			_insertStatement.parameters["@date"] = videoData.date;
			_insertStatement.parameters["@torrent"] = videoData.torrent;
			_insertStatement.parameters["@actress"] = videoData.actress;
			_insertStatement.parameters["@cover"] = BitmapBytes.bitmapDataToByteArray(videoData.cover);
			_insertStatement.parameters["@coverSub"] = BitmapBytes.bitmapDataToByteArray(videoData.coverSub);
			var b:ByteArray = new ByteArray();
			b.writeObject(videoData.classification);
			_insertStatement.parameters["@classification"] = b;
			_insertStatement.execute();
		}	
	}
}