package services.command.backend
{
	import com.adobe.cairngorm.commands.ICommand;
	import com.adobe.cairngorm.control.CairngormEvent;
	import com.adobe.cairngorm.control.CairngormEventDispatcher;
	
	import services.business.backend.LoginInHotelDelegate;
	import services.business.common.CommonDelegate;
	import services.events.backend.LoginInHotelEvent;
	import services.events.common.GetSystemDateEvent;
	import framework.model.AppModelLocator;
	import services.vo.frontend.RoleVO;
	
	import mx.controls.Alert;
	import mx.rpc.IResponder;

	/**
	* The LoginInHotelCommand class is 
	*
	* @author Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-07-18 11:52:03 +0300 (Сб, 18 июл 2009) $
	*
	*/
	public class LoginInHotelCommand implements ICommand, IResponder
	{
		private var model:AppModelLocator = AppModelLocator.getInstance();
		private var callBack:Function;
		
		public function execute(event:CairngormEvent):void
		{
			var delegate:LoginInHotelDelegate = new LoginInHotelDelegate( this );	
			this.callBack = (event as LoginInHotelEvent).callBack;		
			delegate.loginInHotel(event as LoginInHotelEvent);
		}
		
		public function result(data:Object):void
		{
			model.currentUser.oRole = data as RoleVO;			
			model.appEnabled--;
			
			var evt:GetSystemDateEvent = new GetSystemDateEvent(CommonDelegate.GET_SYSTEM_DATE);
			CairngormEventDispatcher.getInstance().dispatchEvent( evt );
								
			if(callBack != null)
			{
				callBack();
			}
		}
		
		public function fault(info:Object):void
		{			
			Alert.show("Error");			 
			model.appEnabled--;
		}
		
	}
}