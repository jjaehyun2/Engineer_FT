//@todo draw display
//@todo change initialization
//@todo TRACE
package {

import configuration.*;

import flash.events.*;

import mx.containers.Canvas;
import mx.controls.*;

import reader.*;

import writer.*;

public class UIClient extends Canvas {

    public static var textArea:TextArea;
    public static var display:Display;
    private var imageLoader:Image;
    private var connection:UIClientConnection;
    private static var currentDate:Date;

    private var dReader:UIDocumentReader;
    private var dWriter:UIDocumentWriter;

    private var cReader:ConfigurationReader;

    public function UIClient() {
        super();
        init();
    }

    private function init():void {

        cReader = ConfigurationReader.getInstance();
        cReader.init();
        display = new Display();
        loadImage();
        loadText();
        loadDisplay();

        function configurationLoadedHandler(e:Event):void {
            if (cReader.isLoaded()) {
                UIClient.debug("Configuration loaded");
                connection = new UIClientConnection(display);
                //UIClient.debug(cReader.toString());
            }
        }

        cReader.addEventListener(Event.COMPLETE, configurationLoadedHandler);

    }

    private function loadImage():void {
        imageLoader = new Image();
        imageLoader.x = 0;
        imageLoader.y = 0;
        imageLoader.load("iPhone-mini copy cut.png");
        addChild(imageLoader);

    }

    private function loadText():void {
        textArea = new TextArea();
        textArea.height = 550;
        textArea.width = 600;
        textArea.x = 395;
        textArea.y = 0;
        //textField.backgroundColor = 0x00FF00;
        //textField.background = true;
        //textField.scrollV = 1;
        addChild(textArea);
    }

    private function loadDisplay():Display {
        display.x = 35;
        display.y = 120;
        addChild(display);
        return display;

    }

    public static function debug(message:String):void {
        currentDate = new Date();
        textArea.text = textArea.text + "[" + currentDate.getHours() + ":" + currentDate.getMinutes() + ":" + currentDate.getSeconds() + "] " + message + "\n";
        trace("[" + currentDate.getHours() + ":" + currentDate.getMinutes() + ":" + currentDate.getSeconds() + "] " + message + "\n");
    }

}
}