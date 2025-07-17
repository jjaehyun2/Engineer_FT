/**
 * Created by vizoli on 4/9/16.
 */
package ageofai.home.model
{
    import ageofai.cost.constant.CUnitCost;
    import ageofai.home.ai.HomeAI;
    import ageofai.home.constant.CHome;
    import ageofai.home.event.HomeEvent;
    import ageofai.home.vo.HomeVO;
    import ageofai.villager.vo.VillagerVO;
    import flash.utils.Dictionary;

    import caurina.transitions.Tweener;

    import common.mvc.model.base.BaseModel;

    import flash.events.TimerEvent;
    import flash.utils.Timer;

    public class HomeModel extends BaseModel implements IHomeModel
    {
        private var _homes:Vector.<HomeVO>;
        private var _homeAI:HomeAI;

        private var _progressDic:Dictionary = new Dictionary(true);
        
        public function HomeModel()
        {
            this._homeAI = new HomeAI();
        }

        public function tick():void
        {
            this.calculateVillagerCreation();
        }

        private function calculateVillagerCreation():void
        {
            for ( var i:int = 0; i < this._homes.length; i++ )
            {
                if ( !this._homes[ i ].villagerIsCreating )
                {
                    if ( this._homeAI.isNewVillagerAvailable( this._homes[ i ].food, this._homes[ i ].villagers.length ) )
                    {
                        this._homes[ i ].villagerIsCreating = true;
                        this._homes[ i ].food -= CUnitCost.VILLAGER.food;

                        this.updateFoodAmount( this._homes[ i ], this._homes[ i ].food );

                        var home:HomeVO = this._homes[ i ];

                        var creationTimer:Timer = new Timer( CHome.VILLAGER_CREATION_TIME / CHome.VILLAGER_CREATION_TIMELY, CHome.VILLAGER_CREATION_TIMELY );
                        creationTimer.addEventListener( TimerEvent.TIMER, creationTimerHandler );
                        _progressDic[creationTimer] = home;

                        Tweener.addTween( this, {
                            time: 2,
                            onComplete: creationTimerCompleteHandler,
                            onCompleteParams: [ home ]
                        } );

                        creationTimer.start();
                    }
                }
            }
        }

        private function creationTimerHandler(e:TimerEvent):void
        {
            var home:HomeVO = _progressDic[e.currentTarget];
            var homeEvent:HomeEvent = new HomeEvent( HomeEvent.VILLAGER_CREATION_IN_PROGRESS );
            homeEvent.progressPercentage = e.currentTarget.currentCount * CHome.VILLAGER_CREATION_TIMELY;
            homeEvent.homeVO = home;

            dispatch( homeEvent );
        }
        
        private function creationTimerCompleteHandler( homeVO:HomeVO ):void
        {
            homeVO.villagerIsCreating = false;

            var homeEvent:HomeEvent = new HomeEvent( HomeEvent.REQUEST_TO_CREATE_VILLAGER );
            homeEvent.homeVO = homeVO;

            this.dispatch( homeEvent );
        }

        public function setInitHomes( homes:Vector.<HomeVO> ):void
        {
            this._homes = homes;

            this.setHomeVOIds();
        }

        private function setHomeVOIds():void
        {
            for ( var i:int = 0; i < this._homes.length; i++ )
            {
                this._homes[ i ].id = i;
            }
        }

        public function addVillager( homeVO:HomeVO, villagerVO:VillagerVO ):void
        {
            homeVO.villagers.push( villagerVO );
        }

        public function updateFoodAmount( homeVO:HomeVO, amount:int ):void
        {
            homeVO.food = amount;

            var event:HomeEvent = new HomeEvent( HomeEvent.FOOD_AMOUNT_UPDATED );
            event.homeVO = homeVO;

            this.dispatch( event );
        }

        public function updateWoodAmount( homeVO:HomeVO, amount:int ):void
        {
            homeVO.wood = amount;

            var event:HomeEvent = new HomeEvent( HomeEvent.WOOD_AMOUNT_UPDATED );
            event.homeVO = homeVO;

            this.dispatch( event );
        }

        public function getHomeByVillager( villagerVO:VillagerVO ):HomeVO
        {
            for ( var i:int = 0; i < this._homes.length; i++ )
            {
                for ( var j:int = 0; j < this._homes[ i ].villagers.length; j++ )
                {
                    if ( this._homes[ i ].villagers[ j ] == villagerVO )
                    {
                        return this._homes[ i ];
                    }
                }
            }

            return null;
        }
    }
}