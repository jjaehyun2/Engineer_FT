package flash.display {


    public class Stage extends DisplayObjectContainer {


        public function Stage(width:uint, height:uint) {
            if (__locked) {
                throw new Error("Can not create instance of Stage");
            }
            htmlElement = document.createElement("div") as HTMLElement;
            htmlElement.style.position = "relative";
            htmlElement.style.width = width + "px";
            htmlElement.style.height = height + "px";
            htmlElement.style.overflow = 'hidden';
            htmlElement.style.perspective = "800px";
            htmlElement.style.perspectiveOrigin = "center";
        }

        private static var __locked:Boolean = true;

        internal static function createStage(width:uint = 550, height:uint = 400):Stage {
            __locked = false;
            var s:Stage = new Stage(width, height);
            __locked = true;
            return s;
        }

        override public function get stage():Stage {
            return this;
        }
    }
}