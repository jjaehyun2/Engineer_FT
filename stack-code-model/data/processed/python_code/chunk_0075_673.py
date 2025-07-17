package services.command.security
{
	import com.adobe.cairngorm.commands.ICommand;
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.security.SecurityDelegate;
	import framework.model.AppModelLocator;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Alert;
	import mx.rpc.IResponder;

	public class GetUserListCommand implements ICommand, IResponder
	{
		private var model:AppModelLocator = AppModelLocator.getInstance();
		
		public function execute(event:CairngormEvent):void
		{
			var delegate:SecurityDelegate = new SecurityDelegate( this );			 
			delegate.getUserList();
		}
		
 		public function result(data:Object):void
		{
			model.securityModule.userList = new ArrayCollection(data as Array);
			model.appEnabled--;
		}
		
		public function fault(info:Object):void
		{
			Alert.show("Error");			
			model.appEnabled--;
		}
		
	}
}