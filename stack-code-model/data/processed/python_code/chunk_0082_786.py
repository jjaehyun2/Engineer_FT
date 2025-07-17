/**
 * @author Peter Hansen
 * @author Daniel Wilken
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.zzznake.Game.Model.Snack
{	
	import mx.core.SpriteAsset;
	
	import de.p3337.zzznake.Game.Model.GameObject;
	import de.p3337.zzznake.Game.Model.Field.Field;

	/**
	 * The SnackElement is the base class for all types of food.
	 * 
	 * @see de.p3337.zzznake.Game.Model.Snack.PizzaElement
	 */
	public class SnackElement extends GameObject {
		
		/**
		 * Creates a new SnackElement.
		 * 
		 * @param position The reference to a Field of the PlayingField this object is tied to.
		 * @see de.p3337.zzznake.Game.Model.Field.PlayingField
		 */
		public function SnackElement(position:Field) {
			super(position);
		}
		
		public function getSpriteAsset():SpriteAsset {
			return null;
		}
	}
}