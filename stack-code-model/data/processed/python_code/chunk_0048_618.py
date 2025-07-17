package 
{

    dynamic public class TypeError extends Error
    {
        public static const length:int = 1;

        public function TypeError(param1 = "", param2 = 0)
        {
            super(param1, param2);
            this.name = prototype.name;
            return;
        }// end function

        prototype.name = "TypeError";
    }
}