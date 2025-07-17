package away3d.containers 
{
	import away3d.cameras.Camera3D;
	import away3d.core.render.RendererBase;
	import flash.geom.Vector3D;
	
	/** Use instead of View3D when using shared context like when using Starling. **/
	public class SharedContextView3D extends View3D 
	{
		
		public function SharedContextView3D(scene:Scene3D=null, camera:Camera3D=null, renderer:RendererBase=null, forceSoftware:Boolean=false, profile:String="baseline") 
		{
			super(scene, camera, renderer, forceSoftware, profile);
			
		}
		
		/**
		 * Calculates the projected position in screen space of the given scene position.
		 *
		 * @param point3d the position vector of the point to be projected.
		 * @return The absolute screen position of the given scene coordinates.
		 */
		override public function project( point3d: Vector3D ):Vector3D
		{ 
			var v:Vector3D = _camera.project(point3d);
			
			v.x = (v.x + 1.0)*_stage3DProxy.width/2.0;
			v.y = (v.y + 1.0)*_stage3DProxy.height/2.0;
			
			return v;
		}
		
		
	}

}