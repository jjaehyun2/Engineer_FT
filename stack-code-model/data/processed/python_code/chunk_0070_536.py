//
// $Id$

package com.threerings.msoy.item.data.all {

import com.threerings.io.ObjectInputStream;
import com.threerings.io.ObjectOutputStream;

import com.threerings.util.ByteEnum;

import com.threerings.msoy.data.all.StaticMediaDesc;

/**
 * Provides an item's default media.
 */
public class DefaultItemMediaDesc extends StaticMediaDesc
{
    public function DefaultItemMediaDesc (
        mimeType :int = 0, itemType :int = 0 /* ItemTypes.NOT_A_TYPE - WTFF Mr. Compiler? */,
        mediaType :String = null, constraint :int = NOT_CONSTRAINED)
    {
        super(mimeType, itemType == ItemTypes.NOT_A_TYPE ? null : Item.getTypeName(itemType),
              mediaType, constraint);
        _itemTypeCode = itemType;
    }

    // documentation inherited from interface Streamable
    override public function readObject (ins :ObjectInputStream) :void
    {
        super.readObject(ins);
        _itemTypeCode = MsoyItemType(ins.readObject()).toByte();
    }

    // documentation inherited from interface Streamable
    override public function writeObject (out :ObjectOutputStream) :void
    {
        super.writeObject(out);
        out.writeObject(ByteEnum.fromByte(MsoyItemType, _itemTypeCode));
    }

    protected var _itemTypeCode :int;
}
}