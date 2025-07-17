package org.ranapat.bundles {
	import flash.events.Event;
	
	public class MeshEvent extends Event {
		public static const COMPLETE:String = "MeshEvent::complete";
		public static const FAILED:String = "MeshEvent::failed";
		public static const YELL:String = "MeshEvent::yell";
		
		public var mesh:Mesh;
		public var parameters:*;
		
		public function MeshEvent(type:String, mesh:Mesh, parameters:* = null) {
			super(type);
			
			this.mesh = mesh;
			this.parameters = parameters;
		}
		
	}

}