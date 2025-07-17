package {
public class XMLTools {

    private static var xmlIn:XML;

    public static function validateXML(xml:XML, string:String):XML {

        if (string.length < 54) return null;
        if (string.substr(0, 6) != "<?xml ") return null;
        if (string.indexOf(">", 24) > string.indexOf("<", 24) || string.indexOf(">") == -1) return null;
        if (string.indexOf("encoding") == -1 || string.indexOf("encoding") > string.indexOf(">", 24)) return null;
        xmlIn = new XML(string);
        if (xmlIn.localName().toString() != "UIProtocol") return null;
        if (xmlIn.attribute("version").length() == 0) return null;

        var xmlList:XMLList = xmlIn.children();

        for each (var n:XML in xmlList) {
            UIClient.debug(n.name);
            if (n.name() != "actions" && n.name() != "events" && n.name() != "interfaces" && n.name() != "models") return null;
        }

        return xmlIn;
    }
}
}