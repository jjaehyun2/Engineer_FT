/*
 * VERSION:3.0
 * DATE:2014-10-15
 * ACTIONSCRIPT VERSION: 3.0
 * UPDATES AND DOCUMENTATION AT: http://www.wdmir.net 
 * MAIL:mir3@163.com
 */
package com.adobe.ac.mxeffects
{
	import flash.geom.Matrix;
	
	public class Triangle
	{
		public var p0 : SandyPoint;
		public var p1 : SandyPoint;
		public var p2 : SandyPoint;
		public var tMat : Matrix;
		
		public function Triangle( p0 : SandyPoint, p1 : SandyPoint, p2 : SandyPoint, tMat : Matrix )
		{
			this.p0 = p0;
			this.p1 = p1
			this.p2 = p2;
			this.tMat = tMat;			
		}
	}
}