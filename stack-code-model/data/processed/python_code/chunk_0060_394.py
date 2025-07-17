package org.ranapat.bundles {
	
	public class Bundle {
		public static const CONTROL_MODE_AUTOMATIC:String = "automatic";
		public static const CONTROL_MODE_MANUAL:String = "manual";
		
		protected var _controlMode:String;
		private var _started:Boolean;
		private var _mesh:Mesh;
		
		public function Bundle() {
			Tools.ensureAbstractClass(this, Bundle);
			
			this._controlMode = Bundle.CONTROL_MODE_AUTOMATIC;
		}
		
		public function create():void {
			//
		}
		
		public function destroy():void {
			//
		}
		
		public function get controlMode():String {
			return this._controlMode;
		}
		
		public function get started():Boolean {
			return this._started;
		}
		
		public function link(mesh:Mesh):void {
			this._mesh = mesh;
		}
		
		public function start():void {
			this._started = true;
		}
		
		public function stop():void {
			this._started = false;
		}
		
		protected function meld(name:String, parameters:* = null):void {
			if (this._mesh) {
				this._mesh.announce(new Command(name, parameters));
			}
		}
		
		protected function announce(command:Command):void {
			if (this._mesh) {
				this._mesh.announce(command);
			}
		}
	}

}