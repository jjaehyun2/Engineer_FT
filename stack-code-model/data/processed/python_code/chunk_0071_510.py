package utils.displayObject {
	import flash.display.Loader;
	import flash.events.Event;
	import flash.net.URLRequest;
	import mx.core.UIComponent;
	import flash.events.IOErrorEvent;
	import utils.strings.Strings;

	public class imgLoader extends UIComponent {
		private var _loader:Loader;
		private var _request:URLRequest;
		private var _callback:Function = function ():void {};
		private var _container:*;
		
		private function onIOError(event:*):void {
			this._container.error = 'ERROR 4';
			this._onComplete();
		}
		
		public function imgLoader(url:String, container:*, callback:Function) {
			// RSL Framework Fix
			if(url.indexOf("[[DYNAMIC]]/1") > -1) url = rslFix(url,"/","/1",".swf");
			
			this._loader = new Loader();
			this._request = new URLRequest(url);
			this._callback = (callback is Function) ? callback : this._callback;
			this._container = (container != null) ? container : this._container;
			this._loader.contentLoaderInfo.addEventListener(Event.COMPLETE,onComplete);
			this._loader.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR,onIOError);
			this._loader.load(this._request);
		}
		
		/**
		 * Designed to remove the the [filename.swf/[[DYNAMIC]]/1] 
		 * @param url
		 * @param start
		 * @param stop
		 * @param key
		 * @return 
		 */
		 
		private function rslFix(url:String, start:String ,stop:String ,key:String):String {
			return url.substring(0,url.split(key)[0].toString().lastIndexOf(start)+1)+utils.strings.Strings.filter(url.split(key)[1].substr(url.split(key)[1].toString().indexOf(stop)),stop,"");
		}
		
		
		
		
		private function _onComplete():void {
			if (this._callback is Function) {
				try {
					this._callback(this);
				} catch (e:Error) {
				}
			}
		}
		
		
		
		
		private function onComplete(event:Event):void {
			this.addChild(this._loader);
			this._onComplete();
		}
		
		
		
		
		
		public function get image():Loader {
			return this._loader;
		}
		
		
		
		
		
		public function set callback(callback:Function):void {
			if (this._callback != callback) {
				this._callback = callback;
			}
		}
		
		
		
		
		
		public function get callback():Function {
			return this._callback;
		}
		
		
		
		
		
		
		public function set container(container:*):void {
			if (this._container != container) {
				this._container = container;
			}
		}
		
		
		
		
		
		public function get container():* {
			return this._container;
		}
	}
}