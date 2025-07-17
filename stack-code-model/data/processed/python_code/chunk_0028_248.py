package com.adobe.dashboard.model.chart
{

	public class SalesPipelineModel
	{


		private var _name:String;

		public function get name():String
		{
			return _name;
		}

		public function set name(value:String):void
		{
			_name = value;
		}


		private var _myGross:Number;

		public function get myGross():Number
		{
			return _myGross;
		}

		public function set myGross(value:Number):void
		{
			_myGross = value;
		}


		private var _averageGross:Number;

		public function get averageGross():Number
		{
			return _averageGross;
		}

		public function set averageGross(value:Number):void
		{
			_averageGross = value;
		}



		public function SalesPipelineModel()
		{
		}
	}
}