package zpp_nape.util
{
   import zpp_nape.geom.ZPP_PartitionVertex;
   
   public class ZPP_Set_ZPP_PartitionVertex extends Object
   {
      
      public function ZPP_Set_ZPP_PartitionVertex()
      {
      }
      
      public static var zpp_pool:ZPP_Set_ZPP_PartitionVertex;
      
      public function verify() : Boolean
      {
         var _loc1_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc2_:* = null as ZPP_PartitionVertex;
         var _loc3_:* = false;
         var _loc4_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc5_:* = null as ZPP_PartitionVertex;
         if(!empty())
         {
            _loc1_ = parent;
            while(_loc1_.prev != null)
            {
               _loc1_ = _loc1_.prev;
            }
            while(_loc1_ != null)
            {
               _loc2_ = _loc1_.data;
               _loc3_ = true;
               if(!empty())
               {
                  _loc4_ = parent;
                  while(_loc4_.prev != null)
                  {
                     _loc4_ = _loc4_.prev;
                  }
                  while(_loc4_ != null)
                  {
                     _loc5_ = _loc4_.data;
                     if(!_loc3_)
                     {
                        if(!lt(_loc2_,_loc5_))
                        {
                           false;
                        }
                        if(false)
                        {
                           return false;
                        }
                     }
                     else if(_loc2_ == _loc5_)
                     {
                        _loc3_ = false;
                     }
                     else
                     {
                        if(!lt(_loc5_,_loc2_))
                        {
                           false;
                        }
                        if(false)
                        {
                           return false;
                        }
                     }
                     
                     if(_loc4_.next != null)
                     {
                        _loc4_ = _loc4_.next;
                        while(_loc4_.prev != null)
                        {
                           _loc4_ = _loc4_.prev;
                        }
                     }
                     else
                     {
                        while(true)
                        {
                           if(_loc4_.parent != null)
                           {
                              false;
                           }
                           if(!false)
                           {
                              break;
                           }
                           _loc4_ = _loc4_.parent;
                        }
                        _loc4_ = _loc4_.parent;
                     }
                  }
               }
               if(_loc1_.next != null)
               {
                  _loc1_ = _loc1_.next;
                  while(_loc1_.prev != null)
                  {
                     _loc1_ = _loc1_.prev;
                  }
               }
               else
               {
                  while(true)
                  {
                     if(_loc1_.parent != null)
                     {
                        false;
                     }
                     if(!false)
                     {
                        break;
                     }
                     _loc1_ = _loc1_.parent;
                  }
                  _loc1_ = _loc1_.parent;
               }
            }
         }
         return true;
      }
      
      public function try_insert_bool(param1:ZPP_PartitionVertex) : Boolean
      {
         var _loc2_:ZPP_Set_ZPP_PartitionVertex = null;
         var _loc3_:ZPP_Set_ZPP_PartitionVertex = null;
         if(parent == null)
         {
            if(ZPP_Set_ZPP_PartitionVertex.zpp_pool == null)
            {
               _loc2_ = new ZPP_Set_ZPP_PartitionVertex();
            }
            else
            {
               _loc2_ = ZPP_Set_ZPP_PartitionVertex.zpp_pool;
               ZPP_Set_ZPP_PartitionVertex.zpp_pool = _loc2_.next;
               _loc2_.next = null;
            }
            _loc2_.alloc();
            _loc2_.data = param1;
            parent = _loc2_;
         }
         else
         {
            _loc3_ = parent;
            while(true)
            {
               if(lt(param1,_loc3_.data))
               {
                  if(_loc3_.prev == null)
                  {
                     if(ZPP_Set_ZPP_PartitionVertex.zpp_pool == null)
                     {
                        _loc2_ = new ZPP_Set_ZPP_PartitionVertex();
                     }
                     else
                     {
                        _loc2_ = ZPP_Set_ZPP_PartitionVertex.zpp_pool;
                        ZPP_Set_ZPP_PartitionVertex.zpp_pool = _loc2_.next;
                        _loc2_.next = null;
                     }
                     _loc2_.alloc();
                     _loc2_.data = param1;
                     _loc3_.prev = _loc2_;
                     _loc2_.parent = _loc3_;
                     break;
                  }
                  _loc3_ = _loc3_.prev;
                  continue;
               }
               if(lt(_loc3_.data,param1))
               {
                  if(_loc3_.next == null)
                  {
                     if(ZPP_Set_ZPP_PartitionVertex.zpp_pool == null)
                     {
                        _loc2_ = new ZPP_Set_ZPP_PartitionVertex();
                     }
                     else
                     {
                        _loc2_ = ZPP_Set_ZPP_PartitionVertex.zpp_pool;
                        ZPP_Set_ZPP_PartitionVertex.zpp_pool = _loc2_.next;
                        _loc2_.next = null;
                     }
                     _loc2_.alloc();
                     _loc2_.data = param1;
                     _loc3_.next = _loc2_;
                     _loc2_.parent = _loc3_;
                     break;
                  }
                  _loc3_ = _loc3_.next;
                  continue;
               }
               break;
            }
         }
         if(_loc2_ == null)
         {
            return false;
         }
         if(_loc2_.parent == null)
         {
            _loc2_.colour = 1;
         }
         else
         {
            _loc2_.colour = 0;
            if(_loc2_.parent.colour == 0)
            {
               __fix_dbl_red(_loc2_);
            }
         }
         return true;
      }
      
      public function try_insert(param1:ZPP_PartitionVertex) : ZPP_Set_ZPP_PartitionVertex
      {
         var _loc2_:ZPP_Set_ZPP_PartitionVertex = null;
         var _loc3_:ZPP_Set_ZPP_PartitionVertex = null;
         if(parent == null)
         {
            if(ZPP_Set_ZPP_PartitionVertex.zpp_pool == null)
            {
               _loc2_ = new ZPP_Set_ZPP_PartitionVertex();
            }
            else
            {
               _loc2_ = ZPP_Set_ZPP_PartitionVertex.zpp_pool;
               ZPP_Set_ZPP_PartitionVertex.zpp_pool = _loc2_.next;
               _loc2_.next = null;
            }
            _loc2_.alloc();
            _loc2_.data = param1;
            parent = _loc2_;
         }
         else
         {
            _loc3_ = parent;
            while(true)
            {
               if(lt(param1,_loc3_.data))
               {
                  if(_loc3_.prev == null)
                  {
                     if(ZPP_Set_ZPP_PartitionVertex.zpp_pool == null)
                     {
                        _loc2_ = new ZPP_Set_ZPP_PartitionVertex();
                     }
                     else
                     {
                        _loc2_ = ZPP_Set_ZPP_PartitionVertex.zpp_pool;
                        ZPP_Set_ZPP_PartitionVertex.zpp_pool = _loc2_.next;
                        _loc2_.next = null;
                     }
                     _loc2_.alloc();
                     _loc2_.data = param1;
                     _loc3_.prev = _loc2_;
                     _loc2_.parent = _loc3_;
                     break;
                  }
                  _loc3_ = _loc3_.prev;
                  continue;
               }
               if(lt(_loc3_.data,param1))
               {
                  if(_loc3_.next == null)
                  {
                     if(ZPP_Set_ZPP_PartitionVertex.zpp_pool == null)
                     {
                        _loc2_ = new ZPP_Set_ZPP_PartitionVertex();
                     }
                     else
                     {
                        _loc2_ = ZPP_Set_ZPP_PartitionVertex.zpp_pool;
                        ZPP_Set_ZPP_PartitionVertex.zpp_pool = _loc2_.next;
                        _loc2_.next = null;
                     }
                     _loc2_.alloc();
                     _loc2_.data = param1;
                     _loc3_.next = _loc2_;
                     _loc2_.parent = _loc3_;
                     break;
                  }
                  _loc3_ = _loc3_.next;
                  continue;
               }
               break;
            }
         }
         if(_loc2_ == null)
         {
            return _loc3_;
         }
         if(_loc2_.parent == null)
         {
            _loc2_.colour = 1;
         }
         else
         {
            _loc2_.colour = 0;
            if(_loc2_.parent.colour == 0)
            {
               __fix_dbl_red(_loc2_);
            }
         }
         return _loc2_;
      }
      
      public var swapped:Function;
      
      public function successor_node(param1:ZPP_Set_ZPP_PartitionVertex) : ZPP_Set_ZPP_PartitionVertex
      {
         var _loc2_:* = null as ZPP_Set_ZPP_PartitionVertex;
         if(param1.next != null)
         {
            param1 = param1.next;
            while(param1.prev != null)
            {
               param1 = param1.prev;
            }
         }
         else
         {
            _loc2_ = param1;
            param1 = param1.parent;
            while(true)
            {
               if(param1 != null)
               {
                  false;
               }
               if(!false)
               {
                  break;
               }
               _loc2_ = param1;
               param1 = param1.parent;
            }
         }
         return param1;
      }
      
      public function successor(param1:ZPP_PartitionVertex) : ZPP_PartitionVertex
      {
         var _loc2_:ZPP_Set_ZPP_PartitionVertex = successor_node(find(param1));
         return _loc2_ == null?null:_loc2_.data;
      }
      
      public function size() : int
      {
         var _loc2_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc3_:* = null as ZPP_PartitionVertex;
         var _loc1_:* = 0;
         if(!empty())
         {
            _loc2_ = parent;
            while(_loc2_.prev != null)
            {
               _loc2_ = _loc2_.prev;
            }
            while(_loc2_ != null)
            {
               _loc3_ = _loc2_.data;
               _loc1_++;
               if(_loc2_.next != null)
               {
                  _loc2_ = _loc2_.next;
                  while(_loc2_.prev != null)
                  {
                     _loc2_ = _loc2_.prev;
                  }
               }
               else
               {
                  while(true)
                  {
                     if(_loc2_.parent != null)
                     {
                        false;
                     }
                     if(!false)
                     {
                        break;
                     }
                     _loc2_ = _loc2_.parent;
                  }
                  _loc2_ = _loc2_.parent;
               }
            }
         }
         return _loc1_;
      }
      
      public function singular() : Boolean
      {
         if(parent != null)
         {
            false;
         }
         if(false)
         {
            false;
         }
         return false;
      }
      
      public function remove_node(param1:ZPP_Set_ZPP_PartitionVertex) : void
      {
         var _loc2_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc3_:* = null as ZPP_PartitionVertex;
         var _loc4_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc5_:* = null as ZPP_Set_ZPP_PartitionVertex;
         if(param1.next != null)
         {
            false;
         }
         if(false)
         {
            _loc2_ = param1.next;
            while(_loc2_.prev != null)
            {
               _loc2_ = _loc2_.prev;
            }
            _loc3_ = param1.data;
            param1.data = _loc2_.data;
            _loc2_.data = _loc3_;
            if(swapped != null)
            {
               swapped(param1.data,_loc2_.data);
            }
            param1 = _loc2_;
         }
         _loc2_ = param1.prev == null?param1.next:param1.prev;
         if(param1.colour == 1)
         {
            if(param1.prev == null)
            {
               true;
            }
            if(true)
            {
               _loc2_.colour = 1;
            }
            else if(param1.parent != null)
            {
               _loc4_ = param1.parent;
               while(true)
               {
                  _loc4_.colour = _loc4_.colour + 1;
                  _loc4_.prev.colour = _loc4_.prev.colour - 1;
                  _loc4_.next.colour = _loc4_.next.colour - 1;
                  _loc5_ = _loc4_.prev;
                  if(_loc5_.colour == -1)
                  {
                     __fix_neg_red(_loc5_);
                     break;
                  }
                  if(_loc5_.colour == 0)
                  {
                     if(_loc5_.prev != null)
                     {
                        false;
                     }
                     if(false)
                     {
                        __fix_dbl_red(_loc5_.prev);
                        break;
                     }
                     if(_loc5_.next != null)
                     {
                        false;
                     }
                     if(false)
                     {
                        __fix_dbl_red(_loc5_.next);
                        break;
                     }
                  }
                  _loc5_ = _loc4_.next;
                  if(_loc5_.colour == -1)
                  {
                     __fix_neg_red(_loc5_);
                     break;
                  }
                  if(_loc5_.colour == 0)
                  {
                     if(_loc5_.prev != null)
                     {
                        false;
                     }
                     if(false)
                     {
                        __fix_dbl_red(_loc5_.prev);
                        break;
                     }
                     if(_loc5_.next != null)
                     {
                        false;
                     }
                     if(false)
                     {
                        __fix_dbl_red(_loc5_.next);
                        break;
                     }
                  }
                  if(_loc4_.colour == 2)
                  {
                     if(_loc4_.parent == null)
                     {
                        _loc4_.colour = 1;
                     }
                     else
                     {
                        _loc4_ = _loc4_.parent;
                        continue;
                     }
                  }
                  break;
               }
            }
            
         }
         _loc4_ = param1.parent;
         if(_loc4_ == null)
         {
            parent = _loc2_;
         }
         else if(_loc4_.prev == param1)
         {
            _loc4_.prev = _loc2_;
         }
         else
         {
            _loc4_.next = _loc2_;
         }
         
         if(_loc2_ != null)
         {
            _loc2_.parent = _loc4_;
         }
         _loc4_ = null;
         param1.next = _loc4_;
         _loc4_ = _loc4_;
         param1.prev = _loc4_;
         param1.parent = _loc4_;
         _loc4_ = param1;
         _loc4_.free();
         _loc4_.next = ZPP_Set_ZPP_PartitionVertex.zpp_pool;
         ZPP_Set_ZPP_PartitionVertex.zpp_pool = _loc4_;
      }
      
      public function remove(param1:ZPP_PartitionVertex) : void
      {
         var _loc2_:ZPP_Set_ZPP_PartitionVertex = find(param1);
         remove_node(_loc2_);
      }
      
      public var prev:ZPP_Set_ZPP_PartitionVertex;
      
      public function predecessor_node(param1:ZPP_Set_ZPP_PartitionVertex) : ZPP_Set_ZPP_PartitionVertex
      {
         var _loc2_:* = null as ZPP_Set_ZPP_PartitionVertex;
         if(param1.prev != null)
         {
            param1 = param1.prev;
            while(param1.next != null)
            {
               param1 = param1.next;
            }
         }
         else
         {
            _loc2_ = param1;
            param1 = param1.parent;
            while(true)
            {
               if(param1 != null)
               {
                  false;
               }
               if(!false)
               {
                  break;
               }
               _loc2_ = param1;
               param1 = param1.parent;
            }
         }
         return param1;
      }
      
      public function predecessor(param1:ZPP_PartitionVertex) : ZPP_PartitionVertex
      {
         var _loc2_:ZPP_Set_ZPP_PartitionVertex = predecessor_node(find(param1));
         return _loc2_ == null?null:_loc2_.data;
      }
      
      public function pop_front() : ZPP_PartitionVertex
      {
         var _loc1_:ZPP_Set_ZPP_PartitionVertex = parent;
         while(_loc1_.prev != null)
         {
            _loc1_ = _loc1_.prev;
         }
         var _loc2_:ZPP_PartitionVertex = _loc1_.data;
         remove_node(_loc1_);
         return _loc2_;
      }
      
      public var parent:ZPP_Set_ZPP_PartitionVertex;
      
      public var next:ZPP_Set_ZPP_PartitionVertex;
      
      public var lt:Function;
      
      public function lower_bound(param1:ZPP_PartitionVertex) : ZPP_PartitionVertex
      {
         var _loc3_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc4_:* = null as ZPP_PartitionVertex;
         var _loc2_:ZPP_PartitionVertex = null;
         if(!empty())
         {
            _loc3_ = parent;
            while(_loc3_.prev != null)
            {
               _loc3_ = _loc3_.prev;
            }
            while(_loc3_ != null)
            {
               _loc4_ = _loc3_.data;
               if(!lt(_loc4_,param1))
               {
                  _loc2_ = _loc4_;
                  break;
               }
               if(_loc3_.next != null)
               {
                  _loc3_ = _loc3_.next;
                  while(_loc3_.prev != null)
                  {
                     _loc3_ = _loc3_.prev;
                  }
               }
               else
               {
                  while(true)
                  {
                     if(_loc3_.parent != null)
                     {
                        false;
                     }
                     if(!false)
                     {
                        break;
                     }
                     _loc3_ = _loc3_.parent;
                  }
                  _loc3_ = _loc3_.parent;
               }
            }
         }
         return _loc2_;
      }
      
      public function insert(param1:ZPP_PartitionVertex) : ZPP_Set_ZPP_PartitionVertex
      {
         var _loc2_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc3_:* = null as ZPP_Set_ZPP_PartitionVertex;
         if(ZPP_Set_ZPP_PartitionVertex.zpp_pool == null)
         {
            _loc2_ = new ZPP_Set_ZPP_PartitionVertex();
         }
         else
         {
            _loc2_ = ZPP_Set_ZPP_PartitionVertex.zpp_pool;
            ZPP_Set_ZPP_PartitionVertex.zpp_pool = _loc2_.next;
            _loc2_.next = null;
         }
         _loc2_.alloc();
         _loc2_.data = param1;
         if(parent == null)
         {
            parent = _loc2_;
         }
         else
         {
            _loc3_ = parent;
            while(true)
            {
               if(lt(_loc2_.data,_loc3_.data))
               {
                  if(_loc3_.prev == null)
                  {
                     _loc3_.prev = _loc2_;
                     _loc2_.parent = _loc3_;
                     break;
                  }
                  _loc3_ = _loc3_.prev;
               }
               else
               {
                  if(_loc3_.next == null)
                  {
                     _loc3_.next = _loc2_;
                     _loc2_.parent = _loc3_;
                     break;
                  }
                  _loc3_ = _loc3_.next;
               }
            }
         }
         if(_loc2_.parent == null)
         {
            _loc2_.colour = 1;
         }
         else
         {
            _loc2_.colour = 0;
            if(_loc2_.parent.colour == 0)
            {
               __fix_dbl_red(_loc2_);
            }
         }
         return _loc2_;
      }
      
      public function has_weak(param1:ZPP_PartitionVertex) : Boolean
      {
         return !(find_weak(param1) == null);
      }
      
      public function has(param1:ZPP_PartitionVertex) : Boolean
      {
         return !(find(param1) == null);
      }
      
      public function free() : void
      {
         data = null;
         lt = null;
         swapped = null;
      }
      
      public function first() : ZPP_PartitionVertex
      {
         var _loc1_:ZPP_Set_ZPP_PartitionVertex = parent;
         while(_loc1_.prev != null)
         {
            _loc1_ = _loc1_.prev;
         }
         return _loc1_.data;
      }
      
      public function find_weak(param1:ZPP_PartitionVertex) : ZPP_Set_ZPP_PartitionVertex
      {
         var _loc2_:ZPP_Set_ZPP_PartitionVertex = parent;
         while(_loc2_ != null)
         {
            if(lt(param1,_loc2_.data))
            {
               _loc2_ = _loc2_.prev;
               continue;
            }
            if(lt(_loc2_.data,param1))
            {
               _loc2_ = _loc2_.next;
               continue;
            }
            break;
         }
         return _loc2_;
      }
      
      public function find(param1:ZPP_PartitionVertex) : ZPP_Set_ZPP_PartitionVertex
      {
         var _loc2_:ZPP_Set_ZPP_PartitionVertex = parent;
         while(true)
         {
            if(_loc2_ != null)
            {
               false;
            }
            if(!false)
            {
               break;
            }
            if(lt(param1,_loc2_.data))
            {
               _loc2_ = _loc2_.prev;
            }
            else
            {
               _loc2_ = _loc2_.next;
            }
         }
         return _loc2_;
      }
      
      public function empty() : Boolean
      {
         return parent == null;
      }
      
      public var data:ZPP_PartitionVertex;
      
      public var colour:int;
      
      public function clear_with(param1:Function) : void
      {
         var _loc2_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc3_:* = null as ZPP_Set_ZPP_PartitionVertex;
         if(parent == null)
         {
            return;
         }
         _loc2_ = parent;
         while(_loc2_ != null)
         {
            if(_loc2_.prev == null)
            {
               if(_loc2_.next == null)
               {
                  param1(_loc2_.data);
                  _loc3_ = _loc2_.parent;
                  if(_loc3_ != null)
                  {
                     if(_loc2_ == _loc3_.prev)
                     {
                        _loc3_.prev = null;
                     }
                     else
                     {
                        _loc3_.next = null;
                     }
                     _loc2_.parent = null;
                  }
               }
            }
            if(_loc2_.prev != null)
            {
               _loc2_ = _loc2_.prev;
            }
            else
            {
               _loc2_ = _loc2_.next != null?_loc2_.next:_loc3_;
            }
         }
         parent = null;
      }
      
      public function clear_node(param1:ZPP_Set_ZPP_PartitionVertex, param2:Function) : ZPP_Set_ZPP_PartitionVertex
      {
         param2(param1.data);
         var _loc3_:ZPP_Set_ZPP_PartitionVertex = param1.parent;
         if(_loc3_ != null)
         {
            if(param1 == _loc3_.prev)
            {
               _loc3_.prev = null;
            }
            else
            {
               _loc3_.next = null;
            }
            param1.parent = null;
         }
         return _loc3_;
      }
      
      public function clear() : void
      {
         var _loc1_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc2_:* = null as ZPP_Set_ZPP_PartitionVertex;
         if(parent == null)
         {
            null;
         }
         else
         {
            _loc1_ = parent;
            while(_loc1_ != null)
            {
               if(_loc1_.prev == null)
               {
                  if(_loc1_.next == null)
                  {
                     _loc2_ = _loc1_.parent;
                     if(_loc2_ != null)
                     {
                        if(_loc1_ == _loc2_.prev)
                        {
                           _loc2_.prev = null;
                        }
                        else
                        {
                           _loc2_.next = null;
                        }
                        _loc1_.parent = null;
                     }
                  }
               }
               if(_loc1_.prev != null)
               {
                  _loc1_ = _loc1_.prev;
               }
               else
               {
                  _loc1_ = _loc1_.next != null?_loc1_.next:_loc2_;
               }
            }
            parent = null;
         }
      }
      
      public function alloc() : void
      {
      }
      
      public function __fix_neg_red(param1:ZPP_Set_ZPP_PartitionVertex) : void
      {
         var _loc4_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc5_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc6_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc7_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc8_:* = 0;
         var _loc9_:* = null as ZPP_PartitionVertex;
         var _loc2_:ZPP_Set_ZPP_PartitionVertex = param1.parent;
         if(_loc2_.prev == param1)
         {
            _loc4_ = param1.prev;
            _loc5_ = param1.next;
            _loc6_ = _loc5_.prev;
            _loc7_ = _loc5_.next;
            _loc4_.colour = 0;
            _loc8_ = 1;
            _loc2_.colour = _loc8_;
            param1.colour = _loc8_;
            param1.next = _loc6_;
            if(_loc6_ != null)
            {
               _loc6_.parent = param1;
            }
            _loc9_ = _loc2_.data;
            _loc2_.data = _loc5_.data;
            _loc5_.data = _loc9_;
            if(swapped != null)
            {
               swapped(_loc2_.data,_loc5_.data);
            }
            _loc5_.prev = _loc7_;
            if(_loc7_ != null)
            {
               _loc7_.parent = _loc5_;
            }
            _loc5_.next = _loc2_.next;
            if(_loc2_.next != null)
            {
               _loc2_.next.parent = _loc5_;
            }
            _loc2_.next = _loc5_;
            if(_loc5_ != null)
            {
               _loc5_.parent = _loc2_;
            }
         }
         else
         {
            _loc4_ = param1.next;
            _loc5_ = param1.prev;
            _loc6_ = _loc5_.next;
            _loc7_ = _loc5_.prev;
            _loc4_.colour = 0;
            _loc8_ = 1;
            _loc2_.colour = _loc8_;
            param1.colour = _loc8_;
            param1.prev = _loc6_;
            if(_loc6_ != null)
            {
               _loc6_.parent = param1;
            }
            _loc9_ = _loc2_.data;
            _loc2_.data = _loc5_.data;
            _loc5_.data = _loc9_;
            if(swapped != null)
            {
               swapped(_loc2_.data,_loc5_.data);
            }
            _loc5_.next = _loc7_;
            if(_loc7_ != null)
            {
               _loc7_.parent = _loc5_;
            }
            _loc5_.prev = _loc2_.prev;
            if(_loc2_.prev != null)
            {
               _loc2_.prev.parent = _loc5_;
            }
            _loc2_.prev = _loc5_;
            if(_loc5_ != null)
            {
               _loc5_.parent = _loc2_;
            }
         }
         if(_loc2_.prev == param1)
         {
            _loc3_ = _loc4_;
            if(_loc3_.prev != null)
            {
               false;
            }
            if(false)
            {
               __fix_dbl_red(_loc3_.prev);
            }
            else
            {
               if(_loc3_.next != null)
               {
                  false;
               }
               if(false)
               {
                  __fix_dbl_red(_loc3_.next);
               }
            }
            return;
         }
         var _loc3_:ZPP_Set_ZPP_PartitionVertex = _loc4_;
         if(_loc3_.prev != null)
         {
            false;
         }
         if(false)
         {
            __fix_dbl_red(_loc3_.prev);
         }
         else
         {
            if(_loc3_.next != null)
            {
               false;
            }
            if(false)
            {
               __fix_dbl_red(_loc3_.next);
            }
         }
      }
      
      public function __fix_dbl_red(param1:ZPP_Set_ZPP_PartitionVertex) : void
      {
         var _loc2_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc3_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc4_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc5_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc6_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc7_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc8_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc9_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc10_:* = null as ZPP_Set_ZPP_PartitionVertex;
         var _loc11_:* = null as ZPP_Set_ZPP_PartitionVertex;
         while(true)
         {
            _loc2_ = param1.parent;
            _loc3_ = _loc2_.parent;
            if(_loc3_ == null)
            {
               _loc2_.colour = 1;
               break;
            }
            if(_loc2_ == _loc3_.prev)
            {
               _loc6_ = _loc3_;
               _loc10_ = _loc3_.next;
               if(param1 == _loc2_.prev)
               {
                  _loc4_ = param1;
                  _loc5_ = _loc2_;
                  _loc7_ = param1.prev;
                  _loc8_ = param1.next;
                  _loc9_ = _loc2_.next;
               }
               else
               {
                  _loc4_ = _loc2_;
                  _loc5_ = param1;
                  _loc7_ = _loc2_.prev;
                  _loc8_ = param1.prev;
                  _loc9_ = param1.next;
               }
            }
            else
            {
               _loc4_ = _loc3_;
               _loc7_ = _loc3_.prev;
               if(param1 == _loc2_.prev)
               {
                  _loc5_ = param1;
                  _loc6_ = _loc2_;
                  _loc8_ = param1.prev;
                  _loc9_ = param1.next;
                  _loc10_ = _loc2_.next;
               }
               else
               {
                  _loc5_ = _loc2_;
                  _loc6_ = param1;
                  _loc8_ = _loc2_.prev;
                  _loc9_ = param1.prev;
                  _loc10_ = param1.next;
               }
            }
            _loc11_ = _loc3_.parent;
            if(_loc11_ == null)
            {
               parent = _loc5_;
            }
            else if(_loc11_.prev == _loc3_)
            {
               _loc11_.prev = _loc5_;
            }
            else
            {
               _loc11_.next = _loc5_;
            }
            
            if(_loc5_ != null)
            {
               _loc5_.parent = _loc11_;
            }
            _loc4_.prev = _loc7_;
            if(_loc7_ != null)
            {
               _loc7_.parent = _loc4_;
            }
            _loc4_.next = _loc8_;
            if(_loc8_ != null)
            {
               _loc8_.parent = _loc4_;
            }
            _loc5_.prev = _loc4_;
            if(_loc4_ != null)
            {
               _loc4_.parent = _loc5_;
            }
            _loc5_.next = _loc6_;
            if(_loc6_ != null)
            {
               _loc6_.parent = _loc5_;
            }
            _loc6_.prev = _loc9_;
            if(_loc9_ != null)
            {
               _loc9_.parent = _loc6_;
            }
            _loc6_.next = _loc10_;
            if(_loc10_ != null)
            {
               _loc10_.parent = _loc6_;
            }
            _loc5_.colour = _loc3_.colour - 1;
            _loc4_.colour = 1;
            _loc6_.colour = 1;
            if(_loc5_ == parent)
            {
               parent.colour = 1;
            }
            else
            {
               if(_loc5_.colour == 0)
               {
                  false;
               }
               if(false)
               {
                  param1 = _loc5_;
                  continue;
               }
            }
            break;
         }
      }
   }
}