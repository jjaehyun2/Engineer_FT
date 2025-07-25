package zpp_nape.util
{
   import nape.dynamics.ContactList;
   import zpp_nape.dynamics.ZPP_Contact;
   import flash._-2v;
   
   public class ZPP_ContactList extends Object
   {
      
      public function ZPP_ContactList()
      {
         if(_-2v._-7E)
         {
            return;
         }
         inner = new ZPP_Contact();
         _invalidated = true;
      }
      
      public static var internal:Boolean;
      
      public static function get(param1:ZPP_Contact, param2:Boolean = false) : ContactList
      {
         var _loc3_:ContactList = new ContactList();
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
      
      public var push_ite:ZPP_Contact;
      
      public var post_adder:Function;
      
      public var outer:ContactList;
      
      public function modify_test() : void
      {
      }
      
      public function modified() : void
      {
         zip_length = true;
         at_ite = null;
         push_ite = null;
      }
      
      public var iterators:ZNPList_ContactIterator;
      
      public function invalidate() : void
      {
         _invalidated = true;
         if(_invalidate != null)
         {
            _invalidate(this);
         }
      }
      
      public var inner:ZPP_Contact;
      
      public var immutable:Boolean;
      
      public var dontremove:Boolean;
      
      public var at_ite:ZPP_Contact;
      
      public var at_index:int;
      
      public var adder:Function;
      
      public var _validate:Function;
      
      public var _modifiable:Function;
      
      public var _invalidated:Boolean;
      
      public var _invalidate:Function;
   }
}