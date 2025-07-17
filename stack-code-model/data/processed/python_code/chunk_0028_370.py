﻿package com.company.assembleegameclient.objects {
import com.company.assembleegameclient.objects.animation.AnimationsData;
import com.company.assembleegameclient.parameters.Parameters;
import com.company.assembleegameclient.util.TextureRedrawer;
import com.company.assembleegameclient.util.redrawers.GlowRedrawer;
import com.company.util.AssetLibrary;
import com.company.util.ConversionUtil;

import flash.display.BitmapData;
import flash.utils.Dictionary;
import flash.utils.getDefinitionByName;

import kabam.rotmg.constants.GeneralConstants;
import kabam.rotmg.constants.ItemConstants;
import kabam.rotmg.messaging.impl.data.StatData;

public class ObjectLibrary {

    public static const IMAGE_SET_NAME:String = "lofiObj3";
    public static const IMAGE_ID:int = 0xFF;
    public static const projectileObjectTypeLibrary_:Dictionary = new Dictionary();
    public static const propsLibrary_:Dictionary = new Dictionary();
    public static const xmlLibrary_:Dictionary = new Dictionary();
    public static const idToType_:Dictionary = new Dictionary();
    public static const typeToDisplayId_:Dictionary = new Dictionary();
    public static const typeToTextureData_:Dictionary = new Dictionary();
    public static const typeToTopTextureData_:Dictionary = new Dictionary();
    public static const typeToAnimationsData_:Dictionary = new Dictionary();
    public static const petXMLDataLibrary_:Dictionary = new Dictionary();
    public static const skinSetXMLDataLibrary_:Dictionary = new Dictionary();
    public static const dungeonsXMLLibrary_:Dictionary = new Dictionary(true);
    public static const ENEMY_FILTER_LIST:Vector.<String> = new <String>["None", "Hp", "Defense"];
    public static const TILE_FILTER_LIST:Vector.<String> = new <String>["ALL", "Walkable", "Unwalkable", "Slow", "Speed=1"];
    public static const defaultProps_:ObjectProperties = new ObjectProperties(null);
    public static const TYPE_MAP:Object = {
        "ArenaGuard": ArenaGuard,
        "ArenaPortal": ArenaPortal,
        "CaveWall": CaveWall,
        "Character": Character,
        "CharacterChanger": CharacterChanger,
        "ClosedGiftChest": ClosedGiftChest,
        "ClosedVaultChest": ClosedVaultChest,
        "ConnectedWall": ConnectedWall,
        "Container": Container,
        "DoubleWall": DoubleWall,
        "FortuneGround": FortuneGround,
        "FortuneTeller": FortuneTeller,
        "GameObject": GameObject,
        "GuildBoard": GuildBoard,
        "GuildChronicle": GuildChronicle,
        "GuildHallPortal": GuildHallPortal,
        "GuildMerchant": GuildMerchant,
        "GuildRegister": GuildRegister,
        "Merchant": Merchant,
        "MoneyChanger": MoneyChanger,
        "MysteryBoxGround": MysteryBoxGround,
        "NameChanger": NameChanger,
        "ReskinVendor": ReskinVendor,
        "OneWayContainer": OneWayContainer,
        "Player": Player,
        "Portal": Portal,
        "Projectile": Projectile,
        "QuestRewards": QuestRewards,
        "DailyLoginRewards": DailyLoginRewards,
        "Sign": Sign,
        "SpiderWeb": SpiderWeb,
        "Stalagmite": Stalagmite,
        "Wall": Wall,
        "Pet": Pet,
        "PetUpgrader": PetUpgrader,
        "YardUpgrader": YardUpgrader
    };

    public static var textureDataFactory:TextureDataFactory = new TextureDataFactory();
    public static var playerChars_:Vector.<XML> = new Vector.<XML>();
    public static var hexTransforms_:Vector.<XML> = new Vector.<XML>();
    public static var playerClassAbbr_:Dictionary = new Dictionary();
    private static var currentDungeon:String = "";

    public static function parseDungeonXML(_arg1:String, _arg2:XML):void {
        var _local3:int = (_arg1.indexOf("_") + 1);
        var _local4:int = _arg1.indexOf("CXML");
        currentDungeon = _arg1.substr(_local3, (_local4 - _local3));
        dungeonsXMLLibrary_[currentDungeon] = new Dictionary(true);
        parseFromXML(_arg2, parseDungeonCallback);
    }

    private static function parseDungeonCallback(_arg1:int, _arg2:XML):void {
        if (((!((currentDungeon == ""))) && (!((dungeonsXMLLibrary_[currentDungeon] == null))))) {
            dungeonsXMLLibrary_[currentDungeon][_arg1] = _arg2;
            propsLibrary_[_arg1].belonedDungeon = currentDungeon;
        }
    }

    private static function SerializeProjectiles(_id:String, _objectType:int, _class:String, _file:String, _index:int):void {
        projectileObjectTypeLibrary_[Parameters.toHex(_objectType)] = {
            objectId: _id,
            objectTypeInt: _objectType,
            objectTypeHex: Parameters.toHex(_objectType),
            objectClass: _class,
            textureFile: _file,
            textureIndex: _index
        };
    }

    public static function parseFromXML(_arg1:XML, _arg2:Function = null):void {
        var _xmlDoc:XML;
        var _id:String;
        var _displayId:String;
        var _objectType:int;
        var _local7:Boolean;
        var _local8:int;
        for each (_xmlDoc in _arg1.Object) {
            _id = String(_xmlDoc.@id);
            _displayId = _id;
            if (_xmlDoc.hasOwnProperty("DisplayId")) {
                _displayId = _xmlDoc.DisplayId;
            }
            if (_xmlDoc.hasOwnProperty("Group")) {
                if (_xmlDoc.Group == "Hexable") {
                    hexTransforms_.push(_xmlDoc);
                }
            }
            _objectType = int(_xmlDoc.@type);
            if (((_xmlDoc.hasOwnProperty("PetBehavior")) || (_xmlDoc.hasOwnProperty("PetAbility")))) {
                petXMLDataLibrary_[_objectType] = _xmlDoc;
            }
            else {
                // store only projectiles
                if (String(_xmlDoc.Class) == "Projectile") {
                    var file:String = null;
                    var index:int = -1;
                    if (_xmlDoc.hasOwnProperty("Texture")) {
                        file = String(new XML(_xmlDoc.Texture).File);
                        index = int(new XML(_xmlDoc.Texture).Index);
                    }
                    SerializeProjectiles(_id, _objectType, String(_xmlDoc.Class), file, index);
                }
                propsLibrary_[_objectType] = new ObjectProperties(_xmlDoc);
                xmlLibrary_[_objectType] = _xmlDoc;
                idToType_[_id] = _objectType;
                typeToDisplayId_[_objectType] = _displayId;
                if (_arg2 != null) {
                    (_arg2(_objectType, _xmlDoc));
                }
                if (String(_xmlDoc.Class) == "Player") {
                    playerClassAbbr_[_objectType] = String(_xmlDoc.@id).substr(0, 2);
                    _local7 = false;
                    _local8 = 0;
                    while (_local8 < playerChars_.length) {
                        if (int(playerChars_[_local8].@type) == _objectType) {
                            playerChars_[_local8] = _xmlDoc;
                            _local7 = true;
                        }
                        _local8++;
                    }
                    if (!_local7) {
                        playerChars_.push(_xmlDoc);
                    }
                }
                typeToTextureData_[_objectType] = textureDataFactory.create(_xmlDoc);
                if (_xmlDoc.hasOwnProperty("Top")) {
                    typeToTopTextureData_[_objectType] = textureDataFactory.create(XML(_xmlDoc.Top));
                }
                if (_xmlDoc.hasOwnProperty("Animation")) {
                    typeToAnimationsData_[_objectType] = new AnimationsData(_xmlDoc);
                }
            }
        }
    }

    public static function getIdFromType(_arg1:int):String {
        var _local2:XML = xmlLibrary_[_arg1];
        if (_local2 == null) {
            return (null);
        }
        return (String(_local2.@id));
    }

    public static function getPropsFromId(_arg1:String):ObjectProperties {
        var _local2:int = idToType_[_arg1];
        return (propsLibrary_[_local2]);
    }

    public static function getXMLfromId(_arg1:String):XML {
        var _local2:int = idToType_[_arg1];
        return (xmlLibrary_[_local2]);
    }

    public static function getObjectFromType(objectType:int):GameObject {
        var objectXML:XML;
        var typeReference:String;
        try {
            objectXML = xmlLibrary_[objectType];
            typeReference = objectXML.Class;
        }
        catch (e:Error) {
            throw (new Error(("Type: 0x" + objectType.toString(16))));
        }
        var typeClass:Class = ((TYPE_MAP[typeReference]) || (makeClass(typeReference)));
        return (new (typeClass)(objectXML));
    }

    private static function makeClass(_arg1:String):Class {
        var _local2:String = ("com.company.assembleegameclient.objects." + _arg1);
        return ((getDefinitionByName(_local2) as Class));
    }

    public static function getTextureFromType(_arg1:int):BitmapData {
        var _local2:TextureData = typeToTextureData_[_arg1];
        if (_local2 == null) {
            return (null);
        }
        return (_local2.getTexture());
    }

    public static function getBitmapData(_arg1:int):BitmapData {
        var _local2:TextureData = typeToTextureData_[_arg1];
        var _local3:BitmapData = ((_local2) ? _local2.getTexture() : null);
        if (_local3) {
            return (_local3);
        }
        return (AssetLibrary.getImageFromSet(IMAGE_SET_NAME, IMAGE_ID));
    }

    public static function getRedrawnTextureFromType(_arg1:int, _arg2:int, _arg3:Boolean, _arg4:Boolean = true, _arg5:Number = 5):BitmapData {
        var _local6:BitmapData = getBitmapData(_arg1);
        var _local9:XML = xmlLibrary_[_arg1]|| new XML();
        if (_local8 == null && _local9.hasOwnProperty("Blue"))
            return (TextureRedrawer.redraw(_local6, _arg2, _arg3, 0x00FFFF, _arg4, _arg5));
        if (_local8 == null && _local9.hasOwnProperty("Red"))
            return (TextureRedrawer.redraw(_local6, _arg2, _arg3, 0xFF0000, _arg4, _arg5));
        if (_local8 == null && _local9.hasOwnProperty("Green"))
            return (TextureRedrawer.redraw(_local6, _arg2, _arg3, 0x11CE00, _arg4, _arg5));
        if (((!((Parameters.itemTypes16.indexOf(_arg1) == -1))) || ((_local6.height == 16)))) {
            _arg2 = (_arg2 * 0.5);
        }
        var _local7:TextureData = typeToTextureData_[_arg1];
        var _local8:BitmapData = ((_local7) ? _local7.mask_ : null);
        if (_local8 == null) {
            return (TextureRedrawer.redraw(_local6, _arg2, _arg3, 0, _arg4, _arg5));
        }
        var _local10:int = ((_local9.hasOwnProperty("Tex1")) ? int(_local9.Tex1) : 0);
        var _local11:int = ((_local9.hasOwnProperty("Tex2")) ? int(_local9.Tex2) : 0);
        _local6 = TextureRedrawer.resize(_local6, _local8, _arg2, _arg3, _local10, _local11, _arg5);
        _local6 = GlowRedrawer.outlineGlow(_local6, 0);
        return (_local6);
    }

    public static function getSizeFromType(_arg1:int):int {
        var _local2:XML = xmlLibrary_[_arg1];
        if (!_local2.hasOwnProperty("Size")) {
            return (100);
        }
        return (int(_local2.Size));
    }

    public static function getSlotTypeFromType(_arg1:int):int {
        var _local2:XML = xmlLibrary_[_arg1];
        if (!_local2.hasOwnProperty("SlotType")) {
            return (-1);
        }
        return (int(_local2.SlotType));
    }

    public static function isEquippableByPlayer(_arg1:int, _arg2:Player):Boolean {
        if (_arg1 == ItemConstants.NO_ITEM) {
            return (false);
        }
        var _local3:XML = xmlLibrary_[_arg1];
        var _local4:int = int(_local3.SlotType.toString());
        var _local5:uint;
        while (_local5 < GeneralConstants.NUM_EQUIPMENT_SLOTS) {
            if (_arg2.slotTypes_[_local5] == _local4) {
                return (true);
            }
            _local5++;
        }
        return (false);
    }

    public static function getMatchingSlotIndex(_arg1:int, _arg2:Player):int {
        var _local3:XML;
        var _local4:int;
        var _local5:uint;
        if (_arg1 != ItemConstants.NO_ITEM) {
            _local3 = xmlLibrary_[_arg1];
            _local4 = int(_local3.SlotType);
            _local5 = 0;
            while (_local5 < GeneralConstants.NUM_EQUIPMENT_SLOTS) {
                if (_arg2.slotTypes_[_local5] == _local4) {
                    return (_local5);
                }
                _local5++;
            }
        }
        return (-1);
    }

    public static function isUsableByPlayer(_arg1:int, _arg2:Player):Boolean {
        if ((((_arg2 == null)) || ((_arg2.slotTypes_ == null)))) {
            return (true);
        }
        var _local3:XML = xmlLibrary_[_arg1];
        if ((((_local3 == null)) || (!(_local3.hasOwnProperty("SlotType"))))) {
            return (false);
        }
        var _local4:int = _local3.SlotType;
        if (_local4 == ItemConstants.POTION_TYPE || _local4 == ItemConstants.EGG_TYPE || _local4 == ItemConstants.NEW_EGG_TYPE || _local4 == ItemConstants.NEW_EGG_LIMITED_EDITION_TYPE)
            return (true);
        var _local5:int;
        while (_local5 < _arg2.slotTypes_.length) {
            if (_arg2.slotTypes_[_local5] == _local4) {
                return (true);
            }
            _local5++;
        }
        return (false);
    }

    public static function isSoulbound(_arg1:int):Boolean {
        var _local2:XML = xmlLibrary_[_arg1];
        return (((!((_local2 == null))) && (_local2.hasOwnProperty("Soulbound"))));
    }

    public static function usableBy(_arg1:int):Vector.<String> {
        var _local5:XML;
        var _local6:Vector.<int>;
        var _local7:int;
        var _local2:XML = xmlLibrary_[_arg1];
        if ((((_local2 == null)) || (!(_local2.hasOwnProperty("SlotType"))))) {
            return (null);
        }
        var _local3:int = _local2.SlotType;
        if (_local3 == ItemConstants.POTION_TYPE || _local3 == ItemConstants.RING_TYPE || _local3 == ItemConstants.EGG_TYPE || _local3 == ItemConstants.NEW_EGG_TYPE || _local3 == ItemConstants.NEW_EGG_LIMITED_EDITION_TYPE)
            return (null);
        var _local4:Vector.<String> = new Vector.<String>();
        for each (_local5 in playerChars_) {
            _local6 = ConversionUtil.toIntVector(_local5.SlotTypes);
            _local7 = 0;
            while (_local7 < _local6.length) {
                if (_local6[_local7] == _local3) {
                    _local4.push(typeToDisplayId_[int(_local5.@type)]);
                    break;
                }
                _local7++;
            }
        }
        return (_local4);
    }

    public static function playerMeetsRequirements(_arg1:int, _arg2:Player):Boolean {
        var _local4:XML;
        if (_arg2 == null) {
            return (true);
        }
        var _local3:XML = xmlLibrary_[_arg1];
        for each (_local4 in _local3.EquipRequirement) {
            if (!playerMeetsRequirement(_local4, _arg2)) {
                return (false);
            }
        }
        return (true);
    }

    public static function playerMeetsRequirement(_arg1:XML, _arg2:Player):Boolean {
        var _local3:int;
        if (_arg1.toString() == "Stat") {
            _local3 = int(_arg1.@value);
            switch (int(_arg1.@stat)) {
                case StatData.MAX_HP_STAT:
                    return ((_arg2.maxHP_ >= _local3));
                case StatData.MAX_MP_STAT:
                    return ((_arg2.maxMP_ >= _local3));
                case StatData.LEVEL_STAT:
                    return ((_arg2.level_ >= _local3));
                case StatData.ATTACK_STAT:
                    return ((Parameters.parse(_arg2.attack_) >= _local3));
                case StatData.DEFENSE_STAT:
                    return ((Parameters.parse(_arg2.defense_) >= _local3));
                case StatData.SPEED_STAT:
                    return ((Parameters.parse(_arg2.speed_) >= _local3));
                case StatData.VITALITY_STAT:
                    return ((Parameters.parse(_arg2.vitality_) >= _local3));
                case StatData.WISDOM_STAT:
                    return ((Parameters.parse(_arg2.wisdom_) >= _local3));
                case StatData.DEXTERITY_STAT:
                    return ((Parameters.parse(_arg2.dexterity_) >= _local3));
            }
        }
        return (false);
    }

    public static function getPetDataXMLByType(_arg1:int):XML {
        return (petXMLDataLibrary_[_arg1]);
    }


}
}