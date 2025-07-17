package com.adobe.mobiledashboard.view.renderer
{
	import com.adobe.dashboard.model.chart.ChartSaleModel;

	import flash.display.CapsStyle;
	import flash.display.GradientType;
	import flash.geom.Matrix;
	import flash.globalization.LocaleID;

	import mx.core.IDataRenderer;
	import mx.core.mx_internal;
	import mx.styles.CSSStyleDeclaration;

	import spark.components.LabelItemRenderer;
	import spark.components.supportClasses.StyleableTextField;
	import spark.formatters.CurrencyFormatter;

	use namespace mx_internal;


	/**
	 * Styles for StyleableTextFields
	 */
	[Style(name="titleStyleName", type="String", inherit="no")]
	[Style(name="statusStyleName", type="String", inherit="no")]
	[Style(name="totalStyleName", type="String", inherit="no")]
	[Style(name="dateStyleName", type="String", inherit="no")]


	public class SaleRenderer extends LabelItemRenderer implements IDataRenderer
	{


		//
		// Constants
		//


		public static const V_PADDING:int=16;

		public static const H_PADDING:int=10;

		public static const V_GAP:int=4;

		public static const H_GAP:int=30;


		//
		// Variables
		//

		private var titleStyles:CSSStyleDeclaration;

		private var statusStyles:CSSStyleDeclaration;

		private var totalStyles:CSSStyleDeclaration;

		private var dateStyles:CSSStyleDeclaration;

		private var currencyFormatter:CurrencyFormatter;



		//
		// Properties
		//


		protected var chartSaleModel:ChartSaleModel;



		//
		// UI Bits
		//

		protected var dateDisplay:StyleableTextField;

		protected var titleDisplay:StyleableTextField;

		protected var statusDisplay:StyleableTextField;

		protected var totalDisplay:StyleableTextField;




		/**
		 * Constuctor
		 */
		public function SaleRenderer()
		{
			super();

			currencyFormatter=new CurrencyFormatter();
			currencyFormatter.setStyle("locale", LocaleID.DEFAULT);
			currencyFormatter.useCurrencySymbol=true;
			currencyFormatter.trailingZeros=true;
		}

		/**
		 * Required by IDataRenderer
		 */
		override public function set data(value:Object):void
		{
			super.data=value;

			if (value is ChartSaleModel)
			{
				chartSaleModel=ChartSaleModel(value);
			}
		}


		//
		//  Overridden methods: UIComponent
		//

		/**
		 *  @private
		 */
		override protected function createChildren():void
		{
			//super.createChildren();
			setStyle("selectionColor", "0xCCEEFF");
			setStyle("rollOverColor", "0xCCEEFF");

			if (!titleDisplay)
			{

				titleDisplay=StyleableTextField(createInFontContext(StyleableTextField));
				titleDisplay.styleName=this;
				if (getStyle("titleStyleName"))
				{
					titleDisplay.styleDeclaration=styleManager.getMergedStyleDeclaration("." + getStyle("titleStyleName"));
				}
				titleDisplay.commitStyles();
				titleDisplay.editable=false;
				titleDisplay.selectable=false;
				titleDisplay.multiline=false;
				titleDisplay.wordWrap=false;
				titleDisplay.width=unscaledWidth / 2;
				titleDisplay.height=Math.min(titleDisplay.textHeight + 4, 60);
				addChild(titleDisplay);
			}

			if (!statusDisplay)
			{
				statusDisplay=StyleableTextField(createInFontContext(StyleableTextField));
				statusDisplay.styleName=this;
				if (getStyle("statusStyleName"))
				{
					statusDisplay.styleDeclaration=styleManager.getMergedStyleDeclaration("." + getStyle("statusStyleName"));
				}
				statusDisplay.commitStyles();
				statusDisplay.editable=false;
				statusDisplay.selectable=false;
				statusDisplay.multiline=false;
				statusDisplay.wordWrap=false;
				statusDisplay.width=unscaledWidth / 2;
				statusDisplay.height=Math.min(statusDisplay.textHeight + 4, 60);
				addChild(statusDisplay);
			}

			if (!totalDisplay)
			{
				totalDisplay=StyleableTextField(createInFontContext(StyleableTextField));
				totalDisplay.styleName=this;
				if (getStyle("totalStyleName"))
				{
					totalDisplay.styleDeclaration=styleManager.getMergedStyleDeclaration("." + getStyle("totalStyleName"));
				}
				totalDisplay.commitStyles();
				totalDisplay.editable=false;
				totalDisplay.selectable=false;
				totalDisplay.multiline=false;
				totalDisplay.wordWrap=false;
				totalDisplay.width=unscaledWidth / 2;
				totalDisplay.height=Math.min(totalDisplay.textHeight + 4, 60);
				addChild(totalDisplay);
			}

			if (!dateDisplay)
			{
				dateDisplay=StyleableTextField(createInFontContext(StyleableTextField));
				dateDisplay.styleName=this;
				if (getStyle("dateStyleName"))
				{
					dateDisplay.styleDeclaration=styleManager.getMergedStyleDeclaration("." + getStyle("dateStyleName"));
				}
				dateDisplay.commitStyles();
				dateDisplay.editable=false;
				dateDisplay.selectable=false;
				dateDisplay.multiline=false;
				dateDisplay.wordWrap=false;
				dateDisplay.width=unscaledWidth / 2;
				dateDisplay.height=Math.min(dateDisplay.textHeight + 4, 60);
				addChild(dateDisplay);
			}


		}


		override protected function measure():void
		{
			measuredHeight=80;

			measuredWidth=400;

			// Minimums
			measuredMinWidth=80;
			measuredMinHeight=measuredHeight;
		}

		override protected function drawBackground(unscaledWidth:Number, unscaledHeight:Number):void
		{

			graphics.beginFill(0x232323);
			graphics.drawRect(0, 0, unscaledWidth, unscaledHeight);
			graphics.endFill();

			// Header box
			graphics.beginFill(0x000000);
			graphics.drawRect(0, 0, unscaledWidth, 44);
			graphics.endFill();

			// Draw our own color divider
			graphics.lineStyle(1, 0x0C0C0C, 1, false, "normal", CapsStyle.NONE);
			graphics.moveTo(0, 44);
			graphics.lineTo(unscaledWidth, 44);
		}

		override protected function layoutContents(unscaledWidth:Number, unscaledHeight:Number):void
		{
			super.layoutContents(unscaledWidth, unscaledHeight);

			// Hide the default label display
			if (labelDisplay)
			{
				labelDisplay.visible=false;
			}

			if (dateDisplay)
			{
				dateDisplay.text=chartSaleModel.date.toDateString();
				setElementPosition(dateDisplay, H_PADDING, V_PADDING);
				setElementSize(dateDisplay, dateDisplay.textWidth + 4, dateDisplay.textHeight + 4);
			}

			if (titleDisplay)
			{
				titleDisplay.text=chartSaleModel.clientName;
				setElementPosition(titleDisplay, H_PADDING, 10 + dateDisplay.y + dateDisplay.height + V_GAP);
				setElementSize(titleDisplay, unscaledWidth - (H_PADDING * 2), titleDisplay.textHeight + 4);
			}

			if (statusDisplay)
			{
				statusDisplay.text="Closed sale";
				setElementPosition(statusDisplay, H_PADDING, titleDisplay.y + titleDisplay.height + V_GAP);
				setElementSize(statusDisplay, titleDisplay.width, statusDisplay.textHeight + 4);
			}

			if (totalDisplay)
			{
				totalDisplay.text=currencyFormatter.format(chartSaleModel.myGross);
				setElementPosition(totalDisplay, unscaledWidth - 140, statusDisplay.y);
				setElementSize(totalDisplay, 120, totalDisplay.textHeight + 4);
			}

		}

	}
}