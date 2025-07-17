package
{
   import flash.display.Sprite;
   import flash.events.MouseEvent;
   import flash.events.TimerEvent;
   import flash.text.TextField;
   import flash.text.TextFormat;
   import flash.utils.Timer;
   
   public class Game
   {
       
      
      var tableTopSprite;
      
      public var trumpBox;
      
      public var handScoreBox;
      
      public var trickScoreBox;
      
      public var topCard;
      
      public var topCardX;
      
      public var topCardY;
      
      public var dealer;
      
      public var dealerBmp;
      
      var dealerSprite;
      
      public var dealerX;
      
      var dealerY;
      
      var noWinner;
      
      var trumpPlayer;
      
      var trumpSuit;
      
      public var theParent;
      
      var theTable;
      
      public var theDeck;
      
      var Human;
      
      public var AI1;
      
      public var AI2;
      
      public var AI3;
      
      public var team1Score;
      
      public var team2Score;
      
      public var cSuitSprite;
      
      public var dSuitSprite;
      
      public var hSuitSprite;
      
      public var sSuitSprite;
      
      public var DetermineTrumpTurn;
      
      public var DetermineTrumpTrumpCalled;
      
      public var DetermineTrumpCount;
      
      public var DetermineTrumpNumFunCalls;
      
      public var DetermineTrumpGoAroundTheTable;
      
      var delayCallTrumpTimer;
      
      var debug:Boolean;
      
      public function Game(param1:*, param2:*, param3:*)
      {
         var _loc4_:* = undefined;
         var _loc5_:* = undefined;
         var _loc6_:* = undefined;
         var _loc7_:* = undefined;
         var _loc9_:* = undefined;
         super();
         this.debug = false;
         this.theParent = param1;
         this.theTable = param2;
         this.theDeck = param3;
         this.DetermineTrumpTurn = 1;
         this.DetermineTrumpCount = 0;
         this.DetermineTrumpNumFunCalls = 1;
         this.noWinner = true;
         this.team1Score = 0;
         this.team2Score = 0;
         this.topCard = new Card();
         this.dealer = 0;
         this.dealerX = new Array();
         this.dealerY = new Array();
         this.dealerX[0] = this.theParent.stage.stageWidth / 2 + 90;
         this.dealerY[0] = this.theParent.stage.stageHeight / 2 + 168;
         this.dealerX[1] = this.theParent.stage.stageWidth / 5 + 195;
         this.dealerY[1] = this.theParent.stage.stageHeight / 2 - 27;
         this.dealerX[2] = this.theParent.stage.stageWidth / 2 + 95;
         this.dealerY[2] = this.theParent.stage.stageHeight / 2 - 197;
         this.dealerX[3] = this.theParent.stage.stageWidth - 257;
         this.dealerY[3] = this.theParent.stage.stageHeight / 2 - 27;
         _loc4_ = new clubSuitBmp();
         this.cSuitSprite = makeSprite(_loc4_,_loc4_.width,_loc4_.height);
         this.cSuitSprite.x = this.theParent.stage.stageWidth / 2;
         this.cSuitSprite.y = this.theParent.stage.stageHeight / 2 - _loc4_.height;
         this.theParent.stage.addChild(this.cSuitSprite);
         _loc5_ = new diamondSuitBmp();
         this.dSuitSprite = makeSprite(_loc5_,_loc5_.width,_loc5_.height);
         this.dSuitSprite.x = this.theParent.stage.stageWidth / 2 + 134;
         this.dSuitSprite.y = this.cSuitSprite.y + _loc4_.height - _loc5_.height;
         this.theParent.stage.addChild(this.dSuitSprite);
         _loc6_ = new heartSuitBmp();
         this.hSuitSprite = makeSprite(_loc6_,_loc6_.width,_loc6_.height);
         this.hSuitSprite.x = this.theParent.stage.stageWidth / 2 - 5;
         this.hSuitSprite.y = this.cSuitSprite.y + _loc4_.height + 20;
         this.theParent.stage.addChild(this.hSuitSprite);
         _loc7_ = new spadeSuitBmp();
         this.sSuitSprite = makeSprite(_loc7_,_loc7_.width,_loc7_.height);
         this.sSuitSprite.x = this.theParent.stage.stageWidth / 2 + 128;
         this.sSuitSprite.y = this.cSuitSprite.y + _loc4_.height + 20;
         this.theParent.stage.addChild(this.sSuitSprite);
         this.delayCallTrumpTimer = new Timer(1000);
         this.delayCallTrumpTimer.addEventListener(TimerEvent.TIMER,this.delayCallTrump);
         var _loc8_:* = 0;
         this.trumpBox = makeTextBox();
         _loc9_ = this.theParent.stage.stageHeight - 100;
         this.trumpBox.x = _loc8_;
         this.trumpBox.y = _loc9_;
         this.theParent.stage.addChild(this.trumpBox);
         this.trumpBox.text = "";
         this.trumpBox.visible = true;
      }
      
      static function makeSprite(param1:*, param2:*, param3:*) : *
      {
         var _loc4_:* = new Sprite();
         _loc4_.graphics.beginBitmapFill(param1);
         _loc4_.graphics.drawRect(0,0,param2,param3);
         _loc4_.graphics.endFill();
         _loc4_.x = 0;
         _loc4_.y = 0;
         _loc4_.visible = false;
         return _loc4_;
      }
      
      static function makeTextBox() : *
      {
         var _loc1_:* = new TextField();
         _loc1_.x = 0;
         _loc1_.y = 0;
         _loc1_.width = 300;
         _loc1_.height = 100;
         var _loc2_:TextFormat = new TextFormat();
         _loc2_.font = "Times";
         _loc2_.color = 16777215;
         _loc2_.size = 24;
         _loc1_.defaultTextFormat = _loc2_;
         return _loc1_;
      }
      
      public function SetupGame() : *
      {
         this.handScoreBox = makeTextBox();
         this.handScoreBox.x = 0;
         this.handScoreBox.y = 0;
         this.theParent.stage.addChild(this.handScoreBox);
         this.handScoreBox.text = "Hand Score\nTeam 1: 0    Team 2: 0";
         this.handScoreBox.visible = true;
         this.trickScoreBox = makeTextBox();
         this.trickScoreBox.x = 0;
         this.trickScoreBox.y = 100;
         this.theParent.stage.addChild(this.trickScoreBox);
         this.trickScoreBox.text = "Trick Score\nTeam 1: 0   \tTeam 2: 0";
         this.trickScoreBox.visible = true;
         this.dealerBmp = new DealerBmp();
         this.dealerSprite = makeSprite(this.dealerBmp,this.dealerBmp.width,this.dealerBmp.height);
         this.dealerSprite.x = this.dealerX[0];
         this.dealerSprite.y = this.dealerY[0];
         this.theParent.stage.addChild(this.dealerSprite);
         this.dealerSprite.visible = true;
         this.theDeck.CreateDeck();
      }
      
      public function PlayGame() : *
      {
         if(this.noWinner)
         {
            this.theDeck.ShuffleDeck();
            if(this.dealer == 0)
            {
               this.dealerSprite.x = this.dealerX[0];
               this.dealerSprite.y = this.dealerY[0];
               this.theDeck.DealCards(this.Human,this.AI1,this.AI2,this.AI3);
            }
            else if(this.dealer == 1)
            {
               this.dealerSprite.x = this.dealerX[1];
               this.dealerSprite.y = this.dealerY[1];
               this.theDeck.DealCards(this.AI1,this.AI2,this.AI3,this.Human);
            }
            else if(this.dealer == 2)
            {
               this.dealerSprite.x = this.dealerX[2];
               this.dealerSprite.y = this.dealerY[2];
               this.theDeck.DealCards(this.AI2,this.AI3,this.Human,this.AI1);
            }
            else if(this.dealer == 3)
            {
               this.dealerSprite.x = this.dealerX[3];
               this.dealerSprite.y = this.dealerY[3];
               this.theDeck.DealCards(this.AI3,this.Human,this.AI1,this.AI2);
            }
            this.DetermineTrump();
         }
         else
         {
            trace("game over");
         }
      }
      
      public function DetermineTrump() : *
      {
         var _loc5_:* = undefined;
         var _loc1_:* = "Clubs";
         var _loc2_:* = "Diamonds";
         var _loc3_:* = "Hearts";
         var _loc4_:* = "Spades";
         if(this.DetermineTrumpNumFunCalls == 1)
         {
            this.DetermineTrumpNumFunCalls++;
            this.DetermineTrumpTrumpCalled = -1;
            this.topCard = this.theDeck.GiveTopCard();
            this.topCardX = this.theParent.stage.stageWidth / 2 + 80;
            this.topCardY = this.theParent.stage.stageHeight / 2 - 60;
            this.topCard.sprite.x = this.topCardX;
            this.topCard.sprite.y = this.topCardY;
            this.theParent.stage.addChild(this.topCard.sprite);
            this.topCard.sprite.visible = true;
            if(this.dealer == 3)
            {
               this.DetermineTrumpGoAroundTheTable = 0;
            }
            else
            {
               this.DetermineTrumpGoAroundTheTable = this.dealer + 1;
            }
         }
         if(this.topCard != null)
         {
         }
         if(this.DetermineTrumpTrumpCalled == -1 && this.DetermineTrumpCount < 8)
         {
            this.delayCallTrumpTimer.start();
         }
         else
         {
            this.trumpSuit = this.DetermineTrumpTrumpCalled;
            if(this.trumpSuit == 0)
            {
               this.trumpBox.text = "\t    Trump Suit:\n\t        " + _loc1_;
            }
            else if(this.trumpSuit == 1)
            {
               this.trumpBox.text = "\t    Trump Suit:\n\t     " + _loc2_;
            }
            else if(this.trumpSuit == 2)
            {
               this.trumpBox.text = "\t    Trump Suit:\n\t        " + _loc3_;
            }
            else
            {
               this.trumpBox.text = "\t    Trump Suit:\n\t       " + _loc4_;
            }
            this.AI1.passBox.text = "";
            this.AI2.passBox.text = "";
            this.AI3.passBox.text = "";
            this.SetTrump();
            this.PlayHand();
         }
      }
      
      function delayCallTrump(param1:TimerEvent) : *
      {
         this.delayCallTrumpTimer.stop();
         if(this.DetermineTrumpTurn == 1)
         {
            if(this.DetermineTrumpGoAroundTheTable == 0)
            {
               this.Human.CallTrump1();
            }
            else if(this.DetermineTrumpGoAroundTheTable == 1)
            {
               this.AI1.CallTrump1();
            }
            else if(this.DetermineTrumpGoAroundTheTable == 2)
            {
               this.AI2.CallTrump1();
            }
            else if(this.DetermineTrumpGoAroundTheTable == 3)
            {
               this.AI3.CallTrump1();
            }
         }
         else if(this.DetermineTrumpTurn == 2)
         {
            if(this.DetermineTrumpGoAroundTheTable == 0)
            {
               this.Human.CallTrump2();
            }
            else if(this.DetermineTrumpGoAroundTheTable == 1)
            {
               this.DetermineTrumpTrumpCalled = this.AI1.CallTrump2();
            }
            else if(this.DetermineTrumpGoAroundTheTable == 2)
            {
               this.DetermineTrumpTrumpCalled = this.AI2.CallTrump2();
            }
            else if(this.DetermineTrumpGoAroundTheTable == 3)
            {
               this.DetermineTrumpTrumpCalled = this.AI3.CallTrump2();
            }
         }
      }
      
      public function WasTrumpCalled() : *
      {
         if(this.DetermineTrumpTrumpCalled != -1)
         {
            this.trumpPlayer = this.DetermineTrumpGoAroundTheTable;
            trace("in was trump called dealer= " + this.dealer);
            if(this.dealer == 3)
            {
               this.theTable.whoGoesFirst = 0;
            }
            else
            {
               this.theTable.whoGoesFirst++;
            }
         }
         if(this.DetermineTrumpGoAroundTheTable == 3)
         {
            this.DetermineTrumpGoAroundTheTable = 0;
         }
         else
         {
            this.DetermineTrumpGoAroundTheTable++;
         }
         if(this.DetermineTrumpCount == 3 && this.DetermineTrumpTrumpCalled == -1)
         {
            this.AI1.passBox.text = "";
            this.AI2.passBox.text = "";
            this.AI3.passBox.text = "";
            this.topCard.sprite.visible = false;
            this.DetermineTrumpTurn++;
         }
         this.DetermineTrumpCount++;
         trace("in wastrumpcalled wgf= " + this.theTable.whoGoesFirst);
         this.DetermineTrump();
      }
      
      function SetTrump() : *
      {
         this.Human.setPriority();
         this.AI1.setPriority();
         this.AI2.setPriority();
         this.AI3.setPriority();
      }
      
      function PlayHand() : *
      {
         var _loc1_:* = new Array();
         this.theTable.numTricks = 0;
         this.theTable.ReceiveTrumpSuit(this.trumpSuit);
         this.theTable.ReceiveTrumpPlayer(this.trumpPlayer);
         trace("in playhand wgf= " + this.theTable.whoGoesFirst);
         if(this.theTable.whoGoesFirst != 0)
         {
            this.theTable.delayFirstPlayTimer.start();
         }
         else
         {
            this.theTable.PlayTricks(this.Human,this.AI1,this.AI2,this.AI3);
         }
      }
      
      public function UpdateNoWinner() : *
      {
         if(this.team1Score >= 10)
         {
            this.noWinner = false;
         }
         else if(this.team2Score >= 10)
         {
            this.noWinner = false;
         }
      }
      
      public function MoveDealer() : *
      {
         if(this.dealer == 3)
         {
            this.dealer = 0;
            this.theTable.whoGoesFirst++;
         }
         else
         {
            this.dealer++;
            this.theTable.whoGoesFirst = 0;
         }
         this.dealerSprite.x = this.dealerX[this.dealer];
         this.dealerSprite.y = this.dealerY[this.dealer];
      }
      
      function GiveTrumpPlayer() : *
      {
         this.theTable.ReceiveTrumpPlayer(this.trumpPlayer);
      }
      
      public function GiveTrumpSuit() : *
      {
         return this.trumpSuit;
      }
      
      public function getPlayersRef(param1:*, param2:*, param3:*, param4:*) : *
      {
         this.Human = param1;
         this.AI1 = param2;
         this.AI2 = param3;
         this.AI3 = param4;
         this.cSuitSprite.addEventListener(MouseEvent.CLICK,this.Human.clubTrump);
         this.dSuitSprite.addEventListener(MouseEvent.CLICK,this.Human.diamondTrump);
         this.hSuitSprite.addEventListener(MouseEvent.CLICK,this.Human.heartTrump);
         this.sSuitSprite.addEventListener(MouseEvent.CLICK,this.Human.spadeTrump);
      }
      
      public function GetTableRef(param1:*) : *
      {
         this.theTable = param1;
      }
      
      public function GetDeckRef(param1:*) : *
      {
         this.theDeck = param1;
      }
   }
}