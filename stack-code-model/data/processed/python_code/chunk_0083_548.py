package writer {

import uidocument.commons.api.document.*;

public class PropertyWriter {



    public function PropertyWriter() {

    }

    public function processProperties(action:Action, bProperties:Property):XML {
        var xml:XML = new XML(<Event/>);
        xml.@id=action.getId();
        for (var i:Number = 0; i < bProperties.getLength(); i++) {
            xml.appendChild(<Property/>);
            xml.Property[i].@name = bProperties.getProperty(i)[0];
            xml.Property[i].@value = bProperties.getProperty(i)[1];
        }
        return xml;
    }

}
}