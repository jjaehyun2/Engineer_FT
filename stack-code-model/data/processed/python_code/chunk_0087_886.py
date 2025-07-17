package ageofai.config
{
	import ageofai.building.model.BuildingModel;
	import ageofai.building.model.IBuildingModel;
	import ageofai.fruit.model.FruitModel;
	import ageofai.fruit.model.IFruitModel;
	import ageofai.game.model.GameModel;
	import ageofai.game.model.IGameModel;
	import ageofai.home.model.HomeModel;
	import ageofai.home.model.IHomeModel;
	import ageofai.map.model.IMapModel;
	import ageofai.map.model.MapModel;
	import ageofai.unit.model.IUnitModel;
	import ageofai.unit.model.UnitModel;
	import ageofai.villager.model.IVillagerModel;
	import ageofai.villager.model.VillagerModel;

	import robotlegs.bender.framework.api.IConfig;
import robotlegs.bender.framework.api.IInjector;


	public class ModelConfig implements IConfig
	{
		[Inject]
		public var injector:IInjector;
		
		/**
		 * Configure.
		 */
		public function configure():void
		{
			this.injector.map( IMapModel ).toSingleton( MapModel );
			this.injector.map( IFruitModel ).toSingleton( FruitModel );
			this.injector.map( IUnitModel ).toSingleton( UnitModel );
			this.injector.map( IGameModel ).toSingleton( GameModel );
			this.injector.map( IBuildingModel ).toSingleton( BuildingModel );
			this.injector.map( IHomeModel ).toSingleton( HomeModel );
			this.injector.map( IVillagerModel ).toSingleton( VillagerModel );
		}
		
	}

}