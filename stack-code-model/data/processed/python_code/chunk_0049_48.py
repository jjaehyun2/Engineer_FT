package cmodule.lua_wrapper
{
   import avm2.intrinsics.memory.li32;
   import avm2.intrinsics.memory.si32;
   
   public final class FSM_luaB_assert extends Machine
   {
      
      public static const intRegCount:int = 3;
      
      public static const NumberRegCount:int = 0;
       
      
      public var i0:int;
      
      public var i1:int;
      
      public var i2:int;
      
      public function FSM_luaB_assert()
      {
         super();
      }
      
      public static function start() : void
      {
         var _loc1_:FSM_luaB_assert = null;
         _loc1_ = new FSM_luaB_assert();
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
               this.i0 = 1;
               mstate.esp -= 8;
               this.i1 = li32(mstate.ebp + 8);
               si32(this.i1,mstate.esp);
               si32(this.i0,mstate.esp + 4);
               mstate.esp -= 4;
               FSM_index2adr.start();
            case 1:
               this.i0 = mstate.eax;
               mstate.esp += 8;
               this.i2 = _luaO_nilobject_;
               if(this.i0 != this.i2)
               {
                  this.i0 = li32(this.i0 + 8);
                  if(this.i0 != -1)
                  {
                     addr147:
                     this.i0 = 1;
                     mstate.esp -= 8;
                     si32(this.i1,mstate.esp);
                     si32(this.i0,mstate.esp + 4);
                     mstate.esp -= 4;
                     FSM_index2adr.start();
                     this.i0 = mstate.eax;
                     mstate.esp += 8;
                     this.i2 = li32(this.i0 + 8);
                     if(this.i2 != 0)
                     {
                        if(this.i2 == 1)
                        {
                           this.i0 = li32(this.i0);
                           if(this.i0 == 0)
                           {
                              addr216:
                              this.i0 = 2;
                              mstate.esp -= 8;
                              si32(this.i1,mstate.esp);
                              si32(this.i0,mstate.esp + 4);
                              mstate.esp -= 4;
                              FSM_index2adr.start();
                              addr246:
                              this.i0 = mstate.eax;
                              mstate.esp += 8;
                              this.i2 = _luaO_nilobject_;
                              if(this.i0 != this.i2)
                              {
                                 this.i0 = li32(this.i0 + 8);
                                 if(this.i0 >= 1)
                                 {
                                    this.i0 = 0;
                                    mstate.esp -= 12;
                                    this.i2 = 2;
                                    si32(this.i1,mstate.esp);
                                    si32(this.i2,mstate.esp + 4);
                                    si32(this.i0,mstate.esp + 8);
                                    state = 5;
                                    mstate.esp -= 4;
                                    FSM_luaL_checklstring.start();
                                    return;
                                 }
                              }
                              this.i0 = __2E_str53343;
                              break;
                           }
                        }
                        this.i0 = li32(this.i1 + 8);
                        this.i1 = li32(this.i1 + 12);
                        this.i0 -= this.i1;
                        this.i0 /= 12;
                        mstate.eax = this.i0;
                        §§goto(addr427);
                     }
                     §§goto(addr216);
                  }
               }
               this.i0 = __2E_str11186329;
               mstate.esp -= 12;
               this.i2 = 1;
               si32(this.i1,mstate.esp);
               si32(this.i2,mstate.esp + 4);
               si32(this.i0,mstate.esp + 8);
               state = 2;
               mstate.esp -= 4;
               FSM_luaL_argerror.start();
               return;
            case 2:
               mstate.esp += 12;
               §§goto(addr147);
            case 3:
               §§goto(addr147);
            case 4:
               §§goto(addr246);
            case 5:
               this.i0 = mstate.eax;
               mstate.esp += 12;
               break;
            case 6:
               mstate.esp += 12;
               this.i1 = 0;
               mstate.eax = this.i1;
               addr427:
               mstate.esp = mstate.ebp;
               mstate.ebp = li32(mstate.esp);
               mstate.esp += 4;
               mstate.esp += 4;
               mstate.gworker = caller;
               return;
            default:
               throw "Invalid state in _luaB_assert";
         }
         this.i2 = __2E_str54344;
         mstate.esp -= 12;
         si32(this.i1,mstate.esp);
         si32(this.i2,mstate.esp + 4);
         si32(this.i0,mstate.esp + 8);
         state = 6;
         mstate.esp -= 4;
         FSM_luaL_error.start();
      }
   }
}