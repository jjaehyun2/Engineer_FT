package p0ng_fla
{
   import flash.display.MovieClip;
   import flash.display.SimpleButton;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.ui.Mouse;
   
   public dynamic class MainTimeline extends MovieClip
   {
       
      
      public var yspeed2:Number;
      
      public var yspeed3:Number;
      
      public var paddle1:MovieClip;
      
      public var paddle2:MovieClip;
      
      public var paddle3:MovieClip;
      
      public var paddle4:MovieClip;
      
      public var endtext:TextField;
      
      public var ball2:MovieClip;
      
      public var ball3:MovieClip;
      
      public var scoreText1:TextField;
      
      public var scoreText2:TextField;
      
      public var Startbutton2:SimpleButton;
      
      public var xspeed2:Number;
      
      public var xspeed3:Number;
      
      public var xspeed:Number;
      
      public var score1:Number;
      
      public var score2:Number;
      
      public var yspeed:Number;
      
      public var ballcount:Number;
      
      public var Startbutton:SimpleButton;
      
      public var ball:MovieClip;
      
      public function MainTimeline()
      {
         super();
         addFrameScript(0,this.frame1,1,this.frame2,2,this.frame3);
      }
      
      public function cleanup2() : *
      {
         this.ball.removeEventListener(Event.ENTER_FRAME,this.moveBall);
         this.paddle4.removeEventListener(Event.ENTER_FRAME,this.computerPaddle4);
         this.paddle3.removeEventListener(Event.ENTER_FRAME,this.computerPaddle3);
         this.paddle2.removeEventListener(Event.ENTER_FRAME,this.computerPaddle);
         this.paddle1.removeEventListener(Event.ENTER_FRAME,this.playerPaddle);
         this.ball3.removeEventListener(Event.ENTER_FRAME,this.moveBall3);
         this.ball2.removeEventListener(Event.ENTER_FRAME,this.moveBall2);
         this.ball.removeEventListener(Event.ENTER_FRAME,this.moveBall);
      }
      
      public function playerPaddle(param1:Event) : void
      {
         param1.target.y = mouseY - param1.target.height / 2 + 150;
      }
      
      public function moveBall2(param1:Event) : void
      {
         this.ball2.x = this.ball2.x + this.xspeed2;
         this.ball2.y = this.ball2.y + this.yspeed2;
         if(this.ball2.x > 1280)
         {
            this.ball.x = 300;
            this.ball.y = 200;
            this.xspeed = 6;
            this.yspeed = 6;
            this.ball2.x = 300;
            this.ball2.y = -200;
            this.xspeed2 = 0;
            this.yspeed2 = 0;
            this.ball3.x = 300;
            this.ball3.y = -200;
            this.xspeed3 = 0;
            this.yspeed3 = 0;
            this.score2++;
            this.scoreText2.text = String(this.score2);
            this.ballcount = 0;
         }
         if(this.ball2.x < 0)
         {
            this.ball.x = 300;
            this.ball.y = 200;
            this.xspeed = 6;
            this.yspeed = 6;
            this.ball2.x = 300;
            this.ball2.y = -200;
            this.xspeed2 = 0;
            this.yspeed2 = 0;
            this.ball3.x = 300;
            this.ball3.y = -200;
            this.xspeed3 = 0;
            this.yspeed3 = 0;
            this.score1++;
            this.scoreText1.text = String(this.score1);
            this.ballcount = 0;
         }
         if(this.ball2.y > 720 || this.ball2.y < 0)
         {
            this.yspeed2 = this.yspeed2 * -1;
         }
         if(this.ball2.hitTestObject(this.paddle1) && this.xspeed2 > 0)
         {
            this.xspeed2 = this.xspeed2 * -1.03;
            this.ballcount++;
         }
         if(this.ball2.hitTestObject(this.paddle2) && this.xspeed2 < 0)
         {
            this.xspeed2 = this.xspeed2 * -1.03;
         }
         if(this.ball2.hitTestObject(this.paddle3) && this.xspeed2 < 0)
         {
            this.xspeed2 = this.xspeed2 * -1.03;
         }
         if(this.ballcount == 3)
         {
            this.ball2.x = 300;
            this.ball2.y = 200;
            this.xspeed2 = 3;
            this.yspeed2 = 3;
            this.paddle3.x = 10;
            this.paddle3.y = 360;
         }
         if(this.ballcount == 5)
         {
            this.ball3.x = 300;
            this.ball3.y = 200;
            this.xspeed3 = 3;
            this.yspeed3 = 3;
            this.paddle4.x = 30;
            this.paddle4.y = 360;
         }
      }
      
      public function moveBall3(param1:Event) : void
      {
         this.ball3.x = this.ball3.x + this.xspeed3;
         this.ball3.y = this.ball3.y + this.yspeed3;
         if(this.ball3.x > 1280)
         {
            this.ball.x = 300;
            this.ball.y = 200;
            this.xspeed = 6;
            this.yspeed = 6;
            this.ball2.x = 300;
            this.ball2.y = -200;
            this.xspeed2 = 0;
            this.yspeed2 = 0;
            this.ball3.x = 300;
            this.ball3.y = -200;
            this.xspeed3 = 0;
            this.yspeed3 = 0;
            this.score2++;
            this.scoreText2.text = String(this.score2);
            this.ballcount = 0;
         }
         if(this.ball3.x < 0)
         {
            this.ball.x = 300;
            this.ball.y = 200;
            this.xspeed = 6;
            this.yspeed = 6;
            this.ball2.x = 300;
            this.ball2.y = -200;
            this.xspeed2 = 0;
            this.yspeed2 = 0;
            this.ball3.x = 300;
            this.ball3.y = -200;
            this.xspeed3 = 0;
            this.yspeed3 = 0;
            this.score1++;
            this.scoreText1.text = String(this.score1);
            this.ballcount = 0;
         }
         if(this.ball3.y > 720 || this.ball3.y < 0)
         {
            this.yspeed3 = this.yspeed3 * -1;
         }
         if(this.ball3.hitTestObject(this.paddle1) && this.xspeed3 > 0)
         {
            this.xspeed3 = this.xspeed3 * -1.15;
            this.ballcount++;
         }
         if(this.ball3.hitTestObject(this.paddle2) && this.xspeed3 < 0)
         {
            this.xspeed3 = this.xspeed3 * -1.15;
         }
         if(this.ball3.hitTestObject(this.paddle4) && this.xspeed3 < 0)
         {
            this.xspeed3 = this.xspeed3 * -1.15;
         }
         if(this.score1 == 5)
         {
            this.cleanup2();
            gotoAndStop(3);
            this.endtext.text = "You Win";
         }
         if(this.score2 == 5)
         {
            this.cleanup2();
            gotoAndStop(3);
            this.endtext.text = "You Lose";
         }
      }
      
      public function startgame(param1:MouseEvent) : void
      {
         gotoAndStop(2);
      }
      
      public function startgame2(param1:MouseEvent) : void
      {
         gotoAndStop(2);
      }
      
      public function computerPaddle(param1:Event) : void
      {
         if(param1.target.y > this.ball.y)
         {
            param1.target.y = param1.target.y - 7.5;
         }
         if(param1.target.y < this.ball.y)
         {
            param1.target.y = param1.target.y + 7.5;
         }
      }
      
      function frame1() : *
      {
         stop();
         this.Startbutton.addEventListener(MouseEvent.CLICK,this.startgame);
      }
      
      function frame2() : *
      {
         Mouse.hide();
         stop();
         this.xspeed = 8;
         this.yspeed = 8;
         this.xspeed2 = 0;
         this.yspeed2 = 0;
         this.xspeed3 = 0;
         this.yspeed3 = 0;
         this.score1 = 0;
         this.score2 = 0;
         this.ballcount = 0;
         this.ball.addEventListener(Event.ENTER_FRAME,this.moveBall);
         this.ball2.addEventListener(Event.ENTER_FRAME,this.moveBall2);
         this.ball3.addEventListener(Event.ENTER_FRAME,this.moveBall3);
         this.paddle1.addEventListener(Event.ENTER_FRAME,this.playerPaddle);
         this.paddle2.addEventListener(Event.ENTER_FRAME,this.computerPaddle);
         this.paddle3.addEventListener(Event.ENTER_FRAME,this.computerPaddle3);
         this.paddle4.addEventListener(Event.ENTER_FRAME,this.computerPaddle4);
      }
      
      function frame3() : *
      {
         this.Startbutton2.addEventListener(MouseEvent.CLICK,this.startgame);
         Mouse.show();
      }
      
      public function computerPaddle4(param1:Event) : void
      {
         if(param1.target.y > this.ball3.y)
         {
            param1.target.y = param1.target.y - 2.65;
         }
         if(param1.target.y < this.ball3.y)
         {
            param1.target.y = param1.target.y + 2.65;
         }
      }
      
      public function computerPaddle3(param1:Event) : void
      {
         if(param1.target.y > this.ball2.y)
         {
            param1.target.y = param1.target.y - 2.33;
         }
         if(param1.target.y < this.ball2.y)
         {
            param1.target.y = param1.target.y + 2.33;
         }
      }
      
      public function moveBall(param1:Event) : void
      {
         this.ball.x = this.ball.x + this.xspeed;
         this.ball.y = this.ball.y + this.yspeed;
         if(this.ball.x > 1280)
         {
            this.ball.x = 300;
            this.ball.y = 200;
            this.xspeed = 6;
            this.yspeed = 6;
            this.ball2.x = 300;
            this.ball2.y = -200;
            this.xspeed2 = 0;
            this.yspeed2 = 0;
            this.ball3.x = 300;
            this.ball3.y = -200;
            this.xspeed3 = 0;
            this.yspeed3 = 0;
            this.score2++;
            this.scoreText2.text = String(this.score2);
            this.ballcount = 0;
         }
         if(this.ball.x < 0)
         {
            this.ball.x = 300;
            this.ball2.x = 300;
            this.ball2.y = -200;
            this.xspeed2 = 0;
            this.yspeed2 = 0;
            this.ball3.x = 300;
            this.ball3.y = -200;
            this.xspeed3 = 0;
            this.yspeed3 = 0;
            this.score1++;
            this.xspeed = 6;
            this.yspeed = 6;
            this.scoreText1.text = String(this.score1);
            this.ballcount = 0;
         }
         if(this.ball.y > 720 || this.ball.y < 0)
         {
            this.yspeed = this.yspeed * -1.01;
         }
         if(this.ball.hitTestObject(this.paddle1) && this.xspeed > 0)
         {
            this.xspeed = this.xspeed * -1.01;
            this.ballcount++;
         }
         if(this.ball.hitTestObject(this.paddle2) && this.xspeed < 0)
         {
            this.xspeed = this.xspeed * -1.01;
            this.ballcount++;
         }
      }
   }
}