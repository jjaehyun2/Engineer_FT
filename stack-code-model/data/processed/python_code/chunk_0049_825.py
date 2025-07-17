//
// $Id$

package com.threerings.msoy.room.client {

import com.threerings.msoy.data.all.MediaDescImpl;

/**
 * Hacktacular. Do not emulate. I should hide this class somewhere.
 */
public class StudioMediaDesc extends MediaDescImpl
{
    public function StudioMediaDesc (url :String)
    {
        _url = url;
    }

    // from MediaDesc
    override public function getMediaId () :String
    {
        return "studio";
    }

    // from EntityMedia
    override public function getMediaPath () :String
    {
        return _url;
    }

    // from MediaDesc
    override public function isBleepable () :Boolean
    {
        return false;
    }

    override public function equals (other :Object) :Boolean
    {
        return (other is StudioMediaDesc) &&
            (getMediaPath() == StudioMediaDesc(other).getMediaPath());
    }

    public function toString () :String
    {
        return "[StudioMediaDesc:" + _url + "]";
    }

    protected var _url :String;
}
}