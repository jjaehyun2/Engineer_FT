package utils.compression.as3zlib {
	
	import flash.utils.ByteArray;
	
	public final class Adler32 {
	
		// largest prime smaller than 65536
		static private var BASE:int=65521; 
		// NMAX is the largest n such that 255n(n+1)/2 + (n+1)(BASE-1) <= 2^32-1
		static private var NMAX:int=5552;
	
		public function adler32(adler:Number, buf:ByteArray, index:int, len:int):Number {
			if (buf == null) {
				return 1;
			}
	
			var s1:Number=adler & 0xffff;
			var s2:Number=(adler>>16) & 0xffff;
			var k:int;
	
			while(len > 0) {
				k=len<NMAX?len:NMAX;
				len-=k;
				
				while(k>=16) {
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					s1+=buf[index++]&0xff; s2+=s1;
					k-=16;
					
				}
				
				if (k!=0) {
					do {
						s1+=buf[index++]&0xff;
						s2+=s1;
					} while(--k!=0);
				}
				s1%=BASE;
				s2%=BASE;
			}
			return (s2<<16)|s1;
		}
	}
}