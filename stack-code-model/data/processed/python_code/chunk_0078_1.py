package metaswarm.build {
    import flash.display.DisplayObject;
    import flash.display.Graphics;
    import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	import flash.ui.Keyboard;
	import flash.net.*;
	import flash.utils.*;

    public class Preloader extends Sprite
    {
		private var _dataLoader:DataLoader;
		//var main:Main;
		private var _builder:Builder;
		
        public function Preloader(_builder:Builder):void{
			this._builder = _builder;
			this._dataLoader = new DataLoader(this);
			init();
		}
		
		//loads external data
		private function init():void{
			_dataLoader.preload();
		}
		
		public function preloadComplete(parsedData:Array):void{
			//trace("gw.preloadComplete");
			_builder.load(parsedData);
			_builder.make();
			_builder.go();
		}
		
    }//end class
}//end pkg