//
// $Id$

package com.threerings.msoy.data {

import com.threerings.io.ObjectInputStream;

import com.threerings.util.Comparators;
import com.threerings.util.Name;

import com.threerings.presents.dobj.DSet;

import com.threerings.crowd.data.BodyObject;
import com.threerings.crowd.data.TokenRing;

import com.threerings.msoy.data.all.ContactEntry;
import com.threerings.msoy.data.all.GroupName;
import com.threerings.msoy.data.all.MemberMailUtil;
import com.threerings.msoy.data.all.MemberName;
import com.threerings.msoy.data.all.PlayerEntry;
import com.threerings.msoy.data.all.VisitorInfo;
import com.threerings.msoy.data.all.VizMemberName;
import com.threerings.msoy.game.data.GameSummary;
import com.threerings.msoy.group.data.all.GroupMembership;
import com.threerings.msoy.group.data.all.GroupMembership_Rank;
import com.threerings.msoy.item.data.all.Avatar;
import com.threerings.msoy.room.data.Track;

/**
 * Represents a connected msoy user.
 */
public class MemberObject extends BodyObject
{
    MsoyAuthName; // filled into username

    /** The field name of the <code>memberName</code> field. */
    public static const MEMBER_NAME :String = "memberName";

    /** The field name of the <code>following</code> field. */
    public static const FOLLOWING :String = "following";

    /** The field name of the <code>followers</code> field. */
    public static const FOLLOWERS :String = "followers";

    /** The field name of the <code>coins</code> field. */
    public static const COINS :String = "coins";

    /** The field name of the <code>bars</code> field. */
    public static const BARS :String = "bars";

    /** The field name of the <code>level</code> field. */
    public static const LEVEL :String = "level";

    /** The field name of the <code>tokens</code> field. */
    public static const TOKENS :String = "tokens";

    /** The field name of the <code>homeSceneId</code> field. */
    public static const HOME_SCENE_ID :String = "homeSceneId";

    /** The field name of the <code>theme</code> field. */
    public static const THEME :String = "theme";

    /** The field name of the <code>avatar</code> field. */
    public static const AVATAR :String = "avatar";

    /** The field name of the <code>avatarCache</code> field. */
    public static const AVATAR_CACHE :String = "avatarCache";

    /** The field name of the <code>friends</code> field. */
    public static const FRIENDS :String = "friends";

    /** The field name of the <code>gateways</code> field. */
    public static const GATEWAYS :String = "gateways";

    /** The field name of the <code>aimContacts</code> field. */
    public static const IM_CONTACTS :String = "imContacts";

    /** The field name of the <code>groups</code> field. */
    public static const GROUPS :String = "groups";

    /** The field name of the <code>newMailCount</code> field. */
    public static const NEW_MAIL_COUNT :String = "newMailCount";

    /** The field name of the <code>game</code> field. */
    public static const GAME :String = "game";

    /** The field name of the <code>walkingId</code> field. */
    public static const WALKING_ID :String = "walkingId";

    /** The field name of the <code>headline</code> field. */
    public static const HEADLINE :String = "headline";

    /** The field name of the <code>visitorInfo</code> field. */
    public static const VISITOR_INFO :String = "visitorInfo";

    /** The field name of the <code>onTour</code> field. */
    public static const ON_TOUR :String = "onTour";

    /** The field name of the <code>partyId</code> field. */
    public static const PARTY_ID :String = "partyId";

    /** The field name of the <code>experiences</code> field. */
    public static const EXPERIENCES :String = "experiences";

    /** A message sent by the server to denote a notification to be displayed.
     * Format: [ Notification ]. */
    public static const NOTIFICATION :String = "notification";

    public static const TRACKS :String = "tracks";

    /** The member name and id for this user. */
    public var memberName :VizMemberName;

    /** The current state of the body's actor, or null if unset/unknown/default. */
    public var actorState :String;

    /** How many coins we've got jangling around on our person. */
    public var coins :int;

    /** How many bars total this member has. */
    public var bars :int;

    /** This user's current level. */
    public var level :int;

    /** The name of the member this member is following or null. */
    public var following :MemberName;

    /** The names of members following this member. */
    public var followers :DSet;

    /** The tokens defining the access controls for this user. */
    public var tokens :MsoyTokenRing;

    /** The id of the user's home scene. */
    public var homeSceneId :int;

    /** The definition of the theme this member is currently in, or null. */
    public var theme :GroupName;

    /** The avatar that the user has chosen, or null for guests. */
    public var avatar :Avatar;

    /** A cache of the user's 5 most recently touched avatars. */
    public var avatarCache :DSet;

    /** The online friends of this player. */
    public var friends :DSet;

    /** The IM gateways available to this player. */
    public var gateways :DSet;

    /** The IM contacts of this player. */
    public var imContacts :DSet;

    /** The groups of this player. */
    public var groups :DSet;

    /** A field that contains the number of unread messages in our mail inbox. */
    public var newMailCount :int;

    /* The game summary for the game that the player is lobbying for or currently playing. */
    public var game :GameSummary;

    /** If this member is currently walking a pet, the id of the pet being walked, else 0. */
    public var walkingId :int;

    /** The headline/status of this player. */
    public var headline :String;

    /** Player's tracking information. */
    public var visitorInfo :VisitorInfo;

    /** Whether this player is on the "whirled tour". */
    public var onTour :Boolean;

    /** The player's current partyId, or 0 if they're not in a party. */
    public var partyId :int;

    /** Experiences this player has had. */
    public var experiences :DSet; /* of */ MemberExperience;

    /** If this player is DJ-ing, the songs they have queued up. */
    public var tracks :DSet; /* of */ Track;

    /**
     * Return this member's unique id.
     */
    public function getMemberId () :int
    {
        return memberName.getId();
    }

    /**
     * Returns true if this user is a permaguest.
     */
    public function isPermaguest () :Boolean
    {
        return MemberMailUtil.isPermaguest(username.toString());
    }

    /**
     * Returns true if this member is away.
     */
    public function isAway () :Boolean
    {
        return (awayMessage != null);
    }

    /**
     * Return true if this user is only viewing the scene and should not be rendered within it.
     */
    public function isViewer () :Boolean
    {
        return memberName.isViewer();
    }

    /**
     * Returns our home scene id if we're a member, 1 if we're a guest.
     */
    public function getHomeSceneId () :int
    {
        return (homeSceneId == 0) ? 1 : homeSceneId;
    }

    /**
     * Get a sorted list of friends.
     */
    public function getSortedFriends () :Array
    {
        return friends.toArray().sort(PlayerEntry.sortByName);
    }

    /**
     * Get a sorted list of groups we're a member of.
     */
    public function getSortedGroups () :Array
    {
        return groups.toArray().sort(GroupMembership.sortByName);
    }

    /**
     * Get a sorted list of gateways.
     */
    public function getSortedGateways () :Array
    {
        return gateways.toArray().sort(Comparators.compareComparables);
    }

    /**
     * Get a sorted list of aim contacts for a specified gateway.
     */
    public function getSortedImContacts (gateway :String) :Array
    {
        var contacts :Array = imContacts.toArray();
        contacts = contacts.filter(
            function (ce :ContactEntry, ... ignored) :Boolean {
                return ce.getGateway() == gateway;
            });
        return contacts.sort(Comparators.compareComparables);
    }

    // documentation inherited
    override public function getTokens () :TokenRing
    {
        return tokens;
    }

    override public function getVisibleName () :Name
    {
        return memberName;
    }

    /**
     * Convenience.
     */
    public function isOnlineFriend (memberId :int) :Boolean
    {
        return friends.containsKey(memberId);
    }

    /**
     * Is this user a member of the specified group?
     */
    public function isGroupMember (groupId :int) :Boolean
    {
        return isGroupRank(groupId, GroupMembership_Rank.MEMBER);
    }

    /**
     * Is this user a manager in the specified group?
     */
    public function isGroupManager (groupId :int) :Boolean
    {
        return isGroupRank(groupId, GroupMembership_Rank.MANAGER);
    }

    /**
     * @return true if the user has at least the specified rank in the
     * specified group.
     */
    public function isGroupRank (groupId :int, requiredRank :GroupMembership_Rank) :Boolean
    {
        return getGroupRank(groupId).compareTo(requiredRank) >= 0;
    }

    /**
     * Get the user's rank in the specified group.
     */
    public function getGroupRank (groupId :int) :GroupMembership_Rank
    {
        if (groups != null) {
            var membInfo :GroupMembership = (groups.get(groupId) as GroupMembership);
            if (membInfo != null) {
                return membInfo.rank;
            }
        }
        return GroupMembership_Rank.NON_MEMBER;
    }

    override public function readObject (ins :ObjectInputStream) :void
    {
        super.readObject(ins);

        memberName = VizMemberName(ins.readObject());
        actorState = (ins.readField(String) as String);
        coins = ins.readInt();
        bars = ins.readInt();
        level = ins.readInt();
        following = MemberName(ins.readObject());
        followers = DSet(ins.readObject());
        tokens = MsoyTokenRing(ins.readObject());
        homeSceneId = ins.readInt();
        theme = GroupName(ins.readObject());
        avatar = Avatar(ins.readObject());
        avatarCache = DSet(ins.readObject());
        friends = DSet(ins.readObject());
        gateways = DSet(ins.readObject());
        imContacts = DSet(ins.readObject());
        groups = DSet(ins.readObject());
        newMailCount = ins.readInt();
        game = GameSummary(ins.readObject());
        walkingId = ins.readInt();
        headline = ins.readField(String) as String;
        visitorInfo = VisitorInfo(ins.readObject());
        onTour = ins.readBoolean();
        partyId = ins.readInt();
        experiences = DSet(ins.readObject());
        tracks = DSet(ins.readObject());
    }
}
}