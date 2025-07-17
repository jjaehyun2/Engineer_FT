//
// $Id$

package com.threerings.msoy.game.client {

import flash.events.Event;

import com.whirled.game.client.WhirledGameConfigurator;

import mx.containers.HBox;
import mx.containers.VBox;
import mx.controls.Label;
import mx.controls.TextInput;
import mx.core.Container;

import com.threerings.util.Log;

import com.threerings.parlor.client.TableConfigurator;
import com.threerings.parlor.data.RangeParameter;
import com.threerings.parlor.data.ToggleParameter;
import com.threerings.parlor.game.client.GameConfigurator;
import com.threerings.parlor.game.data.GameConfig;

import com.threerings.flex.CommandButton;
import com.threerings.flex.CommandCheckBox;
import com.threerings.flex.FlexUtil;

import com.threerings.msoy.client.Msgs;
import com.threerings.msoy.data.all.FriendEntry;
import com.threerings.msoy.game.data.LobbyObject;
import com.threerings.msoy.game.data.MsoyMatchConfig;
import com.threerings.msoy.game.data.ParlorGameConfig;
import com.threerings.msoy.party.client.PartyDirector;
import com.threerings.msoy.ui.SimpleGrid;

/**
 * Displays an interface for creating a new game table.
 */
public class TableCreationPanel extends VBox
{
    public function TableCreationPanel (ctx :GameContext, ctrl :LobbyController, lobj :LobbyObject)
    {
        _ctx = ctx;
        _ctrl = ctrl;
        _lobj = lobj;
    }

    protected function friendToggled (event :Event) :void
    {
        _inviteAll.selected = false;
//
//        // _inviteAll.selected = every friend box selected?
//        _inviteAll.selected = true;
//        for (var i :int = 0; i < _friendsGrid.numChildren; ++i) {
//            if ( ! (_friendsGrid.getCellAt(i) as FriendCheckBox).check.selected) {
//                _inviteAll.selected = false;
//                return;
//            }
//        }
    }

    protected function inviteAllToggled (selected :Boolean) :void
    {
        for (var i :int = 0; i < _friendsGrid.cellCount; ++i) {
            var fcb :FriendCheckBox = _friendsGrid.getCellAt(i) as FriendCheckBox;
            fcb.check.selected = selected;
        }
    }

    override protected function createChildren () :void
    {
        super.createChildren();
        styleName = "tableCreationPanel";

        const partyDir :PartyDirector = _ctx.getWorldContext().getPartyDirector();
        const isPartyLeader :Boolean = partyDir.isPartyLeader();

        var titleKey :String = isPartyLeader ? "t.create_party_table" : "t.create_table";
        addChild(FlexUtil.createLabel(Msgs.GAME.get(titleKey), "lobbyTitle"));

        // create our various game configuration bits but do not add them
        var rparam :ToggleParameter = new ToggleParameter();
        rparam.name = Msgs.GAME.get("l.rated");
        rparam.tip = Msgs.GAME.get("t.rated");
        rparam.start = true;
        var gconf :WhirledGameConfigurator = new WhirledGameConfigurator(rparam);
        gconf.setColumns(1);
        gconf.init(_ctx);

        // add a configuration for the table name (before we give the game
        var tableName :TextInput = new TextInput();
        tableName.text = Msgs.GAME.get("l.default_table", _ctx.getMyName());
        gconf.addControl(
            FlexUtil.createLabel(Msgs.GAME.get("l.table"), null, Msgs.GAME.get("i.table")),
            tableName);

        var plparam :RangeParameter = new RangeParameter();
        plparam.name = Msgs.GAME.get("l.players");
        plparam.tip = Msgs.GAME.get("t.players");
        var wparam :ToggleParameter = null;
        var pvparam :ToggleParameter = null;

        var match :MsoyMatchConfig = (_lobj.gameDef.match as MsoyMatchConfig);
        switch (match.getMatchType()) {
        case GameConfig.PARTY:
            // plparam stays with zeros
            // wparam stays null
            if (!isPartyLeader) {
                pvparam = new ToggleParameter();
                pvparam.name = Msgs.GAME.get("l.private");
                pvparam.tip = Msgs.GAME.get("t.private");
            }
            break;

        case GameConfig.SEATED_GAME:
            plparam.minimum = Math.max(
                Math.min(match.maxSeats, partyDir.getPartySize()), match.minSeats)
            plparam.maximum = match.maxSeats;
            plparam.start = match.maxSeats; // game creators don't configure start seats, so use
                                            // the max; they can always start the game early
            if (!match.unwatchable) {
                wparam = new ToggleParameter();
                wparam.name = Msgs.GAME.get("l.watchable");
                wparam.tip = Msgs.GAME.get("t.watchable");
                wparam.start = true;
            }
            // pvparam stays null
            break;

        default:
            log.warning("<match type='" + match.getMatchType() + "'> is not a valid type");
            return;
        }

        var tconfigger :TableConfigurator =
            new MsoyTableConfigurator(plparam, wparam, pvparam, tableName);
        tconfigger.init(_ctx, gconf);

        var config :ParlorGameConfig = new ParlorGameConfig();
        config.init(_lobj.game, _lobj.gameDef);
        gconf.setGameConfig(config);

        _configBox = gconf.getContainer();
        _configBox.percentWidth = 100;
        addChild(_configBox);

        // add an interface for inviting friends to play
        addChild(FlexUtil.createLabel(Msgs.GAME.get("l.invite_friends"), "lobbyTitle"));
        // TODO: turn this into an action label
        _inviteAll = new CommandCheckBox(Msgs.GAME.get("l.invite_all"), inviteAllToggled);
        _inviteAll.styleName = "lobbyLabel";
        // TODO: add with label to HBox

        var onlineFriends :Array = _ctx.getSortedFriends();
        if (onlineFriends.length == 0) {
            addChild(FlexUtil.createLabel(Msgs.GAME.get("l.invite_no_friends")));

        } else {
            _friendsGrid = new SimpleGrid(FRIENDS_GRID_COLUMNS);
            _friendsGrid.setStyle("horizontalGap", 5);
            for each (var friend :FriendEntry in onlineFriends) {
                try {
                    var fcb :FriendCheckBox = new FriendCheckBox(friend);
                    fcb.check.addEventListener(Event.CHANGE, friendToggled);
                    _friendsGrid.addCell(fcb);
                } catch (e :Error) {
                    log.warning("Failed to add checkbox for friend", "friend", friend, e);
                }
            }
            addChild(_friendsGrid);
        }

        // only show invite all if we have more than one friend to invite
        _inviteAll.visible = (onlineFriends.length > 1);

        // finally add buttons for create and cancel
        var bottomRow :HBox = new HBox();
        bottomRow.percentWidth = 100;
        bottomRow.setStyle("horizontalAlign", "right");
        bottomRow.addChild(new CommandButton(Msgs.GAME.get("b.cancel"), function () : void {
            _ctrl.panel.setMode(_ctrl.getStartMode(true));
        }));
        bottomRow.addChild(new CommandButton(Msgs.GAME.get("b.create"),
            createGame, [ tconfigger, gconf ]));
        addChild(bottomRow);
    }

    protected function createGame (tconf :TableConfigurator, gconf :GameConfigurator) :void
    {
        var invIds :Array = [];
        if (_friendsGrid != null) {
            for (var ii :int = 0; ii < _friendsGrid.cellCount; ii++) {
                var fcb :FriendCheckBox = (_friendsGrid.getCellAt(ii) as FriendCheckBox);
                if (fcb.check.selected) {
                    invIds.push(fcb.friend.name.getId());
                }
            }
        }
        _ctrl.handleSubmitTable(tconf.getTableConfig(), gconf.getGameConfig(), invIds);
    }

    protected var _ctx :GameContext;
    protected var _ctrl :LobbyController;
    protected var _lobj :LobbyObject;

    protected var _configBox :Container;
    protected var _friendsGrid :SimpleGrid;
    protected var _inviteAll :CommandCheckBox;

    protected const log :Log = Log.getLog(this);

    protected static const FRIENDS_GRID_COLUMNS :int = 4;
}
}

import flash.events.Event;
import flash.events.MouseEvent;

import mx.containers.VBox;
import mx.controls.CheckBox;
import mx.controls.Label;

import com.threerings.orth.data.MediaDescSize;
import com.threerings.orth.ui.MediaWrapper;

import com.threerings.flex.FlexUtil;

import com.threerings.msoy.data.all.FriendEntry;

class FriendCheckBox extends VBox
{
    public var friend :FriendEntry;
    public var check :CheckBox;

    public function FriendCheckBox (friend :FriendEntry)
    {
        styleName = "friendCheckBox";
        this.friend = friend;

        addChild(MediaWrapper.createView(friend.name.getPhoto(), MediaDescSize.HALF_THUMBNAIL_SIZE));
        var name :Label = FlexUtil.createLabel(friend.name.toString());
        name.maxWidth = 4*MediaDescSize.THUMBNAIL_WIDTH/5;
        addChild(name);
        addChild(check = new CheckBox());
        check.width = 14; // don't ask; go punch someone at adobe instead

        addEventListener(MouseEvent.CLICK, handleClick);
    }

    // allow all kinds of sloppy clicking to toggle the checkbox
    protected function handleClick (event :MouseEvent) :void
    {
        if (event.target != check) { // because the checkbox will have already handled it
            check.selected = !check.selected;
            check.dispatchEvent(new Event(Event.CHANGE));
        }
    }
}