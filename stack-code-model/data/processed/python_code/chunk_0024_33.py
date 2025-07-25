package com.hurlant.crypto.symmetric
{
   import flash.utils.ByteArray;
   
   public class CTRMode extends IVMode implements IMode
   {
       
      
      public function CTRMode(key:ISymmetricKey, padding:IPad = null)
      {
         super(key,padding);
      }
      
      public function encrypt(src:ByteArray) : void
      {
         padding.pad(src);
         var vector:ByteArray = getIV4e();
         this.core(src,vector);
      }
      
      public function decrypt(src:ByteArray) : void
      {
         var vector:ByteArray = getIV4d();
         this.core(src,vector);
         padding.unpad(src);
      }
      
      private function core(src:ByteArray, iv:ByteArray) : void
      {
         var j:uint = 0;
         var X:ByteArray = new ByteArray();
         var Xenc:ByteArray = new ByteArray();
         X.writeBytes(iv);
         for(var i:uint = 0; i < src.length; i += blockSize)
         {
            Xenc.position = 0;
            Xenc.writeBytes(X);
            key.encrypt(Xenc);
            for(j = 0; j < blockSize; j++)
            {
               src[i + j] ^= Xenc[j];
            }
            for(j = blockSize - 1; j >= 0; j--)
            {
               ++X[j];
               if(X[j] != 0)
               {
                  break;
               }
            }
         }
      }
      
      public function toString() : String
      {
         return key.toString() + "-ctr";
      }
   }
}