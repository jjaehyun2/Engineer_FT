package 
{
    import fl.transitions.*;
    import fl.transitions.easing.*;
    import flash.display.*;
    import flash.events.*;
    import flash.geom.*;

    dynamic public class featuresPage extends MovieClip
    {
        public var xmlURL:String;
        public var pc:contentPage;
        public var pcsHtween:Tween;
        public var scrollBASE:scrollBase;
        public var pcsXtween:Tween;
        public var Rsh:Number;
        public var Rsw:Number;
        public var PageMask:Sprite;
        public var scrolla:scroller;
        public var pcsWtween:Tween;
        public var pcAtween:Tween;
        public var rectangle:Rectangle;
        public var _W:Number;
        public var pcsYtween:Tween;
        public var percentage:Number;
        public var holder:MovieClip;
        public var page:Tween;
        public var _H:Number;
        public var pageMask_border:maskBorder;
        public var _X:Number;
        public var _Y:Number;

        public function featuresPage()
        {
            addFrameScript(0, frame1);
            return;
        }// end function

        public function scrollContent(param1:Event) : void
        {
            var _loc_2:Number;
            percentage = (scrolla.y - 115) / rectangle.height;
            _loc_2 = pc.height - Rsh + 200;
            page = new Tween(pc, "y", Regular.easeOut, pc.y, percentage * (-_loc_2) + 95, 2, true);
            return;
        }// end function

        public function stopMove(param1:Event) : void
        {
            scrolla.stopDrag();
            stage.removeEventListener(MouseEvent.MOUSE_MOVE, scrollContent);
            stage.removeEventListener(MouseEvent.MOUSE_UP, stopMove);
            return;
        }// end function

        public function startMove(param1:Event) : void
        {
            scrolla.startDrag(false, rectangle);
            stage.addEventListener(MouseEvent.MOUSE_MOVE, scrollContent);
            stage.addEventListener(MouseEvent.MOUSE_UP, stopMove);
            return;
        }// end function

        public function getContent() : void
        {
            holder.graphics.clear();
            holder.graphics.beginFill(789516, 1);
            holder.graphics.drawRect(_X, _Y, 700, _H);
            holder.graphics.endFill();
            scrollBASE.x = _X + _W;
            scrollBASE.y = _Y + 10;
            scrollBASE.height = _H - 20;
            scrolla.x = _X + _W - 5;
            scrolla.y = _Y + 20;
            rectangle = new Rectangle(_X + _W - 5, _Y + 20, 0, _H - 108);
            holder.addChild(scrollBASE);
            holder.addChild(scrolla);
            scrollBASE.alpha = 1;
            scrolla.alpha = 1;
            scrolla.buttonMode = true;
            scrolla.addEventListener(MouseEvent.MOUSE_DOWN, startMove);
            pageMask_border.x = 0;
            pageMask_border.y = _Y;
            pageMask_border.width = Rsw;
            pageMask_border.height = _H;
            PageMask.graphics.clear();
            PageMask.graphics.beginFill(16777215, 1);
            PageMask.graphics.drawRect(0, _Y, Rsw, _H);
            PageMask.graphics.endFill();
            pc.x = _X;
            pc.y = _Y;
            holder.addChild(pc);
            pc.kickitoff(xmlURL);
            pc.mask = PageMask;
            stage.addEventListener(Event.RESIZE, this.resizeHandler);
            resizeHandler(null);
            return;
        }// end function

        function frame1()
        {
            Rsw = stage.stageWidth;
            Rsh = stage.stageHeight;
            holder = new MovieClip();
            addChild(holder);
            PageMask = new Sprite();
            addChild(PageMask);
            pageMask_border = new maskBorder();
            addChild(pageMask_border);
            pc = new contentPage();
            scrollBASE = new scrollBase();
            scrolla = new scroller();
            _X = Rsw / 2 - 700 / 2;
            _Y = 95;
            _W = 700;
            _H = Rsh - 150;
            percentage = 0;
            getContent();
            return;
        }// end function

        public function resizeHandler(param1:Event) : void
        {
            Rsw = stage.stageWidth;
            Rsh = stage.stageHeight;
            _X = Rsw / 2 - 700 / 2;
            _Y = 95;
            _W = 700;
            _H = Rsh - 150;
            holder.graphics.clear();
            holder.graphics.beginFill(789516, 1);
            holder.graphics.drawRect(_X, _Y, 700, _H);
            holder.graphics.endFill();
            pc.x = _X;
            pc.y = _Y;
            scrollBASE.x = _X + _W;
            scrollBASE.y = _Y + 10;
            scrollBASE.height = _H - 20;
            scrolla.x = _X + _W - 5;
            rectangle.x = _X + _W - 5;
            rectangle.y = _Y + 20;
            rectangle.height = _H - 108;
            scrolla.y = rectangle.y + rectangle.height * percentage;
            pageMask_border.x = 0;
            pageMask_border.y = _Y;
            pageMask_border.width = Rsw;
            pageMask_border.height = _H;
            PageMask.graphics.clear();
            PageMask.graphics.beginFill(16777215, 1);
            PageMask.graphics.drawRect(0, _Y, Rsw, _H);
            PageMask.graphics.endFill();
            return;
        }// end function

    }
}