package reader{

import uidocument.commons.api.document.*;

import writer.UIDocumentWriter;

public class UIDocumentReader {

    private var document:UIDocument;
    private var display:Display;
    private var aReader:ActionsReader;
    private var eReader:EventsReader;
    private var iReader:InterfacesReader;
    private var mReader:ModelsReader;

    public function UIDocumentReader(display:Display, connection:UIClientConnection) {
        this.document = DocumentObjectFactory.createUIDocument();
        this.display = display;
        display.init(new UIDocumentWriter(document, connection))
        this.aReader = new ActionsReader(this);
        this.eReader = new EventsReader(this);
        this.iReader = new InterfacesReader(this);
        this.mReader = new ModelsReader(this);
    }

    public function processDocument(xmlIn:XML):void {
        //if (document.getInterfaces().length == 0) 
            processMainContainer(xmlIn);
    }

    private function processMainContainer(xmlIn:XML):void {
        var mContainer:XML = xmlIn.models[0];
        for (var i:Number = 0; i < mContainer.children().length(); i++) {
            document.addModelUpdate(mReader.processModel(mContainer.children()[i]));
        }
        UIClient.debug("Models processed\n");

        var iContainer:XML = xmlIn.interfaces[0];
        for (var j:Number = 0; j < iContainer.children().length(); j++) {
            document.addInterface(iReader.processInterface(iContainer.children()[j]));
        }
        UIClient.debug("Elements processed\n");

        var aContainer:XML = xmlIn.actions[0];
        for (var k:Number = 0; k < aContainer.children().length(); k++) {
            document.addAction(aReader.processAction(aContainer.children()[k],processModel(aContainer.children()[k])));
        }
        UIClient.debug("Actions processed\n");

        display.displayInterface(document.getInterfaces()[0]);
    }

    public function processModel(xml:XML):ModelUpdate {
        return mReader.processModel(xml);

    }

    public function findAction(action:String):Action {
        var actions:Array = document.getActions();
        for (var i:Number = 0; i < actions.length; i++) {
            if (actions[i].getId() == action)
                return actions[i];
        }
        return null;
    }

    public function findEvent(event:String):Event {
        var events:Array = document.getEvents();
        for (var i:Number = 0; i < events.length; i++) {
            if (events[i].getId() == event)
                return events[i];
        }
        return null;
    }

    public function findInterface(iface:String):Interface {
        var interfaces:Array = document.getInterfaces();
        for (var i:Number = 0; i < interfaces.length; i++) {
            if (interfaces[i].getId() == iface)
                return interfaces[i];
        }
        return null;
    }

    public function findModel(model:String):ModelUpdate {
        var models:Vector.<ModelUpdate> = document.getModelUpdates();
        for (var i:Number = 0; i < models.length; i++) {
            if (models[i].getId() == model)
                return models[i];
        }
        return null;
    }

}
}