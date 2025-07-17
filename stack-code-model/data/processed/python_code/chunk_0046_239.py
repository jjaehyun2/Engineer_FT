class events.EventGenerator
{
   function EventGenerator()
   {
   }
   static function generateEvent()
   {
      var _loc2_ = 0;
      var _loc3_ = _root.playerActivity.length;
      var _loc4_ = 0;
      while(_loc4_ < _loc3_)
      {
         _loc2_ = _loc2_ + _root.playerActivity[_loc4_];
         _loc4_ = _loc4_ + 1;
      }
      if(_loc2_ < 4)
      {
         new events.AngryMobEvent();
      }
      else if((mvcFarm.FarmModel.getModel().getMoney() > _root.maxMoney || mvcFarm.FarmModel.getModel().getInvestmentsValue() > _root.maxMoney) && random(100) < 50 || random(100) < 30)
      {
         events.EventGenerator.generateRichEvent();
      }
      else
      {
         events.EventGenerator.generateNormalEvent();
      }
   }
   static function generateRichEvent()
   {
      var _loc1_ = random(6) + 1;
      switch(_loc1_)
      {
         case 1:
            new events.VeryGoodSeasonEvent();
            break;
         case 2:
            new events.VeryGoodSeasonEvent();
            break;
         case 3:
            new events.VeryGoodSeasonEvent();
            break;
         case 4:
            new events.VeryGoodSeasonEvent();
            break;
         case 5:
            new events.VeryGoodSeasonEvent();
            break;
         case 6:
            new events.VeryGoodSeasonEvent();
      }
   }
   static function generateNormalEvent()
   {
      var _loc2_ = mvcFarm.FarmModel.getModel().getInvestments();
      var _loc1_ = random(15) + 1;
      switch(_loc1_)
      {
         case 1:
            new events.VeryGoodSeasonEvent();
            break;
         case 2:
            new events.VeryGoodSeasonEvent();
            break;
         case 3:
            new events.VeryGoodSeasonEvent();
            break;
         case 4:
            new events.VeryGoodSeasonEvent();
            break;
         case 5:
            new events.VeryGoodSeasonEvent();
            break;
         case 6:
            new events.VeryGoodSeasonEvent();
            break;
         case 7:
            new events.VeryGoodSeasonEvent();
            break;
         case 8:
            new events.VeryGoodSeasonEvent();
            break;
         case 9:
            new events.VeryGoodSeasonEvent();
            break;
         case 10:
            new events.VeryGoodSeasonEvent();
            break;
         case 11:
            new events.VeryGoodSeasonEvent();
            break;
         case 12:
            new events.VeryGoodSeasonEvent();
            break;
         case 13:
            new events.VeryGoodSeasonEvent();
            break;
         case 14:
            new events.VeryGoodSeasonEvent();
            break;
         case 15:
            new events.VeryGoodSeasonEvent();
      }
   }
}