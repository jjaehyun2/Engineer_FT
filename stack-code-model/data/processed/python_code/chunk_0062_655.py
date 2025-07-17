package com.adobe.dashboard.model.chart
{
	import mx.collections.ArrayCollection;

	public class SalesGoalModel implements IChartOverviewDataModel
	{

		private var _dateRangeName:String;

		[Bindable]
		public function get dateRangeName():String
		{
			return _dateRangeName;
		}

		public function set dateRangeName(value:String):void
		{
			_dateRangeName=value;
		}


		private var _goalGross:Number;

		[Bindable]
		public function get goal():Number
		{
			return _goalGross;
		}

		public function set goal(value:Number):void
		{
			_goalGross=value;

			// Set a helper property
			goalProgressPercent=myGross / goal;
		}


		private var _myGross:Number;

		[Bindable]
		public function get myGross():Number
		{
			return _myGross;
		}

		public function set myGross(value:Number):void
		{
			_myGross=value;
			// Set a helper property
			goalProgressPercent=myGross / goal;
		}

		private var _myNet:Number;

		[Bindable]
		public function get myNet():Number
		{
			return _myNet;
		}

		public function set myNet(value:Number):void
		{
			_myNet=value;
		}


		private var _myCost:Number;

		[Bindable]
		public function get myCost():Number
		{
			return _myCost;
		}

		public function set myCost(value:Number):void
		{
			_myCost=value;
		}


		private var _startDate:Date;

		[Bindable]
		public function get startDate():Date
		{
			return _startDate;
		}

		public function set startDate(value:Date):void
		{
			_startDate=value;
		}


		private var _endDate:Date;

		[Bindable]
		public function get endDate():Date
		{
			return _endDate;
		}

		public function set endDate(value:Date):void
		{
			_endDate=value;
		}



		[Bindable]
		public var goalProgressPercent:Number=0;


		public function SalesGoalModel(dataRangeName:String=null, goalGross:Number=NaN, myGross:Number=NaN, startDate:Date=null, endDate:Date=null)
		{
			_dateRangeName=dataRangeName;
			_goalGross=goalGross;
			_myGross=myGross;
			_startDate=startDate;
			_endDate=endDate;
		}
	}
}