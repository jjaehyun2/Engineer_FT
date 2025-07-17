//
// $Id$

package com.threerings.msoy.room.data {

import com.threerings.io.ObjectInputStream;

import com.threerings.util.Joiner;

import com.threerings.msoy.data.MsoyUserOccupantInfo;
import com.threerings.msoy.data.all.MemberName;
import com.threerings.msoy.game.data.GameSummary;
import com.threerings.msoy.party.data.PartyOccupantInfo;

/**
 * Contains published information about a member in a scene.
 */
public class MemberInfo extends ActorInfo
    implements MsoyUserOccupantInfo, PartyOccupantInfo
{
    /**
     * Get the member id for this user, or 0 if they're a guest.
     */
    public function getMemberId () :int
    {
        return (username as MemberName).getId();
    }

    /**
     * Returns information on a game this user is currently lobbying or playing.
     */
    public function getGameSummary () :GameSummary
    {
        return _game;
    }

    /**
     * Return the scale that should be used for the media.
     */
    public function getScale () :Number
    {
        return _scale;
    }

    /**
     * Update the scale. This method currently only exists on the actionscript side.  We update the
     * scale immediately when someone is futzing with the scale in the avatar viewer.
     */
    public function setScale (scale :Number) :void
    {
        _scale = scale;
    }

    /**
     * Tests if this member is able to manage the room.
     * Note that this is not a definitive check, but rather one that can be used by clients
     * to check other occupants. The value is computed at the time the occupant enters the
     * room, and is not recomputed even if the room ownership changes. The server should
     * continue to do definitive checks where it matters.
     */
    public function isManager () :Boolean
    {
        return (_flags & MANAGER) != 0;
    }

    /**
     * Returns true if this member is away, false otherwise.
     */
    public function isAway () :Boolean
    {
        return (_flags & AWAY) != 0;
    }

    // from PartyOccupantInfo
    public function getPartyId () :int
    {
        return _partyId;
    }

    // from MsoyUserOccupantInfo
    public function isSubscriber () :Boolean
    {
        return (_flags & SUBSCRIBER) != 0;
    }

    // from ActorInfo
    override public function clone () :Object
    {
        var that :MemberInfo = super.clone() as MemberInfo;
        that._scale = this._scale;
        that._game = this._game;
        that._partyId = this._partyId;
        return that;
    }

    // from ActorInfo
    override public function readObject (ins :ObjectInputStream) :void
    {
        super.readObject(ins);
        _scale = ins.readFloat();
        _game = GameSummary(ins.readObject());
        _partyId = ins.readInt();
    }

    /** @inheritDoc */
    // from SimpleStreamableObject
    override protected function toStringJoiner (j :Joiner): void
    {
        super.toStringJoiner(j);
        j.add("scale", _scale, "game", _game, "partyId", _partyId);
    }

    protected var _scale :Number;
    protected var _game :GameSummary;
    protected var _partyId :int;
}
}