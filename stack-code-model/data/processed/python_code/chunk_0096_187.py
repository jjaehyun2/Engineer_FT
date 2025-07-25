package game.view.experience
{
   import com.pickgliss.ui.ComponentFactory;
   import ddt.utils.PositionUtils;
   import flash.events.Event;
   
   public class ExpExploitItem extends ExpFightExpItem
   {
       
      
      public function ExpExploitItem(param1:Array)
      {
         super(param1);
      }
      
      override protected function init() : void
      {
         _itemType = ExpTypeTxt.EXPLOIT_EXP;
         PositionUtils.setPos(this,"experience.ExploitExpItemPos");
         _bg = ComponentFactory.Instance.creatBitmap("asset.experience.attachExploitItemBg");
         _titleBitmap = ComponentFactory.Instance.creatBitmap("asset.experience.attachExploitItemTitle");
         addChild(_bg);
         addChild(_titleBitmap);
      }
      
      override protected function createNumTxt() : void
      {
         _numTxt = new ExpCountingTxt("experience.expCountTxt2","experience.exploitTxtFilter_1,experience.exploitTxtFilter_2");
         _numTxt.addEventListener(Event.CHANGE,__onTextChange);
         addChild(_numTxt);
      }
   }
}