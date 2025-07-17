//
// $Id$

package com.threerings.msoy.avrg.client {

import flash.utils.ByteArray;

import com.whirled.game.client.PropertySpaceHelper;
import com.whirled.game.data.GameData;
import com.whirled.game.data.PropertySpaceObject;
import com.whirled.game.data.WhirledPlayerObject;

import com.threerings.util.Integer;
import com.threerings.util.Iterator;
import com.threerings.util.Log;
import com.threerings.util.ObjectMarshaller;
import com.threerings.util.StringUtil;

import com.threerings.presents.client.Client;
import com.threerings.presents.client.ResultAdapter;

import com.threerings.crowd.data.OccupantInfo;

import com.threerings.whirled.spot.data.SceneLocation;

import com.threerings.msoy.avrg.client.BackendUtils;
import com.threerings.msoy.avrg.data.AVRGameAgentObject;
import com.threerings.msoy.avrg.data.AVRGameObject;
import com.threerings.msoy.avrg.data.PlayerLocation;
import com.threerings.msoy.avrg.data.PropertySpaceObjectImpl;
import com.threerings.msoy.bureau.util.MsoyBureauContext;
import com.threerings.msoy.data.all.MemberName;
import com.threerings.msoy.game.data.PlayerObject;
import com.threerings.msoy.item.data.all.Audio;
import com.threerings.msoy.item.data.all.Item;
import com.threerings.msoy.item.data.all.ItemIdent;
import com.threerings.msoy.party.client.PartyGameHelper;
import com.threerings.msoy.room.data.ActorInfo;
import com.threerings.msoy.room.data.MsoyLocation;
import com.threerings.msoy.room.data.RoomObject;
import com.threerings.msoy.room.data.RoomPropertiesObject;

/**
 * Manages the connection to the server agent thane user code for an AVRG.
 */
public class ThaneAVRGameBackend
{
    public const log :Log = Log.getLog(this);

    /**
     * Constructs a new base avr game backend.
     */
    public function ThaneAVRGameBackend (
        ctx :MsoyBureauContext, gameObj :AVRGameObject, gameAgentObj: AVRGameAgentObject,
        controller :ThaneAVRGameController)
    {
        _ctx = ctx;
        _gameObj = gameObj;
        _gameAgentObj = gameAgentObj;
        _controller = controller;
        _partyHelper.init(gameObj, callUserCode);
    }

    /**
     * Determines if we are connected to the front end code.
     */
    public function isConnected () :Boolean
    {
        return _userFuncs != null;
    }

    /**
     * Retrieves the function pointer that will be called with the user properties when the front
     * end connects.
     */
    public function getConnectListener () :Function
    {
        return handleUserCodeConnect;
    }

    /**
     * Cleans up our references when this agent is going away.
     */
    public function shutdown () :void
    {
        // shut down sub-backends, remove listeners
        if (_privateMessageAdapter != null) {
            _privateMessageAdapter.release();
        }
        _partyHelper.shutdown();
    }

    /**
     * Informs the user code that the room is no longer accessible.
     */
    public function roomUnloaded (roomId :int) :void
    {
        callUserCode("roomUnloaded_v1", roomId);
    }

    /**
     * Informs the user code that a player has joined the game.
     */
    public function playerJoinedGame (memberId :int) :void
    {
        log.info("Player joined game", "memberId", memberId);
        callUserCode("playerJoinedGame_v1", memberId);
    }

    /**
     * Informs the user code that a player has left the game.
     */
    public function playerLeftGame (memberId :int) :void
    {
        log.info("Player left game", "memberId", memberId);
        callUserCode("playerLeftGame_v1", memberId);
    }

    /**
     * Informs the user code that a player has entered a room.
     */
    public function playerEnteredRoom (memberId :int, roomId :int) :void
    {
        log.info("Player entered room", "memberId", memberId, "roomId", roomId);
        callUserCode("enteredRoom_v1", memberId, roomId);
        callUserCode("playerEntered_v1", roomId, memberId);
    }

    /**
     * Informs the user code that a player has left a room.
     */
    public function playerLeftRoom (memberId :int, roomId :int) :void
    {
        log.info("Player left room", "memberId", memberId, "roomId", roomId);
        callUserCode("playerLeft_v1", roomId, memberId);
        callUserCode("leftRoom_v1", memberId, roomId);
    }

    /**
     * Creates an adapter that will dispatch to the player controls in the user code.
     */
    public function createPlayerNetAdapter (player :PlayerObject) :BackendNetAdapter
    {
        var adapter :BackendNetAdapter = new BackendNetAdapter(
            player, [ RoomPropertiesObject.USER_MESSAGE ], _userFuncs, "player_propertyWasSet_v1",
            null);
        adapter.setTargetId(player.getMemberId());
        return adapter;
    }

    /**
     * Creates an adapter that will dispatch avatar actions to the user code.
     */
    public function createAvatarAdapter (room :RoomObject) :BackendAvatarAdapter
    {
        var adapter :BackendAvatarAdapter = new BackendAvatarAdapter(
            _gameObj, room, _userFuncs, "playerMoved_v1", "actorStateSet_v1",
            "actorAppearanceChanged_v1");
        return adapter;
    }

    /**
     * Informs the user code that a mob has been spawned and is ready to control.
     */
    public function mobSpawned (roomId :int, mobId :String) :void
    {
        callUserCode("mobSpawned_v1", roomId, mobId);
    }

    /**
     * Informs the user code that a mob has now been fully removed.
     */
    public function mobRemoved (roomId :int, mobId :String) :void
    {
        callUserCode("mobRemoved_v1", roomId, mobId);
    }

    /**
     * Informs the user code that a mob change has now taken effect.
     */
    public function mobChanged (roomId :int, mobId :String) :void
    {
        callUserCode("mobAppearanceChanged_v1", roomId, mobId);
    }

    /**
     * Informs the user code that a room signal has been received.
     */
    public function signalReceived (roomId :int, name :String, value :ByteArray) :void
    {
        callUserCode("signalReceived_v1", roomId, name, ObjectMarshaller.decode(value));
    }

    public function processMusicStartStop (roomId :int, started :Boolean) :void
    {
        callUserCode("musicStartStop_v1", roomId, started);
    }

    /**
     * Call an exposed function in usercode.
     */
    public function callUserCode (name :String, ... args) :*
    {
        if (_userFuncs != null) {
            try {
                var func :Function = (_userFuncs[name] as Function);
                if (func == null) {
                    // TODO: Can we detect if this is user's fault? If so, throw UserError

                } else {
                    return func.apply(null, args);
                }
            } catch (err :Error) {
                _controller.outputToUserCode("An Error occurred while calling " + name, err);
            }
        } else {
            log.warning("Calling user code before connection", "name", name);
        }
        return undefined;
    }

    protected function handleUserCodeConnect (evt :Object) :void
    {
        var props :Object = evt.props;

        if (_userFuncs != null) {
            props.alreadyConnected = true;
            log.warning("User code connected more than once", "backend", this);
            return;
        }

        _userFuncs = props.userProps;

        var ourProps :Object = new Object();
        populateProperties(ourProps);
        props.hostProps = ourProps;

        _privateMessageAdapter = new BackendNetAdapter(
            _ctx.getClient().getClientObject(),
            [ WhirledPlayerObject.getMessageName(_gameObj.getOid()) ], _userFuncs, null,
            "game_messageReceived_v1");
    }

    protected function populateProperties (o :Object) :void
    {
        // .*
        o["startTransaction"] = startTransaction_v1;
        o["commitTransaction"] = commitTransaction_v1;

        // .props
        o["agent_getGameData_v1"] = agent_getGameData_v1;
        o["agent_setProperty_v1"] = agent_setProperty_v1;

        // .game
        o["game_getPlayerIds_v1"] = game_getPlayerIds_v1;
        o["game_getOccupantName_v1"] = game_getOccupantName_v1;
        o["game_sendMessage_v1"] = game_sendMessage_v1;
        o["isRoomLoaded_v1"] = isRoomLoaded_v1
        o["getLevelPacks_v2"] = getLevelPacks_v2;
        o["getItemPacks_v1"] = getItemPacks_v1;
        o["loadLevelPackData_v1"] = loadLevelPackData_v1;
        o["loadItemPackData_v1"] = loadItemPackData_v1;
        _partyHelper.populateProperties(o);

        // .game.props
        o["game_getGameData_v1"] = game_getGameData_v1;
        o["game_setProperty_v1"] = game_setProperty_v1;

        // .getRoom()
        o["room_getPlayerIds_v1"] = room_getPlayerIds_v1;
        o["room_getOccupantIds_v1"] = room_getOccupantIds_v1;
        o["room_getOccupantName_v1"] = room_getOccupantName_v1;
        o["room_getRoomName_v1"] = room_getRoomName_v1;
        o["isPlayerHere_v1"] = isPlayerHere_v1;
        o["getAvatarInfo_v2"] = getAvatarInfo_v2;
        o["spawnMob_v1"] = spawnMob_v1;
        o["despawnMob_v1"] = despawnMob_v1;
        o["getSpawnedMobs_v1"] = getSpawnedMobs_v1;
        o["moveMob_v1"] = moveMob_v1;
        o["room_sendMessage_v1"] = room_sendMessage_v1;
        o["room_sendSignal_v1"] = room_sendSignal_v1;
        o["getMusicOwner_v1"] = getMusicOwner_v1;
        // .getRoom() backwards compat
        o["getAvatarInfo_v1"] = getAvatarInfo_v1;

        // .getRoom().props
        o["room_getGameData_v1"] = room_getGameData_v1;
        o["room_setProperty_v1"] = room_setProperty_v1;

        // .getPlayer()
        o["player_getRoomId_v1"] = player_getRoomId_v1;
        o["player_moveToRoom_v1"] = player_moveToRoom_v1;
        o["getPlayerName_v1"] = getPlayerName_v1;
        o["holdsTrophy_v1"] = holdsTrophy_v1;
        o["awardTrophy_v1"] = awardTrophy_v1;
        o["awardPrize_v1"] = awardPrize_v1;
        o["getPlayerItemPacks_v1"] = getPlayerItemPacks_v1;
        o["getPlayerLevelPacks_v1"] = getPlayerLevelPacks_v1;
        o["deactivateGame_v1"] = deactivateGame_v1;
        o["completeTask_v1"] = completeTask_v1;
        o["loadOfflinePlayer_v1"] = loadOfflinePlayer_v1;
        o["setOfflinePlayerProperty_v1"] = setOfflinePlayerProperty_v1;
        o["playAvatarAction_v1"] = playAvatarAction_v1;
        o["setAvatarState_v1"] = setAvatarState_v1;
        o["setAvatarMoveSpeed_v1"] = setAvatarMoveSpeed_v1;
        o["setAvatarLocation_v1"] = setAvatarLocation_v1;
        o["setAvatarOrientation_v1"] = setAvatarOrientation_v1;
        o["getCoins_v1"] = getCoins_v1;
        o["getBars_v1"] = getBars_v1;
        o["player_sendMessage_v1"] = player_sendMessage_v1;
        o["purchaseItemPack_v1"] = purchaseItemPack_v1;
        o["consumeItemPack_v1"] = consumeItemPack_v1;

        // .getPlayer().props
        o["player_getGameData_v1"] = player_getGameData_v1;
        o["player_setProperty_v1"] = player_setProperty_v1;
    }

    // -------------------- .* --------------------
    protected function startTransaction_v1 () :void
    {
        _controller.getTransactions().start();
    }

    protected function commitTransaction_v1 () :void
    {
        _controller.getTransactions().commit();
    }

    // -------------------- .game --------------------
    protected function game_getPlayerIds_v1 () :Array
    {
        return BackendUtils.getPlayerIds(_gameObj, null, 0, filterPlayer);
    }

    protected function game_getOccupantName_v1 (playerId :int) :String
    {
        return BackendUtils.getOccupantName(_gameObj, playerId);
    }

    protected function game_sendMessage_v1 (name :String, value :Object) :void
    {
        ensureGameClient(); // TODO invChange: this still needed?
        BackendUtils.sendMessage(_gameObj.messageService, name, value, "game");
    }

    protected function isRoomLoaded_v1 (roomId :int) :Boolean
    {
        return _controller.getRoomProps(roomId) != null;
    }

    protected function getLevelPacks_v2 (filter :Function = null) :Array
    {
        return BackendUtils.getLevelPacks(_gameObj.gameData, filter);
    }

    protected function getItemPacks_v1 (filter :Function = null) :Array
    {
        return BackendUtils.getItemPacks(_gameObj.gameData, filter);
    }

    protected function loadLevelPackData_v1 (
        ident :String, onLoaded :Function, onFailure :Function) :void
    {
        BackendUtils.loadPackData(_gameObj, ident, GameData.LEVEL_DATA,
                                  onLoaded, onFailure);
    }

    protected function loadItemPackData_v1 (
        ident :String, onLoaded :Function, onFailure :Function) :void
    {
        BackendUtils.loadPackData(_gameObj, ident, GameData.ITEM_DATA,
                                  onLoaded, onFailure);
    }

    // -------------------- .props --------------------
    protected function agent_getGameData_v1 (targetId :int) :Object
    {
        if (targetId != 0) {
            throw new UserError("Internal error: unexpected target id");
        }
        return _gameAgentObj.getUserProps();
    }

    protected function agent_setProperty_v1 (
        targetId :int, name :String, value :Object, key :Object, isArray :Boolean,
        immediate :Boolean) :void
    {
        if (targetId != 0) {
            throw new UserError("Internal error: unexpected target id");
        }
        ensureGameClient(); // TODO invChange: this still needed?
        BackendUtils.encodeAndSet(_gameAgentObj, name, value, key, isArray, immediate);
    }

    // -------------------- .game.props --------------------
    protected function game_getGameData_v1 (targetId :int) :Object
    {
        if (targetId != 0) {
            throw new UserError("Internal error: unexpected target id");
        }
        return _gameObj.getUserProps();
    }

    protected function game_setProperty_v1 (
        targetId :int, name :String, value :Object, key :Object, isArray :Boolean,
        immediate :Boolean) :void
    {
        if (targetId != 0) {
            throw new UserError("Internal error: unexpected target id");
        }
        ensureGameClient(); // TODO invChange: this still needed?
        BackendUtils.encodeAndSet(_gameObj, name, value, key, isArray, immediate);
    }

    // -------------------- .getRoom() --------------------
    protected function room_getRoomName_v1 (roomId :int) :String
    {
        var roomObj :RoomObject = _controller.getRoom(roomId);
        return (roomObj == null) ? null : roomObj.name;
    }

    protected function room_getPlayerIds_v1 (roomId :int) :Array
    {
        var roomObj :RoomObject = _controller.getRoom(roomId);
        return BackendUtils.getPlayerIds(_gameObj, roomObj, roomId, filterPlayer);
    }

    protected function room_getOccupantIds_v1 (roomId :int) :Array
    {
        var roomObj :RoomObject = _controller.getRoom(roomId);
        return BackendUtils.getOccupantIds(roomObj);
    }

    protected function room_getOccupantName_v1 (roomId :int, playerId :int) :String
    {
        var roomObj :RoomObject = _controller.getRoom(roomId);
        return BackendUtils.getOccupantName(roomObj, playerId);
    }

    protected function isPlayerHere_v1 (roomId :int, playerId :int) :Boolean
    {
        try {
            var playerRoomId :int = getPlayerRoomId(playerId);
            return playerRoomId != 0 && playerRoomId == roomId;
        } catch (e :UserError) {
        }
        return false;
    }

    protected function getAvatarInfo_v1 (roomId :int, playerId :int) :Array
    {
        var obj :Object = getAvatarInfo_v2(roomId, playerId);
        return [ obj["name"], obj["state"], obj["x"], obj["y"], obj["z"], obj["orient"],
                 obj["moveSpeed"], obj["isMoving"], obj["isIdle"], obj["bounds"] ];
    }

    protected function getAvatarInfo_v2 (roomId :int, playerId :int) :Object
    {
        var roomId :int = getPlayerRoomId(playerId);
        if (roomId == 0) {
            throw new UserError("Player not in any room [playerId=" + playerId + "]");
        }
        var roomObj :RoomObject = _controller.getRoom(roomId);
        var actorInfo :ActorInfo;
        actorInfo = BackendUtils.resolvePlayerWorldInfo(_gameObj, roomObj, playerId) as ActorInfo;
        var loc :MsoyLocation;
        loc = (roomObj.occupantLocs.get(actorInfo.bodyOid) as SceneLocation).loc as MsoyLocation;
        if (loc == null) {
            log.warning(
                "Location not found", "playerId", playerId, "bodyOid", actorInfo.bodyOid,
                "sceneLoc", roomObj.occupantLocs.get(actorInfo.bodyOid));
            loc = new MsoyLocation(.5, 0, .5);
        }

        var data :Object = new Object();
        data["entityId"] = actorInfo.getItemIdent().toString();
        data["state"] = actorInfo.getState();
        data["x"] = loc.x;
        data["y"] = loc.y;
        data["z"] = loc.z;
        data["orient"] = loc.orient;
        data["moveSpeed"] = 1.0; // TODO moveSpeed
        data["isMoving"] = false; // TODO isMoving
        data["isIdle"] = actorInfo.isIdle();
        data["bounds"] = null; // TODO: bounds
        data["name"] = actorInfo.username.toString(); // deprecated, only for _v1
        return data;
    }

    protected function spawnMob_v1 (
        roomId :int, mobId :String, mobName :String, x :Number, y :Number, z :Number) :void
    {
        if (StringUtil.isBlank(mobId)) {
            throw new UserError("Blank mobId in spawnMob");
        }

        if (StringUtil.isBlank(mobName)) {
            throw new UserError("Blank mobName in spawnMob");
        }

        var roomObj :RoomObject = _controller.getRoom(roomId);
        var loc :MsoyLocation = new MsoyLocation(x, y, z);
        ensureRoomClient(roomId); // TODO invChange: this still needed?
        roomObj.roomService.spawnMob(_controller.getGameId(), mobId, mobName, loc,
            BackendUtils.loggingInvocationListener("spawnMob", _controller.outputToUserCode));
    }

    protected function despawnMob_v1 (roomId :int, mobId :String) :void
    {
        if (StringUtil.isBlank(mobId)) {
            throw new UserError("Blank mobId in despawnMob");
        }

        var roomObj :RoomObject = _controller.getRoom(roomId);
        ensureRoomClient(roomId); // TODO invChange: this still needed?
        roomObj.roomService.despawnMob(_controller.getGameId(), mobId,
            BackendUtils.loggingInvocationListener("despawnMob", _controller.outputToUserCode));
    }

    protected function getSpawnedMobs_v1 (roomId :int) :Array
    {
        return _controller.getMobIds(roomId);
    }

    protected function moveMob_v1 (roomId :int, id :String, x :Number, y :Number, z :Number) :void
    {
        var roomObj :RoomObject = _controller.getRoom(roomId);
        ensureRoomClient(roomId); // TODO invChange: this still needed?
        roomObj.roomService.moveMob(_controller.getGameId(), id, new MsoyLocation(x, y, z),
            BackendUtils.loggingConfirmListener("moveMob", null, _controller.outputToUserCode));
    }

    protected function room_sendMessage_v1 (roomId :int, name :String, value :Object) :void
    {
        var roomProps :RoomPropertiesObject = _controller.getRoomProps(roomId);
        ensureRoomClient(roomId); // TODO invChange: this still needed?
        BackendUtils.sendMessage(roomProps.messageService, name, value, "room");
    }

    protected function room_sendSignal_v1 (roomId :int, name :String, value :Object) :void
    {
        var roomObj :RoomObject = _controller.getRoom(roomId);
        ensureRoomClient(roomId); // TODO invChange: this still needed?
        roomObj.roomService.sendSpriteSignal(name, ObjectMarshaller.encode(value) as ByteArray);
    }

    protected function getMusicOwner_v1 (roomId :int) :int
    {
        var roomObj :RoomObject = _controller.getRoom(roomId);
        var audio :Audio =
            roomObj.playlist.get(new ItemIdent(Item.AUDIO, roomObj.currentSongId)) as Audio;
        return (audio == null) ? 0 : audio.ownerId;
    }

    // -------------------- .getRoom().props --------------------
    protected function room_getGameData_v1 (roomId :int) :Object
    {
        var roomProps :RoomPropertiesObject = _controller.getRoomProps(roomId);
        return roomProps.getUserProps();
    }

    protected function room_setProperty_v1 (
        roomId :int, name :String, value :Object, key :Object, isArray :Boolean,
        immediate :Boolean) :void
    {
        var roomProps :RoomPropertiesObject = _controller.getRoomProps(roomId);
        ensureRoomClient(roomId); // TODO invChange: this still needed?
        BackendUtils.encodeAndSet(roomProps, name, value, key, isArray, immediate);
    }

    // -------------------- .getPlayer() --------------------
    protected function player_getRoomId_v1 (playerId :int) :int
    {
        return getPlayerRoomId(playerId);
    }

    protected function player_moveToRoom_v1 (playerId :int, roomId :int, exitCoords :Array) :void
    {
        var exit :MsoyLocation = null;
        if (exitCoords != null) {
            exit = new MsoyLocation(exitCoords[0], exitCoords[1], exitCoords[2]);
        }
        _gameObj.avrgService.movePlayerToRoom(playerId, roomId, exit,
            BackendUtils.loggingConfirmListener(
                "movePlayerToRoom", null, _controller.outputToUserCode));
    }

    protected function getPlayerName_v1 (playerId :int) :String
    {
        var iterator :Iterator = _gameObj.occupantInfo.iterator();
        while (iterator.hasNext()) {
            var name :MemberName = OccupantInfo(iterator.next()).username as MemberName;
            if (name != null && name.getId() == playerId) {
                return name.toString();
            }
        }
        return null;
    }

    protected function holdsTrophy_v1 (targetId :int /* ignored */, ident :String) :Boolean
    {
        return BackendUtils.holdsTrophy(targetId, ident, playerOwnsData);
    }

    protected function awardTrophy_v1 (targetId :int, ident :String) :Boolean
    {
        if (playerOwnsData(GameData.TROPHY_DATA, ident, targetId)) {
            return false;
        }

        _gameObj.prizeService.awardTrophy(ident, targetId,
            BackendUtils.loggingConfirmListener("awardTrophy", null,
                _controller.outputToUserCode));

        return true;
    }

    protected function awardPrize_v1 (targetId :int, ident :String) :void
    {
        if (!playerOwnsData(GameData.PRIZE_MARKER, ident, targetId)) {
            _gameObj.prizeService.awardPrize(ident, targetId,
                BackendUtils.loggingConfirmListener("awardPrize", null,
                    _controller.outputToUserCode));
        }
    }

    protected function getPlayerItemPacks_v1 (targetId :int /* ignored */) :Array
    {
        return BackendUtils.getPlayerItemPacks(_gameObj.gameData, targetId, countPlayerData);
    }

    protected function getPlayerLevelPacks_v1 (targetId :int /* ignored */) :Array
    {
        return BackendUtils.getPlayerLevelPacks(_gameObj.gameData, targetId, playerOwnsData);
    }

    protected function deactivateGame_v1 (playerId :int) :void
    {
        _controller.deactivateGame(playerId);
    }

    protected function completeTask_v1 (playerId :int, taskId :String, payout :Number) :void
    {
        if (StringUtil.isBlank(taskId)) {
            throw new UserError("Task id must not be blank");
        }

        payout = Math.max(0, Math.min(payout, 1));
        ensureGameClient(); // TODO invChange: this still needed?
        _gameObj.avrgService.completeTask(playerId, taskId, payout,
            BackendUtils.loggingConfirmListener("completeTask", null,
                _controller.outputToUserCode));
    }

    protected function loadOfflinePlayer_v1 (
        playerId :int, success :Function, failure :Function) :void
    {
        PropertySpaceObjectImpl;

        ensureGameClient(); // TODO invChange: this still needed?
        _gameObj.avrgService.loadOfflinePlayer(playerId, new ResultAdapter(
            function (props :PropertySpaceObject) :void {
                if (props == null) {
                    // this means the player had no existing persistent properties, which means
                    // we are not allowed to set offline properties on it
                    failure("Cannot set offline properties on player without existing " +
                            " persistent properties [playerId=" + playerId + "]");
                    return;
                }
                // mark this offline player as a valid target for offline property sets
                _offline = playerId;
                try {
                    // trigger whatever actions the usercode wants to take for this offline player
                    success(props.getUserProps());

                } catch (e :Error) {
                    // turn off offline player access
                    failure("Error in callback: " + e);
                    _offline = 0;
                    throw e;
                }
                // turn off offline player access
                _offline = 0;
            }, failure));
    }

    protected function setOfflinePlayerProperty_v1 (
        playerId :int, name :String, value :Object, key :Object, isArray :Boolean,
        immediate :Boolean) :void
    {
        if (_offline != playerId) {
            throw new Error("Illegal access to offline player properties [playerId=" + playerId +
                            ", name=" + name + "]");
        }

        BackendUtils.validatePropertyChange(name, value, isArray, key);

        var encoded :Object = PropertySpaceHelper.encodeProperty(value, (key == null));
        var ikey :Integer = (key == null) ? null : new Integer(int(key));

        ensureGameClient(); // TODO invChange: this still needed?
        _gameObj.avrgService.setOfflinePlayerProperty(playerId, name, encoded, ikey, isArray,
            BackendUtils.loggingConfirmListener("setOfflinePlayerProperty"));
    }

    protected function playAvatarAction_v1 (playerId :int, action :String) :void
    {
        resolveRoomAndClient(playerId, function (roomObj :RoomObject, client :Client) :void {
            BackendUtils.playAvatarAction(_gameObj, roomObj, playerId, action);
        });
    }

    protected function setAvatarState_v1 (playerId :int, state :String) :void
    {
        resolveRoomAndClient(playerId, function (roomObj :RoomObject, client :Client) :void {
            BackendUtils.setAvatarState(_gameObj, roomObj, playerId, state);
        });
    }

    protected function setAvatarMoveSpeed_v1 (playerId :int, pixelsPerSecond :Number) :void
    {
        resolveRoomAndClient(playerId, function (roomObj :RoomObject, client :Client) :void {
            BackendUtils.setAvatarMoveSpeed(_gameObj, roomObj, playerId, pixelsPerSecond);
        });
    }

    protected function setAvatarLocation_v1 (
        playerId :int, x :Number, y :Number, z: Number, orient :Number) :void
    {
        resolveRoomAndClient(playerId, function (roomObj :RoomObject, client :Client) :void {
            BackendUtils.setAvatarLocation(_gameObj, roomObj, playerId, x, y, z, orient);
        });
    }

    protected function setAvatarOrientation_v1 (playerId :int, orient :Number) :void
    {
        resolveRoomAndClient(playerId, function (roomObj :RoomObject, client :Client) :void {
            BackendUtils.setAvatarOrientation(_gameObj, roomObj, playerId, orient);
        });
    }

    protected function getCoins_v1 (playerId :int) :int
    {
        var player :PlayerObject = _controller.getPlayerForUser(playerId);
        return (_gameObj.isApproved && player != null) ? player.coins : 0;
    }

    protected function getBars_v1 (playerId :int) :int
    {
        var player :PlayerObject = _controller.getPlayerForUser(playerId);
        return (_gameObj.isApproved && player != null) ? player.bars : 0;
    }

    protected function player_sendMessage_v1 (playerId :int, name :String, value :Object) :void
    {
        ensureGameClient(); // TODO invChange: this still needed?
        BackendUtils.sendPrivateMessage(_gameObj.messageService, playerId, name, value, "room");
    }

    protected function purchaseItemPack_v1 (playerId :int, ident :String) :void
    {
        ensureGameClient(); // TODO invChange: this still needed?
        _gameObj.contentService.purchaseItemPack(playerId, ident,
            BackendUtils.loggingInvocationListener(
                "purchaseItemPack", _controller.outputToUserCode));
    }

    protected function consumeItemPack_v1 (playerId :int, ident :String) :Boolean
    {
        if (countPlayerData(GameData.ITEM_DATA, ident, playerId) < 1) {
            return false;
        }
        ensureGameClient(); // TODO invChange: this still needed?
        _gameObj.contentService.consumeItemPack(playerId, ident,
            BackendUtils.loggingInvocationListener(
                "consumeItemPack", _controller.outputToUserCode));
        return true;
    }

    // -------------------- .getPlayer().props --------------------
    protected function player_getGameData_v1 (playerId :int) :Object
    {
        var player :PlayerObject = _controller.getPlayerForUser(playerId);
        return player.getUserProps();
    }

    protected function player_setProperty_v1 (
        playerId :int, name :String, value :Object, key :Object, isArray :Boolean,
        immediate :Boolean) :void
    {
        var player :PlayerObject = _controller.getPlayerForUser(playerId);
        ensureGameClient(); // TODO invChange: this still needed?
        BackendUtils.encodeAndSet(player, name, value, key, isArray, immediate);
    }

    // -------------------- end of versioned methods --------------------

    protected function getPlayerRoomId (playerId :int) :int
    {
        var pl :PlayerLocation = _gameObj.playerLocs.get(playerId) as PlayerLocation;
        if (pl == null) {
            return 0;
        }
        return pl.sceneId;
    }

    /**
     * Find the given player's room and the client session that is connected to the room and call
     * fn(roomObj, client) if found.
     */
    protected function resolveRoomAndClient (playerId :int, fn :Function) :void
    {
        var roomId :int = getPlayerRoomId(playerId);
        if (roomId == 0) {
            throw new UserError("Player not in any room [playerId=" + playerId + "]");
        }

        // TODO: maybe expose ThaneAVRGameController::SceneBinding instead of always doing lookup
        // twice
        var roomObj :RoomObject = _controller.getRoom(roomId);
        fn(roomObj, ensureRoomClient(roomId));
    }

    /**
     * Determine whether or not the specified player has access to some item or level pack.
     */
    protected function playerOwnsData (type :int, ident :String, playerId :int) :Boolean
    {
        return countPlayerData(type, ident, playerId) > 0;
    }

    /**
     * Returns the number of copies of the specified item or level pack owned by the player.
     */
    protected function countPlayerData (type :int, ident :String, playerId :int) :int
    {
        var player :PlayerObject = _controller.getPlayerForUser(playerId);
        return player.countGameContent(_controller.getGameId(), type, ident)
    }

    /**
     * Returns true if a player should be included in getPlayerIds, for use as a callback with
     * <code>BackendUtils.getPlayerIds</code>.
     * @see BackendUtils.getPlayerIds
     */
    protected function filterPlayer (memberId :int) :Boolean
    {
        return _controller.getPlayer(memberId) != null;
    }

    /**
     * Accesses the game server client, making sure that a transaction is started for it if
     * <code>startTransaction_v1</code> was previously called.
     */
    protected function ensureGameClient () :Client
    {
        var gameClient :Client = _ctx.getClient();
        _controller.getTransactions().addClient(gameClient);
        return gameClient;
    }

    /**
     * Accesses the world server client for a given room, making sure that a transaction is started
     * for it if <code>startTransaction_v1</code> was previously called.
     */
    protected function ensureRoomClient (roomId :int) :Client
    {
        var roomClient :Client = _controller.getRoomClient(roomId);
        _controller.getTransactions().addClient(roomClient);
        return roomClient;
    }

    protected var _userFuncs :Object;
    protected var _ctx :MsoyBureauContext; // this is for the game server
    protected var _controller :ThaneAVRGameController;
    protected var _partyHelper :PartyGameHelper = new PartyGameHelper();
    protected var _gameObj :AVRGameObject;
    protected var _gameAgentObj :AVRGameAgentObject;

    protected var _offline :int = 0;

    protected var _privateMessageAdapter :BackendNetAdapter;
}
}