package GMJournal_fla
{
   import LS_Classes.listDisplay;
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.text.TextField;
   
   public dynamic class category_30 extends MovieClip
   {
       
      public var expand_mc:expand;
      public var text_txt:TextField;
      public var _list:listDisplay;
      public var _linesCount:int;
      public var heightOverride:Number;
      
      public function category_30()
      {
         super();
         addFrameScript(0,this.frame1);
      }
      
      public function Init() : *
      {
         this.expand_mc.init(this.onExpandPressed);   // Initialize LSStateButton
      }
      
      public function onExpandPressed() : *
      {
         var listIsActive:* = false;

         if(this._list)
         {
            listIsActive = !this.expand_mc.isActive;
            this._list.visible = listIsActive;
            if(listIsActive)
            {
               this._list.positionElements();
            }
            dispatchEvent(new Event("HeightChanged"));
         }
      }
      
      public function mouseUp() : *
      {
         this.expand_mc.setActive(!this.expand_mc.isActive);
         this.onExpandPressed();
      }
      
      public function attachList(param1:listDisplay) : *
      {
         this._list = param1;
      }
      
      function frame1() : *
      {
      }
   }
}