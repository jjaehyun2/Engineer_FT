package cmodule.lua_wrapper
{
   import avm2.intrinsics.memory.li32;
   import avm2.intrinsics.memory.li8;
   import avm2.intrinsics.memory.si32;
   
   public final class FSM_luaL_optlstring extends Machine
   {
      
      public static const intRegCount:int = 7;
      
      public static const NumberRegCount:int = 0;
       
      
      public var i0:int;
      
      public var i1:int;
      
      public var i2:int;
      
      public var i3:int;
      
      public var i4:int;
      
      public var i5:int;
      
      public var i6:int;
      
      public function FSM_luaL_optlstring()
      {
         super();
      }
      
      public static function start() : void
      {
         var _loc1_:FSM_luaL_optlstring = null;
         _loc1_ = new FSM_luaL_optlstring();
         gstate.gworker = _loc1_;
      }
      
      override public final function work() : void
      {
         switch(state)
         {
            case 0:
               mstate.esp -= 4;
               si32(mstate.ebp,mstate.esp);
               mstate.ebp = mstate.esp;
               mstate.esp -= 0;
               this.i0 = _luaO_nilobject_;
               this.i1 = li32(mstate.ebp + 8);
               mstate.esp -= 8;
               this.i2 = li32(mstate.ebp + 12);
               si32(this.i1,mstate.esp);
               si32(this.i2,mstate.esp + 4);
               mstate.esp -= 4;
               FSM_index2adr.start();
            case 1:
               this.i3 = mstate.eax;
               mstate.esp += 8;
               this.i4 = li32(mstate.ebp + 16);
               this.i5 = li32(mstate.ebp + 20);
               this.i6 = this.i4;
               if(this.i3 != this.i0)
               {
                  this.i0 = li32(this.i3 + 8);
                  if(this.i0 > 0)
                  {
                     mstate.esp -= 12;
                     si32(this.i1,mstate.esp);
                     si32(this.i2,mstate.esp + 4);
                     si32(this.i5,mstate.esp + 8);
                     state = 2;
                     mstate.esp -= 4;
                     FSM_luaL_checklstring.start();
                     return;
                  }
               }
               if(this.i5 != 0)
               {
                  if(this.i4 != 0)
                  {
                     this.i1 = li8(this.i4);
                     if(this.i1 != 0)
                     {
                        this.i1 = this.i6;
                        while(true)
                        {
                           this.i2 = li8(this.i1 + 1);
                           this.i1 += 1;
                           this.i0 = this.i1;
                           if(this.i2 == 0)
                           {
                              break;
                           }
                           this.i1 = this.i0;
                        }
                     }
                     else
                     {
                        this.i1 = this.i4;
                     }
                     this.i1 -= this.i6;
                  }
                  else
                  {
                     this.i1 = 0;
                  }
                  si32(this.i1,this.i5);
                  break;
               }
               break;
            case 2:
               this.i4 = mstate.eax;
               mstate.esp += 12;
               break;
            default:
               throw "Invalid state in _luaL_optlstring";
         }
         mstate.eax = this.i4;
         mstate.esp = mstate.ebp;
         mstate.ebp = li32(mstate.esp);
         mstate.esp += 4;
         mstate.esp += 4;
         mstate.gworker = caller;
      }
   }
}