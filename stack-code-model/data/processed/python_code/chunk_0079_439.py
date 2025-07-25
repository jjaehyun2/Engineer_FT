package zpp_nape.space
{
   import zpp_nape.util.ZNPList_ZPP_Component;
   import flash._-2v;
   
   public class ZPP_Island extends Object
   {
      
      public function ZPP_Island()
      {
         if(_-2v._-7E)
         {
            return;
         }
         comps = new ZNPList_ZPP_Component();
      }
      
      public static var zpp_pool:ZPP_Island;
      
      public var waket:int;
      
      public function try_remove(param1:ZPP_Island) : Boolean
      {
         var _loc2_:ZPP_Island = null;
         var _loc3_:ZPP_Island = next;
         var _loc4_:* = false;
         while(_loc3_ != null)
         {
            if(_loc3_ == param1)
            {
               erase(_loc2_);
               _loc4_ = true;
               break;
            }
            _loc2_ = _loc3_;
            _loc3_ = _loc3_.next;
         }
         return _loc4_;
      }
      
      public function splice(param1:ZPP_Island, param2:int) : ZPP_Island
      {
         while(true)
         {
            param2--;
            if(param2 > 0)
            {
               false;
            }
            if(!false)
            {
               break;
            }
            erase(param1);
         }
         return param1.next;
      }
      
      public var sleep:Boolean;
      
      public function reverse() : void
      {
         var _loc3_:* = null as ZPP_Island;
         var _loc1_:ZPP_Island = next;
         var _loc2_:ZPP_Island = null;
         while(_loc1_ != null)
         {
            _loc3_ = _loc1_.next;
            _loc1_.next = _loc2_;
            next = _loc1_;
            _loc2_ = _loc1_;
            _loc1_ = _loc3_;
         }
         modified = true;
         pushmod = true;
      }
      
      public function remove(param1:ZPP_Island) : void
      {
         var _loc5_:* = null as ZPP_Island;
         var _loc6_:* = null as ZPP_Island;
         var _loc2_:ZPP_Island = null;
         var _loc3_:ZPP_Island = next;
         var _loc4_:* = false;
         while(_loc3_ != null)
         {
            if(_loc3_ == param1)
            {
               if(_loc2_ == null)
               {
                  _loc5_ = next;
                  _loc6_ = _loc5_.next;
                  next = _loc6_;
                  if(next == null)
                  {
                     pushmod = true;
                  }
               }
               else
               {
                  _loc5_ = _loc2_.next;
                  _loc6_ = _loc5_.next;
                  _loc2_.next = _loc6_;
                  if(_loc6_ == null)
                  {
                     pushmod = true;
                  }
               }
               _loc5_._inuse = false;
               modified = true;
               length = length - 1;
               pushmod = true;
               _loc6_;
               _loc4_ = true;
               break;
            }
            _loc2_ = _loc3_;
            _loc3_ = _loc3_.next;
         }
         _loc4_;
      }
      
      public var pushmod:Boolean;
      
      public function pop_unsafe() : ZPP_Island
      {
         var _loc1_:ZPP_Island = next;
         pop();
         return _loc1_;
      }
      
      public function pop() : void
      {
         var _loc1_:ZPP_Island = next;
         next = _loc1_.next;
         _loc1_._inuse = false;
         if(next == null)
         {
            pushmod = true;
         }
         modified = true;
         length = length - 1;
      }
      
      public var next:ZPP_Island;
      
      public var modified:Boolean;
      
      public var length:int;
      
      public function iterator_at(param1:int) : ZPP_Island
      {
         var _loc2_:ZPP_Island = next;
         while(true)
         {
            param1--;
            if(param1 > 0)
            {
               false;
            }
            if(!false)
            {
               break;
            }
            _loc2_ = _loc2_.next;
         }
         return _loc2_;
      }
      
      public function insert(param1:ZPP_Island, param2:ZPP_Island) : ZPP_Island
      {
         param2._inuse = true;
         var _loc3_:ZPP_Island = param2;
         if(param1 == null)
         {
            _loc3_.next = next;
            next = _loc3_;
         }
         else
         {
            _loc3_.next = param1.next;
            param1.next = _loc3_;
         }
         var _loc4_:* = true;
         modified = _loc4_;
         pushmod = _loc4_;
         length = length + 1;
         return _loc3_;
      }
      
      public function has(param1:ZPP_Island) : Boolean
      {
         var _loc4_:* = null as ZPP_Island;
         var _loc2_:* = false;
         var _loc3_:ZPP_Island = next;
         while(_loc3_ != null)
         {
            _loc4_ = _loc3_;
            if(_loc4_ == param1)
            {
               _loc2_ = true;
               break;
            }
            _loc3_ = _loc3_.next;
         }
         return _loc2_;
      }
      
      public function erase(param1:ZPP_Island) : ZPP_Island
      {
         var _loc2_:* = null as ZPP_Island;
         var _loc3_:* = null as ZPP_Island;
         if(param1 == null)
         {
            _loc2_ = next;
            _loc3_ = _loc2_.next;
            next = _loc3_;
            if(next == null)
            {
               pushmod = true;
            }
         }
         else
         {
            _loc2_ = param1.next;
            _loc3_ = _loc2_.next;
            param1.next = _loc3_;
            if(_loc3_ == null)
            {
               pushmod = true;
            }
         }
         _loc2_._inuse = false;
         modified = true;
         length = length - 1;
         pushmod = true;
         return _loc3_;
      }
      
      public var comps:ZNPList_ZPP_Component;
      
      public function clear() : void
      {
      }
      
      public function back() : ZPP_Island
      {
         var _loc1_:ZPP_Island = next;
         var _loc2_:ZPP_Island = _loc1_;
         while(_loc2_ != null)
         {
            _loc1_ = _loc2_;
            _loc2_ = _loc2_.next;
         }
         return _loc1_;
      }
      
      public function at(param1:int) : ZPP_Island
      {
         var _loc2_:ZPP_Island = iterator_at(param1);
         return _loc2_ != null?_loc2_:null;
      }
      
      public function addAll(param1:ZPP_Island) : void
      {
         var _loc3_:* = null as ZPP_Island;
         var _loc2_:ZPP_Island = param1.next;
         while(_loc2_ != null)
         {
            _loc3_ = _loc2_;
            add(_loc3_);
            _loc2_ = _loc2_.next;
         }
      }
      
      public function add(param1:ZPP_Island) : ZPP_Island
      {
         param1._inuse = true;
         var _loc2_:ZPP_Island = param1;
         _loc2_.next = next;
         next = _loc2_;
         modified = true;
         length = length + 1;
         return param1;
      }
      
      public var _inuse:Boolean;
   }
}