package org.ro.to {
dynamic public class Property extends Member {
    public static const FRIENDLY_NAME:String = "friendlyName";
    public static const DESCRIBED_BY:String = "describedby";
    public static const RETURN_TYPE:String = "urn:org.restfulobjects:rels/return-type";

    internal var parameters:Object;
    internal var maxLength:uint;

    public function Property(jsonObj:Object = null) {
        memberType = Member.PROPERTY;
        if (jsonObj != null) {
            this.fromJSON(jsonObj);
            init();
        }
    }

    override protected function init():void {
        super.init();
    }

    public function descriptionLink():Link {
        for each(var l:Link in linkList) {
            if (l.rel == DESCRIBED_BY)
                return l;
        }
        return null;
    }

}
}