package writer {

import uidocument.commons.api.document.*;

public class EventsWriter extends PropertyWriter {

    private static var instance:EventsWriter;

    public function EventsWriter() {
        super();
    }

    public static function getInstance():EventsWriter {
        if (instance == null) {
            instance = new EventsWriter();
        }
        return instance;
    }

    public function writeEventXML (action:Action, bProperties:Property):XML {
        var xml:XML =  new XML(<UIProtocol version="1.0"/>);
        xml.appendChild(<events/>);
        xml.events.appendChild(processEvent(action, bProperties));
        return xml;
    }

    public function writeRequestXML (type:String, classes:Array):XML {
        var xml:XML =  new XML(<UIProtocol version="1.0"/>);
        xml.appendChild(<events/>);
        xml.events.appendChild(processRequest(type, classes));
        return xml;
    }

}
}