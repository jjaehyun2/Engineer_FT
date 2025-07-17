package dom.tidesdk.database
{
	/**
	 * <p>An object representing a TideSDK Database.
	 * After opening a database (<a
	 * href="#!/api/Ti.Database" rel="Ti.Database"
	 * class="docClass">Ti.Database</a>), you can use the
	 * properties of this object to interact with it.</p>
	 * 
	 *   <h2>Querying Databases</h2>
	 * 
	 *   <p>Note - Please make sure that all queries are
	 * SQLite compatible. Please refer to the code
	 * examples below:</p>
	 * 
	 *   <pre><code>//Open the database first var db = <a
	 * href="#!/api/Ti.Database-method-openFile"
	 * rel="Ti.Database-method-openFile"
	 * class="docClass">Ti.Database.openFile</a>(<a
	 * href="#!/api/Ti.Filesystem-method-getFile"
	 * rel="Ti.Filesystem-method-getFile"
	 * class="docClass">Ti.Filesystem.getFile</a>(       
	 *                        <a
	 * href="#!/api/Ti.Filesystem-method-getApplicationDataDirectory"
	 * rel="Ti.Filesystem-method-getApplicationDataDirectory"
	 * class="docClass">Ti.Filesystem.getApplicationDataDirectory</a>(),
	 * 'customdatabase.db'));     //Create a table and
	 * insert values into it db.execute("CREATE TABLE IF
	 * NOT EXISTS Users(id INTEGER, firstName TEXT)");
	 * db.execute("INSERT INTO Users VALUES(1,'Joe
	 * Bloggs')");        //Select from Table var rows =
	 * db.execute("SELECT * FROM Users"); while
	 * (rows.isValidRow()) {     //Alert the value of
	 * fields id and firstName from the Users database   
	 *  alert('The user id is '+rows.fieldByName('id')+',
	 * and user name is '+rows.fieldByName('firstName'));
	 *     rows.next();     }  //Release memory once you
	 * are done with the resultset and the database
	 * rows.close(); db.close(); </code></pre>
	 */
	public class TDB
	{
		//
		// PROPERTIES
		//

		/**
		 * <p>The row id of the last insert operation.</p>
		 */
		public var lastInsertRowId:Number;

		/**
		 * <p>The number of rows affected by the last execute
		 * call.</p>
		 */
		public var rowsAffected:Number;

		//
		// METHODS
		//

		/**
		 * <p>Close an open Database.DB. If the database is
		 * not open, this method will do nothing.</p>
		 */
		public function close():void {}

		/**
		 * <p>Executes an SQL query on this Database.DB.
		 * Currently all queries must be valid SQLite-style
		 * SQL.</p>
		 * 
		 * @param query  The SQL query to execute on this Database.DB. 
		 * @param multiple  A variable-length argument list of values to use with the given query 
		 * 
		 * @return Ti.Database.ResultSet   
		 */
		public function execute(query:String, multiple:Array=null):TResultSet { return null; }

		/**
		 * <p>Get the full filesystem path to the database.
		 * If this database was opened via Datbase.openFile
		 * this path will be the originally path used,
		 * otherwise it will be the path to a WebKit database
		 * in the application data directory.</p>
		 * 
		 * @return String   
		 */
		public function getPath():String { return ""; }

		/**
		 * <p>Remove a Database.DB. This method will close
		 * the database if it is open and remove the file
		 * from the filesystem.</p>
		 */
		public function remove():void {}

		public function TDB() {}
	}
}