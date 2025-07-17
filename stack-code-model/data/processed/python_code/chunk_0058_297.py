/**
 * Created by vizoli on 4/8/16.
 */
package ageofai.game.controller
{
    import ageofai.building.model.IBuildingModel;
    import ageofai.home.model.IHomeModel;
    import ageofai.villager.model.IVillagerModel;

    import common.mvc.controller.base.BaseCommand;

    public class ProcessTickCommand extends BaseCommand
    {
        [Inject]
        public var buildingModel:IBuildingModel;

        [Inject]
        public var homeModel:IHomeModel;

        [Inject]
        public var villagerModel:IVillagerModel;

        override public function execute():void
        {
            this.buildingModel.tick();
            this.homeModel.tick();
            this.villagerModel.tick();
        }
    }
}