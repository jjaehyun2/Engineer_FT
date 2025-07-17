package masputih.patterns.mvc.model {
	import flash.events.IEventDispatcher;
	import org.casalib.collection.UniqueList;

	/**
	 * Hold references to all models used in the game. Models are stored in unique list with no duplicate entries.
	 * @author Anggie Bratadinata
	 */
	public class ModelLocator {


		private var _models:UniqueList = new UniqueList();
		
		/**
		 * Register a model
		 * @param	model
		 */
		public function register(model:Model):void { 
			_models.addItem(model);	
		}
		
		/**
		 * Remove a reference to a model
		 * @param	model
		 */
		public function remove(model:Model):void {
			_models.removeItem(model);
		}
		
		/**
		 * Find a model by its name. Throws an error if a model can't be found.
		 * @param	name 
		 * @return	Model
		 */
		public function getModelByName(name:String):Model {
			for (var i:int = 0, len:int = _models.size; i < len; i++) {
				var model:Model = Model(_models.getItemAt(i));
				if (model.name == name) return model;
			}
			throw new Error("Unknown model name");
			return null;
		}

		/****************************************
		 * Singleton init
		 ****************************************/
		private static var _instance:ModelLocator;

		public function ModelLocator(enf:SingletonEnforcer){

		}

		public static function getInstance():ModelLocator {
			if (_instance == null)
				_instance = new ModelLocator(new SingletonEnforcer());
			return _instance;
		}

	}

}

class SingletonEnforcer {
};