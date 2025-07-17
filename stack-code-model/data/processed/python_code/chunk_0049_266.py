/**
 * User: Dave Long
 * Date: 09/10/13
 * Time: 23:05
 */
package {

    import com.sixfootsoftware.pitstop.Border;
    import com.sixfootsoftware.pitstop.ComponentRegistry;
    import com.sixfootsoftware.pitstop.GeneratedBackground;
    import com.sixfootsoftware.pitstop.PitCar;
    import com.sixfootsoftware.pitstop.SpriteRegistry;

    import org.flixel.*;

    public class SplashState extends FlxState {

        public function SplashState() {
        }

        override public function create():void {
            var backdrop:GeneratedBackground = new GeneratedBackground(1, 1);

            add(backdrop.getFlxSprite());
            add(ComponentRegistry.splashScreen);
            add(new Border());
        }

        override public function update():void {
            if (!ComponentRegistry.splashScreen.alive) {
                FlxG.switchState(new MenuState());
            }
            super.update();
        }
    }
}