package zpp_nape.callbacks
{
   import zpp_nape.util.ZNPNode_ZPP_CbType;
   import zpp_nape.util.ZNPList_ZPP_CbType;
   import zpp_nape.util.ZNPList_ZPP_CbSetPair;
   import zpp_nape.util.ZNPNode_ZPP_CbSetPair;
   import zpp_nape.util.ZNPNode_ZPP_InteractionListener;
   import nape.phys.InteractorList;
   import nape.constraint.ConstraintList;
   import zpp_nape.util.ZNPList_ZPP_InteractionListener;
   import zpp_nape.util.ZNPNode_ZPP_ConstraintListener;
   import zpp_nape.util.ZNPList_ZPP_ConstraintListener;
   import zpp_nape.util.ZNPNode_ZPP_BodyListener;
   import zpp_nape.util.ZNPList_ZPP_BodyListener;
   import zpp_nape.space.ZPP_CbSetManager;
   import zpp_nape.util.ZNPList_ZPP_Interactor;
   import zpp_nape.util.ZNPList_ZPP_Constraint;
   import flash._-2v;
   import zpp_nape.ZPP_ID;
   
   public class ZPP_CbSet extends Object
   {
      
      public function ZPP_CbSet()
      {
         if(_-2v._-7E)
         {
            return;
         }
         cbTypes = new ZNPList_ZPP_CbType();
         listeners = new ZNPList_ZPP_InteractionListener();
         zip_listeners = true;
         bodylisteners = new ZNPList_ZPP_BodyListener();
         zip_bodylisteners = true;
         conlisteners = new ZNPList_ZPP_ConstraintListener();
         zip_conlisteners = true;
         constraints = new ZNPList_ZPP_Constraint();
         interactors = new ZNPList_ZPP_Interactor();
         id = ZPP_ID.CbSet();
         cbpairs = new ZNPList_ZPP_CbSetPair();
      }
      
      public static var zpp_pool:ZPP_CbSet;
      
      public static function setlt(param1:ZPP_CbSet, param2:ZPP_CbSet) : Boolean
      {
         var _loc5_:* = null as ZPP_CbType;
         var _loc6_:* = null as ZPP_CbType;
         var _loc3_:ZNPNode_ZPP_CbType = param1.cbTypes.head;
         var _loc4_:ZNPNode_ZPP_CbType = param2.cbTypes.head;
         while(true)
         {
            if(_loc3_ != null)
            {
               false;
            }
            if(!false)
            {
               break;
            }
            _loc5_ = _loc3_.elt;
            _loc6_ = _loc4_.elt;
            if(_loc5_.id < _loc6_.id)
            {
               return true;
            }
            if(_loc6_.id < _loc5_.id)
            {
               return false;
            }
            _loc3_ = _loc3_.next;
            _loc4_ = _loc4_.next;
         }
         if(_loc4_ != null)
         {
            false;
         }
         return false;
      }
      
      public static function get(param1:ZNPList_ZPP_CbType) : ZPP_CbSet
      {
         var _loc2_:* = null as ZPP_CbSet;
         var _loc5_:* = null as ZPP_CbType;
         if(ZPP_CbSet.zpp_pool == null)
         {
            _loc2_ = new ZPP_CbSet();
         }
         else
         {
            _loc2_ = ZPP_CbSet.zpp_pool;
            ZPP_CbSet.zpp_pool = _loc2_.next;
            _loc2_.next = null;
         }
         null;
         var _loc3_:ZNPNode_ZPP_CbType = null;
         var _loc4_:ZNPNode_ZPP_CbType = param1.head;
         while(_loc4_ != null)
         {
            _loc5_ = _loc4_.elt;
            _loc3_ = _loc2_.cbTypes.insert(_loc3_,_loc5_);
            _loc5_.cbsets.add(_loc2_);
            _loc4_ = _loc4_.next;
         }
         return _loc2_;
      }
      
      public static function compatible(param1:ZPP_InteractionListener, param2:ZPP_CbSet, param3:ZPP_CbSet) : Boolean
      {
         var _loc4_:* = null as ZPP_OptionType;
         var _loc5_:* = null as ZNPList_ZPP_CbType;
         _loc4_ = param1.options1;
         _loc5_ = param2.cbTypes;
         if(_loc4_.nonemptyintersection(_loc5_,_loc4_.includes))
         {
            false;
         }
         if(false)
         {
            false;
            _loc4_ = param1.options2;
            _loc5_ = param3.cbTypes;
            if(_loc4_.nonemptyintersection(_loc5_,_loc4_.includes))
            {
               false;
            }
         }
         if(!false)
         {
            true;
            _loc4_ = param1.options2;
            _loc5_ = param2.cbTypes;
            if(_loc4_.nonemptyintersection(_loc5_,_loc4_.includes))
            {
               false;
            }
            if(false)
            {
               false;
               _loc4_ = param1.options1;
               _loc5_ = param3.cbTypes;
               if(_loc4_.nonemptyintersection(_loc5_,_loc4_.includes))
               {
                  false;
               }
            }
         }
         return true;
      }
      
      public static function empty_intersection(param1:ZPP_CbSet, param2:ZPP_CbSet) : Boolean
      {
         var _loc6_:* = null as ZPP_CbSetPair;
         var _loc3_:ZPP_CbSetPair = null;
         var _loc4_:ZNPList_ZPP_CbSetPair = param1.cbpairs.length < param2.cbpairs.length?param1.cbpairs:param2.cbpairs;
         var _loc5_:ZNPNode_ZPP_CbSetPair = _loc4_.head;
         while(_loc5_ != null)
         {
            _loc6_ = _loc5_.elt;
            if(_loc6_.a == param1)
            {
               false;
            }
            if(!false)
            {
               true;
               if(_loc6_.a == param2)
               {
                  false;
               }
            }
            if(true)
            {
               _loc3_ = _loc6_;
               break;
            }
            _loc5_ = _loc5_.next;
         }
         if(_loc3_ == null)
         {
            if(ZPP_CbSetPair.zpp_pool == null)
            {
               _loc6_ = new ZPP_CbSetPair();
            }
            else
            {
               _loc6_ = ZPP_CbSetPair.zpp_pool;
               ZPP_CbSetPair.zpp_pool = _loc6_.next;
               _loc6_.next = null;
            }
            _loc6_.zip_listeners = true;
            if(ZPP_CbSet.setlt(param1,param2))
            {
               _loc6_.a = param1;
               _loc6_.b = param2;
            }
            else
            {
               _loc6_.a = param2;
               _loc6_.b = param1;
            }
            _loc3_ = _loc6_;
            param1.cbpairs.add(_loc3_);
            if(param2 != param1)
            {
               param2.cbpairs.add(_loc3_);
            }
         }
         if(_loc3_.zip_listeners)
         {
            _loc3_.zip_listeners = false;
            _loc3_.__validate();
         }
         return _loc3_.listeners.head == null;
      }
      
      public static function single_intersection(param1:ZPP_CbSet, param2:ZPP_CbSet, param3:ZPP_InteractionListener) : Boolean
      {
         var _loc8_:* = null as ZPP_CbSetPair;
         var _loc5_:ZPP_CbSetPair = null;
         var _loc6_:ZNPList_ZPP_CbSetPair = param1.cbpairs.length < param2.cbpairs.length?param1.cbpairs:param2.cbpairs;
         var _loc7_:ZNPNode_ZPP_CbSetPair = _loc6_.head;
         while(_loc7_ != null)
         {
            _loc8_ = _loc7_.elt;
            if(_loc8_.a == param1)
            {
               false;
            }
            if(!false)
            {
               true;
               if(_loc8_.a == param2)
               {
                  false;
               }
            }
            if(true)
            {
               _loc5_ = _loc8_;
               break;
            }
            _loc7_ = _loc7_.next;
         }
         if(_loc5_ == null)
         {
            if(ZPP_CbSetPair.zpp_pool == null)
            {
               _loc8_ = new ZPP_CbSetPair();
            }
            else
            {
               _loc8_ = ZPP_CbSetPair.zpp_pool;
               ZPP_CbSetPair.zpp_pool = _loc8_.next;
               _loc8_.next = null;
            }
            _loc8_.zip_listeners = true;
            if(ZPP_CbSet.setlt(param1,param2))
            {
               _loc8_.a = param1;
               _loc8_.b = param2;
            }
            else
            {
               _loc8_.a = param2;
               _loc8_.b = param1;
            }
            _loc5_ = _loc8_;
            param1.cbpairs.add(_loc5_);
            if(param2 != param1)
            {
               param2.cbpairs.add(_loc5_);
            }
         }
         if(_loc5_.zip_listeners)
         {
            _loc5_.zip_listeners = false;
            _loc5_.__validate();
         }
         var _loc4_:ZNPNode_ZPP_InteractionListener = _loc5_.listeners.head;
         if(_loc4_ != null)
         {
            false;
         }
         if(false)
         {
            false;
         }
         return false;
      }
      
      public static function find_all(param1:ZPP_CbSet, param2:ZPP_CbSet, param3:int, param4:Function) : void
      {
         var _loc9_:* = null as ZPP_CbSetPair;
         var _loc10_:* = null as ZPP_InteractionListener;
         var _loc6_:ZPP_CbSetPair = null;
         var _loc7_:ZNPList_ZPP_CbSetPair = param1.cbpairs.length < param2.cbpairs.length?param1.cbpairs:param2.cbpairs;
         var _loc8_:ZNPNode_ZPP_CbSetPair = _loc7_.head;
         while(_loc8_ != null)
         {
            _loc9_ = _loc8_.elt;
            if(_loc9_.a == param1)
            {
               false;
            }
            if(!false)
            {
               true;
               if(_loc9_.a == param2)
               {
                  false;
               }
            }
            if(true)
            {
               _loc6_ = _loc9_;
               break;
            }
            _loc8_ = _loc8_.next;
         }
         if(_loc6_ == null)
         {
            if(ZPP_CbSetPair.zpp_pool == null)
            {
               _loc9_ = new ZPP_CbSetPair();
            }
            else
            {
               _loc9_ = ZPP_CbSetPair.zpp_pool;
               ZPP_CbSetPair.zpp_pool = _loc9_.next;
               _loc9_.next = null;
            }
            _loc9_.zip_listeners = true;
            if(ZPP_CbSet.setlt(param1,param2))
            {
               _loc9_.a = param1;
               _loc9_.b = param2;
            }
            else
            {
               _loc9_.a = param2;
               _loc9_.b = param1;
            }
            _loc6_ = _loc9_;
            param1.cbpairs.add(_loc6_);
            if(param2 != param1)
            {
               param2.cbpairs.add(_loc6_);
            }
         }
         if(_loc6_.zip_listeners)
         {
            _loc6_.zip_listeners = false;
            _loc6_.__validate();
         }
         var _loc5_:ZNPNode_ZPP_InteractionListener = _loc6_.listeners.head;
         while(_loc5_ != null)
         {
            _loc10_ = _loc5_.elt;
            if(_loc10_.event == param3)
            {
               param4(_loc10_);
            }
            _loc5_ = _loc5_.next;
         }
      }
      
      public var zip_listeners:Boolean;
      
      public var zip_conlisteners:Boolean;
      
      public var zip_bodylisteners:Boolean;
      
      public var wrap_interactors:InteractorList;
      
      public var wrap_constraints:ConstraintList;
      
      public function validate() : void
      {
         if(zip_listeners)
         {
            zip_listeners = false;
            realvalidate_listeners();
         }
         if(zip_bodylisteners)
         {
            zip_bodylisteners = false;
            realvalidate_bodylisteners();
         }
         if(zip_conlisteners)
         {
            zip_conlisteners = false;
            realvalidate_conlisteners();
         }
      }
      
      public function realvalidate_listeners() : void
      {
         var _loc2_:* = null as ZPP_CbType;
         var _loc3_:* = null as ZNPNode_ZPP_InteractionListener;
         var _loc4_:* = null as ZNPNode_ZPP_InteractionListener;
         var _loc5_:* = null as ZNPNode_ZPP_InteractionListener;
         var _loc6_:* = null as ZPP_InteractionListener;
         var _loc7_:* = null as ZPP_Listener;
         var _loc8_:* = null as ZNPList_ZPP_InteractionListener;
         var _loc9_:* = null as ZNPNode_ZPP_InteractionListener;
         var _loc10_:* = null as ZNPNode_ZPP_InteractionListener;
         var _loc11_:* = false;
         listeners.clear();
         var _loc1_:ZNPNode_ZPP_CbType = cbTypes.head;
         while(_loc1_ != null)
         {
            _loc2_ = _loc1_.elt;
            _loc3_ = null;
            _loc4_ = listeners.head;
            _loc5_ = _loc2_.listeners.head;
            while(_loc5_ != null)
            {
               _loc6_ = _loc5_.elt;
               if(_loc4_ != null)
               {
                  false;
               }
               if(false)
               {
                  _loc5_ = _loc5_.next;
                  _loc3_ = _loc4_;
                  _loc4_ = _loc4_.next;
               }
               else
               {
                  if(_loc4_ != null)
                  {
                     true;
                     _loc7_ = _loc4_.elt;
                     if(_loc6_.precedence <= _loc7_.precedence)
                     {
                        true;
                        if(_loc6_.precedence == _loc7_.precedence)
                        {
                           false;
                        }
                     }
                  }
                  if(true)
                  {
                     if(_loc6_.space == manager.space)
                     {
                        _loc8_ = listeners;
                        if(ZNPNode_ZPP_InteractionListener.zpp_pool == null)
                        {
                           _loc10_ = new ZNPNode_ZPP_InteractionListener();
                        }
                        else
                        {
                           _loc10_ = ZNPNode_ZPP_InteractionListener.zpp_pool;
                           ZNPNode_ZPP_InteractionListener.zpp_pool = _loc10_.next;
                           _loc10_.next = null;
                        }
                        null;
                        _loc10_.elt = _loc6_;
                        _loc9_ = _loc10_;
                        if(_loc3_ == null)
                        {
                           _loc9_.next = _loc8_.head;
                           _loc8_.head = _loc9_;
                        }
                        else
                        {
                           _loc9_.next = _loc3_.next;
                           _loc3_.next = _loc9_;
                        }
                        _loc11_ = true;
                        _loc8_.modified = _loc11_;
                        _loc8_.pushmod = _loc11_;
                        _loc8_.length = _loc8_.length + 1;
                        _loc3_ = _loc9_;
                     }
                     _loc5_ = _loc5_.next;
                  }
                  else
                  {
                     _loc3_ = _loc4_;
                     _loc4_ = _loc4_.next;
                  }
               }
            }
            _loc1_ = _loc1_.next;
         }
      }
      
      public function realvalidate_conlisteners() : void
      {
         var _loc2_:* = null as ZPP_CbType;
         var _loc3_:* = null as ZNPNode_ZPP_ConstraintListener;
         var _loc4_:* = null as ZNPNode_ZPP_ConstraintListener;
         var _loc5_:* = null as ZNPNode_ZPP_ConstraintListener;
         var _loc6_:* = null as ZPP_ConstraintListener;
         var _loc7_:* = null as ZPP_Listener;
         var _loc8_:* = null as ZPP_OptionType;
         var _loc9_:* = null as ZNPList_ZPP_ConstraintListener;
         var _loc10_:* = null as ZNPNode_ZPP_ConstraintListener;
         var _loc11_:* = null as ZNPNode_ZPP_ConstraintListener;
         var _loc12_:* = false;
         conlisteners.clear();
         var _loc1_:ZNPNode_ZPP_CbType = cbTypes.head;
         while(_loc1_ != null)
         {
            _loc2_ = _loc1_.elt;
            _loc3_ = null;
            _loc4_ = conlisteners.head;
            _loc5_ = _loc2_.conlisteners.head;
            while(_loc5_ != null)
            {
               _loc6_ = _loc5_.elt;
               if(_loc4_ != null)
               {
                  false;
               }
               if(false)
               {
                  _loc5_ = _loc5_.next;
                  _loc3_ = _loc4_;
                  _loc4_ = _loc4_.next;
               }
               else
               {
                  if(_loc4_ != null)
                  {
                     true;
                     _loc7_ = _loc4_.elt;
                     if(_loc6_.precedence <= _loc7_.precedence)
                     {
                        true;
                        if(_loc6_.precedence == _loc7_.precedence)
                        {
                           false;
                        }
                     }
                  }
                  if(true)
                  {
                     _loc8_ = _loc6_.options;
                     if(!_loc8_.nonemptyintersection(cbTypes,_loc8_.excludes))
                     {
                        false;
                     }
                     if(false)
                     {
                        _loc9_ = conlisteners;
                        if(ZNPNode_ZPP_ConstraintListener.zpp_pool == null)
                        {
                           _loc11_ = new ZNPNode_ZPP_ConstraintListener();
                        }
                        else
                        {
                           _loc11_ = ZNPNode_ZPP_ConstraintListener.zpp_pool;
                           ZNPNode_ZPP_ConstraintListener.zpp_pool = _loc11_.next;
                           _loc11_.next = null;
                        }
                        null;
                        _loc11_.elt = _loc6_;
                        _loc10_ = _loc11_;
                        if(_loc3_ == null)
                        {
                           _loc10_.next = _loc9_.head;
                           _loc9_.head = _loc10_;
                        }
                        else
                        {
                           _loc10_.next = _loc3_.next;
                           _loc3_.next = _loc10_;
                        }
                        _loc12_ = true;
                        _loc9_.modified = _loc12_;
                        _loc9_.pushmod = _loc12_;
                        _loc9_.length = _loc9_.length + 1;
                        _loc3_ = _loc10_;
                     }
                     _loc5_ = _loc5_.next;
                  }
                  else
                  {
                     _loc3_ = _loc4_;
                     _loc4_ = _loc4_.next;
                  }
               }
            }
            _loc1_ = _loc1_.next;
         }
      }
      
      public function realvalidate_bodylisteners() : void
      {
         var _loc2_:* = null as ZPP_CbType;
         var _loc3_:* = null as ZNPNode_ZPP_BodyListener;
         var _loc4_:* = null as ZNPNode_ZPP_BodyListener;
         var _loc5_:* = null as ZNPNode_ZPP_BodyListener;
         var _loc6_:* = null as ZPP_BodyListener;
         var _loc7_:* = null as ZPP_Listener;
         var _loc8_:* = null as ZPP_OptionType;
         var _loc9_:* = null as ZNPList_ZPP_BodyListener;
         var _loc10_:* = null as ZNPNode_ZPP_BodyListener;
         var _loc11_:* = null as ZNPNode_ZPP_BodyListener;
         var _loc12_:* = false;
         bodylisteners.clear();
         var _loc1_:ZNPNode_ZPP_CbType = cbTypes.head;
         while(_loc1_ != null)
         {
            _loc2_ = _loc1_.elt;
            _loc3_ = null;
            _loc4_ = bodylisteners.head;
            _loc5_ = _loc2_.bodylisteners.head;
            while(_loc5_ != null)
            {
               _loc6_ = _loc5_.elt;
               if(_loc4_ != null)
               {
                  false;
               }
               if(false)
               {
                  _loc5_ = _loc5_.next;
                  _loc3_ = _loc4_;
                  _loc4_ = _loc4_.next;
               }
               else
               {
                  if(_loc4_ != null)
                  {
                     true;
                     _loc7_ = _loc4_.elt;
                     if(_loc6_.precedence <= _loc7_.precedence)
                     {
                        true;
                        if(_loc6_.precedence == _loc7_.precedence)
                        {
                           false;
                        }
                     }
                  }
                  if(true)
                  {
                     _loc8_ = _loc6_.options;
                     if(!_loc8_.nonemptyintersection(cbTypes,_loc8_.excludes))
                     {
                        false;
                     }
                     if(false)
                     {
                        _loc9_ = bodylisteners;
                        if(ZNPNode_ZPP_BodyListener.zpp_pool == null)
                        {
                           _loc11_ = new ZNPNode_ZPP_BodyListener();
                        }
                        else
                        {
                           _loc11_ = ZNPNode_ZPP_BodyListener.zpp_pool;
                           ZNPNode_ZPP_BodyListener.zpp_pool = _loc11_.next;
                           _loc11_.next = null;
                        }
                        null;
                        _loc11_.elt = _loc6_;
                        _loc10_ = _loc11_;
                        if(_loc3_ == null)
                        {
                           _loc10_.next = _loc9_.head;
                           _loc9_.head = _loc10_;
                        }
                        else
                        {
                           _loc10_.next = _loc3_.next;
                           _loc3_.next = _loc10_;
                        }
                        _loc12_ = true;
                        _loc9_.modified = _loc12_;
                        _loc9_.pushmod = _loc12_;
                        _loc9_.length = _loc9_.length + 1;
                        _loc3_ = _loc10_;
                     }
                     _loc5_ = _loc5_.next;
                  }
                  else
                  {
                     _loc3_ = _loc4_;
                     _loc4_ = _loc4_.next;
                  }
               }
            }
            _loc1_ = _loc1_.next;
         }
      }
      
      public var next:ZPP_CbSet;
      
      public var manager:ZPP_CbSetManager;
      
      public var listeners:ZNPList_ZPP_InteractionListener;
      
      public function invalidate_pairs() : void
      {
         var _loc2_:* = null as ZPP_CbSetPair;
         var _loc1_:ZNPNode_ZPP_CbSetPair = cbpairs.head;
         while(_loc1_ != null)
         {
            _loc2_ = _loc1_.elt;
            _loc2_.zip_listeners = true;
            _loc1_ = _loc1_.next;
         }
      }
      
      public var interactors:ZNPList_ZPP_Interactor;
      
      public var id:int;
      
      public var count:int;
      
      public var constraints:ZNPList_ZPP_Constraint;
      
      public var conlisteners:ZNPList_ZPP_ConstraintListener;
      
      public var cbpairs:ZNPList_ZPP_CbSetPair;
      
      public var cbTypes:ZNPList_ZPP_CbType;
      
      public var bodylisteners:ZNPList_ZPP_BodyListener;
   }
}