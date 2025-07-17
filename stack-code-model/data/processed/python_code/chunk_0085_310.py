/**
* @author gyb 20141031
*/
package as3lib.helper.math
{
	import flash.geom.Point;

	/**
	 * 功能：flex几何学工具类
	 */
	public  class GeomHelper
	{
		//===============================================属性=========================================
		public static const Circle:String = "Circle";
		public static const Rectangle:String = "Rectangle";
		public static const Polygon:String = "Polygon";
		public static const Line:String = "Line";
		
		public static var Instance:GeomHelper = new GeomHelper();
		//===============================================方法=========================================
		/**
		 *判断一个点是否在圆内 
		 * @param centerPoint
		 * @param borderPoint
		 * @param point 
		 * @return 
		 */
		public function pointInCircle(point:Point,centerPoint:Point, borderPoint:Point):Boolean
		{
			var flag:Boolean=false;
			var radius:Number = Point.distance(centerPoint, borderPoint);	
			Point.distance(centerPoint,point) <= radius ? (flag= true) : null;
			return flag;
		}
		/**
		 *判断多个点是否在圆内(通常用于判断线段和面上的点)
		 * @param centerPoint
		 * @param borderPoint
		 * @param points 
		 * @return 
		 */
		public function pointsInCircle(points:Vector.<Point>,centerPoint:Point, borderPoint:Point):Boolean
		{
			var flag:Boolean=false;
			for each(var point:Point in points)
			{
				flag = pointInCircle(point,centerPoint,borderPoint);
				if(flag == true) break;
			}
			return flag;
		}
		/**
		 * 相交：单线段与圆
		 **/
		public function lineIntersectCircle(pointA:Point, pointB:Point,centerPoint:Point, borderPoint:Point):Boolean
		{
			var dis:Number=PointToSegDist(centerPoint,pointA,pointB)
			var radius:Number=Math.sqrt((centerPoint.x-borderPoint.x)*(centerPoint.x-borderPoint.x)+(centerPoint.y-borderPoint.y)*(centerPoint.y-borderPoint.y))
			if(dis>radius)
			{
				return false;
			}else
			{
				return true;
			}
		}
		/**
		 * 相交：多线段与圆
		 **/
		public function linesIntersectCircle(lines:Vector.<Point>,centerPoint:Point, borderPoint:Point):Boolean
		{
			var flag:Boolean=false;
			for (var i:int = 0;i < lines.length-1;i++)
			{
				flag = lineIntersectCircle(lines[i],lines[i+1],centerPoint,borderPoint);
				if(flag == true) break;
			}
			return flag;
		}
		/**
		 * 点到线段最短距离
		 **/
		public function PointToSegDist( point:Point,  pointA:Point,  pointB:Point):Number
		{
			
			var cross:Number = (pointB.x - pointA.x) * (point.x - pointA.x) + (pointB.y - pointA.y) * (point.y - pointA.y); 
			if (cross <= 0) return Math.sqrt((point.x - pointA.x) * (point.x - pointA.x) + (point.y - pointA.y) * (point.y - pointA.y));
			
			var d2:Number = (pointB.x - pointA.x) * (pointB.x - pointA.x) + (pointB.y - pointA.y) * (pointB.y - pointA.y);
			if (cross >= d2) return Math.sqrt((point.x - pointB.x) * (point.x - pointB.x) + (point.y - pointB.y) * (point.y - pointB.y));
			
			var r:Number = cross / d2;
			var px:Number = pointA.x + (pointB.x - pointA.x) * r;
			var py:Number = pointA.y + (pointB.y - pointA.y) * r;
			return Math.sqrt((point.x - px) * (point.x - px) + (py - point.y) * (py - point.y));
			
		}
		
		/**
		 *判断点是否在矩形内 
		 * @param point
		 * @param bottomLeft
		 * @param topRight
		 * @return 
		 */
		public function pointInRect(point:Point,bottomLeft:Point, topRight:Point):Boolean
		{
			var flag:Boolean=false;
			if (bottomLeft.x <= point.x && point.x <= topRight.x && bottomLeft.y <= point.y && point.y <= topRight.y)
			{
				flag=true;
			}
			return flag;	
		}
		/**
		 *判断多个点是否在矩形内 (通常用于判断线段和面上的点)
		 * @param point
		 * @param bottomLeft
		 * @param topRight
		 * @return 
		 */
		public function pointsInRect(points:Vector.<Point>,bottomLeft:Point, topRight:Point):Boolean
		{
			var flag:Boolean=false;
			for each(var point:Point in points)
			{
				flag = pointInRect(point,bottomLeft,topRight);
				if(flag == true) break;
			}
			return flag;
		}
		/**
		 *相交：单线段与矩形
		 */
		public function lineIntersectRect(L_start:Point,L_end:Point,R_start:Point,R_end:Point):Boolean
		{
			var R_SE:Point=new Point(R_start.x,R_end.y);
			var R_ES:Point=new Point(R_end.x,R_start.y);
			
			if(lineIntersectLine(L_start,L_end,R_start,R_SE))
			{
				return true;
			}
			if(lineIntersectLine(L_start,L_end,R_start,R_ES))
			{
				return true;
			}
			if(lineIntersectLine(L_start,L_end,R_end,R_SE))
			{
				return true;
			}
			if(lineIntersectLine(L_start,L_end,R_start,R_ES))
			{
				return true;
			}
			
			return false;
		}

		/**
		 *相交：多线段与矩形
		 */
		public function linesIntersectRect(lines:Vector.<Point>,bottomLeft:Point, topRight:Point):Boolean
		{
			var flag:Boolean=false;
			for (var i:int = 0;i < lines.length-1;i++)
			{
				flag = lineIntersectRect(lines[i],lines[i+1],bottomLeft,topRight);
				if(flag == true) break;
			}
			return flag;
		}
		
		/**
		 * 判断单个点是否在多边形中,射线算法
		 * @param p Point对象
		 * @param polygonArr  多边形顶点数组
		 * @return 
		 */
		public function pointInPolygon(p:Point,polygonArr:Vector.<Point>):Boolean
		{	
			var nCross:int = 0;
			if(polygonArr.length>0)
			{
				for (var  i:int = 0;i < polygonArr.length;i++) 
				{ 
					var p0:Point = p;
					var p1:Point = polygonArr[i];			
					var p2:Point = polygonArr[(i + 1) % polygonArr.length];			
					
					// 求解 y=p.y 与 p1p2 的交点
					if ( p1.y == p2.y ) // p1p2 与 y=p0.y平行 
						continue;
					if ( p0.y < (p1.y <= p2.y ? p1.y:p2.y)) // 交点在p1p2延长线上 
						continue; 
					if ( p0.y >= (p1.y>= p2.y ? p1.y:p2.y)) // 交点在p1p2延长线上 
						continue;
					// 求交点的 X 坐标 -------------------------------------------------------------- 
					var x:Number = (Number)(p0.y - p1.y) * (Number)(p2.x - p1.x) / (Number)(p2.y - p1.y) + p1.x;
					if ( x > p0.x ) 
						nCross++; // 只统计单边交点 			
				}	
			}
			// 单边交点为偶数，点在多边形之外 --- 
			return (nCross % 2 == 1); 
		}
		
		/**
		 * 判断多个点是否在多边形中,射线算法
		 * @param p Point对象
		 * @param polygonArr  多边形顶点数组
		 * @return 
		 */
		public function pointsInPolygon(points:Vector.<Point>,polygonArr:Vector.<Point>):Boolean
		{
			var flag:Boolean=false;
			for each(var point:Point in points)
			{
				flag = pointInPolygon(point,polygonArr);
				if(flag == true) break;
			}
			return flag;
		}
		/**
		 * 相交:线段与多边形
		 * @return 
		 **/
		public function lineIntersectPolygon(L_start:Point,L_end:Point,polygonArr:Vector.<Point>):Boolean
		{
			if(polygonArr.length>0)
			{
				for (var  i:int = 0;i < polygonArr.length;i++) 
				{ 
					var P_S:Point = polygonArr[i]
					var P_E:Point = polygonArr[(i + 1) % polygonArr.length]
					if(lineIntersectLine(L_start,L_end,P_S,P_E)==true)
					{
						return true;
					}
				}
			}
			return false;
		}
		/**
		 *相交：多线段与多边形
		 */
		public function linesIntersectPolygon(lines:Vector.<Point>,polygonArr:Vector.<Point>):Boolean
		{
			var flag:Boolean=false;
			for (var i:int = 0;i < lines.length-1;i++)
			{
				flag = lineIntersectPolygon(lines[i],lines[i+1],polygonArr);
				if(flag == true) break;
			}
			return flag;
		}
		/**
		 * 线段相交
		 * @return 
		 * @param aa, bb为一条线段两端点 cc, dd为另一条线段的两端点 相交返回true, 不相交返回false
		 **/
		public function lineIntersectLine( A:Point,  B:Point,  C:Point,  D:Point):Boolean
		{
			if ( Math.max(A.x, B.x)<Math.min(C.x, D.x) )
			{
				return false;
			}
			if ( Math.max(A.y, B.y)<Math.min(C.y, D.y) )
			{
				return false;
			}
			if ( Math.max(C.x, D.x)<Math.min(A.x, B.x) )
			{
				return false;
			}
			if ( Math.max(C.y, D.y)<Math.min(A.y, B.y) )
			{
				return false;
			}
			if ( mult(C, B, A)*mult(B, D, A)<0 )
			{
				return false;
			}
			if ( mult(A, D, C)*mult(D, B, C)<0 )
			{
				return false;
			}
			return true;
			
			//叉积
			function mult( a:Point,  b:Point,  c:Point):Number
			{
				return (a.x-c.x)*(b.y-c.y)-(b.x-c.x)*(a.y-c.y);
			}
		}
		/**
		 *相交：多线段与多线段
		 */
		public function linesIntersectLines(linesA:Vector.<Point>,linesB:Vector.<Point>):Boolean
		{
			for (var i:int = 0;i < linesA.length-1;i++)
			{
				for (var j:int = 0;j < linesB.length-1;j++)
				{
					var flag:Boolean = lineIntersectLine(linesA[i],linesA[i+1],linesB[j],linesB[j+1]);
					if(flag == true) return true;
				}
			}
			return false;
		}
		/**
		 * 获取相交点
		 * @return 
		 */
		public function getIntersectPoint(l_start:Point,l_end:Point,p_start:Point,p_end:Point):Point
		{	
			var point:Point = new Point();
			
			var y1:Number = (l_start.y-l_end.y);
			var x1:Number = (l_start.x-l_end.x);
			var k1:Number = y1/x1;
			
			var y2:Number = (p_start.y-p_end.y);
			var x2:Number = (p_start.x-p_end.x);
			var k2:Number = y2/x2;
			
			var b1:Number = l_start.y-l_start.x*k1;
			var b2:Number = p_start.y-p_start.x*k2;
			
			point.x=(b2-b1)/(k1-k2);
			point.y=k1*point.x+b1;
			if(y1==0 && x2==0)
			{
				point.x=p_start.x;
				point.y=l_start.y;
			}else if(x1==0&&y2==0)
			{
				point.x=l_start.x;
				point.y=p_start.y;
			}else if(x1==0)
			{
				point.x=l_start.x;
				point.y=k2*point.x+b2;
			}else if(x2==0)
			{
				point.x=p_start.x;
				point.y=k1*point.x+b1;
			}
			return point;
		}
		
		public function getGeometryCenter(points:Vector.<Point>):Point
		{
			var X:Number=0;
			var Y:Number=0;
			
			points.forEach(function(item:*, index:int, array:Array):void{
				if(index!=array.length-1)
				{
					X=(X*index+item.x)/(index+1);//平均值计算获取数据中心点
					Y=(Y*index+item.y)/(index+1);
				}
			},null);
			return new Point(X,Y);
		}
		
	}
}