package top.yunp.embedjs {
    import org.apache.royale.utils.Language;

    public class Main {

        private static const IMPORTED_CLASSES:Array = [Language];

        [Embed(source = "Main.js", mimeType = "text/plain")]
        private static var jsContent:String

        public function Main() {

        }

        public function start():void {
            var f:Function = new Function(jsContent);
            f();
        }
    }
}