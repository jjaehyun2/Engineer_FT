package nape.callbacks
{
   import zpp_nape.callbacks.ZPP_OptionType;
   import flash._-2v;
   
   public class OptionType extends Object
   {
      
      public function OptionType(param1:* = undefined, param2:* = undefined)
      {
         if(_-2v._-7E)
         {
            return;
         }
         zpp_inner = new ZPP_OptionType();
         zpp_inner.outer = this;
         if(param1 != null)
         {
            including(param1);
         }
         if(param2 != null)
         {
            excluding(param2);
         }
      }
      
      public var zpp_inner:ZPP_OptionType;
      
      public function toString() : String
      {
         if(zpp_inner.wrap_includes == null)
         {
            zpp_inner.setup_includes();
         }
         var _loc1_:String = zpp_inner.wrap_includes.toString();
         if(zpp_inner.wrap_excludes == null)
         {
            zpp_inner.setup_excludes();
         }
         var _loc2_:String = zpp_inner.wrap_excludes.toString();
         return "@{" + _loc1_ + " excluding " + _loc2_ + "}";
      }
      
      public function including(param1:* = undefined) : OptionType
      {
         zpp_inner.append(zpp_inner.includes,param1);
         return this;
      }
      
      public function get includes() : CbTypeList
      {
         if(zpp_inner.wrap_includes == null)
         {
            zpp_inner.setup_includes();
         }
         return zpp_inner.wrap_includes;
      }
      
      public function get excludes() : CbTypeList
      {
         if(zpp_inner.wrap_excludes == null)
         {
            zpp_inner.setup_excludes();
         }
         return zpp_inner.wrap_excludes;
      }
      
      public function excluding(param1:* = undefined) : OptionType
      {
         zpp_inner.append(zpp_inner.excludes,param1);
         return this;
      }
   }
}