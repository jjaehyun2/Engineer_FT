package com.adobe.dashboard.model.chart
{

	public class TotalSalesByYearModel
	{

		private var _companyGross:Number;

		[Bindable]
		public function get companyGross():Number
		{
			return _companyGross;
		}

		public function set companyGross(value:Number):void
		{
			_companyGross = value;
		}


		private var _myGross:Number;

		[Bindable]
		public function get myGross():Number
		{
			return _myGross;
		}

		public function set myGross(value:Number):void
		{
			_myGross = value;
		}


		private var _growthOverLastYear:Number;

		[Bindable]
		public function get growthOverLastYear():Number
		{
			return _growthOverLastYear;
		}

		public function set growthOverLastYear(value:Number):void
		{
			_growthOverLastYear = value;
		}

		private var _myGrowthOverLastYear:Number;

		[Bindable]
		public function get myGrowthOverLastYear():Number
		{
			return _myGrowthOverLastYear;
		}

		public function set myGrowthOverLastYear(value:Number):void
		{
			_myGrowthOverLastYear = value;
		}


		private var _year:int;

		[Bindable]
		public function get year():int
		{
			return _year;
		}

		public function set year(value:int):void
		{
			_year = value;
		}


		private var _seller:String;

		[Bindable]
		public function get seller():String
		{
			return _seller;
		}

		public function set seller(value:String):void
		{
			_seller = value;
		}

		private var _previousYearCompanyGross:Number;

		public function get previousYearCompanyGross():Number
		{
			return _previousYearCompanyGross;
		}

		public function set previousYearCompanyGross(value:Number):void
		{
			_previousYearCompanyGross = value;
		}


		private var _previousYearMyGross:Number;

		public function get previousYearMyGross():Number
		{
			return _previousYearMyGross;
		}

		public function set previousYearMyGross(value:Number):void
		{
			_previousYearMyGross = value;
		}


		public function TotalSalesByYearModel()
		{
		}
	}
}