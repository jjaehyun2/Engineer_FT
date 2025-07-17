package Euchre_fla
{
   import fl.controls.Button;
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.utils.Dictionary;
   
   public dynamic class MainTimeline extends MovieClip
   {
       
      
      public var passBtn:Button;
      
      public var startButton:Button;
      
      public var callBtn:Button;
      
      public var __setPropDict:Dictionary;
      
      public var __lastFrameProp:int = -1;
      
      public var deck;
      
      public var table;
      
      public var game;
      
      public var human;
      
      public var ai1;
      
      public var ai2;
      
      public var ai3;
      
      public function MainTimeline()
      {
         this.__setPropDict = new Dictionary(true);
         super();
         addFrameScript(0,this.frame1,2,this.frame3);
         addEventListener(Event.FRAME_CONSTRUCTED,this.__setProp_handler,false,0,true);
      }
      
      public function startGame(param1:MouseEvent) : *
      {
         this.startButton.removeEventListener(MouseEvent.CLICK,this.startGame);
         removeChild(this.startButton);
         gotoAndStop(1,"Scene 2");
      }
      
      function __setProp_startButton_Scene1_Layer1_0(param1:int) : *
      {
         if(this.startButton != null && param1 >= 1 && param1 <= 2 && (this.__setPropDict[this.startButton] == undefined || !(int(this.__setPropDict[this.startButton]) >= 1 && int(this.__setPropDict[this.startButton]) <= 2)))
         {
            this.__setPropDict[this.startButton] = param1;
            try
            {
               this.startButton["componentInspectorSetting"] = true;
            }
            catch(e:Error)
            {
            }
            this.startButton.emphasized = false;
            this.startButton.enabled = true;
            this.startButton.label = "START";
            this.startButton.labelPlacement = "right";
            this.startButton.selected = false;
            this.startButton.toggle = false;
            this.startButton.visible = true;
            try
            {
               this.startButton["componentInspectorSetting"] = false;
               return;
            }
            catch(e:Error)
            {
               return;
            }
         }
      }
      
      function __setProp_callBtn_Scene2_Layer1_2(param1:int) : *
      {
         if(this.callBtn != null && param1 >= 3 && param1 <= 4 && (this.__setPropDict[this.callBtn] == undefined || !(int(this.__setPropDict[this.callBtn]) >= 3 && int(this.__setPropDict[this.callBtn]) <= 4)))
         {
            this.__setPropDict[this.callBtn] = param1;
            try
            {
               this.callBtn["componentInspectorSetting"] = true;
            }
            catch(e:Error)
            {
            }
            this.callBtn.emphasized = false;
            this.callBtn.enabled = true;
            this.callBtn.label = "Call";
            this.callBtn.labelPlacement = "right";
            this.callBtn.selected = false;
            this.callBtn.toggle = false;
            this.callBtn.visible = true;
            try
            {
               this.callBtn["componentInspectorSetting"] = false;
               return;
            }
            catch(e:Error)
            {
               return;
            }
         }
      }
      
      function __setProp_passBtn_Scene2_Layer1_2(param1:int) : *
      {
         if(this.passBtn != null && param1 >= 3 && param1 <= 4 && (this.__setPropDict[this.passBtn] == undefined || !(int(this.__setPropDict[this.passBtn]) >= 3 && int(this.__setPropDict[this.passBtn]) <= 4)))
         {
            this.__setPropDict[this.passBtn] = param1;
            try
            {
               this.passBtn["componentInspectorSetting"] = true;
            }
            catch(e:Error)
            {
            }
            this.passBtn.emphasized = false;
            this.passBtn.enabled = true;
            this.passBtn.label = "Pass";
            this.passBtn.labelPlacement = "right";
            this.passBtn.selected = false;
            this.passBtn.toggle = false;
            this.passBtn.visible = true;
            try
            {
               this.passBtn["componentInspectorSetting"] = false;
               return;
            }
            catch(e:Error)
            {
               return;
            }
         }
      }
      
      function __setProp_handler(param1:Object) : *
      {
         var _loc2_:int = currentFrame;
         var _loc3_:int = 0;
         while(_loc3_ < scenes.length - 1)
         {
            if(currentScene.name == scenes[_loc3_].name)
            {
               break;
            }
            _loc2_ = _loc2_ + scenes[_loc3_].numFrames;
            _loc3_++;
         }
         if(this.__lastFrameProp == _loc2_)
         {
            return;
         }
         this.__lastFrameProp = _loc2_;
         this.__setProp_startButton_Scene1_Layer1_0(_loc2_);
         this.__setProp_callBtn_Scene2_Layer1_2(_loc2_);
         this.__setProp_passBtn_Scene2_Layer1_2(_loc2_);
      }
      
      function frame1() : *
      {
         this.startButton.addEventListener(MouseEvent.CLICK,this.startGame);
         stop();
      }
      
      function frame3() : *
      {
         stop();
         this.callBtn.visible = false;
         this.passBtn.visible = false;
         this.deck = new Deck(this);
         this.table = new Table();
         this.game = new Game(this,this.table,this.deck);
         this.game.SetupGame();
         this.table.getGameRef(this.game);
         this.human = new Human(this,this.game,this.table,this.deck,this.callBtn,this.passBtn);
         this.callBtn.addEventListener(MouseEvent.CLICK,this.human.clickedCall);
         this.passBtn.addEventListener(MouseEvent.CLICK,this.human.clickedPass);
         this.ai1 = new AI(this,this.game,this.table,this.deck,0);
         this.ai2 = new AI(this,this.game,this.table,this.deck,1);
         this.ai3 = new AI(this,this.game,this.table,this.deck,2);
         this.game.getPlayersRef(this.human,this.ai1,this.ai2,this.ai3);
         this.game.PlayGame();
      }
   }
}