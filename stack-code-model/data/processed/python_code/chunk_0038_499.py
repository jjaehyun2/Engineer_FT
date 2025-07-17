package com.adobe.dashboard.util
{
	import flash.events.EventDispatcher;

	import spark.core.ContentCache;

	public class ContentCacheUtil extends EventDispatcher
	{

		/**
		 * Single instance of a ConentCache object used for caching images
		 */
		public static const contentCache:ContentCache = new ContentCache();
	}
}