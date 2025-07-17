package org.ro.to {
import org.ro.core.model.Adaptable;
import org.ro.core.model.ObjectAdapter;

dynamic public class TObject extends TitledTO implements Adaptable {
    public var domainType:String;
    public var instanceId:uint;

    public function TObject(jsonObj:Object = null) {
        if (jsonObj != null) {
            this.fromJSON(jsonObj);
            init();
        }
    }

    override protected function init():void {
        super.init();
    }

    public function getId():String {
        return domainType + "/" + instanceId;
    }

    public function getProperties():Vector.<Invokeable> {
        var result:Vector.<Invokeable> = new Vector.<Invokeable>();
        for each(var m:Member in memberList) {
            if (m.memberType == Member.PROPERTY) {
                result.push(m);
            }
        }
        return result;
    }

    /**
     * Post-Constructor function using dynamic nature of class.
     */
    //TODO reduce visibility to internal
    public function addMembersAsProperties():void {
        var members:Vector.<Invokeable> = getProperties();
        for each(var m:Member in members) {
            if (m.getMemberType() == Member.PROPERTY) {
                addAsProperty(this, m);
            }
        }
    }

    private static function addAsProperty(dynObj:TObject, property:Member):void {
        var attribute:Object = null;
        var value:Object = property.getValue();
        if (value != null) {
            var typeSpec:Class = property.getType();
            attribute = new typeSpec(value);
        }
        // if value={} (ie. of class Object), 
        // it is represented as [object Object] 
        if (value == "[object Object]") {
            var link:Link = new Link(value);
            //here the magic of recursive OA's take place
            attribute = new ObjectAdapter(link, link.getTitle(), "Link");
        }
        var key:String = property.getId();
        dynObj[key] = attribute;
    }

}
}