package components.actionstore{

import uidocument.commons.api.document.Property;

public interface IActionStore {
    function getBehavior (trigger:String):Action;
    function addBehavior (action:Action):void;
    function removeBehavior (trigger:String):void;
}
}