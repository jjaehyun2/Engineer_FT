package services.command.items.management
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.items.ItemsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.items.management.SaveHotelArticleEvent;
	import services.vo.items.HotelItemVO;
	
	import mx.collections.ArrayCollection;

	public class SaveHotelArticleCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = SaveHotelArticleEvent(event);
			var delegate:ItemsDelegate = new ItemsDelegate(this);
			delegate.saveHotelArticle(_event as SaveHotelArticleEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var i:int = 0;
			var transaction:HotelItemVO;
			var article:HotelItemVO;
			var item:HotelItemVO = data as HotelItemVO;
			var provider:ArrayCollection = model.transactionModule.transactionList;
			// delete article from list
			for each(transaction in provider)
			{
				for(i = 0; i < transaction.aSubItems.length; i++)
				{
					article = transaction.aSubItems[i] as HotelItemVO;
					if (item.lId == article.lId)
					{
						transaction.aSubItems.splice(i, 1);
						break;
					}
				}
			}
			// get transaction for which article will be added
			for each(transaction in provider)
			{
				if (transaction.lId == (_event as SaveHotelArticleEvent).hotelTransactionId)
				{
					break;
				}
			}
			// 
			transaction.aSubItems.push(item);
			
			super.result(data);
		}
	}
}