/**
 * User: Dave Long
 * Date: 09/10/13
 * Time: 23:05
 */
package {

    import com.sixfootsoftware.pitstop.AssetRegistry;
    import com.sixfootsoftware.pitstop.Border;
    import com.sixfootsoftware.pitstop.CarGrid;
    import com.sixfootsoftware.pitstop.ComponentRegistry;
    import com.sixfootsoftware.pitstop.GeneratedBackground;
    import com.sixfootsoftware.pitstop.PitCar;
    import com.sixfootsoftware.pitstop.SpriteRegistry;

    import org.flixel.*;
    import org.flixel.plugin.photonstorm.FlxButtonPlus;



    public class MenuState extends FlxState {

        public function MenuState() {
        }

        override public function create():void {
            var backdrop:GeneratedBackground = new GeneratedBackground(1, 1);
            ComponentRegistry.reset();
            SpriteRegistry.reset();

            //menu gen
            var menuBg:GeneratedBackground = new GeneratedBackground(1, 1, 355, 462 );
            var menuSprite:FlxSprite = menuBg.getFlxSprite()
            menuSprite.drawLine( 0, 0, 355, 0, 0, 12 );
            menuSprite.drawLine( 0, 0, 0, 462, 0, 12 );
            menuSprite.drawLine( 355, 0, 355, 462, 0, 12 );
            menuSprite.drawLine( 0, 462, 355, 462, 0, 12 );
            menuSprite.x =  PitStop.GAME_X_MIDDLE - ( 355 / 2 );
            menuSprite.y =  PitStop.GAME_Y_MIDDLE - ( 462 / 2 );
            menuSprite.alpha = 0.95;
            var startGame:FlxButtonPlus = new FlxButtonPlus( PitStop.GAME_X_MIDDLE - ( 288 / 2 ), 85, onClickStart );
            var start:FlxSprite = new FlxSprite();
            var hover:FlxSprite = new FlxSprite();

            startGame.loadGraphic( start.loadGraphic( AssetRegistry.Menu_NewGame, false, false )
                                 , hover.loadGraphic( AssetRegistry.Menu_NewGame_Hover, false, false ) );

            configureComponents();

            add(backdrop.getFlxSprite());
            add(ComponentRegistry.gameOver);
            add(ComponentRegistry.pitstopText);
            add(ComponentRegistry.scoreText);
            add(ComponentRegistry.scoreTextGenerator);
            add(ComponentRegistry.pitstopTextGenerator);
            add(ComponentRegistry.stopWatchDisplay);
            add(ComponentRegistry.demoControl);
            add(SpriteRegistry.backgroundCarGrid);
            add(SpriteRegistry.grid);
            SpriteRegistry.grid.setMode( CarGrid.DEMO );
            add(menuSprite);
            add(startGame);

            add(new Border());
        }

        private function onClickStart():void {
            FlxG.switchState( new PlayState() );
            return;
        }

        private function configureComponents():void {
            ComponentRegistry.gameOver.setStopWatch(ComponentRegistry.stopWatch);
            ComponentRegistry.stopWatchDisplay.setStopWatch(ComponentRegistry.stopWatch);
            ComponentRegistry.pitstopTextGenerator.setPitstopCalculator( ComponentRegistry.pitstopCalculator );
            ComponentRegistry.scoreTextGenerator.setScoreCalculator( ComponentRegistry.scoreCalculator );
            ComponentRegistry.demoControl.setPitGridCar( SpriteRegistry.grid.getPitPlacement() as PitCar );
        }

        override public function update():void {
            if (!ComponentRegistry.gameOver.alive) {
                prepareStartOfGame();
            }
            if (ComponentRegistry.gameOver.isGameRunning()) {
                ComponentRegistry.stopWatch.updateElapsed();
                if ( ComponentRegistry.stopWatch.hasTimedOut() ) {
                    prepareStartOfGame();
                }

            }
            super.update();
        }

        private function prepareStartOfGame():void {
            ComponentRegistry.gameOver.startGame();
            ComponentRegistry.pitstopText.revive();
            ComponentRegistry.scoreText.revive();
            ComponentRegistry.scoreTextGenerator.revive();
            ComponentRegistry.pitstopTextGenerator.revive();
            ComponentRegistry.stopWatchDisplay.revive();
            ComponentRegistry.demoControl.revive();
            SpriteRegistry.backgroundCarGrid.revive();
            SpriteRegistry.grid.revive();
        }

    }
}