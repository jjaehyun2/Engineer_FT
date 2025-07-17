package services.command.frontend
{
	import com.adobe.cairngorm.commands.ICommand;
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.frontend.AddIndividualProfileDelegate;
	import services.events.frontend.AddIndividualProfileEvent;
	import framework.model.AppModelLocator;
	
	import mx.controls.Alert;
	import mx.rpc.IResponder;

	public class AddIndividualProfileCommand implements ICommand, IResponder
	{
		private var model:AppModelLocator = AppModelLocator.getInstance();
		private var evt:AddIndividualProfileEvent;
		
		public function execute(event:CairngormEvent):void
		{
			evt = AddIndividualProfileEvent( event );
			var delegate:AddIndividualProfileDelegate = new AddIndividualProfileDelegate(this);
			
			delegate.addProfiles( evt );
		}
		
		public function result(data:Object):void
		{
			model.profilesModule.individualPageList.addItem(model.profilesModule.currentProfile);
			
			if(evt.callBack != null) evt.callBack();
			
			model.appEnabled--;
		}
		
		public function fault(info:Object):void
		{
			model.appEnabled--;
		}
		
	}
}