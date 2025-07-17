/*
Copyright (c) 2007, Yahoo! Inc. All rights reserved.
Code licensed under the BSD License:
http://developer.yahoo.net/yui/license.txt
version: 2.2.0
*/
package com.yahoo.webapis.search
{
	
	
	/**
	 * Cache is a Value Object for the Search API.
     * @langversion ActionScript 3.0
	 * @playerversion Flash 9
	 * @author Alaric Cole 02/22/07
	 */
	 
	public class Cache
	{
		private var _id:String;
		private var _name:String;
		
		private var _url:String;
		private var _size:uint;
		
		/**
		 * Construct a new Cache instance.
		 */
		public function Cache(url:String, size:uint)
		{
			this.url = url;
			this.size = size;
		}
		
		
		
		/**
		 * The ID of the Cache.
		 */
		public function get id():String
		{
			return _id;
		}
		
		public function set id( value:String ):void
		{
			_id = value;
		}
		
		
		
		/**
		 * The Name of the Cache.
		 */
		public function get name():String
		{
			return _name;
		}
		
		public function set name( value:String ):void
		{
			_name = value;
		}
		
		
		/**
		 * The url to the Cache.
		 */
		public function get url():String
		{
			return _url;
		}
		
		public function set url( value:String ):void
		{
			_url = value;
		}
		
		/**
		 * The size of the Cache in bytes.
		 */
		public function get size():uint
		{
			return _size;
		}
		
		public function set size( value:uint ):void
		{
			_size = value;
		}
		
		
		public function toString():String
		{
			return url;
		}
		
	}
}