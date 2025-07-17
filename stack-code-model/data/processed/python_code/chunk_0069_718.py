package services.command.frontend
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.frontend.LoginDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.frontend.LoginEvent;
	import framework.module.CommonModule;
	import services.vo.GlobalFunctions;
	import services.vo.GlobalStorage;
	import services.vo.frontend.LoggedInUserVO;
	import services.vo.frontend.UserHotelsVO;
	import services.vo.hotels.HotelInfoTotalVO;


	public class LoginCommand extends BaseCommand
	{
		private var callback:Function;
		
		override public function execute(event:CairngormEvent):void
		{
			_event = event as LoginEvent;
			var delegate:LoginDelegate = new LoginDelegate(this);
			callback = _event.callBack;
			delegate.sendLogin(_event as LoginEvent);
			
			super.execute(event);
		}
		
		override public function result(data:Object):void
		{
			var res:LoggedInUserVO = data as LoggedInUserVO;
			
			model.currentUser = res;
			
			if (!res)
			{
				return;
			}
			
			if(res.bIsFirstTimeLogin)
			{
				if(res.cLogInUser.bIsAdmin)
				{
					model.currentUser.cLogInUser.bIsAdmin = true;
					handleInitParams(true, false, false, false);
				}
				else handleInitParams(false, true, true, true);
				
				//GlobalStorage.sessionToken = res.sUserCode;
				CommonModule.userOptions.sUserCode = res.sUserCode;
				CommonModule.userOptions.sUserLocale = res.cLogInUser.sLocale;
				model.loginPage.currentPage = 1;
			}
			else
			{
				//GlobalStorage.sessionToken = res.sUserCode;
				CommonModule.userOptions.sUserCode = res.sUserCode;
				CommonModule.userOptions.sUserLocale = res.cLogInUser.sLocale;
				
				model.lCurrentTime = res.lCurrentDate*1000;
				model.currMonthIndex = GlobalFunctions.getDate().getMonth();
				model.currentUser = res;
				
				if(callback != null)
				{
					model.hotelsModule.hotels.removeAll();
					for(var i:int = 0; i < model.currentUser.cUHotels.length; i++)
					{
						var item:* = model.currentUser.cUHotels[i];
						if (item is UserHotelsVO)
						{
							model.hotelsModule.hotels.addItem((item as UserHotelsVO).oHotel);
						}
						if (item is HotelInfoTotalVO)
						{
							model.hotelsModule.hotels.addItem(item);
						}
					}
					//callback();
				}
			}
			
			GlobalStorage.checkCache();
			
			super.result(data);
		}

		private function handleInitParams(isLoginEditable:Boolean, isPositionVisible:Boolean, isPrimaryHotelVisible:Boolean,
										  isSecondaryHotelsVisible:Boolean):void
		{
			model.loginPage.firstLoginModule.isLoginEditable = isLoginEditable;
			model.loginPage.firstLoginModule.isPositionVisible = isPositionVisible;
			model.loginPage.firstLoginModule.isPrimaryHotelVisible = isPrimaryHotelVisible;
			model.loginPage.firstLoginModule.isSecondaryHotelsVisible = isSecondaryHotelsVisible;
		}
	}
}