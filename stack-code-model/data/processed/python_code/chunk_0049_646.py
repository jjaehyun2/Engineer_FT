package zpp_nape.dynamics
{
   import nape.dynamics.ArbiterList;
   import zpp_nape.util.ZNPNode_ZPP_ColArbiter;
   import zpp_nape.util.ZNPNode_ZPP_FluidArbiter;
   import zpp_nape.util.ZNPNode_ZPP_SensorArbiter;
   import nape.dynamics.Arbiter;
   import zpp_nape.space.ZPP_Space;
   import flash._-2v;
   
   public class ZPP_SpaceArbiterList extends ArbiterList
   {
      
      public function ZPP_SpaceArbiterList()
      {
         var _loc2_:* = 0;
         if(_-2v._-7E)
         {
            return;
         }
         super();
         at_index_0 = 0;
         at_index_1 = 0;
         at_index_2 = 0;
         at_index_3 = 0;
         zip_length = true;
         _length = 0;
         lengths = [];
         var _loc1_:* = 0;
         while(_loc1_ < 4)
         {
            _loc1_++;
            _loc2_ = _loc1_;
            lengths.push(0);
         }
      }
      
      override public function zpp_vm() : void
      {
         var _loc1_:* = false;
         if(space.c_arbiters_true.modified)
         {
            _loc1_ = true;
            space.c_arbiters_true.modified = false;
         }
         if(space.c_arbiters_false.modified)
         {
            _loc1_ = true;
            space.c_arbiters_false.modified = false;
         }
         if(space.f_arbiters.modified)
         {
            _loc1_ = true;
            space.f_arbiters.modified = false;
         }
         if(space.s_arbiters.modified)
         {
            _loc1_ = true;
            space.s_arbiters.modified = false;
         }
         if(_loc1_)
         {
            zip_length = true;
            _length = 0;
            ite_0 = null;
            ite_1 = null;
            ite_2 = null;
            ite_3 = null;
         }
      }
      
      override public function zpp_gl() : int
      {
         var _loc1_:* = 0;
         var _loc2_:* = 0;
         var _loc3_:* = null as ZNPNode_ZPP_ColArbiter;
         var _loc4_:* = null as ZPP_ColArbiter;
         var _loc5_:* = null as ZNPNode_ZPP_FluidArbiter;
         var _loc6_:* = null as ZPP_FluidArbiter;
         var _loc7_:* = null as ZNPNode_ZPP_SensorArbiter;
         var _loc8_:* = null as ZPP_SensorArbiter;
         zpp_vm();
         if(zip_length)
         {
            _length = 0;
            _loc1_ = 0;
            _loc2_ = 0;
            _loc3_ = space.c_arbiters_true.head;
            while(_loc3_ != null)
            {
               _loc4_ = _loc3_.elt;
               if(_loc4_.active)
               {
                  _loc2_++;
               }
               _loc3_ = _loc3_.next;
            }
            _loc1_++;
            lengths[_loc1_] = _loc2_;
            _length = _length + _loc2_;
            _loc2_ = 0;
            _loc3_ = space.c_arbiters_false.head;
            while(_loc3_ != null)
            {
               _loc4_ = _loc3_.elt;
               if(_loc4_.active)
               {
                  _loc2_++;
               }
               _loc3_ = _loc3_.next;
            }
            _loc1_++;
            lengths[_loc1_] = _loc2_;
            _length = _length + _loc2_;
            _loc2_ = 0;
            _loc5_ = space.f_arbiters.head;
            while(_loc5_ != null)
            {
               _loc6_ = _loc5_.elt;
               if(_loc6_.active)
               {
                  _loc2_++;
               }
               _loc5_ = _loc5_.next;
            }
            _loc1_++;
            lengths[_loc1_] = _loc2_;
            _length = _length + _loc2_;
            _loc2_ = 0;
            _loc7_ = space.s_arbiters.head;
            while(_loc7_ != null)
            {
               _loc8_ = _loc7_.elt;
               if(_loc8_.active)
               {
                  _loc2_++;
               }
               _loc7_ = _loc7_.next;
            }
            _loc1_++;
            lengths[_loc1_] = _loc2_;
            _length = _length + _loc2_;
            zip_length = false;
         }
         return _length;
      }
      
      public var zip_length:Boolean;
      
      override public function unshift(param1:Arbiter) : Boolean
      {
         return false;
      }
      
      public var space:ZPP_Space;
      
      override public function shift() : Arbiter
      {
         return null;
      }
      
      override public function remove(param1:Arbiter) : Boolean
      {
         return false;
      }
      
      override public function push(param1:Arbiter) : Boolean
      {
         return false;
      }
      
      override public function pop() : Arbiter
      {
         return null;
      }
      
      public var lengths:Array;
      
      public var ite_3:ZNPNode_ZPP_SensorArbiter;
      
      public var ite_2:ZNPNode_ZPP_FluidArbiter;
      
      public var ite_1:ZNPNode_ZPP_ColArbiter;
      
      public var ite_0:ZNPNode_ZPP_ColArbiter;
      
      override public function clear() : void
      {
      }
      
      public var at_index_3:int;
      
      public var at_index_2:int;
      
      public var at_index_1:int;
      
      public var at_index_0:int;
      
      override public function at(param1:int) : Arbiter
      {
         var _loc4_:* = 0;
         var _loc5_:* = null as ZPP_ColArbiter;
         var _loc6_:* = null as ZPP_FluidArbiter;
         var _loc7_:* = null as ZPP_SensorArbiter;
         zpp_vm();
         var _loc2_:Arbiter = null;
         var _loc3_:* = 0;
         if(_loc2_ == null)
         {
            if(param1 < _loc3_ + (lengths[0]))
            {
               _loc4_ = param1 - _loc3_;
               if(_loc4_ >= at_index_0)
               {
                  true;
               }
               if(true)
               {
                  at_index_0 = 0;
                  ite_0 = space.c_arbiters_true.head;
                  while(true)
                  {
                     _loc5_ = ite_0.elt;
                     if(_loc5_.active)
                     {
                        break;
                     }
                     ite_0 = ite_0.next;
                  }
               }
               while(at_index_0 != _loc4_)
               {
                  at_index_0 = at_index_0 + 1;
                  ite_0 = ite_0.next;
                  while(true)
                  {
                     _loc5_ = ite_0.elt;
                     if(_loc5_.active)
                     {
                        break;
                     }
                     ite_0 = ite_0.next;
                  }
               }
               _loc2_ = ite_0.elt.wrapper();
            }
            else
            {
               _loc3_ = _loc3_ + (lengths[0]);
            }
         }
         if(_loc2_ == null)
         {
            if(param1 < _loc3_ + (lengths[1]))
            {
               _loc4_ = param1 - _loc3_;
               if(_loc4_ >= at_index_1)
               {
                  true;
               }
               if(true)
               {
                  at_index_1 = 0;
                  ite_1 = space.c_arbiters_false.head;
                  while(true)
                  {
                     _loc5_ = ite_1.elt;
                     if(_loc5_.active)
                     {
                        break;
                     }
                     ite_1 = ite_1.next;
                  }
               }
               while(at_index_1 != _loc4_)
               {
                  at_index_1 = at_index_1 + 1;
                  ite_1 = ite_1.next;
                  while(true)
                  {
                     _loc5_ = ite_1.elt;
                     if(_loc5_.active)
                     {
                        break;
                     }
                     ite_1 = ite_1.next;
                  }
               }
               _loc2_ = ite_1.elt.wrapper();
            }
            else
            {
               _loc3_ = _loc3_ + (lengths[1]);
            }
         }
         if(_loc2_ == null)
         {
            if(param1 < _loc3_ + (lengths[2]))
            {
               _loc4_ = param1 - _loc3_;
               if(_loc4_ >= at_index_2)
               {
                  true;
               }
               if(true)
               {
                  at_index_2 = 0;
                  ite_2 = space.f_arbiters.head;
                  while(true)
                  {
                     _loc6_ = ite_2.elt;
                     if(_loc6_.active)
                     {
                        break;
                     }
                     ite_2 = ite_2.next;
                  }
               }
               while(at_index_2 != _loc4_)
               {
                  at_index_2 = at_index_2 + 1;
                  ite_2 = ite_2.next;
                  while(true)
                  {
                     _loc6_ = ite_2.elt;
                     if(_loc6_.active)
                     {
                        break;
                     }
                     ite_2 = ite_2.next;
                  }
               }
               _loc2_ = ite_2.elt.wrapper();
            }
            else
            {
               _loc3_ = _loc3_ + (lengths[2]);
            }
         }
         if(_loc2_ == null)
         {
            if(param1 < _loc3_ + (lengths[3]))
            {
               _loc4_ = param1 - _loc3_;
               if(_loc4_ >= at_index_3)
               {
                  true;
               }
               if(true)
               {
                  at_index_3 = 0;
                  ite_3 = space.s_arbiters.head;
                  while(true)
                  {
                     _loc7_ = ite_3.elt;
                     if(_loc7_.active)
                     {
                        break;
                     }
                     ite_3 = ite_3.next;
                  }
               }
               while(at_index_3 != _loc4_)
               {
                  at_index_3 = at_index_3 + 1;
                  ite_3 = ite_3.next;
                  while(true)
                  {
                     _loc7_ = ite_3.elt;
                     if(_loc7_.active)
                     {
                        break;
                     }
                     ite_3 = ite_3.next;
                  }
               }
               _loc2_ = ite_3.elt.wrapper();
            }
            else
            {
               _loc3_ = _loc3_ + (lengths[3]);
            }
         }
         return _loc2_;
      }
      
      public var _length:int;
   }
}