/*
 Copyright (c) 2007 - 2008 Eric J. Feminella <eric@ericfeminella.com>
 All rights reserved.

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is furnished
 to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
 INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
 PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 @internal
 */

package services
{
    import flash.data.SQLConnection;
    import flash.data.SQLResult;
    import flash.data.SQLStatement;
    import flash.events.SQLErrorEvent;
    import flash.events.SQLEvent;
    import flash.filesystem.File;
    import flash.net.Responder;
    
    import services.ISQLResponder;

    /**
     *
     * Provides an API from which Adobe AIR SQL specific classes can be
     * managed uniformly as a Service when building an application on
     * Adobe Cairngorm
     *
     * <p>
     * <code>SQLService</code> wraps both the <code>SQLStatement</code>
     * and <code>SQLConnection</code> in order to provide a Service
     * from which CRUD operations can be performed on a SQLite database
     * in the same manner as one would access typical RPC Services.
     * </p>
     *
     * <p>
     * <code>SQLService</code> supports both synchronous and asyncronous
     * transactions. A set of convenience methods have also been provided
     * to interface with the underlying <code>SQLConnection</code> object
     * in order to perform transactions.
     * </p>
     *
     * @example The following example demonstrates a typical implementation of
     * <code>SQLService</code> defined by <code>AIRServiceLocator</code>
     *
     * <listing version="3.0">
     *
     * &lt;?xml version="1.0" encoding="utf-8"?&gt;
     * &lt;services:AIRServiceLocator xmlns:mx = "http://www.adobe.com/2006/mxml"
     *                                xmlns:services = "com.ericfeminella.air.cairngorm.business.*\" &gt;
     *
     *  &lt;services:SQLService id = "service"
     *               localDatabaseFilePath = "{ File.desktopDirectory.nativePath.toString() }"
     *               localDatabaseFileName = "air.cairngorm.example.db"
     *                  /&gt;
     *
     * </listing>
     *
     * @see com.adobe.cairngorm.business.ServiceLocator
     *
     * @see flash.filesystem.File
     * @see flash.data.SQLConnection
     * @see com.ericfeminella.sql.ISQLResponder
     *
     */
    public class SQLService
    {
        /**
         *
         * Defines the qualified name of a local SQLite database
         *
         */
        protected var databaseFileName:String;

        /**
         *
         * Defines the absolute path to a local SQLite database
         *
         */
        protected var databaseFilePath:String;

        /**
         *
         * Defines a reference to the physical file which contains
         * a local SQLite database
         *
         * @see flash.filesystem.File
         *
         */
        protected var _databaseFile:File;

        /**
         *
         * Defines the <code>SQLConnection</code> from which the
         * Service is connected
         *
         */
        protected var _connection:SQLConnection;

        /**
         *
         * Defines the <code>SQLStatement</code> from which queries
         * are executed
         *
         */
        protected var _statement:SQLStatement;

        /**
         *
         * Creates a new instance of <code>SQLService</code> and
         * initiates members
         *
         */
        public function SQLService()
        {
            _connection = new SQLConnection();
            _statement  = new SQLStatement();
        }

        /**
         *
         * Retrieves the path to the local SQLite database
         *
         * @return the qualified path of the SQLite database
         *
         */
        public function get localDatabaseFilePath() : String
        {
            return databaseFilePath;
        }

        /**
         *
         * Sets the path to the local SQLite database
         *
         * @param the path to the database file
         *
         */
        public function set localDatabaseFilePath(value:String) : void
        {
            databaseFilePath = value;
        }

        /**
         *
         * Retrieves the name of the local SQLite database
         *
         * @return the name of the local SQLite database
         *
         */
        public function get localDatabaseFileName() : String
        {
            return databaseFileName;
        }

        /**
         *
         * Sets the name of the local SQLite database
         *
         * @param the name in which the database is to be named
         *
         */
        public function set localDatabaseFileName(value:String) : void
        {
            databaseFileName = value;
        }

        /**
         *
         * Retrieves the local SQLite database file object
         *
         * @return the local SQLite database file object
         *
         */
        public function databaseFile() : File
        {
            return _databaseFile;
        }

        /**
         *
         * Retrieves the SQLService SQLStatement instance
         *
         * @return SQLService SQLStatement instance
         *
         */
        public function get statement() : SQLStatement
        {
            return _statement;
        }

        /**
         *
         * Retrieves the SQLService SQLConnection instance
         *
         * @return SQLService SQLConnection instance
         *
         */
        public function get connection() : SQLConnection
        {
            return _connection;
        }

        /**
         *
         * Provides a mechanism for opening the underlying SQLite database connection
         * in synchronous mode
         *
         * @return reference to the <code>SQLConnection</code> which has been opened
         *
         */
        public function open() : SQLConnection
        {
            _databaseFile = new File( databaseFilePath + File.separator + databaseFileName );
			trace(_databaseFile.nativePath);
            _connection = new SQLConnection();
            _connection.open( _databaseFile );

            _statement = new SQLStatement();
            _statement.sqlConnection = _connection;

            return _connection;
        }

        /**
         *
         * Provides a mechanism for opening the underlying SQLite database connection
         * in asynchronous mode
         *
         * @param optional handler for an <code>SQLEvent.OPEN</code> event
         * @param  optional handler for an <code>SQLErrorEvent.ERROR</code> event
         *
         */
        public function openAsync(openHandler:Function = null, errorHandler:Function = null) : void
        {
            _databaseFile = new File( databaseFilePath + File.separator + databaseFileName );
            _connection = new SQLConnection();

            _statement = new SQLStatement();
            _statement.sqlConnection = _connection;

            if ( openHandler != null )
            {
                _connection.addEventListener( SQLEvent.OPEN, openHandler );
            }
            if ( openHandler != null )
            {
                _connection.addEventListener( SQLErrorEvent.ERROR, errorHandler );
            }

            _connection.openAsync( _databaseFile );
        }

        /**
         *
         * Executes a specific SQL operation against the <code>SQLService</code>
         * in asynchronous mode
         *
         * @param the SQL statement which to execute
         * @param responder which handles the operation result / fault
         * @param specifies the type in which a result is to be deserialized
         * @param optional prefetch
         *
         */
        public function executeAsync(statement:String, responder:ISQLResponder, dataType:Class = null, prefetch:int = -1.0) : void
        {
            _statement = new SQLStatement();
            _statement.sqlConnection = _connection;
            _statement.text = statement;

            if ( dataType != null )
            {
                _statement.itemClass = dataType;
            }

            _statement.execute( prefetch, new Responder( responder.result, responder.fault) );
        }

        /**
         *
         * Executes a specific SQL operation against the <code>SQLService</code>
         * synchronous mode
         *
         * @param the SQL statement which to execute
         * @param responder which handles the operation result / fault
         * @param specifies the type in which a result is to be deserialized
         * @param optional prefetch
         *
         */
        public function execute(statement:String, dataType:Class = null, prefetch:int = -1.0) : SQLResult
        {
            _statement.text = statement;

            if ( dataType != null )
            {
                _statement.itemClass = dataType;
            }

            _statement.execute( prefetch );
            return _statement.getResult();
        }

        /**
         *
         * Begins a transaction, within which all SQL statements executed
         * against the connection's database(s) are grouped.
         *
         */
        public function beginTransaction(lockType:String = null) : void
        {
            _connection.begin( lockType );
        }

        /**
         *
         * Commits an existing transaction, causing any actions performed by
         * the transaction's statements to be permanently applied to the
         * database.
         *
         */
        public function commitTransaction() : void
        {
            _connection.commit();
        }

        /**
         *
         * Rolls back an existing transaction created using the begin() method,
         * meaning all changes made by any SQL statements in the transaction
         * are discarded.
         *
         */
        public function rollbackTransaction() : void
        {
            _connection.rollback();
        }

        /**
         *
         * Retrieves the <code>SQLResult</code> object instance from the last
         * statement execution. For synchronous mode only.
         *
         * <p>
         * Typically one uses a <code>SQLResult.data</code> object to access the
         * rows of data returned by a SELECT statement.
         * </p>
         *
         * @return
         *
         */
        public function get result() : SQLResult
        {
            return statement.getResult();
        }
    }
}