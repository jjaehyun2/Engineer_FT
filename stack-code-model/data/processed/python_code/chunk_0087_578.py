package services.command.items.management
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.items.ItemsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.items.management.DeleteSystemArticleEvent;
	import services.vo.items.HotelItemVO;
	
	import mx.collections.ArrayCollection;

	public class DeleteSystemArticleCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = DeleteSystemArticleEvent(event);
			var delegate:ItemsDelegate = new ItemsDelegate(this);
			delegate.deleteSystemArticle(_event as DeleteSystemArticleEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var provider:ArrayCollection = model.transactionModule.transactionList as ArrayCollection;
			// delete article from list
			for each(var transaction:HotelItemVO in provider)
			{
				for(var i:int = 0; i < transaction.aSubItems.length; i++)
				{
					var article:HotelItemVO = transaction.aSubItems[i] as HotelItemVO;
					if ((_event as DeleteSystemArticleEvent).articleId == article.lId)
					{
						transaction.aSubItems.splice(i, 1);
						break;
					}
				}
			}
			
			super.result(data);
		}
	}
}