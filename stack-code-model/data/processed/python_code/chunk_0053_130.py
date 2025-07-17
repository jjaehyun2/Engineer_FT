package reader{

import uidocument.commons.api.document.*;

public class InterfacesReader extends PropertiesReader {

    public function InterfacesReader(dReader:UIDocumentReader) {
        super(dReader);
    }

    public function processInterface(xml:XML):Interface {
        var iface:Interface = DocumentObjectFactory.createInterface(xml);
        iface.setRoot(processContainer(xml.children()[0]));
        return iface;
    }

    private function processContainer(xml:XML):Container {
        var container:Container = DocumentObjectFactory.createContainer(xml.children()[0]);
        setElement(xml, container);
        fillContainer(container, xml);
        return container;
    }

    private function fillContainer(container:Container, xml:XML):void {
        for (var i:Number = 0; i < xml.children().length(); i++) {
            container.add(processElement(xml.children()[i]));
        }
    }

    private function processElement(xml:XML):Element {
        var element:Element = DocumentObjectFactory.createElement(xml);
        setElement(xml, element);
        return element;
    }

    private function setElement(xml:XML, element:Element):void {
        
        element.setPosition(processPosition(xml));
        element.setStyle(processStyle(xml));
        element.addBehavior(processBehavior(xml));
        if (xml.@model.length() != 0) {
            element.setProperties(getPropertyFromModel(xml.@model));
        } else {
            element.setProperties(processProperties(xml));
        }
    }

    private function processPosition(xml:XML):Position {
        if (xml.position.length() == 1)
            return DocumentObjectFactory.createPosition(xml.position[0], processProperties(xml.position[0]));
        else
            return null;
    }

    private function processStyle(xml:XML):Style {
        if (xml.style.length() == 1)
            return DocumentObjectFactory.createStyle(xml.style[0]);
        else
            return null;
    }

    private function processBehavior(xml:XML):Behavior {
        if (xml.behavior.length() == 1) {
            return DocumentObjectFactory.createBehavior(xml.behavior[0], processProperties(xml.behavior[0]));
        }
        else
            return null;
    }

}
}