package alternativa.engine3d.controllers
{
	import alternativa.engine3d.collisions.EllipsoidCollider;
	import alternativa.engine3d.controllers.SimpleObjectController;
	import alternativa.engine3d.core.Object3D;
    
    import alternativa.engine3d.core.Camera3D;
    import alternativa.engine3d.core.Object3D;
    import flash.display.InteractiveObject;
    import flash.geom.Vector3D;
    import flash.utils.Dictionary;
    /**
     * ...
     * @author Glenn Ko
     */
    public class SimpleFlyController extends SimpleObjectController
    {
        public var collider:EllipsoidCollider;
        public var collidable:Object3D;
        
        public var displacement:Vector3D = new Vector3D();
        public var collisionPoint:Vector3D = new Vector3D();
        public var lastPosition:Vector3D  = new Vector3D();
        public var excludedObjects:Dictionary = null;
        
        
        public function SimpleFlyController(collider:EllipsoidCollider, collidable:Object3D, eventSource:InteractiveObject, object:Object3D, speed:Number, speedMultiplier:Number = 3, mouseSensitivity:Number = 1) 
        {
            super(eventSource, object, speed, speedMultiplier, mouseSensitivity);
            this.collider = collider;
            this.collidable = collidable;
        }
        

        override public function update(time:Number):void {
            var object:Object3D = this.object;
            
            if (object == null) return;
            if (collider && collidable) {
                lastPosition.x = object.x;
                lastPosition.y = object.y;
                lastPosition.z = object.z;
                super.update(time);
                displacement.x = object.x -  lastPosition.x;
                displacement.y = object.y  - lastPosition.y;
                displacement.z = object.z  - lastPosition.z;

                var dest:Vector3D = collider.calculateDestination(lastPosition, displacement, collidable, excludedObjects);
                 // set back frame coherant transform values
                setObjectPosXYZ(dest.x, dest.y, dest.z);
                // refresh values immediately
                object.x = dest.x; 
                object.y = dest.y;
                object.z = dest.z;
            }
            else {
                super.update(time);
            }
        }
        
    }

}