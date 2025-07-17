package
{
   import flash.display.MovieClip;
   
   public dynamic class rightPageBG extends MovieClip
   {
       
      
      public var bg_mc:pageBG;
      
      public function rightPageBG()
      {
         super();
         addFrameScript(0,this.frame1);
      }
      
      function frame1() : *
      {
         this.bg_mc.init(24,"rightPageLine");
      }
   }
}