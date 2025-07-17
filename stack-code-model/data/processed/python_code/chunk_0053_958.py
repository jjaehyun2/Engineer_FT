/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.straightouttaspace.Views.Objects.Spaceships
{
	import de.p3337.straightouttaspace.Objects.DrawableObject;
	import de.p3337.straightouttaspace.Views.Objects.DrawableObjectView;
	
	public class PlayerSpaceshipView extends DrawableObjectView
	{	
		public function PlayerSpaceshipView(drawableObject:DrawableObject)
		{
			super(drawableObject);
			
			texture.x -= texture.width / 2;
			texture.y -= texture.height / 2;
		}
		
		/**
		 * @inheritDoc
		 */
		override public function update():void
		{
			super.update();
			texture.rotation = drawableObject.rotation;
			texture.scaleX = drawableObject.scaleX;
		}
	}
}