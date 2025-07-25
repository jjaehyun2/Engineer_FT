package cmodule.lua_wrapper
{
   import avm2.intrinsics.memory.li32;
   import avm2.intrinsics.memory.si32;
   
   public final class FSM_lua_checkstack extends Machine
   {
      
      public static const intRegCount:int = 6;
      
      public static const NumberRegCount:int = 0;
       
      
      public var i0:int;
      
      public var i1:int;
      
      public var i2:int;
      
      public var i3:int;
      
      public var i4:int;
      
      public var i5:int;
      
      public function FSM_lua_checkstack()
      {
         super();
      }
      
      public static function start() : void
      {
         var _loc1_:FSM_lua_checkstack = null;
         _loc1_ = new FSM_lua_checkstack();
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
               this.i0 = li32(mstate.ebp + 8);
               this.i1 = li32(mstate.ebp + 12);
               if(this.i1 < 8001)
               {
                  this.i2 = li32(this.i0 + 8);
                  this.i3 = li32(this.i0 + 12);
                  this.i3 = this.i2 - this.i3;
                  this.i4 = this.i0 + 8;
                  this.i3 /= 12;
                  this.i3 += this.i1;
                  if(this.i3 <= 8000)
                  {
                     if(this.i1 > 0)
                     {
                        this.i3 = li32(this.i0 + 28);
                        this.i5 = this.i1 * 12;
                        this.i2 = this.i3 - this.i2;
                        if(this.i2 <= this.i5)
                        {
                           this.i2 = li32(this.i0 + 44);
                           if(this.i2 >= this.i1)
                           {
                              mstate.esp -= 8;
                              this.i2 <<= 1;
                              si32(this.i0,mstate.esp);
                              si32(this.i2,mstate.esp + 4);
                              state = 1;
                              mstate.esp -= 4;
                              FSM_luaD_reallocstack.start();
                              return;
                           }
                           mstate.esp -= 8;
                           this.i2 += this.i1;
                           si32(this.i0,mstate.esp);
                           si32(this.i2,mstate.esp + 4);
                           state = 2;
                           mstate.esp -= 4;
                           FSM_luaD_reallocstack.start();
                           return;
                        }
                        break;
                     }
                     addr110:
                     this.i0 = 1;
                  }
                  else
                  {
                     addr47:
                     this.i0 = 0;
                  }
                  mstate.eax = this.i0;
                  §§goto(addr302);
               }
               §§goto(addr47);
            case 1:
               mstate.esp += 8;
               break;
            case 2:
               mstate.esp += 8;
               break;
            default:
               throw "Invalid state in _lua_checkstack";
         }
         this.i0 = li32(this.i0 + 20);
         this.i2 = li32(this.i0 + 8);
         this.i3 = li32(this.i4);
         this.i1 *= 12;
         this.i1 = this.i3 + this.i1;
         this.i0 += 8;
         if(uint(this.i2) < uint(this.i1))
         {
            this.i2 = 1;
            si32(this.i1,this.i0);
            mstate.eax = this.i2;
         }
         else
         {
            §§goto(addr110);
         }
         addr302:
         mstate.esp = mstate.ebp;
         mstate.ebp = li32(mstate.esp);
         mstate.esp += 4;
         mstate.esp += 4;
         mstate.gworker = caller;
      }
   }
}