package com.IndieGo.utils {

	import flash.events.Event;
	import flash.net.URLRequest;
	import flash.net.URLLoader;

	public function XMLLoader( path:String, callback:Function ): void {

		var urlLoader:URLLoader = new URLLoader( new URLRequest( path ) );
		
		urlLoader.addEventListener( Event.COMPLETE, function( e:Event ) {
			
			callback( new XML( e.currentTarget.data ) );
			
			urlLoader = null;
			
		});

	}

}