﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//io.decagames.rotmg.pets.data.vo.IPetVO

package io.decagames.rotmg.pets.data.vo
{
    import org.osflash.signals.Signal;
    import flash.display.Bitmap;
    import io.decagames.rotmg.pets.data.rarity.PetRarityEnum;
    import com.company.assembleegameclient.util.MaskedImage;

    public interface IPetVO 
    {

        function get updated():Signal;
        function getSkinBitmap():Bitmap;
        function getID():int;
        function getType():int;
        function get name():String;
        function get rarity():PetRarityEnum;
        function get family():String;
        function get abilityList():Array;
        function get isOwned():Boolean;
        function getSkinMaskedImage():MaskedImage;
        function get skinType():int;
        function get maxAbilityPower():int;
        function get isNew():Boolean;
        function set isNew(_arg_1:Boolean):void;

    }
}//package io.decagames.rotmg.pets.data.vo