import view.Vnet_HelpInfomationWindow;
import view.Vnet_manageScriptWindow;
import view.Vnet_manageSubnetWindow;

	protected function listshowHandler(mode:int):void{
		switch(mode){
			case 1: 
				var myPanel1:ControllerListTitleWindow = 
				ControllerListTitleWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, ControllerListTitleWindow, false));
				myPanel1.x = 100;
				myPanel1.y = 150;	
				break;
			case 2: 
				var myPanel2:SwitchListTitleWindow = 
				SwitchListTitleWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, SwitchListTitleWindow, false));
				myPanel2.x = 100;
				myPanel2.y = 150;
				break;
			case 3: 
				var myPanel3:PortListTitleWindow = 
				PortListTitleWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, PortListTitleWindow, false));
				myPanel3.x = 100;
				myPanel3.y = 150;	
				break;
			case 4:
				var myPanel4:LinkListTitleWindow = 
				LinkListTitleWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, LinkListTitleWindow, false));
				myPanel4.x = 100;
				myPanel4.y = 150;	
				break;
			case 5:
				break;
			case 6: 
				var myPanel6:HostListTitleWindow = 
				HostListTitleWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, HostListTitleWindow, false));
				myPanel6.x = 100;
				myPanel6.y = 150;	
				break;
			case 7:
				var myPanel17:addControllerWindow = 
				addControllerWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, addControllerWindow, false)); 
				myPanel17.x = 420;
				myPanel17.y = 170;
				break;
			case 8:
				var myPanel18:deleteControllerWindow=
				deleteControllerWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, deleteControllerWindow, false)); 
				myPanel18.x = 420;
				myPanel18.y = 170;
				break;
			case 9:
				var myPanel19:Vnet_instanceListWindow = 
				Vnet_instanceListWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, Vnet_instanceListWindow, false));
				myPanel19.x = 100;
				myPanel19.y = 150;
				break;

			case 10:
				var myPanel20:Vnet_imageListWindow = 
				Vnet_imageListWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, Vnet_imageListWindow, false));
				myPanel20.x = 100;
				myPanel20.y = 150;
				break;

			case 11:
				var myPanel21:Vnet_flavorListWindow = 
				Vnet_flavorListWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, Vnet_flavorListWindow, false));
				myPanel21.x = 100;
				myPanel21.y = 150;
				break;
			
			case 12:
				var myPanel22:Vnet_manageSubnetWindow = 
				Vnet_manageSubnetWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, Vnet_manageSubnetWindow, false));
				myPanel22.x = 300;
				myPanel22.y = 100;
				break;
			
			case 13:
				var myPanel23:Vnet_manageScriptWindow = 
				Vnet_manageScriptWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, Vnet_manageScriptWindow, false));
				myPanel23.x = 300;
				myPanel23.y = 100;
				break;
			
			case 14:
				var myPanel24:Vnet_HelpInfomationWindow = 
				Vnet_HelpInfomationWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, Vnet_HelpInfomationWindow, true));
				myPanel23.x = 300;
				myPanel23.y = 100;
				break;
		}
	
		
	}