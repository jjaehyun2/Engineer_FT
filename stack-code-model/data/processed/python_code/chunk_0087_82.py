/**
 * Created by newkrok on 08/04/16.
 */
package ageofai.home.view
{
	import ageofai.building.base.BaseBuildingView;
	import ageofai.home.view.event.HomeViewEvent;
	import ageofai.home.vo.HomeVO;
	import ageofai.map.constant.CMap;
	import ageofai.map.geom.IntPoint;
	import ageofai.villager.view.VillagerView;

	public class HomeView extends BaseBuildingView
	{
		private var _foodDisplayView:FoodDisplayView;
		private var _woodDisplayView:WoodDisplayView;

        public var id:int;
        
		public function HomeView()
		{
			this.createUI( HomeUI );
			this.createLifeBar();
			this.createProgressBar();
			this.createFoodDisplayView();
			this.createWoodDisplayView();

			this._graphicUI.x = CMap.TILE_SIZE;
			this._graphicUI.y = CMap.TILE_SIZE;
		}

		public function showProgressValue( value:Number ):void
		{
			this._buildProgressBar.show();
			this._buildProgressBar.drawProcessBar( value );
		}

		public function createVillagerView(homeVO:HomeVO):void
		{
			var homeViewEvent:HomeViewEvent = new HomeViewEvent( HomeViewEvent.VILLAGER_VIEW_CREATED );

			homeVO.pos = this.getRandomMapNodePointAroundTheHome();

			homeViewEvent.villagerView = new VillagerView();
			homeViewEvent.homeVO = homeVO;

			this.dispatchEvent( homeViewEvent );
		}

		private function getRandomMapNodePointAroundTheHome():IntPoint
		{
			var result:IntPoint = new IntPoint( this.x / CMap.TILE_SIZE, this.y / CMap.TILE_SIZE );
			var offsets:Array = [
				[ -1, -1 ], [ 0, -1 ], [ 1, -1 ], [ 2, -1 ],
				[ -1, 0 ], [ 2, 0 ],
				[ -1, 1 ], [ 2, 1 ],
				[ -1, 2 ], [ 0, 2 ], [ 1, 2 ], [ 2, 2 ],
			];

			var randomOffset:Array = offsets[Math.floor( Math.random() * offsets.length )];

			result.x += randomOffset[0];
			result.y += randomOffset[1];

			return result;
		}

		public function createFoodDisplayView():void
		{
			this._foodDisplayView = new FoodDisplayView();
			this._foodDisplayView.x = 40;
			this._foodDisplayView.y = 15;
			this.addChild( this._foodDisplayView );
		}

		public function createWoodDisplayView():void
		{
			this._woodDisplayView = new WoodDisplayView();
			this._woodDisplayView.x = 40;
			this._woodDisplayView.y = 35;
			this.addChild( this._woodDisplayView );
		}

		public function updateFoodAmount( amount:int ):void
		{
			this._foodDisplayView.updateAmount( amount );
		}

		public function updateWoodAmount( amount:int ):void
		{
			this._woodDisplayView.updateAmount( amount );
		}
	}
}