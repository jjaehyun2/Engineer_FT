package contextMenu_fla
{
   import fl.motion.easing.Quartic;
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.external.ExternalInterface;
   import flash.geom.Rectangle;
   import flash.text.TextField;
   
   public dynamic class WContextMenuBG_2 extends MovieClip
   {
       
      
      public var bottom_mc:MovieClip;
      public var container_mc:MovieClip;
      public var firstLine_mc:MovieClip;
      public var mid_mc:MovieClip;
      public var title_txt:TextField;
      public var top_mc:MovieClip;
      public const bottomOffset:uint = 10;
      public const iggyDuration:Number = 0.2;
      public var contextContent:MovieClip;
      public var scaleTween:IggyTween;
      public var listAlphaTween:IggyTween;
      
      public function WContextMenuBG_2()
      {
         super();
         addFrameScript(0,this.frame1);
      }
      
      public function setHeight(param1:Number, param2:MovieClip) : *
      {
         var _loc3_:uint = 0;
         if(param2)
         {
            this.contextContent = param2;
            _loc3_ = this.container_mc.y + this.container_mc.height;
            this.animateOpening(_loc3_);
            ExternalInterface.call("setHeight",param1 + this.bottom_mc.height);
         }
         else
         {
            ExternalInterface.call("UIAssert","There is an empty content list in the contextmenu!");
         }
      }
      
      public function animateOpening(param1:uint) : *
      {
         var frameHeight:uint = param1;
         if(this.scaleTween != null)
         {
            this.scaleTween.stop();
            this.scaleTween = null;
         }
         if(this.listAlphaTween != null)
         {
            this.listAlphaTween.stop();
            this.listAlphaTween = null;
         }
         this.scaleTween = new IggyTween(this.mid_mc,"height",Quartic.easeOut,0,frameHeight,this.iggyDuration,true);
         this.scaleTween.motionFinishCallback = function():*
         {
            removeEventListener(Event.ENTER_FRAME,animationLoop);
         };
         this.listAlphaTween = new IggyTween(this.contextContent,"alpha",Quartic.easeOut,0,1,this.iggyDuration * 2,true);
         addEventListener(Event.ENTER_FRAME,this.animationLoop);
      }
      
      public function animationLoop() : *
      {
         this.contextContent.scrollRect = new Rectangle(0,0,this.contextContent.width,this.mid_mc.height);
         this.bottom_mc.y = this.mid_mc.y + this.mid_mc.height - this.bottomOffset;
      }
      
      function frame1() : *
      {
         this.contextContent = null;
         this.scaleTween = null;
         this.listAlphaTween = null;
      }
   }
}