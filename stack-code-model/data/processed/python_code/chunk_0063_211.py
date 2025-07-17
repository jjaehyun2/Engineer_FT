package org.aswing.util
{
	import starling.display.Sprite;
	import starling.display.DisplayObject;
	import starling.display.DisplayObjectContainer;
	
	/*
	   Copyright aswing.org, see the LICENCE.txt.
	 */
	
	/**
	 * DepthManager to manage the depth of mcs created by AS.
	 *
	 * <p>This Manager can not manage the mcs created by FlashIDE.
	 *
	 * @author iiley
	 */
	public class DepthManager
	{
		public static var MAX_DEPTH:Number = 1048575;
		public static var MIN_DEPTH:Number = 0;
		
		/**
		 * bringToBottom(mc:MovieClip, exceptMC:MovieClip)<br>
		 * bringToBottom(mc:MovieClip)
		 * <p>
		 * Bring the mc to all brother mcs' bottom.
		 * <p>
		 * if exceptMC is undefined or null, the mc will be sent to bottom of all.
		 * else, the mc will be sent to the bottom of all but above the exceptMC.
		 * If you use a exceptMC, make sure the exceptMC is always at the bottom of all mcs, unless, this
		 * method maybe weird(may throw Errors).
		 * @param mc the mc to be set to bottom
		 * @param exceptMC the exceptMC of bottom mc.
		 * @see #isBottom()
		 * @throws Error when the exceptMC is not at the bottom currently.
		 */
		public static function bringToBottom(mc:DisplayObjectContainer, exceptMC:DisplayObjectContainer):void
		{
			var parent:DisplayObjectContainer = mc.parent;
			if (parent == null)
				return;
			if (mc.parent.getChildIndex(mc) == MIN_DEPTH)
				return;
			
			var minDepth:Number = (exceptMC == null ? MIN_DEPTH : exceptMC.parent.getChildIndex(exceptMC) + 1);
			
			//if(parent.getInstanceAtDepth(minDepth) == undefined){
			if (parent.getChildAt(minDepth) == null)
			{
				//mc.swapDepths(minDepth);
				mc.parent.setChildIndex(mc, minDepth);
				return;
			}
			
			var mcs:Array = createMCSequenced(parent);
			if (mc == mcs[0])
				return;
			if (mc == mcs[1] && exceptMC == mcs[0])
				return;
			
			if (exceptMC != mcs[0])
			{
				trace("The exceptMC is not at the bottom currently!");
				throw new Error("The exceptMC is not at the bottom currently!");
			}
			
			var swapMC:DisplayObjectContainer = mc;
			for (var i:Number = 1; mcs[i] != mc; i++)
			{
				//swapMC.swapDepths(mcs[i]);
				swapMC.parent.swapChildren(swapMC, mcs[i]);
				mc.parent.setChildIndex(mc, minDepth);
				swapMC = mcs[i];
			}
		}
		
		/**
		 * Bring the mc to all brother mcs' top.
		 */
		public static function bringToTop(mc:DisplayObject):void
		{
			var parent:DisplayObjectContainer = mc.parent;
			if (parent == null)
				return;
			//var depth:Number = parent.getNextHighestDepth();
			var depth:Number = parent.numChildren - 1;
			//if(mc.getDepth() == (depth - 1)) return;
			if (mc.parent.getChildIndex(mc) == (depth - 1))
				return;
			if (depth < MAX_DEPTH)
			{
				//mc.swapDepths(depth);
				mc.parent.setChildIndex(mc, depth);
				return;
			}
			
			var mcs:Array = createMCSequenced(parent);
			if (mc == mcs[0])
				return;
			
			var swapMC:DisplayObject = mc;
			for (var i:Number = mcs.length - 1; mcs[i] != mc; i--)
			{
				//swapMC.swapDepths(mcs[i]);
				swapMC.parent.swapChildren(swapMC, mcs[i]);
				swapMC = mcs[i];
			}
		}
		
		/**
		 * Returns is the mc is on the top depths in DepthManager's valid depths.
		 * Valid depths is that depths from MIN_DEPTH to MAX_DEPTH.
		 */
		public static function isTop(mc:DisplayObjectContainer):Boolean
		{
			var parent:DisplayObjectContainer = mc.parent;
			if (parent == null)
				return true;
			//var depth:Number = parent.getNextHighestDepth();
			var depth:Number = parent.numChildren;
			return mc.parent.getChildIndex(mc) == (depth - 1);
		}
		
		/**
		 * isBottom(mc:MovieClip, exceptMC:MovieClip)<br>
		 * isBottom(mc:MovieClip)
		 * <p>
		 * Returns is the mc is at the bottom depths in DepthManager's valid depths.
		 * Valid depths is that depths from MIN_DEPTH to MAX_DEPTH.
		 * <p>
		 * if exceptMC is undefined or null, judge is the mc is at bottom of all.
		 * else, the mc judge is the mc is at bottom of all except the exceptMC.
		 * @param mc the mc to be set to bottom
		 * @param exceptMC the exceptMC of bottom mc.
		 * @return is the mc is at the bottom
		 */
		public static function isBottom(mc:DisplayObject, exceptMC:DisplayObject):Boolean
		{
			var parent:DisplayObjectContainer = mc.parent;
			if (parent == null)
				return true;
			var depth:Number = mc.parent.getChildIndex(mc);
			if (depth == MIN_DEPTH)
			{
				return true;
			}
			for (var i:Number = MIN_DEPTH; i < depth; i++)
			{
				//var mcAtDepth:DisplayObject = parent.getInstanceAtDepth(i);
				var mcAtDepth:DisplayObject = parent.getChildAt(i);
				if (mcAtDepth != null && mcAtDepth != exceptMC)
				{
					return false;
				}
			}
			return true;
		}
		
		/**
		 * Return if mc is just first bebow the aboveMC.
		 * if them don't have the same parent, whatever depth they has just return false.
		 */
		public static function isJustBelow(mc:DisplayObject, aboveMC:DisplayObject):Boolean
		{
			var parent:DisplayObjectContainer = mc.parent;
			if (parent == null)
				return false;
			if (aboveMC.parent != parent)
				return false;
			
			if (mc.parent.getChildIndex(mc) >= aboveMC.parent.getChildIndex(aboveMC))
			{
				return false;
			}
			else
			{
				for (var i:Number = aboveMC.parent.getChildIndex(aboveMC) - 1; i >= MIN_DEPTH; i--)
				{
					//var t:MovieClip = parent.getInstanceAtDepth(i);
					var t:DisplayObject = parent.getChildAt(i);
					if (t != null)
					{
						if (t == mc)
						{
							return true;
						}
						else
						{
							return false;
						}
					}
				}
			}
			return false;
		}
		
		/**
		 * Returns if mc is just first above the belowMC.
		 * if them don't have the same parent, whatever depth they has just return false.
		 * @see #isJustBelow
		 */
		public static function isJustAbove(mc:DisplayObjectContainer, belowMC:DisplayObjectContainer):Boolean
		{
			return isJustBelow(belowMC, mc);
		}
		
		/**
		 * Calculates and returns the correct value to use for the new depth
		 * @param mc the parent mc which need to calculates the next available depth
		 * @return the next available depth
		 */
		public static function getNextAvailableDepth(mc:DisplayObjectContainer):Number
		{
			//var depth:Number = mc.getNextHighestDepth();
			var depth:Number = mc.parent.numChildren;
			if (depth >= MIN_DEPTH && depth < MAX_DEPTH)
			{
				return depth;
			}
			else
			{
				for (var i:Number = 0; i < MAX_DEPTH; i++)
				{
					//if(mc.getInstanceAtDepth(i) == undefined){
					if (mc.getChildIndex(mc) == -1)
					{
						return i;
					}
				}
			}
			trace("Warnning : There is no any available depth in " + mc);
			return -1;
		}
		
		/**
		 * Create a sequence contains all mcs sorted by their depth.
		 */
		public static function createMCSequenced(parent:DisplayObjectContainer):Array
		{
			var mcs:Array = new Array();
			for (var i:String in parent)
			{
				if (parent[i] is Sprite)
				{
					mcs.push(parent[i]);
				}
			}
			mcs.sort(depthComparator);
			return mcs;
		}
		
		private static function depthComparator(a:DisplayObjectContainer, b:DisplayObjectContainer):Number
		{
			if (a.parent.getChildIndex(a) > b.parent.getChildIndex(b))
			{
				return -1;
			}
			else
			{
				return 1;
			}
		}
	}
}