package zpp_nape.util
{
   import nape.dynamics.ArbiterList;
   import flash._-2v;
   
   public class ZPP_ArbiterList extends Object
   {
      
      public function ZPP_ArbiterList()
      {
         if(_-2v._-7E)
         {
            return;
         }
         inner = new ZNPList_ZPP_Arbiter();
         _invalidated = true;
      }
      
      public static var internal:Boolean;
      
      public static function get(param1:ZNPList_ZPP_Arbiter, param2:Boolean = false) : ArbiterList
      {
         var _loc3_:ArbiterList = new ArbiterList();
         _loc3_.zpp_inner.inner = param1;
         if(param2)
         {
            _loc3_.zpp_inner.immutable = true;
         }
         _loc3_.zpp_inner.zip_length = true;
         return _loc3_;
      }
      
      public var zip_length:Boolean;
      
      public function valmod() : void
      {
         validate();
         if(inner.modified)
         {
            if(inner.pushmod)
            {
               push_ite = null;
            }
            at_ite = null;
            inner.modified = false;
            inner.pushmod = false;
            zip_length = true;
         }
      }
      
      public function validate() : void
      {
         if(_invalidated)
         {
            _invalidated = false;
            if(_validate != null)
            {
               _validate();
            }
         }
      }
      
      public var user_length:int;
      
      public var subber:Function;
      
      public var reverse_flag:Boolean;
      
      public var push_ite:ZNPNode_ZPP_Arbiter;
      
      public var post_adder:Function;
      
      public var outer:ArbiterList;
      
      public function modify_test() : void
      {
      }
      
      public function modified() : void
      {
         zip_length = true;
         at_ite = null;
         push_ite = null;
      }
      
      public var iterators:ZNPList_ArbiterIterator;
      
      public function invalidate() : void
      {
         _invalidated = true;
         if(_invalidate != null)
         {
            _invalidate(this);
         }
      }
      
      public var inner:ZNPList_ZPP_Arbiter;
      
      public var immutable:Boolean;
      
      public var dontremove:Boolean;
      
      public var at_ite:ZNPNode_ZPP_Arbiter;
      
      public var at_index:int;
      
      public var adder:Function;
      
      public var _validate:Function;
      
      public var _modifiable:Function;
      
      public var _invalidated:Boolean;
      
      public var _invalidate:Function;
   }
}