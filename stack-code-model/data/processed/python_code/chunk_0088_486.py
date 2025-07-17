/*
 *      _________  __      __
 *    _/        / / /____ / /________ ____ ____  ___
 *   _/        / / __/ -_) __/ __/ _ `/ _ `/ _ \/ _ \
 *  _/________/  \__/\__/\__/_/  \_,_/\_, /\___/_//_/
 *                                   /___/
 * 
 * Tetragon : Game Engine for multi-platform ActionScript projects.
 * http://www.tetragonengine.com/ - Copyright (C) 2012 Sascha Balkau
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
package tetragon.util.date
{
	/**
	 * Represents an interval of time.
	 */
	public class TimeSpan
	{
		//-----------------------------------------------------------------------------------------
		// Constants
		//-----------------------------------------------------------------------------------------
		
		/**
		 * The number of milliseconds in one day
		 */
		public static const MILLISECONDS_IN_DAY:uint = 86400000;
		
		/**
		 * The number of milliseconds in one hour
		 */
		public static const MILLISECONDS_IN_HOUR:uint = 3600000;
		
		/**
		 * The number of milliseconds in one minute
		 */
		public static const MILLISECONDS_IN_MINUTE:uint = 60000;
		
		/**
		 * The number of milliseconds in one second
		 */
		public static const MILLISECONDS_IN_SECOND:uint = 1000;
		
		
		//-----------------------------------------------------------------------------------------
		// Properties
		//-----------------------------------------------------------------------------------------
		
		/** @private */
		protected var _totalMilliseconds:Number;
		
		
		//-----------------------------------------------------------------------------------------
		// Constructor
		//-----------------------------------------------------------------------------------------
		
		/**
		 * @param milliseconds
		 */
		public function TimeSpan(milliseconds:Number)
		{
			_totalMilliseconds = Math.floor(milliseconds);
		}
		
		
		//-----------------------------------------------------------------------------------------
		// Public Methods
		//-----------------------------------------------------------------------------------------
		
		/**
		 * Adds the timespan represented by this instance to the date provided and returns a new
		 * date object.
		 * 
		 * @param date The date to add the timespan to
		 * @return A new Date with the offseted time
		 */
		public function add(date:Date):Date
		{
			var ret:Date = new Date(date.time);
			ret.milliseconds += totalMilliseconds;

			return ret;
		}


		/**
		 * Creates a TimeSpan from the different between two dates.
		 * Note that start can be after end, but it will result in negative values. 
		 *  
		 * @param start The start date of the timespan
		 * @param end The end date of the timespan
		 * @return A TimeSpan that represents the difference between the dates
		 * 
		 */
		public static function fromDates(start:Date, end:Date):TimeSpan
		{
			return new TimeSpan(end.time - start.time);
		}


		/**
		 * Creates a TimeSpan from the specified number of milliseconds.
		 * 
		 * @param milliseconds The number of milliseconds in the timespan
		 * @return A TimeSpan that represents the specified value
		 */
		public static function fromMilliseconds(milliseconds:Number):TimeSpan
		{
			return new TimeSpan(milliseconds);
		}


		/**
		 * Creates a TimeSpan from the specified number of seconds.
		 * 
		 * @param seconds The number of seconds in the timespan
		 * @return A TimeSpan that represents the specified value
		 */
		public static function fromSeconds(seconds:Number):TimeSpan
		{
			return new TimeSpan(seconds * MILLISECONDS_IN_SECOND);
		}


		/**
		 * Creates a TimeSpan from the specified number of minutes.
		 * 
		 * @param minutes The number of minutes in the timespan
		 * @return A TimeSpan that represents the specified value
		 */
		public static function fromMinutes(minutes:Number):TimeSpan
		{
			return new TimeSpan(minutes * MILLISECONDS_IN_MINUTE);
		}


		/**
		 * Creates a TimeSpan from the specified number of hours.
		 * 
		 * @param hours The number of hours in the timespan
		 * @return A TimeSpan that represents the specified value
		 */
		public static function fromHours(hours:Number):TimeSpan
		{
			return new TimeSpan(hours * MILLISECONDS_IN_HOUR);
		}


		/**
		 * Creates a TimeSpan from the specified number of days.
		 * 
		 * @param days The number of days in the timespan
		 * @return A TimeSpan that represents the specified value
		 */
		public static function fromDays(days:Number):TimeSpan
		{
			return new TimeSpan(days * MILLISECONDS_IN_DAY);
		}
		
		
		//-----------------------------------------------------------------------------------------
		// Accessors
		//-----------------------------------------------------------------------------------------
		
		/**
		 * Gets the number of whole days
		 * 
		 * @example In a TimeSpan created from TimeSpan.fromHours(25), 
		 *          totalHours will be 1.04, but hours will be 1 
		 * @return A number representing the number of whole days in the TimeSpan
		 */
		public function get days():int
		{
			return int(_totalMilliseconds / MILLISECONDS_IN_DAY);
		}
		
		
		/**
		 * Gets the number of whole hours (excluding entire days)
		 * 
		 * @example In a TimeSpan created from TimeSpan.fromMinutes(1500), 
		 *          totalHours will be 25, but hours will be 1 
		 * @return A number representing the number of whole hours in the TimeSpan
		 */
		public function get hours():int
		{
			return int(_totalMilliseconds / MILLISECONDS_IN_HOUR) % 24;
		}
		
		
		/**
		 * Gets the number of whole minutes (excluding entire hours)
		 * 
		 * @example In a TimeSpan created from TimeSpan.fromMilliseconds(65500), 
		 *          totalSeconds will be 65.5, but seconds will be 5 
		 * @return A number representing the number of whole minutes in the TimeSpan
		 */
		public function get minutes():int
		{
			return int(_totalMilliseconds / MILLISECONDS_IN_MINUTE) % 60;
		}
		
		
		/**
		 * Gets the number of whole seconds (excluding entire minutes)
		 * 
		 * @example In a TimeSpan created from TimeSpan.fromMilliseconds(65500), 
		 *          totalSeconds will be 65.5, but seconds will be 5 
		 * @return A number representing the number of whole seconds in the TimeSpan
		 */
		public function get seconds():int
		{
			return int(_totalMilliseconds / MILLISECONDS_IN_SECOND) % 60;
		}
		
		
		/**
		 * Gets the number of whole milliseconds (excluding entire seconds)
		 * 
		 * @example In a TimeSpan created from TimeSpan.fromMilliseconds(2123), 
		 *          totalMilliseconds will be 2001, but milliseconds will be 123 
		 * @return A number representing the number of whole milliseconds in the TimeSpan
		 */
		public function get milliseconds():int
		{
			return int(_totalMilliseconds) % 1000;
		}
		
		
		/**
		 * Gets the total number of days.
		 * 
		 * @example In a TimeSpan created from TimeSpan.fromHours(25), 
		 *          totalHours will be 1.04, but hours will be 1 
		 * @return A number representing the total number of days in the TimeSpan
		 */
		public function get totalDays():Number
		{
			return _totalMilliseconds / MILLISECONDS_IN_DAY;
		}
		
		
		/**
		 * Gets the total number of hours.
		 * 
		 * @example In a TimeSpan created from TimeSpan.fromMinutes(1500), 
		 *          totalHours will be 25, but hours will be 1 
		 * @return A number representing the total number of hours in the TimeSpan
		 */
		public function get totalHours():Number
		{
			return _totalMilliseconds / MILLISECONDS_IN_HOUR;
		}
		
		
		/**
		 * Gets the total number of minutes.
		 * 
		 * @example In a TimeSpan created from TimeSpan.fromMilliseconds(65500), 
		 *          totalSeconds will be 65.5, but seconds will be 5 
		 * @return A number representing the total number of minutes in the TimeSpan
		 */
		public function get totalMinutes():Number
		{
			return _totalMilliseconds / MILLISECONDS_IN_MINUTE;
		}
		
		
		/**
		 * Gets the total number of seconds.
		 * 
		 * @example In a TimeSpan created from TimeSpan.fromMilliseconds(65500), 
		 *          totalSeconds will be 65.5, but seconds will be 5 
		 * @return A number representing the total number of seconds in the TimeSpan
		 */
		public function get totalSeconds():Number
		{
			return _totalMilliseconds / MILLISECONDS_IN_SECOND;
		}
		
		
		/**
		 * Gets the total number of milliseconds.
		 * 
		 * @example In a TimeSpan created from TimeSpan.fromMilliseconds(2123), 
		 *          totalMilliseconds will be 2001, but milliseconds will be 123 
		 * @return A number representing the total number of milliseconds in the TimeSpan
		 */
		public function get totalMilliseconds():Number
		{
			return _totalMilliseconds;
		}
	}
}