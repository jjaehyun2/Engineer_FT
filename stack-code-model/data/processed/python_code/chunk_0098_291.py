/**
 * @author Peter Hansen
 * @author Daniel Wilken
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.zzznake.Game.Model
{
	import de.p3337.zzznake.Enum.GameObjectType;
	import de.p3337.zzznake.Game.Model.Field.Field;

	/**
	 * The GameObject is the base class for all components that a field can contain.
	 * @see de.p3337.zzznake.Enum.GameObjectType
	 */
	public class GameObject {
		
		private var _position:Field;
		
		/**
		 * Creates a new GameObject.
		 * 
		 * @param position A reference to the Field this object is tied to.
		 */
		public function GameObject(position:Field) {
			this.setPosition(position);
		}

		public function getPosition():Field {
			return _position;
		}
		
		public function getType():GameObjectType {
			return null;
		}
		
		public function dispose():void {
			_position.removeContent(this);
		}

		protected function setPosition(position:Field):void {
			if(_position !== null) {
				_position.removeContent(this);
			}
			_position = position;
			_position.addContent(this);
		}
	}
}