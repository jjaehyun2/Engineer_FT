package zpp_nape.util
{
   import nape.geom.RayResultList;
   import flash._-2v;
   
   public class ZPP_RayResultList extends Object
   {
      
      public function ZPP_RayResultList()
      {
         if(_-2v._-7E)
         {
            return;
         }
         inner = new ZNPList_RayResult();
         _invalidated = true;
      }
      
      public static var internal:Boolean;
      
      public static function get(param1:ZNPList_RayResult, param2:Boolean = false) : RayResultList
      {
         var _loc3_:RayResultList = new RayResultList();
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
      
      public var push_ite:ZNPNode_RayResult;
      
      public var post_adder:Function;
      
      public var outer:RayResultList;
      
      public function modify_test() : void
      {
      }
      
      public function modified() : void
      {
         zip_length = true;
         at_ite = null;
         push_ite = null;
      }
      
      public var iterators:ZNPList_RayResultIterator;
      
      public function invalidate() : void
      {
         _invalidated = true;
         if(_invalidate != null)
         {
            _invalidate(this);
         }
      }
      
      public var inner:ZNPList_RayResult;
      
      public var immutable:Boolean;
      
      public var dontremove:Boolean;
      
      public var at_ite:ZNPNode_RayResult;
      
      public var at_index:int;
      
      public var adder:Function;
      
      public var _validate:Function;
      
      public var _modifiable:Function;
      
      public var _invalidated:Boolean;
      
      public var _invalidate:Function;
   }
}