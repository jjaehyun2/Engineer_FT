package services.business.roomSettings
{
	import services.cairngorm.BaseDelegate;
	import services.events.roomSettings.AddRoomSettingEvent;
	import services.events.roomSettings.DeleteRoomSettingEvent;
	import services.events.roomSettings.EditRoomSettingEvent;
	import services.events.roomSettings.GetRoomSettingsDataEvent;
	import framework.module.CommonModule;
	import services.Services;
	import services.vo.GlobalStorage;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;

	/**
	* The CompanyRatesDelegate class is
	*
	* @author Viktor Potapov / Ramada
	*
	* @version $Revision 2.0 $ $Date: 2009-10-05 11:28:29 +0300 (Mon, 05 Oct 2009) $
	*
	*/
	public class RoomSettingsDelegate extends BaseDelegate
	{
		public function RoomSettingsDelegate(responder:IResponder)
		{
			super(responder);
		}


		public function addRoomSetting(evt:AddRoomSettingEvent):void
		{
			service.getRemoteObject(Services.SERVICE_ROOM_SETTINGS).getOperation("AddNewRoomSetting").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_ROOM_SETTINGS).getOperation("AddNewRoomSetting").send(CommonModule.userOptions, evt.roomSetting);
		}
		
		public function deleteRoomSetting(evt:DeleteRoomSettingEvent):void
		{
			service.getRemoteObject(Services.SERVICE_ROOM_SETTINGS).getOperation("DeleteRoomSetting").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_ROOM_SETTINGS).getOperation("DeleteRoomSetting").send(CommonModule.userOptions, evt.roomSetting);
		}
		
		public function editRoomSetting(evt:EditRoomSettingEvent):void
		{
			service.getRemoteObject(Services.SERVICE_ROOM_SETTINGS).getOperation("EditRoomSetting").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_ROOM_SETTINGS).getOperation("EditRoomSetting").send(CommonModule.userOptions, evt.roomSetting);
		}	
		
		public function getRoomSettingsData(evt:GetRoomSettingsDataEvent):void
		{
			service.getRemoteObject(Services.SERVICE_ROOM_SETTINGS).getOperation("GetRoomSettingsList").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_ROOM_SETTINGS).getOperation("GetRoomSettingsList").send(CommonModule.userOptions, null, evt.isMandatory); // GetRoomSettingsList($iHotelId = null,$bIsMandatory = null)
		}
	}
}