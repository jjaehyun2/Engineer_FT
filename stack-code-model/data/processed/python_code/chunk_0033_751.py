package services.command.frontend
{
	import com.adobe.cairngorm.commands.ICommand;
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.frontend.SetNewPasswordDelegate;
	import services.events.frontend.SetNewPasswordEvent;
	import framework.model.AppModelLocator;
	
	import mx.rpc.IResponder;

	public class SetNewPasswordCommand implements ICommand, IResponder
	{
		private var model:AppModelLocator = AppModelLocator.getInstance();
		
		public function execute(event:CairngormEvent):void
		{
			var evt:SetNewPasswordEvent = SetNewPasswordEvent( event );
			var delegate:SetNewPasswordDelegate = new SetNewPasswordDelegate( this );
			
			delegate.setNewPassword( evt );
			
			model.loginPage.forgotPasswordModule.confirmFormEnable = false;
			
		}
		
		public function result(data:Object):void
		{
			model.loginPage.forgotPasswordModule.currentPage = 3;			
			model.loginPage.forgotPasswordModule.confirmFormEnable = true;
			model.appEnabled --;
		}
		
		public function fault(info:Object):void
		{
			model.appEnabled --;
		}
		
	}
}