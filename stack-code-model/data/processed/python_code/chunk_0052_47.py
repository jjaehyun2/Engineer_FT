package msgbox_fla
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.FocusEvent;
   import flash.events.KeyboardEvent;
   import flash.external.ExternalInterface;
   import flash.text.TextField;
   
   public dynamic class inputField_5 extends MovieClip
   {
      public var copy_mc:MovieClip;
      
      public var input_txt:TextField;
      
      public var paste_mc:MovieClip;

      public function inputField_5()
      {
         super();
         addFrameScript(0,this.frame1);
      }

      public function acceptSave() : *
      {
         var inputString:String = this.input_txt.text;

         // Commenting Out strReplace -- will enable newline and tabs.
         
         //_loc1_ = this.strReplace(_loc1_,"\n","");
         //_loc1_ = this.strReplace(_loc1_,"\t","");
         //_loc1_ = this.strReplace(_loc1_,"\r","");
         
         ExternalInterface.call("acceptInput",inputString);
      }
      
      public function onChange(param1:Event) : *
      {
         this.acceptSave();
      }
      
      public function onFocus(param1:FocusEvent) : *
      {
         this.input_txt.addEventListener(KeyboardEvent.KEY_DOWN,this.inputHandler);
      }
      
      public function onFocusLost(param1:FocusEvent) : *
      {
         this.input_txt.removeEventListener(KeyboardEvent.KEY_DOWN,this.inputHandler);
      }
      
      public function strReplace(param1:String, param2:String, param3:String) : String
      {
         return param1.split(param2).join(param3);
      }
      
      public function inputHandler(param1:KeyboardEvent) : *
      {
         if(param1.charCode == 13)
         {
            this.acceptSave();
         }
      }
      
      function frame1() : *
      {
         stop();
         this.copy_mc.pressedFuncStr = "copyPressed";
         this.paste_mc.pressedFuncStr = "pastePressed";
         //this.input_txt.restrict = "a-zA-Z0-9_ \\-";   // No Restrictions to text.
         this.input_txt.addEventListener(Event.CHANGE,this.onChange);
         this.input_txt.addEventListener(FocusEvent.FOCUS_IN,this.onFocus,false,0,true);
         addEventListener(FocusEvent.FOCUS_OUT,this.onFocusLost,false,0,true);
      }
   }
}