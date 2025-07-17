package 
{
    import fl.transitions.*;
    import fl.transitions.easing.*;
    import flash.display.*;
    import flash.events.*;

    dynamic public class contactPage extends MovieClip
    {
        public var xmlURL:String;
        public var pc:contactContent;
        public var pcsHtween:Tween;
        public var pcsXtween:Tween;
        public var Rsh:Number;
        public var rootVars:MovieClip;
        public var Rsw:Number;
        public var PageContentSprite:Sprite;
        public var pcsWtween:Tween;
        public var pcAtween:Tween;
        public var pcsYtween:Tween;
        public var pcs_H:Number;
        public var pcs_X:Number;
        public var pcs_Y:Number;
        public var pcs_W:Number;

        public function contactPage()
        {
            addFrameScript(0, frame1);
            return;
        }// end function

        public function getContent() : void
        {
            var _loc_1:MovieClip;
            pc.x = (Rsw - 721) / 2;
            pc.y = Rsh / 2 - 408 / 2;
            pc.name = "pcname";
            PageContentSprite.addChild(pc);
            _loc_1 = MovieClip(PageContentSprite.getChildByName("pcname"));
            _loc_1.kickitoff(xmlURL);
            return;
        }// end function

        public function createPCS() : void
        {
            PageContentSprite.graphics.clear();
            PageContentSprite.graphics.beginFill(0, 0.9);
            PageContentSprite.graphics.drawRect(pcs_X, pcs_Y, pcs_W, pcs_H);
            PageContentSprite.graphics.endFill();
            return;
        }// end function

        public function updatepcdimensions() : void
        {
            pc.x = (Rsw - 721) / 2;
            pc.y = Rsh / 2 - 408 / 2;
            return;
        }// end function

        public function updatePCSdimensions() : void
        {
            pcs_X = (Rsw - 721) / 2;
            pcs_Y = Rsh / 2 - 408 / 2;
            pcs_W = 721;
            pcs_H = 408;
            createPCS();
            return;
        }// end function

        function frame1()
        {
            Rsw = stage.stageWidth;
            Rsh = stage.stageHeight;
            rootVars = MovieClip(parent);
            PageContentSprite = new Sprite();
            addChild(PageContentSprite);
            pc = new contactContent();
            stage.addEventListener(Event.RESIZE, this.resizeHandler);
            pageLoadAnimation();
            return;
        }// end function

        public function pageLoadAnimation() : void
        {
            pcs_X = (Rsw - 721) / 2;
            pcs_Y = Rsh / 2 - 408 / 2;
            pcs_W = 721;
            pcs_H = 408;
            PageContentSprite.graphics.beginFill(0, 0.9);
            PageContentSprite.graphics.drawRect(pcs_X, pcs_Y, pcs_W, pcs_H);
            PageContentSprite.graphics.endFill();
            pcsXtween = new Tween(PageContentSprite, "x", Bounce.easeOut, Rsw / 2, 0, 1, true);
            pcsYtween = new Tween(PageContentSprite, "y", Bounce.easeOut, Rsh / 2, 0, 1, true);
            pcsWtween = new Tween(PageContentSprite, "width", Bounce.easeOut, 0, pcs_W, 1, true);
            pcsHtween = new Tween(PageContentSprite, "height", Bounce.easeOut, 0, pcs_H, 1, true);
            getContent();
            return;
        }// end function

        public function resizeHandler(param1:Event) : void
        {
            Rsw = stage.stageWidth;
            Rsh = stage.stageHeight;
            updatePCSdimensions();
            updatepcdimensions();
            return;
        }// end function

    }
}