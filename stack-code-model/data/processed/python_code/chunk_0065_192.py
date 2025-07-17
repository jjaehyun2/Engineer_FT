package com.adobe.dashboard.event
{
	import flash.events.Event;

	import mx.collections.ArrayCollection;

	public class SaleGoalsEvent extends Event
	{
		public static const GET_GOALS_BY_DATE_RANGE:String="getGoalsByDateRange";

		/**
		 * DateRangeEnum type
		 */
		private var _dateRange:String;

		public function get dateRange():String
		{
			return _dateRange;
		}

		/**
		 * the year to fetch the goals for
		 */
		private var _year:Number;

		public function get year():Number
		{
			return _year;
		}

		/**
		 * constuctor
		 */
		public function SaleGoalsEvent(type:String, dateRange:String, year:Number)
		{
			super(type);
			_dateRange=dateRange;
			_year=year;
		}


		/**
		 * always override the clone event
		 */
		override public function clone():Event
		{
			return new SaleGoalsEvent(type, _dateRange, _year);
		}


	}
}