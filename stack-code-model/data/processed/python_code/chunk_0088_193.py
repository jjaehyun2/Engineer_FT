package utils.compression.as3zlib
{
	
	
	import java.io.*;
	
	
	public class ZOutputStream extends OutputStream {
	
	  protected var z:ZStream=new ZStream();
	  protected var bufsize:int=512;
	  protected var flush:int=JZlib.Z_NO_FLUSH;
	  protected var buf:Array=new byte[bufsize], buf1=new byte[1];
	  protected var compress:Boolean;
	  protected var out:OutputStream;



	
	  public function ZOutputStream(out:OutputStream) {
	    super();
	    this.out=out;
	    z.inflateInit();
	    compress=false;
	  }




	
	  public function ZOutputStream(out:OutputStream, level:int) {
	    this(out, level, false);
	  }
	  
	  
	  
	  
	  
	  public function ZOutputStream(out:OutputStream, level:int, nowrap:Boolean) {
	    super();
	    this.out=out;
	    z.deflateInit(level, nowrap);
	    compress=true;
	  }
	
	
	
	
	
	  public function write(b:int):void throws IOException {
	    buf1[0]=byte(b);
	    write(buf1, 0, 1);
	  }
	
	
	
	
	
	
	  public function write(byte b[], off:int, len:int):void throws IOException {
	    if(len==0)
	      return;
	    var err:int;
	    z.next_in=b;
	    z.next_in_index=off;
	    z.avail_in=len;
	    do{
	      z.next_out=buf;
	      z.next_out_index=0;
	      z.avail_out=bufsize;
	      if(compress)
	        err=z.deflate(flush);
	      else
	        err=z.inflate(flush);
	      if(err!=JZlib.Z_OK)
	        throw new ZStreamException((compress?"de":"in")+"flating: "+z.msg);
	      out.write(buf, 0, bufsize-z.avail_out);
	    } 
	    while(z.avail_in>0|| z.avail_out==0);
	  }
	
	
	
	
	
	  public function getFlushMode():int {
	    return(flush);
	  }
	
	
	
	
	
	  public function setFlushMode(flush:int):void {
	    this.flush=flush;
	  }
	
	
	
	
	
	  public function finish():void throws IOException {
	    var err:int;
	    do{
	      z.next_out=buf;
	      z.next_out_index=0;
	      z.avail_out=bufsize;
	      if(compress){ err=z.deflate(JZlib.Z_FINISH);  }
	      else{ err=z.inflate(JZlib.Z_FINISH); }
	      if(err!=JZlib.Z_STREAM_END && err != JZlib.Z_OK)
	      throw new ZStreamException((compress?"de":"in")+"flating: "+z.msg);
	      if(bufsize-z.avail_out>0){
		out.write(buf, 0, bufsize-z.avail_out);
	      }
	    }
	    while(z.avail_in>0|| z.avail_out==0);
	    flush();
	  }
	  
	  
	  
	  
	  public function end():void {
	    if(z==null)
	      return;
	    if(compress){ z.deflateEnd(); }
	    else{ z.inflateEnd(); }
	    z.free();
	    z=null;
	  }
	  
	  
	  
	  
	  
	  public function close():void throws IOException {
	    try{
	      try{finish();}
	      catch (var ignored:IOException) {}
	    }
	    finally{
	      end();
	      out.close();
	      out=null;
	    }
	  }
	
	
	
	
	  /**
	   * Returns the total number of bytes input so far.
	   */
	   
	  public function getTotalIn():Number {
	    return z.total_in;
	  }
	
	
	
	
	
	  /**
	   * Returns the total number of bytes output so far.
	   */
	   
	  public function getTotalOut():Number {
	    return z.total_out;
	  }
	
	
	
	
	
	
	  public function flush():void throws IOException {
	    out.flush();
	  }
	
	}
}