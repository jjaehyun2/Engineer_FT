/**
 * Cyclops Framework
 * 
 * Copyright 2010 Mark Davis Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 * http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.cyclopsframework.actions.animation
{
	import org.cyclopsframework.core.CFAction;
	import org.cyclopsframework.utils.math.CFMath;
	import org.cyclopsframework.utils.misc.CFUtils;
	
	import flash.display.DisplayObject;
	import flash.geom.Point;
	
	public class CFTranslate extends CFAction
	{
		public static const TAG:String = "@CFTranslate";
		
		private var _dynamicTarget:Object = null;
		private var _p1:Point;
		private var _p2:Point;
		
		public function CFTranslate(
			target:Object,
			x1:Number,
			y1:Number,
			x2:Number,
			y2:Number,
			period:Number=0,
			cycles:Number=1,
			bias:Function=null)
		{
			super(period, cycles, bias, [TAG]);
			
			CFUtils.validate(target, "CFTranslate target", ["x", "y"]);
						
			_dynamicTarget = target;
			_p1 = new Point(x1, y1);
			_p2 = new Point(x2, y2);
		}
		
		protected override function onFrame(t:Number):void
		{
			CFMath.lerpTarget2(_dynamicTarget, _p1, _p2, t);
		}
	}
}