package cmodule.lua_wrapper
{
   import avm2.intrinsics.memory.lf64;
   import avm2.intrinsics.memory.li32;
   import avm2.intrinsics.memory.sf64;
   import avm2.intrinsics.memory.si32;
   
   public final class FSM_as3_new extends Machine
   {
      
      public static const intRegCount:int = 9;
      
      public static const NumberRegCount:int = 1;
       
      
      public var i0:int;
      
      public var i1:int;
      
      public var i2:int;
      
      public var i3:int;
      
      public var i4:int;
      
      public var i5:int;
      
      public var i6:int;
      
      public var i8:int;
      
      public var f0:Number;
      
      public var i7:int;
      
      public function FSM_as3_new()
      {
         super();
      }
      
      public static function start() : void
      {
         var _loc1_:FSM_as3_new = null;
         _loc1_ = new FSM_as3_new();
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
               this.i0 = 0;
               this.i1 = li32(mstate.ebp + 8);
               this.i2 = li32(this.i1 + 8);
               this.i3 = li32(this.i1 + 12);
               mstate.esp -= 12;
               this.i4 = 1;
               si32(this.i1,mstate.esp);
               si32(this.i4,mstate.esp + 4);
               si32(this.i0,mstate.esp + 8);
               state = 1;
               mstate.esp -= 4;
               FSM_lua_tolstring.start();
               return;
            case 1:
               this.i0 = mstate.eax;
               this.i2 -= this.i3;
               mstate.esp += 12;
               this.i2 /= 12;
               this.i3 = this.i1 + 12;
               this.i4 = this.i1 + 8;
               if(this.i0 == 0)
               {
                  this.i5 = __2E_str25232;
                  mstate.esp -= 12;
                  this.i6 = 1;
                  si32(this.i1,mstate.esp);
                  si32(this.i6,mstate.esp + 4);
                  si32(this.i5,mstate.esp + 8);
                  state = 2;
                  mstate.esp -= 4;
                  FSM_luaL_argerror.start();
                  return;
               }
               addr183:
               this.i5 = __2E_str131;
               mstate.esp -= 8;
               si32(this.i0,mstate.esp);
               si32(this.i5,mstate.esp + 4);
               mstate.esp -= 4;
               FSM_strstr.start();
               break;
            case 2:
               mstate.esp += 12;
               §§goto(addr183);
            case 3:
               this.i5 = mstate.eax;
               mstate.esp += 8;
               if(uint(this.i5) > uint(this.i0))
               {
                  mstate.esp -= 8;
                  this.i6 = this.i5 - this.i0;
                  si32(this.i0,mstate.esp);
                  si32(this.i6,mstate.esp + 4);
                  state = 4;
                  mstate.esp -= 4;
                  mstate.funcs[_AS3_StringN]();
                  return;
               }
               this.i5 = 0;
               this.i6 = this.i0;
               §§goto(addr309);
               break;
            case 4:
               this.i6 = mstate.eax;
               mstate.esp += 8;
               this.i7 = this.i5 + 2;
               this.i5 = this.i6;
               this.i6 = this.i7;
               addr309:
               mstate.esp -= 8;
               si32(this.i5,mstate.esp);
               si32(this.i6,mstate.esp + 4);
               state = 5;
               mstate.esp -= 4;
               mstate.funcs[_AS3_NSGetS]();
               return;
            case 5:
               this.i6 = mstate.eax;
               mstate.esp += 8;
               if(this.i5 != 0)
               {
                  mstate.esp -= 4;
                  si32(this.i5,mstate.esp);
                  state = 6;
                  mstate.esp -= 4;
                  mstate.funcs[_AS3_Release]();
                  return;
               }
               addr395:
               if(this.i6 == 0)
               {
                  this.i2 = __2E_str28235;
                  mstate.esp -= 12;
                  si32(this.i1,mstate.esp);
                  si32(this.i2,mstate.esp + 4);
                  si32(this.i0,mstate.esp + 8);
                  state = 7;
                  mstate.esp -= 4;
                  FSM_luaL_error.start();
                  return;
               }
               this.i5 = 0;
               this.i7 = li32(this.i4);
               this.i8 = li32(this.i3);
               this.i7 -= this.i8;
               mstate.esp -= 16;
               this.i8 = 2;
               this.i7 /= 12;
               si32(this.i1,mstate.esp);
               si32(this.i8,mstate.esp + 4);
               si32(this.i7,mstate.esp + 8);
               si32(this.i5,mstate.esp + 12);
               state = 8;
               mstate.esp -= 4;
               FSM_create_as3_value_from_lua_stack.start();
               return;
               break;
            case 6:
               mstate.esp += 4;
               §§goto(addr395);
            case 7:
               mstate.esp += 12;
               this.i0 = 0;
               addr2558:
               mstate.eax = this.i0;
               §§goto(addr2562);
            case 8:
               this.i5 = mstate.eax;
               mstate.esp += 16;
               mstate.esp -= 8;
               si32(this.i6,mstate.esp);
               si32(this.i5,mstate.esp + 4);
               state = 9;
               mstate.esp -= 4;
               mstate.funcs[_AS3_New]();
               return;
            case 9:
               this.i7 = mstate.eax;
               mstate.esp += 8;
               if(this.i7 == 0)
               {
                  this.i2 = __2E_str29236;
                  mstate.esp -= 4;
                  si32(this.i6,mstate.esp);
                  state = 10;
                  mstate.esp -= 4;
                  mstate.funcs[_AS3_Release]();
                  return;
               }
               mstate.esp -= 8;
               si32(this.i1,mstate.esp);
               si32(this.i7,mstate.esp + 4);
               state = 13;
               mstate.esp -= 4;
               FSM_push_as3_lua_userdata.start();
               return;
               break;
            case 10:
               mstate.esp += 4;
               mstate.esp -= 4;
               si32(this.i5,mstate.esp);
               state = 11;
               mstate.esp -= 4;
               mstate.funcs[_AS3_Release]();
               return;
            case 11:
               mstate.esp += 4;
               mstate.esp -= 12;
               si32(this.i1,mstate.esp);
               si32(this.i2,mstate.esp + 4);
               si32(this.i0,mstate.esp + 8);
               state = 12;
               mstate.esp -= 4;
               FSM_luaL_error.start();
               return;
            case 12:
               mstate.esp += 12;
               this.i1 = 0;
               mstate.eax = this.i1;
               addr2562:
               mstate.esp = mstate.ebp;
               mstate.ebp = li32(mstate.esp);
               mstate.esp += 4;
               mstate.esp += 4;
               mstate.gworker = caller;
               return;
            case 13:
               mstate.esp += 8;
               mstate.esp -= 4;
               si32(this.i5,mstate.esp);
               state = 14;
               mstate.esp -= 4;
               mstate.funcs[_AS3_Release]();
               return;
            case 14:
               mstate.esp += 4;
               mstate.esp -= 4;
               si32(this.i6,mstate.esp);
               state = 15;
               mstate.esp -= 4;
               mstate.funcs[_AS3_Release]();
               return;
            case 15:
               mstate.esp += 4;
               this.i0 = li32(this.i4);
               this.i5 = li32(this.i3);
               this.i6 = this.i2 + 1;
               this.i0 -= this.i5;
               this.i0 /= 12;
               if(this.i0 != this.i6)
               {
                  mstate.esp -= 8;
                  si32(this.i1,mstate.esp);
                  si32(this.i2,mstate.esp + 4);
                  state = 16;
                  mstate.esp -= 4;
                  FSM_dump_lua_stack.start();
                  return;
               }
               addr2555:
               this.i0 = 1;
               §§goto(addr2558);
               break;
            case 16:
               mstate.esp += 8;
               this.i0 = li32(this.i1 + 16);
               this.i5 = li32(this.i0 + 68);
               this.i0 = li32(this.i0 + 64);
               this.i7 = this.i1 + 16;
               if(uint(this.i5) >= uint(this.i0))
               {
                  mstate.esp -= 4;
                  si32(this.i1,mstate.esp);
                  state = 17;
                  mstate.esp -= 4;
                  FSM_luaC_step.start();
                  return;
               }
               §§goto(addr961);
               break;
            case 17:
               mstate.esp += 4;
               addr961:
               this.i0 = __2E_str19226;
               this.i5 = li32(this.i4);
               mstate.esp -= 12;
               this.i8 = 19;
               si32(this.i1,mstate.esp);
               si32(this.i0,mstate.esp + 4);
               si32(this.i8,mstate.esp + 8);
               state = 18;
               mstate.esp -= 4;
               FSM_luaS_newlstr.start();
               return;
            case 18:
               this.i0 = mstate.eax;
               mstate.esp += 12;
               si32(this.i0,this.i5);
               this.i0 = 4;
               si32(this.i0,this.i5 + 8);
               this.i0 = li32(this.i4);
               this.i0 += 12;
               si32(this.i0,this.i4);
               this.i0 = li32(this.i7);
               this.i5 = li32(this.i0 + 68);
               this.i0 = li32(this.i0 + 64);
               if(uint(this.i5) >= uint(this.i0))
               {
                  mstate.esp -= 4;
                  si32(this.i1,mstate.esp);
                  state = 19;
                  mstate.esp -= 4;
                  FSM_luaC_step.start();
                  return;
               }
               §§goto(addr1111);
               break;
            case 19:
               mstate.esp += 4;
               addr1111:
               this.i0 = __2E_str1100;
               this.i5 = li32(this.i4);
               mstate.esp -= 12;
               this.i8 = 1;
               si32(this.i1,mstate.esp);
               si32(this.i0,mstate.esp + 4);
               si32(this.i8,mstate.esp + 8);
               state = 20;
               mstate.esp -= 4;
               FSM_luaS_newlstr.start();
               return;
            case 20:
               this.i0 = mstate.eax;
               mstate.esp += 12;
               si32(this.i0,this.i5);
               this.i0 = 4;
               si32(this.i0,this.i5 + 8);
               this.i0 = li32(this.i4);
               this.i5 = this.i0 + 12;
               si32(this.i5,this.i4);
               this.i5 = 1080524800;
               this.i8 = 0;
               si32(this.i8,this.i0 + 12);
               si32(this.i5,this.i0 + 16);
               this.i5 = 3;
               si32(this.i5,this.i0 + 20);
               this.i0 = li32(this.i4);
               this.i0 += 12;
               si32(this.i0,this.i4);
               this.i0 = li32(this.i7);
               this.i5 = li32(this.i0 + 68);
               this.i0 = li32(this.i0 + 64);
               if(uint(this.i5) >= uint(this.i0))
               {
                  mstate.esp -= 4;
                  si32(this.i1,mstate.esp);
                  state = 21;
                  mstate.esp -= 4;
                  FSM_luaC_step.start();
                  return;
               }
               §§goto(addr1307);
               break;
            case 21:
               mstate.esp += 4;
               addr1307:
               this.i0 = __2E_str2101;
               this.i5 = li32(this.i4);
               mstate.esp -= 12;
               this.i8 = 38;
               si32(this.i1,mstate.esp);
               si32(this.i0,mstate.esp + 4);
               si32(this.i8,mstate.esp + 8);
               state = 22;
               mstate.esp -= 4;
               FSM_luaS_newlstr.start();
               return;
            case 22:
               this.i0 = mstate.eax;
               mstate.esp += 12;
               si32(this.i0,this.i5);
               this.i0 = 4;
               si32(this.i0,this.i5 + 8);
               this.i0 = li32(this.i4);
               this.i5 = this.i0 + 12;
               si32(this.i5,this.i4);
               this.f0 = Number(this.i2);
               sf64(this.f0,this.i0 + 12);
               this.i2 = 3;
               si32(this.i2,this.i0 + 20);
               this.i0 = li32(this.i4);
               this.i0 += 12;
               si32(this.i0,this.i4);
               this.i0 = li32(this.i7);
               this.i2 = li32(this.i0 + 68);
               this.i0 = li32(this.i0 + 64);
               if(uint(this.i2) >= uint(this.i0))
               {
                  mstate.esp -= 4;
                  si32(this.i1,mstate.esp);
                  state = 23;
                  mstate.esp -= 4;
                  FSM_luaC_step.start();
                  return;
               }
               §§goto(addr1496);
               break;
            case 23:
               mstate.esp += 4;
               addr1496:
               this.i0 = __2E_str3102;
               this.i2 = li32(this.i4);
               mstate.esp -= 12;
               this.i5 = 16;
               si32(this.i1,mstate.esp);
               si32(this.i0,mstate.esp + 4);
               si32(this.i5,mstate.esp + 8);
               state = 24;
               mstate.esp -= 4;
               FSM_luaS_newlstr.start();
               return;
            case 24:
               this.i0 = mstate.eax;
               mstate.esp += 12;
               si32(this.i0,this.i2);
               this.i0 = 4;
               si32(this.i0,this.i2 + 8);
               this.i0 = li32(this.i4);
               this.i2 = this.i0 + 12;
               si32(this.i2,this.i4);
               this.i5 = li32(this.i3);
               this.i2 -= this.i5;
               this.i2 /= 12;
               this.i2 += -7;
               this.f0 = Number(this.i2);
               sf64(this.f0,this.i0 + 12);
               this.i2 = 3;
               si32(this.i2,this.i0 + 20);
               this.i0 = li32(this.i4);
               this.i0 += 12;
               si32(this.i0,this.i4);
               this.i0 = li32(this.i7);
               this.i2 = li32(this.i0 + 68);
               this.i0 = li32(this.i0 + 64);
               if(uint(this.i2) >= uint(this.i0))
               {
                  mstate.esp -= 4;
                  si32(this.i1,mstate.esp);
                  state = 25;
                  mstate.esp -= 4;
                  FSM_luaC_step.start();
                  return;
               }
               §§goto(addr1709);
               break;
            case 25:
               mstate.esp += 4;
               addr1709:
               this.i0 = __2E_str4103;
               this.i2 = li32(this.i4);
               mstate.esp -= 12;
               this.i5 = 18;
               si32(this.i1,mstate.esp);
               si32(this.i0,mstate.esp + 4);
               si32(this.i5,mstate.esp + 8);
               state = 26;
               mstate.esp -= 4;
               FSM_luaS_newlstr.start();
               return;
            case 26:
               this.i0 = mstate.eax;
               mstate.esp += 12;
               si32(this.i0,this.i2);
               this.i0 = 4;
               si32(this.i0,this.i2 + 8);
               this.i0 = li32(this.i4);
               this.i2 = this.i0 + 12;
               si32(this.i2,this.i4);
               this.f0 = Number(this.i6);
               sf64(this.f0,this.i0 + 12);
               this.i2 = 3;
               si32(this.i2,this.i0 + 20);
               this.i0 = li32(this.i4);
               this.i0 += 12;
               si32(this.i0,this.i4);
               this.i0 = li32(this.i7);
               this.i2 = li32(this.i0 + 68);
               this.i0 = li32(this.i0 + 64);
               if(uint(this.i2) >= uint(this.i0))
               {
                  mstate.esp -= 4;
                  si32(this.i1,mstate.esp);
                  state = 27;
                  mstate.esp -= 4;
                  FSM_luaC_step.start();
                  return;
               }
               §§goto(addr1898);
               break;
            case 27:
               mstate.esp += 4;
               addr1898:
               this.i0 = __2E_str10143;
               this.i2 = li32(this.i4);
               mstate.esp -= 12;
               this.i5 = 1;
               si32(this.i1,mstate.esp);
               si32(this.i0,mstate.esp + 4);
               si32(this.i5,mstate.esp + 8);
               state = 28;
               mstate.esp -= 4;
               FSM_luaS_newlstr.start();
               return;
            case 28:
               this.i0 = mstate.eax;
               mstate.esp += 12;
               si32(this.i0,this.i2);
               this.i0 = 4;
               si32(this.i0,this.i2 + 8);
               this.i0 = li32(this.i4);
               this.i0 += 12;
               si32(this.i0,this.i4);
               this.i0 = li32(this.i7);
               this.i2 = li32(this.i0 + 68);
               this.i0 = li32(this.i0 + 64);
               if(uint(this.i2) >= uint(this.i0))
               {
                  mstate.esp -= 4;
                  si32(this.i1,mstate.esp);
                  state = 29;
                  mstate.esp -= 4;
                  FSM_luaC_step.start();
                  return;
               }
               §§goto(addr2048);
               break;
            case 29:
               mstate.esp += 4;
               addr2048:
               this.i0 = 10;
               this.i2 = li32(this.i4);
               this.i5 = li32(this.i3);
               this.i2 -= this.i5;
               this.i2 /= 12;
               mstate.esp -= 12;
               this.i2 += -1;
               si32(this.i1,mstate.esp);
               si32(this.i0,mstate.esp + 4);
               si32(this.i2,mstate.esp + 8);
               state = 30;
               mstate.esp -= 4;
               FSM_luaV_concat.start();
               return;
            case 30:
               mstate.esp += 12;
               this.i0 = li32(this.i4);
               this.i0 += -108;
               si32(this.i0,this.i4);
               mstate.esp -= 8;
               this.i0 = -2;
               si32(this.i1,mstate.esp);
               si32(this.i0,mstate.esp + 4);
               mstate.esp -= 4;
               FSM_index2adr.start();
            case 31:
               this.i0 = mstate.eax;
               mstate.esp += 8;
               this.i2 = li32(this.i4);
               this.f0 = lf64(this.i0);
               sf64(this.f0,this.i2);
               this.i0 = li32(this.i0 + 8);
               si32(this.i0,this.i2 + 8);
               this.i0 = li32(this.i4);
               this.i0 += 12;
               si32(this.i0,this.i4);
               mstate.esp -= 8;
               this.i0 = -3;
               si32(this.i1,mstate.esp);
               si32(this.i0,mstate.esp + 4);
               mstate.esp -= 4;
               FSM_index2adr.start();
            case 32:
               this.i0 = mstate.eax;
               mstate.esp += 8;
               this.i2 = li32(this.i4);
               this.i5 = this.i0;
               this.i6 = this.i0 + 12;
               if(uint(this.i6) >= uint(this.i2))
               {
                  this.i0 = this.i2;
               }
               else
               {
                  this.i0 += 12;
                  this.i2 = this.i5;
                  while(true)
                  {
                     this.f0 = lf64(this.i2 + 12);
                     sf64(this.f0,this.i2);
                     this.i5 = li32(this.i2 + 20);
                     si32(this.i5,this.i2 + 8);
                     this.i2 = li32(this.i4);
                     this.i5 = this.i0 + 12;
                     this.i6 = this.i0;
                     if(uint(this.i5) >= uint(this.i2))
                     {
                        break;
                     }
                     this.i0 = this.i5;
                     this.i2 = this.i6;
                  }
                  this.i0 = this.i2;
               }
               this.i0 += -12;
               si32(this.i0,this.i4);
               this.i0 = li32(this.i7);
               this.i2 = li32(this.i0 + 68);
               this.i0 = li32(this.i0 + 64);
               if(uint(this.i2) >= uint(this.i0))
               {
                  mstate.esp -= 4;
                  si32(this.i1,mstate.esp);
                  state = 33;
                  mstate.esp -= 4;
                  FSM_luaC_step.start();
                  return;
               }
               break;
            case 33:
               mstate.esp += 4;
               break;
            case 34:
               mstate.esp += 12;
               this.i0 = li32(this.i4);
               this.i0 += -12;
               si32(this.i0,this.i4);
               mstate.esp -= 4;
               si32(this.i1,mstate.esp);
               state = 35;
               mstate.esp -= 4;
               FSM_luaG_errormsg.start();
               return;
            case 35:
               mstate.esp += 4;
               §§goto(addr2555);
            default:
               throw "Invalid state in _as3_new";
         }
         this.i0 = 2;
         this.i2 = li32(this.i4);
         this.i3 = li32(this.i3);
         this.i2 -= this.i3;
         this.i2 /= 12;
         mstate.esp -= 12;
         this.i2 += -1;
         si32(this.i1,mstate.esp);
         si32(this.i0,mstate.esp + 4);
         si32(this.i2,mstate.esp + 8);
         state = 34;
         mstate.esp -= 4;
         FSM_luaV_concat.start();
      }
   }
}