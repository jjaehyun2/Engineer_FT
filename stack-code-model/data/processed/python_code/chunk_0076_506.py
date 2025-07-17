package 
{

    dynamic public class DefinitionError extends Error
    {
        public static const length:int = 1;

        public function DefinitionError(param1 = "", param2 = 0)
        {
            super(param1, param2);
            this.name = prototype.name;
            return;
        }// end function

        prototype.name = "DefinitionError";
    }
}