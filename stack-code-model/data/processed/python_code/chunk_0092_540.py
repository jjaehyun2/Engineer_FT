package net.darkglass.FlxFrob
{
	import flash.utils.Dictionary;
	import org.flixel.FlxBasic;
	import flash.utils.getTimer;
	import org.flixel.FlxG;
	
	/**
	 * <p>Simple time-based profiler for Flixel-based projects</p>
	 * 
	 * @author greysondn
	 */
	public class FlxProfiler extends FlxBasic 
	{
		/**
		 * Whether to even enable profiling in the first place
		 */
		public static var enabled:Boolean = true;
		
		/**
		 * Record of data for entries. Yep.
		 */
		public static var record:Array = [];
		
		/**
		 * Record of call stacks. Yep.
		 */
		public static var callRecord:Array = [];
		
		/**
		 * callstack of entries. Yep.
		 */
		public static var callStack:Array = [];
		
		/**
		 * time stack for entries. Yep.
		 */
		public static var timeStack:Array = [];
		
		/**
		 * Lookup table for record locations.
		 */
		public static var lookupTable:Dictionary = new Dictionary();
		
		/**
		 * and call locations
		 */
		public static var callLookupTable:Dictionary = new Dictionary();
		
		/**
		 * total time in all records
		 */
		public static var totalTime:uint = 0;
		
		/**
		 * total call count
		 */
		public static var totalCalls:uint = 0;
		
		/**
		 * private static var
		 */
		private static var currentCall:String = "";
		
		/**
		 * Start time, in milliseconds relative to flash player start
		 */
		public var startTime:int;
		
		/**
		 * entry's key - it's name
		 */
		public var key:String;
		
		public function FlxProfiler(entryName:String)
		{
			FlxG.log("FP deprec: " + entryName);
			trace("FP deprec: " + entryName);
			
			if (enabled)
			{
				startTime = getTimer();
				add(entryName);
				key = entryName;
			}
		}
		
		override public function destroy():void 
		{
			if (enabled)
			{
				// time it took on the clock
				var time:uint = getTimer() - startTime;
				
				// entry's entries
				record[lookupTable[key]].time  += time;
				record[lookupTable[key]].count += 1;
				
				// static entries
				totalTime += time;
				totalCalls += 1;
			}
			
			super.destroy();
		}
		
		public static function enter(entryName:String):void
		{	
			// push stats onto stacks
			callStack.push(entryName);
			timeStack.push(getTimer());
			
			// and string stack
			currentCall = currentCall.concat(entryName + " > ");
			
			// add to dictionary
			add(entryName);
			
			// add callstack to dictionary
			addCallStack(currentCall);
			
			// trace length of stacks
			// trace(callStackToString());
			// trace("callstac: " + callStack.length);
			// trace("timestac: " + timeStack.length);
			// trace("---");
		}
		
		public static function exit():void
		{
			// start by popping the time
			var _time:uint = getTimer() - timeStack.pop();
				
			// figure out your two keys
			// var _stackKey:String = callStackToString();
			var _key:String = callStack.pop();
			
			// um
			// trace("exit: " + _stackKey);
			// add to the counts
			
			// bare calls
			record[lookupTable[_key]].time  += _time;
			record[lookupTable[_key]].count += 1;
			
			// stackCalls
			callRecord[callLookupTable[currentCall]].time  += _time;
			callRecord[callLookupTable[currentCall]].count += 1;
			
			currentCall = currentCall.slice(0, currentCall.lastIndexOf(_key));
			
			// overall entries
			totalTime += _time;
			totalCalls += 1;
		}
		
		public static function callStackToString():String
		{
			// empty return object
			var ret:String = "";
			
			// add each member of the call stack
			for (var i:int = 0; i < callStack.length; ++i)
			{
				ret = ret.concat(callStack[i] + " > ");
			}
			
			// slice that last caret off
			ret = ret.slice(0, ret.length - 3);
			
			// return
			return ret;
		}
		
		public static function addCallStack(entryName:String):void
		{
			if (enabled)
			{
				if (null == callLookupTable[entryName])
				{	
					callRecord.push(new _Entry(entryName));
					callLookupTable[entryName] = (callRecord.length - 1);
				}
			}
		}
		
		public static function add(entryName:String):void
		{
			if (enabled)
			{
				if (null == lookupTable[entryName])
				{	
					record.push(new _Entry(entryName));
					lookupTable[entryName] = (record.length - 1);
				}
			}
		}
		
		public static function dumpData():void
		{
			if (enabled)
			{
				trace("\"name\",\"calls\",\"time\",\"Avg. Time\",\"%calls\",\"%time\"");
				
				for (var i:int = 0; i < record.length; ++i)
				{
					trace("\"" + record[i].name + "\",\"" + record[i].count + "\",\"" + record[i].time + "\",\"" + record[i].time / record[i].count + "\",\"" + record[i].count / totalCalls + "\",\"" + record[i].time / totalTime + "\"");
				}
				
				trace("");
				
				trace("\"" + "Totals" + "\",\"" + totalCalls + "\",\"" + totalTime + "\",\"" + "N/A" + "\",\""+ "100" + "\",\"" + "100" + "\"");
				trace("\"Average time per call: " + totalTime / totalCalls + "\"");
				
				trace("");
				trace("");
				trace("");
				trace("");
				trace("");
				
				trace("\"name\",\"calls\",\"time\"")
				
				for (var j:int = 0; j < callRecord.length; ++j)
				{
					trace("\"" + callRecord[j].name + "\",\"" + callRecord[j].count + "\",\"" + callRecord[j].time + "\"");
				}
			}
		}
	}
}

/**
 * Internal class for a single entry in the records.
 * In another language, I'd have used a simple struct.
 */
class _Entry
{
	/**
	 * Entry's name, as given by the code.
	 */
	public var name:String;
	
	/**
	 * Entry's call count.
	*/
	public var count:uint;
	
	/**
	 * Entry's total time in execution
	 */
	public var time:uint;
	
	/*
	 * Derivable data points:
	 * 		* Average time spent on function
	 * 		* Percentage of total recorded time function occupied
	 * 		* Percentage of total calls function accounted for
	 */
	
	public function _Entry(n:String)
	{
		name  = n;
		count = 0;
		time  = 0;
	}
}