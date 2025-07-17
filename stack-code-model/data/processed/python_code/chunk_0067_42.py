package h2olib.control.headerRenderer
{
    import mx.skins.ProgrammaticSkin;
    import flash.display.Graphics;

    public class BaseSortArrow extends ProgrammaticSkin 
    {

        private var _direction:int;

        public function BaseSortArrow(direction:int=0)
        {
            super();
            _direction=direction;
        }

        override public function get measuredWidth():Number
        {
            return 6;
        }

        override public function get measuredHeight():Number
        {
            return 6;
        }

        override protected function updateDisplayList(w:Number, h:Number):void
        {
            super.updateDisplayList(w, h);

            var g:Graphics = graphics;

            g.clear();
            g.beginFill(0x111111);
            if(_direction>0) 
            {
                g.moveTo(0,0);
                g.lineTo(w, 0);
                g.lineTo(w / 2, h);
                g.lineTo(0,0);
            }
            else 
            {
                g.moveTo(w / 2,0);
                g.lineTo(w, h);
                g.lineTo(0, h);
                g.lineTo(w / 2,0);
            }
            g.endFill();
        }
    }
}