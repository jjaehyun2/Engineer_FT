package services.command.reservation
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.reservation.GetComfLetterDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.reservation.GetPdfUrlFromHtmlEvent;

	public class GetPdfUrlFromHtmlCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = GetPdfUrlFromHtmlEvent(event);
			var evt:GetPdfUrlFromHtmlEvent = GetPdfUrlFromHtmlEvent( event );
			var delegate:GetComfLetterDelegate = new GetComfLetterDelegate( this );

			delegate.getPdfUrlFromHtml(evt);
			super.execute(event);
		}

		override public function result(data:Object):void
		{
			if(data != null)
			{
				model.reservationCreateModule.confirmationLetterURL = data.toString();
			}
			super.result(data);
		}
		
	}
}