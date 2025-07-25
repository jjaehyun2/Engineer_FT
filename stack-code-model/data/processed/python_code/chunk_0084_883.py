package nape.callbacks
{
   import zpp_nape.util.ZPP_ListenerList;
   import zpp_nape.util.ZNPNode_ZPP_Listener;
   import zpp_nape.callbacks.ZPP_Listener;
   import zpp_nape.util.ZNPList_ListenerIterator;
   import flash._-2v;
   
   public class ListenerList extends Object
   {
      
      public function ListenerList()
      {
         if(_-2v._-7E)
         {
            return;
         }
         zpp_inner = new ZPP_ListenerList();
         zpp_inner.outer = this;
      }
      
      public static function fromArray(param1:Array) : ListenerList
      {
         var _loc4_:* = null;
         var _loc2_:ListenerList = new ListenerList();
         var _loc3_:* = 0;
         while(_loc3_ < (param1.length))
         {
            _loc4_ = param1[_loc3_];
            _loc3_++;
            _loc2_.push(_loc4_);
         }
         return _loc2_;
      }
      
      public static function fromVector(param1:Vector.<Listener>) : ListenerList
      {
         var _loc4_:* = null as Listener;
         var _loc2_:ListenerList = new ListenerList();
         var _loc3_:* = 0;
         while(_loc3_ < param1.length)
         {
            _loc4_ = param1[_loc3_];
            _loc3_++;
            _loc2_.push(_loc4_);
         }
         return _loc2_;
      }
      
      public var zpp_inner:ZPP_ListenerList;
      
      public function unshift(param1:Listener) : Boolean
      {
         zpp_inner.modify_test();
         zpp_inner.valmod();
         var _loc2_:Boolean = zpp_inner.adder != null?zpp_inner.adder(param1):true;
         if(_loc2_)
         {
            if(zpp_inner.reverse_flag)
            {
               if(zpp_inner.push_ite == null)
               {
                  if(!empty())
                  {
                     zpp_inner.valmod();
                     if(zpp_inner.zip_length)
                     {
                        zpp_inner.zip_length = false;
                        zpp_inner.user_length = zpp_inner.inner.length;
                     }
                  }
                  if(empty())
                  {
                     zpp_inner.push_ite = null;
                  }
                  else
                  {
                     zpp_inner.push_ite = zpp_inner.inner.iterator_at(zpp_inner.user_length - 1);
                  }
               }
               if(zpp_inner.push_ite == null)
               {
                  zpp_inner.push_ite = zpp_inner.inner.insert(zpp_inner.push_ite,param1.zpp_inner);
               }
               else
               {
                  zpp_inner.push_ite = zpp_inner.inner.insert(zpp_inner.push_ite,param1.zpp_inner);
               }
            }
            else
            {
               zpp_inner.inner.add(param1.zpp_inner);
            }
            zpp_inner.invalidate();
            if(zpp_inner.post_adder != null)
            {
               zpp_inner.post_adder(param1);
            }
         }
         return _loc2_;
      }
      
      public function toString() : String
      {
         var _loc4_:* = null as Listener;
         var _loc1_:String = "[";
         var _loc2_:* = true;
         var _loc3_:* = iterator();
         while(_loc3_.hasNext())
         {
            _loc4_ = _loc3_.next();
            if(!_loc2_)
            {
               _loc1_ = _loc1_ + ",";
            }
            _loc1_ = _loc1_ + (_loc4_ == null?"NULL":_loc4_.toString());
            _loc2_ = false;
         }
         return _loc1_ + "]";
      }
      
      public function shift() : Listener
      {
         var _loc2_:* = null as ZNPNode_ZPP_Listener;
         var _loc3_:* = null as Listener;
         zpp_inner.modify_test();
         zpp_inner.valmod();
         var _loc1_:ZPP_Listener = null;
         if(zpp_inner.reverse_flag)
         {
            if(zpp_inner.at_ite != null)
            {
               false;
            }
            if(false)
            {
               zpp_inner.at_ite = null;
            }
            zpp_inner.valmod();
            if(zpp_inner.zip_length)
            {
               zpp_inner.zip_length = false;
               zpp_inner.user_length = zpp_inner.inner.length;
            }
            if(zpp_inner.user_length != 1)
            {
               zpp_inner.valmod();
               if(zpp_inner.zip_length)
               {
                  zpp_inner.zip_length = false;
                  zpp_inner.user_length = zpp_inner.inner.length;
               }
            }
            if(zpp_inner.user_length == 1)
            {
               _loc2_ = null;
               _loc1_ = _loc2_ == null?zpp_inner.inner.head.elt:_loc2_.next.elt;
               _loc3_ = _loc1_.outer;
               if(zpp_inner.subber != null)
               {
                  zpp_inner.subber(_loc3_);
               }
               if(!zpp_inner.dontremove)
               {
                  zpp_inner.inner.erase(_loc2_);
               }
            }
            else
            {
               _loc2_ = zpp_inner.inner.iterator_at(zpp_inner.user_length - 2);
               _loc1_ = _loc2_ == null?zpp_inner.inner.head.elt:_loc2_.next.elt;
               _loc3_ = _loc1_.outer;
               if(zpp_inner.subber != null)
               {
                  zpp_inner.subber(_loc3_);
               }
               if(!zpp_inner.dontremove)
               {
                  zpp_inner.inner.erase(_loc2_);
               }
            }
         }
         else
         {
            _loc1_ = zpp_inner.inner.head.elt;
            _loc3_ = _loc1_.outer;
            if(zpp_inner.subber != null)
            {
               zpp_inner.subber(_loc3_);
            }
            if(!zpp_inner.dontremove)
            {
               zpp_inner.inner.pop();
            }
         }
         zpp_inner.invalidate();
         _loc3_ = _loc1_.outer;
         return _loc3_;
      }
      
      public function remove(param1:Listener) : Boolean
      {
         var _loc4_:* = null as ZPP_Listener;
         zpp_inner.modify_test();
         zpp_inner.valmod();
         var _loc2_:* = false;
         var _loc3_:ZNPNode_ZPP_Listener = zpp_inner.inner.head;
         while(_loc3_ != null)
         {
            _loc4_ = _loc3_.elt;
            if(_loc4_ == param1.zpp_inner)
            {
               _loc2_ = true;
               break;
            }
            _loc3_ = _loc3_.next;
         }
         if(_loc2_)
         {
            if(zpp_inner.subber != null)
            {
               zpp_inner.subber(param1);
            }
            if(!zpp_inner.dontremove)
            {
               zpp_inner.inner.remove(param1.zpp_inner);
            }
            zpp_inner.invalidate();
         }
         return _loc2_;
      }
      
      public function push(param1:Listener) : Boolean
      {
         zpp_inner.modify_test();
         zpp_inner.valmod();
         var _loc2_:Boolean = zpp_inner.adder != null?zpp_inner.adder(param1):true;
         if(_loc2_)
         {
            if(zpp_inner.reverse_flag)
            {
               zpp_inner.inner.add(param1.zpp_inner);
            }
            else
            {
               if(zpp_inner.push_ite == null)
               {
                  if(!empty())
                  {
                     zpp_inner.valmod();
                     if(zpp_inner.zip_length)
                     {
                        zpp_inner.zip_length = false;
                        zpp_inner.user_length = zpp_inner.inner.length;
                     }
                  }
                  if(empty())
                  {
                     zpp_inner.push_ite = null;
                  }
                  else
                  {
                     zpp_inner.push_ite = zpp_inner.inner.iterator_at(zpp_inner.user_length - 1);
                  }
               }
               if(zpp_inner.push_ite == null)
               {
                  zpp_inner.push_ite = zpp_inner.inner.insert(zpp_inner.push_ite,param1.zpp_inner);
               }
               else
               {
                  zpp_inner.push_ite = zpp_inner.inner.insert(zpp_inner.push_ite,param1.zpp_inner);
               }
            }
            zpp_inner.invalidate();
            if(zpp_inner.post_adder != null)
            {
               zpp_inner.post_adder(param1);
            }
         }
         return _loc2_;
      }
      
      public function pop() : Listener
      {
         var _loc2_:* = null as Listener;
         var _loc3_:* = null as ZNPNode_ZPP_Listener;
         zpp_inner.modify_test();
         zpp_inner.valmod();
         var _loc1_:ZPP_Listener = null;
         if(zpp_inner.reverse_flag)
         {
            _loc1_ = zpp_inner.inner.head.elt;
            _loc2_ = _loc1_.outer;
            if(zpp_inner.subber != null)
            {
               zpp_inner.subber(_loc2_);
            }
            if(!zpp_inner.dontremove)
            {
               zpp_inner.inner.pop();
            }
         }
         else
         {
            if(zpp_inner.at_ite != null)
            {
               false;
            }
            if(false)
            {
               zpp_inner.at_ite = null;
            }
            zpp_inner.valmod();
            if(zpp_inner.zip_length)
            {
               zpp_inner.zip_length = false;
               zpp_inner.user_length = zpp_inner.inner.length;
            }
            if(zpp_inner.user_length != 1)
            {
               zpp_inner.valmod();
               if(zpp_inner.zip_length)
               {
                  zpp_inner.zip_length = false;
                  zpp_inner.user_length = zpp_inner.inner.length;
               }
            }
            if(zpp_inner.user_length == 1)
            {
               _loc3_ = null;
               _loc1_ = _loc3_ == null?zpp_inner.inner.head.elt:_loc3_.next.elt;
               _loc2_ = _loc1_.outer;
               if(zpp_inner.subber != null)
               {
                  zpp_inner.subber(_loc2_);
               }
               if(!zpp_inner.dontremove)
               {
                  zpp_inner.inner.erase(_loc3_);
               }
            }
            else
            {
               _loc3_ = zpp_inner.inner.iterator_at(zpp_inner.user_length - 2);
               _loc1_ = _loc3_ == null?zpp_inner.inner.head.elt:_loc3_.next.elt;
               _loc2_ = _loc1_.outer;
               if(zpp_inner.subber != null)
               {
                  zpp_inner.subber(_loc2_);
               }
               if(!zpp_inner.dontremove)
               {
                  zpp_inner.inner.erase(_loc3_);
               }
            }
         }
         zpp_inner.invalidate();
         _loc2_ = _loc1_.outer;
         return _loc2_;
      }
      
      public function merge(param1:ListenerList) : void
      {
         var _loc3_:* = null as Listener;
         var _loc2_:* = param1.iterator();
         while(_loc2_.hasNext())
         {
            _loc3_ = _loc2_.next();
            if(!has(_loc3_))
            {
               add(_loc3_);
            }
         }
      }
      
      public function iterator() : ListenerIterator
      {
         zpp_inner.valmod();
         if(zpp_inner.iterators == null)
         {
            zpp_inner.iterators = new ZNPList_ListenerIterator();
         }
         return ListenerIterator.get(this);
      }
      
      public function has(param1:Listener) : Boolean
      {
         zpp_inner.valmod();
         return zpp_inner.inner.has(param1.zpp_inner);
      }
      
      public function get length() : int
      {
         zpp_inner.valmod();
         if(zpp_inner.zip_length)
         {
            zpp_inner.zip_length = false;
            zpp_inner.user_length = zpp_inner.inner.length;
         }
         return zpp_inner.user_length;
      }
      
      public function foreach(param1:Function) : void
      {
         var _loc4_:* = null;
         var _loc3_:ListenerIterator = iterator();
      }
      
      public function filter(param1:Function) : ListenerList
      {
         var _loc4_:* = null as Listener;
         var _loc5_:* = null;
         var _loc3_:* = 0;
      }
      
      public function empty() : Boolean
      {
         return zpp_inner.inner.head == null;
      }
      
      public function copy(param1:Boolean = false) : ListenerList
      {
         var _loc4_:* = null as Listener;
         var _loc2_:ListenerList = new ListenerList();
         var _loc3_:* = iterator();
         while(_loc3_.hasNext())
         {
            _loc4_ = _loc3_.next();
            _loc2_.push(param1?null:_loc4_);
         }
         return _loc2_;
      }
      
      public function clear() : void
      {
         if(zpp_inner.reverse_flag)
         {
            while(!(empty()))
            {
               pop();
            }
         }
         else
         {
            while(!(empty()))
            {
               shift();
            }
         }
      }
      
      public function at(param1:int) : Listener
      {
         zpp_inner.valmod();
         if(zpp_inner.reverse_flag)
         {
            zpp_inner.valmod();
            if(zpp_inner.zip_length)
            {
               zpp_inner.zip_length = false;
               zpp_inner.user_length = zpp_inner.inner.length;
            }
            param1 = zpp_inner.user_length - 1 - param1;
         }
         if(param1 >= zpp_inner.at_index)
         {
            true;
         }
         if(true)
         {
            zpp_inner.at_index = param1;
            zpp_inner.at_ite = zpp_inner.inner.iterator_at(param1);
         }
         else
         {
            while(zpp_inner.at_index != param1)
            {
               zpp_inner.at_index = zpp_inner.at_index + 1;
               zpp_inner.at_ite = zpp_inner.at_ite.next;
            }
         }
         return zpp_inner.at_ite.elt.outer;
      }
      
      public function add(param1:Listener) : Boolean
      {
         return zpp_inner.reverse_flag?push(param1):unshift(param1);
      }
   }
}