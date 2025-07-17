package{
    import flash.display.*;
    import flash.events.MouseEvent;
	import flash.events.Event;

    dynamic public class Earth_1 extends MovieClip
    {
        public var startX:Object;
        public var mouseF:Number;
        public var map2:MovieClip;
        public var speed:Object;
        public var map1_memory_x:Number;
        public var map1:MovieClip;
        public var autoPlay:Boolean;
        public var drag_mc:MovieClip;
        public var autoPlay_speed:Number;
        public var isDrag:Boolean;
        public var startX2:Object;

        public function Earth_1()
        {
			//trace("-=------");
            addFrameScript(0, frame1);
            return;
        }// end function

        function frame1()
        {
            autoPlay = false;
            autoPlay_speed = 3;
            buttonMode = true;
            addEventListener(Event.ENTER_FRAME, update);
            isDrag = false;
            speed = 5;
            if (autoPlay == false)
            {
                addEventListener(MouseEvent.MOUSE_DOWN, mouseHandler);
                stage.addEventListener(MouseEvent.MOUSE_UP, mouseHandler);
            }
            return;
        }// end function

        public function update(param1) : void
        {
            if (autoPlay == false)
            {
                if (Math.abs(speed) >= 0)
                {
                    map1.x = map1.x + speed;
                }
            }
            else
            {
                map1.x = map1.x + autoPlay_speed;
            }
            if (map1.x > 0)
            {
                map1.x = -500 + speed;
            }
            if (map1.x <= -500)
            {
                map1.x = speed;
            }
            map2.x = -map1.x - 250;
            mouseF = mouseF + (mouseX - mouseF) / 10;
            if (!isDrag)
            {
                speed = speed + (-speed) / 20;
            }
            else
            {
                speed = speed + (-speed) / 5;
                mouseUpdate();
            }
            if (Math.abs(speed) < 0.5)
            {
                speed = 0;
            }
            return;
        }// end function

        public function mouseUpdate()
        {
            startX2 = startX2 + (mouseX - startX - startX2) / 3;
            map1.x = map1_memory_x + startX2;
            if (map1.x > 0)
            {
                map1.x = map1.x - 500;
            }
            if (map1.x <= -500)
            {
                map1.x = map1.x + 500;
            }
            map2.x = -map1.x - 250;
            return;
        }// end function

        public function mouseHandler(param1)
        {
            if (param1.type == MouseEvent.MOUSE_DOWN)
            {
                map1_memory_x = map1.x;
                startX = mouseX;
                startX2 = mouseX - startX;
                mouseF = mouseX;
                isDrag = true;
                mouseUpdate();
            }
            else if (param1.type == MouseEvent.MOUSE_UP)
            {
                if (isDrag)
                {
                    speed = (-(mouseF - mouseX)) / 10;
                    isDrag = false;
                }
            }
            return;
        }// end function

    }
}