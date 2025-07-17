package com.github.mortido.sqcity.ui.gamefield
{
    import as3isolib.display.IsoSprite;

    import com.github.mortido.sqcity.GameState;
    import com.github.mortido.sqcity.models.Building;
    import com.github.mortido.sqcity.resources.Assets;
    import com.github.mortido.sqcity.ui.Tile;

    public class MoveBuildingFieldState extends EditFieldState
    {
        public function MoveBuildingFieldState()
        {
            guideSprite = new IsoSprite();
            editScene.addChild(guideSprite);
        }

        private var _building:Building;
        private var fittedTile:Tile;
        private var notFittedTile:Tile;
        private var guideSprite:IsoSprite;

        override protected function onTileSelected(x:int, y:int):void
        {
            updateGuideSprite(x, y);
        }

        private function updateGuideSprite(x:int, y:int):void
        {
            if (!_building || !isBuildingInRange(x, y, _building.type))
            {
                // Hide guide sprites.
                guideSprite.container.visible = false;
            }
            else
            {
                guideSprite.container.visible = true;

                // Check placement.
                var fitted:Boolean = checkPlacement(x, y, _building.type);
                fittedTile.visible = fitted;
                notFittedTile.visible = !fitted;
                guideSprite.moveTo(x * GameField.CELL_SIZE, y * GameField.CELL_SIZE, 0);
            }
        }

        override public function release():void
        {
            if (_building)
            {
                // Return building if it was removed.
                field.addBuilding(_building);
            }
            super.release();
        }

        override protected function onTileClicked(x:int, y:int):void
        {
            if (!_building)
            {
                _building = field.getBuildingByCoordinates(x, y);
                if (_building)
                {
                    field.removeBuilding(_building);

                    fittedTile = new Tile(_building.type.xSize, _building.type.ySize, Assets.getColor("@color/guide_sprite_fitted"), 0.5);
                    notFittedTile = new Tile(_building.type.xSize, _building.type.ySize, Assets.getColor("@color/guide_sprite_not_fitted"), 0.5);
                    guideSprite.sprites = [fittedTile, notFittedTile];
                    updateGuideSprite(x, y);
                }
            }
            else if (checkPlacement(x, y, _building.type))
            {
                GameState.instance.moveBuilding(_building, x, y);
                field.addBuilding(_building);
                _building = null;
                field.setState(new ScrollingFieldState());
            }
        }
    }
}