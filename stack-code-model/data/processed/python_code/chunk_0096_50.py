package 
{
	import flash.display.Sprite;
	
	/**
	 * ...
	 * @author 
	 */
	public class Entity extends Sprite 
	{
		
		public function Entity() 
		{
			super();
			
		}
		
		public override function collision(other:Entity) :void {
			
		}
		
		
		public override function destroyEntity() {
			parent.removeChild(this);
			dispatchEvent("removedEntityObject")
		}
	}

}