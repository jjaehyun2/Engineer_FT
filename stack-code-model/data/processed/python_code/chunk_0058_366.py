//@todo edit functions
//@todo create event
package uidocument{

import uidocument.commons.api.document.*;
import flash.utils.getDefinitionByName;

public class DocumentObjectFactory {
    public static function createVariant():Variant {
        return new Variant();
    }

    public static function createPosition(xml:XML, property:Property):Position {
        return new Position(property);
    }

    public static function createBehavior(xml:XML, property:Property):Behavior {
        return new Behavior(xml.@trigger, xml.@action, property);
    }

    public static function createProperty():Property {
        return new Property();
    }

    public static function createModelUpdate(xml:XML):ModelUpdate {
        return new ModelUpdate(xml.@id);
    }

    public static function createInterface(xml:XML):Interface {
        return new Interface(xml.@id);
    }

    public static function createContainer(xml:XML):Container {
        return new Container(xml.@id);
    }

    public static function createElement(xml:XML):Element {
        return new Element(xml.attributes()[0]);
    }

    public static function createStyle(xml:XML):Style {
        return new Style(xml.@model);
    }

    public static function createAction(xml:XML):Action {
        return new Action(xml.@id, xml.@execution);
    }

    public static function createUIDocument():UIDocument {
        return new UIDocument();
    }
}
}