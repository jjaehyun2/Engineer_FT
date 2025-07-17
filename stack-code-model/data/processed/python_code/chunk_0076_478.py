package com.wazooinc
{
    import flash.display.Sprite;
    import flash.events.Event;

    [SWF(width = '640', height = '480')]
    public class Main extends Sprite {

        public function Main() {

            super();

            this.addEventListener(Event.ADDED_TO_STAGE, onAddToStage);

        }

        public function onAddToStage(e:Event): void {
            this.removeEventListener(Event.ADDED_TO_STAGE, onAddToStage);
            this.stage.color = 0xee00ff;
        }
    }
}