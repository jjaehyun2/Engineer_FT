package org.ro.to {

import org.flexunit.Assert;

public class ActionPOSTDeleteTest {
    public function ActionPOSTDeleteTest() {
    }

    [Test(description="parse result of invoking url")]
    public function testParseService():void {
        var actual:Action = new Action(json);
        var links:Vector.<Link> = actual.getLinks();
        Assert.assertEquals(4, links.length);
    }

    // http://localhost:8080/restful/objects/simple.SimpleObject/40/actions/delete
    private var json:Object = {
        "id": "delete",
        "memberType": "action",
        "links": [
            {
                "rel": "self",
                "href": "http://localhost:8080/restful/objects/simple.SimpleObject/40/actions/delete",
                "method": "GET",
                "type": "application/json;profile=\"urn:org.restfulobjects:repr-types/object-action\""
            },
            {
                "rel": "up",
                "href": "http://localhost:8080/restful/objects/simple.SimpleObject/40",
                "method": "GET",
                "type": "application/json;profile=\"urn:org.restfulobjects:repr-types/object\"",
                "title": "Object: Foo"
            },
            {
                "rel": "urn:org.restfulobjects:rels/invoke;action=\"delete\"",
                "href": "http://localhost:8080/restful/objects/simple.SimpleObject/40/actions/delete/invoke",
                "method": "POST",
                "type": "application/json;profile=\"urn:org.restfulobjects:repr-types/object-action\"",
                "arguments": {}
            },
            {
                "rel": "describedby",
                "href": "http://localhost:8080/restful/domain-types/simple.SimpleObject/actions/delete",
                "method": "GET",
                "type": "application/json;profile=\"urn:org.restfulobjects:repr-types/action-description\""
            }
        ],
        "extensions": {
            "actionType": "user",
            "actionSemantics": "nonIdempotentAreYouSure"
        },
        "parameters": {}
    };

}
}