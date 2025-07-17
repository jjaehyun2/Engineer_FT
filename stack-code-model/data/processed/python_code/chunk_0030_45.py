package services.command.rates.packages
{
	import com.adobe.cairngorm.control.CairngormEvent;

	import services.business.rates.packages.PackageDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.rates.packages.GetTransactionItemPageEvent;

	import mx.collections.ArrayCollection;

	/**
	* The GetTransactionItemPageCommand class is
	*
	* @author Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-07-18 11:52:03 +0300 (Сб, 18 июл 2009) $
	*
	*/
	public class GetTransactionItemPageCommand extends BaseCommand
	{

		override public function execute(event:CairngormEvent):void
		{
			_event = event as GetTransactionItemPageEvent;
			var delegate:PackageDelegate = new PackageDelegate( this );
			delegate.getTransactionItemPage(event as GetTransactionItemPageEvent);
			super.execute(event)
		}

		override public function result(data:Object):void
		{
			model.ratesModule.barModule.hotelItemList = new ArrayCollection(data as Array);
			super.result(data);
		}

	}
}