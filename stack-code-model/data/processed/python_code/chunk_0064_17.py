package {
    import flash.display.Sprite;
    import flash.text.TextField;
    import flash.system.System;

    public class Main extends Sprite {
        public function Main() {
            var tf:TextField = new TextField();
            tf.width = 400;
            tf.wordWrap = true;
            addChild(tf);

            var js_env:Function = System['js_env'];
            if (js_env) {
                tf.text = js_env();
            } else {
                tf.text = "Can not get js_env";
            }
        }
    }
}