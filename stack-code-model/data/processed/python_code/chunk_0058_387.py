package com.macys.marketing.sema.view.event
{
    
import flash.events.Event;    
    
public class ReplicateEvent extends Event
{
    public static const REPLICATE_EVENT:String = "replicateEvent";
    
    public static const AD_GROUPS_CHANGED:String = "adGroupsChanged";
    public static const AD_COPY_CHANGED:String = "adCopyChanged";
    public static const AD_KEYWORD_CHANGED:String = "adKeywordChanged";
    
    protected var _key:*;
    protected var _value:*;

    public function ReplicateEvent(key:*=null, value:*=null)
    {
        super(ReplicateEvent.REPLICATE_EVENT, false, true);
        _key = key;
        _value = value;
    }
    
    public function get key():*
    {
        return _key;
    }
    
    public function set key(value:*):void
    {
        _key = value;
    }
    
    public function get value():*
    {
        return _value;
    }
    
    public function set value(value:*):void
    {
        _value = value;
    }
}
}