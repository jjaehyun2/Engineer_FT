package {
    import org.apache.royale.display.UIGraphicsBase;
    import org.apache.royale.display.Graphics;

    public class Main extends UIGraphicsBase {

        private var g:Graphics;
        private var x:Number = 0, y:Number = 0;

        public function Main() {
            g = Graphics.getInstanceFor(this);

            document.body.appendChild(element);
        }

        private function animateHandler():void {
            g.clear();
            g.beginFill(0xffcccccc);
            g.lineStyle(2,0xff000000);
            g.drawCircle(x, y, 15);
            g.endFill();

            x += 0.1;
            y += 0.1;

            requestAnimationFrame(animateHandler);
        }

        public function start():void {
            width = 550;
            height = 400;

            requestAnimationFrame(animateHandler);
        }
    }
}