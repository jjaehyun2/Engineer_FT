package
{
   import flash.utils.ByteArray;
   
   public dynamic class §\x1e\x16§ extends ByteArray
   {
       
      
      var a1:uint = 17;
      
      var a2:uint = 34;
      
      var a3:uint = 51;
      
      var a4:uint = 68;
      
      var a5:uint = 85;
      
      var a6:uint = 102;
      
      var a7:uint = 119;
      
      var a8:uint = 136;
      
      var a9:uint = 153;
      
      var a10:uint = 170;
      
      var a11:uint = 187;
      
      var a12:Object;
      
      var a13:Object;
      
      public function §\x1e\x16§()
      {
         super();
         this.a12 = this;
      }
      
      public function flash25() : Object
      {
         var _loc_:Object = this.flash27(this.a13 as Number);
         return _loc_;
      }
      
      public function flash26(param1:int, parm2:Object) : void
      {
         this["a" + param1++] = parm2.low;
         this["a" + param1] = parm2.hi;
      }
      
      public function flash27(param1:Number) : Object
      {
         this.position = 0;
         this.writeDouble(param1);
         if(false)
         {
            return;
         }
         this.position = 0;
         return {
            "hi":this.readUnsignedInt(),
            "low":this.readUnsignedInt()
         };
      }
   }
}