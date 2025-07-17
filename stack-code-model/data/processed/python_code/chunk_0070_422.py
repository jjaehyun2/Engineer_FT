/**
 * Created by vizoli on 4/8/16.
 */
package ageofai.home.controller
{
    import ageofai.home.model.IHomeModel;
    import ageofai.map.event.MapCreatedEvent;

    import common.mvc.controller.base.BaseCommand;

    public class SetInitHomesCommand extends BaseCommand
    {
        [Inject]
        public var homeModel:IHomeModel;

        [Inject]
        public var event:MapCreatedEvent;

        override public function execute():void
        {
            this.homeModel.setInitHomes( this.event.mapData.homes );
        }
    }
}