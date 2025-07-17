/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package math.testcases
{
	import flash.geom.Point;
	
	import matcher.CloseToPointMatcher;
	
	import net.digitalprimates.math.Circle;
	
	import org.flexunit.assertThat;
	import org.hamcrest.object.equalTo;

	[RunWith("org.flexunit.runners.Parameterized")]
	public class GetPointsTest
	{		
		private static const TOLERANCE:Number = .0001;
		
		[Parameters]
		public static var data:Array = [
			[ new Circle( new Point( 0, 0 ), 5 ), new Point( 5, 0 ), 0 ],
			[ new Circle( new Point( 0, 0 ), 5 ), new Point( -5, 0 ), Math.PI ] ];
		
		private var circle:Circle;
		private var point:Point;
		private var radians:Number;
		
		[Test]
		public function shouldGetPointsOnCircle():void {
			assertThat( circle.getPointOnCircle( radians ), new CloseToPointMatcher( point, TOLERANCE ) );
		}
		
		[Test]
		public function shouldReturnDistanceEqualToRadius():void {
			var distance:Number = Point.distance( circle.getPointOnCircle( radians ), circle.origin );
			
			assertThat( distance, equalTo( circle.radius ) );
		}
		
		public function GetPointsTest( circle:Circle, point:Point, 
									   radians:Number )
		{
			this.circle = circle;
			this.point = point;
			this.radians = radians;
		}
	}
}