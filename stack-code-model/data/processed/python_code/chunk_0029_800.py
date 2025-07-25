package Ankama_Social
{
   import Ankama_Common.Common;
   import Ankama_Social.ui.AddFriendWindow;
   import Ankama_Social.ui.Alliance;
   import Ankama_Social.ui.AllianceAreas;
   import Ankama_Social.ui.AllianceCard;
   import Ankama_Social.ui.AllianceCreator;
   import Ankama_Social.ui.AllianceFights;
   import Ankama_Social.ui.AllianceMembers;
   import Ankama_Social.ui.CollectedTaxCollector;
   import Ankama_Social.ui.Directory;
   import Ankama_Social.ui.Friends;
   import Ankama_Social.ui.Guild;
   import Ankama_Social.ui.GuildCard;
   import Ankama_Social.ui.GuildCreator;
   import Ankama_Social.ui.GuildHouses;
   import Ankama_Social.ui.GuildMemberRights;
   import Ankama_Social.ui.GuildMembers;
   import Ankama_Social.ui.GuildPaddock;
   import Ankama_Social.ui.GuildPersonalization;
   import Ankama_Social.ui.GuildTaxCollector;
   import Ankama_Social.ui.HousesList;
   import Ankama_Social.ui.SocialBase;
   import Ankama_Social.ui.SocialBulletin;
   import Ankama_Social.ui.Spouse;
   import Ankama_Social.ui.TopTaxCollectors;
   import com.ankamagames.berilia.api.UiApi;
   import com.ankamagames.dofus.internalDatacenter.guild.TaxCollectorWrapper;
   import com.ankamagames.dofus.logic.game.common.actions.alliance.AllianceInvitationAnswerAction;
   import com.ankamagames.dofus.logic.game.common.actions.guild.GuildInvitationAnswerAction;
   import com.ankamagames.dofus.logic.game.common.actions.social.SpouseRequestAction;
   import com.ankamagames.dofus.logic.game.roleplay.actions.PlayerFightRequestAction;
   import com.ankamagames.dofus.misc.lists.CustomUiHookList;
   import com.ankamagames.dofus.misc.lists.HookList;
   import com.ankamagames.dofus.misc.lists.SocialHookList;
   import com.ankamagames.dofus.uiApi.DataApi;
   import com.ankamagames.dofus.uiApi.PlayedCharacterApi;
   import com.ankamagames.dofus.uiApi.SocialApi;
   import com.ankamagames.dofus.uiApi.SystemApi;
   import com.ankamagames.dofus.uiApi.TimeApi;
   import com.ankamagames.dofus.uiApi.UtilApi;
   import flash.display.Sprite;
   
   public class Social extends Sprite
   {
      
      private static var _self:Social;
       
      
      protected var socialBase:SocialBase;
      
      protected var friends:Friends;
      
      protected var addFriendWindow:AddFriendWindow;
      
      protected var spouse:Spouse;
      
      protected var guild:Guild;
      
      protected var alliance:Alliance;
      
      protected var directory:Directory;
      
      protected var housesList:HousesList;
      
      protected var guildCard:GuildCard;
      
      protected var allianceCard:AllianceCard;
      
      protected var guildHouses:GuildHouses;
      
      protected var guildMembers:GuildMembers;
      
      protected var guildMemberRights:GuildMemberRights;
      
      protected var guildPaddock:GuildPaddock;
      
      protected var guildPersonalization:GuildPersonalization;
      
      protected var guildTaxCollector:GuildTaxCollector;
      
      protected var guildCreator:GuildCreator;
      
      protected var allianceMembers:AllianceMembers;
      
      protected var allianceAreas:AllianceAreas;
      
      protected var allianceFights:AllianceFights;
      
      protected var allianceCreator:AllianceCreator;
      
      protected var collectedTaxCollector:CollectedTaxCollector;
      
      protected var topTaxCollectors:TopTaxCollectors;
      
      protected var socialBulletin:SocialBulletin;
      
      [Api(name="SystemApi")]
      public var sysApi:SystemApi;
      
      [Api(name="UiApi")]
      public var uiApi:UiApi;
      
      [Api(name="SocialApi")]
      public var socialApi:SocialApi;
      
      [Api(name="PlayedCharacterApi")]
      public var playerApi:PlayedCharacterApi;
      
      [Api(name="DataApi")]
      public var dataApi:DataApi;
      
      [Api(name="UtilApi")]
      public var utilApi:UtilApi;
      
      [Api(name="TimeApi")]
      public var timeApi:TimeApi;
      
      [Module(name="Ankama_Common")]
      public var modCommon:Common;
      
      private var _firstTime:Boolean = true;
      
      private var _ava:Boolean;
      
      private var _targetId:Number;
      
      private var _cellId:int;
      
      private var _popupName:String = null;
      
      private var _popupAllianceName:String = null;
      
      public function Social()
      {
         super();
      }
      
      public static function getInstance() : Social
      {
         return _self;
      }
      
      public function main() : void
      {
         Api.system = this.sysApi;
         Api.social = this.socialApi;
         Api.ui = this.uiApi;
         Api.player = this.playerApi;
         Api.modCommon = this.modCommon;
         Api.data = this.dataApi;
         Api.util = this.utilApi;
         Api.time = this.timeApi;
         _self = this;
         this.sysApi.addHook(SocialHookList.OpenSocial,this.onOpenSocial);
         this.sysApi.addHook(HookList.OpenHouses,this.onOpenHouses);
         this.sysApi.addHook(CustomUiHookList.ClientUIOpened,this.onClientUIOpened);
         this.sysApi.addHook(HookList.ContextChanged,this.onContextChanged);
         this.sysApi.addHook(SocialHookList.GuildCreationStarted,this.onCreateGuild);
         this.sysApi.addHook(SocialHookList.GuildInvited,this.onGuildInvited);
         this.sysApi.addHook(SocialHookList.GuildInvitationStateRecruter,this.onGuildInvitationStateRecruter);
         this.sysApi.addHook(SocialHookList.GuildInvitationStateRecruted,this.onGuildInvitationStateRecruted);
         this.sysApi.addHook(SocialHookList.AllianceCreationStarted,this.onCreateAlliance);
         this.sysApi.addHook(SocialHookList.AllianceInvited,this.onAllianceInvited);
         this.sysApi.addHook(SocialHookList.AllianceInvitationStateRecruter,this.onAllianceInvitationStateRecruter);
         this.sysApi.addHook(SocialHookList.AllianceInvitationStateRecruted,this.onAllianceInvitationStateRecruted);
         this.sysApi.addHook(SocialHookList.AttackPlayer,this.onAttackPlayer);
         this.sysApi.addHook(SocialHookList.DishonourChanged,this.onDishonourChanged);
         this.sysApi.addHook(SocialHookList.OpenOneAlliance,this.onOpenOneAlliance);
         this.sysApi.addHook(SocialHookList.OpenOneGuild,this.onOpenOneGuild);
         this.sysApi.addHook(HookList.ShowCollectedTaxCollector,this.onShowCollectedTaxCollector);
         this.sysApi.addHook(SocialHookList.ShowTopTaxCollectors,this.onShowTopTaxCollectors);
         if(!this.sysApi.getData("guildBulletinLastVisitTimestamp"))
         {
            this.sysApi.setData("guildBulletinLastVisitTimestamp",0);
         }
         if(!this.sysApi.getData("allianceBulletinLastVisitTimestamp"))
         {
            this.sysApi.setData("allianceBulletinLastVisitTimestamp",0);
         }
      }
      
      private function onCreateGuild(modifyName:Boolean, modifyEmblem:Boolean) : void
      {
         this.uiApi.loadUi("guildCreator","guildCreator",[modifyName,modifyEmblem]);
      }
      
      private function onCreateAlliance(modifyName:Boolean, modifyEmblem:Boolean) : void
      {
         this.uiApi.loadUi("allianceCreator","allianceCreator",[modifyName,modifyEmblem]);
      }
      
      private function onOpenOneGuild(guild:Object) : void
      {
         this.uiApi.unloadUi("allianceCard");
         if(!this.uiApi.getUi("guildCard"))
         {
            this.uiApi.loadUi("guildCard","guildCard",{"guild":guild});
         }
      }
      
      private function onOpenOneAlliance(alliance:Object) : void
      {
         this.uiApi.unloadUi("guildCard");
         if(!this.uiApi.getUi("allianceCard"))
         {
            this.uiApi.loadUi("allianceCard","allianceCard",{"alliance":alliance});
         }
      }
      
      private function onOpenSocial(tab:int = -1, subTab:int = -1, params:Object = null) : void
      {
         var args:Object = null;
         this.sysApi.log(8,"onOpenSocial " + tab + ", " + subTab + ", " + params);
         if(tab == 2 && !this.playerApi.characteristics())
         {
            return;
         }
         if(tab == 3)
         {
            if(!this.uiApi.getUi("spouse"))
            {
               this.sysApi.sendAction(new SpouseRequestAction([]));
               this.uiApi.loadUi("spouse");
            }
            else
            {
               this.uiApi.unloadUi("spouse");
            }
            return;
         }
         if(!this.uiApi.getUi("socialBase"))
         {
            if(tab == 3 && this.socialApi.getSpouse() == null)
            {
               return;
            }
            args = {};
            if(tab != -1)
            {
               args.tab = tab;
            }
            if(subTab != -1)
            {
               args.subTab = subTab;
            }
            if(params != null && params.length > 0)
            {
               args.params = params;
            }
            if(subTab == -1)
            {
               this.uiApi.loadUi("socialBase","socialBase",args);
            }
            else
            {
               this.uiApi.loadUi("socialBase","socialBase",args,1,null,false,false,false);
            }
         }
         else if(tab != -1)
         {
            if(this.uiApi.getUi("socialBase").uiClass.getTab() != tab || subTab != -1 && this.uiApi.getUi("socialBase").uiClass.getSubTab() != subTab)
            {
               if(subTab == -1)
               {
                  this.uiApi.getUi("socialBase").uiClass.openTab(tab);
               }
               else if(params == null)
               {
                  this.uiApi.getUi("socialBase").uiClass.openTab(tab,subTab,null,false);
               }
               else
               {
                  this.uiApi.getUi("socialBase").uiClass.openTab(tab,subTab,params,false);
               }
            }
            else
            {
               this.uiApi.unloadUi("socialBase");
            }
         }
         else
         {
            this.uiApi.unloadUi("socialBase");
         }
      }
      
      private function onOpenHouses() : void
      {
         if(!this.uiApi.getUi("housesList"))
         {
            this.uiApi.loadUi("housesList");
         }
      }
      
      private function onContextChanged(context:uint) : void
      {
         if(context == 2)
         {
            this.uiApi.unloadUi("socialBase");
         }
      }
      
      private function onClientUIOpened(type:uint, uid:uint) : void
      {
         if(this.socialApi.hasGuild())
         {
            if(!this.uiApi.getUi("socialBase"))
            {
               switch(type)
               {
                  case 0:
                     this.sysApi.log(16,"Error : wrong UI type to open.");
                     break;
                  case 1:
                     this.uiApi.loadUi("socialBase","socialBase",{
                        "tab":1,
                        "subTab":4
                     },1,null,false,false,false);
                     break;
                  case 2:
                     this.uiApi.loadUi("socialBase","socialBase",{
                        "tab":1,
                        "subTab":3
                     },1,null,false,false,false);
                     break;
                  case 4:
                     this.uiApi.loadUi("socialBase","socialBase",{
                        "tab":1,
                        "subTab":2
                     },1,null,false,false,false);
               }
            }
            else if(this.uiApi.getUi("socialBase").uiClass.getTab() != 1)
            {
               switch(type)
               {
                  case 1:
                     this.uiApi.getUi("socialBase").uiClass.openTab(1,4,null,false);
                     break;
                  case 2:
                     this.uiApi.getUi("socialBase").uiClass.openTab(1,3,null,false);
                     break;
                  case 4:
                     this.uiApi.getUi("socialBase").uiClass.openTab(1,2,null,false);
               }
            }
            else
            {
               this.sysApi.log(16,"Error : Social UI is already open.");
            }
         }
         if(type == 5)
         {
            if(!this.uiApi.getUi("housesList"))
            {
               this.uiApi.loadUi("housesList");
            }
         }
      }
      
      private function onDishonourChanged(dishonour:int) : void
      {
         var text:String = this.uiApi.processText(this.uiApi.getText("ui.social.disgraceSanction",dishonour),"n",dishonour < 2,dishonour == 0);
         text += "\n\n" + this.uiApi.getText("ui.disgrace.sanction.1");
         this.modCommon.openPopup(this.uiApi.getText("ui.common.informations"),text,[this.uiApi.getText("ui.common.ok")]);
      }
      
      private function onAttackPlayer(targetId:Number, ava:Boolean, targetName:String, type:int, cellId:int) : void
      {
         var text:String = null;
         this._targetId = targetId;
         this._cellId = cellId;
         this._ava = ava;
         if(ava || type == 0)
         {
            text = this.uiApi.getText("ui.pvp.doUAttack",targetName);
         }
         else if(type == 2)
         {
            text = this.uiApi.getText("ui.pvp.doUAttackNeutral");
         }
         else if(type == -1)
         {
            text = this.uiApi.getText("ui.pvp.doUAttackNoGain",targetName);
         }
         else if(type == 1)
         {
            text = this.uiApi.getText("ui.pvp.doUAttackBonusGain",targetName);
         }
         this.modCommon.openPopup(this.uiApi.getText("ui.popup.warning"),text,[this.uiApi.getText("ui.common.attack"),this.uiApi.getText("ui.common.cancel")],[this.onConfirmAttack,null],this.onConfirmAttack);
      }
      
      private function onConfirmAttack() : void
      {
         this.sysApi.sendAction(new PlayerFightRequestAction([this._targetId,this._ava,false,true]));
      }
      
      private function onGuildInvited(guildName:String, recruterId:Number, recruterName:String) : void
      {
         this._popupName = this.modCommon.openPopup(this.uiApi.getText("ui.common.invitation"),this.uiApi.getText("ui.social.aInvitYouInGuild",recruterName,guildName),[this.uiApi.getText("ui.common.yes"),this.uiApi.getText("ui.common.no")],[this.onConfirmJoinGuild,this.onCancelJoinGuild],this.onConfirmJoinGuild,this.onCancelJoinGuild);
      }
      
      private function onConfirmJoinGuild() : void
      {
         this.sysApi.sendAction(new GuildInvitationAnswerAction([true]));
      }
      
      private function onCancelJoinGuild() : void
      {
         this.sysApi.sendAction(new GuildInvitationAnswerAction([false]));
      }
      
      private function onGuildInvitationStateRecruter(state:uint, recrutedName:String) : void
      {
         switch(state)
         {
            case 1:
               this._popupName = this.modCommon.openPopup(this.uiApi.getText("ui.common.invitation"),this.uiApi.getText("ui.craft.waitForCraftClient",recrutedName),[this.uiApi.getText("ui.common.cancel")],[this.onCancelJoinGuild],null,this.onCancelJoinGuild);
               break;
            case 2:
            case 3:
               if(this._popupName && this.uiApi.getUi(this._popupName))
               {
                  this.uiApi.unloadUi(this._popupName);
                  this._popupName = null;
               }
         }
      }
      
      private function onGuildInvitationStateRecruted(state:uint) : void
      {
         switch(state)
         {
            case 1:
               break;
            case 2:
            case 3:
               if(this._popupName && this.uiApi.getUi(this._popupName))
               {
                  this.uiApi.unloadUi(this._popupName);
                  this._popupName = null;
               }
         }
      }
      
      private function onAllianceInvited(allianceName:String, recruterId:Number, recruterName:String) : void
      {
         this._popupAllianceName = this.modCommon.openPopup(this.uiApi.getText("ui.common.invitation"),this.uiApi.getText("ui.alliance.youAreInvited",recruterName,allianceName),[this.uiApi.getText("ui.common.yes"),this.uiApi.getText("ui.common.no")],[this.onConfirmJoinAlliance,this.onCancelJoinAlliance],this.onConfirmJoinAlliance,this.onCancelJoinAlliance);
      }
      
      private function onConfirmJoinAlliance() : void
      {
         this.sysApi.sendAction(new AllianceInvitationAnswerAction([true]));
      }
      
      private function onCancelJoinAlliance() : void
      {
         this.sysApi.sendAction(new AllianceInvitationAnswerAction([false]));
      }
      
      private function onAllianceInvitationStateRecruter(state:uint, recrutedName:String) : void
      {
         switch(state)
         {
            case 1:
               this._popupAllianceName = this.modCommon.openPopup(this.uiApi.getText("ui.common.invitation"),this.uiApi.getText("ui.craft.waitForCraftClient",recrutedName),[this.uiApi.getText("ui.common.cancel")],[this.onCancelJoinAlliance],null,this.onCancelJoinAlliance);
               break;
            case 2:
            case 3:
               if(this._popupAllianceName && this.uiApi.getUi(this._popupAllianceName))
               {
                  this.uiApi.unloadUi(this._popupAllianceName);
                  this._popupAllianceName = null;
               }
         }
      }
      
      private function onAllianceInvitationStateRecruted(state:uint) : void
      {
         switch(state)
         {
            case 1:
               break;
            case 2:
            case 3:
               if(this._popupAllianceName && this.uiApi.getUi(this._popupAllianceName))
               {
                  this.uiApi.unloadUi(this._popupAllianceName);
                  this._popupAllianceName = null;
               }
         }
      }
      
      private function onShowCollectedTaxCollector(pTaxCollector:TaxCollectorWrapper) : void
      {
         this.uiApi.loadUi("collectedTaxCollector",null,pTaxCollector,1,null,true);
      }
      
      private function onShowTopTaxCollectors(pDungeonTopTaxCollectors:Object, pTopTaxCollectors:Object) : void
      {
         this.uiApi.loadUi("topTaxCollectors",null,{
            "dungeonTopTaxCollectors":pDungeonTopTaxCollectors,
            "topTaxCollectors":pTopTaxCollectors
         },1,null,true);
      }
   }
}