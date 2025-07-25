package com.ankamagames.dofus.uiApi
{
   import com.ankamagames.berilia.interfaces.IApi;
   import com.ankamagames.dofus.datacenter.alignments.AlignmentOrder;
   import com.ankamagames.dofus.datacenter.alignments.AlignmentRank;
   import com.ankamagames.dofus.datacenter.alignments.AlignmentSide;
   import com.ankamagames.dofus.datacenter.alignments.AlignmentTitle;
   import com.ankamagames.dofus.datacenter.world.MapPosition;
   import com.ankamagames.dofus.kernel.Kernel;
   import com.ankamagames.dofus.logic.game.common.frames.AlignmentFrame;
   import com.ankamagames.dofus.logic.game.common.frames.AllianceFrame;
   import com.ankamagames.dofus.logic.game.roleplay.frames.RoleplayEntitiesFrame;
   import com.ankamagames.jerakine.logger.Log;
   import com.ankamagames.jerakine.logger.Logger;
   import flash.utils.getQualifiedClassName;
   
   [InstanciedApi]
   public class AlignmentApi implements IApi
   {
       
      
      protected var _log:Logger;
      
      private var _orderRanks:Array;
      
      private var _rankGifts:Array;
      
      private var _sideOrders:Array;
      
      private var include_mapPosition:MapPosition = null;
      
      public function AlignmentApi()
      {
         this._log = Log.getLogger(getQualifiedClassName(DataApi));
         super();
      }
      
      private function get allianceFrame() : AllianceFrame
      {
         return Kernel.getWorker().getFrame(AllianceFrame) as AllianceFrame;
      }
      
      private function get alignmentFrame() : AlignmentFrame
      {
         return Kernel.getWorker().getFrame(AlignmentFrame) as AlignmentFrame;
      }
      
      private function get roleplayEntitiesFrame() : RoleplayEntitiesFrame
      {
         return Kernel.getWorker().getFrame(RoleplayEntitiesFrame) as RoleplayEntitiesFrame;
      }
      
      public function destroy() : void
      {
         this._orderRanks = null;
         this._rankGifts = null;
         this._sideOrders = null;
      }
      
      public function getOrder(orderId:uint) : AlignmentOrder
      {
         return AlignmentOrder.getAlignmentOrderById(orderId);
      }
      
      public function getRank(rankId:uint) : AlignmentRank
      {
         return AlignmentRank.getAlignmentRankById(rankId);
      }
      
      public function getOrderRanks(orderId:uint) : Array
      {
         var alignmentRank:AlignmentRank = null;
         var listOrderRanks:Array = new Array();
         var listRanks:Array = AlignmentRank.getAlignmentRanks();
         var nRanks:int = listRanks.length;
         for(var i:int = 0; i < nRanks; i++)
         {
            alignmentRank = listRanks[i];
            if(alignmentRank)
            {
               if(alignmentRank.orderId == orderId)
               {
                  listOrderRanks.push(alignmentRank);
               }
            }
         }
         return listOrderRanks.sortOn("minimumAlignment",Array.NUMERIC);
      }
      
      public function getSide(sideId:uint) : AlignmentSide
      {
         return AlignmentSide.getAlignmentSideById(sideId);
      }
      
      public function getOrderSide(orderId:uint) : AlignmentSide
      {
         return this.getSide(this.getOrder(orderId).sideId);
      }
      
      public function getTitleName(sideId:uint, grade:int) : String
      {
         return AlignmentTitle.getAlignmentTitlesById(sideId).getNameFromGrade(grade);
      }
      
      public function getPlayerRank() : int
      {
         return AlignmentFrame.getInstance().playerRank;
      }
   }
}