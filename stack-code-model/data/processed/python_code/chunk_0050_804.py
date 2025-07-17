package kitaec.view.offer
{
	import flash.events.Event;

	import kitaec.view.BaseView;
	import kitaec.view.offer.popup.AddOfferPopup;

	import mx.collections.ArrayList;
import mx.events.FlexEvent;

import spark.components.DataGrid;

	public class OffersViewBase extends BaseView
	{
		public var gridOffer:DataGrid;

		private var _addOfferPopup:AddOfferPopup;

		public function get addOfferPoup():AddOfferPopup
		{
			if(_addOfferPopup == null)
			{
				_addOfferPopup = new AddOfferPopup();
			}

			return _addOfferPopup;
		}

		public function OffersViewBase()
		{


		}

        override protected function onShow(event:FlexEvent):void
		{
			var list:ArrayList = new ArrayList();
			list.addItem({offerList:[], price:123, actualDate:"11.12.13"});
			list.addItem({offerList:[], price:123, actualDate:"11.12.13"});
			list.addItem({offerList:[], price:123, actualDate:"11.12.13"});
			list.addItem({offerList:[], price:123, actualDate:"11.12.13"});
			gridOffer.dataProvider = list;

		}

		protected function onAddOfferPressed(event:Event):void
		{
			addOfferPoup.show(true);
		}
	}
}