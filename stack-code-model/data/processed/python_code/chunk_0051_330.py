package ManaMason.Structures 
{
	/**
	 * ...
	 * @author Hellrage
	 */
	
	import ManaMason.BlueprintOptions;
	import ManaMason.Utils.BlueprintOption;
	import com.giab.games.gcfw.constants.BuildingType;
	import com.giab.games.gcfw.GV;
	import com.giab.games.gcfw.entity.Pylon;
	
	import ManaMason.Structure;
	
	public class Pylon extends Structure
	{
		public var targetPriority:int;
		
		public function Pylon(bpIX:int, bpIY:int) 
		{
			super("p", bpIX, bpIY);
			this.rendered = false;
			this.size = 2;
			this.xOffset = -4;
			this.yOffset = -5;
			
			this.buildingType = BuildingType.PYLON;
			this.spellButtonIndex = 17;
			this.targetPriority = 0;
		}
		
		public override function castBuild(bpo: BlueprintOptions): void
		{
			var existingBuilding: Object = GV.ingameCore.buildingRegPtMatrix[buildingGridY][buildingGridX];
			
			if (existingBuilding is com.giab.games.gcfw.entity.Pylon)
			{
				if (existingBuilding.insertedGem == null && bpo.read(BlueprintOption.CONJURE_GEMS))
					super.castBuild(bpo);
				return;
			}
			
			if (bpo.read(BlueprintOption.SPEND_MANA) && GV.ingameCore.getMana() < this.getCurrentManaCost())
				return;
				
			if (placeable(bpo, true))
			{
				GV.ingameCore.creator.buildPylon(buildingGridX, buildingGridY);
				if (bpo.read(BlueprintOption.TRACK_STATS))
				{
					GV.ingameCore.stats.spentManaOnPylons += Math.max(0, this.getCurrentManaCost());
				}
			}
			else return;
			
			GV.ingameCore.buildingAreaMatrix[buildingGridY][buildingGridX].targetPriority = this.targetPriority;
			if (bpo.read(BlueprintOption.SPEND_MANA))
			{
				GV.ingameCore.changeMana( -this.getCurrentManaCost(), false, true);
				this.incrementManaCost();
			}
		}
	
		public override function incrementManaCost(): void
		{
			GV.ingameCore.currentPylonBuildingManaCost.s(Math.round(GV.PYLON_COST_MULT.g() * (GV.ingameCore.currentPylonBuildingManaCost.g() + Math.round(GV.PYLON_COST_INCREMENT.g()))));
		}
		
		public override function getCurrentManaCost(): Number
		{
			return GV.ingameCore.currentPylonBuildingManaCost.g();
		}
		
		public override function insertGem(gem:Object): void
		{
			
		}

		public override function isOnPath():Boolean
		{
			if (!fitsOnScene())
				return false;
			return GV.ingameCore.groundMatrix[buildingGridY][buildingGridX] == "#" ||
				GV.ingameCore.groundMatrix[buildingGridY+1][buildingGridX] == "#" ||
				GV.ingameCore.groundMatrix[buildingGridY][buildingGridX+1] == "#" ||
				GV.ingameCore.groundMatrix[buildingGridY+1][buildingGridX+1] == "#";
		}

		public override function placeable(bpo: BlueprintOptions, finalCalculation:Boolean = false):Boolean
		{
			if (!bpo.read(BlueprintOption.BUILD_ON_PATH) && isOnPath())
				return false;
			if (!fitsOnScene())
				return false;
			return bpo.read(BlueprintOption.PLACE_PYLONS) && GV.ingameCore.controller.isBuildingBuildPointFree(buildingGridX, buildingGridY, this.buildingType)
				&& (!finalCalculation || !GV.ingameCore.calculator.isNew2x2BuildingBlocking(buildingGridX, buildingGridY));
		}
	}

}