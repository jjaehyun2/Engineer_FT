package com.controller {
	import com.libs.vo.GlobalsVO;
	
	import flash.system.Security;
	
	import framework.components.Component;

	public class Application extends Container {
		private var _start_callback:Function;
		
		public function Application() {
			super();
			GlobalsVO.setGlobal("stage",stage);
			Component.initStage(stage);
			initialize();
		}
		
		public function set start_callback(start_callback:Function):void {
			if (this._start_callback != start_callback) {
				this._start_callback = start_callback;
				this.issue_start_callback();
			}
		}
		
		public function get start_callback():Function {
			return this._start_callback;
		}
		
		/**
		 * @public 
		 * Initialize
		 */
		 	
		public function initialize():void {
			
			Security.allowDomain("*");
			Security.allowInsecureDomain("*");
			// Clear Output Window
			for(var i:int = 0; i<200;++i) trace();
			this.start();
		}
		
		private function onStatus(o:Object):void {
			trace(o.status+"\n"+o.msg);
		}
		
		
		private function issue_start_callback():void {
			if (this._start_callback is Function) {
				try { this._start_callback(stage); }
					catch (err:Error) {trace('Application.issue_start_callback().ERROR '+err.toString()+'\n'+err.getStackTrace())}
			}
		}

		private function start():void {
			//stage.addChild(ImagesVO.getAsset("logo"));
			this.issue_start_callback();
		}
	}
}