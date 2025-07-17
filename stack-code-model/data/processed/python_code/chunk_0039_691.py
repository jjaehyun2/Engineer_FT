package flash.display3D
{
   import flash.utils.ByteArray;
   
   public final class IndexBuffer3D extends Object
   {
       public var count:int;
	   public var buff:WebGLBuffer;
	   public var gl:WebGLRenderingContext;
      public function IndexBuffer3D()
      {
         super();
      }
      
	  /**
		 * @flexjsignorecoercion Object
		 */
     public function uploadFromVector(data:Vector.<uint>, startOffset:int, count:int) : void{
		gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, buff);
		gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(data as Object), gl.STATIC_DRAW);	
	 }
      
     public function uploadFromByteArray(data:ByteArray, byteArrayOffset:int, startOffset:int, count:int) : void{}
      
     public function dispose() : void{
		 gl.deleteBuffer(buff);
		 buff=null
	 }
   }
}