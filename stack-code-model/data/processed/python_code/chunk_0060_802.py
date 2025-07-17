package net.command
{
    import flash.utils.ByteArray;
    import net.server.QuestServer;

    /**
     * サーバとのコマンドを管理するクラス
     * （自動生成される rake update_command）
     */

    public class QuestCommand extends Command
    {
       private var server:QuestServer;
       public function QuestCommand(s:QuestServer)
        {
            server =s;
            receiveCommands.push(negoCert);
            receiveCommands.push(loginCert);
            receiveCommands.push(loginFail);
            receiveCommands.push(scKeepAlive);
            receiveCommands.push(scEnergyInfo);
            receiveCommands.push(scUpdateEnergyMax);
            receiveCommands.push(scGetQuest);
            receiveCommands.push(scGetExp);
            receiveCommands.push(scLevelUp);
            receiveCommands.push(scUpdateQuestMax);
            receiveCommands.push(scUpdateGems);
            receiveCommands.push(scGetItem);
            receiveCommands.push(scGetSlotCard);
            receiveCommands.push(scGetCharaCard);
            receiveCommands.push(scQuestMapInfo);
            receiveCommands.push(scQuestLogPageInfo);
            receiveCommands.push(scQuestLogInfo);
            receiveCommands.push(scQuestStateUpdate);
            receiveCommands.push(scQuestFindAtUpdate);
            receiveCommands.push(scQuestMapProgressUpdate);
            receiveCommands.push(scDeckStateUpdate);
            receiveCommands.push(scQuestFailed);
            receiveCommands.push(scQuestDeleted);
            receiveCommands.push(scQuestTreasureGot);
            receiveCommands.push(scQuestFinish);
            receiveCommands.push(scGetQuestTreasure);
            receiveCommands.push(scQuestFlagUpdate);
            receiveCommands.push(scFloorCountUpdate);
            receiveCommands.push(scQuestClearNumUpdate);
            receiveCommands.push(scErrorNo);
            receiveCommands.push(scEventQuestFlagUpdate);
            receiveCommands.push(scEventQuestClearNumUpdate);
            receiveCommands.push(scActioncardLength);
            receiveCommands.push(scActioncardInfo);
            receiveCommands.push(scActioncardVerInfo);
            receiveCommands.push(scMessage);
            receiveCommands.push(scMessageStrData);
            receiveCommands.push(scDetermineSession);
            receiveCommands.push(scCharaCardInventoryInfo);
            receiveCommands.push(scOneToOneDuelStart);
            receiveCommands.push(scThreeToThreeDuelStart);
            receiveCommands.push(scOneToOneDuelFinish);
            receiveCommands.push(scThreeToThreeDuelFinish);
            receiveCommands.push(scDuelStartTurnPhase);
            receiveCommands.push(scDuelRefillPhase);
            receiveCommands.push(scDuelRefillEventPhase);
            receiveCommands.push(scDuelMoveCardDropPhaseStart);
            receiveCommands.push(scDuelMoveCardDropPhaseFinish);
            receiveCommands.push(scDuelDetermineMovePhase);
            receiveCommands.push(scDuelCharaChangePhaseStart);
            receiveCommands.push(scDuelCharaChangePhaseFinish);
            receiveCommands.push(scDuelAttackCardDropPhaseStart);
            receiveCommands.push(scDuelAttackCardDropPhaseFinish);
            receiveCommands.push(scDuelDeffenceCardDropPhaseStart);
            receiveCommands.push(scDuelDeffenceCardDropPhaseFinish);
            receiveCommands.push(scDuelDetermineBattlePointPhase);
            receiveCommands.push(scDuelBattleResultPhase);
            receiveCommands.push(scDuelDeadCharaChangePhaseStart);
            receiveCommands.push(scDuelDeadCharaChangePhaseFinish);
            receiveCommands.push(scDuelFinishTurnPhase);
            receiveCommands.push(scEntrantSetDirectionAction);
            receiveCommands.push(scEntrantMoveCardAddAction);
            receiveCommands.push(scEntrantMoveCardRemoveAction);
            receiveCommands.push(scEntrantCardRotateAction);
            receiveCommands.push(scEntrantEventCardRotateAction);
            receiveCommands.push(scEntrantBattleCardAddAction);
            receiveCommands.push(scEntrantBattleCardRemoveAction);
            receiveCommands.push(scEntrantInitDoneAction);
            receiveCommands.push(scEntrantAttackDoneAction);
            receiveCommands.push(scEntrantDeffenceDoneAction);
            receiveCommands.push(scEntrantMoveAction);
            receiveCommands.push(scEntrantHideMoveAction);
            receiveCommands.push(scEntrantCharaChangeAction);
            receiveCommands.push(scEntrantDamagedEvent);
            receiveCommands.push(scEntrantPartyDamagedEvent);
            receiveCommands.push(scEntrantReviveEvent);
            receiveCommands.push(scEntrantConstraintEvent);
            receiveCommands.push(scEntrantHealedEvent);
            receiveCommands.push(scEntrantPartyHealedEvent);
            receiveCommands.push(scEntrantHitPointChangedEvent);
            receiveCommands.push(scEntrantCuredEvent);
            receiveCommands.push(scEntrantSealedEvent);
            receiveCommands.push(scEntrantPointUpdateEvent);
            receiveCommands.push(scEntrantPointRewriteEvent);
            receiveCommands.push(scEntrantUseActionCardEvent);
            receiveCommands.push(scEntrantDiscardEvent);
            receiveCommands.push(scEntrantDiscardTableEvent);
            receiveCommands.push(scEntrantSpecialDealedEvent);
            receiveCommands.push(scEntrantGraveDealedEvent);
            receiveCommands.push(scEntrantStealDealedEvent);
            receiveCommands.push(scEntrantSpecialEventCardDealedEvent);
            receiveCommands.push(scEntrantUpdateCardValueEvent);
            receiveCommands.push(scEntrantUpdateWeaponEvent);
            receiveCommands.push(scEntrantCardsMaxUpdateEvent);
            receiveCommands.push(scEntrantTrapActionEvent);
            receiveCommands.push(scEntrantTrapUpdateEvent);
            receiveCommands.push(scSetFieldStatusEvent);
            receiveCommands.push(scDuelBonusEvent);
            receiveCommands.push(scSetTurnEvent);
            receiveCommands.push(scCardLockEvent);
            receiveCommands.push(scClearCardLocksEvent);
            receiveCommands.push(scDeckInitEvent);
            receiveCommands.push(scActioncardChanceEvent);
            receiveCommands.push(scBuffOnEvent);
            receiveCommands.push(scBuffOffEvent);
            receiveCommands.push(scBuffUpdateEvent);
            receiveCommands.push(scCatStateUpdateEvent);
            receiveCommands.push(scPlFeatOnEvent);
            receiveCommands.push(scPlFeatOffEvent);
            receiveCommands.push(scEntrantChangeFeatEvent);
            receiveCommands.push(scEntrantUseFeatEvent);
            receiveCommands.push(scEntrantUsePassiveEvent);
            receiveCommands.push(scEntrantChangeCharaCardEvent);
            receiveCommands.push(scEntrantOnTransformEvent);
            receiveCommands.push(scEntrantOffTransformEvent);
            receiveCommands.push(scEntrantOnPassiveEvent);
            receiveCommands.push(scEntrantOffPassiveEvent);
            receiveCommands.push(scEntrantOnLostInTheFogEvent);
            receiveCommands.push(scEntrantOffLostInTheFogEvent);
            receiveCommands.push(scEntrantInTheFogEvent);
            receiveCommands.push(scEntrantUpdateFeatConditionEvent);
            receiveCommands.push(scEntrantStuffedToysSetEvent);
            receiveCommands.push(scRewardCandidateCardsList);
            receiveCommands.push(scBottomDiceNum);
            receiveCommands.push(scHighLowResult);
            receiveCommands.push(scRewardResultDice);
            receiveCommands.push(scRewardFinalResult);
            receiveCommands.push(scUseItem);
            receiveCommands.push(scNextSuccess);
            receiveCommands.push(scAchievementClear);
            receiveCommands.push(scAddNewAchievement);
            receiveCommands.push(scDeleteAchievement);
            receiveCommands.push(scUpdateAchievementInfo);
            receiveCommands.push(scGetPart);
            receiveCommands.push(scDialogueInfoUpdate);
            receiveCommands.push(scUpdateCombineWeaponData);

        }
// 送信コマンド

     public function negotiation(uid:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(0);
            cmd.writeInt(uid);

            return cmd;
        }

     public function login(ok:String, crypted_sign:String):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(1);
            cmd.writeUTF(ok);
            cmd.writeUTF(crypted_sign);

            return cmd;
        }

     public function logout():ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(2);

            return cmd;
        }

     public function csKeepAlive():ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(3);

            return cmd;
        }

     public function csAvatarUpdateCheck():ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(4);

            return cmd;
        }

     public function csGetQuest(quest_map_id:int, find_time:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(5);
            cmd.writeInt(quest_map_id);
            cmd.writeInt(find_time);

            return cmd;
        }

     public function csRequestQuestMapInfo(region:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(6);
            cmd.writeInt(region);

            return cmd;
        }

     public function csAvatarUseItem(inv_id:int, quest_map_no:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(7);
            cmd.writeInt(inv_id);
            cmd.writeInt(quest_map_no);

            return cmd;
        }

     public function csAvatarBuyItem(shop_id:int, inv_id:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(8);
            cmd.writeInt(shop_id);
            cmd.writeInt(inv_id);

            return cmd;
        }

     public function csGetQuestLogPageInfo(page:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(9);
            cmd.writeInt(page);

            return cmd;
        }

     public function csGetQuestLogInfo(id:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(10);
            cmd.writeInt(id);

            return cmd;
        }

     public function csSetQuestLog(content:String):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(11);
            cmd.writeUTF(content);

            return cmd;
        }

     public function csQuestConfirm(inv_id:int, deck_index:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(12);
            cmd.writeInt(inv_id);
            cmd.writeByte(deck_index);

            return cmd;
        }

     public function csQuestStart(inv_id:int, deck_index:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(13);
            cmd.writeInt(inv_id);
            cmd.writeByte(deck_index);

            return cmd;
        }

     public function csQuestAbort(inv_id:int, deck_index:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(14);
            cmd.writeInt(inv_id);
            cmd.writeByte(deck_index);

            return cmd;
        }

     public function csQuestDelete(inv_id:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(15);
            cmd.writeInt(inv_id);

            return cmd;
        }

     public function csQuestNextLand(inv_id:int, deck_index:int, next_no:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(16);
            cmd.writeInt(inv_id);
            cmd.writeByte(deck_index);
            cmd.writeByte(next_no);

            return cmd;
        }

     public function csQuestCheckFind(inv_id:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(17);
            cmd.writeInt(inv_id);

            return cmd;
        }

     public function csSendQuest(avt_id:int, inv_id:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(18);
            cmd.writeInt(avt_id);
            cmd.writeInt(inv_id);

            return cmd;
        }

     public function csSelectGameSession(id:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(19);
            cmd.writeInt(id);

            return cmd;
        }

     public function csRequestActioncardInfo(id:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(20);
            cmd.writeInt(id);

            return cmd;
        }

     public function csRequestActioncardVerInfo(id:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(21);
            cmd.writeInt(id);

            return cmd;
        }

     public function csStartOk():ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(22);

            return cmd;
        }

     public function csSetDirection(dir:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(23);
            cmd.writeByte(dir);

            return cmd;
        }

     public function csMoveCardAdd(card:int, index:int, dir:Boolean):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(24);
            cmd.writeInt(card);
            cmd.writeByte(index);
            cmd.writeBoolean(dir);

            return cmd;
        }

     public function csMoveCardRemove(card:int, index:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(25);
            cmd.writeInt(card);
            cmd.writeByte(index);

            return cmd;
        }

     public function csInitDone(card_events:String, chara_events:String):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(26);
            cmd.writeUTF(card_events);
            cmd.writeUTF(chara_events);

            return cmd;
        }

     public function csMoveDone(move:int, card_events:String, chara_events:String):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(27);
            cmd.writeByte(move);
            cmd.writeUTF(card_events);
            cmd.writeUTF(chara_events);

            return cmd;
        }

     public function csAttackCardAdd(card:int, index:int, dir:Boolean):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(28);
            cmd.writeInt(card);
            cmd.writeByte(index);
            cmd.writeBoolean(dir);

            return cmd;
        }

     public function csAttackCardRemove(card:int, index:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(29);
            cmd.writeInt(card);
            cmd.writeByte(index);

            return cmd;
        }

     public function csDeffenceCardAdd(card:int, index:int, dir:Boolean):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(30);
            cmd.writeInt(card);
            cmd.writeByte(index);
            cmd.writeBoolean(dir);

            return cmd;
        }

     public function csDeffenceCardRemove(card:int, index:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(31);
            cmd.writeInt(card);
            cmd.writeByte(index);

            return cmd;
        }

     public function csCardRotate(card:int, table:int, index:int, up:Boolean):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(32);
            cmd.writeInt(card);
            cmd.writeByte(table);
            cmd.writeByte(index);
            cmd.writeBoolean(up);

            return cmd;
        }

     public function csAttackDone(card_events:String, chara_events:String):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(33);
            cmd.writeUTF(card_events);
            cmd.writeUTF(chara_events);

            return cmd;
        }

     public function csDeffenceDone(card_events:String, chara_events:String):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(34);
            cmd.writeUTF(card_events);
            cmd.writeUTF(chara_events);

            return cmd;
        }

     public function csCharaChange(index:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(35);
            cmd.writeByte(index);

            return cmd;
        }

     public function csResultUp():ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(36);

            return cmd;
        }

     public function csResultDown():ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(37);

            return cmd;
        }

     public function csResultCancel():ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(38);

            return cmd;
        }

     public function csRetryReward():ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(39);

            return cmd;
        }

     public function csDebugCode(code:int):ByteArray
     {
        var cmd:ByteArray = new ByteArray();
            cmd.writeShort(40);
            cmd.writeByte(code);

            return cmd;
        }

// 受信コマンド

     private function negoCert(ba:ByteArray):void
     {
            var crypted_sign_length:int;
            crypted_sign_length = ba.readUnsignedInt();
            var crypted_sign:String;
            crypted_sign = ba.readUTFBytes(crypted_sign_length);
            var ok_length:int;
            ok_length = ba.readUnsignedInt();
            var ok:String;
            ok = ba.readUTFBytes(ok_length);
            server.negoCert(crypted_sign, ok);
      }


     private function loginCert(ba:ByteArray):void
     {
            var msg_length:int;
            msg_length = ba.readUnsignedInt();
            var msg:String;
            msg = ba.readUTFBytes(msg_length);
            var hash_key_length:int;
            hash_key_length = ba.readUnsignedInt();
            var hash_key:String;
            hash_key = ba.readUTFBytes(hash_key_length);
            server.loginCert(msg, hash_key);
      }


     private function loginFail(ba:ByteArray):void
     {
            server.loginFail();
      }


     private function scKeepAlive(ba:ByteArray):void
     {
            server.scKeepAlive();
      }


     private function scEnergyInfo(ba:ByteArray):void
     {
            var energy:int;
            energy = ba.readInt();
            var remainTime:int;
            remainTime = ba.readInt();
            server.scEnergyInfo(energy, remainTime);
      }


     private function scUpdateEnergyMax(ba:ByteArray):void
     {
            var energy_max:int;
            energy_max = ba.readInt();
            server.scUpdateEnergyMax(energy_max);
      }


     private function scGetQuest(ba:ByteArray):void
     {
            var inv_id:int;
            inv_id = ba.readInt();
            var quest_id:int;
            quest_id = ba.readInt();
            var find_at:int;
            find_at = ba.readInt();
            var pow:int;
            pow = ba.readInt();
            var state:int;
            state = ba.readByte();
            var ba_name_length:int;
            ba_name_length = ba.readUnsignedInt();
            var ba_name:String;
            ba_name = ba.readUTFBytes(ba_name_length);
            server.scGetQuest(inv_id, quest_id, find_at, pow, state, ba_name);
      }


     private function scGetExp(ba:ByteArray):void
     {
            var exp:int;
            exp = ba.readInt();
            server.scGetExp(exp);
      }


     private function scLevelUp(ba:ByteArray):void
     {
            var level:int;
            level = ba.readInt();
            server.scLevelUp(level);
      }


     private function scUpdateQuestMax(ba:ByteArray):void
     {
            var quest_max:int;
            quest_max = ba.readInt();
            server.scUpdateQuestMax(quest_max);
      }


     private function scUpdateGems(ba:ByteArray):void
     {
            var gems:int;
            gems = ba.readInt();
            server.scUpdateGems(gems);
      }


     private function scGetItem(ba:ByteArray):void
     {
            var inv_id:int;
            inv_id = ba.readInt();
            var item_id:int;
            item_id = ba.readInt();
            server.scGetItem(inv_id, item_id);
      }


     private function scGetSlotCard(ba:ByteArray):void
     {
            var inv_id:int;
            inv_id = ba.readInt();
            var kind:int;
            kind = ba.readInt();
            var card_id:int;
            card_id = ba.readInt();
            server.scGetSlotCard(inv_id, kind, card_id);
      }


     private function scGetCharaCard(ba:ByteArray):void
     {
            var inv_id:int;
            inv_id = ba.readInt();
            var card_id:int;
            card_id = ba.readInt();
            server.scGetCharaCard(inv_id, card_id);
      }


     private function scQuestMapInfo(ba:ByteArray):void
     {
            var region:int;
            region = ba.readInt();
            var map_list_length:int;
            map_list_length = ba.readUnsignedInt();
            var map_list:String;
            map_list = ba.readUTFBytes(map_list_length);
            server.scQuestMapInfo(region, map_list);
      }


     private function scQuestLogPageInfo(ba:ByteArray):void
     {
            var page:int;
            page = ba.readInt();
            var content_ids_length:int;
            content_ids_length = ba.readUnsignedInt();
            var content_ids:String;
            content_ids = ba.readUTFBytes(content_ids_length);
            server.scQuestLogPageInfo(page, content_ids);
      }


     private function scQuestLogInfo(ba:ByteArray):void
     {
            var id:int;
            id = ba.readInt();
            var content_length:int;
            content_length = ba.readUnsignedInt();
            var content:String;
            content = ba.readUTFBytes(content_length);
            server.scQuestLogInfo(id, content);
      }


     private function scQuestStateUpdate(ba:ByteArray):void
     {
            var inv_id:int;
            inv_id = ba.readInt();
            var state:int;
            state = ba.readByte();
            var quest_id:int;
            quest_id = ba.readInt();
            server.scQuestStateUpdate(inv_id, state, quest_id);
      }


     private function scQuestFindAtUpdate(ba:ByteArray):void
     {
            var inv_id:int;
            inv_id = ba.readInt();
            var find_at:int;
            find_at = ba.readInt();
            server.scQuestFindAtUpdate(inv_id, find_at);
      }


     private function scQuestMapProgressUpdate(ba:ByteArray):void
     {
            var inv_id:int;
            inv_id = ba.readInt();
            var progress:int;
            progress = ba.readInt();
            server.scQuestMapProgressUpdate(inv_id, progress);
      }


     private function scDeckStateUpdate(ba:ByteArray):void
     {
            var deck_index:int;
            deck_index = ba.readByte();
            var state:int;
            state = ba.readByte();
            var hp_0:int;
            hp_0 = ba.readByte();
            var hp_1:int;
            hp_1 = ba.readByte();
            var hp_2:int;
            hp_2 = ba.readByte();
            server.scDeckStateUpdate(deck_index, state, hp_0, hp_1, hp_2);
      }


     private function scQuestFailed(ba:ByteArray):void
     {
            var inv_id:int;
            inv_id = ba.readInt();
            server.scQuestFailed(inv_id);
      }


     private function scQuestDeleted(ba:ByteArray):void
     {
            var inv_id:int;
            inv_id = ba.readInt();
            server.scQuestDeleted(inv_id);
      }


     private function scQuestTreasureGot(ba:ByteArray):void
     {
            var type:int;
            type = ba.readByte();
            var id:int;
            id = ba.readInt();
            server.scQuestTreasureGot(type, id);
      }


     private function scQuestFinish(ba:ByteArray):void
     {
            var result:int;
            result = ba.readByte();
            var id:int;
            id = ba.readInt();
            server.scQuestFinish(result, id);
      }


     private function scGetQuestTreasure(ba:ByteArray):void
     {
            var type:int;
            type = ba.readByte();
            var c_type:int;
            c_type = ba.readInt();
            var value:int;
            value = ba.readInt();
            server.scGetQuestTreasure(type, c_type, value);
      }


     private function scQuestFlagUpdate(ba:ByteArray):void
     {
            var flag:int;
            flag = ba.readInt();
            server.scQuestFlagUpdate(flag);
      }


     private function scFloorCountUpdate(ba:ByteArray):void
     {
            var flag:int;
            flag = ba.readInt();
            server.scFloorCountUpdate(flag);
      }


     private function scQuestClearNumUpdate(ba:ByteArray):void
     {
            var clear_num:int;
            clear_num = ba.readInt();
            server.scQuestClearNumUpdate(clear_num);
      }


     private function scErrorNo(ba:ByteArray):void
     {
            var error_type:int;
            error_type = ba.readInt();
            server.scErrorNo(error_type);
      }


     private function scEventQuestFlagUpdate(ba:ByteArray):void
     {
            var quest_type:int;
            quest_type = ba.readInt();
            var flag:int;
            flag = ba.readInt();
            server.scEventQuestFlagUpdate(quest_type, flag);
      }


     private function scEventQuestClearNumUpdate(ba:ByteArray):void
     {
            var quest_type:int;
            quest_type = ba.readInt();
            var clear_num:int;
            clear_num = ba.readInt();
            server.scEventQuestClearNumUpdate(quest_type, clear_num);
      }


     private function scActioncardLength(ba:ByteArray):void
     {
            var length:int;
            length = ba.readInt();
            server.scActioncardLength(length);
      }


     private function scActioncardInfo(ba:ByteArray):void
     {
            var id:int;
            id = ba.readInt();
            var ut:int;
            ut = ba.readByte();
            var uv:int;
            uv = ba.readByte();
            var bt:int;
            bt = ba.readByte();
            var bv:int;
            bv = ba.readByte();
            var en:int;
            en = ba.readByte();
            var image_length:int;
            image_length = ba.readUnsignedInt();
            var image:String;
            image = ba.readUTFBytes(image_length);
            var caption_length:int;
            caption_length = ba.readUnsignedInt();
            var caption:String;
            caption = ba.readUTFBytes(caption_length);
            var version:int;
            version = ba.readInt();
            server.scActioncardInfo(id, ut, uv, bt, bv, en, image, caption, version);
      }


     private function scActioncardVerInfo(ba:ByteArray):void
     {
            var id:int;
            id = ba.readInt();
            var version:int;
            version = ba.readInt();
            server.scActioncardVerInfo(id, version);
      }


     private function scMessage(ba:ByteArray):void
     {
            var msg_length:int;
            msg_length = ba.readUnsignedInt();
            var msg:String;
            msg = ba.readUTFBytes(msg_length);
            server.scMessage(msg);
      }


     private function scMessageStrData(ba:ByteArray):void
     {
            var str_length:int;
            str_length = ba.readUnsignedInt();
            var str:String;
            str = ba.readUTFBytes(str_length);
            server.scMessageStrData(str);
      }


     private function scDetermineSession(ba:ByteArray):void
     {
            var id:int;
            id = ba.readInt();
            var foe_length:int;
            foe_length = ba.readUnsignedInt();
            var foe:String;
            foe = ba.readUTFBytes(foe_length);
            var player_chara_card_id_length:int;
            player_chara_card_id_length = ba.readUnsignedInt();
            var player_chara_card_id:String;
            player_chara_card_id = ba.readUTFBytes(player_chara_card_id_length);
            var foe_chara_card_id_length:int;
            foe_chara_card_id_length = ba.readUnsignedInt();
            var foe_chara_card_id:String;
            foe_chara_card_id = ba.readUTFBytes(foe_chara_card_id_length);
            var start_dialogue_length:int;
            start_dialogue_length = ba.readUnsignedInt();
            var start_dialogue:String;
            start_dialogue = ba.readUTFBytes(start_dialogue_length);
            var foe_dialogue_length:int;
            foe_dialogue_length = ba.readUnsignedInt();
            var foe_dialogue:String;
            foe_dialogue = ba.readUTFBytes(foe_dialogue_length);
            var stage:int;
            stage = ba.readByte();
            var pl_hp0:int;
            pl_hp0 = ba.readByte();
            var pl_hp1:int;
            pl_hp1 = ba.readByte();
            var pl_hp2:int;
            pl_hp2 = ba.readByte();
            var foe_hp0:int;
            foe_hp0 = ba.readByte();
            var foe_hp1:int;
            foe_hp1 = ba.readByte();
            var foe_hp2:int;
            foe_hp2 = ba.readByte();
            server.scDetermineSession(id, foe, player_chara_card_id, foe_chara_card_id, start_dialogue, foe_dialogue, stage, pl_hp0, pl_hp1, pl_hp2, foe_hp0, foe_hp1, foe_hp2);
      }


     private function scCharaCardInventoryInfo(ba:ByteArray):void
     {
            var inv_id_length:int;
            inv_id_length = ba.readUnsignedInt();
            var inv_id:String;
            inv_id = ba.readUTFBytes(inv_id_length);
            var card_id_length:int;
            card_id_length = ba.readUnsignedInt();
            var card_id:String;
            card_id = ba.readUTFBytes(card_id_length);
            server.scCharaCardInventoryInfo(inv_id, card_id);
      }


     private function scOneToOneDuelStart(ba:ByteArray):void
     {
            var deck_size:int;
            deck_size = ba.readByte();
            var player_event_deck_size:int;
            player_event_deck_size = ba.readByte();
            var foe_deck_size:int;
            foe_deck_size = ba.readByte();
            var distance:int;
            distance = ba.readByte();
            server.scOneToOneDuelStart(deck_size, player_event_deck_size, foe_deck_size, distance);
      }


     private function scThreeToThreeDuelStart(ba:ByteArray):void
     {
            var deck_size:int;
            deck_size = ba.readByte();
            var player_event_deck_size:int;
            player_event_deck_size = ba.readByte();
            var foe_event_deck_size:int;
            foe_event_deck_size = ba.readByte();
            var distance:int;
            distance = ba.readByte();
            var multi:Boolean;
            multi = ba.readBoolean();
            server.scThreeToThreeDuelStart(deck_size, player_event_deck_size, foe_event_deck_size, distance, multi);
      }


     private function scOneToOneDuelFinish(ba:ByteArray):void
     {
            var result:int;
            result = ba.readByte();
            var gems:int;
            gems = ba.readInt();
            var exp:int;
            exp = ba.readInt();
            var exp_bonus:int;
            exp_bonus = ba.readInt();
            var gems_pow:int;
            gems_pow = ba.readInt();
            var exp_pow:int;
            exp_pow = ba.readInt();
            var gems_total:int;
            gems_total = ba.readInt();
            var exp_total:int;
            exp_total = ba.readInt();
            var bonus:Boolean;
            bonus = ba.readBoolean();
            server.scOneToOneDuelFinish(result, gems, exp, exp_bonus, gems_pow, exp_pow, gems_total, exp_total, bonus);
      }


     private function scThreeToThreeDuelFinish(ba:ByteArray):void
     {
            var result:int;
            result = ba.readByte();
            var gems:int;
            gems = ba.readInt();
            var exp:int;
            exp = ba.readInt();
            var bonus:Boolean;
            bonus = ba.readBoolean();
            server.scThreeToThreeDuelFinish(result, gems, exp, bonus);
      }


     private function scDuelStartTurnPhase(ba:ByteArray):void
     {
            var turn_count:int;
            turn_count = ba.readByte();
            server.scDuelStartTurnPhase(turn_count);
      }


     private function scDuelRefillPhase(ba:ByteArray):void
     {
            var list_length:int;
            list_length = ba.readUnsignedInt();
            var list:String;
            list = ba.readUTFBytes(list_length);
            var dir:int;
            dir = ba.readInt();
            var foe_size:int;
            foe_size = ba.readByte();
            server.scDuelRefillPhase(list, dir, foe_size);
      }


     private function scDuelRefillEventPhase(ba:ByteArray):void
     {
            var list_length:int;
            list_length = ba.readUnsignedInt();
            var list:String;
            list = ba.readUTFBytes(list_length);
            var dir:int;
            dir = ba.readInt();
            var foe_size:int;
            foe_size = ba.readByte();
            server.scDuelRefillEventPhase(list, dir, foe_size);
      }


     private function scDuelMoveCardDropPhaseStart(ba:ByteArray):void
     {
            server.scDuelMoveCardDropPhaseStart();
      }


     private function scDuelMoveCardDropPhaseFinish(ba:ByteArray):void
     {
            server.scDuelMoveCardDropPhaseFinish();
      }


     private function scDuelDetermineMovePhase(ba:ByteArray):void
     {
            var init:Boolean;
            init = ba.readBoolean();
            var dist:int;
            dist = ba.readByte();
            var list_length:int;
            list_length = ba.readUnsignedInt();
            var list:String;
            list = ba.readUTFBytes(list_length);
            var dir_length:int;
            dir_length = ba.readUnsignedInt();
            var dir:String;
            dir = ba.readUTFBytes(dir_length);
            var foe_list_length:int;
            foe_list_length = ba.readUnsignedInt();
            var foe_list:String;
            foe_list = ba.readUTFBytes(foe_list_length);
            var foe_dir_length:int;
            foe_dir_length = ba.readUnsignedInt();
            var foe_dir:String;
            foe_dir = ba.readUTFBytes(foe_dir_length);
            var pow:int;
            pow = ba.readByte();
            var foe_pow:int;
            foe_pow = ba.readByte();
            var lock:Boolean;
            lock = ba.readBoolean();
            var foe_lock:Boolean;
            foe_lock = ba.readBoolean();
            server.scDuelDetermineMovePhase(init, dist, list, dir, foe_list, foe_dir, pow, foe_pow, lock, foe_lock);
      }


     private function scDuelCharaChangePhaseStart(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var foe:Boolean;
            foe = ba.readBoolean();
            server.scDuelCharaChangePhaseStart(player, foe);
      }


     private function scDuelCharaChangePhaseFinish(ba:ByteArray):void
     {
            server.scDuelCharaChangePhaseFinish();
      }


     private function scDuelAttackCardDropPhaseStart(ba:ByteArray):void
     {
            var attack:Boolean;
            attack = ba.readBoolean();
            server.scDuelAttackCardDropPhaseStart(attack);
      }


     private function scDuelAttackCardDropPhaseFinish(ba:ByteArray):void
     {
            var list_length:int;
            list_length = ba.readUnsignedInt();
            var list:String;
            list = ba.readUTFBytes(list_length);
            var dir_length:int;
            dir_length = ba.readUnsignedInt();
            var dir:String;
            dir = ba.readUTFBytes(dir_length);
            var foe_list_length:int;
            foe_list_length = ba.readUnsignedInt();
            var foe_list:String;
            foe_list = ba.readUTFBytes(foe_list_length);
            var foe_dir_length:int;
            foe_dir_length = ba.readUnsignedInt();
            var foe_dir:String;
            foe_dir = ba.readUTFBytes(foe_dir_length);
            var lock:Boolean;
            lock = ba.readBoolean();
            var foe_lock:Boolean;
            foe_lock = ba.readBoolean();
            server.scDuelAttackCardDropPhaseFinish(list, dir, foe_list, foe_dir, lock, foe_lock);
      }


     private function scDuelDeffenceCardDropPhaseStart(ba:ByteArray):void
     {
            var deffence:Boolean;
            deffence = ba.readBoolean();
            server.scDuelDeffenceCardDropPhaseStart(deffence);
      }


     private function scDuelDeffenceCardDropPhaseFinish(ba:ByteArray):void
     {
            var list_length:int;
            list_length = ba.readUnsignedInt();
            var list:String;
            list = ba.readUTFBytes(list_length);
            var dir_length:int;
            dir_length = ba.readUnsignedInt();
            var dir:String;
            dir = ba.readUTFBytes(dir_length);
            var foe_list_length:int;
            foe_list_length = ba.readUnsignedInt();
            var foe_list:String;
            foe_list = ba.readUTFBytes(foe_list_length);
            var foe_dir_length:int;
            foe_dir_length = ba.readUnsignedInt();
            var foe_dir:String;
            foe_dir = ba.readUTFBytes(foe_dir_length);
            var lock:Boolean;
            lock = ba.readBoolean();
            var foe_lock:Boolean;
            foe_lock = ba.readBoolean();
            server.scDuelDeffenceCardDropPhaseFinish(list, dir, foe_list, foe_dir, lock, foe_lock);
      }


     private function scDuelDetermineBattlePointPhase(ba:ByteArray):void
     {
            var list_length:int;
            list_length = ba.readUnsignedInt();
            var list:String;
            list = ba.readUTFBytes(list_length);
            var dir_length:int;
            dir_length = ba.readUnsignedInt();
            var dir:String;
            dir = ba.readUTFBytes(dir_length);
            var foe_list_length:int;
            foe_list_length = ba.readUnsignedInt();
            var foe_list:String;
            foe_list = ba.readUTFBytes(foe_list_length);
            var foe_dir_length:int;
            foe_dir_length = ba.readUnsignedInt();
            var foe_dir:String;
            foe_dir = ba.readUTFBytes(foe_dir_length);
            var lock:Boolean;
            lock = ba.readBoolean();
            var foe_lock:Boolean;
            foe_lock = ba.readBoolean();
            server.scDuelDetermineBattlePointPhase(list, dir, foe_list, foe_dir, lock, foe_lock);
      }


     private function scDuelBattleResultPhase(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var attack_dice_length:int;
            attack_dice_length = ba.readUnsignedInt();
            var attack_dice:String;
            attack_dice = ba.readUTFBytes(attack_dice_length);
            var deffence_dice_length:int;
            deffence_dice_length = ba.readUnsignedInt();
            var deffence_dice:String;
            deffence_dice = ba.readUTFBytes(deffence_dice_length);
            server.scDuelBattleResultPhase(player, attack_dice, deffence_dice);
      }


     private function scDuelDeadCharaChangePhaseStart(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var foe:Boolean;
            foe = ba.readBoolean();
            var list_length:int;
            list_length = ba.readUnsignedInt();
            var list:String;
            list = ba.readUTFBytes(list_length);
            var foe_list_length:int;
            foe_list_length = ba.readUnsignedInt();
            var foe_list:String;
            foe_list = ba.readUTFBytes(foe_list_length);
            server.scDuelDeadCharaChangePhaseStart(player, foe, list, foe_list);
      }


     private function scDuelDeadCharaChangePhaseFinish(ba:ByteArray):void
     {
            server.scDuelDeadCharaChangePhaseFinish();
      }


     private function scDuelFinishTurnPhase(ba:ByteArray):void
     {
            server.scDuelFinishTurnPhase();
      }


     private function scEntrantSetDirectionAction(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var dir:int;
            dir = ba.readByte();
            server.scEntrantSetDirectionAction(player, dir);
      }


     private function scEntrantMoveCardAddAction(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var index:int;
            index = ba.readByte();
            var id:int;
            id = ba.readInt();
            server.scEntrantMoveCardAddAction(player, index, id);
      }


     private function scEntrantMoveCardRemoveAction(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var index:int;
            index = ba.readByte();
            var id:int;
            id = ba.readInt();
            server.scEntrantMoveCardRemoveAction(player, index, id);
      }


     private function scEntrantCardRotateAction(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var table:int;
            table = ba.readByte();
            var index:int;
            index = ba.readByte();
            var id:int;
            id = ba.readInt();
            var dir:Boolean;
            dir = ba.readBoolean();
            server.scEntrantCardRotateAction(player, table, index, id, dir);
      }


     private function scEntrantEventCardRotateAction(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var table:int;
            table = ba.readByte();
            var index:int;
            index = ba.readByte();
            var id:int;
            id = ba.readInt();
            var dir:Boolean;
            dir = ba.readBoolean();
            server.scEntrantEventCardRotateAction(player, table, index, id, dir);
      }


     private function scEntrantBattleCardAddAction(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var index:int;
            index = ba.readByte();
            var id:int;
            id = ba.readInt();
            server.scEntrantBattleCardAddAction(player, index, id);
      }


     private function scEntrantBattleCardRemoveAction(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var index:int;
            index = ba.readByte();
            var id:int;
            id = ba.readInt();
            server.scEntrantBattleCardRemoveAction(player, index, id);
      }


     private function scEntrantInitDoneAction(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            server.scEntrantInitDoneAction(player);
      }


     private function scEntrantAttackDoneAction(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            server.scEntrantAttackDoneAction(player);
      }


     private function scEntrantDeffenceDoneAction(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            server.scEntrantDeffenceDoneAction(player);
      }


     private function scEntrantMoveAction(ba:ByteArray):void
     {
            var dist:int;
            dist = ba.readByte();
            server.scEntrantMoveAction(dist);
      }


     private function scEntrantHideMoveAction(ba:ByteArray):void
     {
            var dist:int;
            dist = ba.readByte();
            server.scEntrantHideMoveAction(dist);
      }


     private function scEntrantCharaChangeAction(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var index:int;
            index = ba.readByte();
            var card_id:int;
            card_id = ba.readInt();
            var weapon_bonus_length:int;
            weapon_bonus_length = ba.readUnsignedInt();
            var weapon_bonus:String;
            weapon_bonus = ba.readUTFBytes(weapon_bonus_length);
            server.scEntrantCharaChangeAction(player, index, card_id, weapon_bonus);
      }


     private function scEntrantDamagedEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var damage:int;
            damage = ba.readInt();
            var is_not_hostile:Boolean;
            is_not_hostile = ba.readBoolean();
            server.scEntrantDamagedEvent(player, damage, is_not_hostile);
      }


     private function scEntrantPartyDamagedEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var index:int;
            index = ba.readInt();
            var damage:int;
            damage = ba.readInt();
            var is_not_hostile:Boolean;
            is_not_hostile = ba.readBoolean();
            server.scEntrantPartyDamagedEvent(player, index, damage, is_not_hostile);
      }


     private function scEntrantReviveEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var index:int;
            index = ba.readInt();
            var rhp:int;
            rhp = ba.readInt();
            server.scEntrantReviveEvent(player, index, rhp);
      }


     private function scEntrantConstraintEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var flag:int;
            flag = ba.readInt();
            server.scEntrantConstraintEvent(player, flag);
      }


     private function scEntrantHealedEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var heal:int;
            heal = ba.readByte();
            server.scEntrantHealedEvent(player, heal);
      }


     private function scEntrantPartyHealedEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var index:int;
            index = ba.readInt();
            var heal:int;
            heal = ba.readByte();
            server.scEntrantPartyHealedEvent(player, index, heal);
      }


     private function scEntrantHitPointChangedEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var hp:int;
            hp = ba.readInt();
            server.scEntrantHitPointChangedEvent(player, hp);
      }


     private function scEntrantCuredEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            server.scEntrantCuredEvent(player);
      }


     private function scEntrantSealedEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            server.scEntrantSealedEvent(player);
      }


     private function scEntrantPointUpdateEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var list_length:int;
            list_length = ba.readUnsignedInt();
            var list:String;
            list = ba.readUTFBytes(list_length);
            var dir:int;
            dir = ba.readInt();
            var point:int;
            point = ba.readInt();
            server.scEntrantPointUpdateEvent(player, list, dir, point);
      }


     private function scEntrantPointRewriteEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var point:int;
            point = ba.readInt();
            server.scEntrantPointRewriteEvent(player, point);
      }


     private function scEntrantUseActionCardEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var used_card_id:int;
            used_card_id = ba.readInt();
            server.scEntrantUseActionCardEvent(player, used_card_id);
      }


     private function scEntrantDiscardEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var discard_id:int;
            discard_id = ba.readInt();
            server.scEntrantDiscardEvent(player, discard_id);
      }


     private function scEntrantDiscardTableEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var discard_id:int;
            discard_id = ba.readInt();
            server.scEntrantDiscardTableEvent(player, discard_id);
      }


     private function scEntrantSpecialDealedEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var list_length:int;
            list_length = ba.readUnsignedInt();
            var list:String;
            list = ba.readUTFBytes(list_length);
            var dir:int;
            dir = ba.readInt();
            var size:int;
            size = ba.readInt();
            server.scEntrantSpecialDealedEvent(player, list, dir, size);
      }


     private function scEntrantGraveDealedEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var list_length:int;
            list_length = ba.readUnsignedInt();
            var list:String;
            list = ba.readUTFBytes(list_length);
            var dir:int;
            dir = ba.readInt();
            var size:int;
            size = ba.readInt();
            server.scEntrantGraveDealedEvent(player, list, dir, size);
      }


     private function scEntrantStealDealedEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var list_length:int;
            list_length = ba.readUnsignedInt();
            var list:String;
            list = ba.readUTFBytes(list_length);
            var dir:int;
            dir = ba.readInt();
            var size:int;
            size = ba.readInt();
            server.scEntrantStealDealedEvent(player, list, dir, size);
      }


     private function scEntrantSpecialEventCardDealedEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var list_length:int;
            list_length = ba.readUnsignedInt();
            var list:String;
            list = ba.readUTFBytes(list_length);
            var dir:int;
            dir = ba.readInt();
            var size:int;
            size = ba.readInt();
            server.scEntrantSpecialEventCardDealedEvent(player, list, dir, size);
      }


     private function scEntrantUpdateCardValueEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var id:int;
            id = ba.readInt();
            var u_value:int;
            u_value = ba.readInt();
            var b_value:int;
            b_value = ba.readInt();
            var reset:Boolean;
            reset = ba.readBoolean();
            server.scEntrantUpdateCardValueEvent(player, id, u_value, b_value, reset);
      }


     private function scEntrantUpdateWeaponEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var pl_bonus_length:int;
            pl_bonus_length = ba.readUnsignedInt();
            var pl_bonus:String;
            pl_bonus = ba.readUTFBytes(pl_bonus_length);
            var foe_bonus_length:int;
            foe_bonus_length = ba.readUnsignedInt();
            var foe_bonus:String;
            foe_bonus = ba.readUTFBytes(foe_bonus_length);
            server.scEntrantUpdateWeaponEvent(player, pl_bonus, foe_bonus);
      }


     private function scEntrantCardsMaxUpdateEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var cards_max:int;
            cards_max = ba.readByte();
            server.scEntrantCardsMaxUpdateEvent(player, cards_max);
      }


     private function scEntrantTrapActionEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var kind:int;
            kind = ba.readInt();
            var distance:int;
            distance = ba.readInt();
            server.scEntrantTrapActionEvent(player, kind, distance);
      }


     private function scEntrantTrapUpdateEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var kind:int;
            kind = ba.readInt();
            var distance:int;
            distance = ba.readInt();
            var turn:int;
            turn = ba.readInt();
            var visible:Boolean;
            visible = ba.readBoolean();
            server.scEntrantTrapUpdateEvent(player, kind, distance, turn, visible);
      }


     private function scSetFieldStatusEvent(ba:ByteArray):void
     {
            var kind:int;
            kind = ba.readInt();
            var pow:int;
            pow = ba.readInt();
            var turn:int;
            turn = ba.readInt();
            server.scSetFieldStatusEvent(kind, pow, turn);
      }


     private function scDuelBonusEvent(ba:ByteArray):void
     {
            var bonus_type:int;
            bonus_type = ba.readByte();
            var value:int;
            value = ba.readByte();
            server.scDuelBonusEvent(bonus_type, value);
      }


     private function scSetTurnEvent(ba:ByteArray):void
     {
            var turn:int;
            turn = ba.readInt();
            server.scSetTurnEvent(turn);
      }


     private function scCardLockEvent(ba:ByteArray):void
     {
            var id:int;
            id = ba.readInt();
            server.scCardLockEvent(id);
      }


     private function scClearCardLocksEvent(ba:ByteArray):void
     {
            server.scClearCardLocksEvent();
      }


     private function scDeckInitEvent(ba:ByteArray):void
     {
            var deck_size:int;
            deck_size = ba.readByte();
            server.scDeckInitEvent(deck_size);
      }


     private function scActioncardChanceEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var list_length:int;
            list_length = ba.readUnsignedInt();
            var list:String;
            list = ba.readUTFBytes(list_length);
            var dir:int;
            dir = ba.readInt();
            var size:int;
            size = ba.readInt();
            server.scActioncardChanceEvent(player, list, dir, size);
      }


     private function scBuffOnEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var index:int;
            index = ba.readInt();
            var buff_id:int;
            buff_id = ba.readInt();
            var value:int;
            value = ba.readInt();
            var turn:int;
            turn = ba.readInt();
            server.scBuffOnEvent(player, index, buff_id, value, turn);
      }


     private function scBuffOffEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var index:int;
            index = ba.readInt();
            var buff_id:int;
            buff_id = ba.readInt();
            var value:int;
            value = ba.readInt();
            server.scBuffOffEvent(player, index, buff_id, value);
      }


     private function scBuffUpdateEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var buff_id:int;
            buff_id = ba.readInt();
            var value:int;
            value = ba.readInt();
            var index:int;
            index = ba.readInt();
            var turn:int;
            turn = ba.readInt();
            server.scBuffUpdateEvent(player, buff_id, value, index, turn);
      }


     private function scCatStateUpdateEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var index:int;
            index = ba.readInt();
            var value:Boolean;
            value = ba.readBoolean();
            server.scCatStateUpdateEvent(player, index, value);
      }


     private function scPlFeatOnEvent(ba:ByteArray):void
     {
            var feat_id:int;
            feat_id = ba.readInt();
            server.scPlFeatOnEvent(feat_id);
      }


     private function scPlFeatOffEvent(ba:ByteArray):void
     {
            var feat_id:int;
            feat_id = ba.readInt();
            server.scPlFeatOffEvent(feat_id);
      }


     private function scEntrantChangeFeatEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var chara_index:int;
            chara_index = ba.readInt();
            var feat_index:int;
            feat_index = ba.readInt();
            var feat_id:int;
            feat_id = ba.readInt();
            var feat_no:int;
            feat_no = ba.readInt();
            server.scEntrantChangeFeatEvent(player, chara_index, feat_index, feat_id, feat_no);
      }


     private function scEntrantUseFeatEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var used_feat_id:int;
            used_feat_id = ba.readInt();
            server.scEntrantUseFeatEvent(player, used_feat_id);
      }


     private function scEntrantUsePassiveEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var used_passive_id:int;
            used_passive_id = ba.readInt();
            server.scEntrantUsePassiveEvent(player, used_passive_id);
      }


     private function scEntrantChangeCharaCardEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var chara_card_id:int;
            chara_card_id = ba.readInt();
            server.scEntrantChangeCharaCardEvent(player, chara_card_id);
      }


     private function scEntrantOnTransformEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var transform_type:int;
            transform_type = ba.readInt();
            server.scEntrantOnTransformEvent(player, transform_type);
      }


     private function scEntrantOffTransformEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            server.scEntrantOffTransformEvent(player);
      }


     private function scEntrantOnPassiveEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var skill_id:int;
            skill_id = ba.readInt();
            server.scEntrantOnPassiveEvent(player, skill_id);
      }


     private function scEntrantOffPassiveEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var skill_id:int;
            skill_id = ba.readInt();
            server.scEntrantOffPassiveEvent(player, skill_id);
      }


     private function scEntrantOnLostInTheFogEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var distance:int;
            distance = ba.readInt();
            var truth_distance:int;
            truth_distance = ba.readInt();
            server.scEntrantOnLostInTheFogEvent(player, distance, truth_distance);
      }


     private function scEntrantOffLostInTheFogEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var distance:int;
            distance = ba.readInt();
            server.scEntrantOffLostInTheFogEvent(player, distance);
      }


     private function scEntrantInTheFogEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var range_length:int;
            range_length = ba.readUnsignedInt();
            var range:String;
            range = ba.readUTFBytes(range_length);
            server.scEntrantInTheFogEvent(player, range);
      }


     private function scEntrantUpdateFeatConditionEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var chara_index:int;
            chara_index = ba.readInt();
            var feat_index:int;
            feat_index = ba.readInt();
            var condition_length:int;
            condition_length = ba.readUnsignedInt();
            var condition:String;
            condition = ba.readUTFBytes(condition_length);
            server.scEntrantUpdateFeatConditionEvent(player, chara_index, feat_index, condition);
      }


     private function scEntrantStuffedToysSetEvent(ba:ByteArray):void
     {
            var player:Boolean;
            player = ba.readBoolean();
            var num:int;
            num = ba.readInt();
            server.scEntrantStuffedToysSetEvent(player, num);
      }


     private function scRewardCandidateCardsList(ba:ByteArray):void
     {
            var candidate_list_1_length:int;
            candidate_list_1_length = ba.readUnsignedInt();
            var candidate_list_1:String;
            candidate_list_1 = ba.readUTFBytes(candidate_list_1_length);
            var candidate_list_2_length:int;
            candidate_list_2_length = ba.readUnsignedInt();
            var candidate_list_2:String;
            candidate_list_2 = ba.readUTFBytes(candidate_list_2_length);
            var candidate_list_3_length:int;
            candidate_list_3_length = ba.readUnsignedInt();
            var candidate_list_3:String;
            candidate_list_3 = ba.readUTFBytes(candidate_list_3_length);
            var candidate_list_4_length:int;
            candidate_list_4_length = ba.readUnsignedInt();
            var candidate_list_4:String;
            candidate_list_4 = ba.readUTFBytes(candidate_list_4_length);
            var start_bonus:int;
            start_bonus = ba.readInt();
            server.scRewardCandidateCardsList(candidate_list_1, candidate_list_2, candidate_list_3, candidate_list_4, start_bonus);
      }


     private function scBottomDiceNum(ba:ByteArray):void
     {
            var buttom_dice_length:int;
            buttom_dice_length = ba.readUnsignedInt();
            var buttom_dice:String;
            buttom_dice = ba.readUTFBytes(buttom_dice_length);
            server.scBottomDiceNum(buttom_dice);
      }


     private function scHighLowResult(ba:ByteArray):void
     {
            var win:Boolean;
            win = ba.readBoolean();
            var getted_cards_length:int;
            getted_cards_length = ba.readUnsignedInt();
            var getted_cards:String;
            getted_cards = ba.readUTFBytes(getted_cards_length);
            var next_cards_length:int;
            next_cards_length = ba.readUnsignedInt();
            var next_cards:String;
            next_cards = ba.readUTFBytes(next_cards_length);
            var bonus:int;
            bonus = ba.readInt();
            server.scHighLowResult(win, getted_cards, next_cards, bonus);
      }


     private function scRewardResultDice(ba:ByteArray):void
     {
            var result_dice_length:int;
            result_dice_length = ba.readUnsignedInt();
            var result_dice:String;
            result_dice = ba.readUTFBytes(result_dice_length);
            server.scRewardResultDice(result_dice);
      }


     private function scRewardFinalResult(ba:ByteArray):void
     {
            var getted_cards_length:int;
            getted_cards_length = ba.readUnsignedInt();
            var getted_cards:String;
            getted_cards = ba.readUTFBytes(getted_cards_length);
            var total_gems:int;
            total_gems = ba.readInt();
            var total_exp:int;
            total_exp = ba.readInt();
            var add_point:int;
            add_point = ba.readInt();
            server.scRewardFinalResult(getted_cards, total_gems, total_exp, add_point);
      }


     private function scUseItem(ba:ByteArray):void
     {
            var inv_id:int;
            inv_id = ba.readInt();
            server.scUseItem(inv_id);
      }


     private function scNextSuccess(ba:ByteArray):void
     {
            var next_no:int;
            next_no = ba.readByte();
            server.scNextSuccess(next_no);
      }


     private function scAchievementClear(ba:ByteArray):void
     {
            var achi_id:int;
            achi_id = ba.readInt();
            var item_type:int;
            item_type = ba.readInt();
            var item_id:int;
            item_id = ba.readInt();
            var item_num:int;
            item_num = ba.readInt();
            var slot_type:int;
            slot_type = ba.readInt();
            server.scAchievementClear(achi_id, item_type, item_id, item_num, slot_type);
      }


     private function scAddNewAchievement(ba:ByteArray):void
     {
            var achi_id:int;
            achi_id = ba.readInt();
            server.scAddNewAchievement(achi_id);
      }


     private function scDeleteAchievement(ba:ByteArray):void
     {
            var achi_id:int;
            achi_id = ba.readInt();
            server.scDeleteAchievement(achi_id);
      }


     private function scUpdateAchievementInfo(ba:ByteArray):void
     {
            var achievements_length:int;
            achievements_length = ba.readUnsignedInt();
            var achievements:String;
            achievements = ba.readUTFBytes(achievements_length);
            var achievements_state_length:int;
            achievements_state_length = ba.readUnsignedInt();
            var achievements_state:String;
            achievements_state = ba.readUTFBytes(achievements_state_length);
            var achievements_progress_length:int;
            achievements_progress_length = ba.readUnsignedInt();
            var achievements_progress:String;
            achievements_progress = ba.readUTFBytes(achievements_progress_length);
            var achievements_end_at_length:int;
            achievements_end_at_length = ba.readUnsignedInt();
            var achievements_end_at:String;
            achievements_end_at = ba.readUTFBytes(achievements_end_at_length);
            var achievements_code_length:int;
            achievements_code_length = ba.readUnsignedInt();
            var achievements_code:String;
            achievements_code = ba.readUTFBytes(achievements_code_length);
            server.scUpdateAchievementInfo(achievements, achievements_state, achievements_progress, achievements_end_at, achievements_code);
      }


     private function scGetPart(ba:ByteArray):void
     {
            var inv_id:int;
            inv_id = ba.readInt();
            var part_id:int;
            part_id = ba.readInt();
            server.scGetPart(inv_id, part_id);
      }


     private function scDialogueInfoUpdate(ba:ByteArray):void
     {
            var dialogue_length:int;
            dialogue_length = ba.readUnsignedInt();
            var dialogue:String;
            dialogue = ba.readUTFBytes(dialogue_length);
            var id:int;
            id = ba.readInt();
            var type:int;
            type = ba.readByte();
            server.scDialogueInfoUpdate(dialogue, id, type);
      }


     private function scUpdateCombineWeaponData(ba:ByteArray):void
     {
            ba.uncompress();
            var inv_id:int;
            inv_id = ba.readInt();
            var card_id:int;
            card_id = ba.readInt();
            var base_sap:int;
            base_sap = ba.readByte();
            var base_sdp:int;
            base_sdp = ba.readByte();
            var base_aap:int;
            base_aap = ba.readByte();
            var base_adp:int;
            base_adp = ba.readByte();
            var base_max:int;
            base_max = ba.readInt();
            var add_sap:int;
            add_sap = ba.readByte();
            var add_sdp:int;
            add_sdp = ba.readByte();
            var add_aap:int;
            add_aap = ba.readByte();
            var add_adp:int;
            add_adp = ba.readByte();
            var add_max:int;
            add_max = ba.readInt();
            var passive_id_length:int;
            passive_id_length = ba.readUnsignedInt();
            var passive_id:String;
            passive_id = ba.readUTFBytes(passive_id_length);
            var restriction_length:int;
            restriction_length = ba.readUnsignedInt();
            var restriction:String;
            restriction = ba.readUTFBytes(restriction_length);
            var count_str_length:int;
            count_str_length = ba.readUnsignedInt();
            var count_str:String;
            count_str = ba.readUTFBytes(count_str_length);
            var count_max_str_length:int;
            count_max_str_length = ba.readUnsignedInt();
            var count_max_str:String;
            count_max_str = ba.readUTFBytes(count_max_str_length);
            var level:int;
            level = ba.readInt();
            var exp:int;
            exp = ba.readInt();
            var psv_num_max:int;
            psv_num_max = ba.readByte();
            var psv_pass_set_length:int;
            psv_pass_set_length = ba.readUnsignedInt();
            var psv_pass_set:String;
            psv_pass_set = ba.readUTFBytes(psv_pass_set_length);
            var vani_psv_ids_length:int;
            vani_psv_ids_length = ba.readUnsignedInt();
            var vani_psv_ids:String;
            vani_psv_ids = ba.readUTFBytes(vani_psv_ids_length);
            server.scUpdateCombineWeaponData(inv_id, card_id, base_sap, base_sdp, base_aap, base_adp, base_max, add_sap, add_sdp, add_aap, add_adp, add_max, passive_id, restriction, count_str, count_max_str, level, exp, psv_num_max, psv_pass_set, vani_psv_ids);
      }


    }
}