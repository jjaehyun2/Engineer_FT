package org.ro.view {
import flash.display.Shape;

import org.ro.core.event.LogEntry;

import spark.components.gridClasses.GridItemRenderer;
import spark.core.SpriteVisualElement;

public class BarRenderer extends GridItemRenderer {

    private var shape:Shape;

    public function BarRenderer() {
        super();
        shape = new Shape();
        var sve:SpriteVisualElement = new SpriteVisualElement();
        sve.addChild(shape);
        this.addElement(sve);
    }

    override public function set data(value:Object):void {
        var logEntry: LogEntry = value as LogEntry;
        var len:int = logEntry.duration;                          
        var color:uint = getColor(logEntry);
        var offset:int = logEntry.offset;
        shape.graphics.beginFill(color); 
        shape.graphics.drawRect(offset/10, 4, len/10, 16); // (x spacing, y spacing, width, height)
        shape.graphics.endFill(); 
    }

    /**
     * Calculate the length of the bar proportional to the length of the available space
     * @return
     */
    private function normalize():int{
        //TODO implement
        return 100;
    }
    
    private function getColor(logEntry:LogEntry):uint {
        var colorCode:String = getColorCode(logEntry);
        if (colorCode === "#C0504D") {
            return 0xC0504D; //red
        } else if (colorCode === "#F79646") {
            return 0xF79646; //orange 
        } else {
            return 0x9BBB59; // green
        }
    }

    private function getColorCode(logEntry:LogEntry):String {
        if (logEntry.fault != null) {
            return "#C0504D"; //red
        } else if (logEntry.duration == 0) {
            return "#F79646"; //orange 
        } else {
            return "#9BBB59"; // green
        }
    }
}
}