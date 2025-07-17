//
// $Id$

package com.threerings.msoy.chat.client {

import flash.utils.getTimer;

import com.whirled.ui.PlayerList;

import com.threerings.util.ClassUtil;
import com.threerings.util.Log;
import com.threerings.util.MessageBundle;
import com.threerings.util.Name;
import com.threerings.util.Throttle;

import com.threerings.presents.client.Client;
import com.threerings.presents.client.ClientEvent;
import com.threerings.presents.client.InvocationAdapter;
import com.threerings.presents.client.ResultAdapter;

import com.threerings.crowd.chat.client.ChannelSpeakService;
import com.threerings.crowd.chat.client.ChatDirector;
import com.threerings.crowd.chat.client.SpeakService;
import com.threerings.crowd.chat.data.ChannelSpeakMarshaller;
import com.threerings.crowd.chat.data.ChatChannel;
import com.threerings.crowd.chat.data.ChatCodes;
import com.threerings.crowd.chat.data.ChatMessage;
import com.threerings.crowd.chat.data.SystemMessage;
import com.threerings.crowd.chat.data.TellFeedbackMessage;
import com.threerings.crowd.chat.data.UserMessage;
import com.threerings.crowd.data.PlaceObject;

import com.threerings.msoy.chat.client.JabberService;
import com.threerings.msoy.chat.data.JabberMarshaller;
import com.threerings.msoy.chat.data.MsoyChatChannel;
import com.threerings.msoy.client.Msgs;
import com.threerings.msoy.client.MsoyContext;
import com.threerings.msoy.data.MemberObject;
import com.threerings.msoy.data.MsoyCodes;
import com.threerings.msoy.data.PrimaryPlace;
import com.threerings.msoy.data.all.ChannelName;
import com.threerings.msoy.data.all.GroupName;
import com.threerings.msoy.data.all.JabberName;
import com.threerings.msoy.data.all.MemberName;
import com.threerings.msoy.data.all.RoomName;
import com.threerings.msoy.room.data.RoomObject;

/**
 * Handles the dispatching of chat messages based on their "channel" (room/game, individual, or
 * actual custom channel). Manages chat history tracking for same.
 */
public class MsoyChatDirector extends ChatDirector
{
    /** The maximum size of any utterance. */
    public static const MAX_CHAT_LENGTH :int = 200;

    // statically reference classes we require
    JabberMarshaller;
    ChannelSpeakMarshaller;

    public function MsoyChatDirector (ctx :MsoyContext)
    {
        super(ctx, ctx.getMessageManager(), MsoyCodes.CHAT_MSGS);
        _mctx = ctx;

        registerCommandHandler(Msgs.CHAT, "away", new AwayHandler());
        registerCommandHandler(Msgs.CHAT, "bleepall", new BleepAllHandler());

        // override the broadcast command from ChatDirector
        registerCommandHandler(Msgs.CHAT, "broadcast", new MsoyBroadcastHandler());

        // Ye Olde Easter Eggs
        registerCommandHandler(Msgs.CHAT, "~egg", new HackHandler(function (args :String) :void {
            _handlers.remove("~egg");
            _mctx.getControlBar().setFullOn();
            SubtitleGlyph.thumbsEnabled = true;
            displayFeedback(null, MessageBundle.taint("Easter eggs enabled:\n" +
                " * Full-screen button (no chat, due to flash security).\n" +
                " * Chat link hover pics.\n" +
                "\n" +
                "These experimental features may be removed in the future. Let us know if you " +
                "find them incredibly useful."));
        }));

        registerCommandHandler(Msgs.CHAT, "wipe", new WipeHandler());

        addChatDisplay(_chatHistory = new HistoryList(this));

        // create our room occupant list
        _roomOccList = new RoomOccupantList(_mctx);
    }

    /**
     * Whoever creates the chat tab bar is responsible for setting it here, so that we can properly
     * handle chat channels.
     */
    public function setChatTabs (tabs :ChatTabBar) :void
    {
        _chatTabs = tabs;
        addChatDisplay(_chatTabs);
    }

    /**
     * Get the currently-selected chat channel, or null if none.
     */
    public function getCurrentChannel () :MsoyChatChannel
    {
        return _chatTabs.getCurrentChannel();
    }

    /**
     * Get the localType of the currently-selected tab.
     */
    public function getCurrentLocalType () :String
    {
        var channel :MsoyChatChannel = getCurrentChannel();
        return (channel == null) ? ChatCodes.PLACE_CHAT_TYPE : channel.toLocalType();
    }

    /**
     * Our parent's clearDisplays() method will only clear the current channel.
     */
    public function clearAllDisplays () :void
    {
        _chatHistory.clearAll();
        clearDisplays();
    }

    /**
     * Retrieve the global chat history that contains every message received on this client,
     * within a history list size limit.
     */
    public function getHistoryList () :HistoryList
    {
        return _chatHistory;
    }

    /**
     * Return true if we've already got a chat channel open with the specified Name.
     */
    public function hasOpenChannel (name :Name) :Boolean
    {
        return _chatTabs.containsTab(makeChannel(name));
    }

    /**
     * Opens the chat interface for the supplied player, group or private chat channel, selecting
     * the appropriate tab if said channel is already open.
     *
     * @param name either a MemberName, GroupName, ChannelName or RoomName.
     */
    public function openChannel (name :Name) :void
    {
        _chatTabs.openChannelTab(makeChannel(name), true);
    }

    /**
     * Registers a user with an IM gateway and logs them in for chatting.
     */
    public function registerIM (gateway :String, username :String, password :String) :void
    {
        var svc :JabberService = (_mctx.getClient().requireService(JabberService) as JabberService);
        svc.registerIM(gateway, username, password, new InvocationAdapter(
            function (cause :String) :void {
                var msg :String = MessageBundle.compose(
                    "e.im_register_failed", "m." + gateway, cause);
                _mctx.displayFeedback(MsoyCodes.CHAT_MSGS, msg);
            }));
    }

    /**
     * Unregisters a user with an IM gateway, effectively logging them off.
     */
    public function unregisterIM (gateway :String) :void
    {
        var svc :JabberService = (_mctx.getClient().requireService(JabberService) as JabberService);
        svc.unregisterIM(gateway, new InvocationAdapter(
            function (cause :String) :void {
                var msg :String = MessageBundle.compose(
                    "e.im_unregister_failed", "m." + gateway, MessageBundle.taint(cause));
                _mctx.displayFeedback(MsoyCodes.CHAT_MSGS, msg);
            }));
    }

    /**
     * Returns a list containing the chat participants for the specified local type.
     */
    public function getPlayerList (ltype :String) :PlayerList
    {
        if (ltype != ChatCodes.PLACE_CHAT_TYPE) {
            return null;
        }
        if (_roomOccList.havePlace()) {
            return _roomOccList;
        }
        return _gamePlayerList;
    }

    override public function clientDidLogon (event :ClientEvent) :void
    {
        super.clientDidLogon(event);
        _chatTabs.memberObjectUpdated(_mctx.getMemberObject());
    }

    // from ChatDirector
    override public function requestSpeak (
        speakSvc :SpeakService, message :String, mode :int) :void
    {
        var channel :MsoyChatChannel = getCurrentChannel();
        if ((speakSvc != null) || // if a specific service is specified, OR
                (channel == null) || (channel.type == MsoyChatChannel.ROOM_CHANNEL)) {
                // ...if place chat, then we don't need to do anything special.
            super.requestSpeak(speakSvc, message, mode);
            return;
        }
        if (channel.type == MsoyChatChannel.MEMBER_CHANNEL) {
            // route this to requestTell, which will filter
            requestTell(channel.ident as Name, message, null, channel.toLocalType());
            return;
        }

        // ABOVE this line is stuff handled in the base class, that filters properly
        // BELOW this line, we need to filter it ourselves
        message = filter(message, null, true);
        if (message == null) {
            // they filtered it into nothingness!
            return;
        }

        if (channel.type == MsoyChatChannel.JABBER_CHANNEL) {
            // mode is lost here
            requestJabber(channel.ident as JabberName, message, channel.toLocalType());

        } else {
            requestChannelSpeak(channel, message, mode);
        }
    }

    override public function displayFeedback (bundle :String, message :String) :void
    {
        // alter things so that we deliver feedback on the open tab
        displaySystem(bundle, message, SystemMessage.FEEDBACK, getCurrentLocalType());
    }

    // from ChatDirector
    override public function enteredLocation (place :PlaceObject) :void
    {
        if (!(place is PrimaryPlace)) {
            // If it's a non-primary place, only add it as an auxiliary source, just to be sure.
            // TODO: figure out a sensible localtype for non-primary places (presently, only AVRGs)
            addAuxiliarySource(place, "msoyAux");
            return; // block non-primary places from super
        }

        super.enteredLocation(place);

        // let our occupant list know about our new location
        if (place is RoomObject) {
            _roomOccList.setPlaceObject(place);
        }
        _chatTabs.setPlaceName(PrimaryPlace(place).getName());
    }

    // from ChatDirector
    override public function leftLocation (place :PlaceObject) :void
    {
        if (!(place is PrimaryPlace)) {
            // See notes in enteredLocation
            removeAuxiliarySource(place);
            return;
        }

        // only change the name if it's the place we're actually tracking
        if (place == _place) {
            // let our occupant list know that we're nowhere
            _roomOccList.setPlaceObject(null);
            _chatTabs.setPlaceName(null);
        }

        super.leftLocation(place);
    }

    /**
     * Sets the player list for a game that has just started up.
     */
    public function setGamePlayerList (plobj :PlaceObject, list :PlayerList) :void
    {
        _gamePlace = plobj;
        _gamePlayerList = list;
    }

    /**
     * Clears the player list for a game that has just shut down.
     */
    public function clearGamePlayerList (plobj :PlaceObject) :void
    {
        if (_gamePlace != plobj) {
            log.warning("Clearing game player list for a different place?",
                        "plobj", plobj, "gameplace", _gamePlace);
            return;
        }
        _gamePlace = null;
        _gamePlayerList = null;
    }

    // from ChatDirector
    override protected function setClientInfo (msg :ChatMessage, localType :String) :void
    {
        if ((msg.localtype == null) && ( // skip this if msg.localtype is already set
                (msg is UserMessage && localType == ChatCodes.USER_CHAT_TYPE) ||
                (msg is TellFeedbackMessage))) {
            // use a more specific localtype
            var member :MemberName = (msg as UserMessage).getSpeakerDisplayName() as MemberName;
            localType = MsoyChatChannel.makeMemberChannel(member).toLocalType();
        }
        super.setClientInfo(msg, localType);
    }

    // from ChatDirector
    override protected function getChannelLocalType (channel :ChatChannel) :String
    {
        var mchannel :MsoyChatChannel = (channel as MsoyChatChannel);
        // this is called by the ChatDirector when a message arrives, we sneak in here and make
        // sure we have a chat channel tab available for this channel type so that when the chat
        // director goes to dispatch the message, we're all ready to go; if the tab already exists,
        // openChannelTab basically NOOPs
        _chatTabs.openChannelTab(mchannel, false);
        return mchannel.toLocalType();
    }

    // from ChatDirector
    override protected function fetchServices (client :Client) :void
    {
        super.fetchServices(client);
        _csservice = (client.requireService(ChannelSpeakService) as ChannelSpeakService);
        _jservice = (client.requireService(JabberService) as JabberService);
    }

    // from ChatDirector
    override protected function suppressTooManyCaps () :Boolean
    {
        return false;
    }

    // from ChatDirector
    override protected function clearChatOnClientExit () :Boolean
    {
        return false; // TODO: we need this because on msoy we "exit" when change servers
    }

    // from ChatDirector
    override protected function checkCanChat (
        speakSvc :SpeakService, message :String, mode :int) :String
    {
        var now :int = getTimer();
        if (_throttle.throttleOpAt(now)) {
            return "e.chat_throttled";
        }
        // restrict guests from speaking
        if( !_mctx.isRegistered() && _guestThrottle.throttleOpAt(now) )
        {
            return "Sorry, guests are not allowed to speak. Please register an account.";
        }
        // if we allow it, we might also count this message as more than one "op"
        if (message.length > 8) {
            _throttle.noteOp(now);
        }
        if (message.length > (MAX_CHAT_LENGTH / 2)) {
            _throttle.noteOp(now);
        }
        return null;
    }

    /**
     * Requests that a tell message be delivered to the specified jabber user.
     */
    protected function requestJabber (
        target :JabberName, msg :String, feedbackLocaltype :String) :void
    {
        _jservice.sendMessage(target, msg, new ResultAdapter(
            function (result :Object) :void {
                if (result is String) {
                    displaySystem(MsoyCodes.CHAT_MSGS, (result as String), SystemMessage.FEEDBACK,
                                  feedbackLocaltype);
                }
                dispatchMessage(new TellFeedbackMessage(target, msg), feedbackLocaltype);
            },
            function (cause :String) :void {
                var msg :String = MessageBundle.compose(
                    "e.im_tell_failed", MessageBundle.taint(cause));
                displaySystem(MsoyCodes.CHAT_MSGS, msg, SystemMessage.FEEDBACK, feedbackLocaltype);
            }));
    }

    /**
     * Requests that a message be delivered to the specified channel.
     */
    protected function requestChannelSpeak (channel :MsoyChatChannel, msg :String, mode :int) :void
    {
        _csservice.speak(channel, msg, mode);
    }

    /**
     * Create a ChatChannel object for the specified Name.
     */
    protected function makeChannel (name :Name) :MsoyChatChannel
    {
        if (name is MemberName) {
            return MsoyChatChannel.makeMemberChannel(name as MemberName);
        } else if (name is GroupName) {
            return MsoyChatChannel.makeGroupChannel(name as GroupName);
        } else if (name is ChannelName) {
            return MsoyChatChannel.makePrivateChannel(name as ChannelName);
        } else if (name is RoomName) {
            return MsoyChatChannel.makeRoomChannel(name as RoomName);
        } else if (name is JabberName) {
            return MsoyChatChannel.makeJabberChannel(name as JabberName);
        } else {
            Log.getLog(this).warning("Requested to create unknown type of channel",
                "name", name, "type", ClassUtil.getClassName(name));
            return null;
        }
    }

    /** Casted form of our context. */
    protected var _mctx :MsoyContext;

    /** You may utter 8 things per 5 seconds, but large things count as two. */
    protected var _throttle :Throttle = new Throttle(8, 5000);
    /** if you're a guest, you may not speak */
    protected var _guestThrottle :Throttle = new Throttle(0, 1000);

    protected var _chatTabs :ChatTabBar;
    protected var _chatHistory :HistoryList;
    protected var _roomOccList :RoomOccupantList;

    protected var _gamePlayerList :PlayerList;
    protected var _gamePlace :PlaceObject;

    protected var _csservice :ChannelSpeakService;
    protected var _jservice :JabberService;
}
}