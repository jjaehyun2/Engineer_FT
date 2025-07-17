package flash.errors
{
   public dynamic class EOFError extends Error
   {
       
      public function EOFError(message:String = "", id:int = 0)
      {
         super(message,id);
      }
   }
}