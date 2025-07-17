package 
{
    import flash.display.*;
    import flash.events.*;

    dynamic public class meetTHEcrew extends MovieClip
    {
        public var xmlURL:String;
        public var pc:holder;
        public var Rsh:Number;
        public var Rsw:Number;
        public var pageC:PageContent;

        public function meetTHEcrew()
        {
            addFrameScript(0, frame1);
            return;
        }// end function

        function frame1()
        {
            Rsw = stage.stageWidth;
            Rsh = stage.stageHeight;
            pc = new holder();
            pc.alpha = 1;
            pc.x = Math.round(Rsw / 2 - 879 / 2);
            pc.y = Math.round(Rsh / 2 - 385 / 2);
            addChild(pc);
            pageC = new PageContent();
            pageC.x = 0;
            pageC.y = 0;
            pc.addChild(pageC);
            pageC.kickitoff(xmlURL);
            stage.addEventListener(Event.RESIZE, this.resizeHandler);
            return;
        }// end function

        public function resizeHandler(param1:Event) : void
        {
            Rsw = stage.stageWidth;
            Rsh = stage.stageHeight;
            pc.x = Math.round(Rsw / 2 - 879 / 2);
            pc.y = Math.round(Rsh / 2 - 385 / 2);
            return;
        }// end function

    }
}