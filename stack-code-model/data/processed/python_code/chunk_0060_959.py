package
{
	import flash.data.SQLConnection;
	import flash.data.SQLStatement;
	import flash.events.SQLErrorEvent;
	import flash.filesystem.File;
	import flash.net.SharedObject;
	
	import feathers.data.ListCollection;

	public class Model
	{
		private var location:String;
		private var category:String;
		private var userData:SharedObject = SharedObject.getLocal("userData");
		private var adHeight:Number = 0;
		
		public var sqlconnection:SQLConnection = null; 
		public var sqlstatement:SQLStatement = null;
		public var dbOpened:Boolean = false;
		
		public  var listdata:ListCollection;
		
		public function Model()
		{
			if (userData.data.platform == null)
			{
				userData.data.platform = Constants.XBOX;
				userData.flush();
			}
		}
		public function initDB(whichDB:String):Boolean
		{
			if (sqlconnection != null && sqlconnection.open)
				sqlconnection.close();
			sqlstatement = new SQLStatement();
			sqlconnection = new SQLConnection();
			
			sqlconnection.open(File.applicationDirectory.resolvePath("FIFA14.db"));
			trace("DB connected:" + sqlconnection.connected );
			sqlstatement.sqlConnection = sqlconnection;
			return sqlconnection.connected;
		}
		public function closeDB():void
		{
			sqlconnection.close();
			sqlstatement = null;
			sqlconnection = null;
		}
		public function sqlError(event:SQLErrorEvent):void
		{
			trace("Error message:", event.error.message);
			trace("Details:", event.error.details);
		}
		public function setAdHeight(adHeight:Number):void
		{
			if (adHeight > 40)
				this.adHeight = adHeight;
			else
				this.adHeight = Math.round( 44 * Main._appView.getAppScale()); // this would yield 83 for the Galaxy
		}
		public function getAdHeight():Number
		{
			return this.adHeight;
		}
		public function setLocation(location:String):void
		{
			this.location = location;
		}
		public function getLocation():String
		{
			return this.location;
		}
		public function setCategory(category:String):void
		{
			this.category = category;
		}
		public function getCategory():String
		{
			return this.category;
		}
		public function setPlatform(platform:String):void
		{
			userData.data.platform = platform;
			userData.flush();
		}
		public function getPlatform():String
		{
			return userData.data.platform;
		}
	}
}