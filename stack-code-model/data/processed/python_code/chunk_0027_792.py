//
// $Id$

// GENERATED PREAMBLE START
package com.threerings.msoy.room.data {

import com.threerings.io.ObjectInputStream;
import com.threerings.io.ObjectOutputStream;

import com.threerings.msoy.data.all.MemberName;
import com.threerings.msoy.data.all.VizMemberName;
import com.threerings.msoy.room.data.Track;

// GENERATED PREAMBLE END

// GENERATED CLASSDECL START
public class RecentTrack extends Track
{
// GENERATED CLASSDECL END

// GENERATED STREAMING START
    public var dj :VizMemberName;

    public var rating :int;

    override public function readObject (ins :ObjectInputStream) :void
    {
        super.readObject(ins);
        dj = ins.readObject(VizMemberName);
        rating = ins.readInt();
    }

    override public function writeObject (out :ObjectOutputStream) :void
    {
        super.writeObject(out);
        out.writeObject(dj);
        out.writeInt(rating);
    }

// GENERATED STREAMING END

    override public function getKey () :Object
    {
        return order;
    }

// GENERATED CLASSFINISH START
}
}
// GENERATED CLASSFINISH END