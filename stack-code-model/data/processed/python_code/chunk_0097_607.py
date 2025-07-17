package com.adrienheisch.spacewar.background 
{
	
	import flash.display.MovieClip;
	
	/**
	 * ...
	 * @author Adrien Heisch
	 */
	public class BackgroundContainer extends MovieClip 
	{

		/**
		 * instance unique de la classe BackgroundContainer
		 */
		protected static var _instance: BackgroundContainer;
		
		/**
		 * Retourne l'instance unique de la classe, et la crée si elle n'existait pas au préalable
		 * @return instance unique
		 */
		public static function get instance (): BackgroundContainer {
			if (_instance == null) _instance = new BackgroundContainer();
			return _instance;
		}
	
		public function BackgroundContainer() 
		{
			super();
			
			if (_instance != null) throw new Error(this + "is a Singleton, please use BackgroundContainer.instance");
			else {
				_instance = this;
				
			}
		}
		
		/**
		 * détruit l'instance unique et met sa référence interne à null
		 */
		public function destroy (): void {
			_instance = null;
			if (parent != null) parent.removeChild(this);
		}

	}
	
}