package com.adobe.dashboard.model.chart
{

	public class RevenuePerSaleModel
	{


		/**
		 * Either "profit" or "cost"
		 */
		private var _label:String;

		[Bindable]
		public function get label():String
		{
			return _label;
		}

		public function set label(value:String):void
		{
			_label=value;
		}


		/**
		 * Currancy amount (either profict, or cost)
		 */
		private var _value:Number;

		[Bindable]
		public function get value():Number
		{
			return _value;
		}

		public function set value(value:Number):void
		{
			_value=value;
		}


		private var _clientName:String;

		[Bindable]
		public function get clientName():String
		{
			return _clientName;
		}

		public function set clientName(value:String):void
		{
			_clientName=value;
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

		public function RevenuePerSaleModel()
		{
		}

	}
}