package com.adobe.dashboard.presenter
{
	import com.adobe.dashboard.enum.*;
	import com.adobe.dashboard.event.*;
	import com.adobe.dashboard.model.ChartModel;
	import com.adobe.dashboard.util.DateTimeUtil;

	import flash.events.EventDispatcher;
	import flash.events.IEventDispatcher;

	import mx.collections.ArrayCollection;

	public class SalesGoalsPresenter extends EventDispatcher
	{

		private var dispatcher:IEventDispatcher;

		private var lastDateRange:String;

		[Bindable]
		public var currentState:String;

		[Bindable]
		public var isAreaChart:Boolean=true;

		[Bindable]
		public var dateRange:String;

		[Bindable]
		public var dateRangeStartDate:Date=new Date();

		[Bindable]
		public var sliderStartDate:Date=new Date();

		[Bindable]
		public var sliderEndDate:Date=new Date();

		[Bindable]
		public var selectionStartDate:Date=new Date();

		[Bindable]
		public var selectionEndDate:Date=new Date();

		[Bindable]
		public var chartDetailsPresenter:ChartPresenter;

		[Bindable]
		public var chartListDetailsPresenter:ChartPresenter;

		[Bindable]
		public var monthChartOverviewPresenter:ChartOverviewPresenter;

		[Bindable]
		public var quarterChartOverviewPresenter:ChartOverviewPresenter;

		[Bindable]
		public var yearChartOverviewPresenter:ChartOverviewPresenter;

		[Bindable]
		public var dateRangeSelectorList:ArrayCollection;

		[Bindable]
		public var showTourTip:Boolean=true;

		[Bindable]
		public var skipAnimation:Boolean=false;

		public function SalesGoalsPresenter(dispatcher:IEventDispatcher)
		{
			this.dispatcher=dispatcher;

			buildPresenters();
		}

		//
		// Build presenters
		//

		private function buildPresenters():void
		{
			monthChartOverviewPresenter=new ChartOverviewPresenter(dispatcher);
			quarterChartOverviewPresenter=new ChartOverviewPresenter(dispatcher);
			yearChartOverviewPresenter=new ChartOverviewPresenter(dispatcher);

			chartDetailsPresenter=new ChartPresenter(dispatcher);
			chartListDetailsPresenter=new ChartPresenter(dispatcher);
		}


		//
		// Public methods
		//

		public function goDetails():void
		{
			// Navigate to the new page
			var navEvent:NavigationEvent=new NavigationEvent(NavigationEvent.GO_STATE_EVENT, StateEnum.SALES_GOALS_DETAILS_STATE);
			dispatcher.dispatchEvent(navEvent);
		}


		/**
		 * COMPARISON_MY_VS_GOAL_GROSS_MONTH_REPORT
		 */
		public function getSalesGoalsMonthChartData(firstDateInRange:Date, lastDateInRange:Date, getOverview:Boolean=false):void
		{
			if (getOverview)
			{
				// Send along a IChartOverviewDataModel object to be filled with data
				var chartOverviewEvent:ChartOverviewEvent=new ChartOverviewEvent(monthChartOverviewPresenter, ReportTypeEnum.COMPARISON_MY_VS_GOAL_GROSS_MONTH_REPORT);
				dispatcher.dispatchEvent(chartOverviewEvent);
			}
			else
			{
				// Populate chartModel
				chartDetailsPresenter.chartModel=new ChartModel(-1, null, isAreaChart ? ChartTypeEnum.AREA_CHART : ChartTypeEnum.LINE_CHART);

				// Send along a ChartPresenter to be filled with data
				var firstDayOfMonth:Date=DateTimeUtil.getFirstDayOfMonth(firstDateInRange);
				var lastDayOfMonth:Date=DateTimeUtil.getLastDayOfMonth(lastDateInRange);
				var chartDataEvent:ChartDataEvent=new ChartDataEvent(chartDetailsPresenter, ReportTypeEnum.COMPARISON_MY_VS_GOAL_GROSS_MONTH_REPORT, firstDayOfMonth, lastDayOfMonth);
				dispatcher.dispatchEvent(chartDataEvent);
			}
		}

		/**
		 * COMPARISON_MY_VS_GOAL_GROSS_QUARTER_REPORT
		 */
		public function getSalesGoalsQuarterChartData(date:Date, getOverview:Boolean=false):void
		{
			if (getOverview)
			{
				// Send along a IChartOverviewDataModel object to be filled with data
				var chartOverviewEvent:ChartOverviewEvent=new ChartOverviewEvent(quarterChartOverviewPresenter, ReportTypeEnum.COMPARISON_MY_VS_GOAL_GROSS_QUARTER_REPORT);
				dispatcher.dispatchEvent(chartOverviewEvent);
			}
			else
			{
				// Populate chartModel
				chartDetailsPresenter.chartModel=new ChartModel(-1, null, isAreaChart ? ChartTypeEnum.AREA_CHART : ChartTypeEnum.LINE_CHART);

				// Send along a ChartPresenter to be filled with data
				var firstDayOfQuarter:Date=DateTimeUtil.getFirstDateOfQuarter(date);
				var lastDayOfQuarter:Date=DateTimeUtil.getLastDateOfQuarter(date);
				var chartDataEvent:ChartDataEvent=new ChartDataEvent(chartDetailsPresenter, ReportTypeEnum.COMPARISON_MY_VS_GOAL_GROSS_QUARTER_REPORT, firstDayOfQuarter, lastDayOfQuarter);
				dispatcher.dispatchEvent(chartDataEvent);
			}
		}

		/**
		 * COMPARISON_MY_VS_GOAL_GROSS_YEAR_REPORT
		 */
		public function getSalesGoalsYearChartData(date:Date, getOverview:Boolean=false):void
		{
			// Set the date range

			if (getOverview)
			{
				// Send along a IChartOverviewDataModel object to be filled with data
				var chartOverviewEvent:ChartOverviewEvent=new ChartOverviewEvent(yearChartOverviewPresenter, ReportTypeEnum.COMPARISON_MY_VS_GOAL_GROSS_YEAR_REPORT);
				dispatcher.dispatchEvent(chartOverviewEvent);
			}
			else
			{
				// Populate chartModel
				chartDetailsPresenter.chartModel=new ChartModel(-1, null, isAreaChart ? ChartTypeEnum.AREA_CHART : ChartTypeEnum.LINE_CHART);

				// Send along a ChartPresenter to be filled with data
				var firstDayOfYear:Date=new Date(date.fullYear, 0, 1);
				var lastDayOfYear:Date=new Date(date.fullYear, 0, 365);
				var chartDataEvent:ChartDataEvent=new ChartDataEvent(chartDetailsPresenter, ReportTypeEnum.COMPARISON_MY_VS_GOAL_GROSS_YEAR_REPORT, firstDayOfYear, lastDayOfYear);
				dispatcher.dispatchEvent(chartDataEvent);
			}

		}

		/**
		 * COMPARISON_MY_VS_GOAL_GROSS_REPORT
		 */

		/**
		 * MY_GROSS_REPORT
		 */
		public function getSalesGoalDetails(firstDateInRange:Date, lastDateInRange:Date):void
		{
			var firstDate:Date;
			var lastDate:Date;

			// Clear out old data if any
			chartDetailsPresenter.dataProvider=null;

			switch (dateRange)
			{
				case DateRangeEnum.MONTH:
				{
					firstDate=DateTimeUtil.getFirstDayOfMonth(firstDateInRange);
					lastDate=DateTimeUtil.getLastDayOfMonth(lastDateInRange);
					break;
				}
				case DateRangeEnum.QUARTER:
				{
					firstDate=DateTimeUtil.getFirstDateOfQuarter(firstDateInRange);
					lastDate=DateTimeUtil.getLastDateOfQuarter(lastDateInRange);
					break;
				}
				case DateRangeEnum.YEAR:
				{
					firstDate=new Date(firstDateInRange.fullYear, 0, 1);
					lastDate=new Date(lastDateInRange.fullYear, 0, 365);
					break;
				}
				default:
				{
					// do nothing
					break;
				}

			}

			// Get the data
			var chartDataEvent:ChartDataEvent=new ChartDataEvent(chartListDetailsPresenter, ReportTypeEnum.MY_GROSS_REPORT, firstDate, lastDate);

			dispatcher.dispatchEvent(chartDataEvent);
		}

		//
		public function getDateRangeSelectorList(dateRange:String, year:int):void
		{
			dateRangeSelectorList=new ArrayCollection();
			var evt:SaleGoalsEvent=new SaleGoalsEvent(SaleGoalsEvent.GET_GOALS_BY_DATE_RANGE, dateRange, year);
			dispatcher.dispatchEvent(evt);
		}

		/**
		  *
		  */
		public function loadChartData(dateRange:String, firstDateInRange:Date, lastDateInRange:Date):void
		{
			switch (dateRange)
			{
				case DateRangeEnum.MONTH:
				{
					getSalesGoalsMonthChartData(firstDateInRange, lastDateInRange);
					if (dateRange != lastDateRange)
					{
						getDateRangeSelectorList(dateRange, new Date().fullYear);
					}
					break;
				}
				case DateRangeEnum.QUARTER:
				{
					getSalesGoalsQuarterChartData(firstDateInRange);
					if (dateRange != lastDateRange)
					{
						getDateRangeSelectorList(dateRange, new Date().fullYear);
					}
					break;
				}
				case DateRangeEnum.YEAR:
				{
					getSalesGoalsYearChartData(firstDateInRange);
					break;
				}

				default:
				{
					break;
				}
			}

			lastDateRange=dateRange;


		}

		public function hideAllTourTips():void
		{
			dispatcher.dispatchEvent(new TourTipEvent(TourTipEvent.HIDE_ALL_TOUR_TIPS));
		}

		public function hideTourTip():void
		{
			var event:TourTipEvent=new TourTipEvent(TourTipEvent.HIDE_TOUR_TIP, TourTipTypeEnum.SALES_GOAL);
			dispatcher.dispatchEvent(event);
		}

	}
}