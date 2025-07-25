package com.playata.application.data.item
{
   import com.playata.application.data.constants.CBooster;
   import com.playata.framework.core.TypedObject;
   import com.playata.framework.core.util.StringUtil;
   import com.playata.framework.core.util.TimeUtil;
   import com.playata.framework.data.DataObject;
   import com.playata.framework.localization.LocText;
   
   public class LinkedBooster extends DataObject
   {
       
      
      public function LinkedBooster(param1:String)
      {
         var _loc2_:* = null;
         var _loc5_:* = null;
         var _loc7_:* = null;
         var _loc4_:TypedObject = new TypedObject({
            "boosterId":"",
            "days":0
         });
         var _loc3_:Array = param1.split(";");
         var _loc10_:int = 0;
         var _loc9_:* = _loc3_;
         for each(var _loc6_ in _loc3_)
         {
            _loc2_ = _loc6_.split(":");
            _loc5_ = _loc2_[0];
            _loc7_ = _loc2_[1];
            var _loc8_:* = _loc5_;
            switch(_loc8_)
            {
               case "(booster":
                  _loc4_.setString("boosterId",_loc7_);
                  continue;
               case "d":
                  _loc4_.setInt("days",parseInt(_loc7_));
                  continue;
               default:
                  continue;
            }
         }
         super(_loc4_);
      }
      
      public function get imageUrl() : String
      {
         var _loc1_:String = StringUtil.replace(getString("boosterId"),"booster_","");
         return "SymbolLinkedBooster" + StringUtil.capitaliseFirstLetter(_loc1_);
      }
      
      public function getTooltip() : String
      {
         var _loc4_:CBooster = CBooster.fromId(getString("boosterId"));
         var _loc2_:int = _loc4_.amount;
         var _loc3_:int = _loc4_.type;
         var _loc1_:int = getInt("days") * 60 * 60 * 24;
         switch(int(_loc3_) - 1)
         {
            case 0:
               return LocText.current.text("dialog/boosters/button_tooltip_quest",_loc2_,TimeUtil.secondsToString(_loc1_));
            case 1:
               return LocText.current.text("dialog/boosters/button_tooltip_stats",_loc2_,TimeUtil.secondsToString(_loc1_));
            case 2:
               return LocText.current.text("dialog/boosters/button_tooltip_work",_loc2_,TimeUtil.secondsToString(_loc1_));
         }
      }
      
      public function get rewardName() : String
      {
         var _loc3_:CBooster = CBooster.fromId(getString("boosterId"));
         var _loc1_:int = _loc3_.amount;
         var _loc2_:int = _loc3_.type;
         switch(int(_loc2_) - 1)
         {
            case 0:
               return LocText.current.text("booster/type/1/name") + " (-" + _loc1_ + "%)";
            case 1:
               return LocText.current.text("booster/type/2/name") + " (+" + _loc1_ + "%)";
            case 2:
               return LocText.current.text("booster/type/3/name") + " (+" + _loc1_ + "%)";
         }
      }
   }
}