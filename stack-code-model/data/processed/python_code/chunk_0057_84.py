package com.ankamagames.dofus.logic.game.common.actions.guild
{
   import com.ankamagames.dofus.misc.utils.AbstractAction;
   import com.ankamagames.jerakine.handlers.messages.Action;
   
   public class GuildModificationValidAction extends AbstractAction implements Action
   {
       
      
      public var guildName:String;
      
      public var upEmblemId:uint;
      
      public var upColorEmblem:uint;
      
      public var backEmblemId:uint;
      
      public var backColorEmblem:uint;
      
      public function GuildModificationValidAction(params:Array = null)
      {
         super(params);
      }
      
      public static function create(pGuildName:String, pUpEmblemId:uint, pUpColorEmblem:uint, pBackEmblemId:uint, pBackColorEmblem:uint) : GuildModificationValidAction
      {
         var action:GuildModificationValidAction = new GuildModificationValidAction(arguments);
         action.guildName = pGuildName;
         action.upEmblemId = pUpEmblemId;
         action.upColorEmblem = pUpColorEmblem;
         action.backEmblemId = pBackEmblemId;
         action.backColorEmblem = pBackColorEmblem;
         return action;
      }
   }
}