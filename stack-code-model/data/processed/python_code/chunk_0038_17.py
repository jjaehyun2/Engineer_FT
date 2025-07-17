package demo {

import com.roipeker.utils.adl.ScreenEmulator;
import com.roipeker.utils.adl.collections.DeviceBrands;
import com.roipeker.utils.adl.ui.DeviceUI;

import flash.display.BitmapData;
import flash.display.PNGEncoderOptions;
import flash.display.Sprite;
import flash.display.StageAlign;
import flash.display.StageScaleMode;
import flash.events.Event;
import flash.events.KeyboardEvent;
import flash.filesystem.File;
import flash.filesystem.FileMode;
import flash.filesystem.FileStream;
import flash.geom.Rectangle;
import flash.ui.Keyboard;
import flash.utils.ByteArray;
import flash.utils.setTimeout;

import starling.core.Starling;

// swf dimensions are irrelevant for ScreenEmulator :)
[SWF(width="800", height="600", backgroundColor="#232323", frameRate="60")]
public class Boot extends Sprite {

    private var starling:Starling;
    private var screen:ScreenEmulator;

    public function Boot() {
        stage.align = StageAlign.TOP_LEFT;
        stage.scaleMode = StageScaleMode.NO_SCALE;

        screen = ScreenEmulator.instance;
        screen.init(stage, -40, -40, true, ScreenEmulator.ORIENTATION_ANY);
        screen.emulate(DeviceBrands.apple.iphone_6_plus);

        loaderInfo.addEventListener(Event.COMPLETE, onLoaderInfoComplete);
    }

    private function onLoaderInfoComplete(event:Event):void {
        // For size arguments details, check screen.constrainADLSize()
        starling = new Starling(StarlingRoot, stage, screen.getViewPort());
        starling.stage.stageWidth = screen.stageWidthPoints;
        starling.stage.stageHeight = screen.stageHeightPoints;
        starling.supportHighResolutions = true;
        starling.start();
        starling.stage.color = 0xffffff;

        // this handler has to be called before Starling's stage.resize...
        // so put it before initializing starling, or set a high priority.
        // otherwise, Starling's stage will be 1 step behind.
        stage.addEventListener(Event.RESIZE, onStageResize, false, 1);
        stage.addEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
    }

    private function onKeyDown(event:KeyboardEvent):void {
        switch (event.keyCode) {
            case Keyboard.NUMBER_1:
                screen.emulate(DeviceBrands.apple.iphone_x);
                break;
            case Keyboard.NUMBER_2:
                screen.emulate(DeviceBrands.apple.iphone_6_plus);
                break;
            case Keyboard.NUMBER_3:
                screen.emulate(DeviceBrands.apple.iphone_5);
                break;
            case Keyboard.NUMBER_4:
                screen.emulate(DeviceBrands.apple.ipad_air_2);
                break;
            case Keyboard.NUMBER_5:
                screen.emulate(DeviceBrands.apple.ipad_pro_10_5_2017);
                break;
            case Keyboard.NUMBER_6:
                screen.emulate(DeviceBrands.apple.ipad_pro_12_9_2017);
                break;
            case Keyboard.NUMBER_7:
//                screen.emulate(DeviceBrands.google.pixel);
                screen.emulate(DeviceBrands.apple.ipad);
                break;
            case Keyboard.NUMBER_8:
                screen.emulate(DeviceBrands.htc.one);
                break;
            case Keyboard.NUMBER_9:
                screen.emulate(DeviceBrands.samsung.google_nexus_10_p8110);
                break;
            case Keyboard.NUMBER_0:
                screen.emulate(DeviceBrands.samsung.galaxy_note_3);
                break;
            case Keyboard.SPACE:
                if (stage.autoOrients) {
                    screen.isLandscape() ? screen.portrait() : screen.landscape();
                }
                break;
            case Keyboard.D:
                DeviceUI.instance.debugIPhoneXSize = !DeviceUI.instance.debugIPhoneXSize;
                break;
            case Keyboard.S:
                DeviceUI.instance.showStatusbar = !DeviceUI.instance.showStatusbar;
                break;
            case Keyboard.N:
                DeviceUI.instance.showNavbar = !DeviceUI.instance.showNavbar;
                break;
            case Keyboard.P:
                printScreen();
                break;
        }
    }

    /**
     * Useful to make iOS Splashscreens for multiple resolutions based on the initial screen
     * of your app.
     */
    private function printScreen():void {

        // width/height is adjusted to the orientation of ScreenEmulator.
        var tw:int = screen.deviceStageWidth;
        var th:int = screen.deviceStageHeight;

        DeviceUI.instance.visible = false;

        var viewport:Rectangle = starling.viewPort.clone();
        var scale:Number = starling.painter.backBufferScaleFactor;
        screen.resizeStage(tw / scale, th / scale);

        setTimeout(stageDimensionAdjusted, 50);

        function stageDimensionAdjusted() {
            var bd:BitmapData = new BitmapData(tw, th);
            starling.stage.drawToBitmapData(bd, starling.stage.color, 1);

            // todo: resolve splash screen names.
            var name:String = 'screenshot-' + new Date().toString() + '.png';
            var file:File = File.desktopDirectory.resolvePath(name);

            // save image to Desktop.
            var ba:ByteArray = new ByteArray();
            bd.encode(bd.rect, new PNGEncoderOptions(false), ba);
            var fs:FileStream = new FileStream();
            fs.open(file, FileMode.WRITE);
            fs.writeBytes(ba);
            fs.close();
            ba.clear();
            bd.dispose();

            DeviceUI.instance.visible = true;

            // roll back the stage dimensions.
            screen.resizeStage(viewport.width, viewport.height);
        }
    }

    private function onStageResize(event:Event):void {
        if (starling) {
            screen.getViewPort(starling.viewPort);
            starling.stage.stageWidth = screen.stageWidthPoints;
            starling.stage.stageHeight = screen.stageHeightPoints;
        }
    }
}
}