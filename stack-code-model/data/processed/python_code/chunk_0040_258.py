package com.tourism_in_lviv.air.services
{
	import com.tourism_in_lviv.air.services.signals.Failed;
	
	import flash.errors.IllegalOperationError;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.events.SecurityErrorEvent;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	
	import org.osflash.signals.ISignal;

	public class AbstractXmlLoaderService
	{
		private var loader:URLLoader;
		private var request:URLRequest;
		private var url:String;
		private var _failed:Failed;

		public function AbstractXmlLoaderService( url:String )
		{
			this.url = url;

			loader = new URLLoader();
			_failed = new Failed();
		}

		public function get loaded():ISignal
		{
			throw new IllegalOperationError( "Must be overridden in sub-class." );
		}

		public function get failed():ISignal
		{
			return _failed;
		}

		protected function makeRequest( dynamicPaths:Vector.<String> = null, parameters:Vector.<UrlParameter> = null ):void
		{
			var serviceUrl:ServiceUrl = new ServiceUrl( url, dynamicPaths, parameters );

			addLoaderListeners();
			request = new URLRequest( serviceUrl.toString());
			loader.load( request );
		}

		protected function parse( xml:XML ):void
		{
			throw new IllegalOperationError( "Must be overridden in sub-class." );
		}

		protected function fail( message:String = "" ):void
		{
			_failed.dispatch( message );
		}

		protected function createDynamicPaths( ... dynamicPaths ):Vector.<String>
		{
			return Vector.<String>( dynamicPaths );
		}

		protected function createParameters( ... parameterPairs ):Vector.<UrlParameter>
		{
			var parameterVector:Vector.<UrlParameter> = new Vector.<UrlParameter>();

			for ( var index:uint = 0; index < parameterPairs.length; index += 2 )
			{
				if ( parameterPairs[ index ] != "" && parameterPairs[ index + 1 ] != "" )
					parameterVector.push( new UrlParameter( parameterPairs[ index ], parameterPairs[ index + 1 ]));
			}

			return parameterVector;
		}

		private function completeHandler( event:Event ):void
		{
			removeLoaderListeners();

			try
			{
				var xml:XML = XML( loader.data );
				parse( xml );
			}
			catch ( error:Error )
			{
				fail( error.message );
			}
		}

		private function ioErrorHandler( event:IOErrorEvent ):void
		{
			removeLoaderListeners();
			fail( "" );
		}

		private function securityErrorHandler( event:SecurityErrorEvent ):void
		{
			removeLoaderListeners();
			fail( "" );
		}

		private function addLoaderListeners():void
		{
			loader.addEventListener( Event.COMPLETE, completeHandler );
			loader.addEventListener( IOErrorEvent.IO_ERROR, ioErrorHandler );
			loader.addEventListener( SecurityErrorEvent.SECURITY_ERROR, securityErrorHandler );
		}

		private function removeLoaderListeners():void
		{
			loader.removeEventListener( Event.COMPLETE, completeHandler );
			loader.removeEventListener( IOErrorEvent.IO_ERROR, ioErrorHandler );
			loader.removeEventListener( SecurityErrorEvent.SECURITY_ERROR, securityErrorHandler );
		}
	}
}