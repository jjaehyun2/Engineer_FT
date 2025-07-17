package display {
	
	import flash.display.Sprite;
	import utils.randomInt;

	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class Scene extends Sprite {
		
		private var grid:Array;
		private var houses:Vector.<House>;
		
		public function Scene() {
			makeGrid();
			makeHouses();
			sort();
		}
		
		private function makeGrid():void {
			grid = [];
			for (var i:int = 0; i < 10; i++) {
				var row:Array = [];
				for (var j:int = 0; j < 10; j++) {
					row.push( {house:null, row:i, col:j } );
				}
				grid.push(row);
			}
		}
		
		private function makeHouses():void {
			houses = new Vector.<House>();
			
			var housesParams:Vector.<Object> = new < Object > [ { w:6, h:8, x:1, y:1 }, { w:3, h:3, x:7, y:0 }, { w:3, h:2, x:7, y:5 }, { w:2, h:2, x:8, y:8 }, 
				{ w:1, h:2, x:7, y:7 }, { w:2, h:1, x:7, y:4 }, { w:1, h:1, x:8, y:7 }, { w:1, h:1, x:9, y:7 }, { w:1, h:1, x:7, y:3 }, { w:1, h:1, x:8, y:3 },
				{ w:1, h:1, x:9, y:3 }, { w:1, h:1, x:9, y:4 }, { w:1, h:1, x:7, y:9 } ];
				
			for (var l:int = 0; l < 7; l++) {
				housesParams.push( { w:1, h:1, x:l, y:0 } );
				housesParams.push( { w:1, h:1, x:l, y:9 } );
			}
			
			for (var m:int = 1; m <= 8; m++) {
				housesParams.push( { w:1, h:1, x:0, y:m } );
			}
			
			for (var k:int = 0; k < housesParams.length; k++) {
				var house:House = new House(housesParams[k].w, housesParams[k].h);
				house.setPosinion(housesParams[k].x, housesParams[k].y);
				grid[housesParams[k].x][housesParams[k].y].house = house;
				houses.push(house);
			}
		}
		
		private function sort():void {
			for (var i:int = 9; i >= 0; i--) {
				for (var j:int = 0; j <= 9; j++) {
					if (grid[i][j].house != null) 
						addChild(grid[i][j].house)
				}
			}
		}
		
		private function getHouseByPosition(xPos:uint, yPos:uint):House {
			var house:House = null;
			for (var i:int = 0; i < houses.length; i++) {
				if (houses[i].xPosition == xPos && houses[i].yPosition == yPos)
				house = houses[i];
				break;
			}
			return house;
		}
		
	}
}