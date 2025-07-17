package org.ro.to {
public class Service extends TitledTO {
    internal var value:Object;          //TODO clarify type of value
    internal var valueList:Vector.<Invokeable>;
    internal var serviceId:String;

    public function Service(jsonObj:Object = null) {
        if (jsonObj != null) {
            this.fromJSON(jsonObj);
            init();
        }
    }

    override protected function init():void {
        super.init();
        valueList = new Vector.<Invokeable>();
        for each(var v:Object in this.value) {
            valueList.push(new Link(v));
        }
    }

    public function getValues():Vector.<Invokeable> {
        return valueList;
    }

    public function getTitle():String {
        return title;
    }

    public function getServiceId():String {
        return serviceId;
    }

}
}