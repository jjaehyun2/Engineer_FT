package 
{
    import flash.display.*;
    import flash.text.*;

    dynamic public class smallPreloader extends MovieClip
    {
        public var smallTXT:TextField;

        public function smallPreloader()
        {
            addFrameScript(0, frame1);
            return;
        }// end function

        function frame1()
        {
            stop();
            return;
        }// end function

    }
}